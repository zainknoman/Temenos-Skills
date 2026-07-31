# SAACIN.PARAMETER — Table Schema

> Source: `INSERTS/I_F.SAACIN.PARAMETER` in `SABASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SAACIN.PARAM.REDORMANT.DAYS` | `SaacinParameter_RedormantDays` | TField |  | Number of days within which the Customer has to initiate any transaction failing which, the account is declared as Dormant. |
| 2 | `SAACIN.PARAM.ACCOUNT.STATUS` | `SaacinParameter_AccountStatus` |  |  |  |
| 3 | `SAACIN.PARAM.POSTING.RESTRICT` | `SaacinParameter_PostingRestrict` |  |  |  |
| 4 | `SAACIN.PARAM.HIGH.RISK.CUSTOMER.STATUS` | `SaacinParameter_HighRiskCustomerStatus` | TField |  | Specifies the status of the Expatriate or High Risk customer. |
| 5 | `SAACIN.PARAM.RESERVED.2` | `SaacinParameter_Reserved2` | TField |  | reserved for future use. |
| 6 | `SAACIN.PARAM.RESERVED.3` | `SaacinParameter_Reserved3` | TField |  | reserved for future use. |
| 7 | `SAACIN.PARAM.RESERVED.4` | `SaacinParameter_Reserved4` | TField |  | reserved for future use. |
| 8 | `SAACIN.PARAM.RESERVED.5` | `SaacinParameter_Reserved5` | TField |  | reserved for future use. |
| 9 | `SAACIN.PARAM.RESERVED.6` | `SaacinParameter_Reserved6` | TField |  | reserved for future use. |
| 10 | `SAACIN.PARAM.RESERVED.7` | `SaacinParameter_Reserved7` | TField |  | reserved for future use. |
| 11 | `SAACIN.PARAM.RESERVED.8` | `SaacinParameter_Reserved8` | TField |  | reserved for future use. |
| 12 | `SAACIN.PARAM.RESERVED.9` | `SaacinParameter_Reserved9` | TField |  | reserved for future use. |
| 13 | `SAACIN.PARAM.RESERVED.10` | `SaacinParameter_Reserved10` | TField |  | reserved for future use. |
| 14 | `SAACIN.PARAM.LOCAL.REF` | `SaacinParameter_LocalRef` |  |  |  |
| 15 | `SAACIN.PARAM.OVERRIDE` | `SaacinParameter_Override` |  |  |  |
| 16 | `SAACIN.PARAM.RECORD.STATUS` | `SaacinParameter_RecordStatus` | String |  | Indicates the record status |
| 17 | `SAACIN.PARAM.CURR.NO` | `SaacinParameter_CurrNo` | String |  | Indicates the number of time record is modified and saved |
| 18 | `SAACIN.PARAM.INPUTTER` | `SaacinParameter_Inputter` |  |  |  |
| 19 | `SAACIN.PARAM.DATE.TIME` | `SaacinParameter_DateTime` |  |  |  |
| 20 | `SAACIN.PARAM.AUTHORISER` | `SaacinParameter_Authoriser` | String |  |  |
| 21 | `SAACIN.PARAM.CO.CODE` | `SaacinParameter_CoCode` | String |  |  |
| 22 | `SAACIN.PARAM.DEPT.CODE` | `SaacinParameter_DeptCode` | String |  |  |
| 23 | `SAACIN.PARAM.AUDITOR.CODE` | `SaacinParameter_AuditorCode` | String |  |  |
| 24 | `SAACIN.PARAM.AUDIT.DATE.TIME` | `SaacinParameter_AuditDateTime` | String |  |  |
| 25 | `SAACIN.PARAM.BRANCH.MAX.LIMIT` | `SaacinParameter_BranchMaxLimit` | TField |  | This field will be used to update the upper limit or the maximum limit of Cash that the Branch can hold in a day. The limit will be updated in LCY which is inclusive of FCY limits of the Branch |
| 26 | `SAACIN.PARAM.BRANCH.MIN.LIMIT` | `SaacinParameter_BranchMinLimit` | TField |  | This field will be used to update the minimum limit of Cash that the Branch can have every day during COB. The limit will be updated in LCY which is inclusive of FCY limits of the Branch |
| 27 | `SAACIN.PARAM.VAULT.MAX.LIMIT` | `SaacinParameter_VaultMaxLimit` | TField |  | This field will be used to update the upper limit or the maximum limit of Cash that the Vault can hold at any point of time. The limit will be updated in LCY which is inclusive of FCY limits of the Vault |
| 28 | `SAACIN.PARAM.VAULT.MIN.LIMIT` | `SaacinParameter_VaultMinLimit` | TField |  | This field will be used to update the minimum limit of Cash that the Vault should have every day during COB The limit will be updated in LCY which is inclusive of FCY limits of the Vault |
| 29 | `SAACIN.PARAM.VAULT.CATEG` | `SaacinParameter_VaultCateg` |  |  |  |
| 30 | `SAACIN.PARAM.ATM.CATEG` | `SaacinParameter_AtmCateg` |  |  |  |
| 31 | `SAACIN.PARAM.CASH.CATEG` | `SaacinParameter_CashCateg` |  |  |  |
