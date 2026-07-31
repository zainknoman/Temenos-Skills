# CP.OBJECTIVE — Table Schema

> Source: `INSERTS/I_F.CP.OBJECTIVE` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.OBJ.DESCRIPTION` | `CpObjective_Description` |  |  |  |
| 2 | `CP.OBJ.NAME` | `CpObjective_Name` | TField | Yes | This field stores the name of the objective. Validation Rules: Mandatory field, any 50 characters. |
| 3 | `CP.OBJ.LINKED.PRODUCT.GRP` | `CpObjective_LinkedProductGrp` | TField |  | This field stores "Y" and "N" values.It conditions whether or not a product group is linked to an objective."Y" indicates that a product group is linked to the defined objective while "N" indicates that one is not linked. |
| 4 | `CP.OBJ.AA.PRODUCT.GROUP` | `CpObjective_AaProductGroup` | TField |  | This field stores the ID of the product group which is linked to the defined objective.This field links the CP.OBJECTUVE table to the AA.PRODUCT.GROUP one. Validation Rules: 50 text characters. |
| 5 | `CP.OBJ.RESERVED.10` | `CpObjective_Reserved10` | TField |  |  |
| 6 | `CP.OBJ.RESERVED.9` | `CpObjective_Reserved9` | TField |  |  |
| 7 | `CP.OBJ.RESERVED.8` | `CpObjective_Reserved8` | TField |  |  |
| 8 | `CP.OBJ.RESERVED.7` | `CpObjective_Reserved7` | TField |  |  |
| 9 | `CP.OBJ.RESERVED.6` | `CpObjective_Reserved6` | TField |  |  |
| 10 | `CP.OBJ.RESERVED.5` | `CpObjective_Reserved5` | TField |  |  |
| 11 | `CP.OBJ.RESERVED.4` | `CpObjective_Reserved4` | TField |  |  |
| 12 | `CP.OBJ.RESERVED.3` | `CpObjective_Reserved3` | TField |  |  |
| 13 | `CP.OBJ.RESERVED.2` | `CpObjective_Reserved2` | TField |  |  |
| 14 | `CP.OBJ.RESERVED.1` | `CpObjective_Reserved1` | TField |  |  |
| 15 | `CP.OBJ.LOCAL.REF` | `CpObjective_LocalRef` |  |  |  |
| 16 | `CP.OBJ.OVERRIDE` | `CpObjective_Override` |  |  |  |
| 17 | `CP.OBJ.RECORD.STATUS` | `CpObjective_RecordStatus` | String |  |  |
| 18 | `CP.OBJ.CURR.NO` | `CpObjective_CurrNo` | String |  |  |
| 19 | `CP.OBJ.INPUTTER` | `CpObjective_Inputter` |  |  |  |
| 20 | `CP.OBJ.DATE.TIME` | `CpObjective_DateTime` |  |  |  |
| 21 | `CP.OBJ.AUTHORISER` | `CpObjective_Authoriser` | String |  |  |
| 22 | `CP.OBJ.CO.CODE` | `CpObjective_CoCode` | String |  |  |
| 23 | `CP.OBJ.DEPT.CODE` | `CpObjective_DeptCode` | String |  |  |
| 24 | `CP.OBJ.AUDITOR.CODE` | `CpObjective_AuditorCode` | String |  |  |
| 25 | `CP.OBJ.AUDIT.DATE.TIME` | `CpObjective_AuditDateTime` | String |  |  |
