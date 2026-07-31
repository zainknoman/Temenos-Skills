# DLM.PARAMETER — Table Schema

> Source: `INSERTS/I_F.DLM.PARAMETER` in `DL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DLM.PARAM.DESCRIPTION` | `DlmParameter_Description` |  |  |  |
| 2 | `DLM.PARAM.MAX.OPERATION.COUNT` | `DlmParameter_MaxOperationCount` | TField |  | Indicates number of records needs to be processed at a time(before giving control to BATCH.JOB.CONTROL) Validation Rules: Upto 10 Numeric value If the field value is null default value 1000 will be assigned to the field |
| 3 | `DLM.PARAM.MAX.BYTE.LENGTH` | `DlmParameter_MaxByteLength` | TField |  | Indicates the byte length of one XML record content in ACTIVATION.FILE Validation Rules: Upto 6 Numeric value If the field value is null default value 2000 will be assigned to the field |
| 4 | `DLM.PARAM.REVIEW.TIME` | `DlmParameter_ReviewTime` | TField |  | Indicates the time interval after which the ACTIVATION.FILE count needs to be verified Validation Rules: Value should be in HH:MM:SS format If the field value is null default value 00:05:00(HH:MM:SS) will be assigned to the field |
| 5 | `DLM.PARAM.SLEEP.TIME.POST.REVIEW` | `DlmParameter_SleepTimePostReview` | TField |  | Indicates the sleep time if the ACTIVATION.FILE count is matched with the provided ACTIVATION.COUNT Validation Rules: Value should be in HH:MM:SS format If the field value is null default value 00:02:00(HH:MM:SS) will be assigned to the field |
| 6 | `DLM.PARAM.ACTIVATION.COUNT` | `DlmParameter_ActivationCount` | TField |  | Indicates the Count of ACTIVATION.FILE. if the ACTIVATION.FILE count is increased above to the given ACTIVATION.COUNT then the selection service should sleep for given period of SLEEP.TIME and countine to do the selection service process once the ACTIVATION.FILE count reduced less than the given ACTIVATION.COUNT Validation Rules: Upto 10 Numeric value If the field value is null default value 10000 will be assigned to the field |
| 7 | `DLM.PARAM.REDIRECTION.FLAG` | `DlmParameter_RedirectionFlag` | TField |  | Decides to get the Read Only database records during the enquiry execution. YES/No field. If REDIRECTION.FLAG enabled and INCLUDE.DL field value is NULL then enquiry will get the record from both LIVE and Read Only database If REDIRECTION.FLAG not enabled and INCLUDE.DL field value is NULL then enquiry will get the record from LIVE alone |
| 8 | `DLM.PARAM.RESERVED.19` | `DlmParameter_Reserved19` |  |  |  |
| 9 | `DLM.PARAM.RESERVED.18` | `DlmParameter_Reserved18` | TField |  |  |
| 10 | `DLM.PARAM.RESERVED.17` | `DlmParameter_Reserved17` | TField |  |  |
| 11 | `DLM.PARAM.RESERVED.16` | `DlmParameter_Reserved16` | TField |  |  |
| 12 | `DLM.PARAM.RESERVED.15` | `DlmParameter_Reserved15` | TField |  |  |
| 13 | `DLM.PARAM.RESERVED.14` | `DlmParameter_Reserved14` | TField |  |  |
| 14 | `DLM.PARAM.RESERVED.13` | `DlmParameter_Reserved13` | TField |  |  |
| 15 | `DLM.PARAM.RESERVED.12` | `DlmParameter_Reserved12` | TField |  |  |
| 16 | `DLM.PARAM.RESERVED.11` | `DlmParameter_Reserved11` | TField |  |  |
| 17 | `DLM.PARAM.RESERVED.10` | `DlmParameter_Reserved10` | TField |  |  |
| 18 | `DLM.PARAM.RESERVED.9` | `DlmParameter_Reserved9` | TField |  |  |
| 19 | `DLM.PARAM.RESERVED.8` | `DlmParameter_Reserved8` | TField |  |  |
| 20 | `DLM.PARAM.RESERVED.7` | `DlmParameter_Reserved7` | TField |  |  |
| 21 | `DLM.PARAM.RESERVED.6` | `DlmParameter_Reserved6` | TField |  |  |
| 22 | `DLM.PARAM.RESERVED.5` | `DlmParameter_Reserved5` | TField |  |  |
| 23 | `DLM.PARAM.RESERVED.4` | `DlmParameter_Reserved4` | TField |  |  |
| 24 | `DLM.PARAM.RESERVED.3` | `DlmParameter_Reserved3` | TField |  |  |
| 25 | `DLM.PARAM.RESERVED.2` | `DlmParameter_Reserved2` | TField |  |  |
| 26 | `DLM.PARAM.RESERVED.1` | `DlmParameter_Reserved1` | TField |  |  |
| 27 | `DLM.PARAM.OVERRIDE` | `DlmParameter_Override` |  |  |  |
| 28 | `DLM.PARAM.RECORD.STATUS` | `DlmParameter_RecordStatus` | String |  |  |
| 29 | `DLM.PARAM.CURR.NO` | `DlmParameter_CurrNo` | String |  |  |
| 30 | `DLM.PARAM.INPUTTER` | `DlmParameter_Inputter` |  |  |  |
| 31 | `DLM.PARAM.DATE.TIME` | `DlmParameter_DateTime` |  |  |  |
| 32 | `DLM.PARAM.AUTHORISER` | `DlmParameter_Authoriser` | String |  |  |
| 33 | `DLM.PARAM.CO.CODE` | `DlmParameter_CoCode` | String |  |  |
| 34 | `DLM.PARAM.DEPT.CODE` | `DlmParameter_DeptCode` | String |  |  |
| 35 | `DLM.PARAM.AUDITOR.CODE` | `DlmParameter_AuditorCode` | String |  |  |
| 36 | `DLM.PARAM.AUDIT.DATE.TIME` | `DlmParameter_AuditDateTime` | String |  |  |
