# PPT.CLEARINGSETTING — Table Schema

> Source: `INSERTS/I_F.PPT.CLEARINGSETTING` in `PP_LocalClearingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCGS.CompanyID` | `PptClearingsetting_Companyid` |  |  |  |
| 2 | `PPCGS.ClearingID` | `PptClearingsetting_Clearingid` |  |  |  |
| 3 | `PPCGS.ClearingCurrency` | `PptClearingsetting_Clearingcurrency` |  |  |  |
| 4 | `PPCGS.ClearingNatureCode` | `PptClearingsetting_Clearingnaturecode` |  |  |  |
| 5 | `PPCGS.MessageDirection` | `PptClearingsetting_Messagedirection` |  |  |  |
| 6 | `PPCGS.MessagePaymentType` | `PptClearingsetting_Messagepaymenttype` |  |  |  |
| 7 | `PPCGS.StartDateClearingSetting` | `PptClearingsetting_Startdateclearingsetting` |  |  |  |
| 8 | `PPCGS.ClearingAccountCompany` | `PptClearingsetting_Clearingaccountcompany` |  |  |  |
| 9 | `PPCGS.ClearingAccountNumber` | `PptClearingsetting_Clearingaccountnumber` |  |  |  |
| 10 | `PPCGS.ClearingAccountCurrency` | `PptClearingsetting_Clearingaccountcurrency` |  |  |  |
| 11 | `PPCGS.SuspenseAccountCompany` | `PptClearingsetting_Suspenseaccountcompany` |  |  |  |
| 12 | `PPCGS.SuspenseAccountNumber` | `PptClearingsetting_Suspenseaccountnumber` |  |  |  |
| 13 | `PPCGS.SuspenseAccountCurrency` | `PptClearingsetting_Suspenseaccountcurrency` |  |  |  |
| 14 | `PPCGS.SettlementBookingIndicator` | `PptClearingsetting_Settlementbookingindicator` |  |  |  |
| 15 | `PPCGS.ManualVerificationIndicator` | `PptClearingsetting_Manualverificationindicator` |  |  |  |
| 16 | `PPCGS.SettlementShift` | `PptClearingsetting_Settlementshift` |  |  |  |
| 17 | `PPCGS.ScheduledForReleaseIndicator` | `PptClearingsetting_Scheduledforreleaseindicator` |  |  |  |
| 18 | `PPCGS.EndDateClearingSetting` | `PptClearingsetting_Enddateclearingsetting` |  |  |  |
| 19 | `PPCGS.RACClearingSetting` | `PptClearingsetting_Racclearingsetting` |  |  |  |
| 20 | `PPCGS.RSCClearingSetting` | `PptClearingsetting_Rscclearingsetting` |  |  |  |
| 21 | `PPCGS.EntryUserID` | `PptClearingsetting_Entryuserid` |  |  |  |
| 22 | `PPCGS.EntryDateTime` | `PptClearingsetting_Entrydatetime` |  |  |  |
| 23 | `PPCGS.ApproverUserID` | `PptClearingsetting_Approveruserid` |  |  |  |
| 24 | `PPCGS.ApprovedDateTime` | `PptClearingsetting_Approveddatetime` |  |  |  |
| 25 | `PPCGS.ValidationRequired` | `PptClearingsetting_Validationrequired` |  |  |  |
| 26 | `PPCGS.AutomatedReturnIndicator` | `PptClearingsetting_Automatedreturnindicator` |  |  |  |
| 27 | `PPCGS.CreateReturnBookingIndicator` | `PptClearingsetting_Createreturnbookingindicator` |  |  |  |
| 28 | `PPCGS.CreateReturnMessageIndicator` | `PptClearingsetting_Createreturnmessageindicator` |  |  |  |
| 29 | `PPCGS.ReturnSuspenseAccountCompany` | `PptClearingsetting_Returnsuspenseaccountcompany` |  |  |  |
| 30 | `PPCGS.ReturnSuspenseAccountNumber` | `PptClearingsetting_Returnsuspenseaccountnumber` |  |  |  |
| 31 | `PPCGS.ReturnSuspenseAccountCurrency` | `PptClearingsetting_Returnsuspenseaccountcurrency` |  |  |  |
| 32 | `PPCGS.CreateRejectMessageIndicator` | `PptClearingsetting_Createrejectmessageindicator` |  |  |  |
| 33 | `PPCGS.AcceptanceDays` | `PptClearingsetting_Acceptancedays` |  |  |  |
| 34 | `PPCGS.ClearingTransactionType` | `PptClearingsetting_Clearingtransactiontype` |  |  |  |
