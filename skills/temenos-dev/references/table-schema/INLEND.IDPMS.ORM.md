# INLEND.IDPMS.ORM — Table Schema

> Source: `INSERTS/I_F.INLEND.IDPMS.ORM` in `INDPMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INLEND.ORM.OUTWARD.DEBIT.ACCOUNT` | `InlendIdpmsOrm_OutwardDebitAccount` | TField | Yes | Account Number of Remitter. Defaulted from PO MANDATORY |
| 2 | `INLEND.ORM.OUTWARD.REMITTANCE.CURRENCY` | `InlendIdpmsOrm_OutwardRemittanceCurrency` | TField | Yes | Currency of Remitted Amount. Defaulted from PO MANDATORY |
| 3 | `INLEND.ORM.OUTWARD.REMITTANCE.AMOUNT` | `InlendIdpmsOrm_OutwardRemittanceAmount` | TField | Yes | Remitted Amount. If ID is a POA ID, then this field should hold amount from PAYMENT.AMOUNT. If ID is a DRAWINGS ID, then this field should hold amount from REIMBURSE.AMOUNT (DRAWINGS) or PAYMENT.AMOUNT (DRAWINGS) based on parameter settings. MANDATORY |
| 4 | `INLEND.ORM.OUTWARD.REMITTANCE.DATE` | `InlendIdpmsOrm_OutwardRemittanceDate` | TField | Yes | Date of Remittance Defaulted from PO MANDATORY |
| 5 | `INLEND.ORM.TIME.BARRED.DATE` | `InlendIdpmsOrm_TimeBarredDate` | TField |  | Date beyond which ORM cannot be used for settlement against BOE. System updated field. No user input allowed. Derived value Sum of OUTWARD.REMITTANCE.DATE, DAYS.STALE.REMITTANCE and GRACE.PERIOD.ORM |
| 6 | `INLEND.ORM.RECORD.INDICATOR` | `InlendIdpmsOrm_RecordIndicator` | TField |  | A Valid record from virtual table INLEND.IMP.EXP.RECORD.INDICATOR. Allowed values are 1, 2 and 3. SYSTEM UPDATED FIELD. First time when a record is created, this field should hold a value of 1. Any amendments done on the record, this field should hold a value of 2. If record is cancelled this field should hold a value of 3. No user input allowed. |
| 7 | `INLEND.ORM.IS.CAPITAL.GOODS` | `InlendIdpmsOrm_IsCapitalGoods` | TField | Yes | Drop-down field. Valid values are YES or NO. MANDATORY |
| 8 | `INLEND.ORM.REMARKS` | `InlendIdpmsOrm_Remarks` |  |  |  |
| 9 | `INLEND.ORM.PAYMENT.TERMS` | `InlendIdpmsOrm_PaymentTerms` | TField | Yes | A Valid record from virtual table INLEND.PAYMENT.TERMS MANDATORY |
| 10 | `INLEND.ORM.ADV.PMT.TF.REF.NUMBER` | `InlendIdpmsOrm_AdvPmtTfRefNumber` | TField | Yes | Advance Payment TF reference number MANDATORY, if @ID starts with PI, else no input allowed. System updated field. No amendments allowed. No user input. |
| 11 | `INLEND.ORM.DRAWINGS.TF.REF.NUMBER` | `InlendIdpmsOrm_DrawingsTfRefNumber` | TField | Yes | Payment ID created from Drawings Module, when a drawing is made. MANDATORY, if @ID starts with TF, else no input allowed. System updated field. No amendments allowed. No user input allowed. |
| 12 | `INLEND.ORM.SETTLED.BOE.NUMBER` | `InlendIdpmsOrm_SettledBoeNumber` |  |  |  |
| 13 | `INLEND.ORM.SETTLED.INVOICE.NUMBER` | `InlendIdpmsOrm_SettledInvoiceNumber` |  |  |  |
| 14 | `INLEND.ORM.SETTLED.DATE` | `InlendIdpmsOrm_SettledDate` |  |  |  |
| 15 | `INLEND.ORM.SETTLED.INOVICE.AMOUNT` | `InlendIdpmsOrm_SettledInoviceAmount` |  |  |  |
| 16 | `INLEND.ORM.ORM.PENDING.AMOUNT` | `InlendIdpmsOrm_OrmPendingAmount` | TField |  | Amount pending for settlement in ORM System updated field. No user input allowed. |
| 17 | `INLEND.ORM.PO.PAYMENT.AMOUNT` | `InlendIdpmsOrm_PoPaymentAmount` | TField |  | PO Payment remitted amount. Should be updated from DRAWINGS, if REMITTANCE.AMOUNT.GROSS.NET = GROSS System updated field. No user input allowed. Will be updated during BOE settlement process. |
| 18 | `INLEND.ORM.ALLOWED.TO.SETTLE` | `InlendIdpmsOrm_AllowedToSettle` | TField |  | Drop-down field. Allowed values are NULL and YES. DEFAULT VALUE IS YES. System updated field. No user input allowed. |
| 19 | `INLEND.ORM.ORM.EXTENSION.APPROVER` | `InlendIdpmsOrm_OrmExtensionApprover` | TField | Yes | A Valid record from virtual table INLEND.EXTENSION.AUTHORITY. Should be defaulted to 2. MANDATORY, if DATE.OF.EXTENSION is entered. |
| 20 | `INLEND.ORM.ORM.EXTN.LETTER.NUMBER` | `InlendIdpmsOrm_OrmExtnLetterNumber` | TField | Yes | Letter number for extension provided by RBI MANDATORY, if DATE.OF.EXTENSION is entered. |
| 21 | `INLEND.ORM.ORM.EXTN.LETTER.DATE` | `InlendIdpmsOrm_OrmExtnLetterDate` | TField | Yes | Letter date for extension provided by RBI MANDATORY, if DATE.OF.EXTENSION is entered. |
| 22 | `INLEND.ORM.DATE.OF.EXTENSION` | `InlendIdpmsOrm_DateOfExtension` | TField |  | Extended Date. BOE settlement for ORM will be allowed only up to this date. INPUT allowed only when SYSTEM DATE greater than TIME.BARRED.DATE and ALLOWED.TO.SETTLE is NULL |
| 23 | `INLEND.ORM.ORM.EXTENSION.REMARKS` | `InlendIdpmsOrm_OrmExtensionRemarks` | TField |  | ORM closure remarks |
| 24 | `INLEND.ORM.ORM.ADJUSTED.AMOUNT` | `InlendIdpmsOrm_OrmAdjustedAmount` |  |  |  |
| 25 | `INLEND.ORM.ORM.ADJUSTED.DATE` | `InlendIdpmsOrm_OrmAdjustedDate` |  |  |  |
| 26 | `INLEND.ORM.ORM.ADJUSTMENT.INDICATOR` | `InlendIdpmsOrm_OrmAdjustmentIndicator` |  |  |  |
| 27 | `INLEND.ORM.ORM.ADJUSTMENT.SEQ.NUMBER` | `InlendIdpmsOrm_OrmAdjustmentSeqNumber` |  |  |  |
| 28 | `INLEND.ORM.ORM.LETTER.NUMBER` | `InlendIdpmsOrm_OrmLetterNumber` |  |  |  |
| 29 | `INLEND.ORM.ORM.LETTER.DATE` | `InlendIdpmsOrm_OrmLetterDate` |  |  |  |
| 30 | `INLEND.ORM.ORM.DOCUMENT.NUMBER` | `InlendIdpmsOrm_OrmDocumentNumber` |  |  |  |
| 31 | `INLEND.ORM.ORM.DOCUMENT.DATE` | `InlendIdpmsOrm_OrmDocumentDate` |  |  |  |
| 32 | `INLEND.ORM.ORM.CLOSURE.REMARKS` | `InlendIdpmsOrm_OrmClosureRemarks` |  |  |  |
| 33 | `INLEND.ORM.ORM.ADJUSTMENT.APPROVER` | `InlendIdpmsOrm_OrmAdjustmentApprover` |  |  |  |
| 34 | `INLEND.ORM.PAYMENT.PARTY` | `InlendIdpmsOrm_PaymentParty` | TField | Yes | Is payment made to third party. Drop-down field. Allowed values YES / NO. If ORM ID is a PO ID then this field should be defaulted to NO and if ORM ID is a DRAWINGS ID then user can select appropriate value. MANDATORY |
| 35 | `INLEND.ORM.CLOSURE.RECORD.INDICATOR` | `InlendIdpmsOrm_ClosureRecordIndicator` | TField | Yes | Record Indicator. A Valid record from INLEND.IMP.EXP.RECORD.INDICATOR. Allowed values are 1 and 3. MANDATORY if ORM.ADJUSTMENT.APPROVER Not Equal to Null |
| 36 | `INLEND.ORM.ORM.CLOSURE.INDICATOR` | `InlendIdpmsOrm_OrmClosureIndicator` | TField |  | Record Indicator. It is used to indicate whether ORM status is closed or open. |
| 37 | `INLEND.ORM.ORM.CUSTOMER.ID` | `InlendIdpmsOrm_OrmCustomerId` | TField |  | Ordering Customer from Payment Order |
| 38 | `INLEND.ORM.DOE.REFERENCE.DATE` | `InlendIdpmsOrm_DoeReferenceDate` | TField |  | Date on which ORM is referred to RBI and DOE. Should be defaulted to current system date. No past or future date allowed. |
| 39 | `INLEND.ORM.DOE.REASON` | `InlendIdpmsOrm_DoeReason` |  |  |  |
| 40 | `INLEND.ORM.DOE.RECORD.INDICATOR` | `InlendIdpmsOrm_DoeRecordIndicator` | TField | Yes | Record Indicator. A Valid record from INLEND.IMP.EXP.RECORD.INDICATOR. Allowed values are 1 and 3. MANDATORY if DOE.REFERENCE.DATE Not Equal to Null |
| 41 | `INLEND.ORM.LOCAL.REF` | `InlendIdpmsOrm_LocalRef` |  |  |  |
| 42 | `INLEND.ORM.ORM.PROCESS.DATE` | `InlendIdpmsOrm_OrmProcessDate` |  |  |  |
| 43 | `INLEND.ORM.ORM.ERROR.STATUS` | `InlendIdpmsOrm_OrmErrorStatus` |  |  |  |
| 44 | `INLEND.ORM.ORA.PROC.DATE` | `InlendIdpmsOrm_OraProcDate` |  |  |  |
| 45 | `INLEND.ORM.ORA.ERROR.STATUS` | `InlendIdpmsOrm_OraErrorStatus` |  |  |  |
| 46 | `INLEND.ORM.DOE.PROCESS.DATE` | `InlendIdpmsOrm_DoeProcessDate` |  |  |  |
| 47 | `INLEND.ORM.DOE.ERROR.STATUS` | `InlendIdpmsOrm_DoeErrorStatus` |  |  |  |
| 48 | `INLEND.ORM.TRANSMIT.INDICATOR` | `InlendIdpmsOrm_TransmitIndicator` | TField |  | Drop-down field. A Valid record from INLEND.TRANSMIT.INDICATOR. System updated field |
| 49 | `INLEND.ORM.ORM.ADJUSTMENT.REQD` | `InlendIdpmsOrm_OrmAdjustmentReqd` | TField |  | indicates whether adjustment is required for the Orm |
| 50 | `INLEND.ORM.DOE.ORM.REQD` | `InlendIdpmsOrm_DoeOrmReqd` | TField |  | indicates whether DOE is required for the Orm |
| 51 | `INLEND.ORM.INTERFACE.ERROR.RESPONSE` | `InlendIdpmsOrm_InterfaceErrorResponse` | TField |  | Record status as received from IDPMS. Should be vetted against INLEND.IMPORT.ERROR.CODES. System updated field |
| 52 | `INLEND.ORM.OVERRIDE` | `InlendIdpmsOrm_Override` |  |  |  |
| 53 | `INLEND.ORM.RECORD.STATUS` | `InlendIdpmsOrm_RecordStatus` | String |  |  |
| 54 | `INLEND.ORM.CURR.NO` | `InlendIdpmsOrm_CurrNo` | String |  |  |
| 55 | `INLEND.ORM.INPUTTER` | `InlendIdpmsOrm_Inputter` |  |  |  |
| 56 | `INLEND.ORM.DATE.TIME` | `InlendIdpmsOrm_DateTime` |  |  |  |
| 57 | `INLEND.ORM.AUTHORISER` | `InlendIdpmsOrm_Authoriser` | String |  |  |
| 58 | `INLEND.ORM.CO.CODE` | `InlendIdpmsOrm_CoCode` | String |  |  |
| 59 | `INLEND.ORM.DEPT.CODE` | `InlendIdpmsOrm_DeptCode` | String |  |  |
| 60 | `INLEND.ORM.AUDITOR.CODE` | `InlendIdpmsOrm_AuditorCode` | String |  |  |
| 61 | `INLEND.ORM.AUDIT.DATE.TIME` | `InlendIdpmsOrm_AuditDateTime` | String |  |  |
| 62 | `INLEND.ORM.ORA.STATUS` | `InlendIdpmsOrm_OraStatus` |  |  |  |
| 63 | `INLEND.ORM.INV.CANCEL.IND` | `InlendIdpmsOrm_InvCancelInd` |  |  |  |
| 64 | `INLEND.ORM.ORM.PROCESS.NAME` | `InlendIdpmsOrm_OrmProcessName` | TField |  | Indicates the Process. A Valid record from INLEND.IDPMS.ORM.PROCESS.NAME. |
