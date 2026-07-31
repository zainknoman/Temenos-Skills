# LC.TYPES — Table Schema

> Source: `INSERTS/I_F.LC.TYPES` in `LC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LC.TYP.DESCRIPTION` | `LcTypes_Description` |  |  |  |
| 2 | `LC.TYP.CATEGORY.CODE` | `LcTypes_CategoryCode` | TField | Yes | Identifies the category code under which each LC.TYPE should be reported. This field is used as the default when the CATEGORY.CODE is not entered as part of the L/C input data. If any LC transactions are existing with this LC.TYPES in the live file or unauthorised file ,this field cannot be modified, because modifying this field leads to conflict in ASSET.TYPE in CRF entries. Validation Rules: 5 numeric characters. (Mandatory input) The code entered must be present on the CATEGORY file. The value entered must be in the range 23000-23999. |
| 3 | `LC.TYP.IMPORT.EXPORT` | `LcTypes_ImportExport` | TField | Yes | Defines whether the LC.TYPE is an Import (Issuance) or Export (Advising) type credit. Depending on whether this field contains 'I' or 'E' the processing will treat the L/C as an Import or Export credit. If any LC transactions are existing with this LC.TYPES in the live file or unauthorised file ,this field cannot be modified, because modifying this field leads to conflict in ASSET.TYPE in CRF entries. Validation Rules: 'I' or 'E'. (Mandatory input) |
| 4 | `LC.TYP.TRANSFERABLE` | `LcTypes_Transferable` | TField |  | Specifies if the LC.TYPE is able to be transferred. This field is used during the creation of L/C documents and advices and determines whether Transferable is to be printed on the documents. Validation Rules: Valid Inputs - 'YES' or 'NO'. |
| 5 | `LC.TYP.CONFIRMED` | `LcTypes_Confirmed` | TField | Yes | Defines whether the LC.TYPE is a Confirmed or an Unconfirmed credit. This field will have an impact on the Limits and CRF processing relevant to L/Cs. If any LC transactions are existing with this LC.TYPES in the live file or unauthorised file ,this field cannot be modified, because modifying this field leads to conflict in ASSET.TYPE in CRF entries. Validation Rules: 'YES' or 'NO'. (Mandatory input) |
| 6 | `LC.TYP.PAY.TYPE` | `LcTypes_PayType` | TField | Yes | Specifies by which method the LC.TYPE is to be paid. Identifies the payment method for the credit where: 'P' - By Payment 'A' - By Acceptance 'N' - By Negotiation 'M' - Mixed payment 'D' - By Direct credit Reimbursement 'NS' - Negotiate Sight 'NA' - Negotiate Acceptance Validation Rules: 'P' , 'A' , 'M' , 'N' , 'D' ,'NS' or 'NA'. (Mandatory input) |
| 7 | `LC.TYP.DOC.COLLECTION` | `LcTypes_DocCollection` | TField |  | Specifies if the LC.TYPE is a Documentary Collection type, not a Letter of Credit. If set to 'YES' then the LC.TYPE is used for Documentary Collections only. If an L/C is input using this type, then all processing is carried out for Documentary Collections. If any LC transactions are existing with this LC.TYPES in the live file or unauthorised file ,this field cannot be modified, because modifying this field leads to conflict in ASSET.TYPE in CRF entries. Validation Rules: 'YES' or 'NO'. |
| 8 | `LC.TYP.CLEAN.CREDIT` | `LcTypes_CleanCredit` | TField |  | For Letter of Credit type credits, determines whether the LC.TYPE is a clean credit. Field is used during the creation of L/C documents and Advices. If any LC transactions are existing with this LC.TYPES in the live file or unauthorised file ,this field cannot be modified, because modifying this field leads to conflict in ASSET.TYPE in CRF entries. Validation Rules: 'YES' or 'NO'. |
| 9 | `LC.TYP.CLEAN.COLLECTION` | `LcTypes_CleanCollection` | TField |  | For Documentary Collection type Credits, determines whether the LC.TYPE is a Clean collection. Field is used during the creation of Collection documents and advi. If any LC transactions are existing with this LC.TYPES in the live file or unauthorised file ,this field cannot be modified, because modifying this field leads to conflict in ASSET.TYPE in CRF entries. Validation Rules: 'YES' or 'NO'. |
| 10 | `LC.TYP.PRE.ADVISED` | `LcTypes_PreAdvised` | TField |  | Field Not in Use |
| 11 | `LC.TYP.OPENED` | `LcTypes_Opened` | TField |  | Field not in use. |
| 12 | `LC.TYP.EXPIRED.NOT.CLOSED` | `LcTypes_ExpiredNotClosed` | TField |  | Field not in use. |
| 13 | `LC.TYP.BACK.TO.BACK` | `LcTypes_BackToBack` | TField |  | Specifies if the LC.TYPE can be used in Back to Back processing. This field is used during the input of Back to Back documents and indicates whether a further Back to Back document should be created. Validation Rules: 'YES' or 'NO'. |
| 14 | `LC.TYP.BACK.LC.TYPE` | `LcTypes_BackLcType` | TField |  | Back-to-back letters of credit are related to each other usually with one acting as security for the other. T24 can help with the preparation of details by using one as the basis for generating the other. This field indicates the type of LC which will be used in the generated back-to-back transaction. |
| 15 | `LC.TYP.APPLICATION.FORMAT` | `LcTypes_ApplicationFormat` | TField | No | This field can be used to specify the application format which will be used instead of the default value. This allows the format of advices to be defined at the LC type level. When input is valid in this field, appropriate records should be created on the DE.FORMAT.PRINT file. Input in this field will form the second part The value in this field will form the second part of the key to the file DE.FORMAT.PRINT. The key will be derived appending the value in this field to the literal 'LC'. For example, input of a '2' in this field will mean that the key to DE.FORMAT.PRINT will be 700.LC2.1.GB instead of the default 700.1.1.GB. Validation Rules: 4 numeric characters. Optional input. Default is 1 if left blank. |
| 16 | `LC.TYP.STANDBY` | `LcTypes_Standby` | TField |  | Specifies if the LC TYPE supports Standby L/C or not. This field is mapped to the appropriate L/C documents and advices. Validation Rules: Valid inputs - YES or NO (Default NO) |
| 17 | `LC.TYP.UCPDC.DEFAULT` | `LcTypes_UcpdcDefault` |  |  |  |
| 18 | `LC.TYP.DUPLICATE.CHECK` | `LcTypes_DuplicateCheck` |  |  |  |
| 19 | `LC.TYP.LOCAL.REF` | `LcTypes_LocalRef` |  |  |  |
| 20 | `LC.TYP.TRANS.LC.TYPE` | `LcTypes_TransLcType` | TField |  | This field is reserved for transferrable LC initiated through Internet Banking. |
| 21 | `LC.TYP.RESERVED2` | `LcTypes_Reserved2` |  |  |  |
| 22 | `LC.TYP.RESERVED1` | `LcTypes_Reserved1` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 23 | `LC.TYP.OVERRIDE` | `LcTypes_Override` |  |  |  |
| 24 | `LC.TYP.RECORD.STATUS` | `LcTypes_RecordStatus` | String |  |  |
| 25 | `LC.TYP.CURR.NO` | `LcTypes_CurrNo` | String |  |  |
| 26 | `LC.TYP.INPUTTER` | `LcTypes_Inputter` |  |  |  |
| 27 | `LC.TYP.DATE.TIME` | `LcTypes_DateTime` |  |  |  |
| 28 | `LC.TYP.AUTHORISER` | `LcTypes_Authoriser` | String |  |  |
| 29 | `LC.TYP.CO.CODE` | `LcTypes_CoCode` | String |  |  |
| 30 | `LC.TYP.DEPT.CODE` | `LcTypes_DeptCode` | String |  |  |
| 31 | `LC.TYP.AUDITOR.CODE` | `LcTypes_AuditorCode` | String |  |  |
| 32 | `LC.TYP.AUDIT.DATE.TIME` | `LcTypes_AuditDateTime` | String |  |  |
