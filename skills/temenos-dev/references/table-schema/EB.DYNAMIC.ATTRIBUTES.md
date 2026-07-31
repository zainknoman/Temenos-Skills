# EB.DYNAMIC.ATTRIBUTES — Table Schema

> Source: `INSERTS/I_F.EB.DYNAMIC.ATTRIBUTES` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.DYN.ATT.ENQUIRY.RTN` | `EbDynamicAttributes_EnquiryRtn` | TField |  | The name of the user routine to be called that will handle dynamic changes to the ENQUIRY records. |
| 2 | `EB.DYN.ATT.VERSION.RTN` | `EbDynamicAttributes_VersionRtn` | TField |  | The name of the user routine to be called that will handle dynamic changes to the VERSION records. |
| 3 | `EB.DYN.ATT.COS.RTN` | `EbDynamicAttributes_CosRtn` | TField |  | The name of the user routine to be called that will handle dynamic changes to the EB.COMPOSITE.SCREEN records. |
| 4 | `EB.DYN.ATT.MENU.RTN` | `EbDynamicAttributes_MenuRtn` | TField |  | The name of the user routine to be called that will handle dynamic changes to the HELPTEXT.MENU records. |
| 5 | `EB.DYN.ATT.TAB.RTN` | `EbDynamicAttributes_TabRtn` | TField |  | The name of the user routine to be called that will handle dynamic changes to the EB.TABBED.SCREEN records. |
| 6 | `EB.DYN.ATT.RESERVED.4` | `EbDynamicAttributes_Reserved4` | TField |  |  |
| 7 | `EB.DYN.ATT.RESERVED.3` | `EbDynamicAttributes_Reserved3` | TField |  |  |
| 8 | `EB.DYN.ATT.RESERVED.2` | `EbDynamicAttributes_Reserved2` | TField |  |  |
| 9 | `EB.DYN.ATT.RESERVED.1` | `EbDynamicAttributes_Reserved1` | TField |  |  |
| 10 | `EB.DYN.ATT.LOCAL.REF` | `EbDynamicAttributes_LocalRef` |  |  |  |
| 11 | `EB.DYN.ATT.RECORD.STATUS` | `EbDynamicAttributes_RecordStatus` | String |  |  |
| 12 | `EB.DYN.ATT.CURR.NO` | `EbDynamicAttributes_CurrNo` | String |  |  |
| 13 | `EB.DYN.ATT.INPUTTER` | `EbDynamicAttributes_Inputter` |  |  |  |
| 14 | `EB.DYN.ATT.DATE.TIME` | `EbDynamicAttributes_DateTime` |  |  |  |
| 15 | `EB.DYN.ATT.AUTHORISER` | `EbDynamicAttributes_Authoriser` | String |  |  |
| 16 | `EB.DYN.ATT.CO.CODE` | `EbDynamicAttributes_CoCode` | String |  |  |
| 17 | `EB.DYN.ATT.DEPT.CODE` | `EbDynamicAttributes_DeptCode` | String |  |  |
| 18 | `EB.DYN.ATT.AUDITOR.CODE` | `EbDynamicAttributes_AuditorCode` | String |  |  |
| 19 | `EB.DYN.ATT.AUDIT.DATE.TIME` | `EbDynamicAttributes_AuditDateTime` | String |  |  |
