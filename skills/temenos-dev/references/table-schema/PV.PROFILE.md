# PV.PROFILE — Table Schema

> Source: `INSERTS/I_F.PV.PROFILE` in `PV_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PVP.DESCRIPTION` | `PvProfile_Description` |  |  |  |
| 2 | `PVP.PROV.TYPE` | `PvProfile_ProvType` |  |  |  |
| 3 | `PVP.PROV.CALC` | `PvProfile_ProvCalc` |  |  |  |
| 4 | `PVP.SOURCE.BALANCE` | `PvProfile_SourceBalance` |  |  |  |
| 5 | `PVP.CLASS` | `PvProfile_Class` |  |  |  |
| 6 | `PVP.STD.PERCENT` | `PvProfile_StdPercent` |  |  |  |
| 7 | `PVP.SEC.PERCENT` | `PvProfile_SecPercent` |  |  |  |
| 8 | `PVP.DEF.PROB` | `PvProfile_DefProb` |  |  |  |
| 9 | `PVP.LSS.GIVN.DEF` | `PvProfile_LssGivnDef` |  |  |  |
| 10 | `PVP.LSS.ID.PER` | `PvProfile_LssIdPer` |  |  |  |
| 11 | `PVP.IMPAIR.CODE` | `PvProfile_ImpairCode` |  |  |  |
| 12 | `PVP.DEAL.IMPAIR` | `PvProfile_DealImpair` |  |  |  |
| 13 | `PVP.PROV.API` | `PvProfile_ProvApi` |  |  |  |
| 14 | `PVP.ACCOUNTING` | `PvProfile_Accounting` | TField |  | Indicates whether the provision amount (which has been calculated and recorded) should be accounted for. DEAL: To Raise Accounting at Individual Level |
| 15 | `PVP.POSTING.DETAILS` | `PvProfile_PostingDetails` | TField | Yes | Valid record of IFRS.POSTING.DETAILS. ACCT.HEAD.TYPE, CATEGORY, Transaction code everything related to raising entries is defined here. Validation Mandatory field. If Provision calculation is IFRS, then the record in posting details should have position type as 'IF' and ACCT.HEAD.TYPE as 'PROVISION' Otherwise for provision calculation PERCENTAGE, then the record in posting details should have position type as 'TR' and ACCT.HEAD.TYPE as 'PROVISION' |
| 16 | `PVP.COLLATERAL.USE` | `PvProfile_CollateralUse` | TField |  | The field enables the User to configure the usage of collateral, if any allocated to the contract/account for which provision is calculated. The allowed options are - Mitigate or Secured.Unsecured � When the Mitigate option is defined, the collateral amount allocated to the contract will be reduced from the source balance and only the remaining unsecured portion of the source balance is considered for applying the Standard provision percentage to calculate the provision amount. � When the Secured.Unsecured option is defined, the User can define different provision percent for the secured portion and the unsecured portion of the source balance. The provision percent for the secured portion is defined in the Sec.Percent field and that for the unsecured portion is defined in the Std.Percent field for the respective risk classification. This field is allowed input only when the Prov.Calc field is 'Percentage' |
| 17 | `PVP.COLLATERAL.VALUE` | `PvProfile_CollateralValue` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 18 | `PVP.PROB.OF.DEFT` | `PvProfile_ProbOfDeft` |  |  |  |
| 19 | `PVP.LOSS.GIVEN.DEFT` | `PvProfile_LossGivenDeft` | TField |  | Facilitate the option to the bank to configure the Loss Given Default (LGD) at the individual product or range of product level in IFRS 9 impairment Model. Validation Rules: Input enabled only when I9 installed. Accepts number or percentage depending on the values defined on LGD.VAL.FMT field of IFRS Parameter. |
| 20 | `PVP.CCF.CUT.OFF` | `PvProfile_CcfCutOff` | TField |  | This field specifies the percentage of amount to be excluded while calculation the provision amount. Validation Rules: Range is between 0 and 100. |
| 21 | `PVP.SEGMENT` | `PvProfile_Segment` |  |  |  |
| 22 | `PVP.SEG.PROV.TYPE` | `PvProfile_SegProvType` |  |  |  |
| 23 | `PVP.SEG.SOURCE.BALANCE` | `PvProfile_SegSourceBalance` |  |  |  |
| 24 | `PVP.SEG.PROV.CALC` | `PvProfile_SegProvCalc` |  |  |  |
| 25 | `PVP.SEG.CLASS` | `PvProfile_SegClass` |  |  |  |
| 26 | `PVP.LOCAL.REF` | `PvProfile_LocalRef` |  |  |  |
| 27 | `PVP.OVERRIDE` | `PvProfile_Override` |  |  |  |
| 28 | `PVP.RECORD.STATUS` | `PvProfile_RecordStatus` | String |  |  |
| 29 | `PVP.CURR.NO` | `PvProfile_CurrNo` | String |  |  |
| 30 | `PVP.INPUTTER` | `PvProfile_Inputter` |  |  |  |
| 31 | `PVP.DATE.TIME` | `PvProfile_DateTime` |  |  |  |
| 32 | `PVP.AUTHORISER` | `PvProfile_Authoriser` | String |  |  |
| 33 | `PVP.CO.CODE` | `PvProfile_CoCode` | String |  |  |
| 34 | `PVP.DEPT.CODE` | `PvProfile_DeptCode` | String |  |  |
| 35 | `PVP.AUDITOR.CODE` | `PvProfile_AuditorCode` | String |  |  |
| 36 | `PVP.AUDIT.DATE.TIME` | `PvProfile_AuditDateTime` | String |  |  |
| 37 | `PVP.SEG.STD.PERCENT` | `PvProfile_SegStdPercent` |  |  |  |
| 38 | `PVP.SEG.SEC.PERCENT` | `PvProfile_SegSecPercent` |  |  |  |
| 39 | `PVP.SEG.DEF.PROB` | `PvProfile_SegDefProb` |  |  |  |
| 40 | `PVP.SEG.LOSS.GIV.DEF` | `PvProfile_SegLossGivDef` |  |  |  |
| 41 | `PVP.SEG.LOSS.ID.PER` | `PvProfile_SegLossIdPer` |  |  |  |
| 42 | `PVP.SEG.IMPAIR.CODE` | `PvProfile_SegImpairCode` |  |  |  |
| 43 | `PVP.SEG.DEAL.IMPAIR` | `PvProfile_SegDealImpair` |  |  |  |
| 44 | `PVP.COLLATERAL.AMT.API` | `PvProfile_CollateralAmtApi` | TField |  | An API routine to calculate the risk collateral of the contract. Validation Rules: Should be a valid EB.API. |
| 45 | `PVP.SEG.CCF.CUT.OFF` | `PvProfile_SegCcfCutOff` |  |  |  |
| 46 | `PVP.SEG.STD.SEC.API` | `PvProfile_SegStdSecApi` |  |  |  |
