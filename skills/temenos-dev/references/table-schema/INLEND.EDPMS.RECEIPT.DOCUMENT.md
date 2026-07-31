# INLEND.EDPMS.RECEIPT.DOCUMENT — Table Schema

> Source: `INSERTS/I_F.INLEND.EDPMS.RECEIPT.DOCUMENT` in `INDPMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INLEND.EDPMS.SHIPPING.BILL.NUMBER` | `InlendEdpmsReceiptDocument_ShippingBillNumber` | TField |  | Shipping Bill Number Provided By User Which Will Be Used Alternate Key. |
| 2 | `INLEND.EDPMS.SHIPPING.BILL.DATE` | `InlendEdpmsReceiptDocument_ShippingBillDate` | TField |  | Shipping Bill Date as provided by EDPMS or Manually entered. |
| 3 | `INLEND.EDPMS.SHIPPING.FORM.NUMBER` | `InlendEdpmsReceiptDocument_ShippingFormNumber` | TField |  | Shipping Form Number as provided by EDPMS or Manually entered. |
| 4 | `INLEND.EDPMS.SHIPPING.LEO.DATE` | `InlendEdpmsReceiptDocument_ShippingLeoDate` | TField |  | LEO date provided by Customs. |
| 5 | `INLEND.EDPMS.EXPORTER.IE.CODE` | `InlendEdpmsReceiptDocument_ExporterIeCode` | TField |  | IE Code. |
| 6 | `INLEND.EDPMS.EXPORTER.CHANGED.IE.CODE` | `InlendEdpmsReceiptDocument_ExporterChangedIeCode` | TField |  | Changed IE Code. |
| 7 | `INLEND.EDPMS.SHIPPING.BILL.AD.CODE` | `InlendEdpmsReceiptDocument_ShippingBillAdCode` | TField |  | AD Code. |
| 8 | `INLEND.EDPMS.TYPE.OF.EXPORT` | `InlendEdpmsReceiptDocument_TypeOfExport` | TField |  | A Valid record from virtual table INLEND.TYPE.EXPORT. |
| 9 | `INLEND.EDPMS.EXPORT.PORT.CODE` | `InlendEdpmsReceiptDocument_ExportPortCode` | TField |  | A Valid record from virtual table INLEND.PORT.LIST. |
| 10 | `INLEND.EDPMS.EXPORT.AGENCY` | `InlendEdpmsReceiptDocument_ExportAgency` | TField |  | A Valid record from virtual table INLEND.EXPORT.AGENCY. Allowed values are 1 through 6.. |
| 11 | `INLEND.EDPMS.MDF.DESTINATION.COUNTRY` | `InlendEdpmsReceiptDocument_MdfDestinationCountry` | TField |  | Export Destination Country. |
| 12 | `INLEND.EDPMS.MDF.INVOICE.NUMBER` | `InlendEdpmsReceiptDocument_MdfInvoiceNumber` |  |  |  |
| 13 | `INLEND.EDPMS.MDF.INVOICE.SERIAL.NUMBER` | `InlendEdpmsReceiptDocument_MdfInvoiceSerialNumber` |  |  |  |
| 14 | `INLEND.EDPMS.MDF.INVOICE.DATE` | `InlendEdpmsReceiptDocument_MdfInvoiceDate` |  |  |  |
| 15 | `INLEND.EDPMS.MDF.INV.FOB.CURRENCY` | `InlendEdpmsReceiptDocument_MdfInvFobCurrency` |  |  |  |
| 16 | `INLEND.EDPMS.MDF.INV.FOB.AMOUNT` | `InlendEdpmsReceiptDocument_MdfInvFobAmount` |  |  |  |
| 17 | `INLEND.EDPMS.MDF.INV.FRIEGHT.CURRENCY` | `InlendEdpmsReceiptDocument_MdfInvFrieghtCurrency` |  |  |  |
| 18 | `INLEND.EDPMS.MDF.INV.FRIEGHT.AMOUNT` | `InlendEdpmsReceiptDocument_MdfInvFrieghtAmount` |  |  |  |
| 19 | `INLEND.EDPMS.MDF.INV.FRIEGHT.EXCH.RATE` | `InlendEdpmsReceiptDocument_MdfInvFrieghtExchRate` |  |  |  |
| 20 | `INLEND.EDPMS.EQU.MDF.INV.FRIEGHT.AMOUNT` | `InlendEdpmsReceiptDocument_EquMdfInvFrieghtAmount` |  |  |  |
| 21 | `INLEND.EDPMS.MDF.INV.INS.CURRENCY` | `InlendEdpmsReceiptDocument_MdfInvInsCurrency` |  |  |  |
| 22 | `INLEND.EDPMS.MDF.INV.INS.AMOUNT` | `InlendEdpmsReceiptDocument_MdfInvInsAmount` |  |  |  |
| 23 | `INLEND.EDPMS.MDF.INV.INS.EXCH.RATE` | `InlendEdpmsReceiptDocument_MdfInvInsExchRate` |  |  |  |
| 24 | `INLEND.EDPMS.EQU.MDF.INV.INS.AMOUNT` | `InlendEdpmsReceiptDocument_EquMdfInvInsAmount` |  |  |  |
| 25 | `INLEND.EDPMS.MDF.INV.COMMN.CURRENCY` | `InlendEdpmsReceiptDocument_MdfInvCommnCurrency` |  |  |  |
| 26 | `INLEND.EDPMS.MDF.INV.COMMN.AMOUNT` | `InlendEdpmsReceiptDocument_MdfInvCommnAmount` |  |  |  |
| 27 | `INLEND.EDPMS.MDF.INV.COMMN.EXCH.RATE` | `InlendEdpmsReceiptDocument_MdfInvCommnExchRate` |  |  |  |
| 28 | `INLEND.EDPMS.EQU.MDF.INV.COMMN.AMOUNT` | `InlendEdpmsReceiptDocument_EquMdfInvCommnAmount` |  |  |  |
| 29 | `INLEND.EDPMS.MDF.INV.DISCNT.CURRENCY` | `InlendEdpmsReceiptDocument_MdfInvDiscntCurrency` |  |  |  |
| 30 | `INLEND.EDPMS.MDF.INV.DISCNT.AMOUNT` | `InlendEdpmsReceiptDocument_MdfInvDiscntAmount` |  |  |  |
| 31 | `INLEND.EDPMS.MDF.INV.DISCNT.EXCH.RATE` | `InlendEdpmsReceiptDocument_MdfInvDiscntExchRate` |  |  |  |
| 32 | `INLEND.EDPMS.EQU.MDF.INV.DISCNT.AMOUNT` | `InlendEdpmsReceiptDocument_EquMdfInvDiscntAmount` |  |  |  |
| 33 | `INLEND.EDPMS.MDF.INV.DEDN.CURRENCY` | `InlendEdpmsReceiptDocument_MdfInvDednCurrency` |  |  |  |
| 34 | `INLEND.EDPMS.MDF.INV.DEDN.AMOUNT` | `InlendEdpmsReceiptDocument_MdfInvDednAmount` |  |  |  |
| 35 | `INLEND.EDPMS.MDF.INV.DEDN.EXCH.RATE` | `InlendEdpmsReceiptDocument_MdfInvDednExchRate` |  |  |  |
| 36 | `INLEND.EDPMS.EQU.MDF.INV.DEDN.AMOUNT` | `InlendEdpmsReceiptDocument_EquMdfInvDednAmount` |  |  |  |
| 37 | `INLEND.EDPMS.MDF.INV.PCKNG.CURRENCY` | `InlendEdpmsReceiptDocument_MdfInvPckngCurrency` |  |  |  |
| 38 | `INLEND.EDPMS.MDF.INV.PCKNG.AMOUNT` | `InlendEdpmsReceiptDocument_MdfInvPckngAmount` |  |  |  |
| 39 | `INLEND.EDPMS.MDF.INV.PCKNG.EXCH.RATE` | `InlendEdpmsReceiptDocument_MdfInvPckngExchRate` |  |  |  |
| 40 | `INLEND.EDPMS.EQU.MDF.INV.PCKNG.AMOUNT` | `InlendEdpmsReceiptDocument_EquMdfInvPckngAmount` |  |  |  |
| 41 | `INLEND.EDPMS.INVOICE.DISPATCH.INDICATOR` | `InlendEdpmsReceiptDocument_InvoiceDispatchIndicator` | TField |  | A Valid record from virtual table INLEND.DISPATCH.INDICATOR. Allowed values are 1 and 2.. |
| 42 | `INLEND.EDPMS.ACK.BILL.NUMBER` | `InlendEdpmsReceiptDocument_AckBillNumber` |  |  |  |
| 43 | `INLEND.EDPMS.DATE.OF.NEGOTIATION` | `InlendEdpmsReceiptDocument_DateOfNegotiation` | TField |  | Date of presentation. Defaulted from DRAWINGS. |
| 44 | `INLEND.EDPMS.BUYER.NAME` | `InlendEdpmsReceiptDocument_BuyerName` | TField |  | Name of Buyer. Defaulted from APPLICANT field of LC. |
| 45 | `INLEND.EDPMS.BUYER.COUNTRY` | `InlendEdpmsReceiptDocument_BuyerCountry` | TField |  | Country of Buyer. |
| 46 | `INLEND.EDPMS.CUSTOMER.ID` | `InlendEdpmsReceiptDocument_CustomerId` | TField |  | Fetched from INLEND.IEC.STATUS. |
| 47 | `INLEND.EDPMS.INVOICE.WRITE.OFF` | `InlendEdpmsReceiptDocument_InvoiceWriteOff` | TField |  | Drop-down field. Allowed Values are YES / NO. |
| 48 | `INLEND.EDPMS.DRAWING.REF.NUMBER` | `InlendEdpmsReceiptDocument_DrawingRefNumber` |  |  |  |
| 49 | `INLEND.EDPMS.INVOICE.NUMBER` | `InlendEdpmsReceiptDocument_InvoiceNumber` |  |  |  |
| 50 | `INLEND.EDPMS.INVOICE.SERIAL.NUMBER` | `InlendEdpmsReceiptDocument_InvoiceSerialNumber` |  |  |  |
| 51 | `INLEND.EDPMS.INVOICE.CURRENCY` | `InlendEdpmsReceiptDocument_InvoiceCurrency` |  |  |  |
| 52 | `INLEND.EDPMS.INVOICE.AMOUNT` | `InlendEdpmsReceiptDocument_InvoiceAmount` |  |  |  |
| 53 | `INLEND.EDPMS.INVOICE.WRITE.OFF.INDICATOR` | `InlendEdpmsReceiptDocument_InvoiceWriteOffIndicator` |  |  |  |
| 54 | `INLEND.EDPMS.INVOICE.WRITE.OFF.AMOUNT` | `InlendEdpmsReceiptDocument_InvoiceWriteOffAmount` |  |  |  |
| 55 | `INLEND.EDPMS.INVOICE.WRITE.OFF.DATE` | `InlendEdpmsReceiptDocument_InvoiceWriteOffDate` |  |  |  |
| 56 | `INLEND.EDPMS.PENDING.INVOICE.AMOUNT` | `InlendEdpmsReceiptDocument_PendingInvoiceAmount` |  |  |  |
| 57 | `INLEND.EDPMS.INVOICE.CLOSURE.STATUS` | `InlendEdpmsReceiptDocument_InvoiceClosureStatus` |  |  |  |
| 58 | `INLEND.EDPMS.FREIGHT.AMOUNT` | `InlendEdpmsReceiptDocument_FreightAmount` |  |  |  |
| 59 | `INLEND.EDPMS.INSURANCE.AMOUNT` | `InlendEdpmsReceiptDocument_InsuranceAmount` |  |  |  |
| 60 | `INLEND.EDPMS.CUST.TF.STATUS` | `InlendEdpmsReceiptDocument_CustTfStatus` | TField |  | Drop-down field. Allowed Values are YES / NO. |
| 61 | `INLEND.EDPMS.TOTAL.SHIPPING.BILL.AMOUNT` | `InlendEdpmsReceiptDocument_TotalShippingBillAmount` | TField |  | Total Amount in Shipping Bill. |
| 62 | `INLEND.EDPMS.TOT.SHIPPING.BILL.PENDING.AMT` | `InlendEdpmsReceiptDocument_TotShippingBillPendingAmt` | TField |  | Total Pending Amount of Shipping Bill. |
| 63 | `INLEND.EDPMS.SHIPPING.BILL.CLOSURE.IND` | `InlendEdpmsReceiptDocument_ShippingBillClosureInd` | TField |  | A Valid record from virtual table INLEND.IMP.EXP.RECORD.INDICATOR. Allowed values are 1 or 2. |
| 64 | `INLEND.EDPMS.MAX.PAYMENT.REALIZATION.DATE` | `InlendEdpmsReceiptDocument_MaxPaymentRealizationDate` | TField |  | Date within which Payment has to be realized. |
| 65 | `INLEND.EDPMS.REALIZATION.EXTENSION.APPROVER` | `InlendEdpmsReceiptDocument_RealizationExtensionApprover` | TField |  | A Valid record from virtual table INLEND.EXTENSION.AUTHORITY. |
| 66 | `INLEND.EDPMS.REALIZATION.EXT.LETTER.NUMBER` | `InlendEdpmsReceiptDocument_RealizationExtLetterNumber` | TField | Yes | Extension Letter Number. Mandatory if Extension approver is 2 (RBI). |
| 67 | `INLEND.EDPMS.REALIZATION.EXT.LETTER.DATE` | `InlendEdpmsReceiptDocument_RealizationExtLetterDate` | TField | Yes | Extension Letter Date, Mandatory if Extension approver is 2 (RBI). |
| 68 | `INLEND.EDPMS.EXTENDED.REALIZATION.DATE` | `InlendEdpmsReceiptDocument_ExtendedRealizationDate` | TField |  | New Extended Realization Date. |
| 69 | `INLEND.EDPMS.NO.OF.TIMES.PRN.EXTENDED` | `InlendEdpmsReceiptDocument_NoOfTimesPrnExtended` | TField |  | Number of times PRN was extended. Every time PRN is extended this counter should be updated by 1. |
| 70 | `INLEND.EDPMS.REALZN.EXTN.RECORD.INDICATOR` | `InlendEdpmsReceiptDocument_RealznExtnRecordIndicator` | TField |  | A Valid record from virtual table INLEND.IMP.EXP.RECORD.INDICATOR Allowed values are 1, 2 and 3. |
| 71 | `INLEND.EDPMS.WRITE.OFF.SEQUENCE.NUMBER` | `InlendEdpmsReceiptDocument_WriteOffSequenceNumber` | TField |  | A unique Writeoff Transaction Number, any cancellation of Writeoff can be done using this sequence number. |
| 72 | `INLEND.EDPMS.BOE.NUMBER` | `InlendEdpmsReceiptDocument_BoeNumber` | TField |  | A Valid record in INLEND.IDPMS.BOE. |
| 73 | `INLEND.EDPMS.DATE.BILL.OF.ENTRY` | `InlendEdpmsReceiptDocument_DateBillOfEntry` | TField |  | Date of BOE. |
| 74 | `INLEND.EDPMS.BOE.PORT.OF.DISCHARGE` | `InlendEdpmsReceiptDocument_BoePortOfDischarge` | TField |  | A Valid record from INLEND.PORT.LIST. |
| 75 | `INLEND.EDPMS.INV.WRITE.OFF.RECORD.INDICATOR` | `InlendEdpmsReceiptDocument_InvWriteOffRecordIndicator` | TField |  | A Valid record from virtual table INLEND.IMP.EXP.RECORD.INDICATOR Allowed values are 1 and 3. |
| 76 | `INLEND.EDPMS.REQ.BANK.AD.CODE` | `InlendEdpmsReceiptDocument_ReqBankAdCode` | TField |  | AD Code of Bank requesting Transfer of shipping bill. Will be updated by Interface when .tra XML file is received. No user input field. |
| 77 | `INLEND.EDPMS.TFR.REQ.STATUS` | `InlendEdpmsReceiptDocument_TfrReqStatus` | TField |  | A Valid record from virtual table INLEND.TFR.APPROVAL.STATUS. Allowed values are 1 and 2. |
| 78 | `INLEND.EDPMS.TFR.REQ.REMARKS` | `InlendEdpmsReceiptDocument_TfrReqRemarks` |  |  |  |
| 79 | `INLEND.EDPMS.MODE.OF.DATA` | `InlendEdpmsReceiptDocument_ModeOfData` | TField |  | Drop-down. Allowed values are UPLOAD and MANUAL. |
| 80 | `INLEND.EDPMS.ROD.RECORD.INDICATOR` | `InlendEdpmsReceiptDocument_RodRecordIndicator` | TField |  | A Valid record from virtual table INLEND.IMP.EXP.RECORD.INDICATOR. Allowed values are 1, 2 or 3. |
| 81 | `INLEND.EDPMS.ROD.UPLOAD.STATUS` | `InlendEdpmsReceiptDocument_RodUploadStatus` | TField |  | A Valid record from virtual table INLEND.EDPMS.UPLOAD.STATUS. |
| 82 | `INLEND.EDPMS.SET.OFF.INDICATOR` | `InlendEdpmsReceiptDocument_SetOffIndicator` | TField | Yes | Drop-down field. Allowed Values are YES / NO. Mandatory input if INVOICE.WRITE.OFF is selected as YES. |
| 83 | `INLEND.EDPMS.CHG.AD.CODE.REQ.INDICATOR` | `InlendEdpmsReceiptDocument_ChgAdCodeReqIndicator` | TField |  | A Valid record from INLEND.IMP.EXP.RECORD.INDICATOR. Allowed values are 1 or 3. |
| 84 | `INLEND.EDPMS.OLD.BANK.AD.CODE` | `InlendEdpmsReceiptDocument_OldBankAdCode` |  |  |  |
| 85 | `INLEND.EDPMS.TFR.DATE` | `InlendEdpmsReceiptDocument_TfrDate` |  |  |  |
| 86 | `INLEND.EDPMS.SHIPPING.BILL.DOE.REASON` | `InlendEdpmsReceiptDocument_ShippingBillDoeReason` |  |  |  |
| 87 | `INLEND.EDPMS.SHIPPING.BILL.DOE.DATE` | `InlendEdpmsReceiptDocument_ShippingBillDoeDate` | TField |  | Shipping Bill DOE Date. |
| 88 | `INLEND.EDPMS.SHIPPING.BILL.DOE.RECORD.IND` | `InlendEdpmsReceiptDocument_ShippingBillDoeRecordInd` | TField |  | Shipping Bill DOE Record Indicator. |
| 89 | `INLEND.EDPMS.INCOMING.PAYMENT.REF.ID` | `InlendEdpmsReceiptDocument_IncomingPaymentRefId` |  |  |  |
| 90 | `INLEND.EDPMS.TRANSACTION.DATE` | `InlendEdpmsReceiptDocument_TransactionDate` |  |  |  |
| 91 | `INLEND.EDPMS.GENERATE.BRC` | `InlendEdpmsReceiptDocument_GenerateBrc` | TField |  | No longer in use. |
| 92 | `INLEND.EDPMS.EBRC.ID` | `InlendEdpmsReceiptDocument_EbrcId` | TField |  | No longer in use. |
| 93 | `INLEND.EDPMS.BRC.DATE` | `InlendEdpmsReceiptDocument_BrcDate` | TField |  | No longer in use. |
| 94 | `INLEND.EDPMS.BRC.STATUS` | `InlendEdpmsReceiptDocument_BrcStatus` | TField |  | No longer in use. |
| 95 | `INLEND.EDPMS.BILL.ID` | `InlendEdpmsReceiptDocument_BillId` | TField |  | No longer in use. |
| 96 | `INLEND.EDPMS.BRC.CANCEL.DATE` | `InlendEdpmsReceiptDocument_BrcCancelDate` | TField |  | No longer in use. |
| 97 | `INLEND.EDPMS.PROCESS.DATE` | `InlendEdpmsReceiptDocument_ProcessDate` |  |  |  |
| 98 | `INLEND.EDPMS.ERROR.STATUS` | `InlendEdpmsReceiptDocument_ErrorStatus` |  |  |  |
| 99 | `INLEND.EDPMS.TRANSMIT.INDICATOR` | `InlendEdpmsReceiptDocument_TransmitIndicator` | TField |  | Drop-down field. A Valid record from INLEND.TRANSMIT.INDICATOR. System updated field |
| 100 | `INLEND.EDPMS.INTERFACE.ERROR.RESPONSE` | `InlendEdpmsReceiptDocument_InterfaceErrorResponse` | TField |  | Error response updated by EDPMS. |
| 101 | `INLEND.EDPMS.DOE.SB.PROCESS.DATE` | `InlendEdpmsReceiptDocument_DoeSbProcessDate` |  |  |  |
| 102 | `INLEND.EDPMS.DOE.SB.ERROR.CODE` | `InlendEdpmsReceiptDocument_DoeSbErrorCode` |  |  |  |
| 103 | `INLEND.EDPMS.REQ.TFR.AD.PROCESS.DATE` | `InlendEdpmsReceiptDocument_ReqTfrAdProcessDate` |  |  |  |
| 104 | `INLEND.EDPMS.REQ.TFR.AD.ERROR.CODE` | `InlendEdpmsReceiptDocument_ReqTfrAdErrorCode` |  |  |  |
| 105 | `INLEND.EDPMS.RESP.REQ.AD.TFR.PROCESS.DATE` | `InlendEdpmsReceiptDocument_RespReqAdTfrProcessDate` |  |  |  |
| 106 | `INLEND.EDPMS.RESP.REQ.AD.TFR.ERROR.CODE` | `InlendEdpmsReceiptDocument_RespReqAdTfrErrorCode` |  |  |  |
| 107 | `INLEND.EDPMS.LOCAL.REF` | `InlendEdpmsReceiptDocument_LocalRef` |  |  |  |
| 108 | `INLEND.EDPMS.OVERRIDE` | `InlendEdpmsReceiptDocument_Override` |  |  |  |
| 109 | `INLEND.EDPMS.RECORD.STATUS` | `InlendEdpmsReceiptDocument_RecordStatus` | String |  |  |
| 110 | `INLEND.EDPMS.CURR.NO` | `InlendEdpmsReceiptDocument_CurrNo` | String |  |  |
| 111 | `INLEND.EDPMS.INPUTTER` | `InlendEdpmsReceiptDocument_Inputter` |  |  |  |
| 112 | `INLEND.EDPMS.DATE.TIME` | `InlendEdpmsReceiptDocument_DateTime` |  |  |  |
| 113 | `INLEND.EDPMS.AUTHORISER` | `InlendEdpmsReceiptDocument_Authoriser` | String |  |  |
| 114 | `INLEND.EDPMS.CO.CODE` | `InlendEdpmsReceiptDocument_CoCode` | String |  |  |
| 115 | `INLEND.EDPMS.DEPT.CODE` | `InlendEdpmsReceiptDocument_DeptCode` | String |  |  |
| 116 | `INLEND.EDPMS.AUDITOR.CODE` | `InlendEdpmsReceiptDocument_AuditorCode` | String |  |  |
| 117 | `INLEND.EDPMS.AUDIT.DATE.TIME` | `InlendEdpmsReceiptDocument_AuditDateTime` | String |  |  |
| 118 | `INLEND.EDPMS.TOTAL.INV.REALZN.AMOUNT` | `InlendEdpmsReceiptDocument_TotalInvRealznAmount` |  |  |  |
| 119 | `INLEND.EDPMS.PMT.REALIZATION.DATE` | `InlendEdpmsReceiptDocument_PmtRealizationDate` |  |  |  |
| 120 | `INLEND.EDPMS.REALZD.INV.FOB.AMOUNT` | `InlendEdpmsReceiptDocument_RealzdInvFobAmount` |  |  |  |
| 121 | `INLEND.EDPMS.REALZD.INV.FREIGHT.AMOUNT` | `InlendEdpmsReceiptDocument_RealzdInvFreightAmount` |  |  |  |
| 122 | `INLEND.EDPMS.REALZD.INV.INS.AMOUNT` | `InlendEdpmsReceiptDocument_RealzdInvInsAmount` |  |  |  |
| 123 | `INLEND.EDPMS.PYMNT.RLZN.CANCEL.FLAG` | `InlendEdpmsReceiptDocument_PymntRlznCancelFlag` |  |  |  |
| 124 | `INLEND.EDPMS.TOTAL.REALZD.INV.AMOUNT` | `InlendEdpmsReceiptDocument_TotalRealzdInvAmount` |  |  |  |
| 125 | `INLEND.EDPMS.TOTAL.INV.REALZN.PENDING.AMT` | `InlendEdpmsReceiptDocument_TotalInvRealznPendingAmt` |  |  |  |
| 126 | `INLEND.EDPMS.WRITE.OFF.AMOUNT` | `InlendEdpmsReceiptDocument_WriteOffAmount` |  |  |  |
| 127 | `INLEND.EDPMS.WRITE.OFF.DATE` | `InlendEdpmsReceiptDocument_WriteOffDate` |  |  |  |
| 128 | `INLEND.EDPMS.INV.WRITE.OFF.INITIATOR` | `InlendEdpmsReceiptDocument_InvWriteOffInitiator` |  |  |  |
| 129 | `INLEND.EDPMS.INV.WRITE.OFF.CANC.FLAG` | `InlendEdpmsReceiptDocument_InvWriteOffCancFlag` |  |  |  |
| 130 | `INLEND.EDPMS.INV.CLOSURE.STATUS` | `InlendEdpmsReceiptDocument_InvClosureStatus` |  |  |  |
| 131 | `INLEND.EDPMS.INVOICE.CLOSURE.INDICATOR` | `InlendEdpmsReceiptDocument_InvoiceClosureIndicator` |  |  |  |
| 132 | `INLEND.EDPMS.WRITE.OFF.REASON.INDICATOR` | `InlendEdpmsReceiptDocument_WriteOffReasonIndicator` | TField |  | Reason indicator for write-off. A Valid record from INLEND.EXP.WRITEOFF.INDICATOR. |
| 133 | `INLEND.EDPMS.DOE.SB.REQUIRED` | `InlendEdpmsReceiptDocument_DoeSbRequired` | TField |  | Whether DOE SB is required. Drop-down field. Allowed Values are YES / NO. |
| 134 | `INLEND.EDPMS.SB.WRITE.OFF.PROCESS.DATE` | `InlendEdpmsReceiptDocument_SbWriteOffProcessDate` |  |  |  |
| 135 | `INLEND.EDPMS.SB.WRITE.OFF.ERROR.CODE` | `InlendEdpmsReceiptDocument_SbWriteOffErrorCode` |  |  |  |
| 136 | `INLEND.EDPMS.PMT.RLZN.EXTN.REQUIRED` | `InlendEdpmsReceiptDocument_PmtRlznExtnRequired` | TField |  | Whether PMT RLZN extension required. Drop-down field. Allowed values are YES / NO. |
| 137 | `INLEND.EDPMS.PMT.RLZN.EXTN.PROCESS.DATE` | `InlendEdpmsReceiptDocument_PmtRlznExtnProcessDate` |  |  |  |
| 138 | `INLEND.EDPMS.PMT.RLZN.EXTN.ERROR.STATUS` | `InlendEdpmsReceiptDocument_PmtRlznExtnErrorStatus` |  |  |  |
| 139 | `INLEND.EDPMS.DECLARED.CURRENCY` | `InlendEdpmsReceiptDocument_DeclaredCurrency` |  |  |  |
| 140 | `INLEND.EDPMS.TOTAL.INV.COMMISSION.AMOUNT` | `InlendEdpmsReceiptDocument_TotalInvCommissionAmount` |  |  |  |
| 141 | `INLEND.EDPMS.TOTAL.INV.DISCOUNT.AMOUNT` | `InlendEdpmsReceiptDocument_TotalInvDiscountAmount` |  |  |  |
| 142 | `INLEND.EDPMS.TOTAL.INV.DEDUCTION.AMOUNT` | `InlendEdpmsReceiptDocument_TotalInvDeductionAmount` |  |  |  |
| 143 | `INLEND.EDPMS.TOTAL.INV.PACKAGING.AMOUNT` | `InlendEdpmsReceiptDocument_TotalInvPackagingAmount` |  |  |  |
| 144 | `INLEND.EDPMS.DRAWING.INVOICE.UPDATE` | `InlendEdpmsReceiptDocument_DrawingInvoiceUpdate` | TField |  | Whether Invoice details of drawing mapped to shipping bill. Allowed values are YES / NO. |
| 145 | `INLEND.EDPMS.INVOICE.WRITEOFF.REQD` | `InlendEdpmsReceiptDocument_InvoiceWriteoffReqd` |  |  |  |
| 146 | `INLEND.EDPMS.EDPMS.ROD.PROCESS.NAME` | `InlendEdpmsReceiptDocument_EdpmsRodProcessName` | TField |  | Indicates the Receipt Document Process. |
| 147 | `INLEND.EDPMS.PAYMENT.SEQ.NUMBER` | `InlendEdpmsReceiptDocument_PaymentSeqNumber` |  |  |  |
