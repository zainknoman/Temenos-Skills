# SY.UNIT.LOG — Table Schema

> Source: `INSERTS/I_F.SY.UNIT.LOG` in `SY_Unit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.UL.PRODUCT.DEFINITION` | `SyUnitLog_ProductDefinition` | TField |  | This is the first part of the Unit Definition key and is the PRODUCT.DEFINITION that this Unit has been created for. A valid PRODUCT.DEFINITION record which is automatically populated from the first part of the record ID. |
| 2 | `SY.UL.UNIT.NAME` | `SyUnitLog_UnitName` | TField |  | This is the second and last part of the Unit Definition key. As this will usually apply to a specific T24 deal it is advisable to try to make this as descriptive as possible. E.g. �FxHedgeOption� will aid in recognising not just what type of deal this is but what its function is with regards to this Product. This field is automatically populated from second part of the record ID. |
| 3 | `SY.UL.SY.TRANSACTION` | `SyUnitLog_SyTransaction` | TField |  | The transaction for which this unit was created. |
| 4 | `SY.UL.INSTANCE` | `SyUnitLog_Instance` | TField |  | This is the instance of the Unit. In general there will be one instance of a Unit per T24 deal which is encapsulated by this Unit. This will be a zero-padded 4 digit number which will form the fourth element of the Unit key. |
| 5 | `SY.UL.SEQUENCE` | `SyUnitLog_Sequence` | TField |  | This field contains a zero-padded 4-digit sequence number and forms the final part of the SY.UNIT.LOG key. |
| 6 | `SY.UL.T24.APPLICATION` | `SyUnitLog_T24Application` | TField |  | The ID of the underlying T24 application. This cannot be an SY.EVENT and cannot be changed when a T24.APP.ID is present. |
| 7 | `SY.UL.APP.ID.SOURCE` | `SyUnitLog_AppIdSource` | TField |  | If populated, this field will be used to create the T24.APP.ID. This field can be either a �Quoted literal value�, a virtual field name or a valid subroutine name prefixd by an '@' character. |
| 8 | `SY.UL.T24.APP.ID` | `SyUnitLog_T24AppId` | TField |  | This is the ID of the deal within the underlying T24.APPLICATION. It is populated by default with the next ID for the T24.APPLICATION when the 'New' operation is applied to the unit. If the APP.ID.SOURCE field is populated then it will be used to determine the value of the ID. Once populated this cannot change. |
| 9 | `SY.UL.SHORT.DESC` | `SyUnitLog_ShortDesc` |  |  |  |
| 10 | `SY.UL.DESCRIPTION` | `SyUnitLog_Description` |  |  |  |
| 11 | `SY.UL.TRACKING` | `SyUnitLog_Tracking` | TField | Yes | When Tracking is enabled the instantiated Units will track any changes made to the Unit Definition during the product lifecycle. Otherwise the instantiated Units will copy the state of the Unit definition when created. Possible values are 'Yes' or 'No'. This field is mandatory. |
| 12 | `SY.UL.INHERIT.FROM.UNIT` | `SyUnitLog_InheritFromUnit` | TField |  | Allows functionallity to be inherited from an existing Unit Definition. If present this defines the Unit Definition that this unit will inherit its values from. Must be a valid SY.UNIT.DEFINITION ID which must not be this ID. |
| 13 | `SY.UL.APP.OPERATION` | `SyUnitLog_AppOperation` |  |  |  |
| 14 | `SY.UL.FILTER` | `SyUnitLog_Filter` |  |  |  |
| 15 | `SY.UL.ROUTINE` | `SyUnitLog_Routine` |  |  |  |
| 16 | `SY.UL.EB.ACTIVITY` | `SyUnitLog_EbActivity` |  |  |  |
| 17 | `SY.UL.RESERVED.MV.4` | `SyUnitLog_ReservedMv4` |  |  |  |
| 18 | `SY.UL.RESERVED.MV.3` | `SyUnitLog_ReservedMv3` |  |  |  |
| 19 | `SY.UL.RESERVED.MV.2` | `SyUnitLog_ReservedMv2` |  |  |  |
| 20 | `SY.UL.RESERVED.MV.1` | `SyUnitLog_ReservedMv1` |  |  |  |
| 21 | `SY.UL.VERSION` | `SyUnitLog_Version` |  |  |  |
| 22 | `SY.UL.MAP.FROM` | `SyUnitLog_MapFrom` |  |  |  |
| 23 | `SY.UL.FORMAT.ENTRY.REC` | `SyUnitLog_FormatEntryRec` |  |  |  |
| 24 | `SY.UL.FLD.OPERATION` | `SyUnitLog_FldOperation` |  |  |  |
| 25 | `SY.UL.VIRTUAL.FIELD` | `SyUnitLog_VirtualField` |  |  |  |
| 26 | `SY.UL.VIRT.FLD.FILTER` | `SyUnitLog_VirtFldFilter` |  |  |  |
| 27 | `SY.UL.PRI.VALUE` | `SyUnitLog_PriValue` |  |  |  |
| 28 | `SY.UL.FUNCTION` | `SyUnitLog_Function` |  |  |  |
| 29 | `SY.UL.SEC.VALUE` | `SyUnitLog_SecValue` |  |  |  |
| 30 | `SY.UL.DRILLDOWN.ID` | `SyUnitLog_DrilldownId` |  |  |  |
| 31 | `SY.UL.DRILLDOWN.APP` | `SyUnitLog_DrilldownApp` |  |  |  |
| 32 | `SY.UL.DD.FIELD.NAME` | `SyUnitLog_DdFieldName` |  |  |  |
| 33 | `SY.UL.STATUS` | `SyUnitLog_Status` |  |  |  |
| 34 | `SY.UL.RESERVED.SV.1` | `SyUnitLog_ReservedSv1` |  |  |  |
| 35 | `SY.UL.RESERVED.SV.2` | `SyUnitLog_ReservedSv2` |  |  |  |
| 36 | `SY.UL.RESERVED.SV.3` | `SyUnitLog_ReservedSv3` |  |  |  |
| 37 | `SY.UL.STORE` | `SyUnitLog_Store` |  |  |  |
| 38 | `SY.UL.OPERATION` | `SyUnitLog_Operation` | TField |  | This field is used to apply a valid Operation to a Unit. It is populated by the processing engine. |
| 39 | `SY.UL.LIFECYCLE.OP` | `SyUnitLog_LifecycleOp` |  |  |  |
| 40 | `SY.UL.LIFECYCLE.DATE` | `SyUnitLog_LifecycleDate` |  |  |  |
| 41 | `SY.UL.LIFECYCLE.TIME` | `SyUnitLog_LifecycleTime` |  |  |  |
| 42 | `SY.UL.LIFECYCLE.EVENT` | `SyUnitLog_LifecycleEvent` |  |  |  |
| 43 | `SY.UL.LIFECYCLE.FILT` | `SyUnitLog_LifecycleFilt` |  |  |  |
| 44 | `SY.UL.VIRTUAL.FIELD.NAME` | `SyUnitLog_VirtualFieldName` |  |  |  |
| 45 | `SY.UL.VIRTUAL.FIELD.VALUE` | `SyUnitLog_VirtualFieldValue` |  |  |  |
| 46 | `SY.UL.INTERNAL.USE` | `SyUnitLog_InternalUse` | TField |  | This field is not used in SY.UNIT.LOG. This field is for internal use only. |
| 47 | `SY.UL.ACTIVITY.CODE` | `SyUnitLog_ActivityCode` |  |  |  |
| 48 | `SY.UL.RESERVED.52` | `SyUnitLog_Reserved52` |  |  |  |
| 49 | `SY.UL.RESERVED.51` | `SyUnitLog_Reserved51` |  |  |  |
| 50 | `SY.UL.MESSAGE.REF` | `SyUnitLog_MessageRef` |  |  |  |
| 51 | `SY.UL.RESERVED.5` | `SyUnitLog_Reserved5` | TField |  |  |
| 52 | `SY.UL.RESERVED.4` | `SyUnitLog_Reserved4` | TField |  |  |
| 53 | `SY.UL.RESERVED.3` | `SyUnitLog_Reserved3` | TField |  |  |
| 54 | `SY.UL.RESERVED.2` | `SyUnitLog_Reserved2` | TField |  |  |
| 55 | `SY.UL.RESERVED.1` | `SyUnitLog_Reserved1` | TField |  |  |
| 56 | `SY.UL.LOCAL.REF` | `SyUnitLog_LocalRef` |  |  |  |
| 57 | `SY.UL.OVERRIDE` | `SyUnitLog_Override` |  |  |  |
