# TX.TXN.BASE.PARMS — Table Schema

> Source: `INSERTS/I_F.TX.TXN.BASE.PARMS` in `TX_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TE.TBP.TXN.BASE.ID` | `TxTxnBaseParms_TxnBaseId` |  |  |  |
| 2 | `TE.TBP.FIELD.NAME` | `TxTxnBaseParms_FieldName` |  |  |  |
| 3 | `TE.TBP.FIELD.TYPE` | `TxTxnBaseParms_FieldType` |  |  |  |
| 4 | `TE.TBP.FIELD.FMT` | `TxTxnBaseParms_FieldFmt` |  |  |  |
| 5 | `TE.TBP.FLD.VAL.RTN` | `TxTxnBaseParms_FldValRtn` |  |  |  |
| 6 | `TE.TBP.MVAL` | `TxTxnBaseParms_Mval` |  |  |  |
| 7 | `TE.TBP.SVAL` | `TxTxnBaseParms_Sval` |  |  |  |
| 8 | `TE.TBP.ASOCFLD` | `TxTxnBaseParms_Asocfld` |  |  |  |
| 9 | `TE.TBP.REV.ACTION` | `TxTxnBaseParms_RevAction` | TField |  | This field indicates whether the history details need to stored or not in the TXN.BASE file that is being created. Validations : 'ACTION' or 'DELETE' 'ACTION' - stores the history details whereas 'DELETE' does not. |
| 10 | `TE.TBP.SORT.FIELD` | `TxTxnBaseParms_SortField` | TField |  | Specifies the Sorting field, based on which TXN.BASE file data will be sorted. Validations : Should be a valid field defined in FIELD.NAME other than the defaulted fields (TXN.ID, TXN.STATUS ,EVENT.ID,COMPANY) |
| 11 | `TE.TBP.PREFIX` | `TxTxnBaseParms_Prefix` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 12 | `TE.TBP.MAINT.HIST` | `TxTxnBaseParms_MaintHist` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 13 | `TE.TBP.RESERVED8` | `TxTxnBaseParms_Reserved8` | TField |  |  |
| 14 | `TE.TBP.RESERVED7` | `TxTxnBaseParms_Reserved7` | TField |  |  |
| 15 | `TE.TBP.RESERVED6` | `TxTxnBaseParms_Reserved6` | TField |  |  |
| 16 | `TE.TBP.RESERVED5` | `TxTxnBaseParms_Reserved5` | TField |  |  |
| 17 | `TE.TBP.RESERVED4` | `TxTxnBaseParms_Reserved4` | TField |  |  |
| 18 | `TE.TBP.RESERVED3` | `TxTxnBaseParms_Reserved3` | TField |  |  |
| 19 | `TE.TBP.RESERVED2` | `TxTxnBaseParms_Reserved2` | TField |  |  |
| 20 | `TE.TBP.LOCAL.REF` | `TxTxnBaseParms_LocalRef` |  |  |  |
| 21 | `TE.TBP.OVERRIDE` | `TxTxnBaseParms_Override` |  |  |  |
| 22 | `TE.TBP.RECORD.STATUS` | `TxTxnBaseParms_RecordStatus` | String |  |  |
| 23 | `TE.TBP.CURR.NO` | `TxTxnBaseParms_CurrNo` | String |  |  |
| 24 | `TE.TBP.INPUTTER` | `TxTxnBaseParms_Inputter` |  |  |  |
| 25 | `TE.TBP.DATE.TIME` | `TxTxnBaseParms_DateTime` |  |  |  |
| 26 | `TE.TBP.AUTHORISER` | `TxTxnBaseParms_Authoriser` | String |  |  |
| 27 | `TE.TBP.CO.CODE` | `TxTxnBaseParms_CoCode` | String |  |  |
| 28 | `TE.TBP.DEPT.CODE` | `TxTxnBaseParms_DeptCode` | String |  |  |
| 29 | `TE.TBP.AUDITOR.CODE` | `TxTxnBaseParms_AuditorCode` | String |  |  |
| 30 | `TE.TBP.AUDIT.DATE.TIME` | `TxTxnBaseParms_AuditDateTime` | String |  |  |
