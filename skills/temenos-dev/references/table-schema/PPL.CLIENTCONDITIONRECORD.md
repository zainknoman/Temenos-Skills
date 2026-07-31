# PPL.CLIENTCONDITIONRECORD — Table Schema

> Source: `INSERTS/I_F.PPL.CLIENTCONDITIONRECORD` in `PP_ClientConditionsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCR.ClientConditionsID` | `PplClientconditionrecord_Clientconditionsid` |  |  |  |
| 2 | `PPCR.CompanyID` | `PplClientconditionrecord_Companyid` |  |  |  |
| 3 | `PPCR.ClientConditionProduct` | `PplClientconditionrecord_Clientconditionproduct` |  |  |  |
| 4 | `PPCR.SourceProduct` | `PplClientconditionrecord_Sourceproduct` |  |  |  |
| 5 | `PPCR.BusinessLine` | `PplClientconditionrecord_Businessline` |  |  |  |
| 6 | `PPCR.ClientID` | `PplClientconditionrecord_Clientid` |  |  |  |
| 7 | `PPCR.AccountCompanyID` | `PplClientconditionrecord_Accountcompanyid` |  |  |  |
| 8 | `PPCR.AccountNumber` | `PplClientconditionrecord_Accountnumber` |  |  |  |
| 9 | `PPCR.AccountCurrency` | `PplClientconditionrecord_Accountcurrency` |  |  |  |
| 10 | `PPCR.EndDateClientConditionRecord` | `PplClientconditionrecord_Enddateclientconditionrecord` |  |  |  |
| 11 | `PPCR.LanguageID` | `PplClientconditionrecord_Languageid` |  |  |  |
| 12 | `PPCR.DrStatementFormat` | `PplClientconditionrecord_Drstatementformat` |  |  |  |
| 13 | `PPCR.CRStatementFormat` | `PplClientconditionrecord_Crstatementformat` |  |  |  |
| 14 | `PPCR.BillingIndicator` | `PplClientconditionrecord_Billingindicator` |  |  |  |
| 15 | `PPCR.ChargePostingSeparately` | `PplClientconditionrecord_Chargepostingseparately` |  |  |  |
| 16 | `PPCR.ChargePostingDetail` | `PplClientconditionrecord_Chargepostingdetail` |  |  |  |
| 17 | `PPCR.VatPrincipal` | `PplClientconditionrecord_Vatprincipal` |  |  |  |
| 18 | `PPCR.VATOnCharge` | `PplClientconditionrecord_Vatoncharge` |  |  |  |
| 19 | `PPCR.NonSTPIndicator` | `PplClientconditionrecord_Nonstpindicator` |  |  |  |
| 20 | `PPCR.FXNonSTPIndicator` | `PplClientconditionrecord_Fxnonstpindicator` |  |  |  |
| 21 | `PPCR.FXNonSTPAmount` | `PplClientconditionrecord_Fxnonstpamount` |  |  |  |
| 22 | `PPCR.DebitSpecialInstructions` | `PplClientconditionrecord_Debitspecialinstructions` |  |  |  |
| 23 | `PPCR.CreditSpecialInstructions` | `PplClientconditionrecord_Creditspecialinstructions` |  |  |  |
| 24 | `PPCR.AccountSubstitution` | `PplClientconditionrecord_Accountsubstitution` |  |  |  |
| 25 | `PPCR.ReleaseTime` | `PplClientconditionrecord_Releasetime` |  |  |  |
| 26 | `PPCR.DebitFloat` | `PplClientconditionrecord_Debitfloat` |  |  |  |
| 27 | `PPCR.CreditFloat` | `PplClientconditionrecord_Creditfloat` |  |  |  |
| 28 | `PPCR.CCValidityStartDate` | `PplClientconditionrecord_Ccvaliditystartdate` |  |  |  |
| 29 | `PPCR.CCValidityEndDate` | `PplClientconditionrecord_Ccvalidityenddate` |  |  |  |
| 30 | `PPCR.RACClientConditionRecord` | `PplClientconditionrecord_Racclientconditionrecord` |  |  |  |
| 31 | `PPCR.RSCClientConditionRecord` | `PplClientconditionrecord_Rscclientconditionrecord` |  |  |  |
| 32 | `PPCR.EntryUserID` | `PplClientconditionrecord_Entryuserid` |  |  |  |
| 33 | `PPCR.EntryDateTime` | `PplClientconditionrecord_Entrydatetime` |  |  |  |
| 34 | `PPCR.ApproverUserID` | `PplClientconditionrecord_Approveruserid` |  |  |  |
| 35 | `PPCR.ApprovedDateTime` | `PplClientconditionrecord_Approveddatetime` |  |  |  |
| 36 | `PPCR.ThresholdAmount` | `PplClientconditionrecord_Thresholdamount` |  |  |  |
| 37 | `PPCR.BatchACKNACKIndicator` | `PplClientconditionrecord_Batchacknackindicator` |  |  |  |
| 38 | `PPCR.TranNACKIndicator` | `PplClientconditionrecord_Trannackindicator` |  |  |  |
