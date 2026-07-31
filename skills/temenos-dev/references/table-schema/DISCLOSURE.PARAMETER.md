# DISCLOSURE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.DISCLOSURE.PARAMETER` in `CALEND_CostBorrowing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CALEND.COB.DESCRIPTION` | `DisclosureParameter_Description` |  |  |  |
| 2 | `CALEND.COB.OPT.SERVICES` | `DisclosureParameter_OptServices` |  |  |  |
| 3 | `CALEND.COB.COB.FEES` | `DisclosureParameter_CobFees` |  |  |  |
| 4 | `CALEND.COB.PROV.FEES` | `DisclosureParameter_ProvFees` |  |  |  |
| 5 | `CALEND.COB.LOC.PERIOD` | `DisclosureParameter_LocPeriod` | TField |  | The value entered in this field will be numeric number with suffix "D" or "M".Based on the defined period, COB will be disclosed for LOC product, if no eligible activities are performed on LOC in specified period.Eg - 1M, 1D.Validations - Based on the product defined in IS.LOC.PRODUCT field system generates the COB disclosure process based on the period defiend in this field. (if no activities/actions performed on the account during this period). |
| 6 | `CALEND.COB.IS.LOC.PRODUCT` | `DisclosureParameter_IsLocProduct` | TField |  | This field is used to indicate if the Subjected Product as part of ID is a LOC product or Not.Valid Entry - Yes/No--&gt;YES - ID product will be treated as LOC product to trigger cOB activity based on the LOC Period.ID product will be considered as LOC product and COB calculation is based on below formula.LOC Calculation:Annual Interest Rate (AA.ARR.INTEREST&gt;FLOATING.INDEX or AA.ARR.INTEREST &gt; PERIODIC.RATE), plus an adjustment factor (AA.ARR.INTEREST &gt; MARGIN.OPERAND), which is the margin rate. The net effective rate based on these fields (Interest Key, Margin Operand &amp; Margin.--&gt; NO - ID product will not be treated as LOC product.Based on the identification of this field, Annual Interest Rate calculation is considered. added |
| 7 | `CALEND.COB.COB.ACTIVITY` | `DisclosureParameter_CobActivity` | TField |  | This field is used to define the named Activity, which triggers advice generation for COB disclosure process.Validations - Records of AA.ACTIVITY modified |
| 8 | `CALEND.COB.AA.VERSION` | `DisclosureParameter_AaVersion` | TField |  | Purpose of this field to store the version to be used to trigger the activity defined in COB.ACTIVITY.Validations -Valid record of VERSION. modified |
| 9 | `CALEND.COB.OFS.SOURCE` | `DisclosureParameter_OfsSource` | TField |  | Field used to store the OFS source id for COB disclosure process.Validations - Valid record of OFS.SOURCEEg. CAPL.SRC modified |
| 10 | `CALEND.COB.EXCL.PAY.TYPE` | `DisclosureParameter_ExclPayType` |  |  |  |
| 11 | `CALEND.COB.LOAN.INT.PROP` | `DisclosureParameter_LoanIntProp` | TField |  | Field to indicate the Loan Interest Property (AA.PROPERTY) to be considered for COB calculation and Interest related details.Validations - Records of AA.PROPERTYEg. PRINCIPALINTIf a loan account has a payment type with 2 properties like PRINCIPALINT and ESCROW, COB disclosure process will not consider the related due charges of ESCROW. only PRINCIPALINT will be considered. |
| 12 | `CALEND.COB.SCHEDULE.RTN` | `DisclosureParameter_ScheduleRtn` | TField |  | The purpose of this field is to call the escrow schedule routine from L3, which will exclude the escrow related payments in the COB xml generated. If this field is not configured, then CORE schedule routine will be called and payment values will be updated along with escrow related payments(if any) in xml generated |
| 13 | `CALEND.COB.PRIN.BAL.TYPE` | `DisclosureParameter_PrinBalType` | TField |  | The purpose of this field is to input the balance type where the Principal amount for the xml will be fetched using this balance type. This should be a valid AC.BALANCE.TYPE record |
| 14 | `CALEND.COB.OVERRIDE` | `DisclosureParameter_Override` |  |  |  |
| 15 | `CALEND.COB.PROV.ACTIVITY` | `DisclosureParameter_ProvActivity` |  |  |  |
| 16 | `CALEND.COB.MULTIPLE.COLLATERALS` | `DisclosureParameter_MultipleCollaterals` | TField |  | This field is used to denote whether the province fee should be defaulted based on collateral province or customer province, when there are multiple collaterals. Allowed inputs are Customer, NoneCustomer / None � If customer is selected, then Province defaulting will be based on customer province when there are multiple collaterals.Collateral � If collateral is selected, then defaulting will be based on the first collateral, when multiple collaterals exists |
| 17 | `CALEND.COB.EXCL.NEXT.PAYMENT` | `DisclosureParameter_ExclNextPayment` |  |  |  |
| 18 | `CALEND.COB.RESERVED.4` | `DisclosureParameter_Reserved4` | TField |  |  |
| 19 | `CALEND.COB.RESERVED.3` | `DisclosureParameter_Reserved3` | TField |  |  |
| 20 | `CALEND.COB.RESERVED.2` | `DisclosureParameter_Reserved2` | TField |  |  |
| 21 | `CALEND.COB.RESERVED.1` | `DisclosureParameter_Reserved1` | TField |  |  |
| 22 | `CALEND.COB.RECORD.STATUS` | `DisclosureParameter_RecordStatus` | String |  |  |
| 23 | `CALEND.COB.CURR.NO` | `DisclosureParameter_CurrNo` | String |  |  |
| 24 | `CALEND.COB.INPUTTER` | `DisclosureParameter_Inputter` |  |  |  |
| 25 | `CALEND.COB.DATE.TIME` | `DisclosureParameter_DateTime` |  |  |  |
| 26 | `CALEND.COB.AUTHORISER` | `DisclosureParameter_Authoriser` | String |  |  |
| 27 | `CALEND.COB.CO.CODE` | `DisclosureParameter_CoCode` | String |  |  |
| 28 | `CALEND.COB.DEPT.CODE` | `DisclosureParameter_DeptCode` | String |  |  |
| 29 | `CALEND.COB.AUDITOR.CODE` | `DisclosureParameter_AuditorCode` | String |  |  |
| 30 | `CALEND.COB.AUDIT.DATE.TIME` | `DisclosureParameter_AuditDateTime` | String |  |  |
