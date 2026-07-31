# DESCTX.SECTRAS.TAX.TRANSACTIONS — Table Schema

> Source: `INSERTS/I_F.DESCTX.SECTRAS.TAX.TRANSACTIONS` in `DESCTX_Taxation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SECTRAS.TXN.SIMULATION.INDICATOR` | `DesctxSectrasTaxTransactions_SimulationIndicator` | TField |  | Indicates whether the Transaction is simulation or not |
| 2 | `SECTRAS.TXN.PRODUCT.LINE` | `DesctxSectrasTaxTransactions_ProductLine` | TField |  | It defines the Product Line of the contract |
| 3 | `SECTRAS.TXN.ACCOUNT.NO` | `DesctxSectrasTaxTransactions_AccountNo` | TField |  | It defines the Account number for which the transaction happened |
| 4 | `SECTRAS.TXN.INTEREST.DATE` | `DesctxSectrasTaxTransactions_InterestDate` | TField |  | It defines the Interest Capitalization date |
| 5 | `SECTRAS.TXN.ADJUSTMENT.DATE` | `DesctxSectrasTaxTransactions_AdjustmentDate` | TField |  | It defines the date in which the adjustment to the transaction happened |
| 6 | `SECTRAS.TXN.CANCELLATION.INDICATOR` | `DesctxSectrasTaxTransactions_CancellationIndicator` | TField |  | Indicates whether the Transaction is cancellation or not |
| 7 | `SECTRAS.TXN.CANCELLATION.DATE` | `DesctxSectrasTaxTransactions_CancellationDate` | TField |  | It defines the date of cancellation of the transaction |
| 8 | `SECTRAS.TXN.INTEREST.AMOUNT` | `DesctxSectrasTaxTransactions_InterestAmount` | TField |  | It defines the Interest Base amount |
| 9 | `SECTRAS.TXN.INTEREST.CURRENCY` | `DesctxSectrasTaxTransactions_InterestCurrency` | TField |  | It defines the transaction currency |
| 10 | `SECTRAS.TXN.CURRENCY.EXCHANGE.RATE` | `DesctxSectrasTaxTransactions_CurrencyExchangeRate` | TField |  | It specifies the Currency exchange rate used for a foreign currency transaction |
| 11 | `SECTRAS.TXN.STATUS` | `DesctxSectrasTaxTransactions_Status` | TField |  | Indicates the status of the record with the following EB.Lookups 1-Ready To Send 2-Awaiting Acknowledgement 3-Success 4-Success Response 5-Error Response 6-Manually Handled |
| 12 | `SECTRAS.TXN.RETURN.CODE` | `DesctxSectrasTaxTransactions_ReturnCode` | TField |  | Success or Error Code will be updated |
| 13 | `SECTRAS.TXN.CODE.DESCRIPTION` | `DesctxSectrasTaxTransactions_CodeDescription` | TField |  | Defines the detail description of the Return code captured |
| 14 | `SECTRAS.TXN.STMT.ENTRY.ID` | `DesctxSectrasTaxTransactions_StmtEntryId` |  |  |  |
| 15 | `SECTRAS.TXN.BASE.AMT` | `DesctxSectrasTaxTransactions_BaseAmt` | TField |  | It indicates the base amount on which the tax is calculated |
| 16 | `SECTRAS.TXN.TAX.INDICATOR` | `DesctxSectrasTaxTransactions_TaxIndicator` |  |  |  |
| 17 | `SECTRAS.TXN.TAX.AMOUNT` | `DesctxSectrasTaxTransactions_TaxAmount` |  |  |  |
| 18 | `SECTRAS.TXN.LOCAL.REF` | `DesctxSectrasTaxTransactions_LocalRef` |  |  |  |
| 19 | `SECTRAS.TXN.RESERVED.8` | `DesctxSectrasTaxTransactions_Reserved8` | TField |  |  |
| 20 | `SECTRAS.TXN.RESERVED.7` | `DesctxSectrasTaxTransactions_Reserved7` | TField |  |  |
| 21 | `SECTRAS.TXN.RESERVED.6` | `DesctxSectrasTaxTransactions_Reserved6` | TField |  |  |
| 22 | `SECTRAS.TXN.RESERVED.5` | `DesctxSectrasTaxTransactions_Reserved5` | TField |  |  |
| 23 | `SECTRAS.TXN.RESERVED.4` | `DesctxSectrasTaxTransactions_Reserved4` | TField |  |  |
| 24 | `SECTRAS.TXN.RESERVED.3` | `DesctxSectrasTaxTransactions_Reserved3` | TField |  |  |
| 25 | `SECTRAS.TXN.RESERVED.2` | `DesctxSectrasTaxTransactions_Reserved2` | TField |  |  |
| 26 | `SECTRAS.TXN.RESERVED.1` | `DesctxSectrasTaxTransactions_Reserved1` | TField |  |  |
| 27 | `SECTRAS.TXN.OVERRIDE` | `DesctxSectrasTaxTransactions_Override` |  |  |  |
| 28 | `SECTRAS.TXN.RECORD.STATUS` | `DesctxSectrasTaxTransactions_RecordStatus` | String |  |  |
| 29 | `SECTRAS.TXN.CURR.NO` | `DesctxSectrasTaxTransactions_CurrNo` | String |  |  |
| 30 | `SECTRAS.TXN.INPUTTER` | `DesctxSectrasTaxTransactions_Inputter` |  |  |  |
| 31 | `SECTRAS.TXN.DATE.TIME` | `DesctxSectrasTaxTransactions_DateTime` |  |  |  |
| 32 | `SECTRAS.TXN.AUTHORISER` | `DesctxSectrasTaxTransactions_Authoriser` | String |  |  |
| 33 | `SECTRAS.TXN.CO.CODE` | `DesctxSectrasTaxTransactions_CoCode` | String |  |  |
| 34 | `SECTRAS.TXN.DEPT.CODE` | `DesctxSectrasTaxTransactions_DeptCode` | String |  |  |
| 35 | `SECTRAS.TXN.AUDITOR.CODE` | `DesctxSectrasTaxTransactions_AuditorCode` | String |  |  |
| 36 | `SECTRAS.TXN.AUDIT.DATE.TIME` | `DesctxSectrasTaxTransactions_AuditDateTime` | String |  |  |
| 37 | `SECTRAS.TXN.SOURCE` | `DesctxSectrasTaxTransactions_Source` | TField |  | It specifies the which type of source |
| 38 | `SECTRAS.TXN.VERSION.NO` | `DesctxSectrasTaxTransactions_VersionNo` | TField |  | It specifies the VersionNumber of the field |
| 39 | `SECTRAS.TXN.VERSION.NO.EXT` | `DesctxSectrasTaxTransactions_VersionNoExt` | TField |  | It specifies VersionNumberExt of the field |
| 40 | `SECTRAS.TXN.ENTITY.CODE` | `DesctxSectrasTaxTransactions_EntityCode` | TField |  | It specifies the EntityCode of the field |
| 41 | `SECTRAS.TXN.CORR.IND` | `DesctxSectrasTaxTransactions_CorrInd` | TField |  | It specifies the CorrectionIndicator of the field |
| 42 | `SECTRAS.TXN.AMNT.INPUT.IND` | `DesctxSectrasTaxTransactions_AmntInputInd` | TField |  | It specifies the AmountInputInd |
| 43 | `SECTRAS.TXN.WORKFLOW.ENTRY` | `DesctxSectrasTaxTransactions_WorkflowEntry` | TField |  | It specifies the WorkflowEntry of the field |
| 44 | `SECTRAS.TXN.CANC.TRN.REF` | `DesctxSectrasTaxTransactions_CancTrnRef` | TField |  | It specifies the CancelTransactionReference |
| 45 | `SECTRAS.TXN.POST.TRN.REF` | `DesctxSectrasTaxTransactions_PostTrnRef` | TField |  | It specifies the PostTransactionReference |
| 46 | `SECTRAS.TXN.VALUE.DATE` | `DesctxSectrasTaxTransactions_ValueDate` | TField |  | It specifies the ValueDate |
| 47 | `SECTRAS.TXN.FWT.DEDU.AMNT` | `DesctxSectrasTaxTransactions_FwtDeduAmnt` | TField |  | It specifies the FwtDeductionAmount |
| 48 | `SECTRAS.TXN.FWT.CHARG.AMNT` | `DesctxSectrasTaxTransactions_FwtChargAmnt` | TField |  | It specifies the FwtChargeAmount of the field |
| 49 | `SECTRAS.TXN.INTR.PERIOD.FROM` | `DesctxSectrasTaxTransactions_IntrPeriodFrom` | TField |  | It specifies the InterestPeriodFrom |
| 50 | `SECTRAS.TXN.INTR.PERIOD.TO` | `DesctxSectrasTaxTransactions_IntrPeriodTo` | TField |  | It specifies the InterestPeriodTo |
| 51 | `SECTRAS.TXN.ADD.TRN.INFO` | `DesctxSectrasTaxTransactions_AddTrnInfo` | TField |  | It specifies the AdditionalTransactionInformation |
| 52 | `SECTRAS.TXN.MAINT.USER.ID` | `DesctxSectrasTaxTransactions_MaintUserId` | TField |  | It specifies the MaintananceUserId |
| 53 | `SECTRAS.TXN.DETAIL.STATUS` | `DesctxSectrasTaxTransactions_DetailStatus` | TField |  | It specifies the DetailStatus of the field |
