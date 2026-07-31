# INLEND.EDPMS.INTF.REQ.DTLS — Table Schema

> Source: `INSERTS/I_F.INLEND.EDPMS.INTF.REQ.DTLS` in `INDPMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INLEND.INTF.SHIPPING.BILL.NUMBER` | `InlendEdpmsIntfReqDtls_ShippingBillNumber` | TField |  | Shipping Bill Number Provided By User |
| 2 | `INLEND.INTF.INVOICE.NUMBER` | `InlendEdpmsIntfReqDtls_InvoiceNumber` |  |  |  |
| 3 | `INLEND.INTF.INVOICE.DATE` | `InlendEdpmsIntfReqDtls_InvoiceDate` |  |  |  |
| 4 | `INLEND.INTF.INV.FOB.CURRENCY` | `InlendEdpmsIntfReqDtls_InvFobCurrency` |  |  |  |
| 5 | `INLEND.INTF.WRITE.OFF.AMOUNT` | `InlendEdpmsIntfReqDtls_WriteOffAmount` |  |  |  |
| 6 | `INLEND.INTF.WRITE.OFF.DATE` | `InlendEdpmsIntfReqDtls_WriteOffDate` |  |  |  |
| 7 | `INLEND.INTF.INV.WRITE.OFF.INITIATOR` | `InlendEdpmsIntfReqDtls_InvWriteOffInitiator` |  |  |  |
| 8 | `INLEND.INTF.INV.WRITE.OFF.CANC.FLAG` | `InlendEdpmsIntfReqDtls_InvWriteOffCancFlag` |  |  |  |
| 9 | `INLEND.INTF.INV.CLOSURE.STATUS` | `InlendEdpmsIntfReqDtls_InvClosureStatus` |  |  |  |
| 10 | `INLEND.INTF.WRITE.OFF.SEQUENCE.NUMBER` | `InlendEdpmsIntfReqDtls_WriteOffSequenceNumber` | TField |  | A unique Writeoff Transaction Number, any cancellation of Writeoff can be done using this sequence number. |
| 11 | `INLEND.INTF.WRITE.OFF.REASON.INDICATOR` | `InlendEdpmsIntfReqDtls_WriteOffReasonIndicator` | TField |  | Reason indicator for write-off. A Valid record from INLEND.EXP.WRITEOFF.INDICATOR. |
| 12 | `INLEND.INTF.BOE.NUMBER` | `InlendEdpmsIntfReqDtls_BoeNumber` | TField |  | A Valid record in INLEND.IDPMS.BOE. |
| 13 | `INLEND.INTF.DATE.BILL.OF.ENTRY` | `InlendEdpmsIntfReqDtls_DateBillOfEntry` | TField |  | Date of BOE. |
| 14 | `INLEND.INTF.BOE.PORT.OF.DISCHARGE` | `InlendEdpmsIntfReqDtls_BoePortOfDischarge` | TField |  | A Valid record from INLEND.PORT.LIST. |
| 15 | `INLEND.INTF.SB.WRITE.OFF.RECORD.INDICATOR` | `InlendEdpmsIntfReqDtls_SbWriteOffRecordIndicator` | TField |  | A Valid record from virtual table INLEND.IMP.EXP.RECORD.INDICATOR Allowed values are 1 and 3. |
| 16 | `INLEND.INTF.INTERFACE.ERROR.RESPONSE` | `InlendEdpmsIntfReqDtls_InterfaceErrorResponse` | TField |  | Error response updated by EDPMS. |
| 17 | `INLEND.INTF.IRM.REFERENCE` | `InlendEdpmsIntfReqDtls_IrmReference` | TField |  | Derived from POR tables. |
| 18 | `INLEND.INTF.IRM.TRANSACTION.CURRENCY` | `InlendEdpmsIntfReqDtls_IrmTransactionCurrency` | TField |  | Currency. |
| 19 | `INLEND.INTF.IRM.ADJUSTMENT.AMOUNT` | `InlendEdpmsIntfReqDtls_IrmAdjustmentAmount` | TField |  | IRM Adjusted Amount. |
| 20 | `INLEND.INTF.IRM.ADJUSTMENT.INDICATOR` | `InlendEdpmsIntfReqDtls_IrmAdjustmentIndicator` | TField |  | A Valid record from INLEND.IRM.ADJ.INDICATOR. |
| 21 | `INLEND.INTF.IRM.ADJUSTMENT.APPROVER` | `InlendEdpmsIntfReqDtls_IrmAdjustmentApprover` | TField |  | IRM Adjustment Approver. A Valid record from INLEND.EXTENSION.AUTHORITY. |
| 22 | `INLEND.INTF.IRM.ADJ.LETTER.NUMBER` | `InlendEdpmsIntfReqDtls_IrmAdjLetterNumber` | TField |  | IRM Adjustment Letter Number. |
| 23 | `INLEND.INTF.IRM.ADJ.LETTER.DATE` | `InlendEdpmsIntfReqDtls_IrmAdjLetterDate` | TField |  | IRM Adjustment Letter Date. |
| 24 | `INLEND.INTF.IRM.ADJ.EXP.DOC.NUMBER` | `InlendEdpmsIntfReqDtls_IrmAdjExpDocNumber` | TField |  | Export Document Number. |
| 25 | `INLEND.INTF.IRM.ADJ.EXP.DOC.DATE` | `InlendEdpmsIntfReqDtls_IrmAdjExpDocDate` | TField |  | Export Document Date. |
| 26 | `INLEND.INTF.IRM.ADJ.EXP.DOC.PORT.RECV` | `InlendEdpmsIntfReqDtls_IrmAdjExpDocPortRecv` | TField |  | A Valid record from INLEND.PORT.LIST. |
| 27 | `INLEND.INTF.FIRC.UNUTILIZED.AMOUNT` | `InlendEdpmsIntfReqDtls_FircUnutilizedAmount` | TField |  | Un-utilized amount of FIRC. |
| 28 | `INLEND.INTF.FIRC.UTILIZED.AMOUNT` | `InlendEdpmsIntfReqDtls_FircUtilizedAmount` | TField |  | Utilized amount of FIRC. |
| 29 | `INLEND.INTF.TFR.TO.IRM.AMOUNT` | `InlendEdpmsIntfReqDtls_TfrToIrmAmount` | TField |  | Amount transferred to IRM because of FIRC adjustment / closure. |
| 30 | `INLEND.INTF.FIRC.DATE.ADJUSTMENT` | `InlendEdpmsIntfReqDtls_FircDateAdjustment` | TField |  | Date of FIRC Adjustment / Closure. |
| 31 | `INLEND.INTF.FIRC.CLOSURE.AMOUNT` | `InlendEdpmsIntfReqDtls_FircClosureAmount` | TField |  | FIRC Closure Amount. |
| 32 | `INLEND.INTF.FIRC.CLOSURE.REASON` | `InlendEdpmsIntfReqDtls_FircClosureReason` |  |  |  |
| 33 | `INLEND.INTF.FIRC.CLOSURE.REMARKS` | `InlendEdpmsIntfReqDtls_FircClosureRemarks` |  |  |  |
| 34 | `INLEND.INTF.FIRC.CLOSURE.APPROVAL` | `InlendEdpmsIntfReqDtls_FircClosureApproval` | TField |  | Approver of FIRC Closure/Adjustment.A Valid record from INLEND.EXTENSION.AUTHORITY. |
| 35 | `INLEND.INTF.FIRC.CLOSURE.LETTER.NUMBER` | `InlendEdpmsIntfReqDtls_FircClosureLetterNumber` | TField |  | FIRC Closure Approval Letter Number. |
| 36 | `INLEND.INTF.FIRC.CLOSURE.LETTER.DATE` | `InlendEdpmsIntfReqDtls_FircClosureLetterDate` | TField |  | FIRC Closure Approval Letter Date. |
| 37 | `INLEND.INTF.BOE.INVOICE.NUMBER` | `InlendEdpmsIntfReqDtls_BoeInvoiceNumber` | TField |  | Stores Invoice value from INLEND.BOE.SETTLEMENT Template. |
| 38 | `INLEND.INTF.BOE.INVOICE.CURRENCY` | `InlendEdpmsIntfReqDtls_BoeInvoiceCurrency` | TField |  | Stores the Currency of Corresponding BOE Invoice from INLEND.BOE.SETTLEMENT Template. |
| 39 | `INLEND.INTF.BOE.INVOICE.AMOUNT` | `InlendEdpmsIntfReqDtls_BoeInvoiceAmount` | TField |  | Stores the Amount of Corresponding BOE Invoice from INLEND.BOE.SETTLEMENT Template. |
| 40 | `INLEND.INTF.ORM.REFERENCE.NUMBER` | `InlendEdpmsIntfReqDtls_OrmReferenceNumber` | TField |  | Stores Orm Reference value from INLEND.BOE.SETTLEMENT Template. |
| 41 | `INLEND.INTF.ORM.CURRENCY` | `InlendEdpmsIntfReqDtls_OrmCurrency` | TField |  | Stores ORM currency value from INLEND.BOE.SETTLEMENT Template. |
| 42 | `INLEND.INTF.ORM.AMOUNT` | `InlendEdpmsIntfReqDtls_OrmAmount` | TField |  | Stores ORM Amount value from INLEND.BOE.SETTLEMENT Template. |
| 43 | `INLEND.INTF.ORM.SETTLE.INVOICE` | `InlendEdpmsIntfReqDtls_OrmSettleInvoice` | TField |  | Stores ORM Invoice value from INLEND.BOE.SETTLEMENT Template. |
| 44 | `INLEND.INTF.ORM.INVOICE.AMOUNT` | `InlendEdpmsIntfReqDtls_OrmInvoiceAmount` | TField |  | Stores ORM total amount value from INLEND.BOE.SETTLEMENT Template. |
| 45 | `INLEND.INTF.ORM.SETTLE.AMOUNT` | `InlendEdpmsIntfReqDtls_OrmSettleAmount` | TField |  | Stores ORM Settle amount value from INLEND.BOE.SETTLEMENT Template. |
| 46 | `INLEND.INTF.BES.EXCHANGE.RATE` | `InlendEdpmsIntfReqDtls_BesExchangeRate` | TField |  | StoresExchange rate value from INLEND.BOE.SETTLEMENT Template. |
| 47 | `INLEND.INTF.LOCAL.REF` | `InlendEdpmsIntfReqDtls_LocalRef` |  |  |  |
| 48 | `INLEND.INTF.OVERRIDE` | `InlendEdpmsIntfReqDtls_Override` |  |  |  |
| 49 | `INLEND.INTF.RECORD.STATUS` | `InlendEdpmsIntfReqDtls_RecordStatus` | String |  |  |
| 50 | `INLEND.INTF.CURR.NO` | `InlendEdpmsIntfReqDtls_CurrNo` | String |  |  |
| 51 | `INLEND.INTF.INPUTTER` | `InlendEdpmsIntfReqDtls_Inputter` |  |  |  |
| 52 | `INLEND.INTF.DATE.TIME` | `InlendEdpmsIntfReqDtls_DateTime` |  |  |  |
| 53 | `INLEND.INTF.AUTHORISER` | `InlendEdpmsIntfReqDtls_Authoriser` | String |  |  |
| 54 | `INLEND.INTF.CO.CODE` | `InlendEdpmsIntfReqDtls_CoCode` | String |  |  |
| 55 | `INLEND.INTF.DEPT.CODE` | `InlendEdpmsIntfReqDtls_DeptCode` | String |  |  |
| 56 | `INLEND.INTF.AUDITOR.CODE` | `InlendEdpmsIntfReqDtls_AuditorCode` | String |  |  |
| 57 | `INLEND.INTF.AUDIT.DATE.TIME` | `InlendEdpmsIntfReqDtls_AuditDateTime` | String |  |  |
| 58 | `INLEND.INTF.BOE.EQU.INVOICE.SETTLE.AMOUNT` | `InlendEdpmsIntfReqDtls_BoeEquInvoiceSettleAmount` | TField |  | Stores Equivalent BOE Invoice amount value from INLEND.BOE.SETTLEMENT Template. |
| 59 | `INLEND.INTF.BES.PROCESS.DATE` | `InlendEdpmsIntfReqDtls_BesProcessDate` |  |  |  |
| 60 | `INLEND.INTF.BES.ERROR.STATUS` | `InlendEdpmsIntfReqDtls_BesErrorStatus` |  |  |  |
| 61 | `INLEND.INTF.SET.INTERFACE.ERROR.RESPONSE` | `InlendEdpmsIntfReqDtls_SetInterfaceErrorResponse` | TField |  | Field to capture Interface Response. |
| 62 | `INLEND.INTF.RECORD.INDICATOR` | `InlendEdpmsIntfReqDtls_RecordIndicator` | TField |  | Record Indicator.A Valid Record From INLEND.IMP.EXP.RECORD.INDICATOR. |
| 63 | `INLEND.INTF.BOE.PROCESS.NAME` | `InlendEdpmsIntfReqDtls_BoeProcessName` | TField |  | Field to capture the process name of IDPMS. |
| 64 | `INLEND.INTF.SETTLEMENT.ID` | `InlendEdpmsIntfReqDtls_SettlementId` | TField |  | Field to capture the Settlement ID for which the invoices belong to |
