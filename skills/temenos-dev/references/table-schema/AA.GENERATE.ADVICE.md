# AA.GENERATE.ADVICE — Table Schema

> Source: `INSERTS/I_F.AA.GENERATE.ADVICE` in `AF_Advice.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.GNAD.ADVICE.TYPE` | `AaGenerateAdvice_AdviceType` | TField |  | The type of the advice to be generated. Must be a valid ID from AA.ADVICE.TYPE. If Purpose Code is populated then the advice type will be validated against the types specified for the purpose. |
| 2 | `AA.GNAD.INITIATION.TYPE` | `AaGenerateAdvice_InitiationType` |  |  |  |
| 3 | `AA.GNAD.SOURCE` | `AaGenerateAdvice_Source` | TField |  | Each advice will have one "primary" source. It is either a specific application or a stand-alone Needs analysis or Quotation. Application Needs Analysis Quotation |
| 4 | `AA.GNAD.SOURCE.REFERENCE` | `AaGenerateAdvice_SourceReference` | TField | Yes | The reference id of the source. OA.APPLICATION id for Application NA.QUESTIONNAIRE id for Needs Analysis AA.QUOTATION.REQUEST id for Quotation It is a mandatory field. |
| 5 | `AA.GNAD.PURPOSE.CODE` | `AaGenerateAdvice_PurposeCode` | TField | Yes | The purpose for which an advice is being generated. Conditionally available and mandatory if Source is "Application" |
| 6 | `AA.GNAD.RESERVED.10` | `AaGenerateAdvice_Reserved10` | TField |  |  |
| 7 | `AA.GNAD.RESERVED.9` | `AaGenerateAdvice_Reserved9` | TField |  |  |
| 8 | `AA.GNAD.RESERVED.8` | `AaGenerateAdvice_Reserved8` | TField |  |  |
| 9 | `AA.GNAD.RESERVED.7` | `AaGenerateAdvice_Reserved7` | TField |  |  |
| 10 | `AA.GNAD.RESERVED.6` | `AaGenerateAdvice_Reserved6` | TField |  |  |
| 11 | `AA.GNAD.CUSTOMER` | `AaGenerateAdvice_Customer` |  |  |  |
| 12 | `AA.GNAD.CUSTOMER.ROLE` | `AaGenerateAdvice_CustomerRole` |  |  |  |
| 13 | `AA.GNAD.CUSTOMER.ROLE.SEQ` | `AaGenerateAdvice_CustomerRoleSeq` |  |  |  |
| 14 | `AA.GNAD.RESERVED.5` | `AaGenerateAdvice_Reserved5` | TField |  |  |
| 15 | `AA.GNAD.RESERVED.4` | `AaGenerateAdvice_Reserved4` | TField |  |  |
| 16 | `AA.GNAD.RESERVED.3` | `AaGenerateAdvice_Reserved3` | TField |  |  |
| 17 | `AA.GNAD.RESERVED.2` | `AaGenerateAdvice_Reserved2` | TField |  |  |
| 18 | `AA.GNAD.RESERVED.1` | `AaGenerateAdvice_Reserved1` | TField |  |  |
| 19 | `AA.GNAD.LOCAL.REF` | `AaGenerateAdvice_LocalRef` |  |  |  |
| 20 | `AA.GNAD.ADVICE.NO` | `AaGenerateAdvice_AdviceNo` | TField |  | It is a delivery related field, value in this field will be a valid record in EB.ADVICES table. It is a no-input field. |
| 21 | `AA.GNAD.MAPPING.KEY` | `AaGenerateAdvice_MappingKey` | TField |  | DE.MAPPING id. the value in this field will be valid record from DE.MAPPING application |
| 22 | `AA.GNAD.DELIVERY.REFERENCE` | `AaGenerateAdvice_DeliveryReference` |  |  |  |
| 23 | `AA.GNAD.OVERRIDE` | `AaGenerateAdvice_Override` |  |  |  |
| 24 | `AA.GNAD.RECORD.STATUS` | `AaGenerateAdvice_RecordStatus` | String |  |  |
| 25 | `AA.GNAD.CURR.NO` | `AaGenerateAdvice_CurrNo` | String |  |  |
| 26 | `AA.GNAD.INPUTTER` | `AaGenerateAdvice_Inputter` |  |  |  |
| 27 | `AA.GNAD.DATE.TIME` | `AaGenerateAdvice_DateTime` |  |  |  |
| 28 | `AA.GNAD.AUTHORISER` | `AaGenerateAdvice_Authoriser` | String |  |  |
| 29 | `AA.GNAD.CO.CODE` | `AaGenerateAdvice_CoCode` | String |  |  |
| 30 | `AA.GNAD.DEPT.CODE` | `AaGenerateAdvice_DeptCode` | String |  |  |
| 31 | `AA.GNAD.AUDITOR.CODE` | `AaGenerateAdvice_AuditorCode` | String |  |  |
| 32 | `AA.GNAD.AUDIT.DATE.TIME` | `AaGenerateAdvice_AuditDateTime` | String |  |  |
| 33 | `AA.GNAD.ACTIVITY` | `AaGenerateAdvice_Activity` | TField | Yes | This field defines the activity to be processed against Mapping Request. 1. Input in this field should be valid record under AA.CLASS.TYPE.ACTIVITY.CLASS application. 2. Input is mandatory in this field to create the new generate advice transaction. 3. Only allowed activity is GENERATE-ADVICE and System will default this activity when creating the new generate advice transaction. |
