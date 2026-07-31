# FS.GI.APP.FUND.CLASS.EQUIVALENCE — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.FUND.CLASS.EQUIVALENCE` in `FS_FundStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.PARENT.REF.ID` | `FsGiAppFundClassEquivalence_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.ORA.ROWID` | `FsGiAppFundClassEquivalence_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.FOF.EXTERNAL.FUND.ID` | `FsGiAppFundClassEquivalence_FofExternalFundId` | TField |  | Fund external ID. Multifonds DB Column is NPTF_FOF_EXTERN. |
| 4 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.FOF.TA.FUND.ID` | `FsGiAppFundClassEquivalence_FofTaFundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF_FOF. |
| 5 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.FOF.SHARE.CLASS.CODE` | `FsGiAppFundClassEquivalence_FofShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART_FOF. |
| 6 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.FUND.ID` | `FsGiAppFundClassEquivalence_FundId` | TField |  | Fund is in scope for the document type. Multifonds DB Column is MULTIFONDS_ID. |
| 7 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.CLASS.CURRENCY` | `FsGiAppFundClassEquivalence_ClassCurrency` | TField |  | Fund Share Class Currency Multifonds DB Column is CLASS_CURRENCY. |
| 8 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.RESERVED10` | `FsGiAppFundClassEquivalence_Reserved10` | TField |  |  |
| 9 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.RESERVED9` | `FsGiAppFundClassEquivalence_Reserved9` | TField |  |  |
| 10 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.RESERVED8` | `FsGiAppFundClassEquivalence_Reserved8` | TField |  |  |
| 11 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.RESERVED7` | `FsGiAppFundClassEquivalence_Reserved7` | TField |  |  |
| 12 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.RESERVED6` | `FsGiAppFundClassEquivalence_Reserved6` | TField |  |  |
| 13 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.RESERVED5` | `FsGiAppFundClassEquivalence_Reserved5` | TField |  |  |
| 14 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.RESERVED4` | `FsGiAppFundClassEquivalence_Reserved4` | TField |  |  |
| 15 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.RESERVED3` | `FsGiAppFundClassEquivalence_Reserved3` | TField |  |  |
| 16 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.RESERVED2` | `FsGiAppFundClassEquivalence_Reserved2` | TField |  |  |
| 17 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.RESERVED1` | `FsGiAppFundClassEquivalence_Reserved1` | TField |  |  |
| 18 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.LOCAL.REF` | `FsGiAppFundClassEquivalence_LocalRef` |  |  |  |
| 19 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.OVERRIDE` | `FsGiAppFundClassEquivalence_Override` |  |  |  |
| 20 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.RECORD.STATUS` | `FsGiAppFundClassEquivalence_RecordStatus` | String |  |  |
| 21 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.CURR.NO` | `FsGiAppFundClassEquivalence_CurrNo` | String |  |  |
| 22 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.INPUTTER` | `FsGiAppFundClassEquivalence_Inputter` |  |  |  |
| 23 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.DATE.TIME` | `FsGiAppFundClassEquivalence_DateTime` |  |  |  |
| 24 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.AUTHORISER` | `FsGiAppFundClassEquivalence_Authoriser` | String |  |  |
| 25 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.CO.CODE` | `FsGiAppFundClassEquivalence_CoCode` | String |  |  |
| 26 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.DEPT.CODE` | `FsGiAppFundClassEquivalence_DeptCode` | String |  |  |
| 27 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.AUDITOR.CODE` | `FsGiAppFundClassEquivalence_AuditorCode` | String |  |  |
| 28 | `FS.GI.APP.FUND.CLASS.EQUIVALENCE.AUDIT.DATE.TIME` | `FsGiAppFundClassEquivalence_AuditDateTime` | String |  |  |
