# USRETL.STOP.PAYMENT.MATCH — Table Schema

> Source: `INSERTS/I_F.USRETL.STOP.PAYMENT.MATCH` in `USRETL_TransactionStop.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `STP.ACCOUNT` | `UsretlStopPaymentMatch_Account` | TField |  | Account number linked to stop payment instruction |
| 2 | `STP.PROCESS.DATE` | `UsretlStopPaymentMatch_ProcessDate` | TField |  | Date when the search is performed |
| 3 | `STP.START.DATE` | `UsretlStopPaymentMatch_StartDate` | TField |  | Start Date range on which transactions are searched |
| 4 | `STP.END.DATE` | `UsretlStopPaymentMatch_EndDate` | TField |  | End Date range on which transactions are searched |
| 5 | `STP.STATUS` | `UsretlStopPaymentMatch_Status` | TField |  | Status of the analysis process Possible values PENDING, COMPLETED |
| 6 | `STP.STMT.ENTRY.ID` | `UsretlStopPaymentMatch_StmtEntryId` |  |  |  |
| 7 | `STP.MATCHES.FOUND` | `UsretlStopPaymentMatch_MatchesFound` | TField |  | Number of matches found in the period |
| 8 | `STP.RESERVED.9` | `UsretlStopPaymentMatch_Reserved9` |  |  |  |
| 9 | `STP.RESERVED.8` | `UsretlStopPaymentMatch_Reserved8` |  |  |  |
| 10 | `STP.RESERVED.7` | `UsretlStopPaymentMatch_Reserved7` |  |  |  |
| 11 | `STP.RESERVED.6` | `UsretlStopPaymentMatch_Reserved6` |  |  |  |
| 12 | `STP.RESERVED.5` | `UsretlStopPaymentMatch_Reserved5` |  |  |  |
| 13 | `STP.RESERVED.4` | `UsretlStopPaymentMatch_Reserved4` |  |  |  |
| 14 | `STP.RESERVED.3` | `UsretlStopPaymentMatch_Reserved3` |  |  |  |
| 15 | `STP.RESERVED.2` | `UsretlStopPaymentMatch_Reserved2` |  |  |  |
| 16 | `STP.RESERVED.1` | `UsretlStopPaymentMatch_Reserved1` |  |  |  |
| 17 | `STP.LOCAL.REF` | `UsretlStopPaymentMatch_LocalRef` |  |  |  |
