# INTERFACE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.INTERFACE.PARAMETER` in `CAINTR_InteracInstant.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INT.PARAM.PRE.LOCAL.API` | `InterfaceParameter_PreLocalApi` |  |  |  |
| 2 | `INT.PARAM.POST.LOCAL.API` | `InterfaceParameter_PostLocalApi` |  |  |  |
| 3 | `INT.PARAM.TPH.VALUE` | `InterfaceParameter_TphValue` |  |  |  |
| 4 | `INT.PARAM.LOCAL.VALUE` | `InterfaceParameter_LocalValue` |  |  |  |
| 5 | `INT.PARAM.COMPANY.TAG` | `InterfaceParameter_CompanyTag` |  |  |  |
| 6 | `INT.PARAM.ACCOUNT.TAG` | `InterfaceParameter_AccountTag` |  |  |  |
| 7 | `INT.PARAM.BRANCH.ACCOUNTING` | `InterfaceParameter_BranchAccounting` | TField |  | YES or NO field. |
| 8 | `INT.PARAM.DR.CR.INDICATOR` | `InterfaceParameter_DrCrIndicator` |  |  |  |
| 9 | `INT.PARAM.EXC.PROD.LINE` | `InterfaceParameter_ExcProdLine` |  |  |  |
| 10 | `INT.PARAM.EXC.PROD.GRP` | `InterfaceParameter_ExcProdGrp` |  |  |  |
| 11 | `INT.PARAM.EXC.PRODUCT` | `InterfaceParameter_ExcProduct` |  |  |  |
| 12 | `INT.PARAM.REQ.QUEUE` | `InterfaceParameter_ReqQueue` | TField |  | Field to store the OFS request to process the enquiry TPH.PAYMENT.INFO using the API defined in TPH.ENQ.API fieldFree textApplicable for SYSTEM record. |
| 13 | `INT.PARAM.RES.QUEUE` | `InterfaceParameter_ResQueue` | TField |  | Field to store the OFS Response for the enquiry TPH.PAYMENT.INFOFree textApplicable for SYSTEM record. |
| 14 | `INT.PARAM.CONN.FACTORY` | `InterfaceParameter_ConnFactory` | TField |  | Field to store the connection factory details used to process the enquiry - TPH.PAYMENT.INFOApplication for SYSTEM record. |
| 15 | `INT.PARAM.TPH.USERNAME` | `InterfaceParameter_TphUsername` | TField |  | Field to define the OFS user name to be used to process the enquiry TPH.PAYMENT.INFOApplicable for SYSTEM record. |
| 16 | `INT.PARAM.TPH.ENQ.API` | `InterfaceParameter_TphEnqApi` | TField |  | Field to define the valid API which will be called to execute the enquiry (ENQ TPH.PAYMENT.INFO) output from TPH system.Applicable for SYSTEM record. |
| 17 | `INT.PARAM.TPH.TIMEOUT` | `InterfaceParameter_TphTimeout` | TField |  | Field to define the Timeout value for connection to process the enquiry (ENQ TPH.PAYMENT.INFO) and get output from TPH system.Applicable for SYSTEM record. |
| 18 | `INT.PARAM.PRODUCT.LINE` | `InterfaceParameter_ProductLine` |  |  |  |
| 19 | `INT.PARAM.AA.PRODUCT.GROUP` | `InterfaceParameter_AaProductGroup` |  |  |  |
| 20 | `INT.PARAM.AA.PRODUCT` | `InterfaceParameter_AaProduct` |  |  |  |
| 21 | `INT.PARAM.PL.CATEGORY` | `InterfaceParameter_PlCategory` |  |  |  |
| 22 | `INT.PARAM.CR.TXN.CODE` | `InterfaceParameter_CrTransactionCode` |  |  |  |
| 23 | `INT.PARAM.DR.TXN.CODE` | `InterfaceParameter_DrTransactionCode` |  |  |  |
| 24 | `INT.PARAM.RESERVED.1` | `InterfaceParameter_Reserved1` |  |  |  |
| 25 | `INT.PARAM.RESERVED.2` | `InterfaceParameter_Reserved2` |  |  |  |
| 26 | `INT.PARAM.RESERVED.3` | `InterfaceParameter_Reserved3` |  |  |  |
| 27 | `INT.PARAM.RESERVED.4` | `InterfaceParameter_Reserved4` |  |  |  |
| 28 | `INT.PARAM.RESERVED.5` | `InterfaceParameter_Reserved5` |  |  |  |
| 29 | `INT.PARAM.REVERSAL.IDEN.TAG` | `InterfaceParameter_ReversalIdentificationTag` |  |  |  |
| 30 | `INT.PARAM.CHARGE.IDEN.TAG` | `InterfaceParameter_ChargeIdentificationTag` |  |  |  |
| 31 | `INT.PARAM.ORIGTXN.IDEN.TAG` | `InterfaceParameter_OriginaltxnIdentificationTag` |  |  |  |
| 32 | `INT.PARAM.RESERVED.6` | `InterfaceParameter_Reserved6` | TField |  |  |
| 33 | `INT.PARAM.RESERVED.7` | `InterfaceParameter_Reserved7` | TField |  |  |
| 34 | `INT.PARAM.RESERVED.8` | `InterfaceParameter_Reserved8` | TField |  |  |
| 35 | `INT.PARAM.RESERVED.9` | `InterfaceParameter_Reserved9` | TField |  |  |
| 36 | `INT.PARAM.RESERVED.10` | `InterfaceParameter_Reserved10` | TField |  |  |
| 37 | `INT.PARAM.OVERRIDE` | `InterfaceParameter_Override` |  |  |  |
| 38 | `INT.PARAM.RECORD.STATUS` | `InterfaceParameter_RecordStatus` | String |  |  |
| 39 | `INT.PARAM.CURR.NO` | `InterfaceParameter_CurrNo` | String |  |  |
| 40 | `INT.PARAM.INPUTTER` | `InterfaceParameter_Inputter` |  |  |  |
| 41 | `INT.PARAM.DATE.TIME` | `InterfaceParameter_DateTime` |  |  |  |
| 42 | `INT.PARAM.AUTHORISER` | `InterfaceParameter_Authoriser` | String |  |  |
| 43 | `INT.PARAM.CO.CODE` | `InterfaceParameter_CoCode` | String |  |  |
| 44 | `INT.PARAM.DEPT.CODE` | `InterfaceParameter_DeptCode` | String |  |  |
| 45 | `INT.PARAM.AUDITOR.CODE` | `InterfaceParameter_AuditorCode` | String |  |  |
| 46 | `INT.PARAM.AUDIT.DATE.TIME` | `InterfaceParameter_AuditDateTime` | String |  |  |
