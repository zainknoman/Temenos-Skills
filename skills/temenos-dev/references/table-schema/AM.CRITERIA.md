# AM.CRITERIA — Table Schema

> Source: `INSERTS/I_F.AM.CRITERIA` in `AM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.CRI.DESCRIPTION` | `AmCriteria_Description` |  |  |  |
| 2 | `AM.CRI.FILE.NAME` | `AmCriteria_FileName` | A (alphanumeric) | Yes | Defines the datafile to which the criteria field names will relate. This should be a filename without the "Fxxx" prefix. The data filename specified here must be a valid entry on the F.STANDARD.SELECTION file. Validation Rules: 1-32 type A (alphanumeric) characters Mandatory input |
| 3 | `AM.CRI.DESC.FIELD` | `AmCriteria_DescField` | A (alphanumeric) | Yes | Defines the field name display as description in the preview enquiry. The field name specified here must be a field of the file describe in FILE.NAME. Validation Rules: 1-30 type A (alphanumeric) characters. Mandatory input |
| 4 | `AM.CRI.SEL.FIELD` | `AmCriteria_SelField` |  |  |  |
| 5 | `AM.CRI.SEL.OPERAND` | `AmCriteria_SelOperand` |  |  |  |
| 6 | `AM.CRI.SEL.VALUE` | `AmCriteria_SelValue` |  |  |  |
| 7 | `AM.CRI.SEL.SUB.FUNC` | `AmCriteria_SelSubFunc` |  |  |  |
| 8 | `AM.CRI.SEL.MAIN.FUNC` | `AmCriteria_SelMainFunc` |  |  |  |
| 9 | `AM.CRI.SELECTION.RTN` | `AmCriteria_SelectionRtn` | TField |  | Accepts a valid routine for selection criteria. This routine will have three arguments in the following order: AM.CIRTERIA ID (IN), respective AM.CRITERIA record (IN) and Return list (OUT). The return list must be list of AM.GROUP.PORT ID�s with field marker as delimiter. |
| 10 | `AM.CRI.RTN.OPERAND` | `AmCriteria_RtnOperand` | TField |  | Free text field. Validation Rules: Alphanumeric |
| 11 | `AM.CRI.RTN.VALUE` | `AmCriteria_RtnValue` | TField |  | Free text field. Validation Rules: Alphanumeric |
| 12 | `AM.CRI.RESERVED07` | `AmCriteria_Reserved07` | TField |  |  |
| 13 | `AM.CRI.RESERVED06` | `AmCriteria_Reserved06` | TField |  |  |
| 14 | `AM.CRI.RESERVED05` | `AmCriteria_Reserved05` | TField |  |  |
| 15 | `AM.CRI.RESERVED04` | `AmCriteria_Reserved04` | TField |  |  |
| 16 | `AM.CRI.RESERVED03` | `AmCriteria_Reserved03` | TField |  |  |
| 17 | `AM.CRI.RESERVED02` | `AmCriteria_Reserved02` | TField |  |  |
| 18 | `AM.CRI.RESERVED01` | `AmCriteria_Reserved01` | TField |  |  |
| 19 | `AM.CRI.LOCAL.REF` | `AmCriteria_LocalRef` |  |  |  |
| 20 | `AM.CRI.RECORD.STATUS` | `AmCriteria_RecordStatus` | String |  |  |
| 21 | `AM.CRI.CURR.NO` | `AmCriteria_CurrNo` | String |  |  |
| 22 | `AM.CRI.INPUTTER` | `AmCriteria_Inputter` |  |  |  |
| 23 | `AM.CRI.DATE.TIME` | `AmCriteria_DateTime` |  |  |  |
| 24 | `AM.CRI.AUTHORISER` | `AmCriteria_Authoriser` | String |  |  |
| 25 | `AM.CRI.CO.CODE` | `AmCriteria_CoCode` | String |  |  |
| 26 | `AM.CRI.DEPT.CODE` | `AmCriteria_DeptCode` | String |  |  |
| 27 | `AM.CRI.AUDITOR.CODE` | `AmCriteria_AuditorCode` | String |  |  |
| 28 | `AM.CRI.AUDIT.DATE.TIME` | `AmCriteria_AuditDateTime` | String |  |  |
