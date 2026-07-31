# CAREGS.CDIC.CLEARING.CODES — Table Schema

> Source: `INSERTS/I_F.CAREGS.CDIC.CLEARING.CODES` in `CADEPO_CDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CDIC.CLR.CODES.DESCRIPTION` | `CaregsCdicClearingCodes_Description` | TField |  | Field to store the description of the record.Allowed upto 35 char. |
| 2 | `CDIC.CLR.CODES.CLEARING.ACCT.CODE` | `CaregsCdicClearingCodes_ClearingAcctCode` | TField |  |  |
| 3 | `CDIC.CLR.CODES.CATEGORY` | `CaregsCdicClearingCodes_Category` |  |  |  |
| 4 | `CDIC.CLR.CODES.RESERVED.1` | `CaregsCdicClearingCodes_Reserved1` | TField |  |  |
| 5 | `CDIC.CLR.CODES.RESERVED.2` | `CaregsCdicClearingCodes_Reserved2` | TField |  |  |
| 6 | `CDIC.CLR.CODES.RESERVED.3` | `CaregsCdicClearingCodes_Reserved3` | TField |  |  |
| 7 | `CDIC.CLR.CODES.RESERVED.4` | `CaregsCdicClearingCodes_Reserved4` | TField |  |  |
| 8 | `CDIC.CLR.CODES.RESERVED.5` | `CaregsCdicClearingCodes_Reserved5` | TField |  |  |
| 9 | `CDIC.CLR.CODES.LOCAL.REF` | `CaregsCdicClearingCodes_LocalRef` |  |  |  |
| 10 | `CDIC.CLR.CODES.RECORD.STATUS` | `CaregsCdicClearingCodes_RecordStatus` | String |  |  |
| 11 | `CDIC.CLR.CODES.CURR.NO` | `CaregsCdicClearingCodes_CurrNo` | String |  |  |
| 12 | `CDIC.CLR.CODES.INPUTTER` | `CaregsCdicClearingCodes_Inputter` |  |  |  |
| 13 | `CDIC.CLR.CODES.DATE.TIME` | `CaregsCdicClearingCodes_DateTime` |  |  |  |
| 14 | `CDIC.CLR.CODES.AUTHORISER` | `CaregsCdicClearingCodes_Authoriser` | String |  |  |
| 15 | `CDIC.CLR.CODES.CO.CODE` | `CaregsCdicClearingCodes_CoCode` | String |  |  |
| 16 | `CDIC.CLR.CODES.DEPT.CODE` | `CaregsCdicClearingCodes_DeptCode` | String |  |  |
| 17 | `CDIC.CLR.CODES.AUDITOR.CODE` | `CaregsCdicClearingCodes_AuditorCode` | String |  |  |
| 18 | `CDIC.CLR.CODES.AUDIT.DATE.TIME` | `CaregsCdicClearingCodes_AuditDateTime` | String |  |  |
