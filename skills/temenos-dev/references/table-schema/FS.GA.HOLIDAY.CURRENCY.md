# FS.GA.HOLIDAY.CURRENCY — Table Schema

> Source: `INSERTS/I_F.FS.GA.HOLIDAY.CURRENCY` in `FS_SystemConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.HOLIDAY.CURRENCY.PARENT.REF.ID` | `FsGaHolidayCurrency_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.HOLIDAY.CURRENCY.ORA.ROWID` | `FsGaHolidayCurrency_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.HOLIDAY.CURRENCY.LOCAL.CURRENCY` | `FsGaHolidayCurrency_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 4 | `FS.GA.HOLIDAY.CURRENCY.LEGAL.HOLIDAY` | `FsGaHolidayCurrency_LegalHoliday` | TField |  | Legal Holiday Multifonds DB Column is DJOURS_FERIE. |
| 5 | `FS.GA.HOLIDAY.CURRENCY.DESCRIPTION` | `FsGaHolidayCurrency_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 6 | `FS.GA.HOLIDAY.CURRENCY.RESERVED10` | `FsGaHolidayCurrency_Reserved10` | TField |  |  |
| 7 | `FS.GA.HOLIDAY.CURRENCY.RESERVED9` | `FsGaHolidayCurrency_Reserved9` | TField |  |  |
| 8 | `FS.GA.HOLIDAY.CURRENCY.RESERVED8` | `FsGaHolidayCurrency_Reserved8` | TField |  |  |
| 9 | `FS.GA.HOLIDAY.CURRENCY.RESERVED7` | `FsGaHolidayCurrency_Reserved7` | TField |  |  |
| 10 | `FS.GA.HOLIDAY.CURRENCY.RESERVED6` | `FsGaHolidayCurrency_Reserved6` | TField |  |  |
| 11 | `FS.GA.HOLIDAY.CURRENCY.RESERVED5` | `FsGaHolidayCurrency_Reserved5` | TField |  |  |
| 12 | `FS.GA.HOLIDAY.CURRENCY.RESERVED4` | `FsGaHolidayCurrency_Reserved4` | TField |  |  |
| 13 | `FS.GA.HOLIDAY.CURRENCY.RESERVED3` | `FsGaHolidayCurrency_Reserved3` | TField |  |  |
| 14 | `FS.GA.HOLIDAY.CURRENCY.RESERVED2` | `FsGaHolidayCurrency_Reserved2` | TField |  |  |
| 15 | `FS.GA.HOLIDAY.CURRENCY.RESERVED1` | `FsGaHolidayCurrency_Reserved1` | TField |  |  |
| 16 | `FS.GA.HOLIDAY.CURRENCY.LOCAL.REF` | `FsGaHolidayCurrency_LocalRef` |  |  |  |
| 17 | `FS.GA.HOLIDAY.CURRENCY.OVERRIDE` | `FsGaHolidayCurrency_Override` |  |  |  |
| 18 | `FS.GA.HOLIDAY.CURRENCY.RECORD.STATUS` | `FsGaHolidayCurrency_RecordStatus` | String |  |  |
| 19 | `FS.GA.HOLIDAY.CURRENCY.CURR.NO` | `FsGaHolidayCurrency_CurrNo` | String |  |  |
| 20 | `FS.GA.HOLIDAY.CURRENCY.INPUTTER` | `FsGaHolidayCurrency_Inputter` |  |  |  |
| 21 | `FS.GA.HOLIDAY.CURRENCY.DATE.TIME` | `FsGaHolidayCurrency_DateTime` |  |  |  |
| 22 | `FS.GA.HOLIDAY.CURRENCY.AUTHORISER` | `FsGaHolidayCurrency_Authoriser` | String |  |  |
| 23 | `FS.GA.HOLIDAY.CURRENCY.CO.CODE` | `FsGaHolidayCurrency_CoCode` | String |  |  |
| 24 | `FS.GA.HOLIDAY.CURRENCY.DEPT.CODE` | `FsGaHolidayCurrency_DeptCode` | String |  |  |
| 25 | `FS.GA.HOLIDAY.CURRENCY.AUDITOR.CODE` | `FsGaHolidayCurrency_AuditorCode` | String |  |  |
| 26 | `FS.GA.HOLIDAY.CURRENCY.AUDIT.DATE.TIME` | `FsGaHolidayCurrency_AuditDateTime` | String |  |  |
