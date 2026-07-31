# DD.MANDATE.SENT.FILES — Table Schema

> Source: `INSERTS/I_F.DD.MANDATE.SENT.FILES` in `DD_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DD.MSF.COMPANY.ID` | `DdMandateSentFiles_CompanyId` | TField |  | The Transact Company for which the file is sent. |
| 2 | `DD.MSF.RECEIVED.FILE.ID` | `DdMandateSentFiles_ReceivedFileId` | TField |  | The id of DD Mandate Received Files corresponding to the file in which the request has been received, allocated by Transact. |
| 3 | `DD.MSF.FILE.REFERENCE` | `DdMandateSentFiles_FileReference` | TField |  | The Sender File Reference. |
| 4 | `DD.MSF.FILE.NAME` | `DdMandateSentFiles_FileName` | TField |  | The name of the sent file. |
| 5 | `DD.MSF.FILE.SENDER` | `DdMandateSentFiles_FileSender` | TField |  | The Sender Institution. |
| 6 | `DD.MSF.FILE.RECEIVER` | `DdMandateSentFiles_FileReceiver` | TField |  | The Receiving Institution. |
| 7 | `DD.MSF.MANDATE.SERVICE` | `DdMandateSentFiles_MandateService` | TField |  | The Mandate service from where the files are sent. |
| 8 | `DD.MSF.SERVICE.CODE` | `DdMandateSentFiles_ServiceCode` | TField |  | The Service Code assigned to the DD Mandate Service. |
| 9 | `DD.MSF.TEST.CODE` | `DdMandateSentFiles_TestCode` | TField |  | The Test Code. |
| 10 | `DD.MSF.NO.OF.BULKS` | `DdMandateSentFiles_NoOfBulks` | TField |  | Number of Bulks. |
| 11 | `DD.MSF.CLEARING.REASON.CODE` | `DdMandateSentFiles_ClearingReasonCode` | TField |  | The reason code returned in the response from Clearing. |
| 12 | `DD.MSF.CREATE.DATE.TIME` | `DdMandateSentFiles_CreateDateTime` |  |  |  |
| 13 | `DD.MSF.PROCESSED.DATE` | `DdMandateSentFiles_ProcessedDate` | TField |  |  |
| 14 | `DD.MSF.STATUS` | `DdMandateSentFiles_Status` | TField |  | The status of the file processing: NEW, PROCESSED, SENT, COMPLETED, ERROR, ACCREJ. |
| 15 | `DD.MSF.ERROR.CODE` | `DdMandateSentFiles_ErrorCode` | TField |  | Contains the ISO Reason Code corresponding to the T24 Error Id raised during validations. |
| 16 | `DD.MSF.ERROR.REASON` | `DdMandateSentFiles_ErrorReason` | TField |  | Updated during subsequent steps of the inbound process when the file is Rejected. |
| 17 | `DD.MSF.RESERVED.9` | `DdMandateSentFiles_Reserved9` | TField |  |  |
| 18 | `DD.MSF.RESERVED.8` | `DdMandateSentFiles_Reserved8` | TField |  |  |
| 19 | `DD.MSF.RESERVED.7` | `DdMandateSentFiles_Reserved7` | TField |  |  |
| 20 | `DD.MSF.RESERVED.6` | `DdMandateSentFiles_Reserved6` | TField |  |  |
| 21 | `DD.MSF.RESERVED.5` | `DdMandateSentFiles_Reserved5` | TField |  |  |
| 22 | `DD.MSF.RESERVED.4` | `DdMandateSentFiles_Reserved4` | TField |  |  |
| 23 | `DD.MSF.RESERVED.3` | `DdMandateSentFiles_Reserved3` | TField |  |  |
| 24 | `DD.MSF.RESERVED.2` | `DdMandateSentFiles_Reserved2` | TField |  |  |
| 25 | `DD.MSF.RESERVED.1` | `DdMandateSentFiles_Reserved1` | TField |  |  |
| 26 | `DD.MSF.LOCAL.REF` | `DdMandateSentFiles_LocalRef` |  |  |  |
| 27 | `DD.MSF.OVERRIDE` | `DdMandateSentFiles_Override` |  |  |  |
| 28 | `DD.MSF.RECORD.STATUS` | `DdMandateSentFiles_RecordStatus` | String |  |  |
| 29 | `DD.MSF.CURR.NO` | `DdMandateSentFiles_CurrNo` | String |  |  |
| 30 | `DD.MSF.INPUTTER` | `DdMandateSentFiles_Inputter` |  |  |  |
| 31 | `DD.MSF.DATE.TIME` | `DdMandateSentFiles_DateTime` |  |  |  |
| 32 | `DD.MSF.AUTHORISER` | `DdMandateSentFiles_Authoriser` | String |  |  |
| 33 | `DD.MSF.CO.CODE` | `DdMandateSentFiles_CoCode` | String |  |  |
| 34 | `DD.MSF.DEPT.CODE` | `DdMandateSentFiles_DeptCode` | String |  |  |
| 35 | `DD.MSF.AUDITOR.CODE` | `DdMandateSentFiles_AuditorCode` | String |  |  |
| 36 | `DD.MSF.AUDIT.DATE.TIME` | `DdMandateSentFiles_AuditDateTime` | String |  |  |
