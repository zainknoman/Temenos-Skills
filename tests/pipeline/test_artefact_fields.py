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
    assert result.verified == ["AC.CATEGORY", "Account_Customer"]
    assert result.missing == ["AC.CATEGORYY"]
