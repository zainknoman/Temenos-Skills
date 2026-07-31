# USRETL.AUDIT.REPORT — Table Schema

> Source: `INSERTS/I_F.USRETL.AUDIT.REPORT` in `USRETL_AuditReport.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AUDIT.RPT.DESCRIPTION` | `UsretlAuditReport_Description` |  |  |  |
| 2 | `AUDIT.RPT.ARR.ENQUIRY` | `UsretlAuditReport_ArrEnquiry` | TField |  | User must select YES or NO from a Check box. This selection determines if the inquiry is for an arrangement by selecting, or another application. |
| 3 | `AUDIT.RPT.APPLICATION` | `UsretlAuditReport_Application` | TField |  | A valid t24 Application must be entered, and which the inquiry must run against. |
| 4 | `AUDIT.RPT.PRODUCT.LINE` | `UsretlAuditReport_ProductLine` | TField |  | A valid Product Line must be entered and is the sole Product Line that the inquiry must run against. |
| 5 | `AUDIT.RPT.PROPERTY.CLASS` | `UsretlAuditReport_PropertyClass` |  |  |  |
| 6 | `AUDIT.RPT.AA.PRIMARY.FIELD` | `UsretlAuditReport_AaPrimaryField` |  |  |  |
| 7 | `AUDIT.RPT.AA.PRIM.LINK.DESC` | `UsretlAuditReport_AaPrimLinkDesc` |  |  |  |
| 8 | `AUDIT.RPT.AA.PRIM.FLD.LABEL` | `UsretlAuditReport_AaPrimFldLabel` |  |  |  |
| 9 | `AUDIT.RPT.RESERVED.20` | `UsretlAuditReport_Reserved20` | TField |  |  |
| 10 | `AUDIT.RPT.RESERVED.19` | `UsretlAuditReport_Reserved19` | TField |  |  |
| 11 | `AUDIT.RPT.RESERVED.18` | `UsretlAuditReport_Reserved18` | TField |  |  |
| 12 | `AUDIT.RPT.RESERVED.17` | `UsretlAuditReport_Reserved17` | TField |  |  |
| 13 | `AUDIT.RPT.PRIMARY.FIELD` | `UsretlAuditReport_PrimaryField` |  |  |  |
| 14 | `AUDIT.RPT.PRIM.LINK.DESC` | `UsretlAuditReport_PrimLinkDesc` |  |  |  |
| 15 | `AUDIT.RPT.PRIMFIELD.LABEL` | `UsretlAuditReport_PrimfieldLabel` |  |  |  |
| 16 | `AUDIT.RPT.RESERVED.16` | `UsretlAuditReport_Reserved16` | TField |  |  |
| 17 | `AUDIT.RPT.RESERVED.15` | `UsretlAuditReport_Reserved15` | TField |  |  |
| 18 | `AUDIT.RPT.SECONDARY.FIELD` | `UsretlAuditReport_SecondaryField` |  |  |  |
| 19 | `AUDIT.RPT.SECOND.LINK.DESC` | `UsretlAuditReport_SecondLinkDesc` |  |  |  |
| 20 | `AUDIT.RPT.SECOND.FIELD.LABEL` | `UsretlAuditReport_SecondFieldLabel` |  |  |  |
| 21 | `AUDIT.RPT.ALL.PROPERTY.CLASS` | `UsretlAuditReport_AllPropertyClass` | TField |  | This field used to indicate that the report should show audit history of all property class for arrangement account. When this field flaged as YES then property class and primary fields will be used only to extract field label and linked values. The search will not be based on given property class and changes on primary field. |
| 22 | `AUDIT.RPT.RESERVED.13` | `UsretlAuditReport_Reserved13` | TField |  |  |
| 23 | `AUDIT.RPT.RESERVED.12` | `UsretlAuditReport_Reserved12` | TField |  |  |
| 24 | `AUDIT.RPT.RESERVED.11` | `UsretlAuditReport_Reserved11` | TField |  |  |
| 25 | `AUDIT.RPT.RESERVED.10` | `UsretlAuditReport_Reserved10` | TField |  |  |
| 26 | `AUDIT.RPT.RESERVED.9` | `UsretlAuditReport_Reserved9` | TField |  |  |
| 27 | `AUDIT.RPT.RESERVED.8` | `UsretlAuditReport_Reserved8` | TField |  |  |
| 28 | `AUDIT.RPT.RESERVED.7` | `UsretlAuditReport_Reserved7` | TField |  |  |
| 29 | `AUDIT.RPT.RESERVED.6` | `UsretlAuditReport_Reserved6` | TField |  |  |
| 30 | `AUDIT.RPT.RESERVED.5` | `UsretlAuditReport_Reserved5` | TField |  |  |
| 31 | `AUDIT.RPT.RESERVED.4` | `UsretlAuditReport_Reserved4` | TField |  |  |
| 32 | `AUDIT.RPT.RESERVED.3` | `UsretlAuditReport_Reserved3` | TField |  |  |
| 33 | `AUDIT.RPT.RESERVED.2` | `UsretlAuditReport_Reserved2` | TField |  |  |
| 34 | `AUDIT.RPT.RESERVED.1` | `UsretlAuditReport_Reserved1` | TField |  |  |
| 35 | `AUDIT.RPT.LOCAL.REF` | `UsretlAuditReport_LocalRef` |  |  |  |
| 36 | `AUDIT.RPT.OVERRIDE` | `UsretlAuditReport_Override` |  |  |  |
| 37 | `AUDIT.RPT.RECORD.STATUS` | `UsretlAuditReport_RecordStatus` | String |  |  |
| 38 | `AUDIT.RPT.CURR.NO` | `UsretlAuditReport_CurrNo` | String |  |  |
| 39 | `AUDIT.RPT.INPUTTER` | `UsretlAuditReport_Inputter` |  |  |  |
| 40 | `AUDIT.RPT.DATE.TIME` | `UsretlAuditReport_DateTime` |  |  |  |
| 41 | `AUDIT.RPT.AUTHORISER` | `UsretlAuditReport_Authoriser` | String |  |  |
| 42 | `AUDIT.RPT.CO.CODE` | `UsretlAuditReport_CoCode` | String |  |  |
| 43 | `AUDIT.RPT.DEPT.CODE` | `UsretlAuditReport_DeptCode` | String |  |  |
| 44 | `AUDIT.RPT.AUDITOR.CODE` | `UsretlAuditReport_AuditorCode` | String |  |  |
| 45 | `AUDIT.RPT.AUDIT.DATE.TIME` | `UsretlAuditReport_AuditDateTime` | String |  |  |
