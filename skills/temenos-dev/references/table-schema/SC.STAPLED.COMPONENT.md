# SC.STAPLED.COMPONENT — Table Schema

> Source: `INSERTS/I_F.SC.STAPLED.COMPONENT` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SSC.PARENT.STAPLE.SEC` | `ScStapledComponent_ParentStapleSec` | TField |  | This field holds the parent stapled security. Validation Rules: Noinput Field. Updated by the System by extracting it from the ID |
| 2 | `SC.SSC.EFFECTIVE.DATE` | `ScStapledComponent_EffectiveDate` | TField |  | This field holds the Effective date. Validation Rules: Noinput Field. Updated by the System by extracting it from the ID |
| 3 | `SC.SSC.STAPLED.COMP` | `ScStapledComponent_StapledComp` |  |  |  |
| 4 | `SC.SSC.COMP.RATIO` | `ScStapledComponent_CompRatio` |  |  |  |
| 5 | `SC.SSC.VALUE.SPLIT` | `ScStapledComponent_ValueSplit` |  |  |  |
| 6 | `SC.SSC.PRIMARY.CHILD` | `ScStapledComponent_PrimaryChild` |  |  |  |
| 7 | `SC.SSC.REP.COMP.RATIO` | `ScStapledComponent_RepCompRatio` |  |  |  |
| 8 | `SC.SSC.REBUILD` | `ScStapledComponent_Rebuild` | TField |  | This field indicates whether a rebuild needs to be processed when the value split changes.When this field isenabled, the rebuild process would use the value split in this record to determine the cost of the childinstruments. If the value split is updated only for information purposes, this field need not be enabled. Validation Rules: Defaulted to Yes for back-dated record Can be set to Yes, only when value split is changed |
| 9 | `SC.SSC.RESERVED7` | `ScStapledComponent_Reserved7` | TField |  |  |
| 10 | `SC.SSC.RESERVED6` | `ScStapledComponent_Reserved6` | TField |  |  |
| 11 | `SC.SSC.RESERVED5` | `ScStapledComponent_Reserved5` | TField |  |  |
| 12 | `SC.SSC.RESERVED4` | `ScStapledComponent_Reserved4` | TField |  |  |
| 13 | `SC.SSC.RESERVED3` | `ScStapledComponent_Reserved3` | TField |  |  |
| 14 | `SC.SSC.RESERVED2` | `ScStapledComponent_Reserved2` | TField |  |  |
| 15 | `SC.SSC.RESERVED1` | `ScStapledComponent_Reserved1` | TField |  |  |
| 16 | `SC.SSC.LOCAL.REF` | `ScStapledComponent_LocalRef` |  |  |  |
| 17 | `SC.SSC.OVERRIDE` | `ScStapledComponent_Override` |  |  |  |
| 18 | `SC.SSC.RECORD.STATUS` | `ScStapledComponent_RecordStatus` | String |  |  |
| 19 | `SC.SSC.CURR.NO` | `ScStapledComponent_CurrNo` | String |  |  |
| 20 | `SC.SSC.INPUTTER` | `ScStapledComponent_Inputter` |  |  |  |
| 21 | `SC.SSC.DATE.TIME` | `ScStapledComponent_DateTime` |  |  |  |
| 22 | `SC.SSC.AUTHORISER` | `ScStapledComponent_Authoriser` | String |  |  |
| 23 | `SC.SSC.CO.CODE` | `ScStapledComponent_CoCode` | String |  |  |
| 24 | `SC.SSC.DEPT.CODE` | `ScStapledComponent_DeptCode` | String |  |  |
| 25 | `SC.SSC.AUDITOR.CODE` | `ScStapledComponent_AuditorCode` | String |  |  |
| 26 | `SC.SSC.AUDIT.DATE.TIME` | `ScStapledComponent_AuditDateTime` | String |  |  |
