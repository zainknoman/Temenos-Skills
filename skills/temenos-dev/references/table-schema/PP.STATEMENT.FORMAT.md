# PP.STATEMENT.FORMAT — Table Schema

> Source: `INSERTS/I_F.PP.STATEMENT.FORMAT` in `PP_PostingSchemeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.STF.CompanyID` | `PpStatementFormat_Companyid` | TField | Yes | Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: Mandatory field 3 alphanumeric characters. The value links to the field �CompanyID� in PPT.COMPANY |
| 2 | `PP.STF.SequenceNumber` | `PpStatementFormat_Sequencenumber` |  |  |  |
| 3 | `PP.STF.Tag61Indicator` | `PpStatementFormat_Tag61indicator` |  |  |  |
| 4 | `PP.STF.RESERVED.6` | `PpStatementFormat_Reserved6` |  |  |  |
| 5 | `PP.STF.LiteralText` | `PpStatementFormat_Literaltext` |  |  |  |
| 6 | `PP.STF.StatementTextToken` | `PpStatementFormat_Statementtexttoken` |  |  |  |
| 7 | `PP.STF.StartPosition` | `PpStatementFormat_Startposition` |  |  |  |
| 8 | `PP.STF.AmountFormat` | `PpStatementFormat_Amountformat` |  |  |  |
| 9 | `PP.STF.LineContinuityFlag` | `PpStatementFormat_Linecontinuityflag` |  |  |  |
| 10 | `PP.STF.CompactLineFlag` | `PpStatementFormat_Compactlineflag` |  |  |  |
| 11 | `PP.STF.AuthoriserDateTime` | `PpStatementFormat_Authoriserdatetime` | TField |  |  |
| 12 | `PP.STF.RESERVED.5` | `PpStatementFormat_Reserved5` | TField |  | Standard T24 field. Reserved for future use |
| 13 | `PP.STF.RESERVED.4` | `PpStatementFormat_Reserved4` | TField |  | Standard T24 field. Reserved for future use |
| 14 | `PP.STF.RESERVED.3` | `PpStatementFormat_Reserved3` | TField |  | Standard T24 field. Reserved for future use |
| 15 | `PP.STF.RESERVED.2` | `PpStatementFormat_Reserved2` | TField |  | Standard T24 field. Reserved for future use |
| 16 | `PP.STF.RESERVED.1` | `PpStatementFormat_Reserved1` | TField |  | Standard T24 field. Reserved for future use |
| 17 | `PP.STF.LOCAL.REF` | `PpStatementFormat_LocalRef` |  |  |  |
| 18 | `PP.STF.OVERRIDE` | `PpStatementFormat_Override` |  |  |  |
| 19 | `PP.STF.RECORD.STATUS` | `PpStatementFormat_RecordStatus` | String |  |  |
| 20 | `PP.STF.CURR.NO` | `PpStatementFormat_CurrNo` | String |  |  |
| 21 | `PP.STF.INPUTTER` | `PpStatementFormat_Inputter` |  |  |  |
| 22 | `PP.STF.DATE.TIME` | `PpStatementFormat_DateTime` |  |  |  |
| 23 | `PP.STF.AUTHORISER` | `PpStatementFormat_Authoriser` | String |  |  |
| 24 | `PP.STF.CO.CODE` | `PpStatementFormat_CoCode` | String |  |  |
| 25 | `PP.STF.DEPT.CODE` | `PpStatementFormat_DeptCode` | String |  |  |
| 26 | `PP.STF.AUDITOR.CODE` | `PpStatementFormat_AuditorCode` | String |  |  |
| 27 | `PP.STF.AUDIT.DATE.TIME` | `PpStatementFormat_AuditDateTime` | String |  |  |
