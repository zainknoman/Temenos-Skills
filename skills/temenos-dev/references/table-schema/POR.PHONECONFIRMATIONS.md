# POR.PHONECONFIRMATIONS — Table Schema

> Source: `INSERTS/I_F.POR.PHONECONFIRMATIONS` in `PP_ConfirmationsService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPPH.CompanyID` | `PorPhoneconfirmations_Companyid` |  |  |  |
| 2 | `PPPPH.FTNumber` | `PorPhoneconfirmations_Ftnumber` |  |  |  |
| 3 | `PPPPH.AdviceNumber` | `PorPhoneconfirmations_Advicenumber` |  |  |  |
| 4 | `PPPPH.SequenceNumber` | `PorPhoneconfirmations_Sequencenumber` |  |  |  |
| 5 | `PPPPH.PhoneNumber` | `PorPhoneconfirmations_Phonenumber` |  |  |  |
| 6 | `PPPPH.OtherDeliveryDetails` | `PorPhoneconfirmations_Otherdeliverydetails` |  |  |  |
| 7 | `PPPPH.OtherInfo` | `PorPhoneconfirmations_Otherinfo` |  |  |  |
| 8 | `PPPPH.TransactionAmount` | `PorPhoneconfirmations_Transactionamount` |  |  |  |
| 9 | `PPPPH.TransactionCurrency` | `PorPhoneconfirmations_Transactioncurrency` |  |  |  |
| 10 | `PPPPH.DebitMainAccountCompanyID` | `PorPhoneconfirmations_Debitmainaccountcompanyid` |  |  |  |
| 11 | `PPPPH.DebitMainAccount` | `PorPhoneconfirmations_Debitmainaccount` |  |  |  |
| 12 | `PPPPH.CreditMainAccountCompanyID` | `PorPhoneconfirmations_Creditmainaccountcompanyid` |  |  |  |
| 13 | `PPPPH.CreditMainAccount` | `PorPhoneconfirmations_Creditmainaccount` |  |  |  |
| 14 | `PPPPH.SendersReferenceNumber` | `PorPhoneconfirmations_Sendersreferencenumber` |  |  |  |
| 15 | `PPPPH.ConfirmationSent` | `PorPhoneconfirmations_Confirmationsent` |  |  |  |
| 16 | `PPPPH.DebitMainAccountCurrencyCode` | `PorPhoneconfirmations_Debitmainaccountcurrencycode` |  |  |  |
| 17 | `PPPPH.CreditMainAccountCurrencyCode` | `PorPhoneconfirmations_Creditmainaccountcurrencycode` |  |  |  |
