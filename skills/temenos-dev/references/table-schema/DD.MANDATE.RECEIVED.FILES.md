# DD.MANDATE.RECEIVED.FILES — Table Schema

> Source: `INSERTS/I_F.DD.MANDATE.RECEIVED.FILES` in `DD_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DD.MRF.COMPANY.ID` | `DdMandateReceivedFiles_CompanyId` | TField |  | The Transact Company for which the file is received. |
| 2 | `DD.MRF.FILE.REFERENCE` | `DdMandateReceivedFiles_FileReference` | TField |  | The Sender File Reference. |
| 3 | `DD.MRF.CREATE.DATE.TIME` | `DdMandateReceivedFiles_CreateDateTime` |  |  |  |
| 4 | `DD.MRF.RECEIVED.DATE` | `DdMandateReceivedFiles_ReceivedDate` | TField |  | The business server date, which will populate when the file is received. It will be used in the archival process of the received files |
| 5 | `DD.MRF.FILE.TYPE` | `DdMandateReceivedFiles_FileType` | TField |  | The type of the file. |
| 6 | `DD.MRF.FILE.SENDER` | `DdMandateReceivedFiles_FileSender` | TField |  | The Sender Institution. |
| 7 | `DD.MRF.FILE.RECEIVER` | `DdMandateReceivedFiles_FileReceiver` | TField |  | The Receiving Institution. |
| 8 | `DD.MRF.MANDATE.SERVICE` | `DdMandateReceivedFiles_MandateService` | TField |  | The Mandate service from where the files are received. |
| 9 | `DD.MRF.NO.OF.BULKS` | `DdMandateReceivedFiles_NoOfBulks` | TField |  | Number of Bulks in a file. |
| 10 | `DD.MRF.SERVICE.CODE` | `DdMandateReceivedFiles_ServiceCode` | TField |  | The Service identifier. |
| 11 | `DD.MRF.TEST.CODE` | `DdMandateReceivedFiles_TestCode` | TField |  | The Test Code. |
| 12 | `DD.MRF.FILE.NAME` | `DdMandateReceivedFiles_FileName` | TField |  | The name of the received file. |
| 13 | `DD.MRF.FILE.TYPE.INDICATOR` | `DdMandateReceivedFiles_FileTypeIndicator` | TField |  | Indicates the type of the file. I - Incoming requests, default if not provided R - Responses from the central system |
| 14 | `DD.MRF.ORG.FILE.NAME` | `DdMandateReceivedFiles_OrgFileName` | TField |  | Only for R file types. Indicates the name of the original file for which the central system response is received. |
| 15 | `DD.MRF.ORG.FILE.REFERENCE` | `DdMandateReceivedFiles_OrgFileReference` | TField |  | Only for R file types. Indicates the reference of the original file for which the central system response is received. |
| 16 | `DD.MRF.ORG.FILE.REJECT.REASON` | `DdMandateReceivedFiles_OrgFileRejectReason` | TField |  | Only for R file types. Indicates the reject reason of the original file for which the central system response is received. |
| 17 | `DD.MRF.ORG.FILE.DATE.TIME` | `DdMandateReceivedFiles_OrgFileDateTime` |  |  |  |
| 18 | `DD.MRF.STATUS` | `DdMandateReceivedFiles_Status` | TField |  | The status of the file processing: RECEIVED, PROCESSED, REJECTED, CONFIRMED, COMPLETED. |
| 19 | `DD.MRF.ERROR.CODE` | `DdMandateReceivedFiles_ErrorCode` | TField |  | Updated during subsequent steps of the inbound process when the file is Rejected. |
| 20 | `DD.MRF.ERROR.REASON` | `DdMandateReceivedFiles_ErrorReason` | TField |  | Updated during subsequent steps of the inbound process when the file is Rejected. |
| 21 | `DD.MRF.RESERVED` | `DdMandateReceivedFiles_Reserved` | TField |  | Reserved for future use. |
