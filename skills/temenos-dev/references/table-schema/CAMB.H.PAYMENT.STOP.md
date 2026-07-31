# CAMB.H.PAYMENT.STOP — Table Schema

> Source: `INSERTS/I_F.CAMB.H.PAYMENT.STOP` in `CARGPL_RegisteredPlans.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.PS.CHQ.TYPE` | `CambHPaymentStop_ChqType` |  |  |  |
| 2 | `CAMB.PS.FIRST.CHQ` | `CambHPaymentStop_FirstChq` |  |  |  |
| 3 | `CAMB.PS.LAST.CHQ` | `CambHPaymentStop_LastChq` |  |  |  |
| 4 | `CAMB.PS.AMOUNT` | `CambHPaymentStop_Amount` |  |  |  |
| 5 | `CAMB.PS.CHQ.DATE` | `CambHPaymentStop_ChqDate` |  |  |  |
| 6 | `CAMB.PS.EXPIRY.DATE` | `CambHPaymentStop_ExpiryDate` |  |  |  |
| 7 | `CAMB.PS.BENEFICIARY` | `CambHPaymentStop_Beneficiary` |  |  |  |
| 8 | `CAMB.PS.REPLACE.CHQ.NO` | `CambHPaymentStop_ReplaceChqNo` |  |  |  |
| 9 | `CAMB.PS.REPLACE.DESC` | `CambHPaymentStop_ReplaceDesc` |  |  |  |
| 10 | `CAMB.PS.COMMENTS` | `CambHPaymentStop_Comments` |  |  |  |
| 11 | `CAMB.PS.WAIVE.CHARGE` | `CambHPaymentStop_WaiveCharge` |  |  |  |
| 12 | `CAMB.PS.PS.ID` | `CambHPaymentStop_PsId` |  |  |  |
| 13 | `CAMB.PS.STMT.NOS` | `CambHPaymentStop_StmtNos` |  |  |  |
| 14 | `CAMB.PS.OVERRIDES` | `CambHPaymentStop_Overrides` |  |  |  |
| 15 | `CAMB.PS.RECORD.STATUS` | `CambHPaymentStop_RecordStatus` |  |  |  |
| 16 | `CAMB.PS.CURR.NO` | `CambHPaymentStop_CurrNo` |  |  |  |
| 17 | `CAMB.PS.INPUTTER` | `CambHPaymentStop_Inputter` |  |  |  |
| 18 | `CAMB.PS.DATE.TIME` | `CambHPaymentStop_DateTime` |  |  |  |
| 19 | `CAMB.PS.AUTHORISER` | `CambHPaymentStop_Authoriser` |  |  |  |
| 20 | `CAMB.PS.CO.CODE` | `CambHPaymentStop_CoCode` |  |  |  |
| 21 | `CAMB.PS.DEPT.CODE` | `CambHPaymentStop_DeptCode` |  |  |  |
| 22 | `CAMB.PS.AUDITOR.CODE` | `CambHPaymentStop_AuditorCode` |  |  |  |
| 23 | `CAMB.PS.AUDIT.DATE.TIME` | `CambHPaymentStop_AuditDateTime` |  |  |  |
