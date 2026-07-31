# PSD.REPORT — Table Schema

> Source: `INSERTS/I_F.PSD.REPORT` in `PX_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PSD.REP.DATE` | `PsdReport_Date` | TField |  |  |
| 2 | `PSD.REP.TIME` | `PsdReport_Time` | TField |  |  |
| 3 | `PSD.REP.MODUL` | `PsdReport_Modul` | TField |  |  |
| 4 | `PSD.REP.TXN.REF` | `PsdReport_TxnRef` | TField |  |  |
| 5 | `PSD.REP.DATE.LAST.INFO` | `PsdReport_DateLastInfo` | TField |  |  |
| 6 | `PSD.REP.STATUS` | `PsdReport_Status` | TField |  |  |
| 7 | `PSD.REP.FLAG` | `PsdReport_Flag` | TField |  |  |
| 8 | `PSD.REP.NARRATIVE` | `PsdReport_Narrative` |  |  |  |
| 9 | `PSD.REP.PSD.CATEG` | `PsdReport_PsdCateg` | TField |  |  |
| 10 | `PSD.REP.RESERVED10` | `PsdReport_Reserved10` | TField |  |  |
| 11 | `PSD.REP.RESERVED09` | `PsdReport_Reserved09` | TField |  |  |
| 12 | `PSD.REP.RESERVED08` | `PsdReport_Reserved08` | TField |  |  |
| 13 | `PSD.REP.RESERVED07` | `PsdReport_Reserved07` | TField |  |  |
| 14 | `PSD.REP.RESERVED06` | `PsdReport_Reserved06` | TField |  |  |
| 15 | `PSD.REP.RESERVED05` | `PsdReport_Reserved05` | TField |  |  |
| 16 | `PSD.REP.RESERVED04` | `PsdReport_Reserved04` | TField |  |  |
| 17 | `PSD.REP.RESERVED03` | `PsdReport_Reserved03` | TField |  |  |
| 18 | `PSD.REP.RESERVED02` | `PsdReport_Reserved02` | TField |  |  |
| 19 | `PSD.REP.RESERVED01` | `PsdReport_Reserved01` | TField |  |  |
| 20 | `PSD.REP.LOCAL.REF` | `PsdReport_LocalRef` |  |  |  |
| 21 | `PSD.REP.OVERRIDE` | `PsdReport_Override` |  |  |  |
| 22 | `PSD.REP.RECORD.STATUS` | `PsdReport_RecordStatus` | String |  |  |
| 23 | `PSD.REP.CURR.NO` | `PsdReport_CurrNo` | String |  |  |
| 24 | `PSD.REP.INPUTTER` | `PsdReport_Inputter` |  |  |  |
| 25 | `PSD.REP.DATE.TIME` | `PsdReport_DateTime` |  |  |  |
| 26 | `PSD.REP.AUTHORISER` | `PsdReport_Authoriser` | String |  |  |
| 27 | `PSD.REP.CO.CODE` | `PsdReport_CoCode` | String |  |  |
| 28 | `PSD.REP.DEPT.CODE` | `PsdReport_DeptCode` | String |  |  |
| 29 | `PSD.REP.AUDITOR.CODE` | `PsdReport_AuditorCode` | String |  |  |
| 30 | `PSD.REP.AUDIT.DATE.TIME` | `PsdReport_AuditDateTime` | String |  |  |
