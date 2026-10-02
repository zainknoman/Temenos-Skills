import shutil
import subprocess
import zipfile

import pytest

from component_parse import component_name, parse_static_ints, split_constant

JAVA_SRC = """
public class component_ST_Demo_16_cl {
    public static int _Customer_EbCusMnemonic;
    public static int _Customer_EbCusSector;
    public static int _Customer_Big;
    public static int _Customer_Huge;
    public static int _Customer_Neg;
    public static String _notAnInt = "x";
    static {
        _Customer_EbCusMnemonic = 1;
        int k = Integer.getInteger("k", 2);
        switch (k) { case 1: k = 10; break; case 2: k = 20; break; case 3: k = 30; break; default: k = 0; }
        _Customer_EbCusSector = 23;
        _Customer_Big = 300;
        _Customer_Huge = 70000;
        _Customer_Neg = -1;
    }
}
"""


@pytest.fixture(scope="module")
def demo_class(tmp_path_factory):
    javac = shutil.which("javac")
    if not javac:
        pytest.skip("javac not available")
    d = tmp_path_factory.mktemp("cls")
    (d / "component_ST_Demo_16_cl.java").write_text(JAVA_SRC)
    subprocess.run([javac, "-d", str(d), str(d / "component_ST_Demo_16_cl.java")], check=True)
    return (d / "component_ST_Demo_16_cl.class").read_bytes()


def test_parse_static_int_assignments_across_a_switch(demo_class):
    values = parse_static_ints(demo_class)
    assert values["_Customer_EbCusMnemonic"] == 1
    assert values["_Customer_EbCusSector"] == 23   # assigned after a tableswitch
    assert values["_Customer_Big"] == 300          # sipush
    assert values["_Customer_Huge"] == 70000       # ldc Integer
    assert values["_Customer_Neg"] == -1           # iconst_m1
    assert "_notAnInt" not in values


def test_component_name_from_class_path():
    assert component_name("com/temenos/t24/component_ST_Customer_16_cl.class") == "ST.Customer"
    assert component_name("com/temenos/t24/component_AC_AccountOpening_21_cl.class") == "AC.AccountOpening"
    assert component_name("com/temenos/t24/CUSTOMER_FIELDS_cl.class") is None


def test_split_constant():
    assert split_constant("_Customer_EbCusMnemonic") == ("Customer", "EbCusMnemonic")
    assert split_constant("_partypurgeCustomercustomerPurged_sectorId") == ("partypurgeCustomercustomerPurged", "sectorId")
    assert split_constant("_NoField") is None


def test_build_joins_component_constants_to_fields_by_position(db, demo_class, tmp_path):
    from component_parse import build_component_fields
    jars = tmp_path / "jars"
    jars.mkdir()
    with zipfile.ZipFile(jars / "ST_Demo.jar", "w") as z:
        z.writestr("com/temenos/t24/component_ST_Demo_16_cl.class", demo_class)
    stats = build_component_fields(db, jars, release="R23")
    rows = db.execute("SELECT release, app, component, record, comp_field, position, field_name "
                      "FROM component_fields ORDER BY position").fetchall()
    # _Customer_EbCusMnemonic=1 joins CUSTOMER pos 1; _Customer_EbCusSector=23 has no row at pos 23
    assert rows == [("R23", "CUSTOMER", "ST.Demo", "Customer", "EbCusMnemonic", 1, "EB.CUS.MNEMONIC")]
    assert stats["joined"] == 1 and stats["unjoined"] >= 1


def test_rebuild_replaces_only_the_same_release(db, demo_class, tmp_path):
    from component_parse import build_component_fields
    jars = tmp_path / "jars"
    jars.mkdir()
    with zipfile.ZipFile(jars / "ST_Demo.jar", "w") as z:
        z.writestr("com/temenos/t24/component_ST_Demo_16_cl.class", demo_class)
    build_component_fields(db, jars, release="R23")
    build_component_fields(db, jars, release="R23")
    build_component_fields(db, jars, release="R99")
    counts = dict(db.execute("SELECT release, COUNT(*) FROM component_fields GROUP BY release"))
    assert counts == {"R23": 1, "R99": 1}


def test_name_match_requires_the_component_name_to_spell_the_equ_name():
    from component_parse import names_match
    assert names_match("EbCusMnemonic", "EB.CUS.MNEMONIC", "EB.CUS.")
    assert names_match("Category", "AC.CATEGORY", "AC.")                 # prefix dropped
    assert names_match("EbCusNameOne", "EB.CUS.NAME.1", "EB.CUS.")       # number word
    assert names_match("AccountTitle1", "AC.ACCOUNT.TITLE.1", "AC.")     # digit
    assert names_match("TfLcExpiryDate", "TF.LC.EXPIRY.DATE", "TF.LC.")
    # same record name + same position, but another component's own table:
    assert not names_match("CusActivity", "EB.CUS.MNEMONIC", "EB.CUS.")
    assert not names_match("CuCustomerType", "EB.CUS.MNEMONIC", "EB.CUS.")
    assert not names_match("AcAction", "AC.CATEGORY", "AC.")
