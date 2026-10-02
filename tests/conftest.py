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
