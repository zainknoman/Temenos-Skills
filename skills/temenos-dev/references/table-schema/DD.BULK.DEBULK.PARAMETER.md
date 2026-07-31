# DD.BULK.DEBULK.PARAMETER — Table Schema

> Source: `INSERTS/I_F.DD.BULK.DEBULK.PARAMETER` in `DD_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DD.BDP.INW.MAP.LCL.HOOK.API` | `DdBulkDebulkParameter_InwMapLclHookApi` | TField |  | Local hook api that can be used to modify the contents of the payload of the received transaction. This API should contains 3 arguments as below - Argument1 : DD.DDI Record as input and output to send modified record Argument2, Argument3 - Reserved for future use |
| 2 | `DD.BDP.MAX.TRANSACTION.PER.BULK` | `DdBulkDebulkParameter_MaxTransactionPerBulk` | TField |  | The number to denote, maximum number of transactions per bulk. |
| 3 | `DD.BDP.MAX.BULK.PER.FILE` | `DdBulkDebulkParameter_MaxBulkPerFile` | TField |  | The number to denote, maximum number of bulks per file. |
| 4 | `DD.BDP.BULK.CRITERIA.ROUTINE` | `DdBulkDebulkParameter_BulkCriteriaRoutine` | TField |  | The local routine which decides the, filename convention and bulk id convention. Input arguments mandateservice,message type,instrcutedagent. Output arguments BulkReference,FileReference. |
| 5 | `DD.BDP.ARCHIVE.DAYS` | `DdBulkDebulkParameter_ArchiveDays` | TField |  | This will indicate a number of days/months after which completed files, bulk, and requests can be archived. It'll be calender days. |
| 6 | `DD.BDP.BULKING.DAYS` | `DdBulkDebulkParameter_BulkingDays` | TField |  | This indicates the number of days after which Mandate Outward transactions in New status can be bulked. Working or calender can be mentioned. E.g If pain.012 created on 1 April and Bulking days is 2W then the pain,012 will be bulked on 3rd April . |
| 7 | `DD.BDP.TEST.CODE` | `DdBulkDebulkParameter_TestCode` | TField |  | Will allow the bank to paramterise the Test Code which will be sent in the file Header. For e.g. for SEDA this is T for Test and P for Production. |
| 8 | `DD.BDP.MANDATE.SERVICE.BIC` | `DdBulkDebulkParameter_MandateServiceBic` | TField |  | This will be the File Sender Institution/Received Institution, in case of a central mandate service. |
| 9 | `DD.BDP.SERVICE.CODE` | `DdBulkDebulkParameter_ServiceCode` | TField |  | Identifies the Service Code associated with the Mandate Service. |
| 10 | `DD.BDP.MESSAGE.TYPE` | `DdBulkDebulkParameter_MessageType` |  |  |  |
| 11 | `DD.BDP.MSG.BULKING.DAYS` | `DdBulkDebulkParameter_MsgBulkingDays` |  |  |  |
| 12 | `DD.BDP.RESERVED.5` | `DdBulkDebulkParameter_Reserved5` | TField |  |  |
| 13 | `DD.BDP.RESERVED.4` | `DdBulkDebulkParameter_Reserved4` | TField |  |  |
| 14 | `DD.BDP.RESERVED.3` | `DdBulkDebulkParameter_Reserved3` | TField |  |  |
| 15 | `DD.BDP.RESERVED.2` | `DdBulkDebulkParameter_Reserved2` | TField |  |  |
| 16 | `DD.BDP.RESERVED.1` | `DdBulkDebulkParameter_Reserved1` | TField |  |  |
| 17 | `DD.BDP.LOCAL.REF` | `DdBulkDebulkParameter_LocalRef` |  |  |  |
| 18 | `DD.BDP.OVERRIDE` | `DdBulkDebulkParameter_Override` |  |  |  |
| 19 | `DD.BDP.RECORD.STATUS` | `DdBulkDebulkParameter_RecordStatus` | String |  |  |
| 20 | `DD.BDP.CURR.NO` | `DdBulkDebulkParameter_CurrNo` | String |  |  |
| 21 | `DD.BDP.INPUTTER` | `DdBulkDebulkParameter_Inputter` |  |  |  |
| 22 | `DD.BDP.DATE.TIME` | `DdBulkDebulkParameter_DateTime` |  |  |  |
| 23 | `DD.BDP.AUTHORISER` | `DdBulkDebulkParameter_Authoriser` | String |  |  |
| 24 | `DD.BDP.CO.CODE` | `DdBulkDebulkParameter_CoCode` | String |  |  |
| 25 | `DD.BDP.DEPT.CODE` | `DdBulkDebulkParameter_DeptCode` | String |  |  |
| 26 | `DD.BDP.AUDITOR.CODE` | `DdBulkDebulkParameter_AuditorCode` | String |  |  |
| 27 | `DD.BDP.AUDIT.DATE.TIME` | `DdBulkDebulkParameter_AuditDateTime` | String |  |  |
