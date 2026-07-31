# CAPL.H.PAP.DD.DDI — Table Schema

> Source: `INSERTS/I_F.CAPL.H.PAP.DD.DDI` in `CAEFPA_EFTPap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.PAP.DESCRIPTION` | `CaplHPapDdDdi_Description` | TField |  | Field to store the description for which this DD is being created.Free textAllowed upto 35 characters. |
| 2 | `CAPL.PAP.DR.CR.MARKER` | `CaplHPapDdDdi_DrCrMarker` | TField |  | Field to store the Debit or Credit Indicator for the T24 account.If this is set to DR then system will debit T24 account and Credit another financial institution and if this is set to CR then system will do a Credit to T24Allowed inputs : DEBIT/CREDIT |
| 3 | `CAPL.PAP.CUSTOMER.NO` | `CaplHPapDdDdi_CustomerNo` | TField |  | Field which stores the primary customer number whose account is the @ID of this record.Validation : record from CUSTOMER table. |
| 4 | `CAPL.PAP.DES.ACCT.NO.INT` | `CaplHPapDdDdi_DesAcctNoInt` |  |  |  |
| 5 | `CAPL.PAP.DEST.ACCT.NAME` | `CaplHPapDdDdi_DestAcctName` |  |  |  |
| 6 | `CAPL.PAP.FOREIGN.INT.ID` | `CaplHPapDdDdi_ForeignIntId` |  |  |  |
| 7 | `CAPL.PAP.TERMINATION.DATE` | `CaplHPapDdDdi_TerminationDate` |  |  |  |
| 8 | `CAPL.PAP.TERMI.INT.DATE` | `CaplHPapDdDdi_TermiIntDate` |  |  |  |
| 9 | `CAPL.PAP.DES.ACCT.NO.MAT` | `CaplHPapDdDdi_DesAcctNoMat` |  |  |  |
| 10 | `CAPL.PAP.DES.ACT.NAM.MAT` | `CaplHPapDdDdi_DesActNamMat` |  |  |  |
| 11 | `CAPL.PAP.FOREIGN.MAT.ID` | `CaplHPapDdDdi_ForeignMatId` |  |  |  |
| 12 | `CAPL.PAP.TERMI.MAT.DATE` | `CaplHPapDdDdi_TermiMatDate` |  |  |  |
| 13 | `CAPL.PAP.STATUS` | `CaplHPapDdDdi_Status` | TField |  | Purpose of the field to update the status of the payment record, based on which the transactions will be considered for extract reporting.Allowed inputs.ACTIVE, MATURED, PENDING, PROCESS, ERROR, TRANSMITTED.TRANSMITTED - Not in use.ACTIVE - Payment instructions are in active and will be considered for reporting to extract based on the lead days.PENDING - Record will be selected for the reporting N days before the due date and move the status to PROCESSPROCESS - On Value date , reords with PROCESS status will be picked and accounting entries are posted and status moved to PENDING.ERROR - During the extract selection process, due to some failure like insufficient funds will be moved to ERROR |
| 14 | `CAPL.PAP.CREATE.DATE` | `CaplHPapDdDdi_CreateDate` | TField |  | Field is used to store the date on which this record was created.Valid date format field. |
| 15 | `CAPL.PAP.STAND.ALONE.DDI` | `CaplHPapDdDdi_StandAloneDdi` | TField |  | Field is used to indicate the amount for adhoc payments.For All standalone instructions this will be set to YES and for the Scheduled payments coming from Deposits, lending and RRIF this will be set to NO.Allowed inputs - YES/NO |
| 16 | `CAPL.PAP.STAND.ALONE.AMT` | `CaplHPapDdDdi_StandAloneAmt` | TField |  | Purpose of the field is to hold the amount of DD to be generated. This will be an input field only when the field STAND.ALONE.DDI is equal to 'Y'.Value in this field is used to report as the Payment amount in the extract. |
| 17 | `CAPL.PAP.VALUE.DATE` | `CaplHPapDdDdi_ValueDate` | TField |  | Field is used to update the Due date of the Payment.For schedule payments, based on the schedule projector system updates the next payment due date.Validation - valid DATE format field. |
| 18 | `CAPL.PAP.CYCLE.FREQUENCY` | `CaplHPapDdDdi_CycleFrequency` | TField |  | Field is used to update the valid frequency at which the PAP to happen.Udpates based on the payment schedule, for schedule payments.Freqyency type field. |
| 19 | `CAPL.PAP.CPA.TYPE` | `CaplHPapDdDdi_CpaType` | TField |  | Field is used to store the valid CPA types to be sent as part of PAP/ACH files.Validation: Record from CAPL.H.CPA.TYPEeg. 350 |
| 20 | `CAPL.PAP.APPLICATION.REF` | `CaplHPapDdDdi_ApplicationRef` | TField |  | Field is used to store the Application reference from which payments got generated. For Standalone Payments this will be empty.For Scheduled Deposit payments it will be "AD.ACCOUNT" and for RRIF payments it will be "SEC.ACC.MASTER" and for lending it will be "LOAN" |
| 21 | `CAPL.PAP.INT.PAY.AMT` | `CaplHPapDdDdi_IntPayAmt` | TField |  | Field is used to store the Deposit Interest Payment Amount.Applicable for Deposits.Amount in this field is considered for reporting Interest amount for deposits. |
| 22 | `CAPL.PAP.MAT.PAY.AMT` | `CaplHPapDdDdi_MatPayAmt` | TField |  | Field is used to store the Deposit Principal Payment Amount.Applicable for Deposits.Amount in this field is considered for reporting Principal amount for deposits. |
| 23 | `CAPL.PAP.OVER.MSG` | `CaplHPapDdDdi_OverMsg` |  |  |  |
| 24 | `CAPL.PAP.PAP.FOREGN` | `CaplHPapDdDdi_PapForegn` | TField |  | Field is used to store the External Institution Id which will be part of the EFT /PAP extract.Validation: Record from BC.SORT.CODE table. |
| 25 | `CAPL.PAP.CAMB.PAP.ACCT2` | `CaplHPapDdDdi_CambPapAcct2` | TField |  | Field is used to indicate the confirmation of External Account id. This field will be masked. |
| 26 | `CAPL.PAP.CAMB.PAP.ACCT` | `CaplHPapDdDdi_CambPapAcct` | TField |  | Field is used to store the external account ID which is considered for reporting EFT/PAP extract. |
| 27 | `CAPL.PAP.CA.PAP.PURPOSE` | `CaplHPapDdDdi_CaPapPurpose` | TField |  | Field is used to define the purpose of the record being created.Allowed inputs:New Authorization / Amend Existing Authorization / CancellationNew Authorization: Updated when a record is newly created.Amend Existing Authorization: Update when a record is amended and termination date less than today and status NE matured.Cancellation: when the record with status as Matured or reaches termination date. |
| 28 | `CAPL.PAP.CA.PAP.MATDATE` | `CaplHPapDdDdi_CaPapMatdate` | TField |  | Filed to store the Maturity date of the Payment.Valid date format field. |
| 29 | `CAPL.PAP.CAMB.PAD.AGREE` | `CaplHPapDdDdi_CambPadAgree` | TField |  |  |
| 30 | `CAPL.PAP.CAMB.PAP.NAME` | `CaplHPapDdDdi_CambPapName` |  |  |  |
| 31 | `CAPL.PAP.CA.PAP.ID.TYPE` | `CaplHPapDdDdi_CaPapIdType` |  |  |  |
| 32 | `CAPL.PAP.CAMB.PAP.ID.NO` | `CaplHPapDdDdi_CambPapIdNo` |  |  |  |
| 33 | `CAPL.PAP.CAMB.PAP.NAME2` | `CaplHPapDdDdi_CambPapName2` |  |  |  |
| 34 | `CAPL.PAP.CA.PAP.ID.TYPE2` | `CaplHPapDdDdi_CaPapIdType2` |  |  |  |
| 35 | `CAPL.PAP.CAMB.PAP.ID.NO2` | `CaplHPapDdDdi_CambPapIdNo2` |  |  |  |
| 36 | `CAPL.PAP.CAMB.PAP.NAME3` | `CaplHPapDdDdi_CambPapName3` |  |  |  |
| 37 | `CAPL.PAP.CA.PAP.ID.TYPE3` | `CaplHPapDdDdi_CaPapIdType3` |  |  |  |
| 38 | `CAPL.PAP.CAMB.PAP.IDNO3` | `CaplHPapDdDdi_CambPapIdno3` |  |  |  |
| 39 | `CAPL.PAP.CAMB.PAP.AMT` | `CaplHPapDdDdi_CambPapAmt` | TField |  |  |
| 40 | `CAPL.PAP.CAMB.PAP.ACCOUNT` | `CaplHPapDdDdi_CambPapAccount` | TField |  |  |
| 41 | `CAPL.PAP.RECALL` | `CaplHPapDdDdi_Recall` | TField |  | Field is used to indicate the payment to be made for the transactions selected in the extract.If this field is set to "YES" then payment will not be done for the extracted payments in ACH. |
| 42 | `CAPL.PAP.ACCT.ENTRY` | `CaplHPapDdDdi_AcctEntry` | TField |  | Field to indicate whether the accounting to be posted on the value date.Allowed inputs : YES/NOIf this field is YES or blank then system will raise Accounting entries on the Due Date, but if this is set to "NO" then system will not raise accounting entries during Due date |
| 43 | `CAPL.PAP.PROCESS.DATE` | `CaplHPapDdDdi_ProcessDate` | TField |  | Field is used to indicate the date of which extract gets processed.This gets updated during extract process and during Accounting entry process.Accounting entry process happens on the value date.Valid date format field. |
| 44 | `CAPL.PAP.TS.TXN.NO` | `CaplHPapDdDdi_TsTxnNo` | TField |  | This field is used to Indicate Tax Shelter transaction code to be used for Registered Standalone payments.Applicable only for Standalone payments towards Registered Plans.Validation: record from CAPL.PLAN.TXNS |
| 45 | `CAPL.PAP.SUSPEND.FLAG` | `CaplHPapDdDdi_SuspendFlag` | TField |  |  |
| 46 | `CAPL.PAP.SUSPEND.START.DATE` | `CaplHPapDdDdi_SuspendStartDate` | TField |  |  |
| 47 | `CAPL.PAP.SUSPEND.END.DATE` | `CaplHPapDdDdi_SuspendEndDate` | TField |  |  |
| 48 | `CAPL.PAP.LOCAL.REF` | `CaplHPapDdDdi_LocalRef` |  |  |  |
| 49 | `CAPL.PAP.ACCT2.HDN` | `CaplHPapDdDdi_Acct2Hdn` | TField |  | This field is used to store the value of the PAP.ACCT2 fields for validation |
| 50 | `CAPL.PAP.OWN.TRANSFER` | `CaplHPapDdDdi_OwnTransfer` | TField |  |  |
| 51 | `CAPL.PAP.LAST.PAY.DATE` | `CaplHPapDdDdi_LastPayDate` | TField |  |  |
| 52 | `CAPL.PAP.NEXT.PAY.DATE` | `CaplHPapDdDdi_NextPayDate` | TField |  |  |
| 53 | `CAPL.PAP.BENEFICIARY` | `CaplHPapDdDdi_Beneficiary` | TField |  | This field is used to maintain beneficiary information which can then be defaulted in to FUNDS.TRANSFER and STANDING.ORDER thus avoiding having to enter the same information each time a payment is created. |
| 54 | `CAPL.PAP.RESERVED.5` | `CaplHPapDdDdi_Reserved5` | TField |  |  |
| 55 | `CAPL.PAP.RESERVED.6` | `CaplHPapDdDdi_Reserved6` | TField |  |  |
| 56 | `CAPL.PAP.RESERVED.7` | `CaplHPapDdDdi_Reserved7` | TField |  |  |
| 57 | `CAPL.PAP.RESERVED.8` | `CaplHPapDdDdi_Reserved8` | TField |  |  |
| 58 | `CAPL.PAP.RESERVED.9` | `CaplHPapDdDdi_Reserved9` | TField |  |  |
| 59 | `CAPL.PAP.RESERVED.10` | `CaplHPapDdDdi_Reserved10` | TField |  |  |
| 60 | `CAPL.PAP.OVERRIDE` | `CaplHPapDdDdi_Override` |  |  |  |
| 61 | `CAPL.PAP.RECORD.STATUS` | `CaplHPapDdDdi_RecordStatus` | String |  |  |
| 62 | `CAPL.PAP.CURR.NO` | `CaplHPapDdDdi_CurrNo` | String |  |  |
| 63 | `CAPL.PAP.INPUTTER` | `CaplHPapDdDdi_Inputter` |  |  |  |
| 64 | `CAPL.PAP.DATE.TIME` | `CaplHPapDdDdi_DateTime` |  |  |  |
| 65 | `CAPL.PAP.AUTHORISER` | `CaplHPapDdDdi_Authoriser` | String |  |  |
| 66 | `CAPL.PAP.CO.CODE` | `CaplHPapDdDdi_CoCode` | String |  |  |
| 67 | `CAPL.PAP.DEPT.CODE` | `CaplHPapDdDdi_DeptCode` | String |  |  |
| 68 | `CAPL.PAP.AUDITOR.CODE` | `CaplHPapDdDdi_AuditorCode` | String |  |  |
| 69 | `CAPL.PAP.AUDIT.DATE.TIME` | `CaplHPapDdDdi_AuditDateTime` | String |  |  |
