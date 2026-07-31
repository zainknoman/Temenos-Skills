# FS.GA.USER.DEFINED.FIELD.MASTER — Table Schema

> Source: `INSERTS/I_F.FS.GA.USER.DEFINED.FIELD.MASTER` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.USER.DEFINED.FIELD.MASTER.PARENT.REF.ID` | `FsGaUserDefinedFieldMaster_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.USER.DEFINED.FIELD.MASTER.ORA.ROWID` | `FsGaUserDefinedFieldMaster_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.USER.DEFINED.FIELD.MASTER.USER.DEFINABLE.FIELDS.GROUP` | `FsGaUserDefinedFieldMaster_UserDefinableFieldsGroup` | TField |  | User definable Fields group code Multifonds DB Column is GRP_CODE. |
| 4 | `FS.GA.USER.DEFINED.FIELD.MASTER.UDF.CODE` | `FsGaUserDefinedFieldMaster_UdfCode` | TField |  | Udf code Multifonds DB Column is UDF_CODE. |
| 5 | `FS.GA.USER.DEFINED.FIELD.MASTER.ACTIVE.FLG` | `FsGaUserDefinedFieldMaster_ActiveFlg` | TField |  | If ticked , Its active for user to update the fields. If un-ticked, Its inactive for user to update fields but where it was already updated earlier, the same continues to be a visible field. Multifonds DB Column is FLG_ACTIVE. |
| 6 | `FS.GA.USER.DEFINED.FIELD.MASTER.UDF.NAME` | `FsGaUserDefinedFieldMaster_UdfName` | TField | Yes | Long Description of UDF field can be entered up to 30 alphanumeric characters. This field is mandatory field. Multifonds DB Column is UDF_DESC. |
| 7 | `FS.GA.USER.DEFINED.FIELD.MASTER.UDF.FORMAT` | `FsGaUserDefinedFieldMaster_UdfFormat` | TField | Yes | The 'Format' field provides the format attribute of 'UDF' field to be defined either Free Text Or Table Or Numeric Or Date. Mandatory field. Multifonds DB Column is UDF_FORMAT. |
| 8 | `FS.GA.USER.DEFINED.FIELD.MASTER.LOOK.UP.TABLE` | `FsGaUserDefinedFieldMaster_LookUpTable` | TField |  | User can create any code that is identified as Table. This field accepts any alphanumeric value up to 20 characters. Multifonds DB Column is UDF_LOOK_TAB. |
| 9 | `FS.GA.USER.DEFINED.FIELD.MASTER.ELEMENT.REFERENCE` | `FsGaUserDefinedFieldMaster_ElementReference` | TField |  | Filters info. based on the param. in the 'Element' column. E.g. If 'Element' is param. with 'TYPE' systems filters the records by type and displays relevant info. for 'TYPE' viz. 'AM', 'BK','BR' etc. Multifonds DB Column is REF_TYPE. |
| 10 | `FS.GA.USER.DEFINED.FIELD.MASTER.MANDATORY.OR.OPTIONAL` | `FsGaUserDefinedFieldMaster_MandatoryOrOptional` | TField | Conditional | User can input either M (Mandatory) or O (optional) Multifonds DB Column is MANDAT_OPT. |
| 11 | `FS.GA.USER.DEFINED.FIELD.MASTER.FUND` | `FsGaUserDefinedFieldMaster_Fund` | TField |  | If ticked, Populates UDF codes in the UDF tab inside Fund Master Screen. If un-ticked, Doesn't Populate UDF codes in UDF tab inside Fund Master Screen. Multifonds DB Column is FLG_NPTF. |
| 12 | `FS.GA.USER.DEFINED.FIELD.MASTER.SHARE.VALUE.FLG` | `FsGaUserDefinedFieldMaster_ShareValueFlg` | TField |  | If ticked, Populates the UDF codes in UDF tab inside Fund Master Screen specific to Share Class. If un-ticked, Doesn't Populate UDF codes in UDF tab inside Fund Master Screen specific to Share Class. Multifonds DB Column is FLG_TPARTS. |
| 13 | `FS.GA.USER.DEFINED.FIELD.MASTER.SEC.OR.OPT.OR.FU.MASTER.FLG` | `FsGaUserDefinedFieldMaster_SecOrOptOrFuMasterFlg` | TField |  | If ticked, Populates the UDF codes in Sec. Master, Fu. Master and Op. Master. If un-ticked, Doesn't populate the UDF codes in Sec. Master, Fu. Master and Op. Master. Multifonds DB Column is FLG_SEC_SFO. |
| 14 | `FS.GA.USER.DEFINED.FIELD.MASTER.CENTRAL.REGISTER.FLG` | `FsGaUserDefinedFieldMaster_CentralRegisterFlg` | TField |  | If ticked, UDF codes will be populated in the UDF tab inside Central Register Master. If un-ticked, UDF codes will not be populated in the UDF tab inside Central Register Master. Multifonds DB Column is FLG_CENTRAL_REG. |
| 15 | `FS.GA.USER.DEFINED.FIELD.MASTER.SEC.OR.OPT.OR.FUT.TRANS.FLG` | `FsGaUserDefinedFieldMaster_SecOrOptOrFutTransFlg` | TField |  | If ticked, Populates the UDF codes in UDF tab inside Security Trans., Future Trans. and Option Trans. If un-ticked, Doesn't populate the UDF codes. Multifonds DB Column is FLG_SEC_TRANS. |
| 16 | `FS.GA.USER.DEFINED.FIELD.MASTER.SUB.RED.TRANSACTION` | `FsGaUserDefinedFieldMaster_SubRedTransaction` | TField |  | If ticked, Populates the UDF codes in UDF tab inside Sub/Red Transaction Screen. If un-ticked, Doesn't populate the UDF codes in UDF tab inside Sub/Red Transaction Screen. Multifonds DB Column is FLG_SUB_RED. |
| 17 | `FS.GA.USER.DEFINED.FIELD.MASTER.FLAG.TRANSACTION.DP` | `FsGaUserDefinedFieldMaster_FlagTransactionDp` | TField |  | Flag Transaction DP Multifonds DB Column is FLG_TRANS_DP. |
| 18 | `FS.GA.USER.DEFINED.FIELD.MASTER.FLAG.TRANSACTION.TD` | `FsGaUserDefinedFieldMaster_FlagTransactionTd` | TField |  | Flag Transaction TD Multifonds DB Column is FLG_TRANS_TD. |
| 19 | `FS.GA.USER.DEFINED.FIELD.MASTER.FLAG.TRANSACTION.EM` | `FsGaUserDefinedFieldMaster_FlagTransactionEm` | TField |  | Flag Transaction EM Multifonds DB Column is FLG_TRANS_EM. |
| 20 | `FS.GA.USER.DEFINED.FIELD.MASTER.FLAG.TRANSACTION.FX` | `FsGaUserDefinedFieldMaster_FlagTransactionFx` | TField |  | Flag Transaction FX Multifonds DB Column is FLG_TRANS_FX. |
| 21 | `FS.GA.USER.DEFINED.FIELD.MASTER.FLAG.TRANSACTION.IR` | `FsGaUserDefinedFieldMaster_FlagTransactionIr` | TField |  | Flag Transaction IR Multifonds DB Column is FLG_TRANS_IR. |
| 22 | `FS.GA.USER.DEFINED.FIELD.MASTER.FLAG.TRANSACTION.EQS` | `FsGaUserDefinedFieldMaster_FlagTransactionEqs` | TField |  | Flag Transaction EQS Multifonds DB Column is FLG_TRANS_EQS. |
| 23 | `FS.GA.USER.DEFINED.FIELD.MASTER.FLAG.TRANSACTION.CFD` | `FsGaUserDefinedFieldMaster_FlagTransactionCfd` | TField |  | Flag Transaction CFD Multifonds DB Column is FLG_TRANS_CFD. |
| 24 | `FS.GA.USER.DEFINED.FIELD.MASTER.FLAG.TRANSACTION.DBCR` | `FsGaUserDefinedFieldMaster_FlagTransactionDbcr` | TField |  | Flag Transaction DBCR Multifonds DB Column is FLG_TRANS_DBCR. |
| 25 | `FS.GA.USER.DEFINED.FIELD.MASTER.RESERVED10` | `FsGaUserDefinedFieldMaster_Reserved10` | TField |  |  |
| 26 | `FS.GA.USER.DEFINED.FIELD.MASTER.RESERVED9` | `FsGaUserDefinedFieldMaster_Reserved9` | TField |  |  |
| 27 | `FS.GA.USER.DEFINED.FIELD.MASTER.RESERVED8` | `FsGaUserDefinedFieldMaster_Reserved8` | TField |  |  |
| 28 | `FS.GA.USER.DEFINED.FIELD.MASTER.RESERVED7` | `FsGaUserDefinedFieldMaster_Reserved7` | TField |  |  |
| 29 | `FS.GA.USER.DEFINED.FIELD.MASTER.RESERVED6` | `FsGaUserDefinedFieldMaster_Reserved6` | TField |  |  |
| 30 | `FS.GA.USER.DEFINED.FIELD.MASTER.RESERVED5` | `FsGaUserDefinedFieldMaster_Reserved5` | TField |  |  |
| 31 | `FS.GA.USER.DEFINED.FIELD.MASTER.RESERVED4` | `FsGaUserDefinedFieldMaster_Reserved4` | TField |  |  |
| 32 | `FS.GA.USER.DEFINED.FIELD.MASTER.RESERVED3` | `FsGaUserDefinedFieldMaster_Reserved3` | TField |  |  |
| 33 | `FS.GA.USER.DEFINED.FIELD.MASTER.RESERVED2` | `FsGaUserDefinedFieldMaster_Reserved2` | TField |  |  |
| 34 | `FS.GA.USER.DEFINED.FIELD.MASTER.RESERVED1` | `FsGaUserDefinedFieldMaster_Reserved1` | TField |  |  |
| 35 | `FS.GA.USER.DEFINED.FIELD.MASTER.LOCAL.REF` | `FsGaUserDefinedFieldMaster_LocalRef` |  |  |  |
| 36 | `FS.GA.USER.DEFINED.FIELD.MASTER.OVERRIDE` | `FsGaUserDefinedFieldMaster_Override` |  |  |  |
| 37 | `FS.GA.USER.DEFINED.FIELD.MASTER.RECORD.STATUS` | `FsGaUserDefinedFieldMaster_RecordStatus` | String |  |  |
| 38 | `FS.GA.USER.DEFINED.FIELD.MASTER.CURR.NO` | `FsGaUserDefinedFieldMaster_CurrNo` | String |  |  |
| 39 | `FS.GA.USER.DEFINED.FIELD.MASTER.INPUTTER` | `FsGaUserDefinedFieldMaster_Inputter` |  |  |  |
| 40 | `FS.GA.USER.DEFINED.FIELD.MASTER.DATE.TIME` | `FsGaUserDefinedFieldMaster_DateTime` |  |  |  |
| 41 | `FS.GA.USER.DEFINED.FIELD.MASTER.AUTHORISER` | `FsGaUserDefinedFieldMaster_Authoriser` | String |  |  |
| 42 | `FS.GA.USER.DEFINED.FIELD.MASTER.CO.CODE` | `FsGaUserDefinedFieldMaster_CoCode` | String |  |  |
| 43 | `FS.GA.USER.DEFINED.FIELD.MASTER.DEPT.CODE` | `FsGaUserDefinedFieldMaster_DeptCode` | String |  |  |
| 44 | `FS.GA.USER.DEFINED.FIELD.MASTER.AUDITOR.CODE` | `FsGaUserDefinedFieldMaster_AuditorCode` | String |  |  |
| 45 | `FS.GA.USER.DEFINED.FIELD.MASTER.AUDIT.DATE.TIME` | `FsGaUserDefinedFieldMaster_AuditDateTime` | String |  |  |
