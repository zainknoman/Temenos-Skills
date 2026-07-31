# SAPWPS.FILE.DETAILS — Table Schema

> Source: `INSERTS/I_F.SAPWPS.FILE.DETAILS` in `SAPWPS_WagesProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SAPWPS.RECORD.TYPE` | `SapwpsFileDetails_RecordType` | TField |  | Record type indicates whether it is a header, detailed, control record. Sample values are HDR, DTL,SCR, EDR, etc |
| 2 | `SAPWPS.FILE.STATUS` | `SapwpsFileDetails_FileStatus` | TField |  | This field denotes the status that a input file can have. Possible values areError, Unprocessed, Processed, NAK |
| 3 | `SAPWPS.ACK.ID` | `SapwpsFileDetails_AckId` | TField |  | ACK Id received for an input file sent by the Central Bank/Regulatory authority |
| 4 | `SAPWPS.NAK.ID` | `SapwpsFileDetails_NakId` | TField |  | NAK Id received for an input file sent by the central Bank/Regulatory authority |
| 5 | `SAPWPS.LINE.NUMBER` | `SapwpsFileDetails_LineNumber` |  |  |  |
| 6 | `SAPWPS.ERROR.CODE` | `SapwpsFileDetails_ErrorCode` |  |  |  |
| 7 | `SAPWPS.ERROR.DESCRIPTION` | `SapwpsFileDetails_ErrorDescription` |  |  |  |
| 8 | `SAPWPS.ACFA.ID` | `SapwpsFileDetails_AcfaId` | TField |  | Record ID of the AC.FUNDS.AUTHORISATION application while locking the fund for the wages input file processing |
| 9 | `SAPWPS.TRANSACTION.REFERENCE` | `SapwpsFileDetails_TransactionReference` | TField |  | BNK reference of the transaction which will be used to identify the accounting entries |
| 10 | `SAPWPS.PAYMENT.ORDER.REFERENCE` | `SapwpsFileDetails_PaymentOrderReference` | TField |  | Transaction reference related to the PP.ORDER.ENTRY application |
| 11 | `SAPWPS.FILE.RECEIVED.DATE` | `SapwpsFileDetails_FileReceivedDate` | TField |  | Date on which the input file is received |
| 12 | `SAPWPS.FILE.RECEIVED.TIME` | `SapwpsFileDetails_FileReceivedTime` | TField |  | Time , the input file is received |
| 13 | `SAPWPS.NO.OF.RECORDS` | `SapwpsFileDetails_NoOfRecords` |  |  |  |
| 14 | `SAPWPS.SALARY.MONTH` | `SapwpsFileDetails_SalaryMonth` | TField |  | Month for which the salary file is being processed |
| 15 | `SAPWPS.SALARY.AMOUNT` | `SapwpsFileDetails_SalaryAmount` | TField |  | Total salary amount to be debited from the employer account |
| 16 | `SAPWPS.CURRENCY` | `SapwpsFileDetails_Currency` | TField |  | Currency in which the salary file has to be processed |
| 17 | `SAPWPS.EMPLOYER.ID` | `SapwpsFileDetails_EmployerId` | TField |  | Employer Id provided to the establishment by the MoL / Regulatory |
| 18 | `SAPWPS.EMPLOYER.BANK` | `SapwpsFileDetails_EmployerBank` | TField |  | Bank code of the employer where the account is maintained |
| 19 | `SAPWPS.EMPLOYER.ACCOUNT` | `SapwpsFileDetails_EmployerAccount` | TField |  | Account of the employer |
| 20 | `SAPWPS.REFUND.AMOUNT` | `SapwpsFileDetails_RefundAmount` | TField |  | Total Amount requested for refund process |
| 21 | `SAPWPS.NARRATIVE` | `SapwpsFileDetails_Narrative` | TField |  | Used to record remarks provided by Banks, employers and third parties |
| 22 | `SAPWPS.ACCEPTED.COUNT` | `SapwpsFileDetails_AcceptedCount` | TField |  | Total number of accepted refund request records |
| 23 | `SAPWPS.REJECTED.COUNT` | `SapwpsFileDetails_RejectedCount` | TField |  | Total number of rejected refund request records |
| 24 | `SAPWPS.VALUE.DATE` | `SapwpsFileDetails_ValueDate` | TField |  | Value Date used for crediting the salary amount to the employee |
| 25 | `SAPWPS.PROCESS.DATE` | `SapwpsFileDetails_ProcessDate` | TField |  | Debit date used for debiting the salary amount from the employer |
| 26 | `SAPWPS.TOTAL.FIXED.SALARY` | `SapwpsFileDetails_TotalFixedSalary` | TField |  | Total fixed salary to be processed in case of multiple payment files |
| 27 | `SAPWPS.TOTAL.VARIABLE.SALARY` | `SapwpsFileDetails_TotalVariableSalary` | TField |  | Total variable salary to be processed in case of multiple payment files |
| 28 | `SAPWPS.TOTAL.REFUNDS.CLAIMED` | `SapwpsFileDetails_TotalRefundsClaimed` | TField |  | Total Refund amount for claim |
| 29 | `SAPWPS.LOCAL.REF` | `SapwpsFileDetails_LocalRef` |  |  |  |
| 30 | `SAPWPS.OVERRIDE` | `SapwpsFileDetails_Override` |  |  |  |
| 31 | `SAPWPS.RECORD.STATUS` | `SapwpsFileDetails_RecordStatus` | String |  |  |
| 32 | `SAPWPS.CURR.NO` | `SapwpsFileDetails_CurrNo` | String |  |  |
| 33 | `SAPWPS.INPUTTER` | `SapwpsFileDetails_Inputter` |  |  |  |
| 34 | `SAPWPS.DATE.TIME` | `SapwpsFileDetails_DateTime` |  |  |  |
| 35 | `SAPWPS.AUTHORISER` | `SapwpsFileDetails_Authoriser` | String |  |  |
| 36 | `SAPWPS.CO.CODE` | `SapwpsFileDetails_CoCode` | String |  |  |
| 37 | `SAPWPS.DEPT.CODE` | `SapwpsFileDetails_DeptCode` | String |  |  |
| 38 | `SAPWPS.AUDITOR.CODE` | `SapwpsFileDetails_AuditorCode` | String |  |  |
| 39 | `SAPWPS.AUDIT.DATE.TIME` | `SapwpsFileDetails_AuditDateTime` | String |  |  |
