# FICOLL.LTV.CALCULATOR — Table Schema

> Source: `INSERTS/I_F.FICOLL.LTV.CALCULATOR` in `FICOLL_LTVProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FI.LTV.HC.LOAN` | `FicollLtvCalculator_HcLoan` | TField |  | Holds the loan amount of the Housing Company. |
| 2 | `FI.LTV.HC.SHARE` | `FicollLtvCalculator_HcShare` | TField |  | Holds the % share of the borrower in Housing company. |
| 3 | `FI.LTV.LOAN.AMOUNT` | `FicollLtvCalculator_LoanAmount` | TField |  | The loan amount to be granted. |
| 4 | `FI.LTV.YL.VALUE` | `FicollLtvCalculator_YlValue` | TField |  | Customer's share of the housing company's loan |
| 5 | `FI.LTV.PRIMARY.COLL` | `FicollLtvCalculator_PrimaryColl` | TField |  | Holds the Collateral Id of the Primary collateral to be considered. |
| 6 | `FI.LTV.MEL.VALUE` | `FicollLtvCalculator_MelValue` | TField |  | Other housing loans related to the primary housing collateral. |
| 7 | `FI.LTV.AP.VALUE` | `FicollLtvCalculator_ApValue` | TField |  | Loans other than housing loan related to primary housing collateral. |
| 8 | `FI.LTV.OIT.VALUE` | `FicollLtvCalculator_OitValue` | TField |  | Guarantia guarantee. |
| 9 | `FI.LTV.EAP.VALUE` | `FicollLtvCalculator_EapValue` | TField |  | Nominal Value of primary housing collateral. The nominal value has the housing company's loan already subtracted. So YL should not be subtracted again. |
| 10 | `FI.LTV.MOAJ.VALUE` | `FicollLtvCalculator_MoajValue` | TField |  | Other houses of the same customer. |
| 11 | `FI.LTV.OT.VALUE` | `FicollLtvCalculator_OtValue` | TField |  | Cash deposits of the same customer. |
| 12 | `FI.LTV.MR.VALUE` | `FicollLtvCalculator_MrValue` | TField |  | Real collaterals other than OT and houses of the same customer. |
| 13 | `FI.LTV.VVP.VALUE` | `FicollLtvCalculator_VvpValue` | TField |  | Collateral received from 3rd party. |
| 14 | `FI.LTV.TT.VALUE` | `FicollLtvCalculator_TtValue` | TField |  | (HAL guarantee - Nominal value of the primary collateral). Generally 0 during purchase. |
| 15 | `FI.LTV.LTV.NUMERATOR` | `FicollLtvCalculator_LtvNumerator` | TField |  | Holds the value of the numerator in LTV calculation formula given by FSA. |
| 16 | `FI.LTV.LTV.DENOMINATOR` | `FicollLtvCalculator_LtvDenominator` | TField |  | Holds the value of the denominator in LTV calculation formula given by FSA. |
| 17 | `FI.LTV.ALLOC.PERCENTAGE` | `FicollLtvCalculator_AllocPercentage` | TField |  | Used to store the percentage of allocation of linked limits. |
| 18 | `FI.LTV.LTV` | `FicollLtvCalculator_Ltv` | TField |  | Used to store the calculated LTV value. |
| 19 | `FI.LTV.RESERVED.10` | `FicollLtvCalculator_Reserved10` | TField |  |  |
| 20 | `FI.LTV.RESERVED.9` | `FicollLtvCalculator_Reserved9` | TField |  |  |
| 21 | `FI.LTV.RESERVED.8` | `FicollLtvCalculator_Reserved8` | TField |  |  |
| 22 | `FI.LTV.RESERVED.7` | `FicollLtvCalculator_Reserved7` | TField |  |  |
| 23 | `FI.LTV.RESERVED.6` | `FicollLtvCalculator_Reserved6` | TField |  |  |
| 24 | `FI.LTV.RESERVED.5` | `FicollLtvCalculator_Reserved5` | TField |  |  |
| 25 | `FI.LTV.RESERVED.4` | `FicollLtvCalculator_Reserved4` | TField |  |  |
| 26 | `FI.LTV.RESERVED.3` | `FicollLtvCalculator_Reserved3` | TField |  |  |
| 27 | `FI.LTV.RESERVED.2` | `FicollLtvCalculator_Reserved2` | TField |  |  |
| 28 | `FI.LTV.RESERVED.1` | `FicollLtvCalculator_Reserved1` | TField |  |  |
| 29 | `FI.LTV.LOCAL.REF` | `FicollLtvCalculator_LocalRef` |  |  |  |
| 30 | `FI.LTV.OVERRIDE` | `FicollLtvCalculator_Override` |  |  |  |
| 31 | `FI.LTV.RECORD.STATUS` | `FicollLtvCalculator_RecordStatus` | String |  |  |
| 32 | `FI.LTV.CURR.NO` | `FicollLtvCalculator_CurrNo` | String |  |  |
| 33 | `FI.LTV.INPUTTER` | `FicollLtvCalculator_Inputter` |  |  |  |
| 34 | `FI.LTV.DATE.TIME` | `FicollLtvCalculator_DateTime` |  |  |  |
| 35 | `FI.LTV.AUTHORISER` | `FicollLtvCalculator_Authoriser` | String |  |  |
| 36 | `FI.LTV.CO.CODE` | `FicollLtvCalculator_CoCode` | String |  |  |
| 37 | `FI.LTV.DEPT.CODE` | `FicollLtvCalculator_DeptCode` | String |  |  |
| 38 | `FI.LTV.AUDITOR.CODE` | `FicollLtvCalculator_AuditorCode` | String |  |  |
| 39 | `FI.LTV.AUDIT.DATE.TIME` | `FicollLtvCalculator_AuditDateTime` | String |  |  |
