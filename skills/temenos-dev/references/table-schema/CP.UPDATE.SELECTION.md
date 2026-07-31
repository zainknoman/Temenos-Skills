# CP.UPDATE.SELECTION — Table Schema

> Source: `INSERTS/I_F.CP.UPDATE.SELECTION` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.US.OPERATION.TYPE` | `CpUpdateSelection_OperationType` | TField | Yes | This field stores the type of the operation is taken for the given idsExamples: SUSPEND, RESTART Validation Rules: Mandatory field. |
| 2 | `CP.US.APPLICATION.NAME` | `CpUpdateSelection_ApplicationName` | TField | Yes | This field stores the name of the application where the records are found. Validation Rules: Mandatory field. |
| 3 | `CP.US.SELECT.LIST` | `CpUpdateSelection_SelectList` |  |  |  |
| 4 | `CP.US.FIELD.NAME` | `CpUpdateSelection_FieldName` |  |  |  |
| 5 | `CP.US.FIELD.VALUE` | `CpUpdateSelection_FieldValue` |  |  |  |
| 6 | `CP.US.RESERVED.10` | `CpUpdateSelection_Reserved10` | TField |  |  |
| 7 | `CP.US.RESERVED.9` | `CpUpdateSelection_Reserved9` | TField |  |  |
| 8 | `CP.US.RESERVED.8` | `CpUpdateSelection_Reserved8` | TField |  |  |
| 9 | `CP.US.RESERVED.7` | `CpUpdateSelection_Reserved7` | TField |  |  |
| 10 | `CP.US.RESERVED.6` | `CpUpdateSelection_Reserved6` | TField |  |  |
| 11 | `CP.US.RESERVED.5` | `CpUpdateSelection_Reserved5` | TField |  |  |
| 12 | `CP.US.RESERVED.4` | `CpUpdateSelection_Reserved4` | TField |  |  |
| 13 | `CP.US.RESERVED.3` | `CpUpdateSelection_Reserved3` | TField |  |  |
| 14 | `CP.US.RESERVED.2` | `CpUpdateSelection_Reserved2` | TField |  |  |
| 15 | `CP.US.RESERVED.1` | `CpUpdateSelection_Reserved1` | TField |  |  |
| 16 | `CP.US.LOCAL.REF` | `CpUpdateSelection_LocalRef` |  |  |  |
| 17 | `CP.US.OVERRIDE` | `CpUpdateSelection_Override` |  |  |  |
| 18 | `CP.US.RECORD.STATUS` | `CpUpdateSelection_RecordStatus` | String |  |  |
| 19 | `CP.US.CURR.NO` | `CpUpdateSelection_CurrNo` | String |  |  |
| 20 | `CP.US.INPUTTER` | `CpUpdateSelection_Inputter` |  |  |  |
| 21 | `CP.US.DATE.TIME` | `CpUpdateSelection_DateTime` |  |  |  |
| 22 | `CP.US.AUTHORISER` | `CpUpdateSelection_Authoriser` | String |  |  |
| 23 | `CP.US.CO.CODE` | `CpUpdateSelection_CoCode` | String |  |  |
| 24 | `CP.US.DEPT.CODE` | `CpUpdateSelection_DeptCode` | String |  |  |
| 25 | `CP.US.AUDITOR.CODE` | `CpUpdateSelection_AuditorCode` | String |  |  |
| 26 | `CP.US.AUDIT.DATE.TIME` | `CpUpdateSelection_AuditDateTime` | String |  |  |
