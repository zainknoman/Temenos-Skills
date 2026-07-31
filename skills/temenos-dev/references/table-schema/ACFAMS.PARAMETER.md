# ACFAMS.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ACFAMS.PARAMETER` in `ACFAMS_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACFAMS.PAR.FA.STAGE` | `AcfamsParameter_FaStage` | TField |  | The status of the system.Allowed values ONLINE, PREP,SYNC,LIMITED. This will be an EXTERN field. |
| 2 | `ACFAMS.PAR.FA.ALLOWED` | `AcfamsParameter_FaAllowed` | TField |  | The default LSM Allowed flag. Options with YES/NO |
| 3 | `ACFAMS.PAR.START.CATEG` | `AcfamsParameter_StartCateg` |  |  |  |
| 4 | `ACFAMS.PAR.END.CATEG` | `AcfamsParameter_EndCateg` |  |  |  |
| 5 | `ACFAMS.PAR.CATEG.RESERVED5` | `AcfamsParameter_CategReserved5` |  |  |  |
| 6 | `ACFAMS.PAR.CATEG.RESERVED4` | `AcfamsParameter_CategReserved4` |  |  |  |
| 7 | `ACFAMS.PAR.CATEG.RESERVED3` | `AcfamsParameter_CategReserved3` |  |  |  |
| 8 | `ACFAMS.PAR.CATEG.RESERVED2` | `AcfamsParameter_CategReserved2` |  |  |  |
| 9 | `ACFAMS.PAR.CATEG.RESERVED1` | `AcfamsParameter_CategReserved1` |  |  |  |
| 10 | `ACFAMS.PAR.FA.LOG` | `AcfamsParameter_FaLog` | TField |  | FA micro Service to log all requests.YES/NO are options NO or Null = Only LIMITED requests are recorded in FAMS. YES = LIMITED and ONLINE requests are recorded in FAMS |
| 11 | `ACFAMS.PAR.SYNC.ERROR.PERCENT.ALLOWED` | `AcfamsParameter_SyncErrorPercentAllowed` | TField |  | If the percentage of pending queue requests with errors exceeds this amount, the system will not be switched to ONLINE |
| 12 | `ACFAMS.PAR.SYNC.ERRORS.ALLOWED` | `AcfamsParameter_SyncErrorsAllowed` | TField |  | If the number of Accounts with SYNC errors exceeds this amount, the system will not be switched to ONLINE |
| 13 | `ACFAMS.PAR.ERR.POSTING.RESTRICT` | `AcfamsParameter_ErrPostingRestrict` |  |  |  |
| 14 | `ACFAMS.PAR.RESERVED.17` | `AcfamsParameter_Reserved17` |  |  |  |
| 15 | `ACFAMS.PAR.RESERVED.16` | `AcfamsParameter_Reserved16` |  |  |  |
| 16 | `ACFAMS.PAR.RESERVED.15` | `AcfamsParameter_Reserved15` |  |  |  |
| 17 | `ACFAMS.PAR.RESERVED.14` | `AcfamsParameter_Reserved14` | TField |  |  |
| 18 | `ACFAMS.PAR.RESERVED.13` | `AcfamsParameter_Reserved13` | TField |  |  |
| 19 | `ACFAMS.PAR.RESERVED.12` | `AcfamsParameter_Reserved12` | TField |  |  |
| 20 | `ACFAMS.PAR.RESERVED.11` | `AcfamsParameter_Reserved11` | TField |  |  |
| 21 | `ACFAMS.PAR.RESERVED.10` | `AcfamsParameter_Reserved10` | TField |  |  |
| 22 | `ACFAMS.PAR.RESERVED.9` | `AcfamsParameter_Reserved9` | TField |  |  |
| 23 | `ACFAMS.PAR.RESERVED.8` | `AcfamsParameter_Reserved8` | TField |  |  |
| 24 | `ACFAMS.PAR.RESERVED.7` | `AcfamsParameter_Reserved7` | TField |  |  |
| 25 | `ACFAMS.PAR.RESERVED.6` | `AcfamsParameter_Reserved6` | TField |  |  |
| 26 | `ACFAMS.PAR.RESERVED.5` | `AcfamsParameter_Reserved5` | TField |  |  |
| 27 | `ACFAMS.PAR.RESERVED.4` | `AcfamsParameter_Reserved4` | TField |  |  |
| 28 | `ACFAMS.PAR.RESERVED.3` | `AcfamsParameter_Reserved3` | TField |  |  |
| 29 | `ACFAMS.PAR.RESERVED.2` | `AcfamsParameter_Reserved2` | TField |  |  |
| 30 | `ACFAMS.PAR.RESERVED.1` | `AcfamsParameter_Reserved1` | TField |  |  |
| 31 | `ACFAMS.PAR.LOCAL.REF` | `AcfamsParameter_LocalRef` |  |  |  |
| 32 | `ACFAMS.PAR.OVERRIDE` | `AcfamsParameter_Override` |  |  |  |
| 33 | `ACFAMS.PAR.RECORD.STATUS` | `AcfamsParameter_RecordStatus` | String |  |  |
| 34 | `ACFAMS.PAR.CURR.NO` | `AcfamsParameter_CurrNo` | String |  |  |
| 35 | `ACFAMS.PAR.INPUTTER` | `AcfamsParameter_Inputter` |  |  |  |
| 36 | `ACFAMS.PAR.DATE.TIME` | `AcfamsParameter_DateTime` |  |  |  |
| 37 | `ACFAMS.PAR.AUTHORISER` | `AcfamsParameter_Authoriser` | String |  |  |
| 38 | `ACFAMS.PAR.CO.CODE` | `AcfamsParameter_CoCode` | String |  |  |
| 39 | `ACFAMS.PAR.DEPT.CODE` | `AcfamsParameter_DeptCode` | String |  |  |
| 40 | `ACFAMS.PAR.AUDITOR.CODE` | `AcfamsParameter_AuditorCode` | String |  |  |
| 41 | `ACFAMS.PAR.AUDIT.DATE.TIME` | `AcfamsParameter_AuditDateTime` | String |  |  |
