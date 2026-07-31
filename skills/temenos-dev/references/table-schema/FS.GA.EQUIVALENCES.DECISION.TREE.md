# FS.GA.EQUIVALENCES.DECISION.TREE — Table Schema

> Source: `INSERTS/I_F.FS.GA.EQUIVALENCES.DECISION.TREE` in `FS_Equivalence.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.EQUIVALENCES.DECISION.TREE.PARENT.REF.ID` | `FsGaEquivalencesDecisionTree_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.EQUIVALENCES.DECISION.TREE.ORA.ROWID` | `FsGaEquivalencesDecisionTree_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.EQUIVALENCES.DECISION.TREE.PRICING.FACTOR.CODE` | `FsGaEquivalencesDecisionTree_PricingFactorCode` | TField |  | Pricing factor code of security to determine how the price is quoted based on which the transaction amount is determined Multifonds DB Column is CCALCUL. |
| 4 | `FS.GA.EQUIVALENCES.DECISION.TREE.CONTRACT.SIZE` | `FsGaEquivalencesDecisionTree_ContractSize` | TField |  | The contract size (if not zero) is used as a multiplier. Multifonds DB Column is FMULTI. |
| 5 | `FS.GA.EQUIVALENCES.DECISION.TREE.COUNTRY.ID.CODE` | `FsGaEquivalencesDecisionTree_CountryIdCode` | TField |  | Defines the country short code Multifonds DB Column is CPAYS. |
| 6 | `FS.GA.EQUIVALENCES.DECISION.TREE.DECIMAL.ROUNDING.CODE` | `FsGaEquivalencesDecisionTree_DecimalRoundingCode` | TField |  | Number of decimals to be taken for currency amounts . Generally,the number of decimals would be 2 except for currencies like Japanese Yen for instance, where the number of decimals is equal to zero. Multifonds DB Column is CDEC. |
| 7 | `FS.GA.EQUIVALENCES.DECISION.TREE.DEPOSITORY.NUMBER` | `FsGaEquivalencesDecisionTree_DepositoryNumber` | TField |  | Depositary Number Multifonds DB Column is NDEPOSIT. |
| 8 | `FS.GA.EQUIVALENCES.DECISION.TREE.EVALUATION.TYPE` | `FsGaEquivalencesDecisionTree_EvaluationType` | TField |  | Valuation method for specific security types such as zero bonds, polish T-bills, Mortgaged Backed Securities. Multifonds DB Column is TEVALUATION. |
| 9 | `FS.GA.EQUIVALENCES.DECISION.TREE.FEES.CODE` | `FsGaEquivalencesDecisionTree_FeesCode` | TField |  | This field hepls the user to take into account or remove from the fees based amount the sum of specific fees codes setup of the security master. Multifonds DB Column is FFEES. |
| 10 | `FS.GA.EQUIVALENCES.DECISION.TREE.GTI.CODE` | `FsGaEquivalencesDecisionTree_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 11 | `FS.GA.EQUIVALENCES.DECISION.TREE.INCOME.TYPE` | `FsGaEquivalencesDecisionTree_IncomeType` | TField |  | Income type whether from settlement date or settlement date+1 for security lending/borrowing comm accrual Multifonds DB Column is TREVENU. |
| 12 | `FS.GA.EQUIVALENCES.DECISION.TREE.INTERNAL.CATEGORY.CODE` | `FsGaEquivalencesDecisionTree_InternalCategoryCode` | TField |  | Internal Category Code for security master interface Multifonds DB Column is CAT_INTERNE. |
| 13 | `FS.GA.EQUIVALENCES.DECISION.TREE.REPORTING.CODE` | `FsGaEquivalencesDecisionTree_ReportingCode` | TField |  | This is the reporting code tagged to an account. Multifonds DB Column is CODE_RAPPORT. |
| 14 | `FS.GA.EQUIVALENCES.DECISION.TREE.USE.COUPON` | `FsGaEquivalencesDecisionTree_UseCoupon` | TField | Yes | Define if the coupon information are mandatory or not for security master interface. Should not be ticked for Share. Multifonds DB Column is USE_COUPON. |
| 15 | `FS.GA.EQUIVALENCES.DECISION.TREE.USE.CUSANCE` | `FsGaEquivalencesDecisionTree_UseCusance` | TField | Yes | Define if the Day Count Convention is mandatory or not for security master interface. Should not be ticked for shares. Multifonds DB Column is USE_CUSANCE. |
| 16 | `FS.GA.EQUIVALENCES.DECISION.TREE.DAY.COUNT.CONVENTION` | `FsGaEquivalencesDecisionTree_DayCountConvention` | TField |  | Corresponds to default parameters to be used for calculation of specific hedged yield report. Multifonds DB Column is CUSANCE. |
| 17 | `FS.GA.EQUIVALENCES.DECISION.TREE.RESERVED10` | `FsGaEquivalencesDecisionTree_Reserved10` | TField |  |  |
| 18 | `FS.GA.EQUIVALENCES.DECISION.TREE.RESERVED9` | `FsGaEquivalencesDecisionTree_Reserved9` | TField |  |  |
| 19 | `FS.GA.EQUIVALENCES.DECISION.TREE.RESERVED8` | `FsGaEquivalencesDecisionTree_Reserved8` | TField |  |  |
| 20 | `FS.GA.EQUIVALENCES.DECISION.TREE.RESERVED7` | `FsGaEquivalencesDecisionTree_Reserved7` | TField |  |  |
| 21 | `FS.GA.EQUIVALENCES.DECISION.TREE.RESERVED6` | `FsGaEquivalencesDecisionTree_Reserved6` | TField |  |  |
| 22 | `FS.GA.EQUIVALENCES.DECISION.TREE.RESERVED5` | `FsGaEquivalencesDecisionTree_Reserved5` | TField |  |  |
| 23 | `FS.GA.EQUIVALENCES.DECISION.TREE.RESERVED4` | `FsGaEquivalencesDecisionTree_Reserved4` | TField |  |  |
| 24 | `FS.GA.EQUIVALENCES.DECISION.TREE.RESERVED3` | `FsGaEquivalencesDecisionTree_Reserved3` | TField |  |  |
| 25 | `FS.GA.EQUIVALENCES.DECISION.TREE.RESERVED2` | `FsGaEquivalencesDecisionTree_Reserved2` | TField |  |  |
| 26 | `FS.GA.EQUIVALENCES.DECISION.TREE.RESERVED1` | `FsGaEquivalencesDecisionTree_Reserved1` | TField |  |  |
| 27 | `FS.GA.EQUIVALENCES.DECISION.TREE.LOCAL.REF` | `FsGaEquivalencesDecisionTree_LocalRef` |  |  |  |
| 28 | `FS.GA.EQUIVALENCES.DECISION.TREE.OVERRIDE` | `FsGaEquivalencesDecisionTree_Override` |  |  |  |
| 29 | `FS.GA.EQUIVALENCES.DECISION.TREE.RECORD.STATUS` | `FsGaEquivalencesDecisionTree_RecordStatus` | String |  |  |
| 30 | `FS.GA.EQUIVALENCES.DECISION.TREE.CURR.NO` | `FsGaEquivalencesDecisionTree_CurrNo` | String |  |  |
| 31 | `FS.GA.EQUIVALENCES.DECISION.TREE.INPUTTER` | `FsGaEquivalencesDecisionTree_Inputter` |  |  |  |
| 32 | `FS.GA.EQUIVALENCES.DECISION.TREE.DATE.TIME` | `FsGaEquivalencesDecisionTree_DateTime` |  |  |  |
| 33 | `FS.GA.EQUIVALENCES.DECISION.TREE.AUTHORISER` | `FsGaEquivalencesDecisionTree_Authoriser` | String |  |  |
| 34 | `FS.GA.EQUIVALENCES.DECISION.TREE.CO.CODE` | `FsGaEquivalencesDecisionTree_CoCode` | String |  |  |
| 35 | `FS.GA.EQUIVALENCES.DECISION.TREE.DEPT.CODE` | `FsGaEquivalencesDecisionTree_DeptCode` | String |  |  |
| 36 | `FS.GA.EQUIVALENCES.DECISION.TREE.AUDITOR.CODE` | `FsGaEquivalencesDecisionTree_AuditorCode` | String |  |  |
| 37 | `FS.GA.EQUIVALENCES.DECISION.TREE.AUDIT.DATE.TIME` | `FsGaEquivalencesDecisionTree_AuditDateTime` | String |  |  |
