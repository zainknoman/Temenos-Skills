# ITREGE.ACCOUNTEXP — Table Schema

> Source: `INSERTS/I_F.ITREGE.ACCOUNTEXP` in `ITREGE_AccountMovements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ITREGE.ACC.EXP.CUSTOMER.NUMBER` | `ItregeAccountexp_CustomerNumber` | TField |  | This field stores the beneficial customer number of the account |
| 2 | `ITREGE.ACC.EXP.ACCOUNT.NUMBER` | `ItregeAccountexp_AccountNumber` | TField |  | This field stores the account number |
| 3 | `ITREGE.ACC.EXP.AA.ARR.ACT` | `ItregeAccountexp_AaArrAct` | TField |  | This field stores the arrangement activity ID |
| 4 | `ITREGE.ACC.EXP.RESERVED.10` | `ItregeAccountexp_Reserved10` |  |  |  |
| 5 | `ITREGE.ACC.EXP.RESERVED.9` | `ItregeAccountexp_Reserved9` | TField |  |  |
| 6 | `ITREGE.ACC.EXP.RESERVED.8` | `ItregeAccountexp_Reserved8` | TField |  |  |
| 7 | `ITREGE.ACC.EXP.RESERVED.7` | `ItregeAccountexp_Reserved7` | TField |  |  |
| 8 | `ITREGE.ACC.EXP.RESERVED.6` | `ItregeAccountexp_Reserved6` | TField |  |  |
| 9 | `ITREGE.ACC.EXP.RESERVED.5` | `ItregeAccountexp_Reserved5` | TField |  |  |
| 10 | `ITREGE.ACC.EXP.RESERVED.4` | `ItregeAccountexp_Reserved4` | TField |  |  |
| 11 | `ITREGE.ACC.EXP.RESERVED.3` | `ItregeAccountexp_Reserved3` | TField |  |  |
| 12 | `ITREGE.ACC.EXP.RESERVED.2` | `ItregeAccountexp_Reserved2` | TField |  |  |
| 13 | `ITREGE.ACC.EXP.RESERVED.1` | `ItregeAccountexp_Reserved1` | TField |  |  |
| 14 | `ITREGE.ACC.EXP.OVERRIDE` | `ItregeAccountexp_Override` |  |  |  |
| 15 | `ITREGE.ACC.EXP.RECORD.STATUS` | `ItregeAccountexp_RecordStatus` | String |  |  |
| 16 | `ITREGE.ACC.EXP.CURR.NO` | `ItregeAccountexp_CurrNo` | String |  |  |
| 17 | `ITREGE.ACC.EXP.INPUTTER` | `ItregeAccountexp_Inputter` |  |  |  |
| 18 | `ITREGE.ACC.EXP.DATE.TIME` | `ItregeAccountexp_DateTime` |  |  |  |
| 19 | `ITREGE.ACC.EXP.AUTHORISER` | `ItregeAccountexp_Authoriser` | String |  |  |
| 20 | `ITREGE.ACC.EXP.CO.CODE` | `ItregeAccountexp_CoCode` | String |  |  |
| 21 | `ITREGE.ACC.EXP.DEPT.CODE` | `ItregeAccountexp_DeptCode` | String |  |  |
| 22 | `ITREGE.ACC.EXP.AUDITOR.CODE` | `ItregeAccountexp_AuditorCode` | String |  |  |
| 23 | `ITREGE.ACC.EXP.AUDIT.DATE.TIME` | `ItregeAccountexp_AuditDateTime` | String |  |  |
