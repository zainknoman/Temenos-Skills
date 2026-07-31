# EB.DICTIONARY — Table Schema

> Source: `INSERTS/I_F.EB.DICTIONARY` in `EB_SystemTables.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.DIC.DESCRIPTION` | `EbDictionary_Description` |  |  |  |
| 2 | `EB.DIC.SHORT.DESC` | `EbDictionary_ShortDesc` | TField | Yes | Holds description about the Enquiry/Version or field name. When Version name/Enquiry name is specified in Dictionary key, text defined here is mapped to short description of corresponding Enquiry or Version. Validation Rules: 1)Mandatory Input when Text is not entered. 2)Up to 35 characters. |
| 3 | `EB.DIC.TEXT` | `EbDictionary_Text` | TField | Yes | Specifies the text that appears to the left of the field when displayed in Version or Enquiry. This field is mapped to field label of Version and enquiry when corresponding field name is specified in Dictionary key. Field characteristics of this field are similar to TEXT in Version. Validation Rules: 1)Mandatory Input 2)Up to 39 characters. |
| 4 | `EB.DIC.TXT.040..078` | `EbDictionary_Txt040` |  |  |  |
| 5 | `EB.DIC.TXT.079..117` | `EbDictionary_Txt079` |  |  |  |
| 6 | `EB.DIC.TXT.118..132` | `EbDictionary_Txt118` |  |  |  |
| 7 | `EB.DIC.PROMPT.TEXT` | `EbDictionary_PromptText` | TField |  | Text entered here appears as a prompt to the user, replacing the T24 field name. Field characteristics are similar to PROMPT.TEXT in Version. Text Mapping will happen when Field name is specified in dictionary Key. Validation Rules: 1) Up to 1-70 characters. |
| 8 | `EB.DIC.TOOL.TIP` | `EbDictionary_ToolTip` | TField |  | Text entered here is displayed near the mouse pointer when it is at rest pointing to the associated field when fieldname is specified along with Version name in Dictionary Key. Validation Rules: 1) Up to 1-80 characters Field characteristics are similar to field TOOL.TIP in Version. |
| 9 | `EB.DIC.RESERVED.20` | `EbDictionary_Reserved20` | TField |  |  |
| 10 | `EB.DIC.RESERVED.19` | `EbDictionary_Reserved19` | TField |  |  |
| 11 | `EB.DIC.RESERVED.18` | `EbDictionary_Reserved18` | TField |  |  |
| 12 | `EB.DIC.RESERVED.17` | `EbDictionary_Reserved17` | TField |  |  |
| 13 | `EB.DIC.RESERVED.16` | `EbDictionary_Reserved16` | TField |  |  |
| 14 | `EB.DIC.RESERVED.15` | `EbDictionary_Reserved15` | TField |  |  |
| 15 | `EB.DIC.RESERVED.14` | `EbDictionary_Reserved14` | TField |  |  |
| 16 | `EB.DIC.HDR.1.001..039` | `EbDictionary_Hdr1001` |  |  |  |
| 17 | `EB.DIC.HDR.1.040..078` | `EbDictionary_Hdr1040` |  |  |  |
| 18 | `EB.DIC.HDR.1.079..117` | `EbDictionary_Hdr1079` |  |  |  |
| 19 | `EB.DIC.HDR.1.118..132` | `EbDictionary_Hdr1118` |  |  |  |
| 20 | `EB.DIC.HDR.2.001..039` | `EbDictionary_Hdr2001` |  |  |  |
| 21 | `EB.DIC.HDR.2.040..078` | `EbDictionary_Hdr2040` |  |  |  |
| 22 | `EB.DIC.HDR.2.079..117` | `EbDictionary_Hdr2079` |  |  |  |
| 23 | `EB.DIC.HDR.2.118..132` | `EbDictionary_Hdr2118` |  |  |  |
| 24 | `EB.DIC.ENQ.HEADER` | `EbDictionary_EnqHeader` |  |  |  |
| 25 | `EB.DIC.ENQ.SEL.TEXT` | `EbDictionary_EnqSelText` | A (alphanumeric) |  | Holds the text for Selection field name in Enquiry. Text defined here is mapped to Selection field in Enquiry Selection window when Selection field name is specified in Dictionary Key. Validation Rules: 1)Up to 39 type A (alphanumeric) characters. |
| 26 | `EB.DIC.TXT.OPERATION` | `EbDictionary_TxtOperation` |  |  |  |
| 27 | `EB.DIC.ENQ.TOOL.TEXT` | `EbDictionary_EnqToolText` | TField |  | The Text to be displayed on Browser Tool on the Toolbar can be specified in this field. When Tool Id is specified along with Enquiry name in dictionary Key, text defined in this field will be appear on corresponding Tool of Enquiry Output. Validation Rules: - Up to 35 'A' alphanumeric characters. |
| 28 | `EB.DIC.VERSION.ADDL.HDR` | `EbDictionary_VersionAddlHdr` |  |  |  |
| 29 | `EB.DIC.VERSION.ADDL.FTR` | `EbDictionary_VersionAddlFtr` |  |  |  |
| 30 | `EB.DIC.RESERVED.11` | `EbDictionary_Reserved11` | TField |  |  |
| 31 | `EB.DIC.RESERVED.10` | `EbDictionary_Reserved10` | TField |  |  |
| 32 | `EB.DIC.RESERVED.09` | `EbDictionary_Reserved09` | TField |  |  |
| 33 | `EB.DIC.RESERVED.08` | `EbDictionary_Reserved08` | TField |  |  |
| 34 | `EB.DIC.RESERVED.07` | `EbDictionary_Reserved07` | TField |  |  |
| 35 | `EB.DIC.RESERVED.06` | `EbDictionary_Reserved06` | TField |  |  |
| 36 | `EB.DIC.RESERVED.05` | `EbDictionary_Reserved05` | TField |  |  |
| 37 | `EB.DIC.RESERVED.04` | `EbDictionary_Reserved04` | TField |  |  |
| 38 | `EB.DIC.RESERVED.03` | `EbDictionary_Reserved03` | TField |  |  |
| 39 | `EB.DIC.RESERVED.02` | `EbDictionary_Reserved02` | TField |  |  |
| 40 | `EB.DIC.RESERVED.01` | `EbDictionary_Reserved01` | TField |  |  |
| 41 | `EB.DIC.LOCAL.REF` | `EbDictionary_LocalRef` |  |  |  |
| 42 | `EB.DIC.OVERRIDE` | `EbDictionary_Override` |  |  |  |
| 43 | `EB.DIC.RECORD.STATUS` | `EbDictionary_RecordStatus` | String |  |  |
| 44 | `EB.DIC.CURR.NO` | `EbDictionary_CurrNo` | String |  |  |
| 45 | `EB.DIC.INPUTTER` | `EbDictionary_Inputter` |  |  |  |
| 46 | `EB.DIC.DATE.TIME` | `EbDictionary_DateTime` |  |  |  |
| 47 | `EB.DIC.AUTHORISER` | `EbDictionary_Authoriser` | String |  |  |
| 48 | `EB.DIC.CO.CODE` | `EbDictionary_CoCode` | String |  |  |
| 49 | `EB.DIC.DEPT.CODE` | `EbDictionary_DeptCode` | String |  |  |
| 50 | `EB.DIC.AUDITOR.CODE` | `EbDictionary_AuditorCode` | String |  |  |
| 51 | `EB.DIC.AUDIT.DATE.TIME` | `EbDictionary_AuditDateTime` | String |  |  |
