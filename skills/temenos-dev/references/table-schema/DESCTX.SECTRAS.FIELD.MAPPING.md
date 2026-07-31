# DESCTX.SECTRAS.FIELD.MAPPING — Table Schema

> Source: `INSERTS/I_F.DESCTX.SECTRAS.FIELD.MAPPING` in `DESCTX_Taxation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SECTRAS.MAPPING.SECTRAS.ATTRIBUTE.NAME` | `DesctxSectrasFieldMapping_SectrasAttributeName` |  |  |  |
| 2 | `SECTRAS.MAPPING.T24.FIELD.VALUE` | `DesctxSectrasFieldMapping_T24FieldValue` |  |  |  |
| 3 | `SECTRAS.MAPPING.SECTRAS.FIELD.VALUE` | `DesctxSectrasFieldMapping_SectrasFieldValue` |  |  |  |
| 4 | `SECTRAS.MAPPING.LOCAL.REF` | `DesctxSectrasFieldMapping_LocalRef` |  |  |  |
| 5 | `SECTRAS.MAPPING.RESERVED.8` | `DesctxSectrasFieldMapping_Reserved8` | TField |  |  |
| 6 | `SECTRAS.MAPPING.RESERVED.7` | `DesctxSectrasFieldMapping_Reserved7` | TField |  |  |
| 7 | `SECTRAS.MAPPING.RESERVED.6` | `DesctxSectrasFieldMapping_Reserved6` | TField |  |  |
| 8 | `SECTRAS.MAPPING.RESERVED.5` | `DesctxSectrasFieldMapping_Reserved5` | TField |  |  |
| 9 | `SECTRAS.MAPPING.RESERVED.4` | `DesctxSectrasFieldMapping_Reserved4` | TField |  |  |
| 10 | `SECTRAS.MAPPING.RESERVED.3` | `DesctxSectrasFieldMapping_Reserved3` | TField |  |  |
| 11 | `SECTRAS.MAPPING.RESERVED.2` | `DesctxSectrasFieldMapping_Reserved2` | TField |  |  |
| 12 | `SECTRAS.MAPPING.RESERVED.1` | `DesctxSectrasFieldMapping_Reserved1` | TField |  |  |
| 13 | `SECTRAS.MAPPING.OVERRIDE` | `DesctxSectrasFieldMapping_Override` |  |  |  |
| 14 | `SECTRAS.MAPPING.RECORD.STATUS` | `DesctxSectrasFieldMapping_RecordStatus` | String |  |  |
| 15 | `SECTRAS.MAPPING.CURR.NO` | `DesctxSectrasFieldMapping_CurrNo` | String |  |  |
| 16 | `SECTRAS.MAPPING.INPUTTER` | `DesctxSectrasFieldMapping_Inputter` |  |  |  |
| 17 | `SECTRAS.MAPPING.DATE.TIME` | `DesctxSectrasFieldMapping_DateTime` |  |  |  |
| 18 | `SECTRAS.MAPPING.AUTHORISER` | `DesctxSectrasFieldMapping_Authoriser` | String |  |  |
| 19 | `SECTRAS.MAPPING.CO.CODE` | `DesctxSectrasFieldMapping_CoCode` | String |  |  |
| 20 | `SECTRAS.MAPPING.DEPT.CODE` | `DesctxSectrasFieldMapping_DeptCode` | String |  |  |
| 21 | `SECTRAS.MAPPING.AUDITOR.CODE` | `DesctxSectrasFieldMapping_AuditorCode` | String |  |  |
| 22 | `SECTRAS.MAPPING.AUDIT.DATE.TIME` | `DesctxSectrasFieldMapping_AuditDateTime` | String |  |  |
