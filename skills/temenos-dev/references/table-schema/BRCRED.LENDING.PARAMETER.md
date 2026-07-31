# BRCRED.LENDING.PARAMETER — Table Schema

> Source: `INSERTS/I_F.BRCRED.LENDING.PARAMETER` in `BRCRED_CreditOperations.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BRCRED.LENP.MAXIMUM.DAYS.IOF` | `BrcredLendingParameter_MaximumDaysIof` | TField |  | This field is used to define the maximum days of the IOF to be calculated. |
| 2 | `BRCRED.LENP.LOCAL.REF` | `BrcredLendingParameter_LocalRef` |  |  |  |
| 3 | `BRCRED.LENP.RESERVED.10` | `BrcredLendingParameter_Reserved10` | TField |  | Reserved for Future use. |
| 4 | `BRCRED.LENP.RESERVED.9` | `BrcredLendingParameter_Reserved9` | TField |  | Reserved for Future use. |
| 5 | `BRCRED.LENP.RESERVED.8` | `BrcredLendingParameter_Reserved8` | TField |  | Reserved for Future use. |
| 6 | `BRCRED.LENP.RESERVED.7` | `BrcredLendingParameter_Reserved7` | TField |  | Reserved for Future use. |
| 7 | `BRCRED.LENP.RESERVED.6` | `BrcredLendingParameter_Reserved6` | TField |  | Reserved for Future use. |
| 8 | `BRCRED.LENP.RESERVED.5` | `BrcredLendingParameter_Reserved5` | TField |  | Reserved for Future use. |
| 9 | `BRCRED.LENP.RESERVED.4` | `BrcredLendingParameter_Reserved4` | TField |  | Reserved for Future use. |
| 10 | `BRCRED.LENP.RESERVED.3` | `BrcredLendingParameter_Reserved3` | TField |  | Reserved for Future use. |
| 11 | `BRCRED.LENP.RESERVED.2` | `BrcredLendingParameter_Reserved2` | TField |  | Reserved for Future use. |
| 12 | `BRCRED.LENP.RESERVED.1` | `BrcredLendingParameter_Reserved1` | TField |  | Reserved for Future use. |
| 13 | `BRCRED.LENP.OVERRIDE` | `BrcredLendingParameter_Override` |  |  |  |
| 14 | `BRCRED.LENP.RECORD.STATUS` | `BrcredLendingParameter_RecordStatus` | String |  |  |
| 15 | `BRCRED.LENP.CURR.NO` | `BrcredLendingParameter_CurrNo` | String |  |  |
| 16 | `BRCRED.LENP.INPUTTER` | `BrcredLendingParameter_Inputter` |  |  |  |
| 17 | `BRCRED.LENP.DATE.TIME` | `BrcredLendingParameter_DateTime` |  |  |  |
| 18 | `BRCRED.LENP.AUTHORISER` | `BrcredLendingParameter_Authoriser` | String |  |  |
| 19 | `BRCRED.LENP.CO.CODE` | `BrcredLendingParameter_CoCode` | String |  |  |
| 20 | `BRCRED.LENP.DEPT.CODE` | `BrcredLendingParameter_DeptCode` | String |  |  |
| 21 | `BRCRED.LENP.AUDITOR.CODE` | `BrcredLendingParameter_AuditorCode` | String |  |  |
| 22 | `BRCRED.LENP.AUDIT.DATE.TIME` | `BrcredLendingParameter_AuditDateTime` | String |  |  |
