# FS.GI.APP.COMMISSION.PERIOD.DETAILS — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.COMMISSION.PERIOD.DETAILS` in `FS_CommissionManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.PARENT.REF.ID` | `FsGiAppCommissionPeriodDetails_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.ORA.ROWID` | `FsGiAppCommissionPeriodDetails_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.PERIOD` | `FsGiAppCommissionPeriodDetails_Period` | TField |  | Period code used for the details defintion. Multifonds DB Column is CPERIOD. |
| 4 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.PERIOD.START` | `FsGiAppCommissionPeriodDetails_PeriodStart` | TField |  | Start period for the commission details. Multifonds DB Column is PERIOD_FROM. |
| 5 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.PERIOD.END` | `FsGiAppCommissionPeriodDetails_PeriodEnd` | TField |  | End period for the commission details. Multifonds DB Column is PERIOD_TO. |
| 6 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.COMM.TYPE` | `FsGiAppCommissionPeriodDetails_CommType` | TField |  | Period Commission type for debit operations Multifonds DB Column is TYPE_COMM. |
| 7 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.COMMISSION.PERCENTAGE` | `FsGiAppCommissionPeriodDetails_CommissionPercentage` | TField |  | Percentage of the commission . Multifonds DB Column is PC_MNT. |
| 8 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.COMMISSION.AMOUNT` | `FsGiAppCommissionPeriodDetails_CommissionAmount` | TField |  | Amount of the Commission Multifonds DB Column is PC_AMMOUNT. |
| 9 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.SCALE` | `FsGiAppCommissionPeriodDetails_Scale` | TField |  | Scale code of the period definition. Multifonds DB Column is SCALE_NAME. |
| 10 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.RESERVED10` | `FsGiAppCommissionPeriodDetails_Reserved10` | TField |  |  |
| 11 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.RESERVED9` | `FsGiAppCommissionPeriodDetails_Reserved9` | TField |  |  |
| 12 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.RESERVED8` | `FsGiAppCommissionPeriodDetails_Reserved8` | TField |  |  |
| 13 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.RESERVED7` | `FsGiAppCommissionPeriodDetails_Reserved7` | TField |  |  |
| 14 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.RESERVED6` | `FsGiAppCommissionPeriodDetails_Reserved6` | TField |  |  |
| 15 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.RESERVED5` | `FsGiAppCommissionPeriodDetails_Reserved5` | TField |  |  |
| 16 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.RESERVED4` | `FsGiAppCommissionPeriodDetails_Reserved4` | TField |  |  |
| 17 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.RESERVED3` | `FsGiAppCommissionPeriodDetails_Reserved3` | TField |  |  |
| 18 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.RESERVED2` | `FsGiAppCommissionPeriodDetails_Reserved2` | TField |  |  |
| 19 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.RESERVED1` | `FsGiAppCommissionPeriodDetails_Reserved1` | TField |  |  |
| 20 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.LOCAL.REF` | `FsGiAppCommissionPeriodDetails_LocalRef` |  |  |  |
| 21 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.OVERRIDE` | `FsGiAppCommissionPeriodDetails_Override` |  |  |  |
| 22 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.RECORD.STATUS` | `FsGiAppCommissionPeriodDetails_RecordStatus` | String |  |  |
| 23 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.CURR.NO` | `FsGiAppCommissionPeriodDetails_CurrNo` | String |  |  |
| 24 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.INPUTTER` | `FsGiAppCommissionPeriodDetails_Inputter` |  |  |  |
| 25 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.DATE.TIME` | `FsGiAppCommissionPeriodDetails_DateTime` |  |  |  |
| 26 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.AUTHORISER` | `FsGiAppCommissionPeriodDetails_Authoriser` | String |  |  |
| 27 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.CO.CODE` | `FsGiAppCommissionPeriodDetails_CoCode` | String |  |  |
| 28 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.DEPT.CODE` | `FsGiAppCommissionPeriodDetails_DeptCode` | String |  |  |
| 29 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.AUDITOR.CODE` | `FsGiAppCommissionPeriodDetails_AuditorCode` | String |  |  |
| 30 | `FS.GI.APP.COMMISSION.PERIOD.DETAILS.AUDIT.DATE.TIME` | `FsGiAppCommissionPeriodDetails_AuditDateTime` | String |  |  |
