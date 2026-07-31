# CZ.CDP.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CZ.CDP.PARAMETER` in `CZ_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CZ.CDP.PAR.CDP.RULE` | `CzCdpParameter_CdpRule` | TField |  | This field denotes the rules for CDP processing which can be defined through the Rules Engine. This rule is used to determine the eligibility of the customer for CDP processing Validation Rule: Valid ID from EB.RULE.GATEWAY. Both CDP.RULE and CDP.API are mutually exclusive |
| 2 | `CZ.CDP.PAR.CDP.API` | `CzCdpParameter_CdpApi` | TField |  | This field allow the user to plug-in an API with the logic to define the rules of CDP. This API is used to determine the eligibility of the customer for CDP processing Validation Rule: A valid record in EB.API table.This API must have 4 arguments. CustomerID and CustomerRecord are input arguments and CdpEligiblity and ErrorMsg are output arguments. Both CDP.RULE and CDP.API are mutually exclusive |
| 3 | `CZ.CDP.PAR.ERASURE.TRIGGER` | `CzCdpParameter_ErasureTrigger` | TField |  | The field defines how the erasure process should be triggered either automatically or will require approval for triggering manually. Validation Rule: Possible values are Auto or Manual or None. Auto means the erasure process will be triggered automatically.Manual which means the erasure process will be triggered manually NONE means that the erasure trigger will be requested from external and the client has different banking system to handle this GDPR regulation |
| 4 | `CZ.CDP.PAR.OVERRIDE.ERROR` | `CzCdpParameter_OverrideError` | TField |  | The field denotes the action to be taken if the customer is not eligible for CDP. Validation Rule: Possible values are Override or Error. If Override, then Non-GDPR customer request can proceed further for approval or it might as well get rejected. If Error, then Non-GDPR customer request gets rejected |
| 5 | `CZ.CDP.PAR.BUILD.ERASURE.LOG` | `CzCdpParameter_BuildErasureLog` | TField |  | If this field is set, the data erased as part of the CDP processing will be logged within the file CZ.CDP.DATA.ERASED.TODAY If the field is set to Yes, the data erased as part of CUSTOMER erasure will be captured. This refers to applications with PARTY.APPLICATION set as CUSTOMER in CZ.CDP.DATA.DEFINITION. If the field is set to Full, the data erased as part of both CUSTOMER and TRANSACTION erasure will be logged. This refers to all the applciations with PARTY.APPLICATION set as CUSTOMER and TRANSACTION in CZ.CDP.DATA.DEFINITION. This file CZ.CDP.DATA.ERASED.TODAY shall be used for reporting purposes or to send data extracts to other third party systems. The table update will be switched off if the field is set as Null. Validation Rule: It will accept Yes or Null or Full. |
| 6 | `CZ.CDP.PAR.ACTIVITY.MOVED` | `CzCdpParameter_ActivityMoved` | TField |  | This field will be updated when all the CZ customer activity related information is moved to ST Customer Activity by the System. Applicable only in case of conversion during upgrade. Validation Rule: No-Input field. Internal use only. |
| 7 | `CZ.CDP.PAR.ALLOW.ACTIVE.ERASURE` | `CzCdpParameter_AllowActiveErasure` | TField |  | Erasure of personal data can be requested for customers who are still active. In order to enable the functionality, this field needs to be set to YES. The data to be erased when a customer is still active are required to be attached to purposes that are only allowed for active erasure. The entire functionality is turned on by this field only when set to YES. Validation Rule: Allowed values are YES_NO. Default value is Null and is considered equivalent to NO. |
| 8 | `CZ.CDP.PAR.ALLOW.CONTRACT.ERASURE` | `CzCdpParameter_AllowContractErasure` | TField |  | Erasure of personal data on a contract of a customer can be requested if the contract is deemed inactive. The contract erasure functionality is enabled by this field when set to YES. Validation Rule: To set this field to YES, it is required that the field ALLOW.ACTIVE.ERASURE to be set to YES. Allowed values are YES_NO. Default value is Null and is considered equivalent to NO. |
| 9 | `CZ.CDP.PAR.CONT.ERASURE.PURPOSES` | `CzCdpParameter_ContErasurePurposes` |  |  |  |
| 10 | `CZ.CDP.PAR.CONT.ERASURE.APPLN` | `CzCdpParameter_ContErasureAppln` |  |  |  |
| 11 | `CZ.CDP.PAR.APP.RETENTION.PERIOD` | `CzCdpParameter_AppRetentionPeriod` |  |  |  |
| 12 | `CZ.CDP.PAR.APP.RET.PERIOD.API` | `CzCdpParameter_AppRetPeriodApi` |  |  |  |
| 13 | `CZ.CDP.PAR.APP.RET.PERIOD.RULE` | `CzCdpParameter_AppRetPeriodRule` |  |  |  |
| 14 | `CZ.CDP.PAR.LOCAL.REF` | `CzCdpParameter_LocalRef` |  |  |  |
| 15 | `CZ.CDP.PAR.OVERRIDE` | `CzCdpParameter_Override` |  |  |  |
| 16 | `CZ.CDP.PAR.RECORD.STATUS` | `CzCdpParameter_RecordStatus` | String |  |  |
| 17 | `CZ.CDP.PAR.CURR.NO` | `CzCdpParameter_CurrNo` | String |  |  |
| 18 | `CZ.CDP.PAR.INPUTTER` | `CzCdpParameter_Inputter` |  |  |  |
| 19 | `CZ.CDP.PAR.DATE.TIME` | `CzCdpParameter_DateTime` |  |  |  |
| 20 | `CZ.CDP.PAR.AUTHORISER` | `CzCdpParameter_Authoriser` | String |  |  |
| 21 | `CZ.CDP.PAR.CO.CODE` | `CzCdpParameter_CoCode` | String |  |  |
| 22 | `CZ.CDP.PAR.DEPT.CODE` | `CzCdpParameter_DeptCode` | String |  |  |
| 23 | `CZ.CDP.PAR.AUDITOR.CODE` | `CzCdpParameter_AuditorCode` | String |  |  |
| 24 | `CZ.CDP.PAR.AUDIT.DATE.TIME` | `CzCdpParameter_AuditDateTime` | String |  |  |
| 25 | `CZ.CDP.PAR.PRST.RET.FLD.NAM` | `CzCdpParameter_PrstRetFldNam` |  |  |  |
| 26 | `CZ.CDP.PAR.PRST.RET.FLD.VAL` | `CzCdpParameter_PrstRetFldVal` |  |  |  |
| 27 | `CZ.CDP.PAR.PRST.FLD.RSVD.15` | `CzCdpParameter_PrstFldRsvd15` |  |  |  |
| 28 | `CZ.CDP.PAR.PRST.FLD.RSVD.14` | `CzCdpParameter_PrstFldRsvd14` |  |  |  |
| 29 | `CZ.CDP.PAR.PRST.FLD.RSVD.13` | `CzCdpParameter_PrstFldRsvd13` |  |  |  |
| 30 | `CZ.CDP.PAR.PRST.FLD.RSVD.12` | `CzCdpParameter_PrstFldRsvd12` |  |  |  |
| 31 | `CZ.CDP.PAR.PRST.FLD.RSVD.11` | `CzCdpParameter_PrstFldRsvd11` |  |  |  |
| 32 | `CZ.CDP.PAR.PRST.FLD.RSVD.10` | `CzCdpParameter_PrstFldRsvd10` |  |  |  |
| 33 | `CZ.CDP.PAR.PRST.FLD.RSVD.09` | `CzCdpParameter_PrstFldRsvd09` |  |  |  |
| 34 | `CZ.CDP.PAR.PRST.FLD.RSVD.08` | `CzCdpParameter_PrstFldRsvd08` |  |  |  |
| 35 | `CZ.CDP.PAR.PRST.FLD.RSVD.07` | `CzCdpParameter_PrstFldRsvd07` |  |  |  |
| 36 | `CZ.CDP.PAR.PRST.FLD.RSVD.06` | `CzCdpParameter_PrstFldRsvd06` |  |  |  |
| 37 | `CZ.CDP.PAR.PRST.FLD.RSVD.05` | `CzCdpParameter_PrstFldRsvd05` |  |  |  |
| 38 | `CZ.CDP.PAR.PRST.FLD.RSVD.04` | `CzCdpParameter_PrstFldRsvd04` |  |  |  |
| 39 | `CZ.CDP.PAR.PRST.FLD.RSVD.03` | `CzCdpParameter_PrstFldRsvd03` |  |  |  |
| 40 | `CZ.CDP.PAR.PRST.FLD.RSVD.02` | `CzCdpParameter_PrstFldRsvd02` |  |  |  |
| 41 | `CZ.CDP.PAR.PRST.FLD.RSVD.01` | `CzCdpParameter_PrstFldRsvd01` |  |  |  |
| 42 | `CZ.CDP.PAR.PRST.DEF.RET.PERIOD` | `CzCdpParameter_PrstDefRetPeriod` |  |  |  |
| 43 | `CZ.CDP.PAR.PRST.REQ.RET.PERIOD` | `CzCdpParameter_PrstReqRetPeriod` |  |  |  |
| 44 | `CZ.CDP.PAR.PRST.RET.RSVD.15` | `CzCdpParameter_PrstRetRsvd15` |  |  |  |
| 45 | `CZ.CDP.PAR.PRST.RET.RSVD.14` | `CzCdpParameter_PrstRetRsvd14` |  |  |  |
| 46 | `CZ.CDP.PAR.PRST.RET.RSVD.13` | `CzCdpParameter_PrstRetRsvd13` |  |  |  |
| 47 | `CZ.CDP.PAR.PRST.RET.RSVD.12` | `CzCdpParameter_PrstRetRsvd12` |  |  |  |
| 48 | `CZ.CDP.PAR.PRST.RET.RSVD.11` | `CzCdpParameter_PrstRetRsvd11` |  |  |  |
| 49 | `CZ.CDP.PAR.PRST.RET.RSVD.10` | `CzCdpParameter_PrstRetRsvd10` |  |  |  |
| 50 | `CZ.CDP.PAR.PRST.RET.RSVD.09` | `CzCdpParameter_PrstRetRsvd09` |  |  |  |
| 51 | `CZ.CDP.PAR.PRST.RET.RSVD.08` | `CzCdpParameter_PrstRetRsvd08` |  |  |  |
| 52 | `CZ.CDP.PAR.PRST.RET.RSVD.07` | `CzCdpParameter_PrstRetRsvd07` |  |  |  |
| 53 | `CZ.CDP.PAR.PRST.RET.RSVD.06` | `CzCdpParameter_PrstRetRsvd06` |  |  |  |
| 54 | `CZ.CDP.PAR.PRST.RET.RSVD.05` | `CzCdpParameter_PrstRetRsvd05` |  |  |  |
| 55 | `CZ.CDP.PAR.PRST.RET.RSVD.04` | `CzCdpParameter_PrstRetRsvd04` |  |  |  |
| 56 | `CZ.CDP.PAR.PRST.RET.RSVD.03` | `CzCdpParameter_PrstRetRsvd03` |  |  |  |
| 57 | `CZ.CDP.PAR.PRST.RET.RSVD.02` | `CzCdpParameter_PrstRetRsvd02` |  |  |  |
| 58 | `CZ.CDP.PAR.PRST.RET.RSVD.01` | `CzCdpParameter_PrstRetRsvd01` |  |  |  |
| 59 | `CZ.CDP.PAR.ERASURE.METHOD` | `CzCdpParameter_ErasureMethod` | TField | Yes | The field decides the type of erasure to be set for the system. COMPLETE � Where this is set, all customer data will be anonymised at the same time. If this field is set it will be mandatory for the bank to define the retention periods/erasure logic at the parameter level. PHASED � Where this is set, the phased/purpose retention period will be used for erasure. If the field is set to PHASED, the parameter level retention defintions are not allowed. Null� This is the same as PHASED. This will accommodate for and maintain functionality for existing, upgrading clients. Validation Rule: During first time input of CZ.CDP.PARAMETER ,it is mandatory to define this field. If left null, PHASED erasure will be considered. This cannot be later changed once the parameter record is authorised. |
| 60 | `CZ.CDP.PAR.CUST.RET.FLD.NAM` | `CzCdpParameter_CustRetFldNam` |  |  |  |
| 61 | `CZ.CDP.PAR.CUST.RET.FLD.VAL` | `CzCdpParameter_CustRetFldVal` |  |  |  |
| 62 | `CZ.CDP.PAR.CUST.RET.FLD.RSVD.15` | `CzCdpParameter_CustRetFldRsvd15` |  |  |  |
| 63 | `CZ.CDP.PAR.CUST.RET.FLD.RSVD.14` | `CzCdpParameter_CustRetFldRsvd14` |  |  |  |
| 64 | `CZ.CDP.PAR.CUST.RET.FLD.RSVD.13` | `CzCdpParameter_CustRetFldRsvd13` |  |  |  |
| 65 | `CZ.CDP.PAR.CUST.RET.FLD.RSVD.12` | `CzCdpParameter_CustRetFldRsvd12` |  |  |  |
| 66 | `CZ.CDP.PAR.CUST.RET.FLD.RSVD.11` | `CzCdpParameter_CustRetFldRsvd11` |  |  |  |
| 67 | `CZ.CDP.PAR.CUST.RET.FLD.RSVD.10` | `CzCdpParameter_CustRetFldRsvd10` |  |  |  |
| 68 | `CZ.CDP.PAR.CUST.RET.FLD.RSVD.09` | `CzCdpParameter_CustRetFldRsvd09` |  |  |  |
| 69 | `CZ.CDP.PAR.CUST.RET.FLD.RSVD.08` | `CzCdpParameter_CustRetFldRsvd08` |  |  |  |
| 70 | `CZ.CDP.PAR.CUST.RET.FLD.RSVD.07` | `CzCdpParameter_CustRetFldRsvd07` |  |  |  |
| 71 | `CZ.CDP.PAR.CUST.RET.FLD.RSVD.06` | `CzCdpParameter_CustRetFldRsvd06` |  |  |  |
| 72 | `CZ.CDP.PAR.CUST.RET.FLD.RSVD.05` | `CzCdpParameter_CustRetFldRsvd05` |  |  |  |
| 73 | `CZ.CDP.PAR.CUST.RET.FLD.RSVD.04` | `CzCdpParameter_CustRetFldRsvd04` |  |  |  |
| 74 | `CZ.CDP.PAR.CUST.RET.FLD.RSVD.03` | `CzCdpParameter_CustRetFldRsvd03` |  |  |  |
| 75 | `CZ.CDP.PAR.CUST.RET.FLD.RSVD.02` | `CzCdpParameter_CustRetFldRsvd02` |  |  |  |
| 76 | `CZ.CDP.PAR.CUST.RET.FLD.RSVD.01` | `CzCdpParameter_CustRetFldRsvd01` |  |  |  |
| 77 | `CZ.CDP.PAR.CUST.RET.PERIOD` | `CzCdpParameter_CustRetPeriod` |  |  |  |
| 78 | `CZ.CDP.PAR.CUST.RET.RSVD.15` | `CzCdpParameter_CustRetRsvd15` |  |  |  |
| 79 | `CZ.CDP.PAR.CUST.RET.RSVD.14` | `CzCdpParameter_CustRetRsvd14` |  |  |  |
| 80 | `CZ.CDP.PAR.CUST.RET.RSVD.13` | `CzCdpParameter_CustRetRsvd13` |  |  |  |
| 81 | `CZ.CDP.PAR.CUST.RET.RSVD.12` | `CzCdpParameter_CustRetRsvd12` |  |  |  |
| 82 | `CZ.CDP.PAR.CUST.RET.RSVD.11` | `CzCdpParameter_CustRetRsvd11` |  |  |  |
| 83 | `CZ.CDP.PAR.CUST.RET.RSVD.10` | `CzCdpParameter_CustRetRsvd10` |  |  |  |
| 84 | `CZ.CDP.PAR.CUST.RET.RSVD.09` | `CzCdpParameter_CustRetRsvd09` |  |  |  |
| 85 | `CZ.CDP.PAR.CUST.RET.RSVD.08` | `CzCdpParameter_CustRetRsvd08` |  |  |  |
| 86 | `CZ.CDP.PAR.CUST.RET.RSVD.07` | `CzCdpParameter_CustRetRsvd07` |  |  |  |
| 87 | `CZ.CDP.PAR.CUST.RET.RSVD.06` | `CzCdpParameter_CustRetRsvd06` |  |  |  |
| 88 | `CZ.CDP.PAR.CUST.RET.RSVD.05` | `CzCdpParameter_CustRetRsvd05` |  |  |  |
| 89 | `CZ.CDP.PAR.CUST.RET.RSVD.04` | `CzCdpParameter_CustRetRsvd04` |  |  |  |
| 90 | `CZ.CDP.PAR.CUST.RET.RSVD.03` | `CzCdpParameter_CustRetRsvd03` |  |  |  |
| 91 | `CZ.CDP.PAR.CUST.RET.RSVD.02` | `CzCdpParameter_CustRetRsvd02` |  |  |  |
| 92 | `CZ.CDP.PAR.CUST.RET.RSVD.01` | `CzCdpParameter_CustRetRsvd01` |  |  |  |
| 93 | `CZ.CDP.PAR.CUST.PROD.CAT` | `CzCdpParameter_CustProdCat` |  |  |  |
| 94 | `CZ.CDP.PAR.CUST.PROD.CAT.RET.PER` | `CzCdpParameter_CustProdCatRetPer` |  |  |  |
| 95 | `CZ.CDP.PAR.CUST.CAT.RSVD.15` | `CzCdpParameter_CustCatRsvd15` |  |  |  |
| 96 | `CZ.CDP.PAR.CUST.CAT.RSVD.14` | `CzCdpParameter_CustCatRsvd14` |  |  |  |
| 97 | `CZ.CDP.PAR.CUST.CAT.RSVD.13` | `CzCdpParameter_CustCatRsvd13` |  |  |  |
| 98 | `CZ.CDP.PAR.CUST.CAT.RSVD.12` | `CzCdpParameter_CustCatRsvd12` |  |  |  |
| 99 | `CZ.CDP.PAR.CUST.CAT.RSVD.11` | `CzCdpParameter_CustCatRsvd11` |  |  |  |
| 100 | `CZ.CDP.PAR.CUST.CAT.RSVD.10` | `CzCdpParameter_CustCatRsvd10` |  |  |  |
| 101 | `CZ.CDP.PAR.CUST.CAT.RSVD.09` | `CzCdpParameter_CustCatRsvd09` |  |  |  |
| 102 | `CZ.CDP.PAR.CUST.CAT.RSVD.08` | `CzCdpParameter_CustCatRsvd08` |  |  |  |
| 103 | `CZ.CDP.PAR.CUST.CAT.RSVD.07` | `CzCdpParameter_CustCatRsvd07` |  |  |  |
| 104 | `CZ.CDP.PAR.CUST.CAT.RSVD.06` | `CzCdpParameter_CustCatRsvd06` |  |  |  |
| 105 | `CZ.CDP.PAR.CUST.CAT.RSVD.05` | `CzCdpParameter_CustCatRsvd05` |  |  |  |
| 106 | `CZ.CDP.PAR.CUST.CAT.RSVD.04` | `CzCdpParameter_CustCatRsvd04` |  |  |  |
| 107 | `CZ.CDP.PAR.CUST.CAT.RSVD.03` | `CzCdpParameter_CustCatRsvd03` |  |  |  |
| 108 | `CZ.CDP.PAR.CUST.CAT.RSVD.02` | `CzCdpParameter_CustCatRsvd02` |  |  |  |
| 109 | `CZ.CDP.PAR.CUST.CAT.RSVD.01` | `CzCdpParameter_CustCatRsvd01` |  |  |  |
| 110 | `CZ.CDP.PAR.RET.PRIORITY` | `CzCdpParameter_RetPriority` | TField | Yes | This field defines which criteria takes priority when calculating the overall erasure date of a Customer. Allowed options are: � CUSTOMER � Uses only the Customer related criteria to calculate the erasure date.The erasure date is calculated from the Inactive Since Date for the Customer using the Customer Retention Period and is irrespective of the products held by the Customer. � PRODUCT � Uses only the Product level criteria to calculate the erasure date. The calculation of erasure date logic involves calculating erasure date for all the contracts and taking the longest (or the most future date) from them. The erasure date for each contract is arrived by adding the product retention period from Completed or Delinked Date of the respective contract. The calculation does not consider the customer retention criteria. � LATEST.DATE � Uses the most future date of both the Customer level and Product level criteria as the erasure date for the Customer. Validation: � Where any of the above fields (related to customer and/or product retention periods) are configured, this field is mandatory to be input by a user. � Only allowed input when ERASURE.METHOD is COMPLETE. � Allows values CUSTOMER, PRODUCT, LATEST.DATE and (null). |
| 111 | `CZ.CDP.PAR.TXN.APPLICATION` | `CzCdpParameter_TxnApplication` |  |  |  |
| 112 | `CZ.CDP.PAR.TXN.APP.RET.PERIOD` | `CzCdpParameter_TxnAppRetPeriod` |  |  |  |
| 113 | `CZ.CDP.PAR.TXN.APP.RET.API` | `CzCdpParameter_TxnAppRetApi` |  |  |  |
| 114 | `CZ.CDP.PAR.TXN.APP.RET.RULE` | `CzCdpParameter_TxnAppRetRule` |  |  |  |
