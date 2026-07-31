# AFRTRD.TRADE.MANUAL.INPUTATION — Table Schema

> Source: `INSERTS/I_F.AFRTRD.TRADE.MANUAL.INPUTATION` in `AFRTRD_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AFRTRD.MANUAL.DECLARATION.ID` | `AfrtrdTradeManualInputation_DeclarationId` | TField |  | Declaration Id for which the manual inputation is done. |
| 2 | `AFRTRD.MANUAL.DOMICILED.TXN` | `AfrtrdTradeManualInputation_DomiciledTxn` |  |  |  |
| 3 | `AFRTRD.MANUAL.TRANSACTION.REF` | `AfrtrdTradeManualInputation_TransactionRef` |  |  |  |
| 4 | `AFRTRD.MANUAL.TRANSACTION.DATE` | `AfrtrdTradeManualInputation_TransactionDate` |  |  |  |
| 5 | `AFRTRD.MANUAL.TRANSACTION.AMOUNT` | `AfrtrdTradeManualInputation_TransactionAmount` |  |  |  |
| 6 | `AFRTRD.MANUAL.TRANSACTION.CURRENCY` | `AfrtrdTradeManualInputation_TransactionCurrency` |  |  |  |
| 7 | `AFRTRD.MANUAL.LOCAL.REF` | `AfrtrdTradeManualInputation_LocalRef` |  |  |  |
| 8 | `AFRTRD.MANUAL.OVERRIDE` | `AfrtrdTradeManualInputation_Override` |  |  |  |
| 9 | `AFRTRD.MANUAL.RECORD.STATUS` | `AfrtrdTradeManualInputation_RecordStatus` | String |  |  |
| 10 | `AFRTRD.MANUAL.CURR.NO` | `AfrtrdTradeManualInputation_CurrNo` | String |  |  |
| 11 | `AFRTRD.MANUAL.INPUTTER` | `AfrtrdTradeManualInputation_Inputter` |  |  |  |
| 12 | `AFRTRD.MANUAL.DATE.TIME` | `AfrtrdTradeManualInputation_DateTime` |  |  |  |
| 13 | `AFRTRD.MANUAL.AUTHORISER` | `AfrtrdTradeManualInputation_Authoriser` | String |  |  |
| 14 | `AFRTRD.MANUAL.CO.CODE` | `AfrtrdTradeManualInputation_CoCode` | String |  |  |
| 15 | `AFRTRD.MANUAL.DEPT.CODE` | `AfrtrdTradeManualInputation_DeptCode` | String |  |  |
| 16 | `AFRTRD.MANUAL.AUDITOR.CODE` | `AfrtrdTradeManualInputation_AuditorCode` | String |  |  |
| 17 | `AFRTRD.MANUAL.AUDIT.DATE.TIME` | `AfrtrdTradeManualInputation_AuditDateTime` | String |  |  |
