# AM.NEW.MODEL — Table Schema

> Source: `INSERTS/I_F.AM.NEW.MODEL` in `AM_DynamicModelling.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.NM.SHORT.NAME` | `AmNewModel_ShortName` |  |  |  |
| 2 | `AM.NM.RESERVED10` | `AmNewModel_Reserved10` | TField |  |  |
| 3 | `AM.NM.DESCRIPTION` | `AmNewModel_Description` |  |  |  |
| 4 | `AM.NM.RESERVED09` | `AmNewModel_Reserved09` | TField |  |  |
| 5 | `AM.NM.REFERENCE.CCY` | `AmNewModel_ReferenceCcy` | TField |  | The reference currency for the model Must be a valid currency (i.e. a valid CURRENCY record id). All nodes within this hierarchy must share the same reference currency. Once this has been input it cannot be changed. |
| 6 | `AM.NM.RESERVED08` | `AmNewModel_Reserved08` | TField |  |  |
| 7 | `AM.NM.BASE.OVERLAY` | `AmNewModel_BaseOverlay` | TField |  | the hierarchy for the model is generated based on this field It should contain a valid record in AM.SEGMENTED.HIERARCHY |
| 8 | `AM.NM.RESERVED07` | `AmNewModel_Reserved07` | TField |  |  |
| 9 | `AM.NM.MODEL.TYPE` | `AmNewModel_ModelType` | TField |  | this field describes type of the model to be generated in AM.DYNAMIC.MODEL input could be DYNAMIC or STATIC |
| 10 | `AM.NM.VALUE.TYPE` | `AmNewModel_ValueType` | TField |  | this field depends on the MODEL.TYPE field if MODEL.TYPE = DYNAMIC then value of this field is NOMINAL if MODEL.TYPE = STATIC then value of this field is PERCENTAGE |
| 11 | `AM.NM.MODEL.ID` | `AmNewModel_ModelId` | TField |  | ID for the record to be created in respective model |
| 12 | `AM.NM.RESERVED05` | `AmNewModel_Reserved05` | TField |  |  |
| 13 | `AM.NM.LIVE.DATE` | `AmNewModel_LiveDate` | TField |  | date for the model record should not be less than current date |
| 14 | `AM.NM.RESERVED03` | `AmNewModel_Reserved03` | TField |  |  |
| 15 | `AM.NM.RESERVED02` | `AmNewModel_Reserved02` | TField |  |  |
| 16 | `AM.NM.RESERVED01` | `AmNewModel_Reserved01` | TField |  |  |
| 17 | `AM.NM.RESERVED00` | `AmNewModel_Reserved00` | TField |  |  |
| 18 | `AM.NM.LOCAL.REF` | `AmNewModel_LocalRef` |  |  |  |
| 19 | `AM.NM.OVERRIDE` | `AmNewModel_Override` | TField |  |  |
| 20 | `AM.NM.RECORD.STATUS` | `AmNewModel_RecordStatus` | String |  |  |
| 21 | `AM.NM.CURR.NO` | `AmNewModel_CurrNo` | String |  |  |
| 22 | `AM.NM.INPUTTER` | `AmNewModel_Inputter` |  |  |  |
| 23 | `AM.NM.DATE.TIME` | `AmNewModel_DateTime` |  |  |  |
| 24 | `AM.NM.AUTHORISER` | `AmNewModel_Authoriser` | String |  |  |
| 25 | `AM.NM.CO.CODE` | `AmNewModel_CoCode` | String |  |  |
| 26 | `AM.NM.DEPT.CODE` | `AmNewModel_DeptCode` | String |  |  |
| 27 | `AM.NM.AUDITOR.CODE` | `AmNewModel_AuditorCode` | String |  |  |
| 28 | `AM.NM.AUDIT.DATE.TIME` | `AmNewModel_AuditDateTime` | String |  |  |
