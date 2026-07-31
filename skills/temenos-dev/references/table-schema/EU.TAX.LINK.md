# EU.TAX.LINK — Table Schema

> Source: `INSERTS/I_F.EU.TAX.LINK` in `ET_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EU.LNK.TXN.BASIS` | `EuTaxLink_TxnBasis` | TField |  | This field holds the transaction basis of the record. Each transaction that involve the mentioned portfolio and security from the key field, are filed under this transaction basis. Valid Transaction Basis are 'FIFO','LIFO' and 'AVERAGE'. |
| 2 | `EU.LNK.TXN.DATE` | `EuTaxLink_TxnDate` |  |  |  |
| 3 | `EU.LNK.TXN.INPUT` | `EuTaxLink_TxnInput` |  |  |  |
| 4 | `EU.LNK.TRA.CODE` | `EuTaxLink_TraCode` |  |  |  |
| 5 | `EU.LNK.DATE.TIME` | `EuTaxLink_DateTime` |  |  |  |
| 6 | `EU.LNK.ACTUAL.NOM` | `EuTaxLink_ActualNom` |  |  |  |
| 7 | `EU.LNK.AVAIL.NOM` | `EuTaxLink_AvailNom` |  |  |  |
| 8 | `EU.LNK.REWORK.FLAG` | `EuTaxLink_ReworkFlag` |  |  |  |
| 9 | `EU.LNK.FIRST.REWORK.TXN` | `EuTaxLink_FirstReworkTxn` | TField |  | This field holds the SECURITY.TRANS key to start the first reworking of transaction that needs to be done that involve the mentioned portfolio and security from the key field. |
| 10 | `EU.LNK.EARLIEST.TXN` | `EuTaxLink_EarliestTxn` | TField |  | This field acts as a pointer for FIFO allocation of nominal which holds the SECURITY.TRANS key to start the allocation that involve the mentioned portfolio and security from the key field. |
| 11 | `EU.LNK.EARLIEST.INS.DT` | `EuTaxLink_EarliestInsDt` | TField |  | This field holds the date on when the earliest transaction was updated in the record for FIFO allocation of nominal that involve the mentioned portfolio and security from the key field. |
| 12 | `EU.LNK.LATEST.TXN` | `EuTaxLink_LatestTxn` | TField |  | This field acts as a pointer for LIFO allocation of nominal which holds the SECURITY.TRANS key to start the allocation that involve the mentioned portfolio and security from the key field. |
| 13 | `EU.LNK.LATEST.INS.DT` | `EuTaxLink_LatestInsDt` | TField |  | This field holds the date on when the latest transaction was updated in the record for LIFO allocation of nominal that involve the mentioned portfolio and security from the key field. |
| 14 | `EU.LNK.LAST.UPDATED.TXN` | `EuTaxLink_LastUpdatedTxn` | TField |  | This field holds the last updated SECURITY.TRANS key in the record for FIFO/LIFO allocation of nominal that involve the mentioned portfolio and security from the key field. |
| 15 | `EU.LNK.LAST.UPD.DATE` | `EuTaxLink_LastUpdDate` | TField |  | This field holds the date on when the SECURITY.TRANS key is last updated in the record for FIFO/LIFO allocation of nominal that involve the mentioned portfolio and security from the key field. |
| 16 | `EU.LNK.TOTAL.NOMINAL` | `EuTaxLink_TotalNominal` | TField |  | This field holds the total nominal of all transactions for AVERAGE transaction basis. |
| 17 | `EU.LNK.TOTAL.COST` | `EuTaxLink_TotalCost` | TField |  | This field holds the total weighted cost of all transactions for AVERAGE transaction basis. |
| 18 | `EU.LNK.AVG.COST` | `EuTaxLink_AvgCost` | TField |  | This field holds the total weighted average cost of all transactions for AVERAGE transaction basis. |
| 19 | `EU.LNK.TOTAL.INT.CTR` | `EuTaxLink_TotalIntCtr` | TField |  | This field holds the total weighted interest counter value of all transactions for AVERAGE transaction basis. |
| 20 | `EU.LNK.INT.CTR` | `EuTaxLink_IntCtr` | TField |  | This field holds the total weighted average interest counter value of all transactions for AVERAGE transaction basis. |
| 21 | `EU.LNK.EU.PURGE.DATE` | `EuTaxLink_EuPurgeDate` | TField |  | This field holds the date on when the last purging of the record happens (i.e.) The transaction details upto this date would be purged from EU.TAX.LINK file and moved to EU.TAX.LINK.PAST file. |
| 22 | `EU.LNK.TOTAL.HPI` | `EuTaxLink_TotalHpi` | TField |  | This field will hold the average total interest of the outstanding nominal. |
| 23 | `EU.LNK.AVG.HPI` | `EuTaxLink_AvgHpi` | TField |  | This field will hold the average interest of the position. |
| 24 | `EU.LNK.TOTAL.DISCOUNT` | `EuTaxLink_TotalDiscount` | TField |  | This field will hold the average total discount of the outstanding nominal. |
| 25 | `EU.LNK.AVG.DISC` | `EuTaxLink_AvgDisc` | TField |  | This field will hold the average discount of the position. |
