# INLEND.BOE.SETTLEMENT — Table Schema

> Source: `INSERTS/I_F.INLEND.BOE.SETTLEMENT` in `INDPMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INLEND.BOE.DATE.BILL.OF.ENTRY` | `InlendBoeSettlement_DateBillOfEntry` | TField |  | Date of Bill of Entry.Should be Defaulted from INLEND.IDPMS.BOE |
| 2 | `INLEND.BOE.DATE.OF.BOE.SETTLEMENT` | `InlendBoeSettlement_DateOfBoeSettlement` | TField |  | Date of BOE Settlement.Should be Current System Date.. |
| 3 | `INLEND.BOE.BOE.INVOICE.NUMBER` | `InlendBoeSettlement_BoeInvoiceNumber` |  |  |  |
| 4 | `INLEND.BOE.BOE.INVOICE.CURRENCY` | `InlendBoeSettlement_BoeInvoiceCurrency` |  |  |  |
| 5 | `INLEND.BOE.BOE.INVOICE.AMOUNT` | `InlendBoeSettlement_BoeInvoiceAmount` |  |  |  |
| 6 | `INLEND.BOE.BTT.UNRLZD.INVOICE.AMOUNT` | `InlendBoeSettlement_BttUnrlzdInvoiceAmount` |  |  |  |
| 7 | `INLEND.BOE.ORM.REFERENCE.NUMBER` | `InlendBoeSettlement_OrmReferenceNumber` |  |  |  |
| 8 | `INLEND.BOE.ORM.SETTLE.INVOICE` | `InlendBoeSettlement_OrmSettleInvoice` |  |  |  |
| 9 | `INLEND.BOE.ORM.SETTLE.AMOUNT` | `InlendBoeSettlement_OrmSettleAmount` |  |  |  |
| 10 | `INLEND.BOE.PAYMENT.REF.NUMBER` | `InlendBoeSettlement_PaymentRefNumber` |  |  |  |
| 11 | `INLEND.BOE.BOE.CLOSURE.INDICATOR` | `InlendBoeSettlement_BoeClosureIndicator` | TField |  | This field is no longer in use |
| 12 | `INLEND.BOE.RECORD.INDICATOR` | `InlendBoeSettlement_RecordIndicator` | TField |  | Record Indicator.A Valid Record From INLEND.IMP.EXP.RECORD.INDICATOR. |
| 13 | `INLEND.BOE.BOE.NUMBER` | `InlendBoeSettlement_BoeNumber` | TField |  | BOE Id of the settlement |
| 14 | `INLEND.BOE.BES.PROCESS.DATE` | `InlendBoeSettlement_BesProcessDate` |  |  |  |
| 15 | `INLEND.BOE.BES.ERROR.STATUS` | `InlendBoeSettlement_BesErrorStatus` |  |  |  |
| 16 | `INLEND.BOE.TRANSMIT.INDICATOR` | `InlendBoeSettlement_TransmitIndicator` | TField |  | Drop-down field. Allowed values are 1. Ready to Transmit. 2. Transmit successful and 3. Transmit Error. SYSTEM UPDATED FIELDS |
| 17 | `INLEND.BOE.BOE.SETTLEMENT.SEQ` | `InlendBoeSettlement_BoeSettlementSeq` | TField |  | Sequence number of a BOE Settlement ID. |
| 18 | `INLEND.BOE.BOE.INVOICE.CNCY` | `InlendBoeSettlement_BoeInvoiceCncy` |  |  |  |
| 19 | `INLEND.BOE.TOTAL.BOE.SETTLEMENT.AMOUNT` | `InlendBoeSettlement_TotalBoeSettlementAmount` |  |  |  |
| 20 | `INLEND.BOE.INTERFACE.ERROR.RESPONSE` | `InlendBoeSettlement_InterfaceErrorResponse` | TField |  | Field to capture Interface Response |
| 21 | `INLEND.BOE.BOE.PROCESS.NAME` | `InlendBoeSettlement_BoeProcessName` | TField |  | Field to capture the process name of IDPMS |
| 22 | `INLEND.BOE.RESERVED.1` | `InlendBoeSettlement_Reserved1` | TField |  | Reserved for future purpose |
| 23 | `INLEND.BOE.LOCAL.REF` | `InlendBoeSettlement_LocalRef` |  |  |  |
| 24 | `INLEND.BOE.OVERRIDE` | `InlendBoeSettlement_Override` |  |  |  |
| 25 | `INLEND.BOE.RECORD.STATUS` | `InlendBoeSettlement_RecordStatus` | String |  |  |
| 26 | `INLEND.BOE.CURR.NO` | `InlendBoeSettlement_CurrNo` | String |  |  |
| 27 | `INLEND.BOE.INPUTTER` | `InlendBoeSettlement_Inputter` |  |  |  |
| 28 | `INLEND.BOE.DATE.TIME` | `InlendBoeSettlement_DateTime` |  |  |  |
| 29 | `INLEND.BOE.AUTHORISER` | `InlendBoeSettlement_Authoriser` | String |  |  |
| 30 | `INLEND.BOE.CO.CODE` | `InlendBoeSettlement_CoCode` | String |  |  |
| 31 | `INLEND.BOE.DEPT.CODE` | `InlendBoeSettlement_DeptCode` | String |  |  |
| 32 | `INLEND.BOE.AUDITOR.CODE` | `InlendBoeSettlement_AuditorCode` | String |  |  |
| 33 | `INLEND.BOE.AUDIT.DATE.TIME` | `InlendBoeSettlement_AuditDateTime` | String |  |  |
| 34 | `INLEND.BOE.BTT.RLZD.INVOICE.AMOUNT` | `InlendBoeSettlement_BttRlzdInvoiceAmount` |  |  |  |
| 35 | `INLEND.BOE.ORM.CURRENCY` | `InlendBoeSettlement_OrmCurrency` |  |  |  |
| 36 | `INLEND.BOE.ORM.AMOUNT` | `InlendBoeSettlement_OrmAmount` |  |  |  |
| 37 | `INLEND.BOE.ORM.INVOICE.AMOUNT` | `InlendBoeSettlement_OrmInvoiceAmount` |  |  |  |
| 38 | `INLEND.BOE.BES.EXCHANGE.RATE` | `InlendBoeSettlement_BesExchangeRate` |  |  |  |
| 39 | `INLEND.BOE.BOE.EQU.INVOICE.SETTLE.AMOUNT` | `InlendBoeSettlement_BoeEquInvoiceSettleAmount` |  |  |  |
