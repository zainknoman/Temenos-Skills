# ARACCT.EMBARGO.CONCAT — Table Schema

> Source: `INSERTS/I_F.ARACCT.EMBARGO.CONCAT` in `ARACCT_AccountAlias.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARACCT.CUSTOMER` | `AracctEmbargoConcat_Customer` | TField |  | Customer value of the current request |
| 2 | `ARACCT.FILE.AGENT` | `AracctEmbargoConcat_FileAgent` | TField |  | File Agent filed will be updated with the court employee number in the seizure request |
| 3 | `ARACCT.TRADE.DATE` | `AracctEmbargoConcat_TradeDate` | TField |  | Trade date will be updated with the trade date available in the seizure request |
| 4 | `ARACCT.COURT.NO` | `AracctEmbargoConcat_CourtNo` | TField |  | Court Number will be updated with the Court Number in the seizure request |
| 5 | `ARACCT.LOCKED.AMOUNT` | `AracctEmbargoConcat_LockedAmount` | TField |  | Locked Amount will be updated with the locked amount on the account |
| 6 | `ARACCT.TRANSFERRED.AMOUNT` | `AracctEmbargoConcat_TransferredAmount` | TField |  | Transferred Amount will be updated with the seizure amount transferred to the internal suspense account for reference |
| 7 | `ARACCT.TRANSACTION.EXECUTION` | `AracctEmbargoConcat_TransactionExecution` | TField |  | Transaction execution will be updated, once the internal transfer is successful |
| 8 | `ARACCT.TRANSACTION.REFERENCE` | `AracctEmbargoConcat_TransactionReference` | TField |  | Transaction reference will be updated with the transaction reference id, for the transferred made between the customer account and internal suspense account |
| 9 | `ARACCT.RECONCILIED` | `AracctEmbargoConcat_Reconcilied` | TField |  | Reconciled field will be updated, during the reconciliation file processing |
| 10 | `ARACCT.REASON.FOR.SEZIURE.LIFT` | `AracctEmbargoConcat_ReasonForSeziureLift` |  |  |  |
| 11 | `ARACCT.CUIT` | `AracctEmbargoConcat_Cuit` | TField |  | Cuit will be updated with the Cuit in the seizure request |
| 12 | `ARACCT.SEIZURE.NUMBER` | `AracctEmbargoConcat_SeizureNumber` | TField |  | Seizure Number will be updated with the Seizure Number in the seizure request |
| 13 | `ARACCT.RESERVATION.ID` | `AracctEmbargoConcat_ReservationId` | TField |  | Holds the @Id of AC.LOCKED.EVENTS record created for the current account number |
