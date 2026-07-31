# SY.UNIT — Table Schema

> Source: `INSERTS/I_F.SY.UNIT` in `SY_Unit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.UN.PRODUCT.DEFINITION` | `SyUnit_ProductDefinition` | TField |  | This is the first part of the Unit Definition key and is the PRODUCT.DEFINITION that this Unit has been created for. A valid PRODUCT.DEFINITION record which is automatically populated from the first part of the record ID. |
| 2 | `SY.UN.UNIT.NAME` | `SyUnit_UnitName` | TField |  | This is the second and last part of the Unit Definition key. As this will usually apply to a specific T24 deal it is advisable to try to make this as descriptive as possible. E.g. �FxHedgeOption� will aid in recognising not just what type of deal this is but what its function is with regards to this Product. This field is automatically populated from second part of the record ID. |
| 3 | `SY.UN.SY.TRANSACTION` | `SyUnit_SyTransaction` | TField |  | The transaction for which this unit was created. |
| 4 | `SY.UN.INSTANCE` | `SyUnit_Instance` | TField |  | This is the instance of the Unit. In general there will be one instance of a Unit per T24 deal which is encapsulated by this Unit. This will be a zero-padded 4 digit number which will form the fourth element of the Unit key. |
| 5 | `SY.UN.SEQUENCE` | `SyUnit_Sequence` | TField |  | Not used on the Unit |
| 6 | `SY.UN.T24.APPLICATION` | `SyUnit_T24Application` | TField |  | The ID of the underlying T24 application. This cannot be an SY.EVENT and cannot be changed when a T24.APP.ID is present. |
| 7 | `SY.UN.APP.ID.SOURCE` | `SyUnit_AppIdSource` | TField |  | If populated, this field will be used to create the T24.APP.ID. This field can be either a �Quoted literal value�, a virtual field name or a valid subroutine name prefixd by an '@' character. |
| 8 | `SY.UN.T24.APP.ID` | `SyUnit_T24AppId` | TField |  | This is the ID of the deal within the underlying T24.APPLICATION. The default is for this to be populated with the next ID for the application when the 'New' operation is applied to the unit. If the APP.ID.SOURCE field can be used override the default behaviour and specify the ID that appears here. Once populated, this will not change. |
| 9 | `SY.UN.SHORT.DESC` | `SyUnit_ShortDesc` |  |  |  |
| 10 | `SY.UN.DESCRIPTION` | `SyUnit_Description` |  |  |  |
| 11 | `SY.UN.TRACKING` | `SyUnit_Tracking` | TField | Yes | When Tracking is enabled the instantiated Units will track any changes made to the Unit Definition during the product lifecycle. Otherwise the instantiated Units will copy the state of the Unit definition when created. Possible values are 'Yes' or 'No'. This field is mandatory. |
| 12 | `SY.UN.INHERIT.FROM.UNIT` | `SyUnit_InheritFromUnit` | TField |  | Allows functionallity to be inherited from an existing Unit Definition. If present this defines the Unit Definition that this unit will inherit its values from. Must be a valid SY.UNIT.DEFINITION ID which must not be this ID. |
| 13 | `SY.UN.APP.OPERATION` | `SyUnit_AppOperation` |  |  |  |
| 14 | `SY.UN.FILTER` | `SyUnit_Filter` |  |  |  |
| 15 | `SY.UN.ROUTINE` | `SyUnit_Routine` |  |  |  |
| 16 | `SY.UN.EB.ACTIVITY` | `SyUnit_EbActivity` |  |  |  |
| 17 | `SY.UN.RESERVED.MV.4` | `SyUnit_ReservedMv4` |  |  |  |
| 18 | `SY.UN.RESERVED.MV.3` | `SyUnit_ReservedMv3` |  |  |  |
| 19 | `SY.UN.RESERVED.MV.2` | `SyUnit_ReservedMv2` |  |  |  |
| 20 | `SY.UN.RESERVED.MV.1` | `SyUnit_ReservedMv1` |  |  |  |
| 21 | `SY.UN.VERSION` | `SyUnit_Version` |  |  |  |
| 22 | `SY.UN.MAP.FROM` | `SyUnit_MapFrom` |  |  |  |
| 23 | `SY.UN.FORMAT.ENTRY.REC` | `SyUnit_FormatEntryRec` |  |  |  |
| 24 | `SY.UN.FLD.OPERATION` | `SyUnit_FldOperation` |  |  |  |
| 25 | `SY.UN.VIRTUAL.FIELD` | `SyUnit_VirtualField` |  |  |  |
| 26 | `SY.UN.VIRT.FLD.FILTER` | `SyUnit_VirtFldFilter` |  |  |  |
| 27 | `SY.UN.PRI.VALUE` | `SyUnit_PriValue` |  |  |  |
| 28 | `SY.UN.FUNCTION` | `SyUnit_Function` |  |  |  |
| 29 | `SY.UN.SEC.VALUE` | `SyUnit_SecValue` |  |  |  |
| 30 | `SY.UN.DRILLDOWN.ID` | `SyUnit_DrilldownId` |  |  |  |
| 31 | `SY.UN.DRILLDOWN.APP` | `SyUnit_DrilldownApp` |  |  |  |
| 32 | `SY.UN.DD.FIELD.NAME` | `SyUnit_DdFieldName` |  |  |  |
| 33 | `SY.UN.STATUS` | `SyUnit_Status` |  |  |  |
| 34 | `SY.UN.RESERVED.SV.1` | `SyUnit_ReservedSv1` |  |  |  |
| 35 | `SY.UN.RESERVED.SV.2` | `SyUnit_ReservedSv2` |  |  |  |
| 36 | `SY.UN.RESERVED.SV.3` | `SyUnit_ReservedSv3` |  |  |  |
| 37 | `SY.UN.STORE` | `SyUnit_Store` |  |  |  |
| 38 | `SY.UN.OPERATION` | `SyUnit_Operation` | TField |  | This field is used to apply a valid Operation to a Unit. It is populated by the processing engine. |
| 39 | `SY.UN.LIFECYCLE.OP` | `SyUnit_LifecycleOp` |  |  |  |
| 40 | `SY.UN.LIFECYCLE.DATE` | `SyUnit_LifecycleDate` |  |  |  |
| 41 | `SY.UN.LIFECYCLE.TIME` | `SyUnit_LifecycleTime` |  |  |  |
| 42 | `SY.UN.LIFECYCLE.EVENT` | `SyUnit_LifecycleEvent` |  |  |  |
| 43 | `SY.UN.LIFECYCLE.FILT` | `SyUnit_LifecycleFilt` |  |  |  |
| 44 | `SY.UN.VIRTUAL.FIELD.NAME` | `SyUnit_VirtualFieldName` |  |  |  |
| 45 | `SY.UN.VIRTUAL.FIELD.VALUE` | `SyUnit_VirtualFieldValue` |  |  |  |
| 46 | `SY.UN.INTERNAL.USE` | `SyUnit_InternalUse` | TField |  | System-generated field. For internal system use only. |
| 47 | `SY.UN.ACTIVITY.CODE` | `SyUnit_ActivityCode` |  |  |  |
| 48 | `SY.UN.RESERVED.52` | `SyUnit_Reserved52` |  |  |  |
| 49 | `SY.UN.RESERVED.51` | `SyUnit_Reserved51` |  |  |  |
| 50 | `SY.UN.MESSAGE.REF` | `SyUnit_MessageRef` |  |  |  |
| 51 | `SY.UN.RESERVED.5` | `SyUnit_Reserved5` | TField |  |  |
| 52 | `SY.UN.RESERVED.4` | `SyUnit_Reserved4` | TField |  |  |
| 53 | `SY.UN.RESERVED.3` | `SyUnit_Reserved3` | TField |  |  |
| 54 | `SY.UN.RESERVED.2` | `SyUnit_Reserved2` | TField |  |  |
| 55 | `SY.UN.RESERVED.1` | `SyUnit_Reserved1` | TField |  |  |
| 56 | `SY.UN.LOCAL.REF` | `SyUnit_LocalRef` |  |  |  |
| 57 | `SY.UN.OVERRIDE` | `SyUnit_Override` |  |  |  |
| 58 | `SY.UN.RECORD.STATUS` | `SyUnit_RecordStatus` | String |  |  |
| 59 | `SY.UN.CURR.NO` | `SyUnit_CurrNo` | String |  |  |
| 60 | `SY.UN.INPUTTER` | `SyUnit_Inputter` |  |  |  |
| 61 | `SY.UN.DATE.TIME` | `SyUnit_DateTime` |  |  |  |
| 62 | `SY.UN.AUTHORISER` | `SyUnit_Authoriser` | String |  |  |
| 63 | `SY.UN.CO.CODE` | `SyUnit_CoCode` | String |  |  |
| 64 | `SY.UN.DEPT.CODE` | `SyUnit_DeptCode` | String |  |  |
| 65 | `SY.UN.AUDITOR.CODE` | `SyUnit_AuditorCode` | String |  |  |
| 66 | `SY.UN.AUDIT.DATE.TIME` | `SyUnit_AuditDateTime` | String |  |  |
