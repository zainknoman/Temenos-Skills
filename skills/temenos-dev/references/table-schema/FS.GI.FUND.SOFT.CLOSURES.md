# FS.GI.FUND.SOFT.CLOSURES — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.SOFT.CLOSURES` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.SOFT.CLOSURES.PARENT.REF.ID` | `FsGiFundSoftClosures_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.SOFT.CLOSURES.ORA.ROWID` | `FsGiFundSoftClosures_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.SOFT.CLOSURES.TA.FUND.ID` | `FsGiFundSoftClosures_TaFundId` | TField |  | Fund internal Id. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.SOFT.CLOSURES.OPERATION.CODE` | `FsGiFundSoftClosures_OperationCode` | TField |  | Operation code for which the soft closures are applicable. Multifonds DB Column is COPERATION. |
| 5 | `FS.GI.FUND.SOFT.CLOSURES.SHARE.CLASS.CODE` | `FsGiFundSoftClosures_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 6 | `FS.GI.FUND.SOFT.CLOSURES.EFFECTIVE.DATE` | `FsGiFundSoftClosures_EffectiveDate` | TField |  | Date from which the blockage is effective. If set up, the record will only concern investors where zero or null positions in a fund share class. Multifonds DB Column is EFF_DATE. |
| 7 | `FS.GI.FUND.SOFT.CLOSURES.MESSAGE` | `FsGiFundSoftClosures_Message` | TField |  | Message to be displayed when the blockage occurs. The available values are 0001-Soft/Hard closure - no investment allowed, 0003-Softclosure - no operations allowed at the moment etc., Multifonds DB Column is MESSAGE. |
| 8 | `FS.GI.FUND.SOFT.CLOSURES.INTERNAL.ID` | `FsGiFundSoftClosures_InternalId` | TField |  | Unique internal identifier of the soft closures record. Multifonds DB Column is INTERNAL_ID. |
| 9 | `FS.GI.FUND.SOFT.CLOSURES.FUND.ID` | `FsGiFundSoftClosures_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 10 | `FS.GI.FUND.SOFT.CLOSURES.CLASS.CURRENCY` | `FsGiFundSoftClosures_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 11 | `FS.GI.FUND.SOFT.CLOSURES.RESERVED10` | `FsGiFundSoftClosures_Reserved10` | TField |  |  |
| 12 | `FS.GI.FUND.SOFT.CLOSURES.RESERVED9` | `FsGiFundSoftClosures_Reserved9` | TField |  |  |
| 13 | `FS.GI.FUND.SOFT.CLOSURES.RESERVED8` | `FsGiFundSoftClosures_Reserved8` | TField |  |  |
| 14 | `FS.GI.FUND.SOFT.CLOSURES.RESERVED7` | `FsGiFundSoftClosures_Reserved7` | TField |  |  |
| 15 | `FS.GI.FUND.SOFT.CLOSURES.RESERVED6` | `FsGiFundSoftClosures_Reserved6` | TField |  |  |
| 16 | `FS.GI.FUND.SOFT.CLOSURES.RESERVED5` | `FsGiFundSoftClosures_Reserved5` | TField |  |  |
| 17 | `FS.GI.FUND.SOFT.CLOSURES.RESERVED4` | `FsGiFundSoftClosures_Reserved4` | TField |  |  |
| 18 | `FS.GI.FUND.SOFT.CLOSURES.RESERVED3` | `FsGiFundSoftClosures_Reserved3` | TField |  |  |
| 19 | `FS.GI.FUND.SOFT.CLOSURES.RESERVED2` | `FsGiFundSoftClosures_Reserved2` | TField |  |  |
| 20 | `FS.GI.FUND.SOFT.CLOSURES.RESERVED1` | `FsGiFundSoftClosures_Reserved1` | TField |  |  |
| 21 | `FS.GI.FUND.SOFT.CLOSURES.LOCAL.REF` | `FsGiFundSoftClosures_LocalRef` |  |  |  |
| 22 | `FS.GI.FUND.SOFT.CLOSURES.OVERRIDE` | `FsGiFundSoftClosures_Override` |  |  |  |
| 23 | `FS.GI.FUND.SOFT.CLOSURES.RECORD.STATUS` | `FsGiFundSoftClosures_RecordStatus` | String |  |  |
| 24 | `FS.GI.FUND.SOFT.CLOSURES.CURR.NO` | `FsGiFundSoftClosures_CurrNo` | String |  |  |
| 25 | `FS.GI.FUND.SOFT.CLOSURES.INPUTTER` | `FsGiFundSoftClosures_Inputter` |  |  |  |
| 26 | `FS.GI.FUND.SOFT.CLOSURES.DATE.TIME` | `FsGiFundSoftClosures_DateTime` |  |  |  |
| 27 | `FS.GI.FUND.SOFT.CLOSURES.AUTHORISER` | `FsGiFundSoftClosures_Authoriser` | String |  |  |
| 28 | `FS.GI.FUND.SOFT.CLOSURES.CO.CODE` | `FsGiFundSoftClosures_CoCode` | String |  |  |
| 29 | `FS.GI.FUND.SOFT.CLOSURES.DEPT.CODE` | `FsGiFundSoftClosures_DeptCode` | String |  |  |
| 30 | `FS.GI.FUND.SOFT.CLOSURES.AUDITOR.CODE` | `FsGiFundSoftClosures_AuditorCode` | String |  |  |
| 31 | `FS.GI.FUND.SOFT.CLOSURES.AUDIT.DATE.TIME` | `FsGiFundSoftClosures_AuditDateTime` | String |  |  |
