# FS.GA.SECURITY.POSITION — Table Schema

> Source: `INSERTS/I_F.FS.GA.SECURITY.POSITION` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SECURITY.POSITION.PARENT.REF.ID` | `FsGaSecurityPosition_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.SECURITY.POSITION.ORA.ROWID` | `FsGaSecurityPosition_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.SECURITY.POSITION.FUND.ID` | `FsGaSecurityPosition_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.SECURITY.POSITION.INTERNAL.SECURITY.ID` | `FsGaSecurityPosition_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 5 | `FS.GA.SECURITY.POSITION.CORRESPONDENT` | `FsGaSecurityPosition_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 6 | `FS.GA.SECURITY.POSITION.SERVICE.CODE` | `FsGaSecurityPosition_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 7 | `FS.GA.SECURITY.POSITION.LOT.NUMBER` | `FsGaSecurityPosition_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 8 | `FS.GA.SECURITY.POSITION.MANAGER.CODE` | `FsGaSecurityPosition_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 9 | `FS.GA.SECURITY.POSITION.CHARGE.CODE` | `FsGaSecurityPosition_ChargeCode` | TField |  | Corresponds to Multifonds fee code or NAV charge number Multifonds DB Column is NOFRAIS. |
| 10 | `FS.GA.SECURITY.POSITION.PERCENTAGE.OF.FEES` | `FsGaSecurityPosition_PercentageOfFees` | TField |  | The percentage of fee calculated at target fund level is set in the field Percentage of fees&quot; Multifonds DB Column is PCT_FPRT. |
| 11 | `FS.GA.SECURITY.POSITION.RESERVED10` | `FsGaSecurityPosition_Reserved10` | TField |  |  |
| 12 | `FS.GA.SECURITY.POSITION.RESERVED9` | `FsGaSecurityPosition_Reserved9` | TField |  |  |
| 13 | `FS.GA.SECURITY.POSITION.RESERVED8` | `FsGaSecurityPosition_Reserved8` | TField |  |  |
| 14 | `FS.GA.SECURITY.POSITION.RESERVED7` | `FsGaSecurityPosition_Reserved7` | TField |  |  |
| 15 | `FS.GA.SECURITY.POSITION.RESERVED6` | `FsGaSecurityPosition_Reserved6` | TField |  |  |
| 16 | `FS.GA.SECURITY.POSITION.RESERVED5` | `FsGaSecurityPosition_Reserved5` | TField |  |  |
| 17 | `FS.GA.SECURITY.POSITION.RESERVED4` | `FsGaSecurityPosition_Reserved4` | TField |  |  |
| 18 | `FS.GA.SECURITY.POSITION.RESERVED3` | `FsGaSecurityPosition_Reserved3` | TField |  |  |
| 19 | `FS.GA.SECURITY.POSITION.RESERVED2` | `FsGaSecurityPosition_Reserved2` | TField |  |  |
| 20 | `FS.GA.SECURITY.POSITION.RESERVED1` | `FsGaSecurityPosition_Reserved1` | TField |  |  |
| 21 | `FS.GA.SECURITY.POSITION.LOCAL.REF` | `FsGaSecurityPosition_LocalRef` |  |  |  |
| 22 | `FS.GA.SECURITY.POSITION.OVERRIDE` | `FsGaSecurityPosition_Override` |  |  |  |
| 23 | `FS.GA.SECURITY.POSITION.RECORD.STATUS` | `FsGaSecurityPosition_RecordStatus` | String |  |  |
| 24 | `FS.GA.SECURITY.POSITION.CURR.NO` | `FsGaSecurityPosition_CurrNo` | String |  |  |
| 25 | `FS.GA.SECURITY.POSITION.INPUTTER` | `FsGaSecurityPosition_Inputter` |  |  |  |
| 26 | `FS.GA.SECURITY.POSITION.DATE.TIME` | `FsGaSecurityPosition_DateTime` |  |  |  |
| 27 | `FS.GA.SECURITY.POSITION.AUTHORISER` | `FsGaSecurityPosition_Authoriser` | String |  |  |
| 28 | `FS.GA.SECURITY.POSITION.CO.CODE` | `FsGaSecurityPosition_CoCode` | String |  |  |
| 29 | `FS.GA.SECURITY.POSITION.DEPT.CODE` | `FsGaSecurityPosition_DeptCode` | String |  |  |
| 30 | `FS.GA.SECURITY.POSITION.AUDITOR.CODE` | `FsGaSecurityPosition_AuditorCode` | String |  |  |
| 31 | `FS.GA.SECURITY.POSITION.AUDIT.DATE.TIME` | `FsGaSecurityPosition_AuditDateTime` | String |  |  |
