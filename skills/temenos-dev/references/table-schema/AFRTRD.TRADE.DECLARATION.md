# AFRTRD.TRADE.DECLARATION — Table Schema

> Source: `INSERTS/I_F.AFRTRD.TRADE.DECLARATION` in `AFRTRD_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AFRTRD.TRADE.CUSTOMER.NO` | `AFRTRDTradeDeclaration_CustomerNo` |  |  |  |
| 2 | `AFRTRD.TRADE.ACCOUNT` | `AFRTRDTradeDeclaration_Account` |  |  |  |
| 3 | `AFRTRD.TRADE.QUANTITY` | `AFRTRDTradeDeclaration_Quantity` |  |  |  |
| 4 | `AFRTRD.TRADE.DECLARATION.CURRENCY` | `AFRTRDTradeDeclaration_DeclarationCurrency` |  |  |  |
| 5 | `AFRTRD.TRADE.DECLARATION.AMOUNT` | `AFRTRDTradeDeclaration_DeclarationAmount` |  |  |  |
| 6 | `AFRTRD.TRADE.CHARGE.CODE` | `AFRTRDTradeDeclaration_ChargeCode` |  |  |  |
| 7 | `AFRTRD.TRADE.OPENING.DATE` | `AFRTRDTradeDeclaration_OpeningDate` |  |  |  |
| 8 | `AFRTRD.TRADE.EXPIRY.DATE` | `AFRTRDTradeDeclaration_ExpiryDate` |  |  |  |
| 9 | `AFRTRD.TRADE.COUNTRY.OF.ORIGIN` | `AFRTRDTradeDeclaration_CountryOfOrigin` |  |  |  |
| 10 | `AFRTRD.TRADE.MERCHANDISE.DESC` | `AFRTRDTradeDeclaration_MerchandiseDesc` |  |  |  |
| 11 | `AFRTRD.TRADE.EXTERNAL.REFERENCE` | `AFRTRDTradeDeclaration_ExternalReference` |  |  |  |
| 12 | `AFRTRD.TRADE.MANDATORY.DOC.REF` | `AFRTRDTradeDeclaration_MandatoryDocRef` |  |  |  |
| 13 | `AFRTRD.TRADE.DECLARATION.PROD.REF` | `AFRTRDTradeDeclaration_DeclarationProdRef` |  |  |  |
| 14 | `AFRTRD.TRADE.LIMIT.RECORD.ID` | `AFRTRDTradeDeclaration_LimitRecordId` |  |  |  |
| 15 | `AFRTRD.TRADE.NARRATION` | `AFRTRDTradeDeclaration_Narration` |  |  |  |
| 16 | `AFRTRD.TRADE.CONTRACT.REF` | `AFRTRDTradeDeclaration_ContractRef` |  |  |  |
| 17 | `AFRTRD.TRADE.PRODUCT.DOC.TYPE` | `AFRTRDTradeDeclaration_ProductDocType` |  |  |  |
| 18 | `AFRTRD.TRADE.PRODUCT.DOC.REF` | `AFRTRDTradeDeclaration_ProductDocRef` |  |  |  |
| 19 | `AFRTRD.TRADE.PROD.DOC.ISSUE.DATE` | `AFRTRDTradeDeclaration_ProdDocIssueDate` |  |  |  |
| 20 | `AFRTRD.TRADE.STATUS` | `AFRTRDTradeDeclaration_Status` |  |  |  |
| 21 | `AFRTRD.TRADE.COMM.TXN.ID` | `AFRTRDTradeDeclaration_CommTxnId` |  |  |  |
| 22 | `AFRTRD.TRADE.LOCAL.REF` | `AFRTRDTradeDeclaration_LocalRef` |  |  |  |
| 23 | `AFRTRD.TRADE.TYPE.OF.DECLARATION` | `AFRTRDTradeDeclaration_TypeOfDeclaration` |  |  |  |
| 24 | `AFRTRD.TRADE.NATURE.OF.DECLARATION` | `AFRTRDTradeDeclaration_NatureOfDeclaration` |  |  |  |
| 25 | `AFRTRD.TRADE.PRODUCT.RESTRICTIONS` | `AFRTRDTradeDeclaration_ProductRestrictions` |  |  |  |
| 26 | `AFRTRD.TRADE.PREFINANCING` | `AFRTRDTradeDeclaration_Prefinancing` |  |  |  |
| 27 | `AFRTRD.TRADE.AVAILABLE.BALANCE` | `AFRTRDTradeDeclaration_AvailableBalance` |  |  |  |
| 28 | `AFRTRD.TRADE.UTILIZED.BALANCE` | `AFRTRDTradeDeclaration_UtilizedBalance` |  |  |  |
| 29 | `AFRTRD.TRADE.UNAUTH.UTIL.AMT` | `AFRTRDTradeDeclaration_UnauthUtilAmt` |  |  |  |
| 30 | `AFRTRD.TRADE.TRANSACTION.REF` | `AFRTRDTradeDeclaration_TransactionRef` |  |  |  |
| 31 | `AFRTRD.TRADE.RESERVED.8` | `AFRTRDTradeDeclaration_Reserved8` |  |  |  |
| 32 | `AFRTRD.TRADE.RESERVED.9` | `AFRTRDTradeDeclaration_Reserved9` |  |  |  |
| 33 | `AFRTRD.TRADE.OVERRIDE` | `AFRTRDTradeDeclaration_Override` |  |  |  |
| 34 | `AFRTRD.TRADE.RECORD.STATUS` | `AFRTRDTradeDeclaration_RecordStatus` |  |  |  |
| 35 | `AFRTRD.TRADE.CURR.NO` | `AFRTRDTradeDeclaration_CurrNo` |  |  |  |
| 36 | `AFRTRD.TRADE.INPUTTER` | `AFRTRDTradeDeclaration_Inputter` |  |  |  |
| 37 | `AFRTRD.TRADE.DATE.TIME` | `AFRTRDTradeDeclaration_DateTime` |  |  |  |
| 38 | `AFRTRD.TRADE.AUTHORISER` | `AFRTRDTradeDeclaration_Authoriser` |  |  |  |
| 39 | `AFRTRD.TRADE.CO.CODE` | `AFRTRDTradeDeclaration_CoCode` |  |  |  |
| 40 | `AFRTRD.TRADE.DEPT.CODE` | `AFRTRDTradeDeclaration_DeptCode` |  |  |  |
| 41 | `AFRTRD.TRADE.AUDITOR.CODE` | `AFRTRDTradeDeclaration_AuditorCode` |  |  |  |
| 42 | `AFRTRD.TRADE.AUDIT.DATE.TIME` | `AFRTRDTradeDeclaration_AuditDateTime` |  |  |  |
