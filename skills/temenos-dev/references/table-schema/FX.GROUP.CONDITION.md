# FX.GROUP.CONDITION — Table Schema

> Source: `INSERTS/I_F.FX.GROUP.CONDITION` in `FX_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FX.GR.PORTFOLIO` | `FxGroupCondition_Portfolio` |  |  |  |
| 2 | `FX.GR.DEAL.TYPE` | `FxGroupCondition_DealType` |  |  |  |
| 3 | `FX.GR.MARGIN` | `FxGroupCondition_Margin` |  |  |  |
| 4 | `FX.GR.FX.COMM.GROUP` | `FxGroupCondition_FxCommGroup` |  |  |  |
| 5 | `FX.GR.RESERVED.15` | `FxGroupCondition_Reserved15` |  |  |  |
| 6 | `FX.GR.RESERVED.14` | `FxGroupCondition_Reserved14` |  |  |  |
| 7 | `FX.GR.RESERVED.13` | `FxGroupCondition_Reserved13` |  |  |  |
| 8 | `FX.GR.RESERVED.12` | `FxGroupCondition_Reserved12` |  |  |  |
| 9 | `FX.GR.RESERVED.11` | `FxGroupCondition_Reserved11` |  |  |  |
| 10 | `FX.GR.RESERVED.10` | `FxGroupCondition_Reserved10` |  |  |  |
| 11 | `FX.GR.RESERVED.9` | `FxGroupCondition_Reserved9` |  |  |  |
| 12 | `FX.GR.RESERVED.8` | `FxGroupCondition_Reserved8` |  |  |  |
| 13 | `FX.GR.RESERVED.7` | `FxGroupCondition_Reserved7` |  |  |  |
| 14 | `FX.GR.RESERVED.6` | `FxGroupCondition_Reserved6` |  |  |  |
| 15 | `FX.GR.RESERVED.5` | `FxGroupCondition_Reserved5` |  |  |  |
| 16 | `FX.GR.RESERVED.4` | `FxGroupCondition_Reserved4` |  |  |  |
| 17 | `FX.GR.RESERVED.3` | `FxGroupCondition_Reserved3` |  |  |  |
| 18 | `FX.GR.RESERVED.2` | `FxGroupCondition_Reserved2` |  |  |  |
| 19 | `FX.GR.RESERVED.1` | `FxGroupCondition_Reserved1` |  |  |  |
| 20 | `FX.GR.LOCAL.REF` | `FxGroupCondition_LocalRef` |  |  |  |
| 21 | `FX.GR.RECORD.STATUS` | `FxGroupCondition_RecordStatus` | String |  |  |
| 22 | `FX.GR.CURR.NO` | `FxGroupCondition_CurrNo` | String |  |  |
| 23 | `FX.GR.INPUTTER` | `FxGroupCondition_Inputter` |  |  |  |
| 24 | `FX.GR.DATE.TIME` | `FxGroupCondition_DateTime` |  |  |  |
| 25 | `FX.GR.AUTHORISER` | `FxGroupCondition_Authoriser` | String |  |  |
| 26 | `FX.GR.CO.CODE` | `FxGroupCondition_CoCode` | String |  |  |
| 27 | `FX.GR.DEPT.CODE` | `FxGroupCondition_DeptCode` | String |  |  |
| 28 | `FX.GR.AUDITOR.CODE` | `FxGroupCondition_AuditorCode` | String |  |  |
| 29 | `FX.GR.AUDIT.DATE.TIME` | `FxGroupCondition_AuditDateTime` | String |  |  |
