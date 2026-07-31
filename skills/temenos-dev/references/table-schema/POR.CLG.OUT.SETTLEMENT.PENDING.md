# POR.CLG.OUT.SETTLEMENT.PENDING — Table Schema

> Source: `INSERTS/I_F.POR.CLG.OUT.SETTLEMENT.PENDING` in `PP_OutwardMappingFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCSP.ClearingID` | `PorClgOutSettlementPending_Clearingid` | TField |  |  |
| 2 | `PPCSP.FileSendersReference` | `PorClgOutSettlementPending_Filesendersreference` | TField |  |  |
| 3 | `PPCSP.FileReferenceOutgoing` | `PorClgOutSettlementPending_Filereferenceoutgoing` | TField |  |  |
| 4 | `PPCSP.OriginatingSource` | `PorClgOutSettlementPending_Originatingsource` | TField |  |  |
| 5 | `PPCSP.OriginatingChannel` | `PorClgOutSettlementPending_Originatingchannel` | TField |  |  |
| 6 | `PPCSP.IncomingMessageType` | `PorClgOutSettlementPending_Incomingmessagetype` | TField |  |  |
| 7 | `PPCSP.ClearingTransactionType` | `PorClgOutSettlementPending_Clearingtransactiontype` | TField |  |  |
| 8 | `PPCSP.TransactionAmount` | `PorClgOutSettlementPending_Transactionamount` | TField |  |  |
| 9 | `PPCSP.TransactionCurrencyCode` | `PorClgOutSettlementPending_Transactioncurrencycode` | TField |  |  |
| 10 | `PPCSP.SettlementID` | `PorClgOutSettlementPending_Settlementid` | TField |  |  |
| 11 | `PPCSP.NumberOfChildren` | `PorClgOutSettlementPending_Numberofchildren` | TField |  |  |
| 12 | `PPCSP.CreditAccountCompany` | `PorClgOutSettlementPending_Creditaccountcompany` | TField |  |  |
| 13 | `PPCSP.CreditAccountNumber` | `PorClgOutSettlementPending_Creditaccountnumber` | TField |  |  |
| 14 | `PPCSP.CreditAccountCurrency` | `PorClgOutSettlementPending_Creditaccountcurrency` | TField |  |  |
| 15 | `PPCSP.DebitAccountCompany` | `PorClgOutSettlementPending_Debitaccountcompany` | TField |  |  |
| 16 | `PPCSP.DebitAccountNumber` | `PorClgOutSettlementPending_Debitaccountnumber` | TField |  |  |
| 17 | `PPCSP.DebitAccountCurrency` | `PorClgOutSettlementPending_Debitaccountcurrency` | TField |  |  |
| 18 | `PPCSP.RejectedAmount` | `PorClgOutSettlementPending_Rejectedamount` |  |  |  |
| 19 | `PPCSP.FTNumber` | `PorClgOutSettlementPending_Ftnumber` |  |  |  |
| 20 | `PPCSP.SettlementDate` | `PorClgOutSettlementPending_Settlementdate` | TField |  |  |
| 21 | `PPCSP.SettlementFlag` | `PorClgOutSettlementPending_Settlementflag` | TField |  |  |
