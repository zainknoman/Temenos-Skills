# PPARMS.ARG.CCY.RESTRICT.PARAM — Table Schema

> Source: `INSERTS/I_F.PPARMS.ARG.CCY.RESTRICT.PARAM` in `PPARMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPARMS.PAR.PAYMENT.TYPE` | `PparmsArgCcyRestrictParam_PaymentType` |  |  |  |
| 2 | `PPARMS.PAR.TIME.PERIOD` | `PparmsArgCcyRestrictParam_TimePeriod` | TField |  | Time period to be given in the format of CBWMY(Calendar Days,Business Days,Weeks,Months,Years) |
| 3 | `PPARMS.PAR.RESERVED.5` | `PparmsArgCcyRestrictParam_Reserved5` | TField |  | Reserved for future purpose |
| 4 | `PPARMS.PAR.RESERVED.4` | `PparmsArgCcyRestrictParam_Reserved4` | TField |  | Reserved for future purpose |
| 5 | `PPARMS.PAR.RESERVED.3` | `PparmsArgCcyRestrictParam_Reserved3` | TField |  | Reserved for future purpose |
| 6 | `PPARMS.PAR.RESERVED.2` | `PparmsArgCcyRestrictParam_Reserved2` | TField |  | Reserved for future purpose |
| 7 | `PPARMS.PAR.RESERVED.1` | `PparmsArgCcyRestrictParam_Reserved1` | TField |  | Reserved for future purpose |
| 8 | `PPARMS.PAR.LOCAL.REF` | `PparmsArgCcyRestrictParam_LocalRef` |  |  |  |
| 9 | `PPARMS.PAR.OVERRIDE` | `PparmsArgCcyRestrictParam_Override` |  |  |  |
| 10 | `PPARMS.PAR.RECORD.STATUS` | `PparmsArgCcyRestrictParam_RecordStatus` | String |  |  |
| 11 | `PPARMS.PAR.CURR.NO` | `PparmsArgCcyRestrictParam_CurrNo` | String |  |  |
| 12 | `PPARMS.PAR.INPUTTER` | `PparmsArgCcyRestrictParam_Inputter` |  |  |  |
| 13 | `PPARMS.PAR.DATE.TIME` | `PparmsArgCcyRestrictParam_DateTime` |  |  |  |
| 14 | `PPARMS.PAR.AUTHORISER` | `PparmsArgCcyRestrictParam_Authoriser` | String |  |  |
| 15 | `PPARMS.PAR.CO.CODE` | `PparmsArgCcyRestrictParam_CoCode` | String |  |  |
| 16 | `PPARMS.PAR.DEPT.CODE` | `PparmsArgCcyRestrictParam_DeptCode` | String |  |  |
| 17 | `PPARMS.PAR.AUDITOR.CODE` | `PparmsArgCcyRestrictParam_AuditorCode` | String |  |  |
| 18 | `PPARMS.PAR.AUDIT.DATE.TIME` | `PparmsArgCcyRestrictParam_AuditDateTime` | String |  |  |
