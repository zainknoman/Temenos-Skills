# USRETL.ACCOUNT.LOCKED.EVENTS — Table Schema

> Source: `INSERTS/I_F.USRETL.ACCOUNT.LOCKED.EVENTS` in `USRETL_AccountAnalysis.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USRETL.ACLE.FROM.DATE` | `UsretlAccountLockedEvents_FromDate` |  |  |  |
| 2 | `USRETL.ACLE.LOCKED.AMOUNT` | `UsretlAccountLockedEvents_LockedAmount` |  |  |  |
| 3 | `USRETL.ACLE.RESERVED.10` | `UsretlAccountLockedEvents_Reserved10` | TField |  |  |
| 4 | `USRETL.ACLE.RESERVED.9` | `UsretlAccountLockedEvents_Reserved9` | TField |  |  |
| 5 | `USRETL.ACLE.RESERVED.8` | `UsretlAccountLockedEvents_Reserved8` | TField |  |  |
| 6 | `USRETL.ACLE.RESERVED.7` | `UsretlAccountLockedEvents_Reserved7` | TField |  |  |
| 7 | `USRETL.ACLE.RESERVED.6` | `UsretlAccountLockedEvents_Reserved6` | TField |  |  |
| 8 | `USRETL.ACLE.RESERVED.5` | `UsretlAccountLockedEvents_Reserved5` | TField |  |  |
| 9 | `USRETL.ACLE.RESERVED.4` | `UsretlAccountLockedEvents_Reserved4` | TField |  |  |
| 10 | `USRETL.ACLE.RESERVED.3` | `UsretlAccountLockedEvents_Reserved3` | TField |  |  |
| 11 | `USRETL.ACLE.RESERVED.2` | `UsretlAccountLockedEvents_Reserved2` | TField |  |  |
| 12 | `USRETL.ACLE.RESERVED.1` | `UsretlAccountLockedEvents_Reserved1` | TField |  |  |
