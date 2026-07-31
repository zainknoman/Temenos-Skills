# CHQ.PAYMENT.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CHQ.PAYMENT.PARAMETER` in `CACQMG_ChequeManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CHQ.PAY.GEN.CHQ.NUMBER` | `ChqPaymentParameter_GenChqNumber` | TField |  | This field is used to define whether CHEQUE.NUMBER to be defaulted automatically in the xml file or not. Yes/No type field. Yes - Cheque number will default in the xml. No - Cheque number will not default in the xml. Validations - Applicable only for the office cheques issued via Payment order. |
| 2 | `CHQ.PAY.NOM.CONSOLIDATED.CHQ` | `ChqPaymentParameter_NomConsolidatedChq` | TField |  | This field will decide whether maturity payments of nominee will be grouped together and paid as one cheque or individual cheques for each term will be issued. Allowed values are: None/Single - Payment will be paid as an individual cheque. Consolidate - Payment will be paid by consolidating the total amount and paid as a single cheque. |
| 3 | `CHQ.PAY.ADDRESS.OPTION` | `ChqPaymentParameter_AddressOption` | TField |  | This field will decide whether cheque xml should be produced only with client address or only with Nominee address or it should have both the details. If consolidate option is selected in NOM.CONSOLIDATED.CHQ field then Nominee address will be printed. Note: If PO BENEFICIARY has an address then it will be used for xml instead of taking it from CIF. It will be either mapped to client address tags. |
| 4 | `CHQ.PAY.PO.PRODUCT` | `ChqPaymentParameter_PoProduct` |  |  |  |
| 5 | `CHQ.PAY.STOCK.SERIES.ID` | `ChqPaymentParameter_StockSeriesId` |  |  |  |
| 6 | `CHQ.PAY.STOCK.REGISTER` | `ChqPaymentParameter_StockRegister` |  |  |  |
| 7 | `CHQ.PAY.PRINT.SIGNATURE` | `ChqPaymentParameter_PrintSignature` |  |  |  |
| 8 | `CHQ.PAY.RESERVED.20` | `ChqPaymentParameter_Reserved20` |  |  |  |
| 9 | `CHQ.PAY.RESERVED.19` | `ChqPaymentParameter_Reserved19` |  |  |  |
| 10 | `CHQ.PAY.RESERVED.18` | `ChqPaymentParameter_Reserved18` |  |  |  |
| 11 | `CHQ.PAY.RESERVED.17` | `ChqPaymentParameter_Reserved17` |  |  |  |
| 12 | `CHQ.PAY.RESERVED.16` | `ChqPaymentParameter_Reserved16` |  |  |  |
| 13 | `CHQ.PAY.MIN.STOCK.QTY` | `ChqPaymentParameter_MinStockQty` | TField |  | This field is used to define the minimum quantity. Based on which the reorder will be placed.Allowed up to 99 numeric. |
| 14 | `CHQ.PAY.REORDER.QTY` | `ChqPaymentParameter_ReorderQty` | TField |  | This field will hold the quantity to be reordered when the Stock gets lower than the minimum quantity.Allowed up to 99 numeric |
| 15 | `CHQ.PAY.UNCLAIM.DAYS` | `ChqPaymentParameter_UnclaimDays` |  |  |  |
| 16 | `CHQ.PAY.UNCLAIM.STATUS` | `ChqPaymentParameter_UnclaimStatus` |  |  |  |
| 17 | `CHQ.PAY.UNCLAIM.GL.CCY` | `ChqPaymentParameter_UnclaimGlCcy` |  |  |  |
| 18 | `CHQ.PAY.UNPAID.GL.ACCT` | `ChqPaymentParameter_UnpaidGlAcct` |  |  |  |
| 19 | `CHQ.PAY.MOVE.FUNDS` | `ChqPaymentParameter_MoveFunds` |  |  |  |
| 20 | `CHQ.PAY.RESERVED.15` | `ChqPaymentParameter_Reserved15` |  |  |  |
| 21 | `CHQ.PAY.RESERVED.14` | `ChqPaymentParameter_Reserved14` |  |  |  |
| 22 | `CHQ.PAY.RESERVED.13` | `ChqPaymentParameter_Reserved13` |  |  |  |
| 23 | `CHQ.PAY.RESERVED.12` | `ChqPaymentParameter_Reserved12` |  |  |  |
| 24 | `CHQ.PAY.RESERVED.11` | `ChqPaymentParameter_Reserved11` |  |  |  |
| 25 | `CHQ.PAY.FT.TXN.TYPE` | `ChqPaymentParameter_FtTxnType` | TField |  | This field will hold the valid transaction code to be used for transferring the unpaid funds.Must be valid record from FT.TXN.TYPE.CONDITION table. |
| 26 | `CHQ.PAY.UNCLAIM.FT.VERSION` | `ChqPaymentParameter_UnclaimFtVersion` | TField |  | This field will be used to specify the FT version using which the funds will be moved after the cheque issued is not presented after X days.Valid record from VERSION table.E.g. FUNDS.TRANSFER,AC |
| 27 | `CHQ.PAY.OC.THRESHOLD.AMT` | `ChqPaymentParameter_OcThresholdAmt` | TField |  | This field is used to define the maximum threshold amount for which the office cheque can be issued.Validation:Valid amount to be defined here. If the value in the field exceeds an override message will be triggered. |
| 28 | `CHQ.PAY.MICR.CCY.CODE` | `ChqPaymentParameter_MicrCcyCode` |  |  |  |
| 29 | `CHQ.PAY.MICR.CODE` | `ChqPaymentParameter_MicrCode` |  |  |  |
| 30 | `CHQ.PAY.CHQ.PRINT.PATH` | `ChqPaymentParameter_ChqPrintPath` | TField |  | This filed will be used to store the batch printing path in which the xml file will be stored.Valid path to be defined here.E.g. .\bnk.interface\REPRINT.CHQ |
| 31 | `CHQ.PAY.UNCLAIM.XML.STATUS` | `ChqPaymentParameter_UnclaimXmlStatus` | TField |  | This field will carry the status for which the xml file will be produced every year on a specific date. This xml will be used to report the unclaimed funds remitted to BOC.Valid record from EB.LOOKUP > CHQ.STATUSE.g Remittance to BOC |
| 32 | `CHQ.PAY.UNCLAIM.XML.PATH` | `ChqPaymentParameter_UnclaimXmlPath` | TField |  | This field will carry the path in which the unclaimed xml will be stored.Valid path to be defined here.E.g. .\bnk.interface\PRINT.CHQ |
| 33 | `CHQ.PAY.NOM.DEMAND.PROD` | `ChqPaymentParameter_NomDemandProd` |  |  |  |
| 34 | `CHQ.PAY.OFS.SOURCE` | `ChqPaymentParameter_OfsSource` | TField |  | OFS source record used for all the cheque related OFS postings.Valid record from OFS.SOURCE table. |
| 35 | `CHQ.PAY.CHQ.XML.MAPPING` | `ChqPaymentParameter_ChqXmlMapping` | TField |  | DFE Mapping used for producing the cheque XML extract.Valid record from DFE.PARAMETER table. |
| 36 | `CHQ.PAY.STOCK.ENTRY.VERSION` | `ChqPaymentParameter_StockEntryVersion` | TField |  | This field used to specify the version used for posting the STOCK.ENTRY whenever the stock mentioned in this table goes below the minimum stock quantity.Valid record from VERSION table. |
| 37 | `CHQ.PAY.PO.VERSION` | `ChqPaymentParameter_PoVersion` | TField |  | This field used to specify the version used for posting PO for the nominee cheque payments.Valid record from VERSION table. |
| 38 | `CHQ.PAY.CRS.VERSION` | `ChqPaymentParameter_CrsVersion` | TField |  | This field used to specify the version used for posting CRS for the new local status updatesValid record from VERSION table. |
| 39 | `CHQ.PAY.NOMINEE.PO.PRODUCT` | `ChqPaymentParameter_NomineePoProduct` | TField |  | This field used to specify the PO product used for posting office cheque transaction using POValid record from PAYMENT.ORER.PRODUCT table. |
| 40 | `CHQ.PAY.LOCAL.REF` | `ChqPaymentParameter_LocalRef` |  |  |  |
| 41 | `CHQ.PAY.INTER.ACCT.CATEGORY` | `ChqPaymentParameter_InterAcctCategory` | TField |  | Field to store the category to which Internal account for cheque transactions to be posted. Valid record of CATEGORY |
| 42 | `CHQ.PAY.RESERVED.9` | `ChqPaymentParameter_Reserved9` |  |  |  |
| 43 | `CHQ.PAY.RESERVED.8` | `ChqPaymentParameter_Reserved8` | TField |  |  |
| 44 | `CHQ.PAY.RESERVED.7` | `ChqPaymentParameter_Reserved7` | TField |  |  |
| 45 | `CHQ.PAY.RESERVED.6` | `ChqPaymentParameter_Reserved6` | TField |  |  |
| 46 | `CHQ.PAY.RESERVED.5` | `ChqPaymentParameter_Reserved5` | TField |  |  |
| 47 | `CHQ.PAY.RESERVED.4` | `ChqPaymentParameter_Reserved4` | TField |  |  |
| 48 | `CHQ.PAY.RESERVED.3` | `ChqPaymentParameter_Reserved3` | TField |  |  |
| 49 | `CHQ.PAY.RESERVED.2` | `ChqPaymentParameter_Reserved2` | TField |  |  |
| 50 | `CHQ.PAY.RESERVED.1` | `ChqPaymentParameter_Reserved1` | TField |  |  |
| 51 | `CHQ.PAY.OVERRIDE` | `ChqPaymentParameter_Override` |  |  |  |
| 52 | `CHQ.PAY.RECORD.STATUS` | `ChqPaymentParameter_RecordStatus` | String |  |  |
| 53 | `CHQ.PAY.CURR.NO` | `ChqPaymentParameter_CurrNo` | String |  |  |
| 54 | `CHQ.PAY.INPUTTER` | `ChqPaymentParameter_Inputter` |  |  |  |
| 55 | `CHQ.PAY.DATE.TIME` | `ChqPaymentParameter_DateTime` |  |  |  |
| 56 | `CHQ.PAY.AUTHORISER` | `ChqPaymentParameter_Authoriser` | String |  |  |
| 57 | `CHQ.PAY.CO.CODE` | `ChqPaymentParameter_CoCode` | String |  |  |
| 58 | `CHQ.PAY.DEPT.CODE` | `ChqPaymentParameter_DeptCode` | String |  |  |
| 59 | `CHQ.PAY.AUDITOR.CODE` | `ChqPaymentParameter_AuditorCode` | String |  |  |
| 60 | `CHQ.PAY.AUDIT.DATE.TIME` | `ChqPaymentParameter_AuditDateTime` | String |  |  |
