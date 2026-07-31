# FS.GA.GROUP.FOREXRATE.MANAGEMENT — Table Schema

> Source: `INSERTS/I_F.FS.GA.GROUP.FOREXRATE.MANAGEMENT` in `FS_PricesRates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.GROUP` | `FsGaGroupForexrateManagement_Group` | TField |  | Group Multifonds DB Column is GROUPE. |
| 2 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.EFFECTIVE.DATE` | `FsGaGroupForexrateManagement_EffectiveDate` | TField |  | Effective date to be applied. Multifonds DB Column is DATE_EFFECTIVE. |
| 3 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.BOOK.CURRENCY` | `FsGaGroupForexrateManagement_BookCurrency` | TField |  | Currency for expressing exchange rate. Also used to denote currency for various reporting. Multifonds DB Column is CMONREF. |
| 4 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.APPLICATION.CCY.FLAG` | `FsGaGroupForexrateManagement_ApplicationCcyFlag` | TField |  | Flag the application currency record Multifonds DB Column is FLG_APPL_CRANG. |
| 5 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.TECHNICAL.CURRENCY` | `FsGaGroupForexrateManagement_TechnicalCurrency` | TField |  | To set this box only if the "Application ccy" used in this screen is a dummy currency. Multifonds DB Column is FLG_TECH_CCY. |
| 6 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.DISPLAY.CURRENCY` | `FsGaGroupForexrateManagement_DisplayCurrency` | TField |  | Works along with the "Technical currency" check box. The currency listed is the actual currency in use and will be displayed in all the reports. Multifonds DB Column is CMONREF_ORIG. |
| 7 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.RESERVED10` | `FsGaGroupForexrateManagement_Reserved10` | TField |  |  |
| 8 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.RESERVED9` | `FsGaGroupForexrateManagement_Reserved9` | TField |  |  |
| 9 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.RESERVED8` | `FsGaGroupForexrateManagement_Reserved8` | TField |  |  |
| 10 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.RESERVED7` | `FsGaGroupForexrateManagement_Reserved7` | TField |  |  |
| 11 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.RESERVED6` | `FsGaGroupForexrateManagement_Reserved6` | TField |  |  |
| 12 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.RESERVED5` | `FsGaGroupForexrateManagement_Reserved5` | TField |  |  |
| 13 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.RESERVED4` | `FsGaGroupForexrateManagement_Reserved4` | TField |  |  |
| 14 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.RESERVED3` | `FsGaGroupForexrateManagement_Reserved3` | TField |  |  |
| 15 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.RESERVED2` | `FsGaGroupForexrateManagement_Reserved2` | TField |  |  |
| 16 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.RESERVED1` | `FsGaGroupForexrateManagement_Reserved1` | TField |  |  |
| 17 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.RECORD.STATUS` | `FsGaGroupForexrateManagement_RecordStatus` | String |  |  |
| 18 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.CURR.NO` | `FsGaGroupForexrateManagement_CurrNo` | String |  |  |
| 19 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.INPUTTER` | `FsGaGroupForexrateManagement_Inputter` |  |  |  |
| 20 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.DATE.TIME` | `FsGaGroupForexrateManagement_DateTime` |  |  |  |
| 21 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.AUTHORISER` | `FsGaGroupForexrateManagement_Authoriser` | String |  |  |
| 22 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.CO.CODE` | `FsGaGroupForexrateManagement_CoCode` | String |  |  |
| 23 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.DEPT.CODE` | `FsGaGroupForexrateManagement_DeptCode` | String |  |  |
| 24 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.AUDITOR.CODE` | `FsGaGroupForexrateManagement_AuditorCode` | String |  |  |
| 25 | `FS.GA.GROUP.FOREXRATE.MANAGEMENT.AUDIT.DATE.TIME` | `FsGaGroupForexrateManagement_AuditDateTime` | String |  |  |
