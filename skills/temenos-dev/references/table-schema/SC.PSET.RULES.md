# SC.PSET.RULES — Table Schema

> Source: `INSERTS/I_F.SC.PSET.RULES` in `SC_SctTrading.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PSR.CLEARING.CODE` | `ScPsetRules_ClearingCode` | TField |  | This Field will be defaulted from ID It is a NO INPUT field This field is not applicable when PSET.RULES.DIRECT is set to Yes in SC.SSI.PARAM |
| 2 | `SC.PSR.COUNTRY.CODE` | `ScPsetRules_CountryCode` |  |  |  |
| 3 | `SC.PSR.ASSET.TYPE` | `ScPsetRules_AssetType` |  |  |  |
| 4 | `SC.PSR.SUB.ASSET.TYPE` | `ScPsetRules_SubAssetType` |  |  |  |
| 5 | `SC.PSR.PSET` | `ScPsetRules_Pset` |  |  |  |
| 6 | `SC.PSR.RESERVED.10` | `ScPsetRules_Reserved10` |  |  |  |
| 7 | `SC.PSR.RESERVED.9` | `ScPsetRules_Reserved9` |  |  |  |
| 8 | `SC.PSR.RESERVED.8` | `ScPsetRules_Reserved8` |  |  |  |
| 9 | `SC.PSR.RESERVED.7` | `ScPsetRules_Reserved7` |  |  |  |
| 10 | `SC.PSR.RESERVED.6` | `ScPsetRules_Reserved6` |  |  |  |
| 11 | `SC.PSR.RESERVED.5` | `ScPsetRules_Reserved5` |  |  |  |
| 12 | `SC.PSR.RESERVED.4` | `ScPsetRules_Reserved4` |  |  |  |
| 13 | `SC.PSR.RESERVED.3` | `ScPsetRules_Reserved3` |  |  |  |
| 14 | `SC.PSR.RESERVED.2` | `ScPsetRules_Reserved2` |  |  |  |
| 15 | `SC.PSR.RESERVED.1` | `ScPsetRules_Reserved1` |  |  |  |
| 16 | `SC.PSR.LOCAL.REF` | `ScPsetRules_LocalRef` |  |  |  |
| 17 | `SC.PSR.OVERRIDE` | `ScPsetRules_Override` |  |  |  |
| 18 | `SC.PSR.RECORD.STATUS` | `ScPsetRules_RecordStatus` | String |  |  |
| 19 | `SC.PSR.CURR.NO` | `ScPsetRules_CurrNo` | String |  |  |
| 20 | `SC.PSR.INPUTTER` | `ScPsetRules_Inputter` |  |  |  |
| 21 | `SC.PSR.DATE.TIME` | `ScPsetRules_DateTime` |  |  |  |
| 22 | `SC.PSR.AUTHORISER` | `ScPsetRules_Authoriser` | String |  |  |
| 23 | `SC.PSR.CO.CODE` | `ScPsetRules_CoCode` | String |  |  |
| 24 | `SC.PSR.DEPT.CODE` | `ScPsetRules_DeptCode` | String |  |  |
| 25 | `SC.PSR.AUDITOR.CODE` | `ScPsetRules_AuditorCode` | String |  |  |
| 26 | `SC.PSR.AUDIT.DATE.TIME` | `ScPsetRules_AuditDateTime` | String |  |  |
