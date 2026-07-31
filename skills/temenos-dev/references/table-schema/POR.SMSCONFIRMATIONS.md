# POR.SMSCONFIRMATIONS — Table Schema

> Source: `INSERTS/I_F.POR.SMSCONFIRMATIONS` in `PP_ConfirmationsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPSM.CompanyID` | `PorSmsconfirmations_Companyid` |  |  |  |
| 2 | `PPPSM.FTNumber` | `PorSmsconfirmations_Ftnumber` |  |  |  |
| 3 | `PPPSM.AdviceNumber` | `PorSmsconfirmations_Advicenumber` |  |  |  |
| 4 | `PPPSM.SequenceNumber` | `PorSmsconfirmations_Sequencenumber` |  |  |  |
| 5 | `PPPSM.PhoneNumber` | `PorSmsconfirmations_Phonenumber` |  |  |  |
| 6 | `PPPSM.AdviceType` | `PorSmsconfirmations_Advicetype` |  |  |  |
| 7 | `PPPSM.DebitCreditAdvice` | `PorSmsconfirmations_Debitcreditadvice` |  |  |  |
| 8 | `PPPSM.ProductName` | `PorSmsconfirmations_Productname` |  |  |  |
| 9 | `PPPSM.ProcessingDate` | `PorSmsconfirmations_Processingdate` |  |  |  |
| 10 | `PPPSM.TransactionAmount` | `PorSmsconfirmations_Transactionamount` |  |  |  |
| 11 | `PPPSM.TransactionCurrencyCode` | `PorSmsconfirmations_Transactioncurrencycode` |  |  |  |
| 12 | `PPPSM.DebitClientID` | `PorSmsconfirmations_Debitclientid` |  |  |  |
| 13 | `PPPSM.DebitMainAccount` | `PorSmsconfirmations_Debitmainaccount` |  |  |  |
| 14 | `PPPSM.DebitValueDate` | `PorSmsconfirmations_Debitvaluedate` |  |  |  |
| 15 | `PPPSM.OrderingPartyAccountNumber` | `PorSmsconfirmations_Orderingpartyaccountnumber` |  |  |  |
| 16 | `PPPSM.OrderingPartyName` | `PorSmsconfirmations_Orderingpartyname` |  |  |  |
| 17 | `PPPSM.CreditClientID` | `PorSmsconfirmations_Creditclientid` |  |  |  |
| 18 | `PPPSM.CreditMainAccount` | `PorSmsconfirmations_Creditmainaccount` |  |  |  |
| 19 | `PPPSM.CreditValueDate` | `PorSmsconfirmations_Creditvaluedate` |  |  |  |
| 20 | `PPPSM.BeneficiaryAccountNumber` | `PorSmsconfirmations_Beneficiaryaccountnumber` |  |  |  |
| 21 | `PPPSM.BeneficiaryName` | `PorSmsconfirmations_Beneficiaryname` |  |  |  |
| 22 | `PPPSM.SendersReferenceNumber` | `PorSmsconfirmations_Sendersreferencenumber` |  |  |  |
| 23 | `PPPSM.AlertSent` | `PorSmsconfirmations_Alertsent` |  |  |  |
| 24 | `PPPSM.SMSReversalIndicator` | `PorSmsconfirmations_Smsreversalindicator` |  |  |  |
| 25 | `PPPSM.ErrorReasonCodeDesc` | `PorSmsconfirmations_Errorreasoncodedesc` |  |  |  |
