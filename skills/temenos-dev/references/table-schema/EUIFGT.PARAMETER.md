# EUIFGT.PARAMETER — Table Schema

> Source: `INSERTS/I_F.EUIFGT.PARAMETER` in `EUIFGT_InvestmentFundGuarantee.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EUIFGTPARAM.EIF.CUSTOMER.CODE` | `EuifgtParameter_EifCustomerCode` | TField |  | Customer id of EIF Guarantee |
| 2 | `EUIFGTPARAM.EIF.COLLATERAL.TYPE` | `EuifgtParameter_EifCollateralType` | TField |  | Collateral Type of EIF Guarantee. |
| 3 | `EUIFGTPARAM.COLLATERAL.MAX.VALUE` | `EuifgtParameter_CollateralMaxValue` | TField |  | Maximum allowed Execution Value of EIF Guarantee type Collateral. |
| 4 | `EUIFGTPARAM.LOAN.MAX.VALUE` | `EuifgtParameter_LoanMaxValue` | TField |  | Maximum loan value that can be backed up by EIF Guarantee. |
| 5 | `EUIFGTPARAM.EIF.COMMISSION.DESCRIPTION` | `EuifgtParameter_EifCommissionDescription` |  |  |  |
| 6 | `EUIFGTPARAM.RESERVED.9` | `EuifgtParameter_Reserved9` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 7 | `EUIFGTPARAM.RESERVED.8` | `EuifgtParameter_Reserved8` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 8 | `EUIFGTPARAM.RESERVED.7` | `EuifgtParameter_Reserved7` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 9 | `EUIFGTPARAM.RESERVED.6` | `EuifgtParameter_Reserved6` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 10 | `EUIFGTPARAM.RESERVED.5` | `EuifgtParameter_Reserved5` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 11 | `EUIFGTPARAM.RESERVED.4` | `EuifgtParameter_Reserved4` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 12 | `EUIFGTPARAM.RESERVED.3` | `EuifgtParameter_Reserved3` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 13 | `EUIFGTPARAM.RESERVED.2` | `EuifgtParameter_Reserved2` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 14 | `EUIFGTPARAM.RESERVED.1` | `EuifgtParameter_Reserved1` | TField |  | Reserved for future use. Validation Rules: System field, no input. |
| 15 | `EUIFGTPARAM.LOCAL.REF` | `EuifgtParameter_LocalRef` |  |  |  |
| 16 | `EUIFGTPARAM.OVERRIDE` | `EuifgtParameter_Override` |  |  |  |
| 17 | `EUIFGTPARAM.RECORD.STATUS` | `EuifgtParameter_RecordStatus` | String |  |  |
| 18 | `EUIFGTPARAM.CURR.NO` | `EuifgtParameter_CurrNo` | String |  |  |
| 19 | `EUIFGTPARAM.INPUTTER` | `EuifgtParameter_Inputter` |  |  |  |
| 20 | `EUIFGTPARAM.DATE.TIME` | `EuifgtParameter_DateTime` |  |  |  |
| 21 | `EUIFGTPARAM.AUTHORISER` | `EuifgtParameter_Authoriser` | String |  |  |
| 22 | `EUIFGTPARAM.CO.CODE` | `EuifgtParameter_CoCode` | String |  |  |
| 23 | `EUIFGTPARAM.DEPT.CODE` | `EuifgtParameter_DeptCode` | String |  |  |
| 24 | `EUIFGTPARAM.AUDITOR.CODE` | `EuifgtParameter_AuditorCode` | String |  |  |
| 25 | `EUIFGTPARAM.AUDIT.DATE.TIME` | `EuifgtParameter_AuditDateTime` | String |  |  |
