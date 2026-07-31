# HKDEPO.PARAMETER — Table Schema

> Source: `INSERTS/I_F.HKDEPO.PARAMETER` in `HKDEPO_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HKDEPO.PARAM.CAMPAIGN.PRODUCT` | `HkdepoParameter_CampaignProduct` | TField |  | Will hold valid Product group for Campaign deposits. |
| 2 | `HKDEPO.PARAM.LOCAL.REF` | `HkdepoParameter_LocalRef` |  |  |  |
| 3 | `HKDEPO.PARAM.RESERVED.1` | `HkdepoParameter_Reserved1` |  |  |  |
| 4 | `HKDEPO.PARAM.RESERVED.2` | `HkdepoParameter_Reserved2` |  |  |  |
| 5 | `HKDEPO.PARAM.RESERVED.3` | `HkdepoParameter_Reserved3` |  |  |  |
| 6 | `HKDEPO.PARAM.RESERVED.4` | `HkdepoParameter_Reserved4` |  |  |  |
| 7 | `HKDEPO.PARAM.RESERVED.5` | `HkdepoParameter_Reserved5` |  |  |  |
| 8 | `HKDEPO.PARAM.RESERVED.6` | `HkdepoParameter_Reserved6` |  |  |  |
| 9 | `HKDEPO.PARAM.RESERVED.7` | `HkdepoParameter_Reserved7` |  |  |  |
| 10 | `HKDEPO.PARAM.RESERVED.8` | `HkdepoParameter_Reserved8` | TField |  |  |
| 11 | `HKDEPO.PARAM.RESERVED.9` | `HkdepoParameter_Reserved9` | TField |  |  |
| 12 | `HKDEPO.PARAM.RESERVED.10` | `HkdepoParameter_Reserved10` | TField |  |  |
| 13 | `HKDEPO.PARAM.OVERRIDE` | `HkdepoParameter_Override` |  |  |  |
| 14 | `HKDEPO.PARAM.RECORD.STATUS` | `HkdepoParameter_RecordStatus` | String |  |  |
| 15 | `HKDEPO.PARAM.CURR.NO` | `HkdepoParameter_CurrNo` | String |  |  |
| 16 | `HKDEPO.PARAM.INPUTTER` | `HkdepoParameter_Inputter` |  |  |  |
| 17 | `HKDEPO.PARAM.DATE.TIME` | `HkdepoParameter_DateTime` |  |  |  |
| 18 | `HKDEPO.PARAM.AUTHORISER` | `HkdepoParameter_Authoriser` | String |  |  |
| 19 | `HKDEPO.PARAM.CO.CODE` | `HkdepoParameter_CoCode` | String |  |  |
| 20 | `HKDEPO.PARAM.DEPT.CODE` | `HkdepoParameter_DeptCode` | String |  |  |
| 21 | `HKDEPO.PARAM.AUDITOR.CODE` | `HkdepoParameter_AuditorCode` | String |  |  |
| 22 | `HKDEPO.PARAM.AUDIT.DATE.TIME` | `HkdepoParameter_AuditDateTime` | String |  |  |
