# FS.GI.WEM.CONDITIONAL.CONTROLS — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.CONDITIONAL.CONTROLS` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.WEM.COND.CONTROLS.CONTROL.ID` | `FsGiWemConditionalControls_ControlId` | TField |  | Unique control number. Multifonds DB Column is TYP_CTRL_ID. |
| 2 | `GI.WEM.COND.CONTROLS.PARENT.TYPE` | `FsGiWemConditionalControls_ParentType` | TField |  | Type of entity for which this wem conditional control is held. Multifonds DB Column is ENTITY_TYPE. |
| 3 | `GI.WEM.COND.CONTROLS.PARENT.ID` | `FsGiWemConditionalControls_ParentId` | TField |  | ID of the entity for which this wem conditional control is held. Multifonds DB Column is ENTITY_ID. |
| 4 | `GI.WEM.COND.CONTROLS.SHARE.CLASS.CODE` | `FsGiWemConditionalControls_ShareClassCode` | TField |  | Share class code for which the wem conditional control is defined. Multifonds DB Column is TPART. |
| 5 | `GI.WEM.COND.CONTROLS.SHARE.CLASS.TYPE` | `FsGiWemConditionalControls_ShareClassType` | TField |  | Corresponds the value set up in the fields 'Fund msg.' and 'Description' at share class level. Multifonds DB Column is TPART_TYPE. |
| 6 | `GI.WEM.COND.CONTROLS.RECEIVED.MODE` | `FsGiWemConditionalControls_ReceivedMode` | TField |  | Mode received of the transactions in scope for the control. Multifonds DB Column is MODE_RECEIVED. |
| 7 | `GI.WEM.COND.CONTROLS.THRESHOLD.AMOUNT` | `FsGiWemConditionalControls_ThresholdAmount` | TField |  | Threshold amount for the specific control. Multifonds DB Column is THRESHOLD_AMT. |
| 8 | `GI.WEM.COND.CONTROLS.THRESHOLD.CURRENCY` | `FsGiWemConditionalControls_ThresholdCurrency` | TField |  | Threshold amount currency. Multifonds DB Column is THRESHOLD_CCY. |
| 9 | `GI.WEM.COND.CONTROLS.SETTLEMENT.TYPE` | `FsGiWemConditionalControls_SettlementType` | TField |  | Settlement type of the transactions in scope for the control. If blank, the control will apply to all settlement types. Multifonds DB Column is TYPE_SETTLEMENT. |
| 10 | `GI.WEM.COND.CONTROLS.RIGHT.TYPE` | `FsGiWemConditionalControls_RightType` | TField |  | The rights on funds by right type ID. Multifonds DB Column is RIGHT_TYPE. |
| 11 | `GI.WEM.COND.CONTROLS.WEM.EXCH.GRP` | `FsGiWemConditionalControls_WemExchGrp` | TField |  | WEM exchange group linked to the selected entity. Multifonds DB Column is EXCH_GRP. |
| 12 | `GI.WEM.COND.CONTROLS.CONDITIONAL.CONTROL.SEQUENCE` | `FsGiWemConditionalControls_ConditionalControlSequence` | TField |  | Conditional control setup sequence number to maintain new index logic. Multifonds DB Column is COND_CTRL_SEQ. |
| 13 | `GI.WEM.COND.CONTROLS.RESERVED10` | `FsGiWemConditionalControls_Reserved10` | TField |  |  |
| 14 | `GI.WEM.COND.CONTROLS.RESERVED9` | `FsGiWemConditionalControls_Reserved9` | TField |  |  |
| 15 | `GI.WEM.COND.CONTROLS.RESERVED8` | `FsGiWemConditionalControls_Reserved8` | TField |  |  |
| 16 | `GI.WEM.COND.CONTROLS.RESERVED7` | `FsGiWemConditionalControls_Reserved7` | TField |  |  |
| 17 | `GI.WEM.COND.CONTROLS.RESERVED6` | `FsGiWemConditionalControls_Reserved6` | TField |  |  |
| 18 | `GI.WEM.COND.CONTROLS.RESERVED5` | `FsGiWemConditionalControls_Reserved5` | TField |  |  |
| 19 | `GI.WEM.COND.CONTROLS.RESERVED4` | `FsGiWemConditionalControls_Reserved4` | TField |  |  |
| 20 | `GI.WEM.COND.CONTROLS.RESERVED3` | `FsGiWemConditionalControls_Reserved3` | TField |  |  |
| 21 | `GI.WEM.COND.CONTROLS.RESERVED2` | `FsGiWemConditionalControls_Reserved2` | TField |  |  |
| 22 | `GI.WEM.COND.CONTROLS.RESERVED1` | `FsGiWemConditionalControls_Reserved1` | TField |  |  |
| 23 | `GI.WEM.COND.CONTROLS.LOCAL.REF` | `FsGiWemConditionalControls_LocalRef` |  |  |  |
| 24 | `GI.WEM.COND.CONTROLS.OVERRIDE` | `FsGiWemConditionalControls_Override` |  |  |  |
| 25 | `GI.WEM.COND.CONTROLS.RECORD.STATUS` | `FsGiWemConditionalControls_RecordStatus` | String |  |  |
| 26 | `GI.WEM.COND.CONTROLS.CURR.NO` | `FsGiWemConditionalControls_CurrNo` | String |  |  |
| 27 | `GI.WEM.COND.CONTROLS.INPUTTER` | `FsGiWemConditionalControls_Inputter` |  |  |  |
| 28 | `GI.WEM.COND.CONTROLS.DATE.TIME` | `FsGiWemConditionalControls_DateTime` |  |  |  |
| 29 | `GI.WEM.COND.CONTROLS.AUTHORISER` | `FsGiWemConditionalControls_Authoriser` | String |  |  |
| 30 | `GI.WEM.COND.CONTROLS.CO.CODE` | `FsGiWemConditionalControls_CoCode` | String |  |  |
| 31 | `GI.WEM.COND.CONTROLS.DEPT.CODE` | `FsGiWemConditionalControls_DeptCode` | String |  |  |
| 32 | `GI.WEM.COND.CONTROLS.AUDITOR.CODE` | `FsGiWemConditionalControls_AuditorCode` | String |  |  |
| 33 | `GI.WEM.COND.CONTROLS.AUDIT.DATE.TIME` | `FsGiWemConditionalControls_AuditDateTime` | String |  |  |
