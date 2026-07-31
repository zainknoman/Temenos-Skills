# INTRF.MAPPING — Table Schema

> Source: `INSERTS/I_F.INTRF.MAPPING` in `ATMFRM_Mapping.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INTRF.MAP.DESCRIPTION` | `IntrfMapping_Description` |  |  |  |
| 2 | `INTRF.MAP.MSG.TYPE` | `IntrfMapping_MsgType` | TField |  | Informative field displays whether the mapping is for Request, Response or Error |
| 3 | `INTRF.MAP.DELIMITER` | `IntrfMapping_Delimiter` | TField |  | For future Use |
| 4 | `INTRF.MAP.UPLOAD.PATH` | `IntrfMapping_UploadPath` | TField |  | For future Use |
| 5 | `INTRF.MAP.PRE.RTN` | `IntrfMapping_PreRtn` |  |  |  |
| 6 | `INTRF.MAP.APPLICATION` | `IntrfMapping_Application` | TField |  | Valid T24 application |
| 7 | `INTRF.MAP.OFS.FUNCTION` | `IntrfMapping_OfsFunction` | TField |  | Holds the OFS function for be performed while forming the OFS Request |
| 8 | `INTRF.MAP.OFS.OPERATION` | `IntrfMapping_OfsOperation` | TField |  | Holds the Processing Flag of either PROCESS or VALIDATE. |
| 9 | `INTRF.MAP.OFS.UTIL.NAME` | `IntrfMapping_OfsUtilName` | TField |  | This field will hold the version name or enquiry name to be used by OFS. |
| 10 | `INTRF.MAP.COMP.COD.MODE` | `IntrfMapping_CompCodMode` | TField |  | This field indicates which company the transaction has hit, the customer account company or the company to which the ATM machine is attached. This field holds the value CUST or ATM. This field holds SINGLE if there is a single lead company. |
| 11 | `INTRF.MAP.OFS.COM.CODE` | `IntrfMapping_OfsComCode` | TField |  | This field holds routine which loads the Company. If CUST is selected in above field, then Company Id is loaded based on customer account. If ATM is selected, then Company Id is loaded based on Company code configured in Terminal Routine can accept the value of configured data elements as first argument and returns Company Id as second argument. Routine name and arguments must be separated with either : or ^ symbol. Routine attached could be either: A jBC implementation by using an EB.API record with a source type of BASIC. For java implementations: An EB.API record id with a source type of HOOK which implements an interface defined in the EB.API record INTRF.MAPPING.OFS.COM.CODE.HOOK This field supports the AtmMessageLifecycle.getCompanyCode() method. The AtmMessageLifecycleclass is in the com.temenos.t24.api.hook.atm package which is in ATMFRM_MessageHook.jar shipped with T24. |
| 12 | `INTRF.MAP.ID.GEN` | `IntrfMapping_IdGen` | TField |  | Will accept Y or N contains information about the id of the application being updated by OFS. Customized Hook Routine can be attached here which helps to control an upcoming ATM reversal transaction including the function, transactionId and reversalAmount. Routine name and arguments must be separated with either : or ^ symbol. Routine attached could be either: A jBC implementation by using an EB.API record with a source type of BASIC. For java implementations: An EB.API record id with a source type of HOOK which implements an interface defined in the EB.API record INTRF.MAP.ID.GEN.HOOK This field supports the AtmMessageLifecycle.getTransactionData() method. The AtmMessageLifecycleclass is in the com.temenos.t24.api.hook.atm package which is in ATMFRM_MessageHook.jar shipped with T24. |
| 13 | `INTRF.MAP.OFS.USER` | `IntrfMapping_OfsUser` | TField |  | User Sign on to be used by OFS. |
| 14 | `INTRF.MAP.CLEARING.PARAM` | `IntrfMapping_ClearingParam` | TField |  | Valid AC.ENTRY.PARAM Id |
| 15 | `INTRF.MAP.RES.MAP.ID` | `IntrfMapping_ResMapId` | TField |  | Response mapping id for the request |
| 16 | `INTRF.MAP.INTRF.FLD.NAME` | `IntrfMapping_IntrfFldName` |  |  |  |
| 17 | `INTRF.MAP.INTRF.FLD.PS` | `IntrfMapping_IntrfFldPs` |  |  |  |
| 18 | `INTRF.MAP.GLO.FLD.NAME` | `IntrfMapping_GloFldName` |  |  |  |
| 19 | `INTRF.MAP.GLO.FLD.LN.TYPE` | `IntrfMapping_GloFldLnType` |  |  |  |
| 20 | `INTRF.MAP.GLO.CONSTANT` | `IntrfMapping_GloConstant` |  |  |  |
| 21 | `INTRF.MAP.FIELD.SOURCE` | `IntrfMapping_FieldSource` |  |  |  |
| 22 | `INTRF.MAP.FIELD.SRC.VALUE` | `IntrfMapping_FieldSrcValue` |  |  |  |
| 23 | `INTRF.MAP.RESERVED.5` | `IntrfMapping_Reserved5` |  |  |  |
| 24 | `INTRF.MAP.RESERVED.4` | `IntrfMapping_Reserved4` |  |  |  |
| 25 | `INTRF.MAP.RESERVED.3` | `IntrfMapping_Reserved3` |  |  |  |
| 26 | `INTRF.MAP.RESERVED.2` | `IntrfMapping_Reserved2` |  |  |  |
| 27 | `INTRF.MAP.RESERVED.1` | `IntrfMapping_Reserved1` |  |  |  |
| 28 | `INTRF.MAP.RES.Y.N` | `IntrfMapping_ResYN` | TField |  | This field holds the value of Y or N decides Currently not used. For future use . |
| 29 | `INTRF.MAP.ERROR.CONV.TAB` | `IntrfMapping_ErrorConvTab` | TField |  | For future use in error mapping |
| 30 | `INTRF.MAP.TYPE.OF.TXN` | `IntrfMapping_TypeOfTxn` | TField | Yes | This field holds the value of ENQ or FIN or ACT decides whether the transaction is Enquiry or Financial or Acct to Acct transactions. Mandatory field for non-financial request mapping record with value as ENQ. |
| 31 | `INTRF.MAP.TXN.CODE` | `IntrfMapping_TxnCode` | TField |  | This field holds the TRANSACTION code with which the transaction has to be booked. |
| 32 | `INTRF.MAP.MESSAGE.ID` | `IntrfMapping_MessageId` |  |  |  |
| 33 | `INTRF.MAP.RESERVED.15` | `IntrfMapping_Reserved15` | TField |  |  |
| 34 | `INTRF.MAP.RESERVED.14` | `IntrfMapping_Reserved14` | TField |  |  |
| 35 | `INTRF.MAP.RESERVED.13` | `IntrfMapping_Reserved13` | TField |  |  |
| 36 | `INTRF.MAP.RESERVED.12` | `IntrfMapping_Reserved12` | TField |  |  |
| 37 | `INTRF.MAP.RESERVED.11` | `IntrfMapping_Reserved11` | TField |  |  |
| 38 | `INTRF.MAP.LOCAL.REF` | `IntrfMapping_LocalRef` |  |  |  |
| 39 | `INTRF.MAP.RESERVED.10` | `IntrfMapping_Reserved10` | TField |  |  |
| 40 | `INTRF.MAP.RESERVED.9` | `IntrfMapping_Reserved9` | TField |  |  |
| 41 | `INTRF.MAP.RESERVED.8` | `IntrfMapping_Reserved8` | TField |  |  |
| 42 | `INTRF.MAP.RESERVED.7` | `IntrfMapping_Reserved7` | TField |  |  |
| 43 | `INTRF.MAP.RESERVED.6` | `IntrfMapping_Reserved6` | TField |  |  |
| 44 | `INTRF.MAP.RECORD.STATUS` | `IntrfMapping_RecordStatus` | String |  |  |
| 45 | `INTRF.MAP.CURR.NO` | `IntrfMapping_CurrNo` | String |  |  |
| 46 | `INTRF.MAP.INPUTTER` | `IntrfMapping_Inputter` |  |  |  |
| 47 | `INTRF.MAP.DATE.TIME` | `IntrfMapping_DateTime` |  |  |  |
| 48 | `INTRF.MAP.AUTHORISER` | `IntrfMapping_Authoriser` | String |  |  |
| 49 | `INTRF.MAP.CO.CODE` | `IntrfMapping_CoCode` | String |  |  |
| 50 | `INTRF.MAP.DEPT.CODE` | `IntrfMapping_DeptCode` | String |  |  |
| 51 | `INTRF.MAP.AUDITOR.CODE` | `IntrfMapping_AuditorCode` | String |  |  |
| 52 | `INTRF.MAP.AUDIT.DATE.TIME` | `IntrfMapping_AuditDateTime` | String |  |  |
