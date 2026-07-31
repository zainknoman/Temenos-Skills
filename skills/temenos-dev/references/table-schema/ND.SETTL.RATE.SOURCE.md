# ND.SETTL.RATE.SOURCE — Table Schema

> Source: `INSERTS/I_F.ND.SETTL.RATE.SOURCE` in `ND_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ND.SR.DESCRIPTION` | `NdSettlRateSource_Description` |  |  |  |
| 2 | `ND.SR.RESERVED.10` | `NdSettlRateSource_Reserved10` | TField |  |  |
| 3 | `ND.SR.RESERVED.9` | `NdSettlRateSource_Reserved9` | TField |  |  |
| 4 | `ND.SR.RESERVED.8` | `NdSettlRateSource_Reserved8` | TField |  |  |
| 5 | `ND.SR.RESERVED.7` | `NdSettlRateSource_Reserved7` | TField |  |  |
| 6 | `ND.SR.RESERVED.6` | `NdSettlRateSource_Reserved6` | TField |  |  |
| 7 | `ND.SR.RESERVED.5` | `NdSettlRateSource_Reserved5` | TField |  |  |
| 8 | `ND.SR.RESERVED.4` | `NdSettlRateSource_Reserved4` | TField |  |  |
| 9 | `ND.SR.RESERVED.3` | `NdSettlRateSource_Reserved3` | TField |  |  |
| 10 | `ND.SR.RESERVED.2` | `NdSettlRateSource_Reserved2` | TField |  |  |
| 11 | `ND.SR.RESERVED.1` | `NdSettlRateSource_Reserved1` | TField |  |  |
| 12 | `ND.SR.LOCAL.REF` | `NdSettlRateSource_LocalRef` |  |  |  |
| 13 | `ND.SR.OVERRIDE` | `NdSettlRateSource_Override` |  |  |  |
| 14 | `ND.SR.RECORD.STATUS` | `NdSettlRateSource_RecordStatus` | String |  |  |
| 15 | `ND.SR.CURR.NO` | `NdSettlRateSource_CurrNo` | String |  |  |
| 16 | `ND.SR.INPUTTER` | `NdSettlRateSource_Inputter` |  |  |  |
| 17 | `ND.SR.DATE.TIME` | `NdSettlRateSource_DateTime` |  |  |  |
| 18 | `ND.SR.AUTHORISER` | `NdSettlRateSource_Authoriser` | String |  |  |
| 19 | `ND.SR.CO.CODE` | `NdSettlRateSource_CoCode` | String |  |  |
| 20 | `ND.SR.DEPT.CODE` | `NdSettlRateSource_DeptCode` | String |  |  |
| 21 | `ND.SR.AUDITOR.CODE` | `NdSettlRateSource_AuditorCode` | String |  |  |
| 22 | `ND.SR.AUDIT.DATE.TIME` | `NdSettlRateSource_AuditDateTime` | String |  |  |
