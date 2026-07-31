# RF.RTP.CLR.REPORTS.FILE — Table Schema

> Source: `INSERTS/I_F.RF.RTP.CLR.REPORTS.FILE` in `RF_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RFCRF.Scheme` | `RfRtpClrReportsFile_Scheme` | TField |  | Name of the RTP Clearing scheme. Must be a valid record in RF.RTP.SCHEME. |
| 2 | `RFCRF.RecordType` | `RfRtpClrReportsFile_Recordtype` |  |  |  |
| 3 | `RFCRF.FileType` | `RfRtpClrReportsFile_Filetype` | TField |  | This field Type of the report file received. Mapped from the clearing report. |
| 4 | `RFCRF.FileReference` | `RfRtpClrReportsFile_Filereference` | TField |  | Reference of the file received from the clearing.. Mapped from the clearing report. |
| 5 | `RFCRF.DateTimeReceived` | `RfRtpClrReportsFile_Datetimereceived` | TField |  | The date and time at which R2P report file is sent by the clearing. Mapped from the clearing report. |
| 6 | `RFCRF.BusinessDate` | `RfRtpClrReportsFile_Businessdate` | TField |  | The business date of the report file. Mapped from the clearing report. |
| 7 | `RFCRF.FieldName` | `RfRtpClrReportsFile_Fieldname` |  |  |  |
| 8 | `RFCRF.FieldContent` | `RfRtpClrReportsFile_Fieldcontent` |  |  |  |
| 9 | `RFCRF.RESERVED.5` | `RfRtpClrReportsFile_Reserved5` | TField |  |  |
| 10 | `RFCRF.RESERVED.4` | `RfRtpClrReportsFile_Reserved4` | TField |  |  |
| 11 | `RFCRF.RESERVED.3` | `RfRtpClrReportsFile_Reserved3` | TField |  |  |
| 12 | `RFCRF.RESERVED.2` | `RfRtpClrReportsFile_Reserved2` | TField |  |  |
| 13 | `RFCRF.RESERVED.1` | `RfRtpClrReportsFile_Reserved1` | TField |  |  |
| 14 | `RFCRF.RECORD.STATUS` | `RfRtpClrReportsFile_RecordStatus` | String |  |  |
| 15 | `RFCRF.CURR.NO` | `RfRtpClrReportsFile_CurrNo` | String |  |  |
| 16 | `RFCRF.INPUTTER` | `RfRtpClrReportsFile_Inputter` |  |  |  |
| 17 | `RFCRF.DATE.TIME` | `RfRtpClrReportsFile_DateTime` |  |  |  |
| 18 | `RFCRF.AUTHORISER` | `RfRtpClrReportsFile_Authoriser` | String |  |  |
| 19 | `RFCRF.CO.CODE` | `RfRtpClrReportsFile_CoCode` | String |  |  |
| 20 | `RFCRF.DEPT.CODE` | `RfRtpClrReportsFile_DeptCode` | String |  |  |
| 21 | `RFCRF.AUDITOR.CODE` | `RfRtpClrReportsFile_AuditorCode` | String |  |  |
| 22 | `RFCRF.AUDIT.DATE.TIME` | `RfRtpClrReportsFile_AuditDateTime` | String |  |  |
