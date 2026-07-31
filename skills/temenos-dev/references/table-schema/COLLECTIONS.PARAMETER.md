# COLLECTIONS.PARAMETER — Table Schema

> Source: `INSERTS/I_F.COLLECTIONS.PARAMETER` in `USLEND_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COL.PARAM.DESCRIPTION` | `CollectionsParameter_Description` |  |  |  |
| 2 | `COL.PARAM.CREDIT.AGENCY` | `CollectionsParameter_CreditAgency` | TField |  | Credit bureau or Agency whose Credit score will be returned to the extract file. Linked to lookup CREDIT.BUREAU . 15 chars |
| 3 | `COL.PARAM.RESERVED.20` | `CollectionsParameter_Reserved20` | TField |  | Reserved Field. |
| 4 | `COL.PARAM.RESERVED.19` | `CollectionsParameter_Reserved19` | TField |  | Reserved Field. |
| 5 | `COL.PARAM.RESERVED.18` | `CollectionsParameter_Reserved18` | TField |  | Reserved Field. |
| 6 | `COL.PARAM.RESERVED.17` | `CollectionsParameter_Reserved17` | TField |  | Reserved Field. |
| 7 | `COL.PARAM.RESERVED.16` | `CollectionsParameter_Reserved16` | TField |  | Reserved Field. |
| 8 | `COL.PARAM.RESERVED.15` | `CollectionsParameter_Reserved15` | TField |  | Reserved Field. |
| 9 | `COL.PARAM.RESERVED.14` | `CollectionsParameter_Reserved14` | TField |  | Reserved Field. |
| 10 | `COL.PARAM.RESERVED.13` | `CollectionsParameter_Reserved13` | TField |  | Reserved Field. |
| 11 | `COL.PARAM.RESERVED.12` | `CollectionsParameter_Reserved12` | TField |  | Reserved Field. |
| 12 | `COL.PARAM.RESERVED.11` | `CollectionsParameter_Reserved11` | TField |  | Reserved Field. |
| 13 | `COL.PARAM.RESERVED.10` | `CollectionsParameter_Reserved10` | TField |  | Reserved Field. |
| 14 | `COL.PARAM.RESERVED.09` | `CollectionsParameter_Reserved09` | TField |  |  |
| 15 | `COL.PARAM.RESERVED.08` | `CollectionsParameter_Reserved08` | TField |  |  |
| 16 | `COL.PARAM.RESERVED.07` | `CollectionsParameter_Reserved07` | TField |  |  |
| 17 | `COL.PARAM.RESERVED.06` | `CollectionsParameter_Reserved06` | TField |  |  |
| 18 | `COL.PARAM.RESERVED.05` | `CollectionsParameter_Reserved05` | TField |  |  |
| 19 | `COL.PARAM.RESERVED.04` | `CollectionsParameter_Reserved04` | TField |  |  |
| 20 | `COL.PARAM.RESERVED.03` | `CollectionsParameter_Reserved03` | TField |  |  |
| 21 | `COL.PARAM.RESERVED.02` | `CollectionsParameter_Reserved02` | TField |  |  |
| 22 | `COL.PARAM.RESERVED.01` | `CollectionsParameter_Reserved01` | TField |  |  |
| 23 | `COL.PARAM.LOCAL.REF` | `CollectionsParameter_LocalRef` |  |  |  |
| 24 | `COL.PARAM.RECORD.STATUS` | `CollectionsParameter_RecordStatus` | String |  |  |
| 25 | `COL.PARAM.CURR.NO` | `CollectionsParameter_CurrNo` | String |  |  |
| 26 | `COL.PARAM.INPUTTER` | `CollectionsParameter_Inputter` |  |  |  |
| 27 | `COL.PARAM.DATE.TIME` | `CollectionsParameter_DateTime` |  |  |  |
| 28 | `COL.PARAM.AUTHORISER` | `CollectionsParameter_Authoriser` | String |  |  |
| 29 | `COL.PARAM.CO.CODE` | `CollectionsParameter_CoCode` | String |  |  |
| 30 | `COL.PARAM.DEPT.CODE` | `CollectionsParameter_DeptCode` | String |  |  |
| 31 | `COL.PARAM.AUDITOR.CODE` | `CollectionsParameter_AuditorCode` | String |  |  |
| 32 | `COL.PARAM.AUDIT.DATE.TIME` | `CollectionsParameter_AuditDateTime` | String |  |  |
