# FS.GI.APP.WORK.UNIT.PRICE — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.WORK.UNIT.PRICE` in `FS_Dividend.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.WORK.UNIT.PRICE.FUND.ID` | `FsGiAppWorkUnitPrice_FundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 2 | `FS.GI.APP.WORK.UNIT.PRICE.SHARE.CLASS.CODE` | `FsGiAppWorkUnitPrice_ShareClassCode` | TField |  | Fund share class. Multifonds DB Column is TPART. |
| 3 | `FS.GI.APP.WORK.UNIT.PRICE.UNIT.PRICE` | `FsGiAppWorkUnitPrice_UnitPrice` | TField |  | Unit price for the fund. Multifonds DB Column is PRICE. |
| 4 | `FS.GI.APP.WORK.UNIT.PRICE.USER.ID` | `FsGiAppWorkUnitPrice_UserId` | TField |  | User identification. Multifonds DB Column is USERID. |
| 5 | `FS.GI.APP.WORK.UNIT.PRICE.RESERVED10` | `FsGiAppWorkUnitPrice_Reserved10` | TField |  |  |
| 6 | `FS.GI.APP.WORK.UNIT.PRICE.RESERVED9` | `FsGiAppWorkUnitPrice_Reserved9` | TField |  |  |
| 7 | `FS.GI.APP.WORK.UNIT.PRICE.RESERVED8` | `FsGiAppWorkUnitPrice_Reserved8` | TField |  |  |
| 8 | `FS.GI.APP.WORK.UNIT.PRICE.RESERVED7` | `FsGiAppWorkUnitPrice_Reserved7` | TField |  |  |
| 9 | `FS.GI.APP.WORK.UNIT.PRICE.RESERVED6` | `FsGiAppWorkUnitPrice_Reserved6` | TField |  |  |
| 10 | `FS.GI.APP.WORK.UNIT.PRICE.RESERVED5` | `FsGiAppWorkUnitPrice_Reserved5` | TField |  |  |
| 11 | `FS.GI.APP.WORK.UNIT.PRICE.RESERVED4` | `FsGiAppWorkUnitPrice_Reserved4` | TField |  |  |
| 12 | `FS.GI.APP.WORK.UNIT.PRICE.RESERVED3` | `FsGiAppWorkUnitPrice_Reserved3` | TField |  |  |
| 13 | `FS.GI.APP.WORK.UNIT.PRICE.RESERVED2` | `FsGiAppWorkUnitPrice_Reserved2` | TField |  |  |
| 14 | `FS.GI.APP.WORK.UNIT.PRICE.RESERVED1` | `FsGiAppWorkUnitPrice_Reserved1` | TField |  |  |
| 15 | `FS.GI.APP.WORK.UNIT.PRICE.LOCAL.REF` | `FsGiAppWorkUnitPrice_LocalRef` |  |  |  |
| 16 | `FS.GI.APP.WORK.UNIT.PRICE.OVERRIDE` | `FsGiAppWorkUnitPrice_Override` |  |  |  |
| 17 | `FS.GI.APP.WORK.UNIT.PRICE.RECORD.STATUS` | `FsGiAppWorkUnitPrice_RecordStatus` | String |  |  |
| 18 | `FS.GI.APP.WORK.UNIT.PRICE.CURR.NO` | `FsGiAppWorkUnitPrice_CurrNo` | String |  |  |
| 19 | `FS.GI.APP.WORK.UNIT.PRICE.INPUTTER` | `FsGiAppWorkUnitPrice_Inputter` |  |  |  |
| 20 | `FS.GI.APP.WORK.UNIT.PRICE.DATE.TIME` | `FsGiAppWorkUnitPrice_DateTime` |  |  |  |
| 21 | `FS.GI.APP.WORK.UNIT.PRICE.AUTHORISER` | `FsGiAppWorkUnitPrice_Authoriser` | String |  |  |
| 22 | `FS.GI.APP.WORK.UNIT.PRICE.CO.CODE` | `FsGiAppWorkUnitPrice_CoCode` | String |  |  |
| 23 | `FS.GI.APP.WORK.UNIT.PRICE.DEPT.CODE` | `FsGiAppWorkUnitPrice_DeptCode` | String |  |  |
| 24 | `FS.GI.APP.WORK.UNIT.PRICE.AUDITOR.CODE` | `FsGiAppWorkUnitPrice_AuditorCode` | String |  |  |
| 25 | `FS.GI.APP.WORK.UNIT.PRICE.AUDIT.DATE.TIME` | `FsGiAppWorkUnitPrice_AuditDateTime` | String |  |  |
