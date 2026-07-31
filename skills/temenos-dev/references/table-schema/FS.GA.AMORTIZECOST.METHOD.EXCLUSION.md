# FS.GA.AMORTIZECOST.METHOD.EXCLUSION — Table Schema

> Source: `INSERTS/I_F.FS.GA.AMORTIZECOST.METHOD.EXCLUSION` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.PARENT.REF.ID` | `FsGaAmortizecostMethodExclusion_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.ORA.ROWID` | `FsGaAmortizecostMethodExclusion_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.FUND.ID` | `FsGaAmortizecostMethodExclusion_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.INTERNAL.SECURITY.ID` | `FsGaAmortizecostMethodExclusion_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 5 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.GTI.CODE` | `FsGaAmortizecostMethodExclusion_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 6 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.AMORTISATION.COST.EXCLUSION` | `FsGaAmortizecostMethodExclusion_AmortisationCostExclusion` | TField |  | Cost Exclude Identifier Multifonds DB Column is FLG_AC_EXCLUDE. |
| 7 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.RESERVED10` | `FsGaAmortizecostMethodExclusion_Reserved10` | TField |  |  |
| 8 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.RESERVED9` | `FsGaAmortizecostMethodExclusion_Reserved9` | TField |  |  |
| 9 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.RESERVED8` | `FsGaAmortizecostMethodExclusion_Reserved8` | TField |  |  |
| 10 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.RESERVED7` | `FsGaAmortizecostMethodExclusion_Reserved7` | TField |  |  |
| 11 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.RESERVED6` | `FsGaAmortizecostMethodExclusion_Reserved6` | TField |  |  |
| 12 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.RESERVED5` | `FsGaAmortizecostMethodExclusion_Reserved5` | TField |  |  |
| 13 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.RESERVED4` | `FsGaAmortizecostMethodExclusion_Reserved4` | TField |  |  |
| 14 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.RESERVED3` | `FsGaAmortizecostMethodExclusion_Reserved3` | TField |  |  |
| 15 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.RESERVED2` | `FsGaAmortizecostMethodExclusion_Reserved2` | TField |  |  |
| 16 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.RESERVED1` | `FsGaAmortizecostMethodExclusion_Reserved1` | TField |  |  |
| 17 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.LOCAL.REF` | `FsGaAmortizecostMethodExclusion_LocalRef` |  |  |  |
| 18 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.OVERRIDE` | `FsGaAmortizecostMethodExclusion_Override` |  |  |  |
| 19 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.RECORD.STATUS` | `FsGaAmortizecostMethodExclusion_RecordStatus` | String |  |  |
| 20 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.CURR.NO` | `FsGaAmortizecostMethodExclusion_CurrNo` | String |  |  |
| 21 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.INPUTTER` | `FsGaAmortizecostMethodExclusion_Inputter` |  |  |  |
| 22 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.DATE.TIME` | `FsGaAmortizecostMethodExclusion_DateTime` |  |  |  |
| 23 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.AUTHORISER` | `FsGaAmortizecostMethodExclusion_Authoriser` | String |  |  |
| 24 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.CO.CODE` | `FsGaAmortizecostMethodExclusion_CoCode` | String |  |  |
| 25 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.DEPT.CODE` | `FsGaAmortizecostMethodExclusion_DeptCode` | String |  |  |
| 26 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.AUDITOR.CODE` | `FsGaAmortizecostMethodExclusion_AuditorCode` | String |  |  |
| 27 | `FS.GA.AMORTIZECOST.METHOD.EXCLUSION.AUDIT.DATE.TIME` | `FsGaAmortizecostMethodExclusion_AuditDateTime` | String |  |  |
