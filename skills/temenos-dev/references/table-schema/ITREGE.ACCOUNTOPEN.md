# ITREGE.ACCOUNTOPEN — Table Schema

> Source: `INSERTS/I_F.ITREGE.ACCOUNTOPEN` in `ITREGE_AccountMovements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ITREGE.ACC.OPN.CUSTOMER.NUMBER` | `ItregeAccountopen_CustomerNumber` | TField |  | This field stores the beneficial customer number of the account |
| 2 | `ITREGE.ACC.OPN.ACCOUNT.NUMBER` | `ItregeAccountopen_AccountNumber` | TField |  | This field stores the account number |
| 3 | `ITREGE.ACC.OPN.RESERVED.10` | `ItregeAccountopen_Reserved10` | TField |  |  |
| 4 | `ITREGE.ACC.OPN.RESERVED.9` | `ItregeAccountopen_Reserved9` | TField |  |  |
| 5 | `ITREGE.ACC.OPN.RESERVED.8` | `ItregeAccountopen_Reserved8` | TField |  |  |
| 6 | `ITREGE.ACC.OPN.RESERVED.7` | `ItregeAccountopen_Reserved7` | TField |  |  |
| 7 | `ITREGE.ACC.OPN.RESERVED.6` | `ItregeAccountopen_Reserved6` | TField |  |  |
| 8 | `ITREGE.ACC.OPN.RESERVED.5` | `ItregeAccountopen_Reserved5` | TField |  |  |
| 9 | `ITREGE.ACC.OPN.RESERVED.4` | `ItregeAccountopen_Reserved4` | TField |  |  |
| 10 | `ITREGE.ACC.OPN.RESERVED.3` | `ItregeAccountopen_Reserved3` | TField |  |  |
| 11 | `ITREGE.ACC.OPN.RESERVED.2` | `ItregeAccountopen_Reserved2` | TField |  |  |
| 12 | `ITREGE.ACC.OPN.RESERVED.1` | `ItregeAccountopen_Reserved1` | TField |  |  |
| 13 | `ITREGE.ACC.OPN.OVERRIDE` | `ItregeAccountopen_Override` |  |  |  |
| 14 | `ITREGE.ACC.OPN.RECORD.STATUS` | `ItregeAccountopen_RecordStatus` | String |  |  |
| 15 | `ITREGE.ACC.OPN.CURR.NO` | `ItregeAccountopen_CurrNo` | String |  |  |
| 16 | `ITREGE.ACC.OPN.INPUTTER` | `ItregeAccountopen_Inputter` |  |  |  |
| 17 | `ITREGE.ACC.OPN.DATE.TIME` | `ItregeAccountopen_DateTime` |  |  |  |
| 18 | `ITREGE.ACC.OPN.AUTHORISER` | `ItregeAccountopen_Authoriser` | String |  |  |
| 19 | `ITREGE.ACC.OPN.CO.CODE` | `ItregeAccountopen_CoCode` | String |  |  |
| 20 | `ITREGE.ACC.OPN.DEPT.CODE` | `ItregeAccountopen_DeptCode` | String |  |  |
| 21 | `ITREGE.ACC.OPN.AUDITOR.CODE` | `ItregeAccountopen_AuditorCode` | String |  |  |
| 22 | `ITREGE.ACC.OPN.AUDIT.DATE.TIME` | `ItregeAccountopen_AuditDateTime` | String |  |  |
