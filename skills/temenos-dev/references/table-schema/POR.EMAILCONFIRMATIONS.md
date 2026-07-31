# POR.EMAILCONFIRMATIONS — Table Schema

> Source: `INSERTS/I_F.POR.EMAILCONFIRMATIONS` in `PP_ConfirmationsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPEM.CompanyID` | `PorEmailconfirmations_Companyid` |  |  |  |
| 2 | `PPPEM.FTNumber` | `PorEmailconfirmations_Ftnumber` |  |  |  |
| 3 | `PPPEM.AdviceNumber` | `PorEmailconfirmations_Advicenumber` |  |  |  |
| 4 | `PPPEM.SequenceNumber` | `PorEmailconfirmations_Sequencenumber` |  |  |  |
| 5 | `PPPEM.EmailID` | `PorEmailconfirmations_Emailid` |  |  |  |
| 6 | `PPPEM.AdviceType` | `PorEmailconfirmations_Advicetype` |  |  |  |
| 7 | `PPPEM.DebitCreditAdvice` | `PorEmailconfirmations_Debitcreditadvice` |  |  |  |
| 8 | `PPPEM.ProductName` | `PorEmailconfirmations_Productname` |  |  |  |
| 9 | `PPPEM.ProcessingDate` | `PorEmailconfirmations_Processingdate` |  |  |  |
| 10 | `PPPEM.TransactionAmount` | `PorEmailconfirmations_Transactionamount` |  |  |  |
| 11 | `PPPEM.TransactionCurrencyCode` | `PorEmailconfirmations_Transactioncurrencycode` |  |  |  |
| 12 | `PPPEM.DebitClientID` | `PorEmailconfirmations_Debitclientid` |  |  |  |
| 13 | `PPPEM.DebitMainAccount` | `PorEmailconfirmations_Debitmainaccount` |  |  |  |
| 14 | `PPPEM.DebitValueDate` | `PorEmailconfirmations_Debitvaluedate` |  |  |  |
| 15 | `PPPEM.OrderingPartyAccountNumber` | `PorEmailconfirmations_Orderingpartyaccountnumber` |  |  |  |
| 16 | `PPPEM.OrderingPartyName` | `PorEmailconfirmations_Orderingpartyname` |  |  |  |
| 17 | `PPPEM.CreditClientID` | `PorEmailconfirmations_Creditclientid` |  |  |  |
| 18 | `PPPEM.CreditMainAccount` | `PorEmailconfirmations_Creditmainaccount` |  |  |  |
| 19 | `PPPEM.CreditValueDate` | `PorEmailconfirmations_Creditvaluedate` |  |  |  |
| 20 | `PPPEM.BeneficiaryAccountNumber` | `PorEmailconfirmations_Beneficiaryaccountnumber` |  |  |  |
| 21 | `PPPEM.BeneficiaryName` | `PorEmailconfirmations_Beneficiaryname` |  |  |  |
| 22 | `PPPEM.SendersReferenceNumber` | `PorEmailconfirmations_Sendersreferencenumber` |  |  |  |
| 23 | `PPPEM.AlertSent` | `PorEmailconfirmations_Alertsent` |  |  |  |
| 24 | `PPPEM.EmailReversalIndicator` | `PorEmailconfirmations_Emailreversalindicator` |  |  |  |
| 25 | `PPPEM.ErrorReasonCodeDesc` | `PorEmailconfirmations_Errorreasoncodedesc` |  |  |  |
