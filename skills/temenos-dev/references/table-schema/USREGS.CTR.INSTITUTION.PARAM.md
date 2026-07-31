# USREGS.CTR.INSTITUTION.PARAM — Table Schema

> Source: `INSERTS/I_F.USREGS.CTR.INSTITUTION.PARAM` in `USREGS_CTR.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CTR.PARAM.PRIMARY.FED.REGULATOR` | `UsregsCtrInstitutionParam_PrimaryFedRegulator` | TField | No | Alphanumeric, with attached dropdown. Optional field. Primary Federal regulator will have a dropdown list with the following values: 1 � Federal Reserve Board (FRB) 2 � Federal Deposit Ins Corp (FDIC) 3 National Credit Union Admin (NCUA) 4 � Office of the Comp of the Ccy (OCC) |
| 2 | `CTR.PARAM.CONTACT.OFFICE` | `UsregsCtrInstitutionParam_ContactOffice` | TField | No | Text field allowing 1-150 characters. Optional field. |
| 3 | `CTR.PARAM.PHONE` | `UsregsCtrInstitutionParam_Phone` | TField | No | 10 numeric characters; not all same digit, such as all 0 or all 9, otherwise system will generate error message. Optional field. |
| 4 | `CTR.PARAM.EXT` | `UsregsCtrInstitutionParam_Ext` | TField | No | 1-6 numeric characters. Optional field. |
| 5 | `CTR.PARAM.FILE.PATH` | `UsregsCtrInstitutionParam_FilePath` | TField |  | File Path for CTR xml file generation location |
| 6 | `CTR.PARAM.FILE.NAME` | `UsregsCtrInstitutionParam_FileName` | TField |  |  |
| 7 | `CTR.PARAM.RESERVED.10` | `UsregsCtrInstitutionParam_Reserved10` |  |  |  |
| 8 | `CTR.PARAM.RESERVED.9` | `UsregsCtrInstitutionParam_Reserved9` |  |  |  |
| 9 | `CTR.PARAM.RESERVED.8` | `UsregsCtrInstitutionParam_Reserved8` |  |  |  |
| 10 | `CTR.PARAM.RESERVED.7` | `UsregsCtrInstitutionParam_Reserved7` |  |  |  |
| 11 | `CTR.PARAM.RESERVED.6` | `UsregsCtrInstitutionParam_Reserved6` |  |  |  |
| 12 | `CTR.PARAM.RESERVED.5` | `UsregsCtrInstitutionParam_Reserved5` |  |  |  |
| 13 | `CTR.PARAM.RESERVED.4` | `UsregsCtrInstitutionParam_Reserved4` |  |  |  |
| 14 | `CTR.PARAM.RESERVED.3` | `UsregsCtrInstitutionParam_Reserved3` |  |  |  |
| 15 | `CTR.PARAM.RESERVED.2` | `UsregsCtrInstitutionParam_Reserved2` |  |  |  |
| 16 | `CTR.PARAM.RESERVED.1` | `UsregsCtrInstitutionParam_Reserved1` |  |  |  |
| 17 | `CTR.PARAM.RECORD.STATUS` | `UsregsCtrInstitutionParam_RecordStatus` | String |  |  |
| 18 | `CTR.PARAM.CURR.NO` | `UsregsCtrInstitutionParam_CurrNo` | String |  |  |
| 19 | `CTR.PARAM.INPUTTER` | `UsregsCtrInstitutionParam_Inputter` |  |  |  |
| 20 | `CTR.PARAM.DATE.TIME` | `UsregsCtrInstitutionParam_DateTime` |  |  |  |
| 21 | `CTR.PARAM.AUTHORISER` | `UsregsCtrInstitutionParam_Authoriser` | String |  |  |
| 22 | `CTR.PARAM.CO.CODE` | `UsregsCtrInstitutionParam_CoCode` | String |  |  |
| 23 | `CTR.PARAM.DEPT.CODE` | `UsregsCtrInstitutionParam_DeptCode` | String |  |  |
| 24 | `CTR.PARAM.AUDITOR.CODE` | `UsregsCtrInstitutionParam_AuditorCode` | String |  |  |
| 25 | `CTR.PARAM.AUDIT.DATE.TIME` | `UsregsCtrInstitutionParam_AuditDateTime` | String |  |  |
