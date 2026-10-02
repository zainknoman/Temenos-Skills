import pytest

from artefact_fields import UnknownApp, app_prefix, check_fields, extract_refs, record_class


def test_prefix_is_common_dotted_prefix(db):
    assert app_prefix(db, "ACCOUNT") == "AC."
    assert app_prefix(db, "CUSTOMER") == "EB.CUS."


def test_unknown_app_is_an_error_not_a_pass(db):
    with pytest.raises(UnknownApp):
        app_prefix(db, "ACCOUT")


def test_record_class():
    assert record_class("ACCOUNT") == "Account"
    assert record_class("FUNDS.TRANSFER") == "FundsTransfer"


def test_legacy_refs():
    src = "lvCat = R.NEW(AC.CATEGORY)\nlvT = R.NEW(AC.ACCOUNT.TITLE.1)\n"
    refs = extract_refs(src, "AC.", "Account")
    assert refs.legacy == {"AC.CATEGORY", "AC.ACCOUNT.TITLE.1"}


def test_componentised_refs_skip_method_calls():
    src = (
        "x = EB.SystemTables.getRNew(AC.AccountOpening.Account.Category)\n"
        "r = AC.AccountOpening.Account.Read(id, err)\n"
    )
    refs = extract_refs(src, "AC.", "Account")
    assert refs.componentised == {"AC.AccountOpening.Account.Category"}


def test_comments_are_ignored():
    src = "* uses AC.NOT.A.FIELD in a comment\nRETURN\n"
    assert extract_refs(src, "AC.", "Account").legacy == set()


def test_check_reports_missing(db):
    src = "a = R.NEW(AC.CATEGORY)\nb = R.NEW(AC.CATEGORYY)\nc = AC.AccountOpening.Account.Customer\n"
    result = check_fields(db, "ACCOUNT", src)
    assert result.verified == ["AC.CATEGORY"]
    assert result.missing == ["AC.CATEGORYY"]
    # Componentised names are NOT java aliases (R25: EB.CUS.SHORT.NAME -> Customer.EbCusShortName,
    # AC.CATEGORY -> Account.Category), so they are left to the compiler, never "verified" here.
    assert result.compiler_checked == ["AC.AccountOpening.Account.Customer"]


def test_componentised_name_is_not_verified_by_java_alias(db):
    # Customer_Mnemonic exists as a java alias, but ST.Customer.Customer.Mnemonic is undefined in R25.
    result = check_fields(db, "CUSTOMER", "x = EB.SystemTables.getRNew(ST.Customer.Customer.Mnemonic)\n")
    assert result.verified == []
    assert result.missing == []
    assert result.compiler_checked == ["ST.Customer.Customer.Mnemonic"]


def test_componentised_refs_verified_when_component_table_exists(db_with_components):
    src = ("a = EB.SystemTables.getRNew(ST.Customer.Customer.EbCusMnemonic)\n"
           "b = EB.SystemTables.getRNew(ST.Customer.Customer.Mnemonic)\n")
    result = check_fields(db_with_components, "CUSTOMER", src)
    assert result.verified == ["ST.Customer.Customer.EbCusMnemonic"]
    assert result.missing == ["ST.Customer.Customer.Mnemonic"]
    assert result.compiler_checked == []


def test_component_must_match_not_just_record_and_field(db_with_components):
    # AA.Customer has its own 'Customer' table -- EbCusMnemonic is not one of its fields.
    result = check_fields(db_with_components, "CUSTOMER", "a = AA.Customer.Customer.EbCusMnemonic\n")
    assert result.missing == ["AA.Customer.Customer.EbCusMnemonic"]
