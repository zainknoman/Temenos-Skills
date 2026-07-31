# ACSWIT.REROUTED.PAY.INFO — Table Schema

> Source: `INSERTS/I_F.ACSWIT.REROUTED.PAY.INFO` in `ACSWIT_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACSWIT.PAY.DEBTOR.NAME` | `AcswitReroutedPayInfo_DebtorName` | TField |  | Stores customer name of debtor. |
| 2 | `ACSWIT.PAY.CREDITOR.NAME` | `AcswitReroutedPayInfo_CreditorName` | TField |  | Stores customer name of creditor. |
| 3 | `ACSWIT.PAY.NEW.ACCOUNT` | `AcswitReroutedPayInfo_NewAccount` | TField |  | Represents the new IBAN/BBAN of the account holder, as indicated in the switch instruction record belonging tothe account holder. |
| 4 | `ACSWIT.PAY.NEW.BIC` | `AcswitReroutedPayInfo_NewBic` | TField |  | Represents the BIC of the new bank, as indicated in the switch instruction record belonging to the accountholder. |
| 5 | `ACSWIT.PAY.OLD.ACCOUNT` | `AcswitReroutedPayInfo_OldAccount` | TField |  | Represents the old IBAN/BBAN of the account holder, as indicated in the switch instruction record belonging tothe account holder. |
| 6 | `ACSWIT.PAY.OLD.BIC` | `AcswitReroutedPayInfo_OldBic` | TField |  | Represents the BIC of the old bank, as indicated in the switch instruction record belonging to the accountholder. |
| 7 | `ACSWIT.PAY.REMITTANCE.INFO` | `AcswitReroutedPayInfo_RemittanceInfo` |  |  |  |
| 8 | `ACSWIT.PAY.END.TO.END.REF` | `AcswitReroutedPayInfo_EndToEndRef` | TField |  | Holds the end to end id from the payments that have been rerouted as a result of an active switch instruction forthe account. The identifier represents the Originators reference of the credit transfer transactions or the Creditor'sreference of the Direct Debit Transaction. |
| 9 | `ACSWIT.PAY.MANDATE.REF` | `AcswitReroutedPayInfo_MandateRef` | TField |  | Contains direct debit mandate reference. |
| 10 | `ACSWIT.PAY.TRANSACTION.TYPE` | `AcswitReroutedPayInfo_TransactionType` | TField |  | Contains transaction type of payment. For example, CT, DD. |
| 11 | `ACSWIT.PAY.DB.CT.INDICATOR` | `AcswitReroutedPayInfo_DbCtIndicator` | TField |  | Field to indicate whether the account switch applied on the payment ( NEW.ACCOUNT, NEW.BIC, OLD.ACCOUNT andOLD.BIC) was on the debtor account or on the beneficiary account (depending on the type of the paymenttransaction). |
| 12 | `ACSWIT.PAY.INITIATOR.ACCOUNT` | `AcswitReroutedPayInfo_InitiatorAccount` | TField |  | Field stores the account number of the originator. For Credit transfer's, the field holds the IBAN/account of theoriginal debtor and for direct debits, the field holds the IBAN/account of the original creditor. |
| 13 | `ACSWIT.PAY.INITIATOR.BIC` | `AcswitReroutedPayInfo_InitiatorBic` | TField |  | Field stores the BIC of the account belonging to the originator. For Credit transfer's, the field holds the BICof the account belonging to the original debtor and for direct debits the field holds the BIC of the accountbelonging to the original creditor. |
| 14 | `ACSWIT.PAY.RESERVED.07` | `AcswitReroutedPayInfo_Reserved07` | TField |  |  |
| 15 | `ACSWIT.PAY.RESERVED.06` | `AcswitReroutedPayInfo_Reserved06` | TField |  |  |
| 16 | `ACSWIT.PAY.RESERVED.05` | `AcswitReroutedPayInfo_Reserved05` | TField |  |  |
| 17 | `ACSWIT.PAY.RESERVED.04` | `AcswitReroutedPayInfo_Reserved04` | TField |  |  |
| 18 | `ACSWIT.PAY.RESERVED.03` | `AcswitReroutedPayInfo_Reserved03` | TField |  |  |
| 19 | `ACSWIT.PAY.RESERVED.02` | `AcswitReroutedPayInfo_Reserved02` | TField |  |  |
| 20 | `ACSWIT.PAY.RESERVED.01` | `AcswitReroutedPayInfo_Reserved01` | TField |  |  |
