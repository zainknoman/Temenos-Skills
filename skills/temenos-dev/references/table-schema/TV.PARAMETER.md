# TV.PARAMETER — Table Schema

> Source: `INSERTS/I_F.TV.PARAMETER` in `TV_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.TVP.OPERATION.MODE` | `TvParameter_OperationMode` | TField | Yes | The types of capture/playback techniques. A mandatory input. Max 4 characters are allowed to input and the types are available in the drop-down list. There are six types such as CT,CTFR,CTUR,CR,TT and NONE. Where CT stands for Capture transactions only, CTFR - Capture transactions with formatted results. CTUR - Capture transactions with un-formatted results, CR - Check results only, TT- Test transactions, NONE - No need to capture/playback transactions. The user can choose the required capture type, as per his/her business requirement. |
| 2 | `EB.TVP.TRANS.STORE.PATH` | `TvParameter_TransStorePath` | TField |  | The path name, to store the captured transactions. Max 50 alphanumeric characters are allowed to input. An error message is displayed, if the existing path is not specified. eg., ../TestBase.run/TRANS.LOG |
| 3 | `EB.TVP.TS.CAPACITY` | `TvParameter_TsCapacity` | TField |  | The n number of transactions, that needs to be stored in every captured log file. Max 6 numeric digits are allowed to input. No commas are allowed. eg., 10000 |
| 4 | `EB.TVP.CAPTURE.START.DATE` | `TvParameter_CaptureStartDate` | TField |  | The bank date, when we start the transaction capture for the first time. No input field. This field value will be updated automatically. |
| 5 | `EB.TVP.RETENTION.DAYS` | `TvParameter_RetentionDays` | TField | Yes | The value in this field signifies the number of days. The transactions in the log will be retained for the number of days specified (other transactions will be purged) Validation Rules: Upto 4 degits allowed. (Not Mandatory Input) Based on the value in this field LOG values are purged. Example: If the value given in this field is 1, and we kept 3 days log in TRANS.LOG. Now we are running COB, last one day transaction will be retained in log. The other days log will be purged during COB |
| 6 | `EB.TVP.SEQUENCE.IN.DIR` | `TvParameter_SequenceInDir` | TField |  | The name of directory, that stores the playback transactions. Max 35 alphanumeric characters are allowed to input. No need to specify the entire path, just the existing directory name alone is enough eg., SEAT.IN |
| 7 | `EB.TVP.UPLOAD.IN.DIR` | `TvParameter_UploadInDir` | TField |  | In-directory defined in BATCH FILE listener of tcserver |
| 8 | `EB.TVP.NO.OF.SESSIONS` | `TvParameter_NoOfSessions` | TField |  | The number of sessions, that the sequencer service is going to run. |
| 9 | `EB.TVP.EXCEPTION.CONTROL` | `TvParameter_ExceptionControl` | TField |  |  |
| 10 | `EB.TVP.RESERVED.7` | `TvParameter_Reserved7` | TField |  |  |
| 11 | `EB.TVP.RESERVED.6` | `TvParameter_Reserved6` | TField |  |  |
| 12 | `EB.TVP.RESERVED.5` | `TvParameter_Reserved5` | TField |  |  |
| 13 | `EB.TVP.RESERVED.4` | `TvParameter_Reserved4` | TField |  |  |
| 14 | `EB.TVP.RESERVED.3` | `TvParameter_Reserved3` | TField |  |  |
| 15 | `EB.TVP.RESERVED.2` | `TvParameter_Reserved2` | TField |  |  |
| 16 | `EB.TVP.RESERVED.1` | `TvParameter_Reserved1` | TField |  |  |
| 17 | `EB.TVP.LOCAL.REF` | `TvParameter_LocalRef` |  |  |  |
| 18 | `EB.TVP.OVERRIDE` | `TvParameter_Override` |  |  |  |
| 19 | `EB.TVP.RECORD.STATUS` | `TvParameter_RecordStatus` | String |  |  |
| 20 | `EB.TVP.CURR.NO` | `TvParameter_CurrNo` | String |  |  |
| 21 | `EB.TVP.INPUTTER` | `TvParameter_Inputter` |  |  |  |
| 22 | `EB.TVP.DATE.TIME` | `TvParameter_DateTime` |  |  |  |
| 23 | `EB.TVP.AUTHORISER` | `TvParameter_Authoriser` | String |  |  |
| 24 | `EB.TVP.CO.CODE` | `TvParameter_CoCode` | String |  |  |
| 25 | `EB.TVP.DEPT.CODE` | `TvParameter_DeptCode` | String |  |  |
| 26 | `EB.TVP.AUDITOR.CODE` | `TvParameter_AuditorCode` | String |  |  |
| 27 | `EB.TVP.AUDIT.DATE.TIME` | `TvParameter_AuditDateTime` | String |  |  |
