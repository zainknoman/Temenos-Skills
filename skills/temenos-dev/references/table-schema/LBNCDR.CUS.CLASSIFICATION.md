# LBNCDR.CUS.CLASSIFICATION — Table Schema

> Source: `INSERTS/I_F.LBNCDR.CUS.CLASSIFICATION` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.CUS.DESCRIPTION` | `LbncdrCusClassification_Description` | TField | Yes | This Multi value field hold the Description of Customer Classification details Validation Rules : Mandatory field, Type : A Length :65.1 |
| 2 | `LBNCDR.CUS.BDL.RATING` | `LbncdrCusClassification_BdlRating` | TField |  | This BDL Rating field hold the Rating for the Customer Validation Rules : Single value field, Type : N Length :3 |
| 3 | `LBNCDR.CUS.JUDICIAL.STATUS` | `LbncdrCusClassification_JudicialStatus` | TField |  |  |
| 4 | `LBNCDR.CUS.RESERVED.1` | `LbncdrCusClassification_Reserved1` | TField |  |  |
| 5 | `LBNCDR.CUS.RESERVED.2` | `LbncdrCusClassification_Reserved2` | TField |  |  |
| 6 | `LBNCDR.CUS.RESERVED.3` | `LbncdrCusClassification_Reserved3` | TField |  |  |
| 7 | `LBNCDR.CUS.RESERVED.4` | `LbncdrCusClassification_Reserved4` | TField |  |  |
| 8 | `LBNCDR.CUS.RESERVED.5` | `LbncdrCusClassification_Reserved5` | TField |  |  |
| 9 | `LBNCDR.CUS.LOCAL.REF` | `LbncdrCusClassification_LocalRef` |  |  |  |
| 10 | `LBNCDR.CUS.OVERRIDE` | `LbncdrCusClassification_Override` |  |  |  |
| 11 | `LBNCDR.CUS.RECORD.STATUS` | `LbncdrCusClassification_RecordStatus` | String |  |  |
| 12 | `LBNCDR.CUS.CURR.NO` | `LbncdrCusClassification_CurrNo` | String |  |  |
| 13 | `LBNCDR.CUS.INPUTTER` | `LbncdrCusClassification_Inputter` |  |  |  |
| 14 | `LBNCDR.CUS.DATE.TIME` | `LbncdrCusClassification_DateTime` |  |  |  |
| 15 | `LBNCDR.CUS.AUTHORISER` | `LbncdrCusClassification_Authoriser` | String |  |  |
| 16 | `LBNCDR.CUS.CO.CODE` | `LbncdrCusClassification_CoCode` | String |  |  |
| 17 | `LBNCDR.CUS.DEPT.CODE` | `LbncdrCusClassification_DeptCode` | String |  |  |
| 18 | `LBNCDR.CUS.AUDITOR.CODE` | `LbncdrCusClassification_AuditorCode` | String |  |  |
| 19 | `LBNCDR.CUS.AUDIT.DATE.TIME` | `LbncdrCusClassification_AuditDateTime` | String |  |  |
