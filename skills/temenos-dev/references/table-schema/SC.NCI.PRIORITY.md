# SC.NCI.PRIORITY — Table Schema

> Source: `INSERTS/I_F.SC.NCI.PRIORITY` in `SC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.NCI.COUNTRY.NAME` | `ScNciPriority_CountryName` |  |  |  |
| 2 | `SC.NCI.PRIORITY.IDENTIFIER` | `ScNciPriority_PriorityIdentifier` |  |  |  |
| 3 | `SC.NCI.NATIONAL.IDNTR.CODE` | `ScNciPriority_NationalIdntrCode` |  |  |  |
| 4 | `SC.NCI.RESERVED.15` | `ScNciPriority_Reserved15` | TField |  |  |
| 5 | `SC.NCI.RESERVED.14` | `ScNciPriority_Reserved14` | TField |  |  |
| 6 | `SC.NCI.RESERVED.13` | `ScNciPriority_Reserved13` | TField |  |  |
| 7 | `SC.NCI.RESERVED.12` | `ScNciPriority_Reserved12` | TField |  |  |
| 8 | `SC.NCI.RESERVED.11` | `ScNciPriority_Reserved11` | TField |  |  |
| 9 | `SC.NCI.RESERVED.10` | `ScNciPriority_Reserved10` | TField |  |  |
| 10 | `SC.NCI.RESERVED.9` | `ScNciPriority_Reserved9` | TField |  |  |
| 11 | `SC.NCI.RESERVED.8` | `ScNciPriority_Reserved8` | TField |  |  |
| 12 | `SC.NCI.RESERVED.7` | `ScNciPriority_Reserved7` | TField |  |  |
| 13 | `SC.NCI.RESERVED.6` | `ScNciPriority_Reserved6` | TField |  |  |
| 14 | `SC.NCI.RESERVED.5` | `ScNciPriority_Reserved5` | TField |  |  |
| 15 | `SC.NCI.RESERVED.4` | `ScNciPriority_Reserved4` | TField |  |  |
| 16 | `SC.NCI.RESERVED.3` | `ScNciPriority_Reserved3` | TField |  |  |
| 17 | `SC.NCI.RESERVED.2` | `ScNciPriority_Reserved2` | TField |  |  |
| 18 | `SC.NCI.RESERVED.1` | `ScNciPriority_Reserved1` | TField |  |  |
| 19 | `SC.NCI.LOCAL.REF` | `ScNciPriority_LocalRef` |  |  |  |
| 20 | `SC.NCI.OVERRIDE` | `ScNciPriority_Override` |  |  |  |
| 21 | `SC.NCI.RECORD.STATUS` | `ScNciPriority_RecordStatus` | String |  |  |
| 22 | `SC.NCI.CURR.NO` | `ScNciPriority_CurrNo` | String |  |  |
| 23 | `SC.NCI.INPUTTER` | `ScNciPriority_Inputter` |  |  |  |
| 24 | `SC.NCI.DATE.TIME` | `ScNciPriority_DateTime` |  |  |  |
| 25 | `SC.NCI.AUTHORISER` | `ScNciPriority_Authoriser` | String |  |  |
| 26 | `SC.NCI.CO.CODE` | `ScNciPriority_CoCode` | String |  |  |
| 27 | `SC.NCI.DEPT.CODE` | `ScNciPriority_DeptCode` | String |  |  |
| 28 | `SC.NCI.AUDITOR.CODE` | `ScNciPriority_AuditorCode` | String |  |  |
| 29 | `SC.NCI.AUDIT.DATE.TIME` | `ScNciPriority_AuditDateTime` | String |  |  |
| 30 | `SC.NCI.SRD.IDNTR.CODE` | `ScNciPriority_SrdIdntrCode` |  |  |  |
