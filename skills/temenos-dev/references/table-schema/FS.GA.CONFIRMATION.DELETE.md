# FS.GA.CONFIRMATION.DELETE — Table Schema

> Source: `INSERTS/I_F.FS.GA.CONFIRMATION.DELETE` in `FS_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CONFIRMATION.DELETE.PARENT.REF.ID` | `FsGaConfirmationDelete_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CONFIRMATION.DELETE.ORA.ROWID` | `FsGaConfirmationDelete_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CONFIRMATION.DELETE.FUND.ID` | `FsGaConfirmationDelete_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.CONFIRMATION.DELETE.NAV.DATE` | `FsGaConfirmationDelete_NavDate` | TField |  | Date of the NAV Multifonds DB Column is NAV_DATE. |
| 5 | `FS.GA.CONFIRMATION.DELETE.RESERVED10` | `FsGaConfirmationDelete_Reserved10` | TField |  |  |
| 6 | `FS.GA.CONFIRMATION.DELETE.RESERVED9` | `FsGaConfirmationDelete_Reserved9` | TField |  |  |
| 7 | `FS.GA.CONFIRMATION.DELETE.RESERVED8` | `FsGaConfirmationDelete_Reserved8` | TField |  |  |
| 8 | `FS.GA.CONFIRMATION.DELETE.RESERVED7` | `FsGaConfirmationDelete_Reserved7` | TField |  |  |
| 9 | `FS.GA.CONFIRMATION.DELETE.RESERVED6` | `FsGaConfirmationDelete_Reserved6` | TField |  |  |
| 10 | `FS.GA.CONFIRMATION.DELETE.RESERVED5` | `FsGaConfirmationDelete_Reserved5` | TField |  |  |
| 11 | `FS.GA.CONFIRMATION.DELETE.RESERVED4` | `FsGaConfirmationDelete_Reserved4` | TField |  |  |
| 12 | `FS.GA.CONFIRMATION.DELETE.RESERVED3` | `FsGaConfirmationDelete_Reserved3` | TField |  |  |
| 13 | `FS.GA.CONFIRMATION.DELETE.RESERVED2` | `FsGaConfirmationDelete_Reserved2` | TField |  |  |
| 14 | `FS.GA.CONFIRMATION.DELETE.RESERVED1` | `FsGaConfirmationDelete_Reserved1` | TField |  |  |
| 15 | `FS.GA.CONFIRMATION.DELETE.LOCAL.REF` | `FsGaConfirmationDelete_LocalRef` |  |  |  |
| 16 | `FS.GA.CONFIRMATION.DELETE.OVERRIDE` | `FsGaConfirmationDelete_Override` |  |  |  |
| 17 | `FS.GA.CONFIRMATION.DELETE.RECORD.STATUS` | `FsGaConfirmationDelete_RecordStatus` | String |  |  |
| 18 | `FS.GA.CONFIRMATION.DELETE.CURR.NO` | `FsGaConfirmationDelete_CurrNo` | String |  |  |
| 19 | `FS.GA.CONFIRMATION.DELETE.INPUTTER` | `FsGaConfirmationDelete_Inputter` |  |  |  |
| 20 | `FS.GA.CONFIRMATION.DELETE.DATE.TIME` | `FsGaConfirmationDelete_DateTime` |  |  |  |
| 21 | `FS.GA.CONFIRMATION.DELETE.AUTHORISER` | `FsGaConfirmationDelete_Authoriser` | String |  |  |
| 22 | `FS.GA.CONFIRMATION.DELETE.CO.CODE` | `FsGaConfirmationDelete_CoCode` | String |  |  |
| 23 | `FS.GA.CONFIRMATION.DELETE.DEPT.CODE` | `FsGaConfirmationDelete_DeptCode` | String |  |  |
| 24 | `FS.GA.CONFIRMATION.DELETE.AUDITOR.CODE` | `FsGaConfirmationDelete_AuditorCode` | String |  |  |
| 25 | `FS.GA.CONFIRMATION.DELETE.AUDIT.DATE.TIME` | `FsGaConfirmationDelete_AuditDateTime` | String |  |  |
