# CP.GLOBAL.DETAILS — Table Schema

> Source: `INSERTS/I_F.CP.GLOBAL.DETAILS` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.GD.GLOBAL.EXCL` | `CpGlobalDetails_GlobalExcl` |  |  |  |
| 2 | `CP.GD.GLOBAL.CAMPAIGN` | `CpGlobalDetails_GlobalCampaign` |  |  |  |
| 3 | `CP.GD.GLOBAL.PRIORITY` | `CpGlobalDetails_GlobalPriority` |  |  |  |
| 4 | `CP.GD.STATUS.CODE` | `CpGlobalDetails_StatusCode` | TField | Yes | This field stores the values of the field STATUS.CODE from the table CP.ENTITY.WORKFLOW. Validation Rules :Mandatory field, any 100 characters. |
| 5 | `CP.GD.RULE.EVAL.TYPE` | `CpGlobalDetails_RuleEvalType` | TField |  | This field stores the type of evaluations |
| 6 | `CP.GD.STATUS.TYPE` | `CpGlobalDetails_StatusType` | TField |  | This field stores the Status type |
| 7 | `CP.GD.LAST.UPDATE` | `CpGlobalDetails_LastUpdate` | TField |  | This field stores the date of the last comment made for this record. |
| 8 | `CP.GD.SUSPEND.REASON.ID` | `CpGlobalDetails_SuspendReasonId` | TField |  | This field stores the SUSPEND.REASON record ID. If this field has a SuspendReasonId -> the record has suspended values on it. It can't be used until they are approved or removed from the record.While there is a value in SuspendReasonId, the record can't be moved in a next stage. |
| 9 | `CP.GD.WORKFLOW.ID` | `CpGlobalDetails_WorkflowId` | TField |  | This field stores the Workflow record ID. |
| 10 | `CP.GD.RESERVED.28` | `CpGlobalDetails_Reserved28` | TField |  |  |
| 11 | `CP.GD.RESERVED.27` | `CpGlobalDetails_Reserved27` | TField |  |  |
| 12 | `CP.GD.RESERVED.26` | `CpGlobalDetails_Reserved26` | TField |  |  |
| 13 | `CP.GD.RESERVED.25` | `CpGlobalDetails_Reserved25` | TField |  |  |
| 14 | `CP.GD.RESERVED.24` | `CpGlobalDetails_Reserved24` | TField |  |  |
| 15 | `CP.GD.RESERVED.23` | `CpGlobalDetails_Reserved23` | TField |  |  |
| 16 | `CP.GD.RESERVED.22` | `CpGlobalDetails_Reserved22` | TField |  |  |
| 17 | `CP.GD.RESERVED.21` | `CpGlobalDetails_Reserved21` | TField |  |  |
| 18 | `CP.GD.RESERVED.20` | `CpGlobalDetails_Reserved20` | TField |  |  |
| 19 | `CP.GD.RESERVED.19` | `CpGlobalDetails_Reserved19` | TField |  |  |
| 20 | `CP.GD.RESERVED.18` | `CpGlobalDetails_Reserved18` | TField |  |  |
| 21 | `CP.GD.RESERVED.17` | `CpGlobalDetails_Reserved17` | TField |  |  |
| 22 | `CP.GD.RESERVED.16` | `CpGlobalDetails_Reserved16` | TField |  |  |
| 23 | `CP.GD.RESERVED.15` | `CpGlobalDetails_Reserved15` | TField |  |  |
| 24 | `CP.GD.RESERVED.14` | `CpGlobalDetails_Reserved14` | TField |  |  |
| 25 | `CP.GD.RESERVED.13` | `CpGlobalDetails_Reserved13` | TField |  |  |
| 26 | `CP.GD.RESERVED.12` | `CpGlobalDetails_Reserved12` | TField |  |  |
| 27 | `CP.GD.RESERVED.11` | `CpGlobalDetails_Reserved11` | TField |  |  |
| 28 | `CP.GD.RESERVED.10` | `CpGlobalDetails_Reserved10` | TField |  |  |
| 29 | `CP.GD.RESERVED.9` | `CpGlobalDetails_Reserved9` | TField |  |  |
| 30 | `CP.GD.RESERVED.8` | `CpGlobalDetails_Reserved8` | TField |  |  |
| 31 | `CP.GD.RESERVED.7` | `CpGlobalDetails_Reserved7` | TField |  |  |
| 32 | `CP.GD.RESERVED.6` | `CpGlobalDetails_Reserved6` | TField |  |  |
| 33 | `CP.GD.RESERVED.5` | `CpGlobalDetails_Reserved5` | TField |  |  |
| 34 | `CP.GD.RESERVED.4` | `CpGlobalDetails_Reserved4` | TField |  |  |
| 35 | `CP.GD.RESERVED.3` | `CpGlobalDetails_Reserved3` | TField |  |  |
| 36 | `CP.GD.RESERVED.2` | `CpGlobalDetails_Reserved2` | TField |  |  |
| 37 | `CP.GD.RESERVED.1` | `CpGlobalDetails_Reserved1` | TField |  |  |
| 38 | `CP.GD.LOCAL.REF` | `CpGlobalDetails_LocalRef` |  |  |  |
| 39 | `CP.GD.OVERRIDE` | `CpGlobalDetails_Override` |  |  |  |
| 40 | `CP.GD.RECORD.STATUS` | `CpGlobalDetails_RecordStatus` | String |  |  |
| 41 | `CP.GD.CURR.NO` | `CpGlobalDetails_CurrNo` | String |  |  |
| 42 | `CP.GD.INPUTTER` | `CpGlobalDetails_Inputter` |  |  |  |
| 43 | `CP.GD.DATE.TIME` | `CpGlobalDetails_DateTime` |  |  |  |
| 44 | `CP.GD.AUTHORISER` | `CpGlobalDetails_Authoriser` | String |  |  |
| 45 | `CP.GD.CO.CODE` | `CpGlobalDetails_CoCode` | String |  |  |
| 46 | `CP.GD.DEPT.CODE` | `CpGlobalDetails_DeptCode` | String |  |  |
| 47 | `CP.GD.AUDITOR.CODE` | `CpGlobalDetails_AuditorCode` | String |  |  |
| 48 | `CP.GD.AUDIT.DATE.TIME` | `CpGlobalDetails_AuditDateTime` | String |  |  |
