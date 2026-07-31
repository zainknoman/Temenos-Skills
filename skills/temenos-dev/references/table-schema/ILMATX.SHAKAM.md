# ILMATX.SHAKAM — Table Schema

> Source: `INSERTS/I_F.ILMATX.SHAKAM` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ILMATX.SHAKAM.SECURITY.REF` | `IlmatxShakam_SecurityRef` | TField |  | This field is Security reference. |
| 2 | `ILMATX.SHAKAM.LAYER.TYPE` | `IlmatxShakam_LayerType` | TField |  | This field is Main investment category / Sub investment category. |
| 3 | `ILMATX.SHAKAM.LAYER.PROC.DATE` | `IlmatxShakam_LayerProcDate` | TField |  | This field is Processing date. |
| 4 | `ILMATX.SHAKAM.SHAKAM.RATE` | `IlmatxShakam_ShakamRate` | TField |  | This field is SHAKAM rate . |
| 5 | `ILMATX.SHAKAM.RESERVED.5` | `IlmatxShakam_Reserved5` | TField |  | Reserved for future use. |
| 6 | `ILMATX.SHAKAM.RESERVED.4` | `IlmatxShakam_Reserved4` | TField |  | Reserved for future use. |
| 7 | `ILMATX.SHAKAM.RESERVED.3` | `IlmatxShakam_Reserved3` | TField |  | Reserved for future use. |
| 8 | `ILMATX.SHAKAM.RESERVED.2` | `IlmatxShakam_Reserved2` | TField |  | Reserved for future use. |
| 9 | `ILMATX.SHAKAM.RESERVED.1` | `IlmatxShakam_Reserved1` | TField |  | Reserved for future use. |
| 10 | `ILMATX.SHAKAM.LOCAL.REF` | `IlmatxShakam_LocalRef` |  |  |  |
| 11 | `ILMATX.SHAKAM.OVERRIDE` | `IlmatxShakam_Override` |  |  |  |
| 12 | `ILMATX.SHAKAM.RECORD.STATUS` | `IlmatxShakam_RecordStatus` | String |  |  |
| 13 | `ILMATX.SHAKAM.CURR.NO` | `IlmatxShakam_CurrNo` | String |  |  |
| 14 | `ILMATX.SHAKAM.INPUTTER` | `IlmatxShakam_Inputter` |  |  |  |
| 15 | `ILMATX.SHAKAM.DATE.TIME` | `IlmatxShakam_DateTime` |  |  |  |
| 16 | `ILMATX.SHAKAM.AUTHORISER` | `IlmatxShakam_Authoriser` | String |  |  |
| 17 | `ILMATX.SHAKAM.CO.CODE` | `IlmatxShakam_CoCode` | String |  |  |
| 18 | `ILMATX.SHAKAM.DEPT.CODE` | `IlmatxShakam_DeptCode` | String |  |  |
| 19 | `ILMATX.SHAKAM.AUDITOR.CODE` | `IlmatxShakam_AuditorCode` | String |  |  |
| 20 | `ILMATX.SHAKAM.AUDIT.DATE.TIME` | `IlmatxShakam_AuditDateTime` | String |  |  |
