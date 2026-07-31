# INLEND.IDPMS.OBB — Table Schema

> Source: `INSERTS/I_F.INLEND.IDPMS.OBB` in `INDPMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INLEND.OBB.BILL.OF.ENTRY.DATE` | `InlendIdpmsObb_BillOfEntryDate` | TField |  |  |
| 2 | `INLEND.OBB.PORT.OF.DISCHARGE` | `InlendIdpmsObb_PortOfDischarge` | TField | Yes | Port where goods are discharged. A Valid record from INLEND.PORT.LIST MANDATORY |
| 3 | `INLEND.OBB.BOE.AD.CODE` | `InlendIdpmsObb_BoeAdCode` | TField | Yes | AD Code. A Valid entry in INLEND.IMPORT.EXPORT.ATTRIBUTES MANDATORY |
| 4 | `INLEND.OBB.BILL.OF.ENTRY.SECTOR` | `InlendIdpmsObb_BillOfEntrySector` | TField |  | Sector to which BOE belongs. Allowed values are G for GOVERNMENT or P for PRIVATE) |
| 5 | `INLEND.OBB.PORT.OF.SHIPMENT` | `InlendIdpmsObb_PortOfShipment` | TField | Yes | Port of shipment MANDATORY |
| 6 | `INLEND.OBB.IGM.NUMBER` | `InlendIdpmsObb_IgmNumber` | TField |  | Import General Manifest Number |
| 7 | `INLEND.OBB.IGM.DATE` | `InlendIdpmsObb_IgmDate` | TField |  | Import General Manifest Date |
| 8 | `INLEND.OBB.MAWB.NUMBER` | `InlendIdpmsObb_MawbNumber` | TField |  | Master AWB Number |
| 9 | `INLEND.OBB.MAWB.DATE` | `InlendIdpmsObb_MawbDate` | TField |  | Master AWB Date |
| 10 | `INLEND.OBB.HBL.NUMBER` | `InlendIdpmsObb_HblNumber` | TField |  | House AWB Number |
| 11 | `INLEND.OBB.HBL.DATE` | `InlendIdpmsObb_HblDate` | TField |  | House AWB Date |
| 12 | `INLEND.OBB.IMPORT.AGENCY` | `InlendIdpmsObb_ImportAgency` | TField | Yes | Allowed values are 1, 2, or 3. 1.Customs, 2.SEZ and 3.BOE Waiver MANDATORY |
| 13 | `INLEND.OBB.IE.CODE.CUSTOMER` | `InlendIdpmsObb_IeCodeCustomer` | TField | Yes | Declared IE Code MANDATORY |
| 14 | `INLEND.OBB.IE.NAME.CUSTOMER` | `InlendIdpmsObb_IeNameCustomer` |  |  |  |
| 15 | `INLEND.OBB.IE.CUSTOMER.ADDRESS` | `InlendIdpmsObb_IeCustomerAddress` |  |  |  |
| 16 | `INLEND.OBB.IE.PAN.NUMBER` | `InlendIdpmsObb_IePanNumber` | TField |  | Declared IE PAN Number |
| 17 | `INLEND.OBB.INVOICE.NUMBER` | `InlendIdpmsObb_InvoiceNumber` |  |  |  |
| 18 | `INLEND.OBB.INVOICE.SERIAL.NUMBER` | `InlendIdpmsObb_InvoiceSerialNumber` |  |  |  |
| 19 | `INLEND.OBB.INVOICE.TERMS` | `InlendIdpmsObb_InvoiceTerms` |  |  |  |
| 20 | `INLEND.OBB.INVOICE.CURRENCY` | `InlendIdpmsObb_InvoiceCurrency` |  |  |  |
| 21 | `INLEND.OBB.INVOICE.AMOUNT` | `InlendIdpmsObb_InvoiceAmount` |  |  |  |
| 22 | `INLEND.OBB.FREIGHT.CURRENCY` | `InlendIdpmsObb_FreightCurrency` |  |  |  |
| 23 | `INLEND.OBB.FREIGHT.AMOUNT` | `InlendIdpmsObb_FreightAmount` |  |  |  |
| 24 | `INLEND.OBB.INSURANCE.CURRENCY` | `InlendIdpmsObb_InsuranceCurrency` |  |  |  |
| 25 | `INLEND.OBB.INSURANCE.AMOUNT` | `InlendIdpmsObb_InsuranceAmount` |  |  |  |
| 26 | `INLEND.OBB.AGENCY.COMMN.CURRENCY` | `InlendIdpmsObb_AgencyCommnCurrency` |  |  |  |
| 27 | `INLEND.OBB.AGENCY.COMMN.AMOUNT` | `InlendIdpmsObb_AgencyCommnAmount` |  |  |  |
| 28 | `INLEND.OBB.DISCOUNT.CHGS.CURRENCY` | `InlendIdpmsObb_DiscountChgsCurrency` |  |  |  |
| 29 | `INLEND.OBB.DISCOUNT.CHGS.AMOUNT` | `InlendIdpmsObb_DiscountChgsAmount` |  |  |  |
| 30 | `INLEND.OBB.MISC.CHGS.CURRENCY` | `InlendIdpmsObb_MiscChgsCurrency` |  |  |  |
| 31 | `INLEND.OBB.MISC.CHGS.AMOUNT` | `InlendIdpmsObb_MiscChgsAmount` |  |  |  |
| 32 | `INLEND.OBB.SUPPLIER.NAME` | `InlendIdpmsObb_SupplierName` |  |  |  |
| 33 | `INLEND.OBB.SUPPLIER.ADDRESS` | `InlendIdpmsObb_SupplierAddress` |  |  |  |
| 34 | `INLEND.OBB.SUPPLIER.COUNTRY` | `InlendIdpmsObb_SupplierCountry` |  |  |  |
| 35 | `INLEND.OBB.SELLER.NAME` | `InlendIdpmsObb_SellerName` |  |  |  |
| 36 | `INLEND.OBB.SELLER.ADDRESS` | `InlendIdpmsObb_SellerAddress` |  |  |  |
| 37 | `INLEND.OBB.SELLER.COUNTRY` | `InlendIdpmsObb_SellerCountry` |  |  |  |
| 38 | `INLEND.OBB.THIRD.PARTY.NAME` | `InlendIdpmsObb_ThirdPartyName` |  |  |  |
| 39 | `INLEND.OBB.THIRD.PARTY.ADDRESS` | `InlendIdpmsObb_ThirdPartyAddress` |  |  |  |
| 40 | `INLEND.OBB.THIRD.PARTY.COUNTRY` | `InlendIdpmsObb_ThirdPartyCountry` |  |  |  |
| 41 | `INLEND.OBB.UTILIZED.INVOICE.AMOUNT` | `InlendIdpmsObb_UtilizedInvoiceAmount` |  |  |  |
| 42 | `INLEND.OBB.PENDING.INVOICE.AMOUNT` | `InlendIdpmsObb_PendingInvoiceAmount` |  |  |  |
| 43 | `INLEND.OBB.TOTAL.INVOICE.CURRENCY` | `InlendIdpmsObb_TotalInvoiceCurrency` |  |  |  |
| 44 | `INLEND.OBB.TOTAL.INVOICE.AMOUNT` | `InlendIdpmsObb_TotalInvoiceAmount` |  |  |  |
| 45 | `INLEND.OBB.TOTAL.UTIL.INVOICE.AMOUNT` | `InlendIdpmsObb_TotalUtilInvoiceAmount` |  |  |  |
| 46 | `INLEND.OBB.TOTAL.PENDING.INVOICE.AMOUNT` | `InlendIdpmsObb_TotalPendingInvoiceAmount` |  |  |  |
| 47 | `INLEND.OBB.OBB.RECORD.INDICATOR` | `InlendIdpmsObb_ObbRecordIndicator` | TField |  | Record Indicator. A Valid record from INLEND.IMP.EXP.RECORD.INDICATOR. Allowed values are 1, 2 and 3 |
| 48 | `INLEND.OBB.OBB.PROCESSING.DATE` | `InlendIdpmsObb_ObbProcessingDate` | TField |  | Date of processing of OBB. |
| 49 | `INLEND.OBB.OBB.RESPONSE.STATUS` | `InlendIdpmsObb_ObbResponseStatus` | TField | Yes | Response status of OBB. A Valid record from virtual table INLEND.IDPMS.OBB.RESPONSE.STATUS MANDATORY. System updated field. |
| 51 | `InlendIdpmsObb_ObbTransmitIndicator` | `INLEND.OBB.RESERVED.10` |  |  |  |
| 52 | `InlendIdpmsObb_Reserved10` | `INLEND.OBB.RESERVED.9` |  |  |  |
| 53 | `InlendIdpmsObb_Reserved9` | `INLEND.OBB.RESERVED.8` |  |  |  |
| 54 | `InlendIdpmsObb_Reserved8` | `INLEND.OBB.RESERVED.7` |  |  |  |
| 55 | `InlendIdpmsObb_Reserved7` | `INLEND.OBB.RESERVED.6` |  |  |  |
| 56 | `InlendIdpmsObb_Reserved6` | `INLEND.OBB.RESERVED.5` |  |  |  |
| 57 | `InlendIdpmsObb_Reserved5` | `INLEND.OBB.RESERVED.4` |  |  |  |
| 58 | `InlendIdpmsObb_Reserved4` | `INLEND.OBB.RESERVED.3` |  |  |  |
| 59 | `InlendIdpmsObb_Reserved3` | `INLEND.OBB.RESERVED.2` |  |  |  |
| 60 | `InlendIdpmsObb_Reserved2` | `INLEND.OBB.RESERVED.1` |  |  |  |
| 61 | `InlendIdpmsObb_Reserved1` | `INLEND.OBB.LOCAL.REF` |  |  |  |
| 62 | `InlendIdpmsObb_LocalRef` | `INLEND.OBB.OVERRIDE` |  |  |  |
| 63 | `InlendIdpmsObb_Override` | `INLEND.OBB.RECORD.STATUS` |  |  |  |
| 64 | `InlendIdpmsObb_RecordStatus` | `INLEND.OBB.CURR.NO` |  |  |  |
| 65 | `InlendIdpmsObb_CurrNo` | `INLEND.OBB.INPUTTER` |  |  |  |
| 66 | `InlendIdpmsObb_Inputter` | `INLEND.OBB.DATE.TIME` |  |  |  |
| 67 | `InlendIdpmsObb_DateTime` | `INLEND.OBB.AUTHORISER` |  |  |  |
| 68 | `InlendIdpmsObb_Authoriser` | `INLEND.OBB.CO.CODE` |  |  |  |
| 69 | `InlendIdpmsObb_CoCode` | `INLEND.OBB.DEPT.CODE` |  |  |  |
| 70 | `InlendIdpmsObb_DeptCode` | `INLEND.OBB.AUDITOR.CODE` |  |  |  |
| 71 | `InlendIdpmsObb_AuditorCode` | `INLEND.OBB.AUDIT.DATE.TIME` |  |  |  |
