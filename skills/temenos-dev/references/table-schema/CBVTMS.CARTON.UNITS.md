# CBVTMS.CARTON.UNITS — Table Schema

> Source: `INSERTS/I_F.CBVTMS.CARTON.UNITS` in `CBVTMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `VTMS.DESCRIPTION` | `CbvtmsCartonUnits_Description` |  |  |  |
| 2 | `VTMS.CARTON.UNITS` | `CbvtmsCartonUnits_CartonUnits` | TField |  | The no of units of currency that makes the carton. |
| 3 | `VTMS.CARTON.TYPE` | `CbvtmsCartonUnits_CartonType` | TField |  | The type of carton that is used |
| 4 | `VTMS.NO.OF.CARTON` | `CbvtmsCartonUnits_NoOfCarton` | TField |  | The no of cartons that make the type of carton type |
| 5 | `VTMS.LOCAL.REF` | `CbvtmsCartonUnits_LocalRef` |  |  |  |
| 6 | `VTMS.RESERVED.5` | `CbvtmsCartonUnits_Reserved5` | TField |  | Reserved field for future use |
| 7 | `VTMS.RESERVED.4` | `CbvtmsCartonUnits_Reserved4` | TField |  | Reserved field for future use |
| 8 | `VTMS.RESERVED.3` | `CbvtmsCartonUnits_Reserved3` | TField |  | Reserved field for future use |
| 9 | `VTMS.RESERVED.2` | `CbvtmsCartonUnits_Reserved2` | TField |  | Reserved field for future use |
| 10 | `VTMS.RESERVED.1` | `CbvtmsCartonUnits_Reserved1` | TField |  | Reserved field for future use |
| 11 | `VTMS.OVERRIDE` | `CbvtmsCartonUnits_Override` |  |  |  |
| 12 | `VTMS.RECORD.STATUS` | `CbvtmsCartonUnits_RecordStatus` | String |  |  |
| 13 | `VTMS.CURR.NO` | `CbvtmsCartonUnits_CurrNo` | String |  |  |
| 14 | `VTMS.INPUTTER` | `CbvtmsCartonUnits_Inputter` |  |  |  |
| 15 | `VTMS.DATE.TIME` | `CbvtmsCartonUnits_DateTime` |  |  |  |
| 16 | `VTMS.AUTHORISER` | `CbvtmsCartonUnits_Authoriser` | String |  |  |
| 17 | `VTMS.CO.CODE` | `CbvtmsCartonUnits_CoCode` | String |  |  |
| 18 | `VTMS.DEPT.CODE` | `CbvtmsCartonUnits_DeptCode` | String |  |  |
| 19 | `VTMS.AUDITOR.CODE` | `CbvtmsCartonUnits_AuditorCode` | String |  |  |
| 20 | `VTMS.AUDIT.DATE.TIME` | `CbvtmsCartonUnits_AuditDateTime` | String |  |  |
