# SAPWPS.FILE.RECORD — Table Schema

> Source: `INSERTS/I_F.SAPWPS.FILE.RECORD` in `SAPWPS_WagesProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SAPWPS.RECORD.TYPE` | `SapwpsFileRecord_RecordType` | TField |  | Record type indicates whether it is a header, detailed, control record. Sample values are HDR, DTL,SCR, EDR, etc |
| 2 | `SAPWPS.EMPLOYEE.ID` | `SapwpsFileRecord_EmployeeId` | TField |  | EmployeeID provided by the organisation / MoL |
| 3 | `SAPWPS.AGENT.CODE` | `SapwpsFileRecord_AgentCode` | TField |  | Agent code / Bank code provided by the MoL / Regulatory |
| 4 | `SAPWPS.EMPLOYEE.ACCOUNT` | `SapwpsFileRecord_EmployeeAccount` | TField |  | Account of the employee with the Agent / Bank |
| 5 | `SAPWPS.PAY.START.DATE` | `SapwpsFileRecord_PayStartDate` | TField |  | Start date for the Salary payment |
| 6 | `SAPWPS.PAY.END.DATE` | `SapwpsFileRecord_PayEndDate` | TField |  | End date for the Salary payment |
| 7 | `SAPWPS.NO.OF.DAYS` | `SapwpsFileRecord_NoOfDays` | TField |  | Number of days in a calendar month |
| 8 | `SAPWPS.FIXED.SALARY` | `SapwpsFileRecord_FixedSalary` |  |  |  |
| 9 | `SAPWPS.VARIABLE.SALARY` | `SapwpsFileRecord_VariableSalary` |  |  |  |
| 10 | `SAPWPS.LEAVE.DAYS` | `SapwpsFileRecord_LeaveDays` | TField |  | Number of days the employee availed leave in a month |
| 11 | `SAPWPS.RETURNED.AMOUNT` | `SapwpsFileRecord_ReturnedAmount` | TField |  | Amount returned to the employer by the bank / Agent |
| 12 | `SAPWPS.RETURN.REASON.CODE` | `SapwpsFileRecord_ReturnReasonCode` | TField |  | Reason code for returning the amount to the employer |
| 13 | `SAPWPS.RETURN.DESCRIPTION` | `SapwpsFileRecord_ReturnDescription` | TField |  | Description for returning the amount to the employer |
| 14 | `SAPWPS.FILE.NAME` | `SapwpsFileRecord_FileName` | TField |  | Name of the input file in which the detailed records are present. Can also be used to store the Reference file names for various files processing |
| 15 | `SAPWPS.TOTAL.RETURNED.AMOUNT` | `SapwpsFileRecord_TotalReturnedAmount` | TField |  | Total amount returned to the bank by WPS |
| 16 | `SAPWPS.PAYMENT.REFERENCE` | `SapwpsFileRecord_PaymentReference` | TField |  | Remarks provided for the payment |
| 17 | `SAPWPS.OE.REPAIR.REASON` | `SapwpsFileRecord_OeRepairReason` | TField |  | Error code or description provided by the Payments application for a particular transaction |
| 18 | `SAPWPS.REFUND.REQUESTED.AMOUNT` | `SapwpsFileRecord_RefundRequestedAmount` | TField |  | Amount requested for refund by the bank to WPS |
| 19 | `SAPWPS.REFUND.STATUS` | `SapwpsFileRecord_RefundStatus` | TField |  | Status of the refund request initiated by the bank |
| 20 | `SAPWPS.REASON.CODE` | `SapwpsFileRecord_ReasonCode` | TField |  | Rejected reason code provided by WPS for a refund request |
| 21 | `SAPWPS.AGENT.BALANCE` | `SapwpsFileRecord_AgentBalance` | TField |  | Balance that the Agents holds with the account in WPS |
| 22 | `SAPWPS.REFUND.REQUEST.CODE` | `SapwpsFileRecord_RefundRequestCode` | TField |  | Refund request code to be sent in the RFR file |
| 23 | `SAPWPS.NARRATIVE` | `SapwpsFileRecord_Narrative` |  |  |  |
| 24 | `SAPWPS.REFERENCE.FILE.NAME` | `SapwpsFileRecord_ReferenceFileName` | TField |  | Reference file name for validating the files |
| 25 | `SAPWPS.TOTAL.FIXED.SALARY` | `SapwpsFileRecord_TotalFixedSalary` | TField |  | Total fixed salary mentioned in the Payment Information file |
| 26 | `SAPWPS.TOTAL.VARIABLE.SALARY` | `SapwpsFileRecord_TotalVariableSalary` | TField |  | Total Variable salary mentioned in the Payment Information file |
| 27 | `SAPWPS.TOTAL.SALARY` | `SapwpsFileRecord_TotalSalary` | TField |  | Total salary mentioned in the Payment Information file |
| 28 | `SAPWPS.TRANSACTION.DATE` | `SapwpsFileRecord_TransactionDate` | TField |  | Date on which salary transaction made on the employee account |
| 29 | `SAPWPS.DESTINATION.COUNTRY` | `SapwpsFileRecord_DestinationCountry` | TField |  | Beneficiary country code incase of the foreign remittance |
| 30 | `SAPWPS.REMITTANCE.AMOUNT` | `SapwpsFileRecord_RemittanceAmount` | TField |  | Amount remitted to the employee account where the account is out of the country |
| 31 | `SAPWPS.EMPLOYEE.BANK` | `SapwpsFileRecord_EmployeeBank` | TField |  | Bank code of employee account |
| 32 | `SAPWPS.LOCAL.REF` | `SapwpsFileRecord_LocalRef` |  |  |  |
| 33 | `SAPWPS.OVERRIDE` | `SapwpsFileRecord_Override` |  |  |  |
| 34 | `SAPWPS.RECORD.STATUS` | `SapwpsFileRecord_RecordStatus` | String |  |  |
| 35 | `SAPWPS.CURR.NO` | `SapwpsFileRecord_CurrNo` | String |  |  |
| 36 | `SAPWPS.INPUTTER` | `SapwpsFileRecord_Inputter` |  |  |  |
| 37 | `SAPWPS.DATE.TIME` | `SapwpsFileRecord_DateTime` |  |  |  |
| 38 | `SAPWPS.AUTHORISER` | `SapwpsFileRecord_Authoriser` | String |  |  |
| 39 | `SAPWPS.CO.CODE` | `SapwpsFileRecord_CoCode` | String |  |  |
| 40 | `SAPWPS.DEPT.CODE` | `SapwpsFileRecord_DeptCode` | String |  |  |
| 41 | `SAPWPS.AUDITOR.CODE` | `SapwpsFileRecord_AuditorCode` | String |  |  |
| 42 | `SAPWPS.AUDIT.DATE.TIME` | `SapwpsFileRecord_AuditDateTime` | String |  |  |
