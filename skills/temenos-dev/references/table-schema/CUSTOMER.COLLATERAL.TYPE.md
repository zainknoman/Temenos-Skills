# CUSTOMER.COLLATERAL.TYPE — Table Schema

> Source: `INSERTS/I_F.CUSTOMER.COLLATERAL.TYPE` in `CO_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CU.CO.DESCRIPTION` | `CustomerCollateralType_Description` |  |  |  |
| 2 | `CU.CO.EXECUTION.VALUE` | `CustomerCollateralType_ExecutionValue` | TField | Yes | Execution value as a percentage of Nominal Value but different from that in the main Collateral Type record. Example. COLLATERAL.TYPE-100-cash collaterals-EXECUTION.VALUE-100%N CUSTOMER.COLLATERAL.TYPE-100053-100-EXECUTION.VALUE-75%N. In the above case Execution Value for the collaterals under Collateral Type 100 for the customer 100053 will be calculated at 75%N only. Validation Rules: Mandatory input; Allowed as %N only, in the range 0-100. (E.g.50%N, 60%N Etc.) Duplication of the percentage in the main record not allowed. |
| 3 | `CU.CO.RESERVED13` | `CustomerCollateralType_Reserved13` | TField |  |  |
| 4 | `CU.CO.RESERVED12` | `CustomerCollateralType_Reserved12` | TField |  |  |
| 5 | `CU.CO.RESERVED11` | `CustomerCollateralType_Reserved11` | TField |  |  |
| 6 | `CU.CO.RESERVED10` | `CustomerCollateralType_Reserved10` | TField |  |  |
| 7 | `CU.CO.RESERVED9` | `CustomerCollateralType_Reserved9` | TField |  |  |
| 8 | `CU.CO.RESERVED8` | `CustomerCollateralType_Reserved8` | TField |  |  |
| 9 | `CU.CO.RESERVED7` | `CustomerCollateralType_Reserved7` | TField |  |  |
| 10 | `CU.CO.RESERVED6` | `CustomerCollateralType_Reserved6` | TField |  |  |
| 11 | `CU.CO.RESERVED5` | `CustomerCollateralType_Reserved5` | TField |  |  |
| 12 | `CU.CO.RESERVED4` | `CustomerCollateralType_Reserved4` | TField |  |  |
| 13 | `CU.CO.RESERVED3` | `CustomerCollateralType_Reserved3` | TField |  |  |
| 14 | `CU.CO.LOCAL.REF` | `CustomerCollateralType_LocalRef` |  |  |  |
| 15 | `CU.CO.OVERRIDE` | `CustomerCollateralType_Override` |  |  |  |
| 16 | `CU.CO.RECORD.STATUS` | `CustomerCollateralType_RecordStatus` | String |  |  |
| 17 | `CU.CO.CURR.NO` | `CustomerCollateralType_CurrNo` | String |  |  |
| 18 | `CU.CO.INPUTTER` | `CustomerCollateralType_Inputter` |  |  |  |
| 19 | `CU.CO.DATE.TIME` | `CustomerCollateralType_DateTime` |  |  |  |
| 20 | `CU.CO.AUTHORISER` | `CustomerCollateralType_Authoriser` | String |  |  |
| 21 | `CU.CO.CO.CODE` | `CustomerCollateralType_CoCode` | String |  |  |
| 22 | `CU.CO.DEPT.CODE` | `CustomerCollateralType_DeptCode` | String |  |  |
| 23 | `CU.CO.AUDITOR.CODE` | `CustomerCollateralType_AuditorCode` | String |  |  |
| 24 | `CU.CO.AUDIT.DATE.TIME` | `CustomerCollateralType_AuditDateTime` | String |  |  |
