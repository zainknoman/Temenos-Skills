# AA.DATA.OBJECT — Table Schema

> Source: `INSERTS/I_F.AA.DATA.OBJECT` in `AF_Advice.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.DO.DESCRIPTION` | `AaDataObject_Description` |  |  |  |
| 2 | `AA.DO.FULL.DESCRIPTION` | `AaDataObject_FullDescription` | TField |  | The Full description of the Data Object |
| 3 | `AA.DO.DATA.MODEL.CATEGORY` | `AaDataObject_DataModelCategory` | TField | Yes | A data object can be defined for one of the following five data Model Categories APPLICATION.FORM EVIDENCE NEEDS.ANALYSIS PROCESS QUOTATION Validation Rules : It is a mandatory field. |
| 4 | `AA.DO.DATA.MODEL` | `AaDataObject_DataModel` | TField | Yes | It is specific model belonging to the Category defined in DATA.MODEL.CATAGORY field. The input should follow below restrictions. A data model will typically have input data (e.g. captured data). For a form or questionnaire this is the information a customer provides. Two of the models, Quotation and Needs Analysis have result data. The user must either specify whether they want input data or output data. 1. It should be valid record from OA.FROM if the data model category is APPLICATION.FROM. 2. It should be valid record from EV.EVIDENCE.TYPE if the data model category is EVIDENCE. 3. It should be valid record from NA.QUESTIONNAIRE.TYPE if the data model category is NEEDS.ANALYSIS. 4. It should be valid record from PW.ACTIVITY if the data model category is PROCESS. 5. It should be valid record from AA.QUOTATION.TYPE if the data model category is QUOTATION. Validation Rules : It is a mandatory field. |
| 5 | `AA.DO.SYS.RESERVED.10` | `AaDataObject_SysReserved10` | TField |  |  |
| 6 | `AA.DO.SYS.RESERVED.9` | `AaDataObject_SysReserved9` | TField |  |  |
| 7 | `AA.DO.SYS.RESERVED.8` | `AaDataObject_SysReserved8` | TField |  |  |
| 8 | `AA.DO.SYS.RESERVED.7` | `AaDataObject_SysReserved7` | TField |  |  |
| 9 | `AA.DO.DATA.INPUT` | `AaDataObject_DataInput` | TField | Yes | A Data Model can be comprised of multiple tables. For example a Form can have multiple formlets. This specifies the exact "input" Data table from the model. 1. It should be a valid OA.FORMLET if the DATA.MODEL is Form. 2. It should be a valid EV.EVIDENCE.CLASS if the DATA.MODEL is Evidence Type. 3. It should be a valid NA.NEEDS.CLASS if the DATA.MODEL is Questionnaire Type. 4. It should be a valid APPLICATION from TARGET field of PW.ACTIVITY, If the DATA.MODEL is Pw Activity. 5. It should be a valid AA.QUOTATION.CLASS if the DATA.MODEL is Quotation Type. Validation Rules: Input mandatory either in DATA.INPUT or DATA.RESULT fields. Input not allowed in both fields. |
| 10 | `AA.DO.DATA.RESULT` | `AaDataObject_DataResult` | TField | Yes | This field will be used to specify whether data has to be captured from output result file. The Options available for this field are NEEDS.RECOMMENDATION, QUOTATION.OUTPUT, REFERENCE and SCHEDULE.DETAILS. 1. The output result will be extracted from NA.PRODUCT.RECOMMENDATION if the DATA.MODEL.CATEGORY is NEEDS.ANALYSIS. 2. The output result will be extracted from AA.QUOTATION.OUTPUT if the DATA.MODEL.CATEGORY is QUOTATION. Validation Rules: Input mandatory either in DATA.INPUT or DATA.RESULT fields. a. If Data Model Category is "Needs Analysis" then Data Result should be "NEEDS.RECOMMENDATION" b. If Data Model Category is "Quotation" then Data Result should be "QUOTATION.OUTPUT" c. If Data Model Category is "Temenos Core" then Data Result should be "REFERENCE" |
| 11 | `AA.DO.SYS.RESERVED.6` | `AaDataObject_SysReserved6` | TField |  |  |
| 12 | `AA.DO.SYS.RESERVED.5` | `AaDataObject_SysReserved5` | TField |  |  |
| 13 | `AA.DO.SYS.RESERVED.4` | `AaDataObject_SysReserved4` | TField |  |  |
| 14 | `AA.DO.SYS.RESERVED.3` | `AaDataObject_SysReserved3` | TField |  |  |
| 15 | `AA.DO.SYS.RESERVED.2` | `AaDataObject_SysReserved2` | TField |  |  |
| 16 | `AA.DO.SYS.RESERVED.1` | `AaDataObject_SysReserved1` | TField |  |  |
| 17 | `AA.DO.LOCAL.REF` | `AaDataObject_LocalRef` |  |  |  |
| 18 | `AA.DO.OVERRIDE` | `AaDataObject_Override` |  |  |  |
| 19 | `AA.DO.RECORD.STATUS` | `AaDataObject_RecordStatus` | String |  |  |
| 20 | `AA.DO.CURR.NO` | `AaDataObject_CurrNo` | String |  |  |
| 21 | `AA.DO.INPUTTER` | `AaDataObject_Inputter` |  |  |  |
| 22 | `AA.DO.DATE.TIME` | `AaDataObject_DateTime` |  |  |  |
| 23 | `AA.DO.AUTHORISER` | `AaDataObject_Authoriser` | String |  |  |
| 24 | `AA.DO.CO.CODE` | `AaDataObject_CoCode` | String |  |  |
| 25 | `AA.DO.DEPT.CODE` | `AaDataObject_DeptCode` | String |  |  |
| 26 | `AA.DO.AUDITOR.CODE` | `AaDataObject_AuditorCode` | String |  |  |
| 27 | `AA.DO.AUDIT.DATE.TIME` | `AaDataObject_AuditDateTime` | String |  |  |
