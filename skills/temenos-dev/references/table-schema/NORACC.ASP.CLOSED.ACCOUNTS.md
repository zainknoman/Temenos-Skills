# NORACC.ASP.CLOSED.ACCOUNTS — Table Schema

> Source: `INSERTS/I_F.NORACC.ASP.CLOSED.ACCOUNTS` in `FIACCT_ASPFoundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NORACC.ASP.CLOSING.DATE` | `NoraccAspClosedAccounts_ClosingDate` | TField |  | It holds the account closing date. |
| 2 | `NORACC.ASP.CONSTRUCTION.START.DATE` | `NoraccAspClosedAccounts_ConstructionStartDate` | TField |  | It holds the construction start date. |
| 3 | `NORACC.ASP.RESERVED.15` | `NoraccAspClosedAccounts_Reserved15` | TField |  |  |
| 4 | `NORACC.ASP.RESERVED.14` | `NoraccAspClosedAccounts_Reserved14` | TField |  |  |
| 5 | `NORACC.ASP.RESERVED.13` | `NoraccAspClosedAccounts_Reserved13` | TField |  |  |
| 6 | `NORACC.ASP.RESERVED.12` | `NoraccAspClosedAccounts_Reserved12` | TField |  |  |
| 7 | `NORACC.ASP.RESERVED.11` | `NoraccAspClosedAccounts_Reserved11` | TField |  |  |
| 8 | `NORACC.ASP.RESERVED.10` | `NoraccAspClosedAccounts_Reserved10` | TField |  |  |
| 9 | `NORACC.ASP.RESERVED.9` | `NoraccAspClosedAccounts_Reserved9` | TField |  |  |
| 10 | `NORACC.ASP.RESERVED.8` | `NoraccAspClosedAccounts_Reserved8` | TField |  |  |
| 11 | `NORACC.ASP.RESERVED.7` | `NoraccAspClosedAccounts_Reserved7` | TField |  |  |
| 12 | `NORACC.ASP.RESERVED.6` | `NoraccAspClosedAccounts_Reserved6` | TField |  |  |
| 13 | `NORACC.ASP.RESERVED.5` | `NoraccAspClosedAccounts_Reserved5` | TField |  |  |
| 14 | `NORACC.ASP.RESERVED.4` | `NoraccAspClosedAccounts_Reserved4` | TField |  |  |
| 15 | `NORACC.ASP.RESERVED.3` | `NoraccAspClosedAccounts_Reserved3` | TField |  |  |
| 16 | `NORACC.ASP.RESERVED.2` | `NoraccAspClosedAccounts_Reserved2` | TField |  |  |
| 17 | `NORACC.ASP.RESERVED.1` | `NoraccAspClosedAccounts_Reserved1` | TField |  |  |
