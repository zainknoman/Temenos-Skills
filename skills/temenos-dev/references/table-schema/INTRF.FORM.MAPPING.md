# INTRF.FORM.MAPPING — Table Schema

> Source: `INSERTS/I_F.INTRF.FORM.MAPPING` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INTRF.FM.SHORT.DESCRP` | `IntrfFormMapping_ShortDescrp` |  |  |  |
| 2 | `INTRF.FM.DESCRIPTION` | `IntrfFormMapping_Description` |  |  |  |
| 3 | `INTRF.FM.DATA.TYPE` | `IntrfFormMapping_DataType` |  |  |  |
| 4 | `INTRF.FM.DATA.LENGTH` | `IntrfFormMapping_DataLength` |  |  |  |
| 5 | `INTRF.FM.OPT.MAN` | `IntrfFormMapping_OptMan` |  |  |  |
| 6 | `INTRF.FM.INTRF.FLD.NAME` | `IntrfFormMapping_IntrfFldName` |  |  |  |
| 7 | `INTRF.FM.INTRF.FLD.LN.TYPE` | `IntrfFormMapping_IntrfFldLnType` |  |  |  |
| 8 | `INTRF.FM.INTRF.FLD.FMT` | `IntrfFormMapping_IntrfFldFmt` |  |  |  |
| 9 | `INTRF.FM.FLD.ST.END` | `IntrfFormMapping_FldStEnd` |  |  |  |
| 10 | `INTRF.FM.PREV.VAL.CNT` | `IntrfFormMapping_PrevValCnt` |  |  |  |
| 11 | `INTRF.FM.GLO.FLD.NAME` | `IntrfFormMapping_GloFldName` |  |  |  |
| 12 | `INTRF.FM.GLO.CONST` | `IntrfFormMapping_GloConst` |  |  |  |
| 13 | `INTRF.FM.Reserved.1` | `IntrfFormMapping_Reserved1` |  |  |  |
| 14 | `INTRF.FM.INTRF.FLD.POS` | `IntrfFormMapping_IntrfFldPos` |  |  |  |
| 15 | `INTRF.FM.FIELD.SOURCE` | `IntrfFormMapping_FieldSource` |  |  |  |
| 16 | `INTRF.FM.FIELD.SRC.VALUE` | `IntrfFormMapping_FieldSrcValue` |  |  |  |
| 17 | `INTRF.FM.OFS.POST.ROUTINE` | `IntrfFormMapping_OfsPostRoutine` |  |  |  |
| 18 | `INTRF.FM.RESERVED.9` | `IntrfFormMapping_Reserved9` |  |  |  |
| 19 | `INTRF.FM.RESERVED.8` | `IntrfFormMapping_Reserved8` |  |  |  |
| 20 | `INTRF.FM.RESERVED.7` | `IntrfFormMapping_Reserved7` |  |  |  |
| 21 | `INTRF.FM.RESERVED.6` | `IntrfFormMapping_Reserved6` |  |  |  |
| 22 | `INTRF.FM.RESERVED.5` | `IntrfFormMapping_Reserved5` |  |  |  |
| 23 | `INTRF.FM.RESERVED.4` | `IntrfFormMapping_Reserved4` |  |  |  |
| 24 | `INTRF.FM.RESERVED.3` | `IntrfFormMapping_Reserved3` |  |  |  |
| 25 | `INTRF.FM.RESERVED.2` | `IntrfFormMapping_Reserved2` |  |  |  |
| 26 | `INTRF.FM.RESERVED.1` | `IntrfFormMapping_Reserved1` |  |  |  |
| 27 | `INTRF.FM.LOCAL.REF` | `IntrfFormMapping_LocalRef` |  |  |  |
| 28 | `INTRF.FM.OVERRIDE` | `IntrfFormMapping_Override` |  |  |  |
| 29 | `INTRF.FM.RECORD.STATUS` | `IntrfFormMapping_RecordStatus` |  |  |  |
| 30 | `INTRF.FM.CURR.NO` | `IntrfFormMapping_CurrNo` |  |  |  |
| 31 | `INTRF.FM.INPUTTER` | `IntrfFormMapping_Inputter` |  |  |  |
| 32 | `INTRF.FM.DATE.TIME` | `IntrfFormMapping_DateTime` |  |  |  |
| 33 | `INTRF.FM.AUTHORISER` | `IntrfFormMapping_Authoriser` |  |  |  |
| 34 | `INTRF.FM.CO.CODE` | `IntrfFormMapping_CoCode` |  |  |  |
| 35 | `INTRF.FM.DEPT.CODE` | `IntrfFormMapping_DeptCode` |  |  |  |
| 36 | `INTRF.FM.AUDITOR.CODE` | `IntrfFormMapping_AuditorCode` |  |  |  |
| 37 | `INTRF.FM.AUDIT.DATE.TIME` | `IntrfFormMapping_AuditDateTime` |  |  |  |
