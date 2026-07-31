# FRPFNL.TAX.PARAMETER — Table Schema

> Source: `INSERTS/I_F.FRPFNL.TAX.PARAMETER` in `FRPFNL_InvestmentIncomeTax.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FR.PARAM.CASH.FUND.DIV.DIARY.TYPE` | `FrpfnlTaxParameter_CashFundDivDiaryType` |  |  |  |
| 2 | `FR.PARAM.CASH.DIV.SAT.START.RG` | `FrpfnlTaxParameter_CashDivSatStartRg` |  |  |  |
| 3 | `FR.PARAM.CASH.DIV.SAT.END.RG` | `FrpfnlTaxParameter_CashDivSatEndRg` |  |  |  |
| 4 | `FR.PARAM.FUND.DIV.SAT.START.RG` | `FrpfnlTaxParameter_FundDivSatStartRg` |  |  |  |
| 5 | `FR.PARAM.FUND.DIV.SAT.END.RG` | `FrpfnlTaxParameter_FundDivSatEndRg` |  |  |  |
| 6 | `FR.PARAM.COUPON.DIARY.TYPE` | `FrpfnlTaxParameter_CouponDiaryType` |  |  |  |
| 7 | `FR.PARAM.REDEMPTION.DIARY.TYPE` | `FrpfnlTaxParameter_RedemptionDiaryType` |  |  |  |
| 8 | `FR.PARAM.TR.FEE.TRANS.CODE` | `FrpfnlTaxParameter_TrFeeTransCode` | TField |  | Define transaction code which will be used to identify Trailer fee credit refund amount in STMT.ENTRY. |
| 9 | `FR.PARAM.PFNL.FT.TRANS.TYPE` | `FrpfnlTaxParameter_PfnlFtTransType` | TField |  | Define transaction code which will be used to create FT for Tax on Trailer fee credit refund amount. |
| 10 | `FR.PARAM.PFNL.TAX.CATEG` | `FrpfnlTaxParameter_PfnlTaxCateg` | TField |  | Define appropriate PFNL tax category as defined in TAX record for PFNL tax to credit tax amount on trailer fee refund. |
| 11 | `FR.PARAM.PFNL.TAX.TYPE.CONDITION` | `FrpfnlTaxParameter_PfnlTaxTypeCondition` | TField |  | Define the PFNL Tax type condition record id. |
| 12 | `FR.PARAM.LOCAL.REF` | `FrpfnlTaxParameter_LocalRef` |  |  |  |
| 13 | `FR.PARAM.OVERRIDE` | `FrpfnlTaxParameter_Override` |  |  |  |
| 14 | `FR.PARAM.RECORD.STATUS` | `FrpfnlTaxParameter_RecordStatus` | String |  |  |
| 15 | `FR.PARAM.CURR.NO` | `FrpfnlTaxParameter_CurrNo` | String |  |  |
| 16 | `FR.PARAM.INPUTTER` | `FrpfnlTaxParameter_Inputter` |  |  |  |
| 17 | `FR.PARAM.DATE.TIME` | `FrpfnlTaxParameter_DateTime` |  |  |  |
| 18 | `FR.PARAM.AUTHORISER` | `FrpfnlTaxParameter_Authoriser` | String |  |  |
| 19 | `FR.PARAM.CO.CODE` | `FrpfnlTaxParameter_CoCode` | String |  |  |
| 20 | `FR.PARAM.DEPT.CODE` | `FrpfnlTaxParameter_DeptCode` | String |  |  |
| 21 | `FR.PARAM.AUDITOR.CODE` | `FrpfnlTaxParameter_AuditorCode` | String |  |  |
| 22 | `FR.PARAM.AUDIT.DATE.TIME` | `FrpfnlTaxParameter_AuditDateTime` | String |  |  |
