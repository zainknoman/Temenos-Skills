import sqlite3
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "pipeline"))

SCHEMA = """CREATE TABLE fields (
    app TEXT, field_name TEXT, position INTEGER, java_alias TEXT,
    source_jar TEXT, field_type TEXT, mandatory TEXT, description TEXT)"""

ROWS = [
    ("ACCOUNT", "AC.CUSTOMER", 1, "Account_Customer", "AC_AccountOpening.jar", "TField", "Yes", "Customer id"),
    ("ACCOUNT", "AC.CATEGORY", 2, "Account_Category", "AC_AccountOpening.jar", "TField", "Yes", "Category"),
    ("ACCOUNT", "AC.ACCOUNT.TITLE.1", 3, "Account_AccountTitle1", "AC_AccountOpening.jar", None, None, None),
    ("CUSTOMER", "EB.CUS.MNEMONIC", 1, "Customer_Mnemonic", "ST_Customer.jar", "TField", "Yes", "Mnemonic"),
    ("CUSTOMER", "EB.CUS.SHORT.NAME", 2, "Customer_ShortName", "ST_Customer.jar", None, None, None),
]


@pytest.fixture
def db():
    conn = sqlite3.connect(":memory:")
    conn.execute(SCHEMA)
    conn.executemany("INSERT INTO fields VALUES (?,?,?,?,?,?,?,?)", ROWS)
    yield conn
    conn.close()


COMPONENT_ROWS = [
    ("R23", "CUSTOMER", "ST.Customer", "Customer", "EbCusMnemonic", 1, "EB.CUS.MNEMONIC"),
    ("R23", "CUSTOMER", "ST.Customer", "Customer", "EbCusShortName", 2, "EB.CUS.SHORT.NAME"),
    ("R23", "ACCOUNT", "AC.AccountOpening", "Account", "Category", 2, "AC.CATEGORY"),
]


@pytest.fixture
def db_with_components(db):
    db.execute("""CREATE TABLE component_fields (release TEXT, app TEXT, component TEXT, record TEXT,
                  comp_field TEXT, position INTEGER, field_name TEXT)""")
    db.executemany("INSERT INTO component_fields VALUES (?,?,?,?,?,?,?)", COMPONENT_ROWS)
    return db


KIND_ROWS = [
    ("R23", "CUSTOMER", "EB.CUS.MNEMONIC", "SV", "CustomerRecord"),
    ("R23", "CUSTOMER", "EB.CUS.SHORT.NAME", "MV", "CustomerRecord"),
    ("R23", "ACCOUNT", "AC.CATEGORY", "SV", "AccountRecord"),
]


@pytest.fixture
def db_with_kinds(db):
    db.execute("CREATE TABLE field_kinds (release TEXT, app TEXT, field_name TEXT, kind TEXT, getter_class TEXT)")
    db.executemany("INSERT INTO field_kinds VALUES (?,?,?,?,?)", KIND_ROWS)
    return db
