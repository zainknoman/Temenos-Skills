# FS.GI.DIVIDEND.REINVESTMENT.DETAILS — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIVIDEND.REINVESTMENT.DETAILS` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GI.DIV.REINVESTMENT.DET.REGISTER.ID` | `FsGiDividendReinvestmentDetails_RegisterId` |  |  |  |
| 2 | `GI.DIV.REINVESTMENT.DET.SEQUENCE.NUMBER` | `FsGiDividendReinvestmentDetails_SequenceNumber` |  |  |  |
| 3 | `GI.DIV.REINVESTMENT.DET.FUND.ID` | `FsGiDividendReinvestmentDetails_FundId` |  |  |  |
| 4 | `GI.DIV.REINVESTMENT.DET.SHARE.CLASS.CODE` | `FsGiDividendReinvestmentDetails_ShareClassCode` |  |  |  |
| 5 | `GI.DIV.REINVESTMENT.DET.PRODUCT.CODE` | `FsGiDividendReinvestmentDetails_ProductCode` |  |  |  |
| 6 | `GI.DIV.REINVESTMENT.DET.GROUP.ID` | `FsGiDividendReinvestmentDetails_GroupId` |  |  |  |
| 7 | `GI.DIV.REINVESTMENT.DET.REINVESTMENT.FUND` | `FsGiDividendReinvestmentDetails_ReinvestmentFund` |  |  |  |
| 8 | `GI.DIV.REINVESTMENT.DET.REINVESTMENT.SHARE.CLASS.CODE` | `FsGiDividendReinvestmentDetails_ReinvestmentShareClassCode` |  |  |  |
| 9 | `GI.DIV.REINVESTMENT.DET.REINVESTMENT.NAV` | `FsGiDividendReinvestmentDetails_ReinvestmentNav` |  |  |  |
| 10 | `GI.DIV.REINVESTMENT.DET.REINVESTMENT.QUANTITY` | `FsGiDividendReinvestmentDetails_ReinvestmentQuantity` |  |  |  |
| 11 | `GI.DIV.REINVESTMENT.DET.REINVESTMENT.COMMISSION` | `FsGiDividendReinvestmentDetails_ReinvestmentCommission` |  |  |  |
| 12 | `GI.DIV.REINVESTMENT.DET.REINVESTMENT.NET.AMT` | `FsGiDividendReinvestmentDetails_ReinvestmentNetAmt` |  |  |  |
| 13 | `GI.DIV.REINVESTMENT.DET.REINVESTMENT.NET.AMT.FUND.CCY` | `FsGiDividendReinvestmentDetails_ReinvestmentNetAmtFundCcy` |  |  |  |
| 14 | `GI.DIV.REINVESTMENT.DET.FX.RATE` | `FsGiDividendReinvestmentDetails_FxRate` |  |  |  |
| 15 | `GI.DIV.REINVESTMENT.DET.PAYMENT.TYPE` | `FsGiDividendReinvestmentDetails_PaymentType` |  |  |  |
| 16 | `GI.DIV.REINVESTMENT.DET.AGENT.ID` | `FsGiDividendReinvestmentDetails_AgentId` |  |  |  |
| 17 | `GI.DIV.REINVESTMENT.DET.REINVESTMENT.ORDER.ID` | `FsGiDividendReinvestmentDetails_ReinvestmentOrderId` |  |  |  |
| 18 | `GI.DIV.REINVESTMENT.DET.REINVESTMENT.INTERNAL.NUMBER` | `FsGiDividendReinvestmentDetails_ReinvestmentInternalNumber` |  |  |  |
| 19 | `GI.DIV.REINVESTMENT.DET.OPERATION.CODE` | `FsGiDividendReinvestmentDetails_OperationCode` |  |  |  |
| 20 | `GI.DIV.REINVESTMENT.DET.CALCULATED.NAV` | `FsGiDividendReinvestmentDetails_CalculatedNav` |  |  |  |
| 21 | `GI.DIV.REINVESTMENT.DET.COMMISSION.PERCENTAGE` | `FsGiDividendReinvestmentDetails_CommissionPercentage` |  |  |  |
| 22 | `GI.DIV.REINVESTMENT.DET.FORCED.COMMISSION.PERCENTAGE` | `FsGiDividendReinvestmentDetails_ForcedCommissionPercentage` |  |  |  |
| 23 | `GI.DIV.REINVESTMENT.DET.COMMISSION.PERIOD.TYPE` | `FsGiDividendReinvestmentDetails_CommissionPeriodType` |  |  |  |
| 24 | `GI.DIV.REINVESTMENT.DET.TEMPLATE.ID` | `FsGiDividendReinvestmentDetails_TemplateId` |  |  |  |
| 25 | `GI.DIV.REINVESTMENT.DET.CONFIRM.USER` | `FsGiDividendReinvestmentDetails_ConfirmUser` |  |  |  |
| 26 | `GI.DIV.REINVESTMENT.DET.RESERVED10` | `FsGiDividendReinvestmentDetails_Reserved10` |  |  |  |
| 27 | `GI.DIV.REINVESTMENT.DET.RESERVED9` | `FsGiDividendReinvestmentDetails_Reserved9` |  |  |  |
| 28 | `GI.DIV.REINVESTMENT.DET.RESERVED8` | `FsGiDividendReinvestmentDetails_Reserved8` |  |  |  |
| 29 | `GI.DIV.REINVESTMENT.DET.RESERVED7` | `FsGiDividendReinvestmentDetails_Reserved7` |  |  |  |
| 30 | `GI.DIV.REINVESTMENT.DET.RESERVED6` | `FsGiDividendReinvestmentDetails_Reserved6` |  |  |  |
| 31 | `GI.DIV.REINVESTMENT.DET.RESERVED5` | `FsGiDividendReinvestmentDetails_Reserved5` |  |  |  |
| 32 | `GI.DIV.REINVESTMENT.DET.RESERVED4` | `FsGiDividendReinvestmentDetails_Reserved4` |  |  |  |
| 33 | `GI.DIV.REINVESTMENT.DET.RESERVED3` | `FsGiDividendReinvestmentDetails_Reserved3` |  |  |  |
| 34 | `GI.DIV.REINVESTMENT.DET.RESERVED2` | `FsGiDividendReinvestmentDetails_Reserved2` |  |  |  |
| 35 | `GI.DIV.REINVESTMENT.DET.RESERVED1` | `FsGiDividendReinvestmentDetails_Reserved1` |  |  |  |
| 36 | `GI.DIV.REINVESTMENT.DET.LOCAL.REF` | `FsGiDividendReinvestmentDetails_LocalRef` |  |  |  |
| 37 | `GI.DIV.REINVESTMENT.DET.OVERRIDE` | `FsGiDividendReinvestmentDetails_Override` |  |  |  |
| 38 | `GI.DIV.REINVESTMENT.DET.RECORD.STATUS` | `FsGiDividendReinvestmentDetails_RecordStatus` |  |  |  |
| 39 | `GI.DIV.REINVESTMENT.DET.CURR.NO` | `FsGiDividendReinvestmentDetails_CurrNo` |  |  |  |
| 40 | `GI.DIV.REINVESTMENT.DET.INPUTTER` | `FsGiDividendReinvestmentDetails_Inputter` |  |  |  |
| 41 | `GI.DIV.REINVESTMENT.DET.DATE.TIME` | `FsGiDividendReinvestmentDetails_DateTime` |  |  |  |
| 42 | `GI.DIV.REINVESTMENT.DET.AUTHORISER` | `FsGiDividendReinvestmentDetails_Authoriser` |  |  |  |
| 43 | `GI.DIV.REINVESTMENT.DET.CO.CODE` | `FsGiDividendReinvestmentDetails_CoCode` |  |  |  |
| 44 | `GI.DIV.REINVESTMENT.DET.DEPT.CODE` | `FsGiDividendReinvestmentDetails_DeptCode` |  |  |  |
| 45 | `GI.DIV.REINVESTMENT.DET.AUDITOR.CODE` | `FsGiDividendReinvestmentDetails_AuditorCode` |  |  |  |
| 46 | `GI.DIV.REINVESTMENT.DET.AUDIT.DATE.TIME` | `FsGiDividendReinvestmentDetails_AuditDateTime` |  |  |  |
