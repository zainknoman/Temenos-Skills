# ESBASE.ID.PARAM — Table Schema

> Source: `INSERTS/I_F.ESBASE.ID.PARAM` in `CMBASE_IdValidation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.PARAM.DESCRIPTION` | `EsbaseIdParam_Description` | TField |  | Description about the Parameters configured |
| 2 | `ID.PARAM.ACTIVE` | `EsbaseIdParam_Active` | TField |  | If Active is selected as 'Yes' then validation will take place If Active is selected as 'No' then validation will not take place |
| 3 | `ID.PARAM.LENGTH` | `EsbaseIdParam_Length` |  |  |  |
| 4 | `ID.PARAM.MODULO` | `EsbaseIdParam_Modulo` |  |  |  |
| 5 | `ID.PARAM.PATTERN` | `EsbaseIdParam_Pattern` |  |  |  |
| 6 | `ID.PARAM.RESERVED.1` | `EsbaseIdParam_Reserved1` |  |  |  |
| 7 | `ID.PARAM.RESERVED.2` | `EsbaseIdParam_Reserved2` |  |  |  |
| 8 | `ID.PARAM.RESERVED.3` | `EsbaseIdParam_Reserved3` |  |  |  |
| 9 | `ID.PARAM.MAPPING.ID` | `EsbaseIdParam_MappingId` | TField |  | Mapping Id with which the system will search the corresponding Mapping Table ESBASE.ID.MAPPER |
| 10 | `ID.PARAM.ID.VALID.ROUTINE` | `EsbaseIdParam_IdValidRoutine` | TField |  | To attach the validation routine. The routine should have an entry in EB.API or an EB.API record of type METHOD which implements an interface defined in the EB.API record HOOK.CMBASE.VALIDATE.LEGALID This validation routine can be used to do customised validations on Id See the EB.API record HOOK.CMBASE.VALIDATE.LEGALID for the full list of supported interfaces. |
| 11 | `ID.PARAM.LOCAL.REF` | `EsbaseIdParam_LocalRef` |  |  |  |
| 12 | `ID.PARAM.APPLICATION.NAME` | `EsbaseIdParam_ApplicationName` | TField |  | Application base from where the fields will be associated. |
| 13 | `ID.PARAM.FIELD.NAME` | `EsbaseIdParam_FieldName` |  |  |  |
| 14 | `ID.PARAM.FIELD.CONVERTION` | `EsbaseIdParam_FieldConvertion` |  |  |  |
| 15 | `ID.PARAM.REFERENCE.ALGORITHM` | `EsbaseIdParam_ReferenceAlgorithm` |  |  |  |
| 16 | `ID.PARAM.ALGORITHM.ID` | `EsbaseIdParam_AlgorithmId` |  |  |  |
| 17 | `ID.PARAM.ALGORITHM.PROCESS.TYPE` | `EsbaseIdParam_AlgorithmProcessType` |  |  |  |
| 18 | `ID.PARAM.ALGORITHM.OPERATION` | `EsbaseIdParam_AlgorithmOperation` |  |  |  |
| 19 | `ID.PARAM.FIELD.TYPE` | `EsbaseIdParam_FieldType` |  |  |  |
| 20 | `ID.PARAM.FIELD.VALUE` | `EsbaseIdParam_FieldValue` |  |  |  |
| 21 | `ID.PARAM.RESERVED.13` | `EsbaseIdParam_Reserved13` |  |  |  |
| 22 | `ID.PARAM.RESERVED.14` | `EsbaseIdParam_Reserved14` | TField |  |  |
| 23 | `ID.PARAM.RESERVED.15` | `EsbaseIdParam_Reserved15` | TField |  |  |
| 24 | `ID.PARAM.OVERRIDE` | `EsbaseIdParam_Override` |  |  |  |
| 25 | `ID.PARAM.RECORD.STATUS` | `EsbaseIdParam_RecordStatus` | String |  | Indicates the record status |
| 26 | `ID.PARAM.CURR.NO` | `EsbaseIdParam_CurrNo` | String |  | Indicates the number of time record is modified and saved |
| 27 | `ID.PARAM.INPUTTER` | `EsbaseIdParam_Inputter` |  |  |  |
| 28 | `ID.PARAM.DATE.TIME` | `EsbaseIdParam_DateTime` |  |  |  |
| 29 | `ID.PARAM.AUTHORISER` | `EsbaseIdParam_Authoriser` | String |  |  |
| 30 | `ID.PARAM.CO.CODE` | `EsbaseIdParam_CoCode` | String |  |  |
| 31 | `ID.PARAM.DEPT.CODE` | `EsbaseIdParam_DeptCode` | String |  |  |
| 32 | `ID.PARAM.AUDITOR.CODE` | `EsbaseIdParam_AuditorCode` | String |  |  |
| 33 | `ID.PARAM.AUDIT.DATE.TIME` | `EsbaseIdParam_AuditDateTime` | String |  |  |
