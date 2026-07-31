# SC.INCOME.CODES — Table Schema

> Source: `INSERTS/I_F.SC.INCOME.CODES` in `SC_SccEventCapture.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.INC.CODE.DESCRIPTION` | `ScIncomeCodes_Description` |  |  |  |
| 2 | `SC.INC.CODE.TAXABLE` | `ScIncomeCodes_Taxable` |  |  |  |
| 3 | `SC.INC.CODE.REPORTABLE` | `ScIncomeCodes_Reportable` |  |  |  |
| 4 | `SC.INC.CODE.SOURCE.OR.LOCAL` | `ScIncomeCodes_SourceOrLocal` |  |  |  |
| 5 | `SC.INC.CODE.TYPE.OF.INCOME` | `ScIncomeCodes_TypeOfIncome` | TField |  | Field to hold the category (type) of Income Validation Rules: Inputtable upto 35 characters. |
| 6 | `SC.INC.CODE.RESERVED.15` | `ScIncomeCodes_Reserved15` | TField |  |  |
| 7 | `SC.INC.CODE.RESERVED.14` | `ScIncomeCodes_Reserved14` | TField |  |  |
| 8 | `SC.INC.CODE.RESERVED.13` | `ScIncomeCodes_Reserved13` | TField |  |  |
| 9 | `SC.INC.CODE.RESERVED.12` | `ScIncomeCodes_Reserved12` | TField |  |  |
| 10 | `SC.INC.CODE.RESERVED.11` | `ScIncomeCodes_Reserved11` | TField |  |  |
| 11 | `SC.INC.CODE.RESERVED.10` | `ScIncomeCodes_Reserved10` | TField |  |  |
| 12 | `SC.INC.CODE.RESERVED.9` | `ScIncomeCodes_Reserved9` | TField |  |  |
| 13 | `SC.INC.CODE.RESERVED.8` | `ScIncomeCodes_Reserved8` | TField |  |  |
| 14 | `SC.INC.CODE.RESERVED.7` | `ScIncomeCodes_Reserved7` | TField |  |  |
| 15 | `SC.INC.CODE.RESERVED.6` | `ScIncomeCodes_Reserved6` | TField |  |  |
| 16 | `SC.INC.CODE.RESERVED.5` | `ScIncomeCodes_Reserved5` | TField |  |  |
| 17 | `SC.INC.CODE.RESERVED.4` | `ScIncomeCodes_Reserved4` | TField |  |  |
| 18 | `SC.INC.CODE.RESERVED.3` | `ScIncomeCodes_Reserved3` | TField |  |  |
| 19 | `SC.INC.CODE.RESERVED.2` | `ScIncomeCodes_Reserved2` | TField |  |  |
| 20 | `SC.INC.CODE.RESERVED.1` | `ScIncomeCodes_Reserved1` | TField |  |  |
| 21 | `SC.INC.CODE.LOCAL.REF` | `ScIncomeCodes_LocalRef` |  |  |  |
| 22 | `SC.INC.CODE.OVERRIDE` | `ScIncomeCodes_Override` |  |  |  |
| 23 | `SC.INC.CODE.RECORD.STATUS` | `ScIncomeCodes_RecordStatus` | String |  |  |
| 24 | `SC.INC.CODE.CURR.NO` | `ScIncomeCodes_CurrNo` | String |  |  |
| 25 | `SC.INC.CODE.INPUTTER` | `ScIncomeCodes_Inputter` |  |  |  |
| 26 | `SC.INC.CODE.DATE.TIME` | `ScIncomeCodes_DateTime` |  |  |  |
| 27 | `SC.INC.CODE.AUTHORISER` | `ScIncomeCodes_Authoriser` | String |  |  |
| 28 | `SC.INC.CODE.CO.CODE` | `ScIncomeCodes_CoCode` | String |  |  |
| 29 | `SC.INC.CODE.DEPT.CODE` | `ScIncomeCodes_DeptCode` | String |  |  |
| 30 | `SC.INC.CODE.AUDITOR.CODE` | `ScIncomeCodes_AuditorCode` | String |  |  |
| 31 | `SC.INC.CODE.AUDIT.DATE.TIME` | `ScIncomeCodes_AuditDateTime` | String |  |  |
| 32 | `SC.INC.CODE.SHORT.DESC` | `ScIncomeCodes_ShortDesc` |  |  |  |
| 33 | `SC.INC.CODE.COMPANY.ID` | `ScIncomeCodes_CompanyId` |  |  |  |
