# CAMB.COF.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CAMB.COF.PARAMETER` in `CAATMI_EverlinkATMInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.COF.EXT.COMPANY` | `CambCofParameter_ExtCompany` |  |  |  |
| 2 | `CAMB.COF.COMPANY.WISE` | `CambCofParameter_CompanyWise` | TField |  | It is a Yes/No field used to define whether lead company wise extract has to be produced or consolidated extract has to be produced.If 'YES' parameterised Lead Company Wise extract generated, otherwise single extract file generated with all parameterised Lead company data. |
| 3 | `CAMB.COF.REORDER.STATUS` | `CambCofParameter_ReorderStatus` | TField |  | During reorder\renewal CARD.ISSUE status will be updated from 13 to this parameterised status.Validation: It should be a valid record from CARD.STATUS table.Eg: 2 |
| 4 | `CAMB.COF.EXCLUDE.STATUS` | `CambCofParameter_ExcludeStatus` |  |  |  |
| 5 | `CAMB.COF.RESERVED.9` | `CambCofParameter_Reserved9` | TField |  |  |
| 6 | `CAMB.COF.RESERVED.8` | `CambCofParameter_Reserved8` | TField |  |  |
| 7 | `CAMB.COF.RESERVED.7` | `CambCofParameter_Reserved7` | TField |  |  |
| 8 | `CAMB.COF.RESERVED.6` | `CambCofParameter_Reserved6` | TField |  |  |
| 9 | `CAMB.COF.RESERVED.5` | `CambCofParameter_Reserved5` | TField |  |  |
| 10 | `CAMB.COF.RESERVED.4` | `CambCofParameter_Reserved4` | TField |  |  |
| 11 | `CAMB.COF.RESERVED.3` | `CambCofParameter_Reserved3` | TField |  |  |
| 12 | `CAMB.COF.RESERVED.2` | `CambCofParameter_Reserved2` | TField |  |  |
| 13 | `CAMB.COF.RESERVED.1` | `CambCofParameter_Reserved1` | TField |  |  |
| 14 | `CAMB.COF.RECORD.STATUS` | `CambCofParameter_RecordStatus` | String |  |  |
| 15 | `CAMB.COF.CURR.NO` | `CambCofParameter_CurrNo` | String |  |  |
| 16 | `CAMB.COF.INPUTTER` | `CambCofParameter_Inputter` |  |  |  |
| 17 | `CAMB.COF.DATE.TIME` | `CambCofParameter_DateTime` |  |  |  |
| 18 | `CAMB.COF.AUTHORISER` | `CambCofParameter_Authoriser` | String |  |  |
| 19 | `CAMB.COF.CO.CODE` | `CambCofParameter_CoCode` | String |  |  |
| 20 | `CAMB.COF.DEPT.CODE` | `CambCofParameter_DeptCode` | String |  |  |
| 21 | `CAMB.COF.AUDITOR.CODE` | `CambCofParameter_AuditorCode` | String |  |  |
| 22 | `CAMB.COF.AUDIT.DATE.TIME` | `CambCofParameter_AuditDateTime` | String |  |  |
