# DFE.MAPPING — Table Schema

> Source: `INSERTS/I_F.DFE.MAPPING` in `EB_Utility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DFE.MAP.FILE.NAME` | `DfeMapping_FileName` | TField |  |  |
| 2 | `DFE.MAP.FILE.SELECTION` | `DfeMapping_FileSelection` |  |  |  |
| 3 | `DFE.MAP.DESCRIPTION` | `DfeMapping_Description` |  |  |  |
| 4 | `DFE.MAP.FIELD.DELIM` | `DfeMapping_FieldDelim` | TField |  |  |
| 5 | `DFE.MAP.VM.DELIM` | `DfeMapping_VmDelim` | TField |  |  |
| 6 | `DFE.MAP.SM.DELIM` | `DfeMapping_SmDelim` | TField |  |  |
| 7 | `DFE.MAP.ID.GEN.TYPE` | `DfeMapping_IdGenType` | TField |  |  |
| 8 | `DFE.MAP.ID.ROUTINE` | `DfeMapping_IdRoutine` | TField |  |  |
| 9 | `DFE.MAP.ID.POSITION` | `DfeMapping_IdPosition` | TField |  |  |
| 10 | `DFE.MAP.ID.LENGTH` | `DfeMapping_IdLength` | TField |  |  |
| 11 | `DFE.MAP.IGNORE.LINE` | `DfeMapping_IgnoreLine` |  |  |  |
| 12 | `DFE.MAP.RECORD.FORMAT` | `DfeMapping_RecordFormat` | TField |  |  |
| 13 | `DFE.MAP.USER.DEF.RTN` | `DfeMapping_UserDefRtn` | TField |  |  |
| 14 | `DFE.MAP.APPL.FIELD.NAME` | `DfeMapping_ApplFieldName` |  |  |  |
| 15 | `DFE.MAP.APPL.FIELD.TEXT` | `DfeMapping_ApplFieldText` |  |  |  |
| 16 | `DFE.MAP.APPL.FIELD.POSN` | `DfeMapping_ApplFieldPosn` |  |  |  |
| 17 | `DFE.MAP.APPL.FIELD.TYPE` | `DfeMapping_ApplFieldType` |  |  |  |
| 18 | `DFE.MAP.APPL.MUL.FLD.POS` | `DfeMapping_ApplMulFldPos` |  |  |  |
| 19 | `DFE.MAP.APPL.SUB.FLD.POS` | `DfeMapping_ApplSubFldPos` |  |  |  |
| 20 | `DFE.MAP.APPL.FIELD.DEF` | `DfeMapping_ApplFieldDef` |  |  |  |
| 21 | `DFE.MAP.FIELD.POSITION` | `DfeMapping_FieldPosition` |  |  |  |
| 22 | `DFE.MAP.FIELD.LENGTH` | `DfeMapping_FieldLength` |  |  |  |
| 23 | `DFE.MAP.FIELD.OPERATION` | `DfeMapping_FieldOperation` |  |  |  |
| 24 | `DFE.MAP.FIELD.CONV` | `DfeMapping_FieldConv` |  |  |  |
| 25 | `DFE.MAP.FIELD.FORMAT` | `DfeMapping_FieldFormat` |  |  |  |
| 26 | `DFE.MAP.FIELD.NORMALIZE` | `DfeMapping_FieldNormalize` |  |  |  |
| 27 | `DFE.MAP.FIELD.ASSOC.TYPE` | `DfeMapping_FieldAssocType` |  |  |  |
| 28 | `DFE.MAP.XML.TAG.NAME` | `DfeMapping_XmlTagName` |  |  |  |
| 29 | `DFE.MAP.RESERVED.22` | `DfeMapping_Reserved22` |  |  |  |
| 30 | `DFE.MAP.PRE.PROCESS.RTN` | `DfeMapping_PreProcessRtn` | TField |  |  |
| 31 | `DFE.MAP.POST.UPDATE.RTN` | `DfeMapping_PostUpdateRtn` | TField |  |  |
| 32 | `DFE.MAP.INDIV.RECORD.RTN` | `DfeMapping_IndivRecordRtn` | TField |  |  |
| 33 | `DFE.MAP.ONLINE.RESP.RTN` | `DfeMapping_OnlineRespRtn` | TField |  |  |
| 34 | `DFE.MAP.LOCAL.REF` | `DfeMapping_LocalRef` |  |  |  |
| 35 | `DFE.MAP.INCL.NOINP.FLDS` | `DfeMapping_InclNoinpFlds` | TField |  |  |
| 36 | `DFE.MAP.RESERVED.18` | `DfeMapping_Reserved18` | TField |  |  |
| 37 | `DFE.MAP.RESERVED.17` | `DfeMapping_Reserved17` | TField |  |  |
| 38 | `DFE.MAP.RESERVED.16` | `DfeMapping_Reserved16` | TField |  |  |
| 39 | `DFE.MAP.RESERVED.15` | `DfeMapping_Reserved15` | TField |  |  |
| 40 | `DFE.MAP.RESERVED.14` | `DfeMapping_Reserved14` | TField |  |  |
| 41 | `DFE.MAP.RESERVED.12` | `DfeMapping_Reserved12` | TField |  |  |
| 42 | `DFE.MAP.RESERVED.10` | `DfeMapping_Reserved10` | TField |  |  |
| 43 | `DFE.MAP.RESERVED.8` | `DfeMapping_Reserved8` | TField |  |  |
| 44 | `DFE.MAP.RESERVED.6` | `DfeMapping_Reserved6` | TField |  |  |
| 45 | `DFE.MAP.RESERVED.4` | `DfeMapping_Reserved4` | TField |  |  |
| 46 | `DFE.MAP.RESERVED.2` | `DfeMapping_Reserved2` | TField |  |  |
| 47 | `DFE.MAP.RECORD.STATUS` | `DfeMapping_RecordStatus` | String |  |  |
| 48 | `DFE.MAP.CURR.NO` | `DfeMapping_CurrNo` | String |  |  |
| 49 | `DFE.MAP.INPUTTER` | `DfeMapping_Inputter` |  |  |  |
| 50 | `DFE.MAP.DATE.TIME` | `DfeMapping_DateTime` |  |  |  |
| 51 | `DFE.MAP.AUTHORISER` | `DfeMapping_Authoriser` | String |  |  |
| 52 | `DFE.MAP.CO.CODE` | `DfeMapping_CoCode` | String |  |  |
| 53 | `DFE.MAP.DEPT.CODE` | `DfeMapping_DeptCode` | String |  |  |
| 54 | `DFE.MAP.AUDITOR.CODE` | `DfeMapping_AuditorCode` | String |  |  |
| 55 | `DFE.MAP.AUDIT.DATE.TIME` | `DfeMapping_AuditDateTime` | String |  |  |
