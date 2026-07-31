# CMBASE.BATCH.INTRF.SELECT.CRITERIA — Table Schema

> Source: `INSERTS/I_F.CMBASE.BATCH.INTRF.SELECT.CRITERIA` in `CMBASE_InterfaceBatchExtract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CMBASE.INTRF.SEL.OPEN.BRACKET` | `CmbaseBatchIntrfSelectCriteria_OpenBracket` |  |  |  |
| 2 | `CMBASE.INTRF.SEL.SEL.FIELD` | `CmbaseBatchIntrfSelectCriteria_SelField` |  |  |  |
| 3 | `CMBASE.INTRF.SEL.SEL.FIELD.OPERATION` | `CmbaseBatchIntrfSelectCriteria_SelFieldOperation` |  |  |  |
| 4 | `CMBASE.INTRF.SEL.SEL.FIELD.VALUE` | `CmbaseBatchIntrfSelectCriteria_SelFieldValue` |  |  |  |
| 5 | `CMBASE.INTRF.SEL.CLOSE.BRACKET` | `CmbaseBatchIntrfSelectCriteria_CloseBracket` |  |  |  |
| 6 | `CMBASE.INTRF.SEL.NEXT.ITEM` | `CmbaseBatchIntrfSelectCriteria_NextItem` |  |  |  |
| 7 | `CMBASE.INTRF.SEL.RESERVED.10` | `CmbaseBatchIntrfSelectCriteria_Reserved10` | TField |  | This field is reserved for future use |
| 8 | `CMBASE.INTRF.SEL.RESERVED.9` | `CmbaseBatchIntrfSelectCriteria_Reserved9` | TField |  | This field is reserved for future use |
| 9 | `CMBASE.INTRF.SEL.RESERVED.8` | `CmbaseBatchIntrfSelectCriteria_Reserved8` | TField |  | This field is reserved for future use |
| 10 | `CMBASE.INTRF.SEL.RESERVED.7` | `CmbaseBatchIntrfSelectCriteria_Reserved7` | TField |  | This field is reserved for future use |
| 11 | `CMBASE.INTRF.SEL.RESERVED.6` | `CmbaseBatchIntrfSelectCriteria_Reserved6` | TField |  | This field is reserved for future use |
| 12 | `CMBASE.INTRF.SEL.RESERVED.5` | `CmbaseBatchIntrfSelectCriteria_Reserved5` | TField |  | This field is reserved for future use |
| 13 | `CMBASE.INTRF.SEL.RESERVED.4` | `CmbaseBatchIntrfSelectCriteria_Reserved4` | TField |  | This field is reserved for future use |
| 14 | `CMBASE.INTRF.SEL.RESERVED.3` | `CmbaseBatchIntrfSelectCriteria_Reserved3` | TField |  | This field is reserved for future use |
| 15 | `CMBASE.INTRF.SEL.RESERVED.2` | `CmbaseBatchIntrfSelectCriteria_Reserved2` | TField |  | This field is reserved for future use |
| 16 | `CMBASE.INTRF.SEL.RESERVED.1` | `CmbaseBatchIntrfSelectCriteria_Reserved1` | TField |  | This field is reserved for future use |
| 17 | `CMBASE.INTRF.SEL.LOCAL.REF` | `CmbaseBatchIntrfSelectCriteria_LocalRef` |  |  |  |
| 18 | `CMBASE.INTRF.SEL.OVERRIDE` | `CmbaseBatchIntrfSelectCriteria_Override` |  |  |  |
| 19 | `CMBASE.INTRF.SEL.RECORD.STATUS` | `CmbaseBatchIntrfSelectCriteria_RecordStatus` | String |  |  |
| 20 | `CMBASE.INTRF.SEL.CURR.NO` | `CmbaseBatchIntrfSelectCriteria_CurrNo` | String |  |  |
| 21 | `CMBASE.INTRF.SEL.INPUTTER` | `CmbaseBatchIntrfSelectCriteria_Inputter` |  |  |  |
| 22 | `CMBASE.INTRF.SEL.DATE.TIME` | `CmbaseBatchIntrfSelectCriteria_DateTime` |  |  |  |
| 23 | `CMBASE.INTRF.SEL.AUTHORISER` | `CmbaseBatchIntrfSelectCriteria_Authoriser` | String |  |  |
| 24 | `CMBASE.INTRF.SEL.CO.CODE` | `CmbaseBatchIntrfSelectCriteria_CoCode` | String |  |  |
| 25 | `CMBASE.INTRF.SEL.DEPT.CODE` | `CmbaseBatchIntrfSelectCriteria_DeptCode` | String |  |  |
| 26 | `CMBASE.INTRF.SEL.AUDITOR.CODE` | `CmbaseBatchIntrfSelectCriteria_AuditorCode` | String |  |  |
| 27 | `CMBASE.INTRF.SEL.AUDIT.DATE.TIME` | `CmbaseBatchIntrfSelectCriteria_AuditDateTime` | String |  |  |
