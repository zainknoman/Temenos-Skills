# FS.GA.WEM.FUND — Table Schema

> Source: `INSERTS/I_F.FS.GA.WEM.FUND` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.WEM.FUND.PARENT.REF.ID` | `FsGaWemFund_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.WEM.FUND.ORA.ROWID` | `FsGaWemFund_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.WEM.FUND.FUND.NAME` | `FsGaWemFund_FundName` | TField |  | Fund Name Multifonds DB Column is FUND_ID. |
| 4 | `FS.GA.WEM.FUND.MODEL.ID` | `FsGaWemFund_ModelId` | TField |  | ID of the Model Multifonds DB Column is MODEL_ID. |
| 5 | `FS.GA.WEM.FUND.FAMILY.ID` | `FsGaWemFund_FamilyId` | TField |  | ID of the Family Multifonds DB Column is FAMILY_ID. |
| 6 | `FS.GA.WEM.FUND.NEXT.THEORETICAL.NAV.DATE` | `FsGaWemFund_NextTheoreticalNavDate` | TField |  | Displays the next theoretical NAV date according to the frequency defined. Multifonds DB Column is NEXT_THEORIC_NAV_DATE. |
| 7 | `FS.GA.WEM.FUND.FUND.STATUS.IDENTIFIER` | `FsGaWemFund_FundStatusIdentifier` | TField |  | Fund Status Identifier Multifonds DB Column is FUND_STATUS_ID. |
| 8 | `FS.GA.WEM.FUND.DAY.MINUS.OR.PREVIOUS.DAY` | `FsGaWemFund_DayMinusOrPreviousDay` | TField |  | Day Minus or Previous Day Multifonds DB Column is DAY_MINUS. |
| 9 | `FS.GA.WEM.FUND.WARNING.EXCEPTION.LEVEL` | `FsGaWemFund_WarningExceptionLevel` | TField |  | Warning Exception Level Multifonds DB Column is WAR_EXCEPTION_ID. |
| 10 | `FS.GA.WEM.FUND.FATAL.EXCEPTION.LEVEL` | `FsGaWemFund_FatalExceptionLevel` | TField |  | Minimum status for Fatal Exception Multifonds DB Column is FAT_EXCEPTION_ID. |
| 11 | `FS.GA.WEM.FUND.NUMBER.OF.DAYS` | `FsGaWemFund_NumberOfDays` | TField |  | Number Of Days Multifonds DB Column is NO_OF_DAYS. |
| 12 | `FS.GA.WEM.FUND.PENDING.STATUS` | `FsGaWemFund_PendingStatus` | TField |  | Pending Delete Multifonds DB Column is PENDING_STATUS. |
| 13 | `FS.GA.WEM.FUND.SPECIFIC.APPROVAL.RIGHTS` | `FsGaWemFund_SpecificApprovalRights` | TField |  | Fund Specific Exception Approval Rights Multifonds DB Column is SPEC_APPROVAL. |
| 14 | `FS.GA.WEM.FUND.NAV.GRP` | `FsGaWemFund_NavGrp` | TField |  | NAV Group Multifonds DB Column is NAV_GRP. |
| 15 | `FS.GA.WEM.FUND.PENDING.DELETE` | `FsGaWemFund_PendingDelete` | TField |  | Pending Delete Multifonds DB Column is PENDING_DELETE. |
| 16 | `FS.GA.WEM.FUND.RESERVED10` | `FsGaWemFund_Reserved10` | TField |  |  |
| 17 | `FS.GA.WEM.FUND.RESERVED9` | `FsGaWemFund_Reserved9` | TField |  |  |
| 18 | `FS.GA.WEM.FUND.RESERVED8` | `FsGaWemFund_Reserved8` | TField |  |  |
| 19 | `FS.GA.WEM.FUND.RESERVED7` | `FsGaWemFund_Reserved7` | TField |  |  |
| 20 | `FS.GA.WEM.FUND.RESERVED6` | `FsGaWemFund_Reserved6` | TField |  |  |
| 21 | `FS.GA.WEM.FUND.RESERVED5` | `FsGaWemFund_Reserved5` | TField |  |  |
| 22 | `FS.GA.WEM.FUND.RESERVED4` | `FsGaWemFund_Reserved4` | TField |  |  |
| 23 | `FS.GA.WEM.FUND.RESERVED3` | `FsGaWemFund_Reserved3` | TField |  |  |
| 24 | `FS.GA.WEM.FUND.RESERVED2` | `FsGaWemFund_Reserved2` | TField |  |  |
| 25 | `FS.GA.WEM.FUND.RESERVED1` | `FsGaWemFund_Reserved1` | TField |  |  |
| 26 | `FS.GA.WEM.FUND.LOCAL.REF` | `FsGaWemFund_LocalRef` |  |  |  |
| 27 | `FS.GA.WEM.FUND.OVERRIDE` | `FsGaWemFund_Override` |  |  |  |
| 28 | `FS.GA.WEM.FUND.RECORD.STATUS` | `FsGaWemFund_RecordStatus` | String |  |  |
| 29 | `FS.GA.WEM.FUND.CURR.NO` | `FsGaWemFund_CurrNo` | String |  |  |
| 30 | `FS.GA.WEM.FUND.INPUTTER` | `FsGaWemFund_Inputter` |  |  |  |
| 31 | `FS.GA.WEM.FUND.DATE.TIME` | `FsGaWemFund_DateTime` |  |  |  |
| 32 | `FS.GA.WEM.FUND.AUTHORISER` | `FsGaWemFund_Authoriser` | String |  |  |
| 33 | `FS.GA.WEM.FUND.CO.CODE` | `FsGaWemFund_CoCode` | String |  |  |
| 34 | `FS.GA.WEM.FUND.DEPT.CODE` | `FsGaWemFund_DeptCode` | String |  |  |
| 35 | `FS.GA.WEM.FUND.AUDITOR.CODE` | `FsGaWemFund_AuditorCode` | String |  |  |
| 36 | `FS.GA.WEM.FUND.AUDIT.DATE.TIME` | `FsGaWemFund_AuditDateTime` | String |  |  |
