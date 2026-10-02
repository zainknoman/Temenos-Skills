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
    assert refs.componentised == {"Account_Category"}


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
    assert result.compiler_checked == ["Account.Customer"]


def test_componentised_name_is_not_verified_by_java_alias(db):
    # Customer_Mnemonic exists as a java alias, but ST.Customer.Customer.Mnemonic is undefined in R25.
    result = check_fields(db, "CUSTOMER", "x = EB.SystemTables.getRNew(ST.Customer.Customer.Mnemonic)\n")
    assert result.verified == []
    assert result.missing == []
    assert result.compiler_checked == ["Customer.Mnemonic"]
