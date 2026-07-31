# EB.PREDEFINE.CONTRACTS — Table Schema

> Source: `INSERTS/I_F.EB.PREDEFINE.CONTRACTS` in `EB_Service.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PRE.CON.DESCRIPTION` | `EbPredefineContracts_Description` | A (alphanumeric) | Yes | Describes this record, which can be used for reporting. Validation Rules: Up to 35 type A (alphanumeric) characters. Mandatory input. No default value |
| 2 | `PRE.CON.RESERVED.15` | `EbPredefineContracts_Reserved15` | TField |  |  |
| 3 | `PRE.CON.RESERVED.14` | `EbPredefineContracts_Reserved14` | TField |  |  |
| 4 | `PRE.CON.RESERVED.13` | `EbPredefineContracts_Reserved13` | TField |  |  |
| 5 | `PRE.CON.RESERVED.12` | `EbPredefineContracts_Reserved12` | TField |  |  |
| 6 | `PRE.CON.RESERVED.11` | `EbPredefineContracts_Reserved11` | TField |  |  |
| 7 | `PRE.CON.BUSINESS.CASE` | `EbPredefineContracts_BusinessCase` |  |  |  |
| 8 | `PRE.CON.CONTRACTS` | `EbPredefineContracts_Contracts` |  |  |  |
| 9 | `PRE.CON.RESERVED.10` | `EbPredefineContracts_Reserved10` |  |  |  |
| 10 | `PRE.CON.RESERVED.9` | `EbPredefineContracts_Reserved9` |  |  |  |
| 11 | `PRE.CON.RESERVED.8` | `EbPredefineContracts_Reserved8` |  |  |  |
| 12 | `PRE.CON.RESERVED.7` | `EbPredefineContracts_Reserved7` |  |  |  |
| 13 | `PRE.CON.RESERVED.6` | `EbPredefineContracts_Reserved6` |  |  |  |
| 14 | `PRE.CON.RESERVED.5` | `EbPredefineContracts_Reserved5` |  |  |  |
| 15 | `PRE.CON.DATE.PROCESSED` | `EbPredefineContracts_DateProcessed` | TField |  | This field is updated with TODAY date when the EB.PREDEFINE.PROCESSING service triggers the JOB in the ID and gets completed. Validation Rules: NOINPUT field updated by the SYSTEM |
| 16 | `PRE.CON.RESERVED.4` | `EbPredefineContracts_Reserved4` | TField |  |  |
| 17 | `PRE.CON.RESERVED.3` | `EbPredefineContracts_Reserved3` | TField |  |  |
| 18 | `PRE.CON.RESERVED.2` | `EbPredefineContracts_Reserved2` | TField |  |  |
| 19 | `PRE.CON.RESERVED.1` | `EbPredefineContracts_Reserved1` | TField |  |  |
| 20 | `PRE.CON.RESERVED.0` | `EbPredefineContracts_Reserved0` | TField |  |  |
| 21 | `PRE.CON.LOCAL.REF` | `EbPredefineContracts_LocalRef` |  |  |  |
| 22 | `PRE.CON.OVERRIDE` | `EbPredefineContracts_Override` |  |  |  |
| 23 | `PRE.CON.RECORD.STATUS` | `EbPredefineContracts_RecordStatus` | String |  |  |
| 24 | `PRE.CON.CURR.NO` | `EbPredefineContracts_CurrNo` | String |  |  |
| 25 | `PRE.CON.INPUTTER` | `EbPredefineContracts_Inputter` |  |  |  |
| 26 | `PRE.CON.DATE.TIME` | `EbPredefineContracts_DateTime` |  |  |  |
| 27 | `PRE.CON.AUTHORISER` | `EbPredefineContracts_Authoriser` | String |  |  |
| 28 | `PRE.CON.CO.CODE` | `EbPredefineContracts_CoCode` | String |  |  |
| 29 | `PRE.CON.DEPT.CODE` | `EbPredefineContracts_DeptCode` | String |  |  |
| 30 | `PRE.CON.AUDITOR.CODE` | `EbPredefineContracts_AuditorCode` | String |  |  |
| 31 | `PRE.CON.AUDIT.DATE.TIME` | `EbPredefineContracts_AuditDateTime` | String |  |  |
