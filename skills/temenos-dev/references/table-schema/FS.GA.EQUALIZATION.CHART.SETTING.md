# FS.GA.EQUALIZATION.CHART.SETTING — Table Schema

> Source: `INSERTS/I_F.FS.GA.EQUALIZATION.CHART.SETTING` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.EQUALIZATION.CHART.SETTING.PARENT.REF.ID` | `FsGaEqualizationChartSetting_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.EQUALIZATION.CHART.SETTING.ORA.ROWID` | `FsGaEqualizationChartSetting_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.EQUALIZATION.CHART.SETTING.FUND.ID` | `FsGaEqualizationChartSetting_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.EQUALIZATION.CHART.SETTING.GL.ACCOUNT` | `FsGaEqualizationChartSetting_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 5 | `FS.GA.EQUALIZATION.CHART.SETTING.EQUALISATION.GROUPS` | `FsGaEqualizationChartSetting_EqualisationGroups` | TField |  | Standard equalization group as defined in the account links on chart level. Multifonds DB Column is CTIF_REGUL. |
| 6 | `FS.GA.EQUALIZATION.CHART.SETTING.COUNTRY.CODE1` | `FsGaEqualizationChartSetting_CountryCode1` | TField |  | User can enter the equalization account groups for the respective country code(s), Multifonds supports up to 10 different equalization tables depending on the countries. Multifonds DB Column is CTIF_REGUL_CPAYS_1. |
| 7 | `FS.GA.EQUALIZATION.CHART.SETTING.COUNTRY.CODE2` | `FsGaEqualizationChartSetting_CountryCode2` | TField |  | User can enter the equalization account groups for the respective country code(s), Multifonds supports up to 10 different equalization tables depending on the countries. Multifonds DB Column is CTIF_REGUL_CPAYS_2. |
| 8 | `FS.GA.EQUALIZATION.CHART.SETTING.COUNTRY.CODE3` | `FsGaEqualizationChartSetting_CountryCode3` | TField |  | User can enter the equalization account groups for the respective country code(s), Multifonds supports up to 10 different equalization tables depending on the countries. Multifonds DB Column is CTIF_REGUL_CPAYS_3. |
| 9 | `FS.GA.EQUALIZATION.CHART.SETTING.COUNTRY.CODE4` | `FsGaEqualizationChartSetting_CountryCode4` | TField |  | User can enter the equalization account groups for the respective country code(s), Multifonds supports up to 10 different equalization tables depending on the countries. Multifonds DB Column is CTIF_REGUL_CPAYS_4. |
| 10 | `FS.GA.EQUALIZATION.CHART.SETTING.COUNTRY.CODE5` | `FsGaEqualizationChartSetting_CountryCode5` | TField |  | User can enter the equalization account groups for the respective country code(s), Multifonds supports up to 10 different equalization tables depending on the countries. Multifonds DB Column is CTIF_REGUL_CPAYS_5. |
| 11 | `FS.GA.EQUALIZATION.CHART.SETTING.COUNTRY.CODE6` | `FsGaEqualizationChartSetting_CountryCode6` | TField |  | User can enter the equalization account groups for the respective country code(s), Multifonds supports up to 10 different equalization tables depending on the countries. Multifonds DB Column is CTIF_REGUL_CPAYS_6. |
| 12 | `FS.GA.EQUALIZATION.CHART.SETTING.COUNTRY.CODE7` | `FsGaEqualizationChartSetting_CountryCode7` | TField |  | User can enter the equalization account groups for the respective country code(s), Multifonds supports up to 10 different equalization tables depending on the countries. Multifonds DB Column is CTIF_REGUL_CPAYS_7. |
| 13 | `FS.GA.EQUALIZATION.CHART.SETTING.COUNTRY.CODE8` | `FsGaEqualizationChartSetting_CountryCode8` | TField |  | User can enter the equalization account groups for the respective country code(s), Multifonds supports up to 10 different equalization tables depending on the countries. Multifonds DB Column is CTIF_REGUL_CPAYS_8. |
| 14 | `FS.GA.EQUALIZATION.CHART.SETTING.COUNTRY.CODE9` | `FsGaEqualizationChartSetting_CountryCode9` | TField |  | User can enter the equalization account groups for the respective country code(s), Multifonds supports up to 10 different equalization tables depending on the countries. Multifonds DB Column is CTIF_REGUL_CPAYS_9. |
| 15 | `FS.GA.EQUALIZATION.CHART.SETTING.COUNTRY.CODE10` | `FsGaEqualizationChartSetting_CountryCode10` | TField |  | User can enter the equalization account groups for the respective country code(s), Multifonds supports up to 10 different equalization tables depending on the countries. Multifonds DB Column is CTIF_REGUL_CPAYS_10. |
| 16 | `FS.GA.EQUALIZATION.CHART.SETTING.RESERVED10` | `FsGaEqualizationChartSetting_Reserved10` | TField |  |  |
| 17 | `FS.GA.EQUALIZATION.CHART.SETTING.RESERVED9` | `FsGaEqualizationChartSetting_Reserved9` | TField |  |  |
| 18 | `FS.GA.EQUALIZATION.CHART.SETTING.RESERVED8` | `FsGaEqualizationChartSetting_Reserved8` | TField |  |  |
| 19 | `FS.GA.EQUALIZATION.CHART.SETTING.RESERVED7` | `FsGaEqualizationChartSetting_Reserved7` | TField |  |  |
| 20 | `FS.GA.EQUALIZATION.CHART.SETTING.RESERVED6` | `FsGaEqualizationChartSetting_Reserved6` | TField |  |  |
| 21 | `FS.GA.EQUALIZATION.CHART.SETTING.RESERVED5` | `FsGaEqualizationChartSetting_Reserved5` | TField |  |  |
| 22 | `FS.GA.EQUALIZATION.CHART.SETTING.RESERVED4` | `FsGaEqualizationChartSetting_Reserved4` | TField |  |  |
| 23 | `FS.GA.EQUALIZATION.CHART.SETTING.RESERVED3` | `FsGaEqualizationChartSetting_Reserved3` | TField |  |  |
| 24 | `FS.GA.EQUALIZATION.CHART.SETTING.RESERVED2` | `FsGaEqualizationChartSetting_Reserved2` | TField |  |  |
| 25 | `FS.GA.EQUALIZATION.CHART.SETTING.RESERVED1` | `FsGaEqualizationChartSetting_Reserved1` | TField |  |  |
| 26 | `FS.GA.EQUALIZATION.CHART.SETTING.LOCAL.REF` | `FsGaEqualizationChartSetting_LocalRef` |  |  |  |
| 27 | `FS.GA.EQUALIZATION.CHART.SETTING.OVERRIDE` | `FsGaEqualizationChartSetting_Override` |  |  |  |
| 28 | `FS.GA.EQUALIZATION.CHART.SETTING.RECORD.STATUS` | `FsGaEqualizationChartSetting_RecordStatus` | String |  |  |
| 29 | `FS.GA.EQUALIZATION.CHART.SETTING.CURR.NO` | `FsGaEqualizationChartSetting_CurrNo` | String |  |  |
| 30 | `FS.GA.EQUALIZATION.CHART.SETTING.INPUTTER` | `FsGaEqualizationChartSetting_Inputter` |  |  |  |
| 31 | `FS.GA.EQUALIZATION.CHART.SETTING.DATE.TIME` | `FsGaEqualizationChartSetting_DateTime` |  |  |  |
| 32 | `FS.GA.EQUALIZATION.CHART.SETTING.AUTHORISER` | `FsGaEqualizationChartSetting_Authoriser` | String |  |  |
| 33 | `FS.GA.EQUALIZATION.CHART.SETTING.CO.CODE` | `FsGaEqualizationChartSetting_CoCode` | String |  |  |
| 34 | `FS.GA.EQUALIZATION.CHART.SETTING.DEPT.CODE` | `FsGaEqualizationChartSetting_DeptCode` | String |  |  |
| 35 | `FS.GA.EQUALIZATION.CHART.SETTING.AUDITOR.CODE` | `FsGaEqualizationChartSetting_AuditorCode` | String |  |  |
| 36 | `FS.GA.EQUALIZATION.CHART.SETTING.AUDIT.DATE.TIME` | `FsGaEqualizationChartSetting_AuditDateTime` | String |  |  |
