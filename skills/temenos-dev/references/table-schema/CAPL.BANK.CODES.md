# CAPL.BANK.CODES — Table Schema

> Source: `INSERTS/I_F.CAPL.BANK.CODES` in `CARGPL_RegisteredPlans.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.BC.INSTITUTION.TYPE` | `CaplBankCodes_InstitutionType` |  |  |  |
| 2 | `CAPL.BC.INSTITUTION.NAME` | `CaplBankCodes_InstitutionName` |  |  |  |
| 3 | `CAPL.BC.RESERVED.10` | `CaplBankCodes_Reserved10` |  |  |  |
| 4 | `CAPL.BC.RESERVED.9` | `CaplBankCodes_Reserved9` |  |  |  |
| 5 | `CAPL.BC.RESERVED.8` | `CaplBankCodes_Reserved8` |  |  |  |
| 6 | `CAPL.BC.RESERVED.7` | `CaplBankCodes_Reserved7` |  |  |  |
| 7 | `CAPL.BC.RESERVED.6` | `CaplBankCodes_Reserved6` |  |  |  |
| 8 | `CAPL.BC.RESERVED.5` | `CaplBankCodes_Reserved5` |  |  |  |
| 9 | `CAPL.BC.RESERVED.4` | `CaplBankCodes_Reserved4` |  |  |  |
| 10 | `CAPL.BC.RESERVED.3` | `CaplBankCodes_Reserved3` |  |  |  |
| 11 | `CAPL.BC.RESERVED.2` | `CaplBankCodes_Reserved2` |  |  |  |
| 12 | `CAPL.BC.RESERVED.1` | `CaplBankCodes_Reserved1` |  |  |  |
| 13 | `CAPL.BC.LOCAL.REF` | `CaplBankCodes_LocalRef` |  |  |  |
| 14 | `CAPL.BC.OVERRIDE` | `CaplBankCodes_Override` |  |  |  |
| 15 | `CAPL.BC.RECORD.STATUS` | `CaplBankCodes_RecordStatus` |  |  |  |
| 16 | `CAPL.BC.CURR.NO` | `CaplBankCodes_CurrNo` |  |  |  |
| 17 | `CAPL.BC.INPUTTER` | `CaplBankCodes_Inputter` |  |  |  |
| 18 | `CAPL.BC.DATE.TIME` | `CaplBankCodes_DateTime` |  |  |  |
| 19 | `CAPL.BC.AUTHORISER` | `CaplBankCodes_Authoriser` |  |  |  |
| 20 | `CAPL.BC.CO.CODE` | `CaplBankCodes_CoCode` |  |  |  |
| 21 | `CAPL.BC.DEPT.CODE` | `CaplBankCodes_DeptCode` |  |  |  |
| 22 | `CAPL.BC.AUDITOR.CODE` | `CaplBankCodes_AuditorCode` |  |  |  |
| 23 | `CAPL.BC.AUDIT.DATE.TIME` | `CaplBankCodes_AuditDateTime` |  |  |  |
