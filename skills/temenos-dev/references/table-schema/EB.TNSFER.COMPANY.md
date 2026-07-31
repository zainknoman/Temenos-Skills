# EB.TNSFER.COMPANY — Table Schema

> Source: `INSERTS/I_F.EB.TNSFER.COMPANY` in `MC_CompanyCreation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.TRAS.COM.COMPANY.TO` | `EbTnsferCompany_CompanyTo` | TField |  | The company to which accounts and contracts are to be transferred. |
| 2 | `EB.TRAS.COM.EFFECTIVE.DATE` | `EbTnsferCompany_EffectiveDate` | TField |  | The effective date of the transfer. |
| 3 | `EB.TRAS.COM.ACCOUNTING.CO.TO` | `EbTnsferCompany_AccountingCoTo` | TField |  | Must be a valid Accounting company to which Accounts and Contracts to be moved. |
| 4 | `EB.TRAS.COM.RESERVED.4` | `EbTnsferCompany_Reserved4` | TField |  |  |
| 5 | `EB.TRAS.COM.RESERVED.3` | `EbTnsferCompany_Reserved3` | TField |  |  |
| 6 | `EB.TRAS.COM.RESERVED.2` | `EbTnsferCompany_Reserved2` | TField |  |  |
| 7 | `EB.TRAS.COM.LOCAL.REF` | `EbTnsferCompany_LocalRef` |  |  |  |
| 8 | `EB.TRAS.COM.OVERRIDE` | `EbTnsferCompany_Override` |  |  |  |
| 9 | `EB.TRAS.COM.RECORD.STATUS` | `EbTnsferCompany_RecordStatus` | String |  |  |
| 10 | `EB.TRAS.COM.CURR.NO` | `EbTnsferCompany_CurrNo` | String |  |  |
| 11 | `EB.TRAS.COM.INPUTTER` | `EbTnsferCompany_Inputter` |  |  |  |
| 12 | `EB.TRAS.COM.DATE.TIME` | `EbTnsferCompany_DateTime` |  |  |  |
| 13 | `EB.TRAS.COM.AUTHORISER` | `EbTnsferCompany_Authoriser` | String |  |  |
| 14 | `EB.TRAS.COM.CO.CODE` | `EbTnsferCompany_CoCode` | String |  |  |
| 15 | `EB.TRAS.COM.DEPT.CODE` | `EbTnsferCompany_DeptCode` | String |  |  |
| 16 | `EB.TRAS.COM.AUDITOR.CODE` | `EbTnsferCompany_AuditorCode` | String |  |  |
| 17 | `EB.TRAS.COM.AUDIT.DATE.TIME` | `EbTnsferCompany_AuditDateTime` | String |  |  |
