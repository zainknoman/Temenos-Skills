# FS.GA.NAV.CONFIRMATION — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.CONFIRMATION` in `FS_Valuation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.CONFIRMATION.PARENT.REF.ID` | `FsGaNavConfirmation_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAV.CONFIRMATION.ORA.ROWID` | `FsGaNavConfirmation_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAV.CONFIRMATION.FUND.ID` | `FsGaNavConfirmation_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.NAV.CONFIRMATION.NAV.DATE` | `FsGaNavConfirmation_NavDate` | TField |  | Date of the NAV Multifonds DB Column is DATE_NAV. |
| 5 | `FS.GA.NAV.CONFIRMATION.NAV.TYPE` | `FsGaNavConfirmation_NavType` | TField |  | Valuation type of the Fund Multifonds DB Column is TYP_TRT. |
| 6 | `FS.GA.NAV.CONFIRMATION.RESERVED10` | `FsGaNavConfirmation_Reserved10` | TField |  |  |
| 7 | `FS.GA.NAV.CONFIRMATION.RESERVED9` | `FsGaNavConfirmation_Reserved9` | TField |  |  |
| 8 | `FS.GA.NAV.CONFIRMATION.RESERVED8` | `FsGaNavConfirmation_Reserved8` | TField |  |  |
| 9 | `FS.GA.NAV.CONFIRMATION.RESERVED7` | `FsGaNavConfirmation_Reserved7` | TField |  |  |
| 10 | `FS.GA.NAV.CONFIRMATION.RESERVED6` | `FsGaNavConfirmation_Reserved6` | TField |  |  |
| 11 | `FS.GA.NAV.CONFIRMATION.RESERVED5` | `FsGaNavConfirmation_Reserved5` | TField |  |  |
| 12 | `FS.GA.NAV.CONFIRMATION.RESERVED4` | `FsGaNavConfirmation_Reserved4` | TField |  |  |
| 13 | `FS.GA.NAV.CONFIRMATION.RESERVED3` | `FsGaNavConfirmation_Reserved3` | TField |  |  |
| 14 | `FS.GA.NAV.CONFIRMATION.RESERVED2` | `FsGaNavConfirmation_Reserved2` | TField |  |  |
| 15 | `FS.GA.NAV.CONFIRMATION.RESERVED1` | `FsGaNavConfirmation_Reserved1` | TField |  |  |
| 16 | `FS.GA.NAV.CONFIRMATION.LOCAL.REF` | `FsGaNavConfirmation_LocalRef` |  |  |  |
| 17 | `FS.GA.NAV.CONFIRMATION.OVERRIDE` | `FsGaNavConfirmation_Override` |  |  |  |
| 18 | `FS.GA.NAV.CONFIRMATION.RECORD.STATUS` | `FsGaNavConfirmation_RecordStatus` | String |  |  |
| 19 | `FS.GA.NAV.CONFIRMATION.CURR.NO` | `FsGaNavConfirmation_CurrNo` | String |  |  |
| 20 | `FS.GA.NAV.CONFIRMATION.INPUTTER` | `FsGaNavConfirmation_Inputter` |  |  |  |
| 21 | `FS.GA.NAV.CONFIRMATION.DATE.TIME` | `FsGaNavConfirmation_DateTime` |  |  |  |
| 22 | `FS.GA.NAV.CONFIRMATION.AUTHORISER` | `FsGaNavConfirmation_Authoriser` | String |  |  |
| 23 | `FS.GA.NAV.CONFIRMATION.CO.CODE` | `FsGaNavConfirmation_CoCode` | String |  |  |
| 24 | `FS.GA.NAV.CONFIRMATION.DEPT.CODE` | `FsGaNavConfirmation_DeptCode` | String |  |  |
| 25 | `FS.GA.NAV.CONFIRMATION.AUDITOR.CODE` | `FsGaNavConfirmation_AuditorCode` | String |  |  |
| 26 | `FS.GA.NAV.CONFIRMATION.AUDIT.DATE.TIME` | `FsGaNavConfirmation_AuditDateTime` | String |  |  |
