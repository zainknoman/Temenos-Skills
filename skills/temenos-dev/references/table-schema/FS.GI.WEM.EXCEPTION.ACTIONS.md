# FS.GI.WEM.EXCEPTION.ACTIONS — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.EXCEPTION.ACTIONS` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EXCEPTION.ACTIONS.FUND.GROUP` | `FsGiWemExceptionActions_FundGroup` | TField |  |  |
| 2 | `EXCEPTION.ACTIONS.NAV.DATE` | `FsGiWemExceptionActions_NavDate` | TField |  |  |
| 3 | `EXCEPTION.ACTIONS.ACCOUNTING.DATE` | `FsGiWemExceptionActions_AccountingDate` | TField |  |  |
| 4 | `EXCEPTION.ACTIONS.CONTROL` | `FsGiWemExceptionActions_Control` | TField |  |  |
| 5 | `EXCEPTION.ACTIONS.STEP` | `FsGiWemExceptionActions_Step` | TField |  |  |
| 6 | `EXCEPTION.ACTIONS.SUB.STEP` | `FsGiWemExceptionActions_SubStep` | TField |  |  |
| 7 | `EXCEPTION.ACTIONS.ERROR.MESSAGE` | `FsGiWemExceptionActions_ErrorMessage` | TField |  |  |
| 8 | `EXCEPTION.ACTIONS.JUSTIFICATION.CODE` | `FsGiWemExceptionActions_JustificationCode` | TField |  |  |
| 9 | `EXCEPTION.ACTIONS.FILE` | `FsGiWemExceptionActions_File` | TField |  |  |
| 10 | `EXCEPTION.ACTIONS.DESCRIPTION` | `FsGiWemExceptionActions_Description` | TField |  |  |
| 11 | `EXCEPTION.ACTIONS.REJECTION.REASON` | `FsGiWemExceptionActions_RejectionReason` | TField |  |  |
| 12 | `EXCEPTION.ACTIONS.ACTION` | `FsGiWemExceptionActions_Action` | TField |  |  |
| 13 | `EXCEPTION.ACTIONS.RESERVED5` | `FsGiWemExceptionActions_Reserved5` | TField |  |  |
| 14 | `EXCEPTION.ACTIONS.RESERVED4` | `FsGiWemExceptionActions_Reserved4` | TField |  |  |
| 15 | `EXCEPTION.ACTIONS.RESERVED3` | `FsGiWemExceptionActions_Reserved3` | TField |  |  |
| 16 | `EXCEPTION.ACTIONS.RESERVED2` | `FsGiWemExceptionActions_Reserved2` | TField |  |  |
| 17 | `EXCEPTION.ACTIONS.RESERVED1` | `FsGiWemExceptionActions_Reserved1` | TField |  |  |
| 18 | `EXCEPTION.ACTIONS.LOCAL.REF` | `FsGiWemExceptionActions_LocalRef` |  |  |  |
| 19 | `EXCEPTION.ACTIONS.OVERRIDE` | `FsGiWemExceptionActions_Override` |  |  |  |
| 20 | `EXCEPTION.ACTIONS.RECORD.STATUS` | `FsGiWemExceptionActions_RecordStatus` | String |  |  |
| 21 | `EXCEPTION.ACTIONS.CURR.NO` | `FsGiWemExceptionActions_CurrNo` | String |  |  |
| 22 | `EXCEPTION.ACTIONS.INPUTTER` | `FsGiWemExceptionActions_Inputter` |  |  |  |
| 23 | `EXCEPTION.ACTIONS.DATE.TIME` | `FsGiWemExceptionActions_DateTime` |  |  |  |
| 24 | `EXCEPTION.ACTIONS.AUTHORISER` | `FsGiWemExceptionActions_Authoriser` | String |  |  |
| 25 | `EXCEPTION.ACTIONS.CO.CODE` | `FsGiWemExceptionActions_CoCode` | String |  |  |
| 26 | `EXCEPTION.ACTIONS.DEPT.CODE` | `FsGiWemExceptionActions_DeptCode` | String |  |  |
| 27 | `EXCEPTION.ACTIONS.AUDITOR.CODE` | `FsGiWemExceptionActions_AuditorCode` | String |  |  |
| 28 | `EXCEPTION.ACTIONS.AUDIT.DATE.TIME` | `FsGiWemExceptionActions_AuditDateTime` | String |  |  |
