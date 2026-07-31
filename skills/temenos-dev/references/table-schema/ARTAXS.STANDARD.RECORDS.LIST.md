# ARTAXS.STANDARD.RECORDS.LIST — Table Schema

> Source: `INSERTS/I_F.ARTAXS.STANDARD.RECORDS.LIST` in `ARTAXS_TaxCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RECORDS.LIST.PRODUCT` | `ArtaxsStandardRecordsList_Product` |  |  |  |
| 2 | `RECORDS.LIST.PROPERTY` | `ArtaxsStandardRecordsList_Property` |  |  |  |
| 3 | `RECORDS.LIST.ACTIVITY` | `ArtaxsStandardRecordsList_Activity` |  |  |  |
| 4 | `RECORDS.LIST.RESERVED.15` | `ArtaxsStandardRecordsList_Reserved15` | TField |  | Field reserved for future use. |
| 5 | `RECORDS.LIST.RESERVED.14` | `ArtaxsStandardRecordsList_Reserved14` | TField |  | Field reserved for future use. |
| 6 | `RECORDS.LIST.RESERVED.13` | `ArtaxsStandardRecordsList_Reserved13` | TField |  | Field reserved for future use. |
| 7 | `RECORDS.LIST.RESERVED.12` | `ArtaxsStandardRecordsList_Reserved12` | TField |  | Field reserved for future use. |
| 8 | `RECORDS.LIST.RESERVED.11` | `ArtaxsStandardRecordsList_Reserved11` | TField |  | Field reserved for future use. |
| 9 | `RECORDS.LIST.RESERVED.10` | `ArtaxsStandardRecordsList_Reserved10` | TField |  | Field reserved for future use. |
| 10 | `RECORDS.LIST.RESERVED.9` | `ArtaxsStandardRecordsList_Reserved9` | TField |  | Field reserved for future use. |
| 11 | `RECORDS.LIST.RESERVED.8` | `ArtaxsStandardRecordsList_Reserved8` | TField |  | Field reserved for future use. |
| 12 | `RECORDS.LIST.RESERVED.7` | `ArtaxsStandardRecordsList_Reserved7` | TField |  | Field reserved for future use. |
| 13 | `RECORDS.LIST.RESERVED.6` | `ArtaxsStandardRecordsList_Reserved6` | TField |  | Field reserved for future use. |
| 14 | `RECORDS.LIST.RESERVED.5` | `ArtaxsStandardRecordsList_Reserved5` | TField |  | Field reserved for future use. |
| 15 | `RECORDS.LIST.RESERVED.4` | `ArtaxsStandardRecordsList_Reserved4` | TField |  | Field reserved for future use. |
| 16 | `RECORDS.LIST.RESERVED.3` | `ArtaxsStandardRecordsList_Reserved3` | TField |  | Field reserved for future use. |
| 17 | `RECORDS.LIST.RESERVED.2` | `ArtaxsStandardRecordsList_Reserved2` | TField |  | Field reserved for future use. |
| 18 | `RECORDS.LIST.RESERVED.1` | `ArtaxsStandardRecordsList_Reserved1` | TField |  | Field reserved for future use. |
| 19 | `RECORDS.LIST.LOCAL.REF` | `ArtaxsStandardRecordsList_LocalRef` |  |  |  |
| 20 | `RECORDS.LIST.OVERRIDE` | `ArtaxsStandardRecordsList_Override` |  |  |  |
| 21 | `RECORDS.LIST.RECORD.STATUS` | `ArtaxsStandardRecordsList_RecordStatus` | String |  |  |
| 22 | `RECORDS.LIST.CURR.NO` | `ArtaxsStandardRecordsList_CurrNo` | String |  |  |
| 23 | `RECORDS.LIST.INPUTTER` | `ArtaxsStandardRecordsList_Inputter` |  |  |  |
| 24 | `RECORDS.LIST.DATE.TIME` | `ArtaxsStandardRecordsList_DateTime` |  |  |  |
| 25 | `RECORDS.LIST.AUTHORISER` | `ArtaxsStandardRecordsList_Authoriser` | String |  |  |
| 26 | `RECORDS.LIST.CO.CODE` | `ArtaxsStandardRecordsList_CoCode` | String |  |  |
| 27 | `RECORDS.LIST.DEPT.CODE` | `ArtaxsStandardRecordsList_DeptCode` | String |  |  |
| 28 | `RECORDS.LIST.AUDITOR.CODE` | `ArtaxsStandardRecordsList_AuditorCode` | String |  |  |
| 29 | `RECORDS.LIST.AUDIT.DATE.TIME` | `ArtaxsStandardRecordsList_AuditDateTime` | String |  |  |
