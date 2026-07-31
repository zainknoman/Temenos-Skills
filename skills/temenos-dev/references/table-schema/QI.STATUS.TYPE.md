# QI.STATUS.TYPE — Table Schema

> Source: `INSERTS/I_F.QI.STATUS.TYPE` in `QI_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `QI.ST.DESCRIPTION` | `QiStatusType_Description` |  |  |  |
| 2 | `QI.ST.STATUS.DOC.TYPE` | `QiStatusType_StatusDocType` | TField |  | This field holds the name of the document required or applicable for the status in the record ID. Document is thebasis in calculating the Customer QI status in most of the cases. Validation Rules: Valid record in DOCUMENT.TYPE table |
| 3 | `QI.ST.QI.TAX.RATE.DOC.TYPE` | `QiStatusType_QiTaxRateDocType` | TField |  | This field holds the name of the withholding statement the system should look for in order to assign a portfoliotax rate. The basis to assign the status such as QIA, QIB, QIC, QID and NQI is a W8-IMY (CWHI) document and the basis toassign a portfolio tax rate is a withholding statement (CWHS). Validation Rules: Valid record in DOCUMENT.TYPE table |
| 4 | `QI.ST.QI.NQI.INSTITUTION` | `QiStatusType_QiNqiInstitution` | TField |  | This field allows the user to specify whether the QI status (the ID) belongs to an Institutional client who isalso a Qualified or Non-Qualified intermediary. Validation Rules: Allowed values are Y or N |
| 5 | `QI.ST.QI.NQI.DEFAULT.STATUS` | `QiStatusType_QiNqiDefaultStatus` | TField |  | Allowed only if QI.NQI.Institution field is set to Y. This represents the system calculated status initially fora QI.NQI.Institution at customer level. For Ex: NTREAT Validation Rules: Valid record in QI.STATUS.TYPE table |
| 6 | `QI.ST.LMTN.BEN.APPLICABLE` | `QiStatusType_LmtnBenApplicable` | TField |  | This field allows the user to specify whether limitation of benefits is applicable for a QI status. If set to Y,system performs validations in QI.CUSTOMER.SUPPLEMENTARY.INFO table where this QI Status is applicable. Validation Rules: Allowed values are Y or N |
| 7 | `QI.ST.EIN.REQUIRED` | `QiStatusType_EinRequired` | TField |  | Field denotes Whether the Employer Identification Number is applicable for a QI status or not. Validation Rules: Allowed values are Y, N and Null. N and Null means the same. |
| 8 | `QI.ST.RECP.CODE.CHAP.3` | `QiStatusType_RecpCodeChap3` | TField | Yes | This field is a mandatory field and allows the user to select the applicable recipient code corresponding to theQI Status from dropdown list values from EB.LOOKUP(QI.STATUS.TYPE.RECP.CODE.CHAP) file.This value gets mapped tothe US tax data base for reporting purposes. The code is associated with the Customer's QI status. System calculated value is held for reporting purposes e.g. 12 for QI Institution and 27 for others including NQI |
| 9 | `QI.ST.US.INCOME.CODE` | `QiStatusType_UsIncomeCode` |  |  |  |
| 10 | `QI.ST.EXEM.CODE.CHAP.3` | `QiStatusType_ExemCodeChap3` |  |  |  |
| 11 | `QI.ST.CODE.RESERVED.10` | `QiStatusType_CodeReserved10` |  |  |  |
| 12 | `QI.ST.CODE.RESERVED.09` | `QiStatusType_CodeReserved09` |  |  |  |
| 13 | `QI.ST.CODE.RESERVED.08` | `QiStatusType_CodeReserved08` |  |  |  |
| 14 | `QI.ST.CODE.RESERVED.07` | `QiStatusType_CodeReserved07` |  |  |  |
| 15 | `QI.ST.CODE.RESERVED.06` | `QiStatusType_CodeReserved06` |  |  |  |
| 16 | `QI.ST.CODE.RESERVED.05` | `QiStatusType_CodeReserved05` |  |  |  |
| 17 | `QI.ST.CODE.RESERVED.04` | `QiStatusType_CodeReserved04` |  |  |  |
| 18 | `QI.ST.CODE.RESERVED.03` | `QiStatusType_CodeReserved03` |  |  |  |
| 19 | `QI.ST.CODE.RESERVED.02` | `QiStatusType_CodeReserved02` |  |  |  |
| 20 | `QI.ST.CODE.RESERVED.01` | `QiStatusType_CodeReserved01` |  |  |  |
| 21 | `QI.ST.EXEM.CODE.CHAP.4` | `QiStatusType_ExemCodeChap4` | TField |  | User can select any value from dropdown list which was configured in EB.LOOKUP(QI.STATUS.TYPE.EXEM.CODE.CHAP)file.This code relates to FATCA but associated with QI status.For Eg: If QI status is QIA�QID then the code is 17 , else it is 15. |
| 22 | `QI.ST.HIST.DATE` | `QiStatusType_HistDate` |  |  |  |
| 23 | `QI.ST.RESERVED.14` | `QiStatusType_Reserved14` | TField |  | Reserved for future use |
| 24 | `QI.ST.RESERVED.13` | `QiStatusType_Reserved13` | TField |  | Reserved for future use |
| 25 | `QI.ST.RESERVED.12` | `QiStatusType_Reserved12` | TField |  | Reserved for future use |
| 26 | `QI.ST.RESERVED.11` | `QiStatusType_Reserved11` | TField |  | Reserved for future use |
| 27 | `QI.ST.RESERVED.10` | `QiStatusType_Reserved10` | TField |  | Reserved for future use |
| 28 | `QI.ST.RESERVED.09` | `QiStatusType_Reserved09` | TField |  | Reserved for future use |
| 29 | `QI.ST.RESERVED.08` | `QiStatusType_Reserved08` | TField |  | Reserved for future use |
| 30 | `QI.ST.RESERVED.07` | `QiStatusType_Reserved07` | TField |  | Reserved for future use |
| 31 | `QI.ST.RESERVED.06` | `QiStatusType_Reserved06` | TField |  | Reserved for future use |
| 32 | `QI.ST.RESERVED.05` | `QiStatusType_Reserved05` | TField |  | Reserved for future use |
| 33 | `QI.ST.RESERVED.04` | `QiStatusType_Reserved04` | TField |  | Reserved for future use |
| 34 | `QI.ST.RESERVED.03` | `QiStatusType_Reserved03` | TField |  | Reserved for future use |
| 35 | `QI.ST.RESERVED.02` | `QiStatusType_Reserved02` | TField |  | Reserved for future use |
| 36 | `QI.ST.RESERVED.01` | `QiStatusType_Reserved01` | TField |  | Reserved for future use |
| 37 | `QI.ST.LOCAL.REF` | `QiStatusType_LocalRef` |  |  |  |
| 38 | `QI.ST.OVERRIDE` | `QiStatusType_Override` |  |  |  |
| 39 | `QI.ST.RECORD.STATUS` | `QiStatusType_RecordStatus` | String |  | Status of the record |
| 40 | `QI.ST.CURR.NO` | `QiStatusType_CurrNo` | String |  | Curr No |
| 41 | `QI.ST.INPUTTER` | `QiStatusType_Inputter` |  |  |  |
| 42 | `QI.ST.DATE.TIME` | `QiStatusType_DateTime` |  |  |  |
| 43 | `QI.ST.AUTHORISER` | `QiStatusType_Authoriser` | String |  | Authoriser |
| 44 | `QI.ST.CO.CODE` | `QiStatusType_CoCode` | String |  | Company code |
| 45 | `QI.ST.DEPT.CODE` | `QiStatusType_DeptCode` | String |  | Department code |
| 46 | `QI.ST.AUDITOR.CODE` | `QiStatusType_AuditorCode` | String |  | Auditor Code |
| 47 | `QI.ST.AUDIT.DATE.TIME` | `QiStatusType_AuditDateTime` | String |  | Audit Date and time |
