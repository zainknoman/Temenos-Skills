# DD.MANDATE.RECEIVED.BULKS — Table Schema

> Source: `INSERTS/I_F.DD.MANDATE.RECEIVED.BULKS` in `DD_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DD.MRB.COMPANY.ID` | `DdMandateReceivedBulks_CompanyId` | TField |  | The Transact Company for which the bulk is received. |
| 2 | `DD.MRB.FILE.ID` | `DdMandateReceivedBulks_FileId` | TField |  | The File ID from DD.MANDATES.RECEIVED.FILES. |
| 3 | `DD.MRB.FILE.REFERENCE` | `DdMandateReceivedBulks_FileReference` | TField |  | The File Reference from DD.MANDATES.RECEIVED.FILES. |
| 4 | `DD.MRB.BULK.REFERENCE` | `DdMandateReceivedBulks_BulkReference` | TField |  | Bulk Reference of the sender. |
| 5 | `DD.MRB.CREATE.DATE.TIME` | `DdMandateReceivedBulks_CreateDateTime` |  |  |  |
| 6 | `DD.MRB.RECEIVED.DATE` | `DdMandateReceivedBulks_ReceivedDate` | TField |  | The business server date, which will populate when the file is received. It will be used in the archival process of the received files |
| 7 | `DD.MRB.BULK.TYPE` | `DdMandateReceivedBulks_BulkType` | TField |  | The Bulk File Type pain.009, pain.010, pain.011, pain.012S. |
| 8 | `DD.MRB.BULK.TYPE.INDICATOR` | `DdMandateReceivedBulks_BulkTypeIndicator` | TField |  | The Bulk type indicator |
| 9 | `DD.MRB.NO.OF.TXNS` | `DdMandateReceivedBulks_NoOfTxns` | TField |  | Number of Transactions in the bulk. |
| 10 | `DD.MRB.INSTG.AGENT.BIC` | `DdMandateReceivedBulks_InstgAgentBic` | TField |  | Sender of the bulk. |
| 11 | `DD.MRB.INSTD.AGENT.BIC` | `DdMandateReceivedBulks_InstdAgentBic` | TField |  | Receiver of the Bulk. |
| 12 | `DD.MRB.STATUS` | `DdMandateReceivedBulks_Status` | TField |  | The status of the batch processing: RECEIVED, PROCESSED, REJECTED, CONFIRMED. |
| 13 | `DD.MRB.ERROR.CODE` | `DdMandateReceivedBulks_ErrorCode` | TField |  | Updated during subsequent steps of the inbound process when the file is Rejected. |
| 14 | `DD.MRB.ERROR.REASON` | `DdMandateReceivedBulks_ErrorReason` | TField |  | Updated during subsequent steps of the inbound process when the file is Rejected. |
