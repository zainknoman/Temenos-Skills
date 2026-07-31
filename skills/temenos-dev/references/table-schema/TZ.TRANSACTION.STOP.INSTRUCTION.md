# TZ.TRANSACTION.STOP.INSTRUCTION — Table Schema

> Source: `INSERTS/I_F.TZ.TRANSACTION.STOP.INSTRUCTION` in `TZ_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TZ.TSI.ACCOUNT` | `TzTransactionStopInstruction_Account` | TField |  | Account on which the Stop Instruction has to be applied. It should be a valid T24 Account Field must have a value if the CUSTOMER.ID field is not defined Entered Account has to be the Account of the Customer entered in CUSTOMER.ID |
| 2 | `TZ.TSI.STOP.CONDITION` | `TzTransactionStopInstruction_StopCondition` | TField |  | This will refer to a Stop Condition record Allowed Values - Valid Record in TZ.TRANSACTION.STOP.CONDITION or Blank If blank the DEFAULT Stop Condition record will be used |
| 3 | `TZ.TSI.TRANSACTION.CHANNEL` | `TzTransactionStopInstruction_TransactionChannel` | TField |  | A valid record in the Transaction Stop Types of the lead company,used to determine if the stop instruction applies to a specific Channel/Payment type If not provided, it means the stop instruction aplies to transactions received via any channel |
| 4 | `TZ.TSI.STOP.INSTR.CHANNEL` | `TzTransactionStopInstruction_StopInstrChannel` | TField |  | The channel through which the Stop Instruction has been received |
| 5 | `TZ.TSI.STOP.REASON` | `TzTransactionStopInstruction_StopReason` | TField |  | The reason for the Stop Instruction to be specified here |
| 6 | `TZ.TSI.ATTRIBUTE.NAME` | `TzTransactionStopInstruction_AttributeName` |  |  |  |
| 7 | `TZ.TSI.OPERAND` | `TzTransactionStopInstruction_Operand` |  |  |  |
| 8 | `TZ.TSI.VALUES` | `TzTransactionStopInstruction_Values` |  |  |  |
| 9 | `TZ.TSI.CHECK.ISSUE.DATE` | `TzTransactionStopInstruction_CheckIssueDate` | TField |  | Will allow the bank to capture the issue date of the check which is in scope of Stop Instruction |
| 10 | `TZ.TSI.REPLACE.CHECK.NUMBER` | `TzTransactionStopInstruction_ReplaceCheckNumber` | TField |  | Will allow the bank to capture a replacement Check number |
| 11 | `TZ.TSI.REPLACE.CHECK.ISSUE.DATE` | `TzTransactionStopInstruction_ReplaceCheckIssueDate` | TField |  | Will allow the bank to capture a replacement Check issue date |
| 12 | `TZ.TSI.EXPIRY.DATE` | `TzTransactionStopInstruction_ExpiryDate` | TField |  | This hold the expiry date of the Transaction Stop Instruction If not entered, then the expiry date is calculated using the default expiry days defined in the Transaction Stop Parameter with respect to the current date If no expiry date is defined in Transaction Stop Parameter then this Transaction Stop Instruction will remain in live forever if expiry date is not input manualy. |
| 13 | `TZ.TSI.CANCEL.INSTRUCTION` | `TzTransactionStopInstruction_CancelInstruction` | TField |  | Will allow the user to cancel an active Transaction Stop Instruction and this will move the Status of the instruction to Cancelled Allowed Values - YES/NO/Blank YES - Moves the Instruction status to Cancelled NO - Moves the cancelled Instruction back to Active |
| 14 | `TZ.TSI.STATUS` | `TzTransactionStopInstruction_Status` | TField |  | This will reflect the status of the Transaction Stop Instruction.Contains values like Active/Cancelled/Expired No Input Field - System Updated |
| 15 | `TZ.TSI.DESCRIPTION` | `TzTransactionStopInstruction_Description` |  |  |  |
| 16 | `TZ.TSI.CREATE.DATE` | `TzTransactionStopInstruction_CreateDate` | TField |  | Date on which Stop Instruction is created No Input Field - System Updated |
| 17 | `TZ.TSI.CANCEL.DATE` | `TzTransactionStopInstruction_CancelDate` | TField |  | Date On which CANCEL.INSTRUCTION was marked to YES No Input Field - System Updated |
| 18 | `TZ.TSI.CUSTOMER.ID` | `TzTransactionStopInstruction_CustomerId` | TField |  | Field to define the Customer Id, so that the Stop Instruction can be defined at Customer level Valid T24 Customer Number |
| 19 | `TZ.TSI.APPLIED.TO` | `TzTransactionStopInstruction_AppliedTo` | TField | No | This field to indicate for next payment only. If this is set, once the instruction is applied for payment, it will be marked as cancelled. Optional Field Allowed Values - Next Payment Only, Null. Default as Null |
| 20 | `TZ.TSI.RESERVED.03` | `TzTransactionStopInstruction_Reserved03` | TField |  |  |
| 21 | `TZ.TSI.RESERVED.02` | `TzTransactionStopInstruction_Reserved02` | TField |  |  |
| 22 | `TZ.TSI.RESERVED.01` | `TzTransactionStopInstruction_Reserved01` | TField |  |  |
| 23 | `TZ.TSI.LOCAL.REF` | `TzTransactionStopInstruction_LocalRef` |  |  |  |
| 24 | `TZ.TSI.OVERRIDE` | `TzTransactionStopInstruction_Override` |  |  |  |
| 25 | `TZ.TSI.RECORD.STATUS` | `TzTransactionStopInstruction_RecordStatus` | String |  |  |
| 26 | `TZ.TSI.CURR.NO` | `TzTransactionStopInstruction_CurrNo` | String |  |  |
| 27 | `TZ.TSI.INPUTTER` | `TzTransactionStopInstruction_Inputter` |  |  |  |
| 28 | `TZ.TSI.DATE.TIME` | `TzTransactionStopInstruction_DateTime` |  |  |  |
| 29 | `TZ.TSI.AUTHORISER` | `TzTransactionStopInstruction_Authoriser` | String |  |  |
| 30 | `TZ.TSI.CO.CODE` | `TzTransactionStopInstruction_CoCode` | String |  |  |
| 31 | `TZ.TSI.DEPT.CODE` | `TzTransactionStopInstruction_DeptCode` | String |  |  |
| 32 | `TZ.TSI.AUDITOR.CODE` | `TzTransactionStopInstruction_AuditorCode` | String |  |  |
| 33 | `TZ.TSI.AUDIT.DATE.TIME` | `TzTransactionStopInstruction_AuditDateTime` | String |  |  |
