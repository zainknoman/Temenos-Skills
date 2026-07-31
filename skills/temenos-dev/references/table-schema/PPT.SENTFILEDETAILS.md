# PPT.SENTFILEDETAILS — Table Schema

> Source: `INSERTS/I_F.PPT.SENTFILEDETAILS` in `PP_OutwardMappingFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPSFD.CompanyID` | `PptSentfiledetails_Companyid` | TField |  | ID of the company for which the record is applicable or processing company. Example: EU1 Validation Rules: It holds 3 alphanumeric characters. The value links to the field �CompanyID� in PPT.COMPANY. |
| 2 | `PPSFD.FileReference` | `PptSentfiledetails_Filereference` |  |  |  |
| 3 | `PPSFD.SentDate` | `PptSentfiledetails_Sentdate` |  |  |  |
| 4 | `PPSFD.FileName` | `PptSentfiledetails_Filename` | TField |  | Name of the file generated from the system, sent to the clearing. |
| 5 | `PPSFD.FileType` | `PptSentfiledetails_Filetype` | TField |  | Type of the file sent to the clearing. Examples for SEPA clearers: ICF, IDF |
| 6 | `PPSFD.SingleMultipleIndicator` | `PptSentfiledetails_Singlemultipleindicator` | TField |  | Indicator to determine if the message is Single or Multiple. Possible values: 'S' - Single transaction file 'C' - Clearing (multiple transactions) 'B' - Batch |
| 7 | `PPSFD.OutputChannel` | `PptSentfiledetails_Outputchannel` | TField |  | Channel on which the file is sent to the recipient. Examples: STEP2, RPSSCL |
| 8 | `PPSFD.CreationDateTime` | `PptSentfiledetails_Creationdatetime` | TField |  | Indicates the system date and time when the status becomes 'READY'. Example: 12 JAN 2015 12:34:25.123 Validation Rules: It needs to be displayed as DD MMM YYYY HH:MM:SS.sss. |
| 9 | `PPSFD.FileStatus` | `PptSentfiledetails_Filestatus` | TField |  | Indicates the current status of the file. Possible values: 'READY' - put in generic tables 'SENT' - file generated and sent to the clearing 'ACCP' - accepted by the clearing 'RJCT' - rejected by the clearing 'PART' - partially accepted by the clearing. |
| 10 | `PPSFD.NumberOfBulks` | `PptSentfiledetails_Numberofbulks` | TField |  | The number of bulks in the file. |
| 11 | `PPSFD.ClearingStatusFileReference` | `PptSentfiledetails_Clearingstatusfilereference` |  |  |  |
| 12 | `PPSFD.ClearingReasonCode` | `PptSentfiledetails_Clearingreasoncode` | TField |  | Code acceptance or rejection as provided in a Clearing Status Report. |
| 13 | `PPSFD.ClearingActionStatusCode` | `PptSentfiledetails_Clearingactionstatuscode` | TField |  | When a Clearing Report with "RJCT" or "PART" comes, it will go into an expection queue.. Possible values: 'PNDG' - pending 'CMPT' - completed 'SUBM' - resubmitted Examples: When the Clearing Report bulk is received, the field is updated at status "PNDG". When an action is taken in the Exception Queue of the Clearing Status Report, the fields is updated at status CMPT. If the Clearing Report is received with "ACCP", this field is updated directly to "CMPT". If the original file is resubmitted to the clearing the filed is updated directly to "SUBM". Validation Rules: 4 alphanumeric characters. |
| 14 | `PPSFD.ClearingActionStatusDateTime` | `PptSentfiledetails_Clearingactionstatusdatetime` | TField |  | Date and time when ClearingActionStatusCode is updated. Validation Rules: 17 characters Date Time format. It need to be displayed as DD MMM YYYY HH:MM:SS.sss. Example: 12 JAN 2015 12:34:25.123 The value is not editable by the user. |
| 15 | `PPSFD.OVERRIDE` | `PptSentfiledetails_Override` |  |  |  |
| 16 | `PPSFD.RECORD.STATUS` | `PptSentfiledetails_RecordStatus` | String |  |  |
| 17 | `PPSFD.CURR.NO` | `PptSentfiledetails_CurrNo` | String |  |  |
| 18 | `PPSFD.INPUTTER` | `PptSentfiledetails_Inputter` |  |  |  |
| 19 | `PPSFD.DATE.TIME` | `PptSentfiledetails_DateTime` |  |  |  |
| 20 | `PPSFD.AUTHORISER` | `PptSentfiledetails_Authoriser` | String |  |  |
| 21 | `PPSFD.CO.CODE` | `PptSentfiledetails_CoCode` | String |  |  |
| 22 | `PPSFD.DEPT.CODE` | `PptSentfiledetails_DeptCode` | String |  |  |
| 23 | `PPSFD.AUDITOR.CODE` | `PptSentfiledetails_AuditorCode` | String |  |  |
| 24 | `PPSFD.AUDIT.DATE.TIME` | `PptSentfiledetails_AuditDateTime` | String |  |  |
| 25 | `PPSFD.OriginalFileReference` | `PptSentfiledetails_Originalfilereference` |  |  |  |
| 26 | `PPSFD.SourceType` | `PptSentfiledetails_Sourcetype` | TField |  |  |
| 27 | `PPSFD.ClearingProcessingDate` | `PptSentfiledetails_Clearingprocessingdate` | TField |  | ClearingProcessingDate is the day when clearing forwards the file to the destination bank. This Processing day will be sent in the DDI outgoing file |
| 28 | `PPSFD.ReceiverAddress` | `PptSentfiledetails_Receiveraddress` | TField |  | Instructed Party i.e BIC/NCC of the party receiving the file. It could be the clearing BIC/NCC or IP NCC/BIC |
| 29 | `PPSFD.ErrorInformation` | `PptSentfiledetails_Errorinformation` | TField |  | This field holds the XSLT and XSD Failure Error Information |
