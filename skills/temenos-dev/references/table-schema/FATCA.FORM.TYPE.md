# FATCA.FORM.TYPE — Table Schema

> Source: `INSERTS/I_F.FATCA.FORM.TYPE` in `FA_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FA.FF.DESCRIPTION` | `FatcaFormType_Description` |  |  |  |
| 2 | `FA.FF.US.DOCUMENT` | `FatcaFormType_UsDocument` | TField |  | The field will be set to YES if the document establishes the US status (for example, W9). Validation rules Yes or No Cannot be Yes if NON.US.DOCUMENT field value is set as Yes. |
| 3 | `FA.FF.NON.US.DOCUMENT` | `FatcaFormType_NonUsDocument` | TField |  | The field will be set to YES if the document establishes the NON-US status (for example, W8). If US DOCUMENT is set as YES, this cannot be set as YES and vice versa. Validation rules Yes or No This field can only be set to Yes if the field US.DOCUMENT is not set to Yes |
| 4 | `FA.FF.ENTITY.ONLY` | `FatcaFormType_EntityOnly` | TField |  | The field is used to specify whether these documents are allowed only for entities For example, EIN, ANNUAL OWNER CONFIRMATION, etc. Validation rules Yes or No |
| 5 | `FA.FF.RESERVED.3` | `FatcaFormType_Reserved3` | TField |  | This field is reserved for future use. |
| 6 | `FA.FF.RESERVED.2` | `FatcaFormType_Reserved2` | TField |  | This field is reserved for future use. |
| 7 | `FA.FF.RESERVED.1` | `FatcaFormType_Reserved1` | TField |  | This field is reserved for future use. |
| 8 | `FA.FF.LOCAL.REF` | `FatcaFormType_LocalRef` |  |  |  |
| 9 | `FA.FF.RECORD.STATUS` | `FatcaFormType_RecordStatus` | String |  |  |
| 10 | `FA.FF.CURR.NO` | `FatcaFormType_CurrNo` | String |  |  |
| 11 | `FA.FF.INPUTTER` | `FatcaFormType_Inputter` |  |  |  |
| 12 | `FA.FF.DATE.TIME` | `FatcaFormType_DateTime` |  |  |  |
| 13 | `FA.FF.AUTHORISER` | `FatcaFormType_Authoriser` | String |  |  |
| 14 | `FA.FF.CO.CODE` | `FatcaFormType_CoCode` | String |  |  |
| 15 | `FA.FF.DEPT.CODE` | `FatcaFormType_DeptCode` | String |  |  |
| 16 | `FA.FF.AUDITOR.CODE` | `FatcaFormType_AuditorCode` | String |  |  |
| 17 | `FA.FF.AUDIT.DATE.TIME` | `FatcaFormType_AuditDateTime` | String |  |  |
