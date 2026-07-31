# IN.EXCLUSION.LIST — Table Schema

> Source: `INSERTS/I_F.IN.EXCLUSION.LIST` in `IN_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IN.EX.LI.MODIFICATION.FLAG` | `InExclusionList_ModificationFlag` | TField |  | A flag which indicates whether there is a change in the record, since the last release of the IBAN structure file. Validation Rules: A - Addition since last IBAN structure file. D - Deletion since last IBAN structure file. U - Unchanged since last IBAN structure file. M - Modification since last IBAN structure file. E - Expired : Reserved for future use. |
| 2 | `IN.EX.LI.RECORD.KEY` | `InExclusionList_RecordKey` | TField |  |  |
| 3 | `IN.EX.LI.COUNTRY.CODE` | `InExclusionList_CountryCode` | TField |  | Country code of the Invalid National id. Validation Rules: A maximum of 2 characters can be entered. |
| 4 | `IN.EX.LI.IBAN.NATIONAL.ID` | `InExclusionList_IbanNationalId` | TField |  | The Invalid National id that when included in IBAN leads to invalid payment. Validation Rules: A maximum of 35 characters can be entered. |
| 5 | `IN.EX.LI.BIC.CODE` | `InExclusionList_BicCode` | TField |  | The BIC of the financial institution that holds/used to hold this NATIONAL ID. Validation Rules: A maximum of 11 characters can be entered. |
| 6 | `IN.EX.LI.VALID.FROM` | `InExclusionList_ValidFrom` | TField |  | The future date from which the IBAN NATIONAL ID will be invalid. If the IBAN NATIONAL ID became invalid in the past, then the field is empty. Validation Rules: A maximum of 8 characters can be entered. |
| 7 | `IN.EX.LI.FIELD.A` | `InExclusionList_FieldA` | TField |  |  |
| 8 | `IN.EX.LI.FIELD.B` | `InExclusionList_FieldB` | TField |  |  |
| 9 | `IN.EX.LI.SOURCE.NAME` | `InExclusionList_SourceName` | TField |  | This field will be populated as a result of the upload process with the File Name of the Exclusion List, through which the record was created in the system or amended This field will not be populated when a manual record is created in DE.BIC Validation Rules: NOINPUT field. |
| 10 | `IN.EX.LI.EXCLUDED.COMPANY` | `InExclusionList_ExcludedCompany` |  |  |  |
| 11 | `IN.EX.LI.ALLOWED.COMPANY` | `InExclusionList_AllowedCompany` |  |  |  |
| 12 | `IN.EX.LI.STATUS` | `InExclusionList_Status` | TField |  | Captures the status of the Exclusion List record Validation Rules: Can be either Blank or DELETE. Default value is Blank |
| 13 | `IN.EX.LI.ENTRY.TYPE` | `InExclusionList_EntryType` | TField |  | Set as UPLOAD when input is record is uploaded through Service. In other scenarios, it is set as CUSTOM. Validation Rules: NOINPUT field. |
| 14 | `IN.EX.LI.RESERVED.5` | `InExclusionList_Reserved5` | TField |  |  |
| 15 | `IN.EX.LI.RESERVED.4` | `InExclusionList_Reserved4` | TField |  |  |
| 16 | `IN.EX.LI.RESERVED.3` | `InExclusionList_Reserved3` | TField |  |  |
| 17 | `IN.EX.LI.LOCAL.REF` | `InExclusionList_LocalRef` |  |  |  |
| 18 | `IN.EX.LI.OVERRIDE` | `InExclusionList_Override` |  |  |  |
| 19 | `IN.EX.LI.RECORD.STATUS` | `InExclusionList_RecordStatus` | String |  |  |
| 20 | `IN.EX.LI.CURR.NO` | `InExclusionList_CurrNo` | String |  |  |
| 21 | `IN.EX.LI.INPUTTER` | `InExclusionList_Inputter` |  |  |  |
| 22 | `IN.EX.LI.DATE.TIME` | `InExclusionList_DateTime` |  |  |  |
| 23 | `IN.EX.LI.AUTHORISER` | `InExclusionList_Authoriser` | String |  |  |
| 24 | `IN.EX.LI.CO.CODE` | `InExclusionList_CoCode` | String |  |  |
| 25 | `IN.EX.LI.DEPT.CODE` | `InExclusionList_DeptCode` | String |  |  |
| 26 | `IN.EX.LI.AUDITOR.CODE` | `InExclusionList_AuditorCode` | String |  |  |
| 27 | `IN.EX.LI.AUDIT.DATE.TIME` | `InExclusionList_AuditDateTime` | String |  |  |
