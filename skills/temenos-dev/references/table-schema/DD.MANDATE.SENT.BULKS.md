# DD.MANDATE.SENT.BULKS — Table Schema

> Source: `INSERTS/I_F.DD.MANDATE.SENT.BULKS` in `DD_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DD.MSB.COMPANY.ID` | `DdMandateSentBulks_CompanyId` | TField |  | The Transact Company for which the file is sent. |
| 2 | `DD.MSB.RECEIVED.FILE.ID` | `DdMandateSentBulks_ReceivedFileId` | TField |  | The File ID from DD.MANDATES.RECEIVED.FILES. |
| 3 | `DD.MSB.RECEIVED.BULK.ID` | `DdMandateSentBulks_ReceivedBulkId` | TField |  | The id of DD Mandate Received Bulks corresponding to the file in which the request has been received, allocated by Transact. |
| 4 | `DD.MSB.FILE.REFERENCE` | `DdMandateSentBulks_FileReference` | TField |  | The reference of the outward bulk in which the message is sent to the central mandate service. |
| 5 | `DD.MSB.BULK.REFERENCE` | `DdMandateSentBulks_BulkReference` | TField |  | The reference assigned to the Bulk. |
| 6 | `DD.MSB.BULK.TYPE` | `DdMandateSentBulks_BulkType` | TField |  | The Bulk File Type pain.009, pain.010, pain.011. |
| 7 | `DD.MSB.INSTG.AGENT.BIC` | `DdMandateSentBulks_InstgAgentBic` | TField |  | Sender of the bulk. |
| 8 | `DD.MSB.INSTD.AGENT.BIC` | `DdMandateSentBulks_InstdAgentBic` | TField |  | Receiver of the Bulk. |
| 9 | `DD.MSB.NO.OF.TXNS` | `DdMandateSentBulks_NoOfTxns` | TField |  | Number of Transactions in the bulk. |
| 10 | `DD.MSB.CREATE.DATE.TIME` | `DdMandateSentBulks_CreateDateTime` |  |  |  |
| 11 | `DD.MSB.PROCESSED.DATE` | `DdMandateSentBulks_ProcessedDate` | TField |  |  |
| 12 | `DD.MSB.STATUS` | `DdMandateSentBulks_Status` | TField |  | The status of the batch processing: NEW, PROCESSED, SENT, COMPLETED, ERROR, ACCREJ. |
| 13 | `DD.MSB.STATUS.CODE` | `DdMandateSentBulks_StatusCode` | TField |  | The Status code. |
| 14 | `DD.MSB.ERROR.REASON` | `DdMandateSentBulks_ErrorReason` | TField |  | Updated during subsequent steps of the inbound process when the file is Rejected. |
| 15 | `DD.MSB.ACCEPTANCE.STATUS` | `DdMandateSentBulks_AcceptanceStatus` | TField |  | Acceptance Status can be ACCEPTED or REJECTED. For outward acceptance confirmations only. |
| 16 | `DD.MSB.ACCEPTANCE.RSN.CODE` | `DdMandateSentBulks_AcceptanceRsnCode` | TField |  | For acceptance confirmations only. Indicates the success or reason code for the original request. |
| 17 | `DD.MSB.FILE.NAME` | `DdMandateSentBulks_FileName` | TField |  | The name of the sent file. |
| 18 | `DD.MSB.RESERVED.9` | `DdMandateSentBulks_Reserved9` | TField |  |  |
| 19 | `DD.MSB.RESERVED.8` | `DdMandateSentBulks_Reserved8` | TField |  |  |
| 20 | `DD.MSB.RESERVED.7` | `DdMandateSentBulks_Reserved7` | TField |  |  |
| 21 | `DD.MSB.RESERVED.6` | `DdMandateSentBulks_Reserved6` | TField |  |  |
| 22 | `DD.MSB.RESERVED.5` | `DdMandateSentBulks_Reserved5` | TField |  |  |
| 23 | `DD.MSB.RESERVED.4` | `DdMandateSentBulks_Reserved4` | TField |  |  |
| 24 | `DD.MSB.RESERVED.3` | `DdMandateSentBulks_Reserved3` | TField |  |  |
| 25 | `DD.MSB.RESERVED.2` | `DdMandateSentBulks_Reserved2` | TField |  |  |
| 26 | `DD.MSB.RESERVED.1` | `DdMandateSentBulks_Reserved1` | TField |  |  |
| 27 | `DD.MSB.LOCAL.REF` | `DdMandateSentBulks_LocalRef` |  |  |  |
| 28 | `DD.MSB.OVERRIDE` | `DdMandateSentBulks_Override` |  |  |  |
| 29 | `DD.MSB.RECORD.STATUS` | `DdMandateSentBulks_RecordStatus` | String |  |  |
| 30 | `DD.MSB.CURR.NO` | `DdMandateSentBulks_CurrNo` | String |  |  |
| 31 | `DD.MSB.INPUTTER` | `DdMandateSentBulks_Inputter` |  |  |  |
| 32 | `DD.MSB.DATE.TIME` | `DdMandateSentBulks_DateTime` |  |  |  |
| 33 | `DD.MSB.AUTHORISER` | `DdMandateSentBulks_Authoriser` | String |  |  |
| 34 | `DD.MSB.CO.CODE` | `DdMandateSentBulks_CoCode` | String |  |  |
| 35 | `DD.MSB.DEPT.CODE` | `DdMandateSentBulks_DeptCode` | String |  |  |
| 36 | `DD.MSB.AUDITOR.CODE` | `DdMandateSentBulks_AuditorCode` | String |  |  |
| 37 | `DD.MSB.AUDIT.DATE.TIME` | `DdMandateSentBulks_AuditDateTime` | String |  |  |
