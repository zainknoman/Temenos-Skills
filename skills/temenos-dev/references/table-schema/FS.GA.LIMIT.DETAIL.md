# FS.GA.LIMIT.DETAIL — Table Schema

> Source: `INSERTS/I_F.FS.GA.LIMIT.DETAIL` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.LIMIT.DETAIL.GROUP.LIMIT` | `FsGaLimitDetail_GroupLimit` | TField |  | Group Limit Multifonds DB Column is CLEGIS. |
| 2 | `FS.GA.LIMIT.DETAIL.INVESTMENT.RESTRICTION.LAW` | `FsGaLimitDetail_InvestmentRestrictionLaw` | TField |  | Select investment restriction law code as predefined. This is specifically created to support various investment restriction or limits. Used in new limits module. Multifonds DB Column is CLAW. |
| 3 | `FS.GA.LIMIT.DETAIL.LIMIT.GROUP.CODE` | `FsGaLimitDetail_LimitGroupCode` | TField |  | This shows the limit group code while defining investment restrictions. This code is linked in fund to have the investment restrictions laws for the fund. Multifonds DB Column is NSL_NO. |
| 4 | `FS.GA.LIMIT.DETAIL.QUOTATION.TYPE` | `FsGaLimitDetail_QuotationType` | TField |  | Quatation Type Multifonds DB Column is CTYPE. |
| 5 | `FS.GA.LIMIT.DETAIL.CONNECTOR` | `FsGaLimitDetail_Connector` | TField |  | Connectors are conditions applied while fetching the numerator. Multifonds DB Column is CCONNECTOR. |
| 6 | `FS.GA.LIMIT.DETAIL.PARAMETER` | `FsGaLimitDetail_Parameter` | TField |  | Various parameters for report set-up Multifonds DB Column is CPARAM. |
| 7 | `FS.GA.LIMIT.DETAIL.OPERATOR` | `FsGaLimitDetail_Operator` | TField |  | Operator codes are used to create the condition. Multifonds DB Column is COPERATOR. |
| 8 | `FS.GA.LIMIT.DETAIL.LIMITS.VALUE` | `FsGaLimitDetail_LimitsValue` | TField |  | Specify the values as per the selected operators while defining limits or investment restrictions. To be asset type code, security identifier, amount or any value depending on the operators selected. Multifonds DB Column is CVALUE. |
| 9 | `FS.GA.LIMIT.DETAIL.LIM.TYPE` | `FsGaLimitDetail_LimType` | TField |  | Field that allows either a percent or amount to be chosen. Multifonds DB Column is CTYP_LIM. |
| 10 | `FS.GA.LIMIT.DETAIL.RESERVED10` | `FsGaLimitDetail_Reserved10` | TField |  |  |
| 11 | `FS.GA.LIMIT.DETAIL.RESERVED9` | `FsGaLimitDetail_Reserved9` | TField |  |  |
| 12 | `FS.GA.LIMIT.DETAIL.RESERVED8` | `FsGaLimitDetail_Reserved8` | TField |  |  |
| 13 | `FS.GA.LIMIT.DETAIL.RESERVED7` | `FsGaLimitDetail_Reserved7` | TField |  |  |
| 14 | `FS.GA.LIMIT.DETAIL.RESERVED6` | `FsGaLimitDetail_Reserved6` | TField |  |  |
| 15 | `FS.GA.LIMIT.DETAIL.RESERVED5` | `FsGaLimitDetail_Reserved5` | TField |  |  |
| 16 | `FS.GA.LIMIT.DETAIL.RESERVED4` | `FsGaLimitDetail_Reserved4` | TField |  |  |
| 17 | `FS.GA.LIMIT.DETAIL.RESERVED3` | `FsGaLimitDetail_Reserved3` | TField |  |  |
| 18 | `FS.GA.LIMIT.DETAIL.RESERVED2` | `FsGaLimitDetail_Reserved2` | TField |  |  |
| 19 | `FS.GA.LIMIT.DETAIL.RESERVED1` | `FsGaLimitDetail_Reserved1` | TField |  |  |
| 20 | `FS.GA.LIMIT.DETAIL.RECORD.STATUS` | `FsGaLimitDetail_RecordStatus` | String |  |  |
| 21 | `FS.GA.LIMIT.DETAIL.CURR.NO` | `FsGaLimitDetail_CurrNo` | String |  |  |
| 22 | `FS.GA.LIMIT.DETAIL.INPUTTER` | `FsGaLimitDetail_Inputter` |  |  |  |
| 23 | `FS.GA.LIMIT.DETAIL.DATE.TIME` | `FsGaLimitDetail_DateTime` |  |  |  |
| 24 | `FS.GA.LIMIT.DETAIL.AUTHORISER` | `FsGaLimitDetail_Authoriser` | String |  |  |
| 25 | `FS.GA.LIMIT.DETAIL.CO.CODE` | `FsGaLimitDetail_CoCode` | String |  |  |
| 26 | `FS.GA.LIMIT.DETAIL.DEPT.CODE` | `FsGaLimitDetail_DeptCode` | String |  |  |
| 27 | `FS.GA.LIMIT.DETAIL.AUDITOR.CODE` | `FsGaLimitDetail_AuditorCode` | String |  |  |
| 28 | `FS.GA.LIMIT.DETAIL.AUDIT.DATE.TIME` | `FsGaLimitDetail_AuditDateTime` | String |  |  |
