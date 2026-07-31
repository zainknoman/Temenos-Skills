# INLEND.IDPMS.BOE — Table Schema

> Source: `INSERTS/I_F.INLEND.IDPMS.BOE` in `INDPMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IDPMS.BOE.DATE.BILL.OF.ENTRY` | `InlendIdpmsBoe_DateBillOfEntry` | TField | Yes | Date of Bill of Entry. A Valid T24 Date MANDATORY |
| 2 | `IDPMS.BOE.BOE.AD.CODE` | `InlendIdpmsBoe_BoeAdCode` | TField | Yes | AD Code. A Valid entry in INLEND.IMPORT.EXPORT.ATTRIBUTES MANDATORY |
| 3 | `IDPMS.BOE.BILL.OF.ENTRY.SECTOR` | `InlendIdpmsBoe_BillOfEntrySector` | TField |  | Sector to which BOE belongs. Allowed values are G for GOVERNMENT or P for PRIVATE) |
| 4 | `IDPMS.BOE.PORT.OF.DISCHARGE` | `InlendIdpmsBoe_PortOfDischarge` | TField | Yes | Port where goods are discharged. A Valid record from INLEND.PORT.LIST MANDATORY |
| 5 | `IDPMS.BOE.PORT.OF.SHIPMENT` | `InlendIdpmsBoe_PortOfShipment` | TField | Yes | Port of shipment MANDATORY |
| 6 | `IDPMS.BOE.IGM.NUMBER` | `InlendIdpmsBoe_IgmNumber` | TField |  | Import General Manifest Number |
| 7 | `IDPMS.BOE.IGM.DATE` | `InlendIdpmsBoe_IgmDate` | TField |  | Import General Manifest Date |
| 8 | `IDPMS.BOE.MAWB.NUMBER` | `InlendIdpmsBoe_MawbNumber` | TField |  | Master AWB Number |
| 9 | `IDPMS.BOE.MAWB.DATE` | `InlendIdpmsBoe_MawbDate` | TField |  | Master AWB Date |
| 10 | `IDPMS.BOE.HBL.NUMBER` | `InlendIdpmsBoe_HblNumber` | TField |  | House AWB Number |
| 11 | `IDPMS.BOE.HBL.DATE` | `InlendIdpmsBoe_HblDate` | TField |  | House AWB Date |
| 12 | `IDPMS.BOE.IMPORT.AGENCY` | `InlendIdpmsBoe_ImportAgency` | TField | Yes | Allowed values are 1, 2, or 3. 1.Customs, 2.SEZ and 3.BOE Waiver MANDATORY |
| 13 | `IDPMS.BOE.IE.CODE.CUSTOMER` | `InlendIdpmsBoe_IeCodeCustomer` | TField | Yes | Declared IE Code MANDATORY |
| 14 | `IDPMS.BOE.IE.NAME.CUSTOMER` | `InlendIdpmsBoe_IeNameCustomer` |  |  |  |
| 15 | `IDPMS.BOE.IE.CUSTOMER.ADDRESS` | `InlendIdpmsBoe_IeCustomerAddress` |  |  |  |
| 16 | `IDPMS.BOE.IE.PAN.NUMBER` | `InlendIdpmsBoe_IePanNumber` | TField |  | Declared IE PAN Number |
| 17 | `IDPMS.BOE.INVOICE.NUMBER` | `InlendIdpmsBoe_InvoiceNumber` |  |  |  |
| 18 | `IDPMS.BOE.INVOICE.SERIAL.NUMBER` | `InlendIdpmsBoe_InvoiceSerialNumber` |  |  |  |
| 19 | `IDPMS.BOE.INVOICE.TERMS` | `InlendIdpmsBoe_InvoiceTerms` |  |  |  |
| 20 | `IDPMS.BOE.INVOICE.CURRENCY` | `InlendIdpmsBoe_InvoiceCurrency` |  |  |  |
| 21 | `IDPMS.BOE.INVOICE.AMOUNT` | `InlendIdpmsBoe_InvoiceAmount` |  |  |  |
| 22 | `IDPMS.BOE.FREIGHT.CURRENCY` | `InlendIdpmsBoe_FreightCurrency` |  |  |  |
| 23 | `IDPMS.BOE.FREIGHT.AMOUNT` | `InlendIdpmsBoe_FreightAmount` |  |  |  |
| 24 | `IDPMS.BOE.INSURANCE.CURRENCY` | `InlendIdpmsBoe_InsuranceCurrency` |  |  |  |
| 25 | `IDPMS.BOE.INSURANCE.AMOUNT` | `InlendIdpmsBoe_InsuranceAmount` |  |  |  |
| 26 | `IDPMS.BOE.AGENCY.COMMN.CURRENCY` | `InlendIdpmsBoe_AgencyCommnCurrency` |  |  |  |
| 27 | `IDPMS.BOE.AGENCY.COMMN.AMOUNT` | `InlendIdpmsBoe_AgencyCommnAmount` |  |  |  |
| 28 | `IDPMS.BOE.DISCOUNT.CHGS.CURRENCY` | `InlendIdpmsBoe_DiscountChgsCurrency` |  |  |  |
| 29 | `IDPMS.BOE.DISCOUNT.CHGS.AMOUNT` | `InlendIdpmsBoe_DiscountChgsAmount` |  |  |  |
| 30 | `IDPMS.BOE.MISC.CHGS.CURRENCY` | `InlendIdpmsBoe_MiscChgsCurrency` |  |  |  |
| 31 | `IDPMS.BOE.MISC.CHGS.AMOUNT` | `InlendIdpmsBoe_MiscChgsAmount` |  |  |  |
| 32 | `IDPMS.BOE.SUPPLIER.NAME` | `InlendIdpmsBoe_SupplierName` |  |  |  |
| 33 | `IDPMS.BOE.SUPPLIER.ADDRESS` | `InlendIdpmsBoe_SupplierAddress` |  |  |  |
| 34 | `IDPMS.BOE.SUPPLIER.COUNTRY` | `InlendIdpmsBoe_SupplierCountry` |  |  |  |
| 35 | `IDPMS.BOE.SELLER.NAME` | `InlendIdpmsBoe_SellerName` |  |  |  |
| 36 | `IDPMS.BOE.SELLER.ADDRESS` | `InlendIdpmsBoe_SellerAddress` |  |  |  |
| 37 | `IDPMS.BOE.SELLER.COUNTRY` | `InlendIdpmsBoe_SellerCountry` |  |  |  |
| 38 | `IDPMS.BOE.THIRD.PARTY.NAME` | `InlendIdpmsBoe_ThirdPartyName` |  |  |  |
| 39 | `IDPMS.BOE.THIRD.PARTY.ADDRESS` | `InlendIdpmsBoe_ThirdPartyAddress` |  |  |  |
| 40 | `IDPMS.BOE.THIRD.PARTY.COUNTRY` | `InlendIdpmsBoe_ThirdPartyCountry` |  |  |  |
| 41 | `IDPMS.BOE.UTILIZED.INVOICE.AMOUNT` | `InlendIdpmsBoe_UtilizedInvoiceAmount` |  |  |  |
| 42 | `IDPMS.BOE.PENDING.INVOICE.AMOUNT` | `InlendIdpmsBoe_PendingInvoiceAmount` |  |  |  |
| 43 | `IDPMS.BOE.BOE.ADJ.INVOICE.AMOUNT` | `InlendIdpmsBoe_BoeAdjInvoiceAmount` |  |  |  |
| 44 | `IDPMS.BOE.TOTAL.INVOICE.AMOUNT` | `InlendIdpmsBoe_TotalInvoiceAmount` |  |  |  |
| 45 | `IDPMS.BOE.TOTAL.UTIL.INVOICE.AMOUNT` | `InlendIdpmsBoe_TotalUtilInvoiceAmount` |  |  |  |
| 46 | `IDPMS.BOE.TOTAL.PENDING.INVOICE.AMOUNT` | `InlendIdpmsBoe_TotalPendingInvoiceAmount` |  |  |  |
| 47 | `IDPMS.BOE.RECORD.INDICATOR` | `InlendIdpmsBoe_RecordIndicator` | TField | Yes | Record Indicator. A Valid record from INLEND.IMP.EXP.RECORD.INDICATOR. Allowed values are 1 and 3. MANDATORY. If record is entered in this table for first time the value should be 1 . |
| 48 | `IDPMS.BOE.BOE.RECORD.STATUS` | `InlendIdpmsBoe_BoeRecordStatus` |  |  |  |
| 49 | `IDPMS.BOE.AD.CODE.STATUS` | `InlendIdpmsBoe_AdCodeStatus` | TField | Yes | Drop-down field, can hold values of OWN or OTHER MANDATORY. System updated field. |
| 50 | `IDPMS.BOE.BOE.CUSTOMER.ID` | `InlendIdpmsBoe_BoeCustomerId` | TField | Yes | Customer ID of IE.CODE.CUSTOMER, if exists in LEGAL.ID of CUSTOMER application. MANDATORY. System updated field. |
| 51 | `IDPMS.BOE.BOE.TOTAL.AMOUNT` | `InlendIdpmsBoe_BoeTotalAmount` | TField |  | Field is No-Longer Used. |
| 52 | `IDPMS.BOE.SETTLEMENT.DATE` | `InlendIdpmsBoe_SettlementDate` |  |  |  |
| 53 | `IDPMS.BOE.SETTLEMENT.AMOUNT` | `InlendIdpmsBoe_SettlementAmount` |  |  |  |
| 54 | `IDPMS.BOE.BOE.PENDING.AMOUNT` | `InlendIdpmsBoe_BoePendingAmount` | TField |  | Field is No-Longer Used. |
| 55 | `IDPMS.BOE.DATE.STALE.BOE` | `InlendIdpmsBoe_DateStaleBoe` | TField | Yes | This is a system calculated field, where DATE.STALE.BOE = DATE.OF.BOE + DAYS.STALE.REMITTANCE(INLEND.IMPORT.EXPORT.ATTRIBUTES). MANDATORY. System updated field. |
| 56 | `IDPMS.BOE.BOE.ADJUST.REF.NUMBER` | `InlendIdpmsBoe_BoeAdjustRefNumber` | TField | Yes | BOE adjustment reference number MANDATORY, if BOE.ADJUSTMENT.INDICATOR not equal to NULL |
| 57 | `IDPMS.BOE.BOE.ADJUSTMENT.INDICATOR` | `InlendIdpmsBoe_BoeAdjustmentIndicator` | TField |  | A Valid record from virtual table INLEND.BOE.ADJUSTMENT.INDICATOR. Default value is NULL. |
| 58 | `IDPMS.BOE.BOE.ADJ.DOC.NUMBER` | `InlendIdpmsBoe_BoeAdjDocNumber` | TField | Yes | Document number in case adjustment done on account of Re-Import / Re-Export / Set-Off / Net-Off. Mandatory field if adjustment indicator is 4 or 5 or 6 MANDATORY, if BOE.ADJUSTMENT.INDICATOR not equal to NULL |
| 59 | `IDPMS.BOE.BOE.ADJ.DOC.DATE` | `InlendIdpmsBoe_BoeAdjDocDate` | TField | Yes | Date of BOE adjustment document MANDATORY, if BOE.ADJUSTMENT.INDICATOR not equal to NULL |
| 60 | `IDPMS.BOE.BOE.ADJ.DOC.PORT.DISCHARGE` | `InlendIdpmsBoe_BoeAdjDocPortDischarge` | TField | Yes | Port of discharge as mentioned in BOE adjustment document. Mandatory field if adjustment indicator is 4 or 5 or 6 MANDATORY, if BOE.ADJUSTMENT.INDICATOR not equal to NULL |
| 61 | `IDPMS.BOE.BOE.ADJUSTMENT.APPROVER` | `InlendIdpmsBoe_BoeAdjustmentApprover` | TField | Yes | A Valid record from virtual table INLEND.EXTENSION.AUTHORITY MANDATORY, if BOE.ADJUSTMENT.INDICATOR not equal to NULL |
| 62 | `IDPMS.BOE.BOE.ADJ.LETTER.NUMBER` | `InlendIdpmsBoe_BoeAdjLetterNumber` | TField | Yes | Letter number for adjustment provided by RBI MANDATORY, if BOE.ADJUSTMENT.INDICATOR not equal to NULL and BOE.ADJUSTMENT.APPROVER = 2 |
| 63 | `IDPMS.BOE.BOE.ADJ.LETTER.DATE` | `InlendIdpmsBoe_BoeAdjLetterDate` | TField | Yes | Letter date for adjustment provided by RBI MANDATORY, if BOE.ADJUSTMENT.INDICATOR not equal to NULL and BOE.ADJUSTMENT.APPROVER = 2 |
| 64 | `IDPMS.BOE.BOE.ADJ.REMARKS` | `InlendIdpmsBoe_BoeAdjRemarks` |  |  |  |
| 65 | `IDPMS.BOE.BOE.INPUT.MODE` | `InlendIdpmsBoe_BoeInputMode` | TField | Yes | Drop-down field. Allowed Values are UPLOAD and MANUAL MANDATORY. When records are uploaded, this field should be defaulted to UPLOAD. When MANUAL is chosen, fields 1 thru 43 are allowed for input by user. |
| 66 | `IDPMS.BOE.BOE.INPUT.MANUAL.STATUS` | `InlendIdpmsBoe_BoeInputManualStatus` | TField | Yes | Drop-down field. Allowed Values are NULL,YES and NO. If BOE.INPUT.MODE is UPLOAD, this filed is a no input field. If BOE.INPUT.MODE is MANUAL, allowed values are YES or NO only. MANDATORY, if BOE.INPUT.MODE = MANUAL |
| 67 | `IDPMS.BOE.BOE.EXTENSION.COUNT` | `InlendIdpmsBoe_BoeExtensionCount` | TField |  | The counter should start with 0 and every time the record is amended, the counter will be updated by 1 |
| 68 | `IDPMS.BOE.BOE.EXTENSION.GIVEN.BY` | `InlendIdpmsBoe_BoeExtensionGivenBy` | TField |  |  |
| 69 | `IDPMS.BOE.BOE.EXTENSION.LETTER.NUMBER` | `InlendIdpmsBoe_BoeExtensionLetterNumber` | TField |  | Letter number given by RBI |
| 70 | `IDPMS.BOE.BOE.EXTENSION.LETTER.DATE` | `InlendIdpmsBoe_BoeExtensionLetterDate` | TField |  | Date of letter given by RBI |
| 71 | `IDPMS.BOE.BOE.DATE.OF.EXTENSION` | `InlendIdpmsBoe_BoeDateOfExtension` | TField |  | Date of Extension until which BOE is valid |
| 72 | `IDPMS.BOE.EXTENSION.REMARKS` | `InlendIdpmsBoe_ExtensionRemarks` |  |  |  |
| 73 | `IDPMS.BOE.EXTENSION.RECORD.INDICATOR` | `InlendIdpmsBoe_ExtensionRecordIndicator` | TField | Yes | Record Indicator. A Valid record from INLEND.IMP.EXP.RECORD.INDICATOR. Allowed values are 1 and 3. MANDATORY, if BOE.ADJUSTMENT.INDICATOR not equal to NULL |
| 74 | `IDPMS.BOE.ADJ.RECORD.INDICATOR` | `InlendIdpmsBoe_AdjRecordIndicator` | TField | Yes | Record Indicator. A Valid record from INLEND.IMP.EXP.RECORD.INDICATOR. Allowed values are 1 and 3. MANDATORY, if BOE.ADJUSTMENT.INDICATOR not equal to NULL |
| 75 | `IDPMS.BOE.BOE.ADJUSTMENT.DATE` | `InlendIdpmsBoe_BoeAdjustmentDate` | TField | Yes | Date of Adjustment MANDATORY, if BOE.ADJUSTMENT.INDICATOR not equal to NULL |
| 76 | `IDPMS.BOE.LOCAL.REF` | `InlendIdpmsBoe_LocalRef` |  |  |  |
| 77 | `IDPMS.BOE.BEE.PROC.DATE` | `InlendIdpmsBoe_BeeProcDate` |  |  |  |
| 78 | `IDPMS.BOE.BEE.ERROR.STATUS` | `InlendIdpmsBoe_BeeErrorStatus` |  |  |  |
| 79 | `IDPMS.BOE.BEA.PROCESS.DATE` | `InlendIdpmsBoe_BeaProcessDate` |  |  |  |
| 80 | `IDPMS.BOE.BEA.ERROR.STATUS` | `InlendIdpmsBoe_BeaErrorStatus` |  |  |  |
| 81 | `IDPMS.BOE.MBE.PROCESS.DATE` | `InlendIdpmsBoe_MbeProcessDate` |  |  |  |
| 82 | `IDPMS.BOE.MBE.ERROR.STATUS` | `InlendIdpmsBoe_MbeErrorStatus` |  |  |  |
| 83 | `IDPMS.BOE.TRANSMIT.INDICATOR` | `InlendIdpmsBoe_TransmitIndicator` | TField |  | Drop-down field. A Valid record from INLEND.TRANSMIT.INDICATOR. System updated field |
| 84 | `IDPMS.BOE.OTHER.BANK.BOE` | `InlendIdpmsBoe_OtherBankBoe` | TField | Yes | Drop-down field. Allowed values are YES / NO. Mandatory, if BOE.INPUT.MODE = UPLOAD |
| 85 | `IDPMS.BOE.OBE.RECEIPT.DATE` | `InlendIdpmsBoe_ObeReceiptDate` | TField | Yes | Should be defaulted to current system date. Mandatory, if BOE.INPUT.MODE = UPLOAD and OTHER.BANK.BOE = YES |
| 86 | `IDPMS.BOE.OBE.RECORD.INDICATOR` | `InlendIdpmsBoe_ObeRecordIndicator` | TField | Yes | Should be vetted against INLEND.IMP.EXP.RECORD.INDICATOR. Mandatory, if BOE.INPUT.MODE = UPLOAD and OTHER.BANK.BOE = YES |
| 87 | `IDPMS.BOE.OVERRIDE` | `InlendIdpmsBoe_Override` |  |  |  |
| 88 | `IDPMS.BOE.RECORD.STATUS` | `InlendIdpmsBoe_RecordStatus` | String | Yes | A Valid record from virtual table INLEND.IMPORT.RECORD.STATUS MANDATORY. System updated field. |
| 89 | `IDPMS.BOE.CURR.NO` | `InlendIdpmsBoe_CurrNo` | String |  |  |
| 90 | `IDPMS.BOE.INPUTTER` | `InlendIdpmsBoe_Inputter` |  |  |  |
| 91 | `IDPMS.BOE.DATE.TIME` | `InlendIdpmsBoe_DateTime` |  |  |  |
| 92 | `IDPMS.BOE.AUTHORISER` | `InlendIdpmsBoe_Authoriser` | String |  |  |
| 93 | `IDPMS.BOE.CO.CODE` | `InlendIdpmsBoe_CoCode` | String |  |  |
| 94 | `IDPMS.BOE.DEPT.CODE` | `InlendIdpmsBoe_DeptCode` | String |  |  |
| 95 | `IDPMS.BOE.AUDITOR.CODE` | `InlendIdpmsBoe_AuditorCode` | String |  |  |
| 96 | `IDPMS.BOE.AUDIT.DATE.TIME` | `InlendIdpmsBoe_AuditDateTime` | String |  |  |
| 97 | `IDPMS.BOE.BOE.INVOICE.CURRENCY` | `InlendIdpmsBoe_BoeInvoiceCurrency` |  |  |  |
| 98 | `IDPMS.BOE.UBE.RECEIPT.DATE` | `InlendIdpmsBoe_UbeReceiptDate` | TField |  | Should be defaulted to current system date. |
| 99 | `IDPMS.BOE.UBE.RECORD.INDICATOR` | `InlendIdpmsBoe_UbeRecordIndicator` | TField | Yes | Should be vetted against INLEND.IMP.EXP.RECORD.INDICATOR. Mandatory. |
| 100 | `IDPMS.BOE.EXTENSION.REQUIRED` | `InlendIdpmsBoe_ExtensionRequired` | TField |  | Drop-down field. Allowed values are YES or NO. |
| 101 | `IDPMS.BOE.BOE.ADJUSTMENT.REQD` | `InlendIdpmsBoe_BoeAdjustmentReqd` | TField |  | Drop-down field. Allowed values are YES or NO. |
| 102 | `IDPMS.BOE.BOE.INVOICE.NUMBER` | `InlendIdpmsBoe_BoeInvoiceNumber` |  |  |  |
| 103 | `IDPMS.BOE.BOE.ADJ.INVOICE.CURRENCY` | `InlendIdpmsBoe_BoeAdjInvoiceCurrency` |  |  |  |
| 104 | `IDPMS.BOE.BOE.INVOICE.AMOUNT` | `InlendIdpmsBoe_BoeInvoiceAmount` |  |  |  |
| 105 | `IDPMS.BOE.BOE.ADJ.PENDING.INVOICE.AMOUNT` | `InlendIdpmsBoe_BoeAdjPendingInvoiceAmount` |  |  |  |
| 106 | `IDPMS.BOE.BOE.ADJ.INVOICE.STATUS` | `InlendIdpmsBoe_BoeAdjInvoiceStatus` |  |  |  |
| 107 | `IDPMS.BOE.BOE.ADJ.INVOICE.AMT` | `InlendIdpmsBoe_BoeAdjInvoiceAmt` |  |  |  |
| 108 | `IDPMS.BOE.BOE.CLOSURE.INDICATOR` | `InlendIdpmsBoe_BoeClosureIndicator` | TField |  | A Valid record from INLEND.IDPMS.BOE.CLOSURE.INDICATOR. |
| 109 | `IDPMS.BOE.MBE.RECORD.INDICATOR` | `InlendIdpmsBoe_MbeRecordIndicator` | TField |  | Manual Bill of Entry Record Indicator. A Valid record from INLEND.IMP.EXP.RECORD.INDICATOR. |
| 110 | `IDPMS.BOE.INTERFACE.ERR.RESP` | `InlendIdpmsBoe_InterfaceErrResp` | TField |  | Holds the Interface Error Response. A Valid record from INLEND.IDPMS.ERROR.CODES. |
| 111 | `IDPMS.BOE.BOE.PROCESS.NAME` | `InlendIdpmsBoe_BoeProcessName` | TField |  | Indicates the Process. A Valid record from INLEND.IDPMS.PROCESS.NAME. |
