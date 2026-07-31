# LBNCDR.LEGAL.FORM — Table Schema

> Source: `INSERTS/I_F.LBNCDR.LEGAL.FORM` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LF.DESCRIPTION` | `LbncdrLegalForm_Description` |  |  |  |
| 2 | `LF.FJ.TYPE` | `LbncdrLegalForm_FjType` | TField |  |  |
| 3 | `LF.FIELD.OBLIGATION` | `LbncdrLegalForm_FieldObligation` | TField |  |  |
| 4 | `LF.LEGAL.DOC` | `LbncdrLegalForm_LegalDoc` | TField | Yes | This Multi-value field can used to capture the Customer's Legal Documents. Validation Rules : Mandatory field, CheckFile: 'LBMB.H.LEGAL.DOC' Type : N Length : 5.1.C |
| 5 | `LF.ROLE` | `LbncdrLegalForm_Role` | TField |  |  |
| 6 | `LF.SHAREHOLDER.TYPE` | `LbncdrLegalForm_ShareholderType` | TField |  |  |
| 7 | `LF.BDL.CODE` | `LbncdrLegalForm_BdlCode` | TField |  |  |
| 8 | `LF.RESERVED.1` | `LbncdrLegalForm_Reserved1` | TField |  |  |
| 9 | `LF.RESERVED.2` | `LbncdrLegalForm_Reserved2` | TField |  |  |
| 10 | `LF.RESERVED.3` | `LbncdrLegalForm_Reserved3` | TField |  |  |
| 11 | `LF.RESERVED.4` | `LbncdrLegalForm_Reserved4` | TField |  |  |
| 12 | `LF.RESERVED.5` | `LbncdrLegalForm_Reserved5` | TField |  |  |
| 13 | `LF.RESERVED.6` | `LbncdrLegalForm_Reserved6` | TField |  |  |
| 14 | `LF.RESERVED.7` | `LbncdrLegalForm_Reserved7` | TField |  |  |
| 15 | `LF.RESERVED.8` | `LbncdrLegalForm_Reserved8` | TField |  |  |
| 16 | `LF.LOCAL.REF` | `LbncdrLegalForm_LocalRef` |  |  |  |
| 17 | `LF.OVERRIDE` | `LbncdrLegalForm_Override` |  |  |  |
| 18 | `LF.RECORD.STATUS` | `LbncdrLegalForm_RecordStatus` | String |  |  |
| 19 | `LF.CURR.NO` | `LbncdrLegalForm_CurrNo` | String |  |  |
| 20 | `LF.INPUTTER` | `LbncdrLegalForm_Inputter` |  |  |  |
| 21 | `LF.DATE.TIME` | `LbncdrLegalForm_DateTime` |  |  |  |
| 22 | `LF.AUTHORISER` | `LbncdrLegalForm_Authoriser` | String |  |  |
| 23 | `LF.CO.CODE` | `LbncdrLegalForm_CoCode` | String |  |  |
| 24 | `LF.DEPT.CODE` | `LbncdrLegalForm_DeptCode` | String |  |  |
| 25 | `LF.AUDITOR.CODE` | `LbncdrLegalForm_AuditorCode` | String |  |  |
| 26 | `LF.AUDIT.DATE.TIME` | `LbncdrLegalForm_AuditDateTime` | String |  |  |
