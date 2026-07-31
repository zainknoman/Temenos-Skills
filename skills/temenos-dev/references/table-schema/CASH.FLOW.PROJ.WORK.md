# CASH.FLOW.PROJ.WORK — Table Schema

> Source: `INSERTS/I_F.CASH.FLOW.PROJ.WORK` in `AM_CashFlow.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CFR.CUSTOMER` | `CashFlowProjWork_Customer` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `CFR.COUPON` | `CashFlowProjWork_Coupon` |  |  |  |
| 3 | `CFR.REDEMPTION` | `CashFlowProjWork_Redemption` |  |  |  |
| 4 | `CFR.MATURITY.DATE` | `CashFlowProjWork_MaturityDate` |  |  |  |
| 5 | `CFR.CURRENCY` | `CashFlowProjWork_Currency` |  |  |  |
| 6 | `CFR.AMOUNT` | `CashFlowProjWork_Amount` |  |  |  |
| 7 | `CFR.DESCRIPTION` | `CashFlowProjWork_Description` |  |  |  |
| 8 | `CFR.REFERENCE` | `CashFlowProjWork_Reference` |  |  |  |
| 9 | `CFR.TRADE.DATE` | `CashFlowProjWork_TradeDate` |  |  |  |
| 10 | `CFR.TRANS.CODE` | `CashFlowProjWork_TransCode` |  |  |  |
| 11 | `CFR.PORTFOLIO` | `CashFlowProjWork_Portfolio` |  |  |  |
| 12 | `CFR.PORTFOLIO.NO` | `CashFlowProjWork_PortfolioNo` |  |  |  |
| 13 | `CFR.START.DATE` | `CashFlowProjWork_StartDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 14 | `CFR.END.DATE` | `CashFlowProjWork_EndDate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 15 | `CFR.DEPT.ACCT.NO` | `CashFlowProjWork_DeptAcctNo` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 16 | `CFR.PRINT` | `CashFlowProjWork_Print` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 17 | `CFR.RECORD.STATUS` | `CashFlowProjWork_RecordStatus` | String |  |  |
| 18 | `CFR.CURR.NO` | `CashFlowProjWork_CurrNo` | String |  |  |
| 19 | `CFR.INPUTTER` | `CashFlowProjWork_Inputter` |  |  |  |
| 20 | `CFR.DATE.TIME` | `CashFlowProjWork_DateTime` |  |  |  |
| 21 | `CFR.AUTHORISER` | `CashFlowProjWork_Authoriser` | String |  |  |
| 22 | `CFR.CO.CODE` | `CashFlowProjWork_CoCode` | String |  |  |
| 23 | `CFR.DEPT.CODE` | `CashFlowProjWork_DeptCode` | String |  |  |
| 24 | `CFR.AUDITOR.CODE` | `CashFlowProjWork_AuditorCode` | String |  |  |
| 25 | `CFR.AUDIT.DATE.TIME` | `CashFlowProjWork_AuditDateTime` | String |  |  |
