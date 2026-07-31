# CUSTOMER.SSI — Table Schema

> Source: `INSERTS/I_F.CUSTOMER.SSI` in `ST_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CUS.SSI.CURRENCY` | `CustomerSsi_Currency` |  |  |  |
| 2 | `CUS.SSI.SYS.CODE` | `CustomerSsi_SysCode` |  |  |  |
| 3 | `CUS.SSI.ACCOUNT` | `CustomerSsi_Account` |  |  |  |
| 4 | `CUS.SSI.COMPANY.ID` | `CustomerSsi_CompanyId` |  |  |  |
| 5 | `CUS.SSI.RESERVED.09` | `CustomerSsi_Reserved09` | TField |  |  |
| 6 | `CUS.SSI.RESERVED.08` | `CustomerSsi_Reserved08` | TField |  |  |
| 7 | `CUS.SSI.RESERVED.07` | `CustomerSsi_Reserved07` | TField |  |  |
| 8 | `CUS.SSI.RESERVED.06` | `CustomerSsi_Reserved06` | TField |  |  |
| 9 | `CUS.SSI.RESERVED.05` | `CustomerSsi_Reserved05` | TField |  |  |
| 10 | `CUS.SSI.RESERVED.04` | `CustomerSsi_Reserved04` | TField |  |  |
| 11 | `CUS.SSI.RESERVED.03` | `CustomerSsi_Reserved03` | TField |  |  |
| 12 | `CUS.SSI.RESERVED.02` | `CustomerSsi_Reserved02` | TField |  |  |
| 13 | `CUS.SSI.RESERVED.01` | `CustomerSsi_Reserved01` | TField |  |  |
| 14 | `CUS.SSI.LOCAL.REF` | `CustomerSsi_LocalRef` |  |  |  |
| 15 | `CUS.SSI.OVERRIDE` | `CustomerSsi_Override` |  |  |  |
| 16 | `CUS.SSI.RECORD.STATUS` | `CustomerSsi_RecordStatus` | String |  |  |
| 17 | `CUS.SSI.CURR.NO` | `CustomerSsi_CurrNo` | String |  |  |
| 18 | `CUS.SSI.INPUTTER` | `CustomerSsi_Inputter` |  |  |  |
| 19 | `CUS.SSI.DATE.TIME` | `CustomerSsi_DateTime` |  |  |  |
| 20 | `CUS.SSI.AUTHORISER` | `CustomerSsi_Authoriser` | String |  |  |
| 21 | `CUS.SSI.CO.CODE` | `CustomerSsi_CoCode` | String |  |  |
| 22 | `CUS.SSI.DEPT.CODE` | `CustomerSsi_DeptCode` | String |  |  |
| 23 | `CUS.SSI.AUDITOR.CODE` | `CustomerSsi_AuditorCode` | String |  |  |
| 24 | `CUS.SSI.AUDIT.DATE.TIME` | `CustomerSsi_AuditDateTime` | String |  |  |
