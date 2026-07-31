# FS.GA.DUPLICATE.ID.CONTROL — Table Schema

> Source: `INSERTS/I_F.FS.GA.DUPLICATE.ID.CONTROL` in `FS_Controls.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GA.DUP.ID.CONTROL.IDENTIFIER.TYPE` | `FsGaDuplicateIdControl_IdentifierType` | TField |  | Corresponds to Identifier Code type like security,Future,option and Industry type Multifonds DB Column is ID_TYPE. |
| 2 | `GA.DUP.ID.CONTROL.PROVIDER.ID` | `FsGaDuplicateIdControl_ProviderId` | TField |  | Relates to Identifier codes of security,Provider,Thirdparty and industry etc Multifonds DB Column is ID_CODE. |
| 3 | `GA.DUP.ID.CONTROL.FLAG.NULL.VALUE.ALLOWED` | `FsGaDuplicateIdControl_FlagNullValueAllowed` | TField |  | This flag allows users to not parameterize an ID code in even if the duplicate control is activated for that ID code in the screen Multifonds DB Column is FLG_CHK_ID. |
| 4 | `GA.DUP.ID.CONTROL.RESERVED10` | `FsGaDuplicateIdControl_Reserved10` | TField |  |  |
| 5 | `GA.DUP.ID.CONTROL.RESERVED9` | `FsGaDuplicateIdControl_Reserved9` | TField |  |  |
| 6 | `GA.DUP.ID.CONTROL.RESERVED8` | `FsGaDuplicateIdControl_Reserved8` | TField |  |  |
| 7 | `GA.DUP.ID.CONTROL.RESERVED7` | `FsGaDuplicateIdControl_Reserved7` | TField |  |  |
| 8 | `GA.DUP.ID.CONTROL.RESERVED6` | `FsGaDuplicateIdControl_Reserved6` | TField |  |  |
| 9 | `GA.DUP.ID.CONTROL.RESERVED5` | `FsGaDuplicateIdControl_Reserved5` | TField |  |  |
| 10 | `GA.DUP.ID.CONTROL.RESERVED4` | `FsGaDuplicateIdControl_Reserved4` | TField |  |  |
| 11 | `GA.DUP.ID.CONTROL.RESERVED3` | `FsGaDuplicateIdControl_Reserved3` | TField |  |  |
| 12 | `GA.DUP.ID.CONTROL.RESERVED2` | `FsGaDuplicateIdControl_Reserved2` | TField |  |  |
| 13 | `GA.DUP.ID.CONTROL.RESERVED1` | `FsGaDuplicateIdControl_Reserved1` | TField |  |  |
| 14 | `GA.DUP.ID.CONTROL.LOCAL.REF` | `FsGaDuplicateIdControl_LocalRef` |  |  |  |
| 15 | `GA.DUP.ID.CONTROL.OVERRIDE` | `FsGaDuplicateIdControl_Override` |  |  |  |
| 16 | `GA.DUP.ID.CONTROL.RECORD.STATUS` | `FsGaDuplicateIdControl_RecordStatus` | String |  |  |
| 17 | `GA.DUP.ID.CONTROL.CURR.NO` | `FsGaDuplicateIdControl_CurrNo` | String |  |  |
| 18 | `GA.DUP.ID.CONTROL.INPUTTER` | `FsGaDuplicateIdControl_Inputter` |  |  |  |
| 19 | `GA.DUP.ID.CONTROL.DATE.TIME` | `FsGaDuplicateIdControl_DateTime` |  |  |  |
| 20 | `GA.DUP.ID.CONTROL.AUTHORISER` | `FsGaDuplicateIdControl_Authoriser` | String |  |  |
| 21 | `GA.DUP.ID.CONTROL.CO.CODE` | `FsGaDuplicateIdControl_CoCode` | String |  |  |
| 22 | `GA.DUP.ID.CONTROL.DEPT.CODE` | `FsGaDuplicateIdControl_DeptCode` | String |  |  |
| 23 | `GA.DUP.ID.CONTROL.AUDITOR.CODE` | `FsGaDuplicateIdControl_AuditorCode` | String |  |  |
| 24 | `GA.DUP.ID.CONTROL.AUDIT.DATE.TIME` | `FsGaDuplicateIdControl_AuditDateTime` | String |  |  |
