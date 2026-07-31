# CAPL.H.TX.SLIP.DATA — Table Schema

> Source: `INSERTS/I_F.CAPL.H.TX.SLIP.DATA` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.SLP.DATA.TXN.DATE` | `CaplHTxSlipData_TxnDate` |  |  |  |
| 2 | `CAPL.SLP.DATA.TXN.REF` | `CaplHTxSlipData_TxnRef` |  |  |  |
| 3 | `CAPL.SLP.DATA.FIELD.NAME` | `CaplHTxSlipData_FieldName` |  |  |  |
| 4 | `CAPL.SLP.DATA.FIELD.VALUE` | `CaplHTxSlipData_FieldValue` |  |  |  |
| 5 | `CAPL.SLP.DATA.SPOUSE.SURNAME` | `CaplHTxSlipData_SpouseSurname` |  |  |  |
| 6 | `CAPL.SLP.DATA.SPOUSE.GIVEN.NAME` | `CaplHTxSlipData_SpouseGivenName` |  |  |  |
| 7 | `CAPL.SLP.DATA.SPOUSE.SIN.NO` | `CaplHTxSlipData_SpouseSinNo` |  |  |  |
| 8 | `CAPL.SLP.DATA.TOT.NO.TXNS` | `CaplHTxSlipData_TotNoTxns` | TField |  | This field holds the total number of transaction for the TFSA account.Numeric field value with 5 characters. |
| 9 | `CAPL.SLP.DATA.TOT.TXNS.AMT` | `CaplHTxSlipData_TotTxnsAmt` |  |  |  |
| 10 | `CAPL.SLP.DATA.EOY.PLAN.VALUE` | `CaplHTxSlipData_EoyPlanValue` | TField |  | This field holds the end of year plan value for the account.Valid amount to be defined here. |
| 11 | `CAPL.SLP.DATA.DEATH.PLAN.VALUE` | `CaplHTxSlipData_DeathPlanValue` | TField |  | This field is holds the death plan value, if the customer is deseased.Valid amount to be defined here. |
| 12 | `CAPL.SLP.DATA.OPENED.THIS.YEAR` | `CaplHTxSlipData_OpenedThisYear` | TField |  | This field denotes whether the plan is opened this year or not.Allowed values are Yes/No. |
| 13 | `CAPL.SLP.DATA.CLOSED.THIS.YEAR` | `CaplHTxSlipData_ClosedThisYear` | TField |  | This field denotes whether the plan is closed this year or not.Allowed values are Yes/No. |
| 14 | `CAPL.SLP.DATA.CLOSURE.DATE` | `CaplHTxSlipData_ClosureDate` | TField |  | If the field CLOSED.THIS.YEAR is set to Yes then the close date to be updated in this field.Valid date to be defined here. |
| 15 | `CAPL.SLP.DATA.SLIP.YEAR` | `CaplHTxSlipData_SlipYear` | TField |  | Field is to denote the slip year, in which year the slip is generated.Valid numeric character. |
| 16 | `CAPL.SLP.DATA.SLIP.NUMBER` | `CaplHTxSlipData_SlipNumber` | TField |  | This field holds the slip number for the corresponding slip year.Allowed value 35 alphanumeric character |
| 17 | `CAPL.SLP.DATA.SLIP.STATUS` | `CaplHTxSlipData_SlipStatus` | TField |  | Field holds the slip status. Whether slip is original or amended or cancelled.Allowed valuse are:OriginalAmendedcancel |
| 18 | `CAPL.SLP.DATA.SLIP.ORIG.DATE` | `CaplHTxSlipData_SlipOrigDate` | TField |  | Field is to store the date on which the original slip is printed.Valid date to be defined here. |
| 19 | `CAPL.SLP.DATA.SLIP.AMND.SEQ` | `CaplHTxSlipData_SlipAmndSeq` | TField |  | Filed denotes the slip amend sequence.Allowed values are 4 numeric character. |
| 20 | `CAPL.SLP.DATA.SLIP.AMND.EDATE` | `CaplHTxSlipData_SlipAmndEdate` | TField |  | This field Is used to CAPTURE THE SLIP amendment date, for amended slips This field is not used in the code checked with Ram. |
| 21 | `CAPL.SLP.DATA.SLIP.CANC.FLAG` | `CaplHTxSlipData_SlipCancFlag` | TField |  | Field to capture if the Slip is cancelled. If the slip is cancelled, flag the field to Yes This field is not used in the code checked with Ram. |
| 22 | `CAPL.SLP.DATA.SLIP.CANC.EDATE` | `CaplHTxSlipData_SlipCancEdate` | TField |  | Fiedl to capture cancellation date This field is not used in the code checked with Ram. |
| 23 | `CAPL.SLP.DATA.EXCL.CUST.FLAG` | `CaplHTxSlipData_ExclCustFlag` | TField |  | This field is to define whether the cust flag to be excluded or not for the receipt generation.Allowed values are Yes/No |
| 24 | `CAPL.SLP.DATA.BAD.ADDRESS` | `CaplHTxSlipData_BadAddress` | TField |  | Field is to map the bad address to de.address of xml.1 and print.1If the bad address is set to YES, then the return mail in DE.ADDRESS will be updated to Yes.Allowed values are Yes/No |
| 25 | `CAPL.SLP.DATA.RESERVED.8` | `CaplHTxSlipData_Reserved8` | TField |  |  |
| 26 | `CAPL.SLP.DATA.RESERVED.7` | `CaplHTxSlipData_Reserved7` | TField |  |  |
| 27 | `CAPL.SLP.DATA.RESERVED.6` | `CaplHTxSlipData_Reserved6` | TField |  |  |
| 28 | `CAPL.SLP.DATA.RESERVED.5` | `CaplHTxSlipData_Reserved5` | TField |  |  |
| 29 | `CAPL.SLP.DATA.RESERVED.4` | `CaplHTxSlipData_Reserved4` | TField |  |  |
| 30 | `CAPL.SLP.DATA.RESERVED.3` | `CaplHTxSlipData_Reserved3` | TField |  |  |
| 31 | `CAPL.SLP.DATA.RESERVED.2` | `CaplHTxSlipData_Reserved2` | TField |  |  |
| 32 | `CAPL.SLP.DATA.RESERVED.1` | `CaplHTxSlipData_Reserved1` | TField |  |  |
| 33 | `CAPL.SLP.DATA.LOCAL.REF` | `CaplHTxSlipData_LocalRef` |  |  |  |
| 34 | `CAPL.SLP.DATA.OVERRIDE` | `CaplHTxSlipData_Override` |  |  |  |
| 35 | `CAPL.SLP.DATA.RECORD.STATUS` | `CaplHTxSlipData_RecordStatus` | String |  |  |
| 36 | `CAPL.SLP.DATA.CURR.NO` | `CaplHTxSlipData_CurrNo` | String |  |  |
| 37 | `CAPL.SLP.DATA.INPUTTER` | `CaplHTxSlipData_Inputter` |  |  |  |
| 38 | `CAPL.SLP.DATA.DATE.TIME` | `CaplHTxSlipData_DateTime` |  |  |  |
| 39 | `CAPL.SLP.DATA.AUTHORISER` | `CaplHTxSlipData_Authoriser` | String |  |  |
| 40 | `CAPL.SLP.DATA.CO.CODE` | `CaplHTxSlipData_CoCode` | String |  |  |
| 41 | `CAPL.SLP.DATA.DEPT.CODE` | `CaplHTxSlipData_DeptCode` | String |  |  |
| 42 | `CAPL.SLP.DATA.AUDITOR.CODE` | `CaplHTxSlipData_AuditorCode` | String |  |  |
| 43 | `CAPL.SLP.DATA.AUDIT.DATE.TIME` | `CaplHTxSlipData_AuditDateTime` | String |  |  |
