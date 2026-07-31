# ID.PDS.CATEGORY — Table Schema

> Source: `INSERTS/I_F.ID.PDS.CATEGORY` in `ID_PdsConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.CAT.DESCRIPTION` | `IdPdsCategory_Description` |  |  |  |
| 2 | `ID.CAT.CALC.BALANCE.TYPE` | `IdPdsCategory_CalcBalanceType` | TField |  | PDS calculation/ distribution for Deposits/ Accounts uses different balance types set in this field. Based upon the balance type set in this field the Participation balance for Deposits/ Accounts is calculated. Allowed values are "Daily", "Average", and "Minimum". 1). Average Balance is calculated by dividing "Sum of Daily end of the day balance between Simulation start date and Simulation end date" AND "Total number of days between Simulation start date and Simulation end date". 2). Daily Balance is to consider the End of the day balance on each date between Simulation start date and Simulation end date. 3). Minimum Balance is arrived by computing the minimum balance between Simulation start date and Simulation end date. 4). If Calc.balance.type is set as NONE then the balance of the Account/ Deposit is considered as Zero |
| 3 | `ID.CAT.DIST.BALANCE.TYPE` | `IdPdsCategory_DistBalanceType` | TField |  | This field is for future use. |
| 4 | `ID.CAT.CURRENCY` | `IdPdsCategory_Currency` |  |  |  |
| 5 | `ID.CAT.MIN.BALANCE` | `IdPdsCategory_MinBalance` |  |  |  |
| 6 | `ID.CAT.MIN.DEP.PERIOD` | `IdPdsCategory_MinDepPeriod` | TField |  | The minimum deposit period can be setup for Mudaraba deposits. During PDS simulation calculation if the deposit is pre-closed within the minimum deposit period configured in this field then deposit balance is excluded in Pool calculation by adding the deposit balance into the excluded balances. If minimum deposit period is left blank then the minimum period for the Deposit product is not evaluated. Allowed values are from 0D � 999D Example: If the expectation is to evaluate the minimum deposit period as 30D then it is required to configure the parameter setup as 29D. |
| 7 | `ID.CAT.RESERVED.10` | `IdPdsCategory_Reserved10` | TField |  |  |
| 8 | `ID.CAT.RESERVED.9` | `IdPdsCategory_Reserved9` | TField |  |  |
| 9 | `ID.CAT.RESERVED.8` | `IdPdsCategory_Reserved8` | TField |  |  |
| 10 | `ID.CAT.RESERVED.7` | `IdPdsCategory_Reserved7` | TField |  |  |
| 11 | `ID.CAT.RESERVED.6` | `IdPdsCategory_Reserved6` | TField |  |  |
| 12 | `ID.CAT.RESERVED.5` | `IdPdsCategory_Reserved5` | TField |  |  |
| 13 | `ID.CAT.RESERVED.4` | `IdPdsCategory_Reserved4` | TField |  |  |
| 14 | `ID.CAT.RESERVED.3` | `IdPdsCategory_Reserved3` | TField |  |  |
| 15 | `ID.CAT.RESERVED.2` | `IdPdsCategory_Reserved2` | TField |  |  |
| 16 | `ID.CAT.RESERVED.1` | `IdPdsCategory_Reserved1` | TField |  |  |
| 17 | `ID.CAT.LOCAL.REF` | `IdPdsCategory_LocalRef` |  |  |  |
| 18 | `ID.CAT.OVERRIDE` | `IdPdsCategory_Override` |  |  |  |
| 19 | `ID.CAT.RECORD.STATUS` | `IdPdsCategory_RecordStatus` | String |  |  |
| 20 | `ID.CAT.CURR.NO` | `IdPdsCategory_CurrNo` | String |  |  |
| 21 | `ID.CAT.INPUTTER` | `IdPdsCategory_Inputter` |  |  |  |
| 22 | `ID.CAT.DATE.TIME` | `IdPdsCategory_DateTime` |  |  |  |
| 23 | `ID.CAT.AUTHORISER` | `IdPdsCategory_Authoriser` | String |  |  |
| 24 | `ID.CAT.CO.CODE` | `IdPdsCategory_CoCode` | String |  |  |
| 25 | `ID.CAT.DEPT.CODE` | `IdPdsCategory_DeptCode` | String |  |  |
| 26 | `ID.CAT.AUDITOR.CODE` | `IdPdsCategory_AuditorCode` | String |  |  |
| 27 | `ID.CAT.AUDIT.DATE.TIME` | `IdPdsCategory_AuditDateTime` | String |  |  |
