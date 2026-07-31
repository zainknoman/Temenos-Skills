# SY.UNIT.DEFINITION — Table Schema

> Source: `INSERTS/I_F.SY.UNIT.DEFINITION` in `SY_Unit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.UD.PRODUCT.DEFINITION` | `SyUnitDefinition_ProductDefinition` | TField |  | This is the first part of the Unit Definition key and is the PRODUCT.DEFINITION that this Unit has been created for. A valid PRODUCT.DEFINITION record which is automatically populated from the first part of the record ID. |
| 2 | `SY.UD.UNIT.NAME` | `SyUnitDefinition_UnitName` | TField |  | This is the second and last part of the Unit Definition key. As this will usually apply to a specific T24 deal it is advisable to try to make this as descriptive as possible. E.g. �FxHedgeOption� will aid in recognising not just what type of deal this is but what its function is with regards to this Product. This field is automatically populated from second part of the record ID. |
| 3 | `SY.UD.SY.TRANSACTION` | `SyUnitDefinition_SyTransaction` | TField |  | Not used on the Unit Definition |
| 4 | `SY.UD.INSTANCE` | `SyUnitDefinition_Instance` | TField |  | Not used on the Unit Definition |
| 5 | `SY.UD.SEQUENCE` | `SyUnitDefinition_Sequence` | TField |  | Not used on the Unit Definition |
| 6 | `SY.UD.T24.APPLICATION` | `SyUnitDefinition_T24Application` | TField |  | The ID of the underlying T24 application. This cannot be an SY.EVENT and cannot be changed when a T24.APP.ID is present. |
| 7 | `SY.UD.APP.ID.SOURCE` | `SyUnitDefinition_AppIdSource` | TField |  | If populated, this field will be used to create the T24.APP.ID. This field can be either a �Quoted literal value�, a virtual field name or a valid subroutine name prefixd by an '@' character. |
| 8 | `SY.UD.T24.APP.ID` | `SyUnitDefinition_T24AppId` | TField |  | Not used on the Unit Definition |
| 9 | `SY.UD.SHORT.DESC` | `SyUnitDefinition_ShortDesc` |  |  |  |
| 10 | `SY.UD.DESCRIPTION` | `SyUnitDefinition_Description` |  |  |  |
| 11 | `SY.UD.TRACKING` | `SyUnitDefinition_Tracking` | TField | Yes | When Tracking is enabled the instantiated Units will track any changes made to the Unit Definition during the product lifecycle. Otherwise the instantiated Units will copy the state of the Unit definition when created. Possible values are 'Yes' or 'No'. This field is mandatory. |
| 12 | `SY.UD.INHERIT.FROM.UNIT` | `SyUnitDefinition_InheritFromUnit` | TField |  | Allows functionallity to be inherited from an existing Unit Definition. If present this defines the Unit Definition that this unit will inherit its values from. Must be a valid SY.UNIT.DEFINITION ID which must not be this ID. |
| 13 | `SY.UD.APP.OPERATION` | `SyUnitDefinition_AppOperation` |  |  |  |
| 14 | `SY.UD.FILTER` | `SyUnitDefinition_Filter` |  |  |  |
| 15 | `SY.UD.ROUTINE` | `SyUnitDefinition_Routine` |  |  |  |
| 16 | `SY.UD.EB.ACTIVITY` | `SyUnitDefinition_EbActivity` |  |  |  |
| 17 | `SY.UD.RESERVED.MV.4` | `SyUnitDefinition_ReservedMv4` |  |  |  |
| 18 | `SY.UD.RESERVED.MV.3` | `SyUnitDefinition_ReservedMv3` |  |  |  |
| 19 | `SY.UD.RESERVED.MV.2` | `SyUnitDefinition_ReservedMv2` |  |  |  |
| 20 | `SY.UD.RESERVED.MV.1` | `SyUnitDefinition_ReservedMv1` |  |  |  |
| 21 | `SY.UD.VERSION` | `SyUnitDefinition_Version` |  |  |  |
| 22 | `SY.UD.MAP.FROM` | `SyUnitDefinition_MapFrom` |  |  |  |
| 23 | `SY.UD.FORMAT.ENTRY.REC` | `SyUnitDefinition_FormatEntryRec` |  |  |  |
| 24 | `SY.UD.FLD.OPERATION` | `SyUnitDefinition_FldOperation` |  |  |  |
| 25 | `SY.UD.VIRTUAL.FIELD` | `SyUnitDefinition_VirtualField` |  |  |  |
| 26 | `SY.UD.VIRT.FLD.FILTER` | `SyUnitDefinition_VirtFldFilter` |  |  |  |
| 27 | `SY.UD.PRI.VALUE` | `SyUnitDefinition_PriValue` |  |  |  |
| 28 | `SY.UD.FUNCTION` | `SyUnitDefinition_Function` |  |  |  |
| 29 | `SY.UD.SEC.VALUE` | `SyUnitDefinition_SecValue` |  |  |  |
| 30 | `SY.UD.DRILLDOWN.ID` | `SyUnitDefinition_DrilldownId` |  |  |  |
| 31 | `SY.UD.DRILLDOWN.APP` | `SyUnitDefinition_DrilldownApp` |  |  |  |
| 32 | `SY.UD.DD.FIELD.NAME` | `SyUnitDefinition_DdFieldName` |  |  |  |
| 33 | `SY.UD.STATUS` | `SyUnitDefinition_Status` |  |  |  |
| 34 | `SY.UD.RESERVED.SV.1` | `SyUnitDefinition_ReservedSv1` |  |  |  |
| 35 | `SY.UD.RESERVED.SV.2` | `SyUnitDefinition_ReservedSv2` |  |  |  |
| 36 | `SY.UD.RESERVED.SV.3` | `SyUnitDefinition_ReservedSv3` |  |  |  |
| 37 | `SY.UD.STORE` | `SyUnitDefinition_Store` |  |  |  |
| 38 | `SY.UD.OPERATION` | `SyUnitDefinition_Operation` | TField |  | Not used on the Unit Definition |
| 39 | `SY.UD.LIFECYCLE.OP` | `SyUnitDefinition_LifecycleOp` |  |  |  |
| 40 | `SY.UD.LIFECYCLE.DATE` | `SyUnitDefinition_LifecycleDate` |  |  |  |
| 41 | `SY.UD.LIFECYCLE.TIME` | `SyUnitDefinition_LifecycleTime` |  |  |  |
| 42 | `SY.UD.LIFECYCLE.EVENT` | `SyUnitDefinition_LifecycleEvent` |  |  |  |
| 43 | `SY.UD.LIFECYCLE.FILT` | `SyUnitDefinition_LifecycleFilt` |  |  |  |
| 44 | `SY.UD.VIRTUAL.FIELD.NAME` | `SyUnitDefinition_VirtualFieldName` |  |  |  |
| 45 | `SY.UD.VIRTUAL.FIELD.VALUE` | `SyUnitDefinition_VirtualFieldValue` |  |  |  |
| 46 | `SY.UD.INTERNAL.USE` | `SyUnitDefinition_InternalUse` | TField |  | System-generated field. Internal system use only. |
| 47 | `SY.UD.ACTIVITY.CODE` | `SyUnitDefinition_ActivityCode` |  |  |  |
| 48 | `SY.UD.RESERVED.52` | `SyUnitDefinition_Reserved52` |  |  |  |
| 49 | `SY.UD.RESERVED.51` | `SyUnitDefinition_Reserved51` |  |  |  |
| 50 | `SY.UD.MESSAGE.REF` | `SyUnitDefinition_MessageRef` |  |  |  |
| 51 | `SY.UD.RESERVED.5` | `SyUnitDefinition_Reserved5` | TField |  |  |
| 52 | `SY.UD.RESERVED.4` | `SyUnitDefinition_Reserved4` | TField |  |  |
| 53 | `SY.UD.RESERVED.3` | `SyUnitDefinition_Reserved3` | TField |  |  |
| 54 | `SY.UD.RESERVED.2` | `SyUnitDefinition_Reserved2` | TField |  |  |
| 55 | `SY.UD.RESERVED.1` | `SyUnitDefinition_Reserved1` | TField |  |  |
| 56 | `SY.UD.LOCAL.REF` | `SyUnitDefinition_LocalRef` |  |  |  |
| 57 | `SY.UD.OVERRIDE` | `SyUnitDefinition_Override` |  |  |  |
| 58 | `SY.UD.RECORD.STATUS` | `SyUnitDefinition_RecordStatus` | String |  |  |
| 59 | `SY.UD.CURR.NO` | `SyUnitDefinition_CurrNo` | String |  |  |
| 60 | `SY.UD.INPUTTER` | `SyUnitDefinition_Inputter` |  |  |  |
| 61 | `SY.UD.DATE.TIME` | `SyUnitDefinition_DateTime` |  |  |  |
| 62 | `SY.UD.AUTHORISER` | `SyUnitDefinition_Authoriser` | String |  |  |
| 63 | `SY.UD.CO.CODE` | `SyUnitDefinition_CoCode` | String |  |  |
| 64 | `SY.UD.DEPT.CODE` | `SyUnitDefinition_DeptCode` | String |  |  |
| 65 | `SY.UD.AUDITOR.CODE` | `SyUnitDefinition_AuditorCode` | String |  |  |
| 66 | `SY.UD.AUDIT.DATE.TIME` | `SyUnitDefinition_AuditDateTime` | String |  |  |
