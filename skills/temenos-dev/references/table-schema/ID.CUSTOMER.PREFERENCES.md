# ID.CUSTOMER.PREFERENCES — Table Schema

> Source: `INSERTS/I_F.ID.CUSTOMER.PREFERENCES` in `ID_PdsConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.CUS.WEIGHTAGE` | `IdCustomerPreferences_Weightage` | TField |  | The weightage to be defined that should be considered for the Customer during Distribution of Profit for Accounts and Deposits. The priority of this weightage is after the weightage defined for the Customer Account in multi-value fields CUSTOMER.ACCT-ACCT.WEIGHTAGE Validation Rules: 1. A valid percentage within the range 0-999.999999 with 6 decimals. |
| 2 | `ID.CUS.CUSTOMER.ACCT` | `IdCustomerPreferences_CustomerAcct` |  |  |  |
| 3 | `ID.CUS.ACCT.WEIGHTAGE` | `IdCustomerPreferences_AcctWeightage` |  |  |  |
| 4 | `ID.CUS.RESERVED.10` | `IdCustomerPreferences_Reserved10` |  |  |  |
| 5 | `ID.CUS.RESERVED.9` | `IdCustomerPreferences_Reserved9` |  |  |  |
| 6 | `ID.CUS.RESERVED.8` | `IdCustomerPreferences_Reserved8` | TField |  |  |
| 7 | `ID.CUS.RESERVED.7` | `IdCustomerPreferences_Reserved7` | TField |  |  |
| 8 | `ID.CUS.RESERVED.6` | `IdCustomerPreferences_Reserved6` | TField |  |  |
| 9 | `ID.CUS.RESERVED.5` | `IdCustomerPreferences_Reserved5` | TField |  |  |
| 10 | `ID.CUS.RESERVED.4` | `IdCustomerPreferences_Reserved4` | TField |  |  |
| 11 | `ID.CUS.RESERVED.3` | `IdCustomerPreferences_Reserved3` | TField |  |  |
| 12 | `ID.CUS.RESERVED.2` | `IdCustomerPreferences_Reserved2` | TField |  |  |
| 13 | `ID.CUS.RESERVED.1` | `IdCustomerPreferences_Reserved1` | TField |  |  |
| 14 | `ID.CUS.LOCAL.REF` | `IdCustomerPreferences_LocalRef` |  |  |  |
| 15 | `ID.CUS.OVERRIDE` | `IdCustomerPreferences_Override` |  |  |  |
| 16 | `ID.CUS.RECORD.STATUS` | `IdCustomerPreferences_RecordStatus` | String |  |  |
| 17 | `ID.CUS.CURR.NO` | `IdCustomerPreferences_CurrNo` | String |  |  |
| 18 | `ID.CUS.INPUTTER` | `IdCustomerPreferences_Inputter` |  |  |  |
| 19 | `ID.CUS.DATE.TIME` | `IdCustomerPreferences_DateTime` |  |  |  |
| 20 | `ID.CUS.AUTHORISER` | `IdCustomerPreferences_Authoriser` | String |  |  |
| 21 | `ID.CUS.CO.CODE` | `IdCustomerPreferences_CoCode` | String |  |  |
| 22 | `ID.CUS.DEPT.CODE` | `IdCustomerPreferences_DeptCode` | String |  |  |
| 23 | `ID.CUS.AUDITOR.CODE` | `IdCustomerPreferences_AuditorCode` | String |  |  |
| 24 | `ID.CUS.AUDIT.DATE.TIME` | `IdCustomerPreferences_AuditDateTime` | String |  |  |
