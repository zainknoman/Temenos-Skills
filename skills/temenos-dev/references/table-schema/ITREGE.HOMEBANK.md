# ITREGE.HOMEBANK — Table Schema

> Source: `INSERTS/I_F.ITREGE.HOMEBANK` in `ITREGE_AccountMovements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ITREGE.HOMEBNK.CUSTOMER.NUMBER` | `ItregeHomebank_CustomerNumber` | TField |  | This field stores the beneficial customer number of the account |
| 2 | `ITREGE.HOMEBNK.ACCOUNT.NUMBER` | `ItregeHomebank_AccountNumber` | TField |  | This field stores the account number |
| 3 | `ITREGE.HOMEBNK.RESERVED.10` | `ItregeHomebank_Reserved10` | TField |  |  |
| 4 | `ITREGE.HOMEBNK.RESERVED.9` | `ItregeHomebank_Reserved9` | TField |  |  |
| 5 | `ITREGE.HOMEBNK.RESERVED.8` | `ItregeHomebank_Reserved8` | TField |  |  |
| 6 | `ITREGE.HOMEBNK.RESERVED.7` | `ItregeHomebank_Reserved7` | TField |  |  |
| 7 | `ITREGE.HOMEBNK.RESERVED.6` | `ItregeHomebank_Reserved6` | TField |  |  |
| 8 | `ITREGE.HOMEBNK.RESERVED.5` | `ItregeHomebank_Reserved5` | TField |  |  |
| 9 | `ITREGE.HOMEBNK.RESERVED.4` | `ItregeHomebank_Reserved4` | TField |  |  |
| 10 | `ITREGE.HOMEBNK.RESERVED.3` | `ItregeHomebank_Reserved3` | TField |  |  |
| 11 | `ITREGE.HOMEBNK.RESERVED.2` | `ItregeHomebank_Reserved2` | TField |  |  |
| 12 | `ITREGE.HOMEBNK.RESERVED.1` | `ItregeHomebank_Reserved1` | TField |  |  |
| 13 | `ITREGE.HOMEBNK.OVERRIDE` | `ItregeHomebank_Override` |  |  |  |
| 14 | `ITREGE.HOMEBNK.RECORD.STATUS` | `ItregeHomebank_RecordStatus` | String |  |  |
| 15 | `ITREGE.HOMEBNK.CURR.NO` | `ItregeHomebank_CurrNo` | String |  |  |
| 16 | `ITREGE.HOMEBNK.INPUTTER` | `ItregeHomebank_Inputter` |  |  |  |
| 17 | `ITREGE.HOMEBNK.DATE.TIME` | `ItregeHomebank_DateTime` |  |  |  |
| 18 | `ITREGE.HOMEBNK.AUTHORISER` | `ItregeHomebank_Authoriser` | String |  |  |
| 19 | `ITREGE.HOMEBNK.CO.CODE` | `ItregeHomebank_CoCode` | String |  |  |
| 20 | `ITREGE.HOMEBNK.DEPT.CODE` | `ItregeHomebank_DeptCode` | String |  |  |
| 21 | `ITREGE.HOMEBNK.AUDITOR.CODE` | `ItregeHomebank_AuditorCode` | String |  |  |
| 22 | `ITREGE.HOMEBNK.AUDIT.DATE.TIME` | `ItregeHomebank_AuditDateTime` | String |  |  |
