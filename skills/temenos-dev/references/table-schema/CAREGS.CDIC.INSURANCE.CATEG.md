# CAREGS.CDIC.INSURANCE.CATEG — Table Schema

> Source: `INSERTS/I_F.CAREGS.CDIC.INSURANCE.CATEG` in `CADEPO_CDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CDIC.INS.CATEG.DESCRIPTION` | `CaregsCdicInsuranceCateg_Description` | TField |  | Field to update the description of the record. |
| 2 | `CDIC.INS.CATEG.INSUR.CATEG.CODE` | `CaregsCdicInsuranceCateg_InsurCategCode` | TField |  |  |
| 3 | `CDIC.INS.CATEG.INSUR.RULE.DEFIN` | `CaregsCdicInsuranceCateg_InsurRuleDefin` |  |  |  |
| 4 | `CDIC.INS.CATEG.TRUST.TYPE` | `CaregsCdicInsuranceCateg_TrustType` |  |  |  |
| 5 | `CDIC.INS.CATEG.TRUST.DESCRIPTION` | `CaregsCdicInsuranceCateg_TrustDescription` |  |  |  |
| 6 | `CDIC.INS.CATEG.TRUST.RULE.DEFIN` | `CaregsCdicInsuranceCateg_TrustRuleDefin` |  |  |  |
| 7 | `CDIC.INS.CATEG.FED.INS.CATEG.CODE` | `CaregsCdicInsuranceCateg_FedInsCategCode` | TField |  | Purpose of the field to define the federal insurance category code that to be reported in table 160Only numeric values allowed. |
| 8 | `CDIC.INS.CATEG.RESERVED.2` | `CaregsCdicInsuranceCateg_Reserved2` | TField |  |  |
| 9 | `CDIC.INS.CATEG.RESERVED.3` | `CaregsCdicInsuranceCateg_Reserved3` | TField |  |  |
| 10 | `CDIC.INS.CATEG.RESERVED.4` | `CaregsCdicInsuranceCateg_Reserved4` | TField |  |  |
| 11 | `CDIC.INS.CATEG.RESERVED.5` | `CaregsCdicInsuranceCateg_Reserved5` | TField |  |  |
| 12 | `CDIC.INS.CATEG.LOCAL.REF` | `CaregsCdicInsuranceCateg_LocalRef` |  |  |  |
| 13 | `CDIC.INS.CATEG.RECORD.STATUS` | `CaregsCdicInsuranceCateg_RecordStatus` | String |  |  |
| 14 | `CDIC.INS.CATEG.CURR.NO` | `CaregsCdicInsuranceCateg_CurrNo` | String |  |  |
| 15 | `CDIC.INS.CATEG.INPUTTER` | `CaregsCdicInsuranceCateg_Inputter` |  |  |  |
| 16 | `CDIC.INS.CATEG.DATE.TIME` | `CaregsCdicInsuranceCateg_DateTime` |  |  |  |
| 17 | `CDIC.INS.CATEG.AUTHORISER` | `CaregsCdicInsuranceCateg_Authoriser` | String |  |  |
| 18 | `CDIC.INS.CATEG.CO.CODE` | `CaregsCdicInsuranceCateg_CoCode` | String |  |  |
| 19 | `CDIC.INS.CATEG.DEPT.CODE` | `CaregsCdicInsuranceCateg_DeptCode` | String |  |  |
| 20 | `CDIC.INS.CATEG.AUDITOR.CODE` | `CaregsCdicInsuranceCateg_AuditorCode` | String |  |  |
| 21 | `CDIC.INS.CATEG.AUDIT.DATE.TIME` | `CaregsCdicInsuranceCateg_AuditDateTime` | String |  |  |
