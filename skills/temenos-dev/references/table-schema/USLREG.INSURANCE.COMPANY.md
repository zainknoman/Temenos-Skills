# USLREG.INSURANCE.COMPANY — Table Schema

> Source: `INSERTS/I_F.USLREG.INSURANCE.COMPANY` in `USLREG_RebatableInsurance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INS.COMP.DESCRIPTION` | `UslregInsuranceCompany_Description` | TField |  | Used to define the full name of the insurance company. |
| 2 | `INS.COMP.TYPE` | `UslregInsuranceCompany_Type` |  |  |  |
| 3 | `INS.COMP.RESERVED.11` | `UslregInsuranceCompany_Reserved11` |  |  |  |
| 4 | `INS.COMP.RESERVED.10` | `UslregInsuranceCompany_Reserved10` |  |  |  |
| 5 | `INS.COMP.EFFECTIVE.DATE` | `UslregInsuranceCompany_EffectiveDate` |  |  |  |
| 6 | `INS.COMP.EXPIRY.DATE` | `UslregInsuranceCompany_ExpiryDate` |  |  |  |
| 7 | `INS.COMP.INACTIVE.DATE` | `UslregInsuranceCompany_InactiveDate` | TField |  |  |
| 8 | `INS.COMP.RESERVED.9` | `UslregInsuranceCompany_Reserved9` | TField |  |  |
| 9 | `INS.COMP.RESERVED.8` | `UslregInsuranceCompany_Reserved8` | TField |  |  |
| 10 | `INS.COMP.RESERVED.7` | `UslregInsuranceCompany_Reserved7` | TField |  |  |
| 11 | `INS.COMP.RESERVED.6` | `UslregInsuranceCompany_Reserved6` | TField |  |  |
| 12 | `INS.COMP.RESERVED.5` | `UslregInsuranceCompany_Reserved5` | TField |  |  |
| 13 | `INS.COMP.RESERVED.4` | `UslregInsuranceCompany_Reserved4` | TField |  |  |
| 14 | `INS.COMP.RESERVED.3` | `UslregInsuranceCompany_Reserved3` | TField |  |  |
| 15 | `INS.COMP.RESERVED.2` | `UslregInsuranceCompany_Reserved2` | TField |  |  |
| 16 | `INS.COMP.RESERVED.1` | `UslregInsuranceCompany_Reserved1` | TField |  |  |
| 17 | `INS.COMP.RECORD.STATUS` | `UslregInsuranceCompany_RecordStatus` | String |  |  |
| 18 | `INS.COMP.CURR.NO` | `UslregInsuranceCompany_CurrNo` | String |  |  |
| 19 | `INS.COMP.INPUTTER` | `UslregInsuranceCompany_Inputter` |  |  |  |
| 20 | `INS.COMP.DATE.TIME` | `UslregInsuranceCompany_DateTime` |  |  |  |
| 21 | `INS.COMP.AUTHORISER` | `UslregInsuranceCompany_Authoriser` | String |  |  |
| 22 | `INS.COMP.CO.CODE` | `UslregInsuranceCompany_CoCode` | String |  |  |
| 23 | `INS.COMP.DEPT.CODE` | `UslregInsuranceCompany_DeptCode` | String |  |  |
| 24 | `INS.COMP.AUDITOR.CODE` | `UslregInsuranceCompany_AuditorCode` | String |  |  |
| 25 | `INS.COMP.AUDIT.DATE.TIME` | `UslregInsuranceCompany_AuditDateTime` | String |  |  |
