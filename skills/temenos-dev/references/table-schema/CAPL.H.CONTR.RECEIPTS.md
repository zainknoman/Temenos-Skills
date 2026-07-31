# CAPL.H.CONTR.RECEIPTS — Table Schema

> Source: `INSERTS/I_F.CAPL.H.CONTR.RECEIPTS` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.CON.RCPT.CONTRIBUTOR.ID` | `CaplHContrReceipts_ContributorId` | TField |  | The field holds the contribution id of the customer.Valid record form CUSTOMER table. |
| 2 | `CAPL.CON.RCPT.PORTFOLIO.ID` | `CaplHContrReceipts_PortfolioId` | TField |  | The field holds the portfolio id of the customer.Valid record from SEC.ACC.MASTER table. |
| 3 | `CAPL.CON.RCPT.ANNUITANT.ID` | `CaplHContrReceipts_AnnuitantId` | TField |  | This field is used to denote the annuitant id for the plan.Valid record from CUSTOMER.table. |
| 4 | `CAPL.CON.RCPT.CONTR.YEAR` | `CaplHContrReceipts_ContrYear` | TField |  | This field denotes the year on which the contribution is done.Valie year to be defined here. |
| 5 | `CAPL.CON.RCPT.AMT.FIRST.PERIOD` | `CaplHContrReceipts_AmtFirstPeriod` | TField |  | This field is to define the amount for the first period, where the contribution is done.Valid amount to be defined here. |
| 6 | `CAPL.CON.RCPT.TXN.FIRST.PERIOD` | `CaplHContrReceipts_TxnFirstPeriod` |  |  |  |
| 7 | `CAPL.CON.RCPT.AMT.SECOND.PERIOD` | `CaplHContrReceipts_AmtSecondPeriod` | TField |  | This field is to define the amount for the second period, where the contribution is done.Valid amount to be defined here. |
| 8 | `CAPL.CON.RCPT.TXN.SECOND.PERIOD` | `CaplHContrReceipts_TxnSecondPeriod` |  |  |  |
| 9 | `CAPL.CON.RCPT.RECEIPT.DATE` | `CaplHContrReceipts_ReceiptDate` | TField |  | Field holds th date on which the receipt was generated.Valid date to be defined here. |
| 10 | `CAPL.CON.RCPT.RECEIPT.STATUS` | `CaplHContrReceipts_ReceiptStatus` | TField |  | Radio button field holds the receipt status.Allowed values are Amended/ Cancelled/ Original |
| 11 | `CAPL.CON.RCPT.STATUS.DATE` | `CaplHContrReceipts_StatusDate` | TField |  | This field holds the status date of the receipt generated.Valid date to be defined here. |
| 12 | `CAPL.CON.RCPT.DUPLICATE.DATE` | `CaplHContrReceipts_DuplicateDate` |  |  |  |
| 13 | `CAPL.CON.RCPT.DUPLICATE.USER` | `CaplHContrReceipts_DuplicateUser` |  |  |  |
| 14 | `CAPL.CON.RCPT.DEL.REF` | `CaplHContrReceipts_DelRef` | TField |  | Field used to store the delivery reference of the contribution slip |
| 15 | `CAPL.CON.RCPT.EXCL.CUST.FLAG` | `CaplHContrReceipts_ExclCustFlag` | TField |  | This field is to define whether the cust flag to be excluded or not for the receipt generation.Allowed values are Yes/No |
| 16 | `CAPL.CON.RCPT.BAD.ADDRESS` | `CaplHContrReceipts_BadAddress` | TField |  | Field is to map the bad address to de.address of xml.1 and print.1If the bad address is set to YES, then the return mail in DE.ADDRESS will be updated to Yes.Allowed values are Yes/No |
| 17 | `CAPL.CON.RCPT.RESERVED.7` | `CaplHContrReceipts_Reserved7` |  |  |  |
| 18 | `CAPL.CON.RCPT.RESERVED.6` | `CaplHContrReceipts_Reserved6` |  |  |  |
| 19 | `CAPL.CON.RCPT.RESERVED.5` | `CaplHContrReceipts_Reserved5` |  |  |  |
| 20 | `CAPL.CON.RCPT.RESERVED.4` | `CaplHContrReceipts_Reserved4` |  |  |  |
| 21 | `CAPL.CON.RCPT.RESERVED.3` | `CaplHContrReceipts_Reserved3` |  |  |  |
| 22 | `CAPL.CON.RCPT.RESERVED.2` | `CaplHContrReceipts_Reserved2` |  |  |  |
| 23 | `CAPL.CON.RCPT.LOCAL.REF` | `CaplHContrReceipts_LocalRef` |  |  |  |
| 24 | `CAPL.CON.RCPT.RECORD.STATUS` | `CaplHContrReceipts_RecordStatus` | String |  |  |
| 25 | `CAPL.CON.RCPT.CURR.NO` | `CaplHContrReceipts_CurrNo` | String |  |  |
| 26 | `CAPL.CON.RCPT.INPUTTER` | `CaplHContrReceipts_Inputter` |  |  |  |
| 27 | `CAPL.CON.RCPT.DATE.TIME` | `CaplHContrReceipts_DateTime` |  |  |  |
| 28 | `CAPL.CON.RCPT.AUTHORISER` | `CaplHContrReceipts_Authoriser` | String |  |  |
| 29 | `CAPL.CON.RCPT.CO.CODE` | `CaplHContrReceipts_CoCode` | String |  |  |
| 30 | `CAPL.CON.RCPT.DEPT.CODE` | `CaplHContrReceipts_DeptCode` | String |  |  |
| 31 | `CAPL.CON.RCPT.AUDITOR.CODE` | `CaplHContrReceipts_AuditorCode` | String |  |  |
| 32 | `CAPL.CON.RCPT.AUDIT.DATE.TIME` | `CaplHContrReceipts_AuditDateTime` | String |  |  |
