# CAMB.MEM.DIR.PARAM — Table Schema

> Source: `INSERTS/I_F.CAMB.MEM.DIR.PARAM` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.MEM.PRODUCT.ID` | `CambMemDirParam_ProductId` | TField |  | This field will have either "MEMBER.NO" or "PAN", If it is set to MEMBER.NO number then system will use the Member Number for constructing the Product id and if PAN is set then system will use incoming PAN number for constructing the product id. Eg: PAN, MEMBER.NO |
| 2 | `CAMB.MEM.LOG.FILE.DIR` | `CambMemDirParam_LogFileDir` | TField |  | This field used to parameterise directory through which the transaction exceptions to be raised. Eg: MDIDIR |
| 3 | `CAMB.MEM.LOG.FILENAME` | `CambMemDirParam_LogFilename` | TField |  | This field used to parameterise a file name were the transaction exceptions should be logged. Eg: LOGMDI |
| 4 | `CAMB.MEM.PAC.MIN.LEN` | `CambMemDirParam_PacMinLen` | TField |  | This field used to parameterise the minimum PAC length. This field value will be used for validation while updating PAC in CARD.ISSUE Eg: 5 |
| 5 | `CAMB.MEM.PAC.MAX.LEN` | `CambMemDirParam_PacMaxLen` | TField |  | This field used to parameterise the maximum PAC length. This field value will be used for validation while updating PAC in CARD.ISSUE Eg: 8 |
| 6 | `CAMB.MEM.TRANSIT` | `CambMemDirParam_Transit` | TField |  | This field used to parameterise transit number which will be used to form the UMID. The UMID is a unique id used to identify a customer among several other bank customers. This transit number is unique for every bank. Eg: 100 |
| 7 | `CAMB.MEM.ROUTE` | `CambMemDirParam_Route` | TField |  | This field used to parameterise route number which will be used to form the UMID. The UMID is a unique id used to identify a customer among several other bank customers. Eg: 999 |
| 8 | `CAMB.MEM.CUS.UMID.LEN` | `CambMemDirParam_CusUmidLen` | TField |  | This field used to parameterise the length of UMID which is to be returned as part of Member Direct Login response. Eg: 15 |
| 9 | `CAMB.MEM.EXC.CARD.STATUS` | `CambMemDirParam_ExcCardStatus` |  |  |  |
| 10 | `CAMB.MEM.INTEND.DESC` | `CambMemDirParam_IntendDesc` |  |  |  |
| 11 | `CAMB.MEM.INTEND.CODE` | `CambMemDirParam_IntendCode` |  |  |  |
| 12 | `CAMB.MEM.DFT.INTEND.CODE` | `CambMemDirParam_DftIntendCode` | TField |  | This field used to parameterise the default Intended use in case if there is no value from the above INTEND.DESC description matching with Account creation ISO request. Eg: 00 |
| 13 | `CAMB.MEM.FE.CHANNEL` | `CambMemDirParam_FeChannel` | TField |  | For future purpose |
| 14 | `CAMB.MEM.ACCT.TITLE.FLD` | `CambMemDirParam_AcctTitleFld` | TField |  | This field value used to parameterise field name of account which will be used while updating the account title and displaying in Member Direct screen. For Ex: SHORT.TITLE |
| 15 | `CAMB.MEM.ACCT.ID.DESC.FLAG` | `CambMemDirParam_AcctIdDescFlag` | TField |  | This is introduced for returning Account Id as part of Account Description for MDB. Possible values are "YES" or "NO". YES - Return Account id along with account title as a part of Product summary response NO - Return only account title as part of product summary response |
| 16 | `CAMB.MEM.INT.MEM.ACCT.DEF` | `CambMemDirParam_IntMemAcctDef` | TField |  | For future purpose |
| 17 | `CAMB.MEM.IVR.CHG.PAC.IND` | `CambMemDirParam_IvrChgPacInd` | TField |  | This field used to parameterise whether the PAC for IVR interface needs to be updated when the PAC for MDI will get updated. Possible values are "YES" or "NO" YES - PAC for IVR interface will get updated in CARD.ISSUE when the PAC for MDI will get updated. NO or Null - Only MDI PAC will get updated. |
| 18 | `CAMB.MEM.LOAN.OD.STATUS` | `CambMemDirParam_LoanOdStatus` |  |  |  |
| 19 | `CAMB.MEM.PAYOFFPEN.PROPERTY` | `CambMemDirParam_PayoffpenProperty` |  |  |  |
| 20 | `CAMB.MEM.OPEN.PAY.METHOD` | `CambMemDirParam_OpenPayMethod` | TField |  | This field used to define 2 digit numeric value to denote the open pay method Eg: 11 |
| 21 | `CAMB.MEM.CLOSED.PAY.METHOD` | `CambMemDirParam_ClosedPayMethod` | TField |  | This field used to define 2 digit numeric value to denote the closed pay method Eg: 12 |
| 22 | `CAMB.MEM.LOC.LIMIT` | `CambMemDirParam_LocLimit` | TField |  | This field used to denote whether LOC limit details attached to the product needs to be sent in product summary response to Central1 or not. Possible values are "YES" or "NO" YES - LOC limit values like next payment date, Payment amount, Deliquent date, deliquent amount will be send NO - LOC limit values will not be send to Central 1 |
| 23 | `CAMB.MEM.ZERO.PAC.VAL` | `CambMemDirParam_ZeroPacVal` | TField |  | This field used to define whether leading 0's in the PAC needs to be validated when the PAC is updated for IVR interface in CARD.ISSUE. Possible values are "YES" or "NO" YES - An override will be thrown if leading 0's are entered. Eg: 012345 NO or Null - No override will be raised and system allowes to enter the PAC |
| 24 | `CAMB.MEM.OFS.USER` | `CambMemDirParam_OfsUser` | TField |  | This field used to define a primary sign on name used to post the OFS messages to T24 for MDI ISO requests. Eg: MDI.USER |
| 25 | `CAMB.MEM.OFS.PASSWORD` | `CambMemDirParam_OfsPassword` | TField |  | The field is no longer in use, as it has become obsolete. |
| 26 | `CAMB.MEM.IMT.EXT.TYPE` | `CambMemDirParam_ImtExtType` | TField |  | The purpose of this field is to get the id of INTRF.EXT.FT table to fetch the account numbers belongs to other customers for which the customer should be able to transfer to. Possible values are CIF and PAN CIF - Customer id should be the @id of INTRF.EXT.FT table PAN - PAN no will be the @id of INTRF.EXT.FT table If it is blank then by default customer id will be used as @id. This combinations of id is only for MDI interface. For IVR it will always be customer id. |
| 27 | `CAMB.MEM.USE.ORIG.PROD` | `CambMemDirParam_UseOrigProd` | TField |  | This field used to defeine whether mdi product type and category to be send to central1 one based on the T24 accounts initial product or based on current product. Possible values are "YES" or "NO" Eg: The current product of the account is SAVINGS.CAD and its equalent mdi product id DMDC-10001. The initial product of the same account is STUDENT.SAVINGS.CAD and its equalent mdi product id as DMDC-10002 If this field is set to YES then DMDC-10002 will be send to Central1. If this field is set to NO or null then DMDC-10001 will be send to Central1 |
| 28 | `CAMB.MEM.SIG.REQ.PROC.CODES` | `CambMemDirParam_SigReqProcCodes` |  |  |  |
| 29 | `CAMB.MEM.CHARGE.TYPE` | `CambMemDirParam_ChargeType` | TField |  | This field used to define whether the charge for initiating stop payment on cheque should be per cheque or per transaction. Possible values are PER.CHEQUE or TRANSACTION PER.CHEQUE - Charges will be applied for each cheque TRANSACTION - Charges will be applied per PAYMENT.STOP record |
| 30 | `CAMB.MEM.FX.CCY.MKT` | `CambMemDirParam_FxCcyMkt` | TField |  | This field used to defeine currency market which is going to used when the foreign currency transaction is initiated from MDI. This currency market will be used if the credit currency is not a local currency. It should be a valid record from CURRENCY.MARKET table. Eg: 1 |
| 31 | `CAMB.MEM.LMI.DISP.PRODS` | `CambMemDirParam_LmiDispProds` |  |  |  |
| 32 | `CAMB.MEM.BUS.CARD.HLD.FLG` | `CambMemDirParam_BusCardHldFlg` | TField |  | This field is used to define how the system is going to identify the business card holders list. This field value is applicable only if the PRODUCT.ID value is PAN. Possible values are AA.ARRANGEMENT and CUSTOMER. AA.ARRANGEMENT - All related customers at account level will be taken to compare their industry against CAPL.H.CUS.TYPE.PARAM>MDSB.IND.AL. If it is matched then those customers will be considered as business card holders. CUSTOMER - ll related customers at customer level will be taken to compare their relation code against CAPL.H.SIGNATORY.RULE>CAPL.SR.PROD.SIGN.REL.CODE. If it is matched then those customers will be considered as business card holders. |
| 33 | `CAMB.MEM.SSO.LOGIN.CUTOFF` | `CambMemDirParam_SsoLoginCutoff` | TField |  | This field used to parameterise the cutoff seconds for single signon request from MDI. So this seconds should be the difference between the current system time at the time of MDI login request and timestamp value in CARD.ISSUE record which was updated by TCIB for PAC update. If the difference is less than or equal then the login will be allowed based on PAC validation else login request will get failed. Eg: 7 |
| 34 | `CAMB.MEM.LOGIN.MEM.ORDER` | `CambMemDirParam_LoginMemOrder` | TField |  |  |
| 35 | `CAMB.MEM.NETWORK.ID` | `CambMemDirParam_NetworkId` |  |  |  |
| 36 | `CAMB.MEM.STATIC.PAC` | `CambMemDirParam_StaticPac` |  |  |  |
| 37 | `CAMB.MEM.CUS.TYPE` | `CambMemDirParam_CusType` |  |  |  |
| 38 | `CAMB.MEM.EX.ACS.TYPE` | `CambMemDirParam_ExAcsType` |  |  |  |
| 39 | `CAMB.MEM.EX.ACCT.NO.ACS` | `CambMemDirParam_ExAcctNoAcs` | TField |  |  |
| 40 | `CAMB.MEM.MD.STOP.TYPE` | `CambMemDirParam_MdStopType` |  |  |  |
| 41 | `CAMB.MEM.PAYMENT.STOP.TYPE` | `CambMemDirParam_PaymentStopType` |  |  |  |
| 42 | `CAMB.MEM.CHEQUE.TYPE` | `CambMemDirParam_ChequeType` |  |  |  |
| 43 | `CAMB.MEM.INT.ACCOUNT.ACTIVE` | `CambMemDirParam_IntAccountActive` | TField |  | Field accepts value as SINGLE or MASS SINGLE - Indicate Inactive account would be activated only on the viewing the single account summary details MASS - Indicate all the accounts associated to Cards will be activated on successful customer login. |
| 44 | `CAMB.MEM.EXTENDED.PAC` | `CambMemDirParam_ExtendedPac` | TField |  | This is a Yes or No field to indicate whether the extended PAC functionality is enabled or not. YES - Extended PAC functionality is enabled by Central1. NO - Extended PAC functionality is not enabled by Central1. |
| 45 | `CAMB.MEM.MDI.CUSTOMER` | `CambMemDirParam_MdiCustomer` | TField |  | This is a field with options 'ALL', 'ACCT.CUST' and None ALL - On login, all the customers available under EBIZ.ACCESS fields in CARD.ACCESS will be displayed once logged in. The customer will be displayed even if there are no accounts ACCT_CUST or None - Existing functionality that is customers with accounts will be displayed |
| 46 | `CAMB.MEM.PRODUCT.LINE` | `CambMemDirParam_ProductLine` |  |  |  |
| 47 | `CAMB.MEM.MDI.INT.PRTY` | `CambMemDirParam_MdiIntPrty` |  |  |  |
| 48 | `CAMB.MEM.LEGACY.MDI.ACTIVITY` | `CambMemDirParam_LegacyMdiActivity` |  |  |  |
| 49 | `CAMB.MEM.ALL.OWNERS` | `CambMemDirParam_AllOwners` | TField |  |  |
| 50 | `CAMB.MEM.ACC.TRANSIT` | `CambMemDirParam_AccTransit` | TField |  | This field is used to retrieve the Route number and will be considered for MDI All account summary Route mapping alone Possible values are YES or NO YES - Route number is retrieved from COMPANY>BC.SORT.CODE's first four digit Transit Number = COMPANY>BC.SORT.CODE. (last 5 digits) NO - Route number is retrived from CAMB.MEM.DIR.PARAM>ROUTE Transit Number = COMPANY > BC.SORT.CODE (last 5 digits) |
| 51 | `CAMB.MEM.MASKING.BITMAP` | `CambMemDirParam_MaskingBitmap` |  |  |  |
| 52 | `CAMB.MEM.LOCAL.REF` | `CambMemDirParam_LocalRef` |  |  |  |
| 53 | `CAMB.MEM.OVERRIDE` | `CambMemDirParam_Override` |  |  |  |
| 54 | `CAMB.MEM.RECORD.STATUS` | `CambMemDirParam_RecordStatus` | String |  |  |
| 55 | `CAMB.MEM.CURR.NO` | `CambMemDirParam_CurrNo` | String |  |  |
| 56 | `CAMB.MEM.INPUTTER` | `CambMemDirParam_Inputter` |  |  |  |
| 57 | `CAMB.MEM.DATE.TIME` | `CambMemDirParam_DateTime` |  |  |  |
| 58 | `CAMB.MEM.AUTHORISER` | `CambMemDirParam_Authoriser` | String |  |  |
| 59 | `CAMB.MEM.CO.CODE` | `CambMemDirParam_CoCode` | String |  |  |
| 60 | `CAMB.MEM.DEPT.CODE` | `CambMemDirParam_DeptCode` | String |  |  |
| 61 | `CAMB.MEM.AUDITOR.CODE` | `CambMemDirParam_AuditorCode` | String |  |  |
| 62 | `CAMB.MEM.AUDIT.DATE.TIME` | `CambMemDirParam_AuditDateTime` | String |  |  |
| 63 | `CAMB.MEM.ADDL.RESP.DATA` | `CambMemDirParam_AddlRespData` |  |  |  |
