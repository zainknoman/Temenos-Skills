# PAYRCN.PARAMETER — Table Schema

> Source: `INSERTS/I_F.PAYRCN.PARAMETER` in `FINEXT_ATMRECON.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PAYRCN.DESCRIPTION` | `PayrcnParameter_Description` |  |  |  |
| 2 | `PAYRCN.INT.APP.NAME` | `PayrcnParameter_IntAppName` |  |  |  |
| 3 | `PAYRCN.ADD.INFO.FIELD` | `PayrcnParameter_AddInfoField` |  |  |  |
| 4 | `PAYRCN.INFO.FLD.DELIMETER` | `PayrcnParameter_InfoFldDelimeter` |  |  |  |
| 5 | `PAYRCN.RELATED.FILE` | `PayrcnParameter_RelatedFile` |  |  |  |
| 6 | `PAYRCN.RESERVED.15` | `PayrcnParameter_Reserved15` |  |  |  |
| 7 | `PAYRCN.RESERVED.14` | `PayrcnParameter_Reserved14` |  |  |  |
| 8 | `PAYRCN.RESERVED.13` | `PayrcnParameter_Reserved13` |  |  |  |
| 9 | `PAYRCN.RESERVED.12` | `PayrcnParameter_Reserved12` |  |  |  |
| 10 | `PAYRCN.RESERVED.11` | `PayrcnParameter_Reserved11` |  |  |  |
| 11 | `PAYRCN.INFO.FIELD.POSITION` | `PayrcnParameter_InfoFieldPosition` |  |  |  |
| 12 | `PAYRCN.INFO.FIELD.NAME` | `PayrcnParameter_InfoFieldName` |  |  |  |
| 13 | `PAYRCN.REL.FIELD.POSITION` | `PayrcnParameter_RelFieldPosition` |  |  |  |
| 14 | `PAYRCN.REL.FIELD.NAME` | `PayrcnParameter_RelFieldName` |  |  |  |
| 15 | `PAYRCN.REL.FIELD.RTN` | `PayrcnParameter_RelFieldRtn` |  |  |  |
| 16 | `PAYRCN.RESERVED.10` | `PayrcnParameter_Reserved10` |  |  |  |
| 17 | `PAYRCN.RESERVED.9` | `PayrcnParameter_Reserved9` |  |  |  |
| 18 | `PAYRCN.RESERVED.8` | `PayrcnParameter_Reserved8` |  |  |  |
| 19 | `PAYRCN.RESERVED.7` | `PayrcnParameter_Reserved7` |  |  |  |
| 20 | `PAYRCN.RESERVED.6` | `PayrcnParameter_Reserved6` |  |  |  |
| 21 | `PAYRCN.MATCH.MULTIPLE` | `PayrcnParameter_MatchMultiple` | TField |  |  |
| 22 | `PAYRCN.CUTOFF.TIME` | `PayrcnParameter_CutoffTime` | TField |  |  |
| 23 | `PAYRCN.BASE.DATE` | `PayrcnParameter_BaseDate` | TField |  |  |
| 24 | `PAYRCN.MATCH.FILE` | `PayrcnParameter_MatchFile` |  |  |  |
| 25 | `PAYRCN.RETENTION.BASE.FIELD` | `PayrcnParameter_RetentionBaseField` |  |  |  |
| 26 | `PAYRCN.RETENTION.DAYS` | `PayrcnParameter_RetentionDays` |  |  |  |
| 27 | `PAYRCN.MATCH.FIELD` | `PayrcnParameter_MatchField` |  |  |  |
| 28 | `PAYRCN.MATCH.FIELD.POS` | `PayrcnParameter_MatchFieldPos` |  |  |  |
| 29 | `PAYRCN.TOLERANCE.CCY` | `PayrcnParameter_ToleranceCcy` |  |  |  |
| 30 | `PAYRCN.TOLERANCE.AMT` | `PayrcnParameter_ToleranceAmt` |  |  |  |
| 31 | `PAYRCN.ITEMS.FLD.NAME` | `PayrcnParameter_ItemsFldName` | TField |  |  |
| 32 | `PAYRCN.ITEMS.FLD.VALUE` | `PayrcnParameter_ItemsFldValue` |  |  |  |
| 33 | `PAYRCN.RESERVED.16` | `PayrcnParameter_Reserved16` |  |  |  |
| 34 | `PAYRCN.RESERVED.17` | `PayrcnParameter_Reserved17` |  |  |  |
| 35 | `PAYRCN.RESERVED.18` | `PayrcnParameter_Reserved18` |  |  |  |
| 36 | `PAYRCN.ITEMS.MAPPING` | `PayrcnParameter_ItemsMapping` |  |  |  |
| 37 | `PAYRCN.RESERVED.5` | `PayrcnParameter_Reserved5` | TField |  |  |
| 38 | `PAYRCN.RESERVED.4` | `PayrcnParameter_Reserved4` | TField |  |  |
| 39 | `PAYRCN.RESERVED.3` | `PayrcnParameter_Reserved3` | TField |  |  |
| 40 | `PAYRCN.RESERVED.2` | `PayrcnParameter_Reserved2` | TField |  |  |
| 41 | `PAYRCN.RESERVED.1` | `PayrcnParameter_Reserved1` | TField |  |  |
| 42 | `PAYRCN.RECORD.STATUS` | `PayrcnParameter_RecordStatus` | String |  |  |
| 43 | `PAYRCN.CURR.NO` | `PayrcnParameter_CurrNo` | String |  |  |
| 44 | `PAYRCN.INPUTTER` | `PayrcnParameter_Inputter` |  |  |  |
| 45 | `PAYRCN.DATE.TIME` | `PayrcnParameter_DateTime` |  |  |  |
| 46 | `PAYRCN.AUTHORISER` | `PayrcnParameter_Authoriser` | String |  |  |
| 47 | `PAYRCN.CO.CODE` | `PayrcnParameter_CoCode` | String |  |  |
| 48 | `PAYRCN.DEPT.CODE` | `PayrcnParameter_DeptCode` | String |  |  |
| 49 | `PAYRCN.AUDITOR.CODE` | `PayrcnParameter_AuditorCode` | String |  |  |
| 50 | `PAYRCN.AUDIT.DATE.TIME` | `PayrcnParameter_AuditDateTime` | String |  |  |
