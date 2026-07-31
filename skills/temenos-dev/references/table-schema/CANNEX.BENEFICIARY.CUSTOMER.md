# CANNEX.BENEFICIARY.CUSTOMER — Table Schema

> Source: `INSERTS/I_F.CANNEX.BENEFICIARY.CUSTOMER` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CNX.BEN.CUS.BENEFICIARY.ID` | `CannexBeneficiaryCustomer_BeneficiaryId` | TField |  |  |
| 2 | `CNX.BEN.CUS.RESERVED.1` | `CannexBeneficiaryCustomer_Reserved1` | TField |  |  |
| 3 | `CNX.BEN.CUS.RESERVED.2` | `CannexBeneficiaryCustomer_Reserved2` | TField |  |  |
| 4 | `CNX.BEN.CUS.RESERVED.3` | `CannexBeneficiaryCustomer_Reserved3` | TField |  |  |
| 5 | `CNX.BEN.CUS.RESERVED.4` | `CannexBeneficiaryCustomer_Reserved4` | TField |  |  |
| 6 | `CNX.BEN.CUS.RESERVED.5` | `CannexBeneficiaryCustomer_Reserved5` | TField |  |  |
| 7 | `CNX.BEN.CUS.LOCAL.REF` | `CannexBeneficiaryCustomer_LocalRef` |  |  |  |
| 8 | `CNX.BEN.CUS.OVERRIDE` | `CannexBeneficiaryCustomer_Override` |  |  |  |
| 9 | `CNX.BEN.CUS.RECORD.STATUS` | `CannexBeneficiaryCustomer_RecordStatus` | String |  |  |
| 10 | `CNX.BEN.CUS.CURR.NO` | `CannexBeneficiaryCustomer_CurrNo` | String |  |  |
| 11 | `CNX.BEN.CUS.INPUTTER` | `CannexBeneficiaryCustomer_Inputter` |  |  |  |
| 12 | `CNX.BEN.CUS.DATE.TIME` | `CannexBeneficiaryCustomer_DateTime` |  |  |  |
| 13 | `CNX.BEN.CUS.AUTHORISER` | `CannexBeneficiaryCustomer_Authoriser` | String |  |  |
| 14 | `CNX.BEN.CUS.CO.CODE` | `CannexBeneficiaryCustomer_CoCode` | String |  |  |
| 15 | `CNX.BEN.CUS.DEPT.CODE` | `CannexBeneficiaryCustomer_DeptCode` | String |  |  |
| 16 | `CNX.BEN.CUS.AUDITOR.CODE` | `CannexBeneficiaryCustomer_AuditorCode` | String |  |  |
| 17 | `CNX.BEN.CUS.AUDIT.DATE.TIME` | `CannexBeneficiaryCustomer_AuditDateTime` | String |  |  |
