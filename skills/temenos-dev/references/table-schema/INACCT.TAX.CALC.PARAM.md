# INACCT.TAX.CALC.PARAM — Table Schema

> Source: `INSERTS/I_F.INACCT.TAX.CALC.PARAM` in `INACCT_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INACCT.TAXPARAM.TAX.DED.SUSP.ACC` | `InacctTaxCalcParam_TaxDedSuspAcc` | TField |  | Contains the suspense account from where the tax has to be deducted. |
| 2 | `INACCT.TAXPARAM.AC.ENTRY.PARAM` | `InacctTaxCalcParam_AcEntryParam` | TField |  | The ID from the AC.ENTRY.PARAM application |
| 3 | `INACCT.TAXPARAM.PRODUCT` | `InacctTaxCalcParam_Product` |  |  |  |
| 4 | `INACCT.TAXPARAM.INFO.INT.PROPERTY` | `InacctTaxCalcParam_InfoIntProperty` | TField | Yes | This field contains the info interest property used in the product. Either Product or Info Interest Property is Mandatory. |
| 5 | `INACCT.TAXPARAM.TDS.TAX.TYPE.CONDITION` | `InacctTaxCalcParam_TdsTaxTypeCondition` | TField |  | Contains the tax Type Condition. Valid record from TAX.TYPE.CONDITION. |
| 6 | `INACCT.TAXPARAM.MINIMUM.INTEREST.PAYOUT` | `InacctTaxCalcParam_MinimumInterestPayout` | TField |  | Minimum Interest Paid out to the Customer, when 100% of Interest is passed as a Tax Amount. |
| 7 | `INACCT.TAXPARAM.PREV.TAX.END.DATE` | `InacctTaxCalcParam_PrevTaxEndDate` | TField |  | Holds the Previous Financial Tax year end date, should be updated before updating Current Tax End in TAX.PARAMETER application. |
| 8 | `INACCT.TAXPARAM.NEW.TDS.VERSION` | `InacctTaxCalcParam_NewTdsVersion` | TField |  | If the Value is set as Y, then the TDS deduction and its reversal will happen Based on the configured Link Tax. |
| 9 | `INACCT.TAXPARAM.PENALTY.TAX.CATEG.ACC` | `InacctTaxCalcParam_PenaltyTaxCategAcc` | TField |  | Holds the Internal Account, Category For this account and Penalty Int Link Tax Category should be same. Account No from which Penalty interest will be recovered. |
| 10 | `INACCT.TAXPARAM.LOCAL.REF` | `InacctTaxCalcParam_LocalRef` |  |  |  |
| 11 | `INACCT.TAXPARAM.OVERRIDE` | `InacctTaxCalcParam_Override` |  |  |  |
| 12 | `INACCT.TAXPARAM.RECORD.STATUS` | `InacctTaxCalcParam_RecordStatus` | String |  |  |
| 13 | `INACCT.TAXPARAM.CURR.NO` | `InacctTaxCalcParam_CurrNo` | String |  |  |
| 14 | `INACCT.TAXPARAM.INPUTTER` | `InacctTaxCalcParam_Inputter` |  |  |  |
| 15 | `INACCT.TAXPARAM.DATE.TIME` | `InacctTaxCalcParam_DateTime` |  |  |  |
| 16 | `INACCT.TAXPARAM.AUTHORISER` | `InacctTaxCalcParam_Authoriser` | String |  |  |
| 17 | `INACCT.TAXPARAM.CO.CODE` | `InacctTaxCalcParam_CoCode` | String |  |  |
| 18 | `INACCT.TAXPARAM.DEPT.CODE` | `InacctTaxCalcParam_DeptCode` | String |  |  |
| 19 | `INACCT.TAXPARAM.AUDITOR.CODE` | `InacctTaxCalcParam_AuditorCode` | String |  |  |
| 20 | `INACCT.TAXPARAM.AUDIT.DATE.TIME` | `InacctTaxCalcParam_AuditDateTime` | String |  |  |
| 21 | `INACCT.TAXPARAM.PENALTY.INT.CR.CATEG` | `InacctTaxCalcParam_PenaltyIntCrCateg` | TField |  | Holds the PL category, which is used to credit the Penalty Interest Valid Range For PL Category is From 50000 to 69999. |
| 22 | `INACCT.TAXPARAM.PEN.AC.ENTRY.PARAM` | `InacctTaxCalcParam_PenAcEntryParam` | TField |  | Holds the ID from the AC.ENTRY.PARAM application, which is used to Initiate the Penalty Interest Transaction. |
| 23 | `INACCT.TAXPARAM.COLLECT.BUCKET.RATE` | `InacctTaxCalcParam_CollectBucketRate` | TField |  | If the Value is set as Y, then collect the interest to be recovered from the customer Based on the Bucket Rate while Redeem a deposit. |
| 24 | `INACCT.TAXPARAM.DEPOSIT.INT.PROPERTY` | `InacctTaxCalcParam_DepositIntProperty` | TField |  | This field contains the Deposit interest property used in the product. |
| 25 | `INACCT.TAXPARAM.PI.EXCLUSION.ACTIVITY` | `InacctTaxCalcParam_PiExclusionActivity` |  |  |  |
| 26 | `INACCT.TAXPARAM.PARTIAL.TAX.CATEG.ACC` | `InacctTaxCalcParam_PartialTaxCategAcc` | TField |  | Account from which the excess tax amount will be debited. |
| 27 | `INACCT.TAXPARAM.DEPOSIT.CREDIT.INT.PROPERTY` | `InacctTaxCalcParam_DepositCreditIntProperty` | TField |  | The interest property that will be set as PAY so that interest during partial withdrawal will be credited to this property, which will be taken up for tax and penalty interest processing. |
