# CAMB.TELPAY.KEY.LOG — Table Schema

> Source: `INSERTS/I_F.CAMB.TELPAY.KEY.LOG` in `CAIVRB_Telpay.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.TP.LOG.CHANNEL` | `CambTelpayKeyLog_Channel` |  |  |  |
| 2 | `CAMB.TP.LOG.ACTION.TYPE` | `CambTelpayKeyLog_ActionType` |  |  |  |
| 3 | `CAMB.TP.LOG.MEMBER.NO` | `CambTelpayKeyLog_MemberNo` |  |  |  |
| 4 | `CAMB.TP.LOG.DATE` | `CambTelpayKeyLog_Date` |  |  |  |
| 5 | `CAMB.TP.LOG.TIME` | `CambTelpayKeyLog_Time` |  |  |  |
| 6 | `CAMB.TP.LOG.TXN.TYPE` | `CambTelpayKeyLog_TxnType` |  |  |  |
| 7 | `CAMB.TP.LOG.TXN.ID` | `CambTelpayKeyLog_TxnId` |  |  |  |
| 8 | `CAMB.TP.LOG.TXN.AMOUNT` | `CambTelpayKeyLog_TxnAmount` |  |  |  |
| 9 | `CAMB.TP.LOG.STATUS` | `CambTelpayKeyLog_Status` |  |  |  |
| 10 | `CAMB.TP.LOG.ERR.CODE` | `CambTelpayKeyLog_ErrCode` |  |  |  |
| 11 | `CAMB.TP.LOG.ERR.MSG` | `CambTelpayKeyLog_ErrMsg` |  |  |  |
| 12 | `CAMB.TP.LOG.TRACE.NO` | `CambTelpayKeyLog_TraceNo` |  |  |  |
