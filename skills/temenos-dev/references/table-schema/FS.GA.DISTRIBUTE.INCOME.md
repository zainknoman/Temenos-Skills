# FS.GA.DISTRIBUTE.INCOME — Table Schema

> Source: `INSERTS/I_F.FS.GA.DISTRIBUTE.INCOME` in `FS_IncomeCorporateAction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.DISTRIBUTE.INCOME.FUND.ID` | `FsGaDistributeIncome_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.DISTRIBUTE.INCOME.EQUALIZATION.COUNTRY` | `FsGaDistributeIncome_EqualizationCountry` | TField |  | This field is to define country code which is applicable for equalization calculation. Multifonds DB Column is CPAYS_EGA. |
| 3 | `FS.GA.DISTRIBUTE.INCOME.DISTRIBUTION.PERCENTAGE` | `FsGaDistributeIncome_DistributionPercentage` | TField |  | This field displays distribution percentage for the given country code Multifonds DB Column is DIST_PCT. |
| 4 | `FS.GA.DISTRIBUTE.INCOME.RESERVED10` | `FsGaDistributeIncome_Reserved10` | TField |  |  |
| 5 | `FS.GA.DISTRIBUTE.INCOME.RESERVED9` | `FsGaDistributeIncome_Reserved9` | TField |  |  |
| 6 | `FS.GA.DISTRIBUTE.INCOME.RESERVED8` | `FsGaDistributeIncome_Reserved8` | TField |  |  |
| 7 | `FS.GA.DISTRIBUTE.INCOME.RESERVED7` | `FsGaDistributeIncome_Reserved7` | TField |  |  |
| 8 | `FS.GA.DISTRIBUTE.INCOME.RESERVED6` | `FsGaDistributeIncome_Reserved6` | TField |  |  |
| 9 | `FS.GA.DISTRIBUTE.INCOME.RESERVED5` | `FsGaDistributeIncome_Reserved5` | TField |  |  |
| 10 | `FS.GA.DISTRIBUTE.INCOME.RESERVED4` | `FsGaDistributeIncome_Reserved4` | TField |  |  |
| 11 | `FS.GA.DISTRIBUTE.INCOME.RESERVED3` | `FsGaDistributeIncome_Reserved3` | TField |  |  |
| 12 | `FS.GA.DISTRIBUTE.INCOME.RESERVED2` | `FsGaDistributeIncome_Reserved2` | TField |  |  |
| 13 | `FS.GA.DISTRIBUTE.INCOME.RESERVED1` | `FsGaDistributeIncome_Reserved1` | TField |  |  |
| 14 | `FS.GA.DISTRIBUTE.INCOME.RECORD.STATUS` | `FsGaDistributeIncome_RecordStatus` | String |  |  |
| 15 | `FS.GA.DISTRIBUTE.INCOME.CURR.NO` | `FsGaDistributeIncome_CurrNo` | String |  |  |
| 16 | `FS.GA.DISTRIBUTE.INCOME.INPUTTER` | `FsGaDistributeIncome_Inputter` |  |  |  |
| 17 | `FS.GA.DISTRIBUTE.INCOME.DATE.TIME` | `FsGaDistributeIncome_DateTime` |  |  |  |
| 18 | `FS.GA.DISTRIBUTE.INCOME.AUTHORISER` | `FsGaDistributeIncome_Authoriser` | String |  |  |
| 19 | `FS.GA.DISTRIBUTE.INCOME.CO.CODE` | `FsGaDistributeIncome_CoCode` | String |  |  |
| 20 | `FS.GA.DISTRIBUTE.INCOME.DEPT.CODE` | `FsGaDistributeIncome_DeptCode` | String |  |  |
| 21 | `FS.GA.DISTRIBUTE.INCOME.AUDITOR.CODE` | `FsGaDistributeIncome_AuditorCode` | String |  |  |
| 22 | `FS.GA.DISTRIBUTE.INCOME.AUDIT.DATE.TIME` | `FsGaDistributeIncome_AuditDateTime` | String |  |  |
