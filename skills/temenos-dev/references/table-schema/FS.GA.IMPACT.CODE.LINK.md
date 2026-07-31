# FS.GA.IMPACT.CODE.LINK — Table Schema

> Source: `INSERTS/I_F.FS.GA.IMPACT.CODE.LINK` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.IMPACT.CODE.LINK.CHART.OF.ACCOUNTS.CODE` | `FsGaImpactCodeLink_ChartOfAccountsCode` | TField |  | This is the chart of accounts number. Multifonds DB Column is CPDC. |
| 2 | `FS.GA.IMPACT.CODE.LINK.IMPACT.CODE` | `FsGaImpactCodeLink_ImpactCode` | TField |  | Refers to the two types of impact code 1. Spec. Expense Impact 2. Hedging impact Multifonds DB Column is IMPACT_CODE. |
| 3 | `FS.GA.IMPACT.CODE.LINK.GL.ACCOUNT` | `FsGaImpactCodeLink_GlAccount` | TField |  | Cash Account Number Multifonds DB Column is NRUBR. |
| 4 | `FS.GA.IMPACT.CODE.LINK.UPDATED.DATE` | `FsGaImpactCodeLink_UpdatedDate` | TField |  | Updated Date Multifonds DB Column is DUPDATE. |
| 5 | `FS.GA.IMPACT.CODE.LINK.FUND.ID` | `FsGaImpactCodeLink_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 6 | `FS.GA.IMPACT.CODE.LINK.RESERVED10` | `FsGaImpactCodeLink_Reserved10` | TField |  |  |
| 7 | `FS.GA.IMPACT.CODE.LINK.RESERVED9` | `FsGaImpactCodeLink_Reserved9` | TField |  |  |
| 8 | `FS.GA.IMPACT.CODE.LINK.RESERVED8` | `FsGaImpactCodeLink_Reserved8` | TField |  |  |
| 9 | `FS.GA.IMPACT.CODE.LINK.RESERVED7` | `FsGaImpactCodeLink_Reserved7` | TField |  |  |
| 10 | `FS.GA.IMPACT.CODE.LINK.RESERVED6` | `FsGaImpactCodeLink_Reserved6` | TField |  |  |
| 11 | `FS.GA.IMPACT.CODE.LINK.RESERVED5` | `FsGaImpactCodeLink_Reserved5` | TField |  |  |
| 12 | `FS.GA.IMPACT.CODE.LINK.RESERVED4` | `FsGaImpactCodeLink_Reserved4` | TField |  |  |
| 13 | `FS.GA.IMPACT.CODE.LINK.RESERVED3` | `FsGaImpactCodeLink_Reserved3` | TField |  |  |
| 14 | `FS.GA.IMPACT.CODE.LINK.RESERVED2` | `FsGaImpactCodeLink_Reserved2` | TField |  |  |
| 15 | `FS.GA.IMPACT.CODE.LINK.RESERVED1` | `FsGaImpactCodeLink_Reserved1` | TField |  |  |
| 16 | `FS.GA.IMPACT.CODE.LINK.RECORD.STATUS` | `FsGaImpactCodeLink_RecordStatus` | String |  |  |
| 17 | `FS.GA.IMPACT.CODE.LINK.CURR.NO` | `FsGaImpactCodeLink_CurrNo` | String |  |  |
| 18 | `FS.GA.IMPACT.CODE.LINK.INPUTTER` | `FsGaImpactCodeLink_Inputter` |  |  |  |
| 19 | `FS.GA.IMPACT.CODE.LINK.DATE.TIME` | `FsGaImpactCodeLink_DateTime` |  |  |  |
| 20 | `FS.GA.IMPACT.CODE.LINK.AUTHORISER` | `FsGaImpactCodeLink_Authoriser` | String |  |  |
| 21 | `FS.GA.IMPACT.CODE.LINK.CO.CODE` | `FsGaImpactCodeLink_CoCode` | String |  |  |
| 22 | `FS.GA.IMPACT.CODE.LINK.DEPT.CODE` | `FsGaImpactCodeLink_DeptCode` | String |  |  |
| 23 | `FS.GA.IMPACT.CODE.LINK.AUDITOR.CODE` | `FsGaImpactCodeLink_AuditorCode` | String |  |  |
| 24 | `FS.GA.IMPACT.CODE.LINK.AUDIT.DATE.TIME` | `FsGaImpactCodeLink_AuditDateTime` | String |  |  |
