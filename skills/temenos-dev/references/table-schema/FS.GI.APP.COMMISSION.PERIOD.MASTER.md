# FS.GI.APP.COMMISSION.PERIOD.MASTER — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.COMMISSION.PERIOD.MASTER` in `FS_CommissionManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.PARENT.REF.ID` | `FsGiAppCommissionPeriodMaster_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.ORA.ROWID` | `FsGiAppCommissionPeriodMaster_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.PERIOD.CODE` | `FsGiAppCommissionPeriodMaster_PeriodCode` | TField |  | Commission period code. Multifonds DB Column is CPERIOD. |
| 4 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.PERIOD.DESCRIPTION` | `FsGiAppCommissionPeriodMaster_PeriodDescription` | TField |  | Commission period description. Multifonds DB Column is LIB_CPERIOD. |
| 5 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.PERIOD.TYPE` | `FsGiAppCommissionPeriodMaster_PeriodType` | TField |  | Commission period type. For example: Days, Months and Years. Multifonds DB Column is TYPE_PERIOD. |
| 6 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.COMM.CURRENCY` | `FsGiAppCommissionPeriodMaster_CommCurrency` | TField |  | Currency of the commission. Multifonds DB Column is CMON. |
| 7 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.MINIMUM.COMMISSION` | `FsGiAppCommissionPeriodMaster_MinimumCommission` | TField |  | Minimum commission amount applicable to the period defintion. Multifonds DB Column is MIN_COMM. |
| 8 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.MAXIMUM.COMMISSION` | `FsGiAppCommissionPeriodMaster_MaximumCommission` | TField |  | Maximum commission amount applicable to the period definition. Multifonds DB Column is MAX_COMM. |
| 9 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.RESERVED10` | `FsGiAppCommissionPeriodMaster_Reserved10` | TField |  |  |
| 10 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.RESERVED9` | `FsGiAppCommissionPeriodMaster_Reserved9` | TField |  |  |
| 11 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.RESERVED8` | `FsGiAppCommissionPeriodMaster_Reserved8` | TField |  |  |
| 12 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.RESERVED7` | `FsGiAppCommissionPeriodMaster_Reserved7` | TField |  |  |
| 13 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.RESERVED6` | `FsGiAppCommissionPeriodMaster_Reserved6` | TField |  |  |
| 14 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.RESERVED5` | `FsGiAppCommissionPeriodMaster_Reserved5` | TField |  |  |
| 15 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.RESERVED4` | `FsGiAppCommissionPeriodMaster_Reserved4` | TField |  |  |
| 16 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.RESERVED3` | `FsGiAppCommissionPeriodMaster_Reserved3` | TField |  |  |
| 17 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.RESERVED2` | `FsGiAppCommissionPeriodMaster_Reserved2` | TField |  |  |
| 18 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.RESERVED1` | `FsGiAppCommissionPeriodMaster_Reserved1` | TField |  |  |
| 19 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.LOCAL.REF` | `FsGiAppCommissionPeriodMaster_LocalRef` |  |  |  |
| 20 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.OVERRIDE` | `FsGiAppCommissionPeriodMaster_Override` |  |  |  |
| 21 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.RECORD.STATUS` | `FsGiAppCommissionPeriodMaster_RecordStatus` | String |  |  |
| 22 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.CURR.NO` | `FsGiAppCommissionPeriodMaster_CurrNo` | String |  |  |
| 23 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.INPUTTER` | `FsGiAppCommissionPeriodMaster_Inputter` |  |  |  |
| 24 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.DATE.TIME` | `FsGiAppCommissionPeriodMaster_DateTime` |  |  |  |
| 25 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.AUTHORISER` | `FsGiAppCommissionPeriodMaster_Authoriser` | String |  |  |
| 26 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.CO.CODE` | `FsGiAppCommissionPeriodMaster_CoCode` | String |  |  |
| 27 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.DEPT.CODE` | `FsGiAppCommissionPeriodMaster_DeptCode` | String |  |  |
| 28 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.AUDITOR.CODE` | `FsGiAppCommissionPeriodMaster_AuditorCode` | String |  |  |
| 29 | `FS.GI.APP.COMMISSION.PERIOD.MASTER.AUDIT.DATE.TIME` | `FsGiAppCommissionPeriodMaster_AuditDateTime` | String |  |  |
