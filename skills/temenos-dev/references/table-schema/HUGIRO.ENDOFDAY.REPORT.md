# HUGIRO.ENDOFDAY.REPORT — Table Schema

> Source: `INSERTS/I_F.HUGIRO.ENDOFDAY.REPORT` in `HUGIRO_IG2SettlementReports.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HU.EOD.CREATION.DATE.TIME` | `HugiroEndofdayReport_CreationDateTime` |  |  |  |
| 2 | `HU.EOD.SETTLEMENT.DATE` | `HugiroEndofdayReport_SettlementDate` | TField |  | It is the settlement date for which IG2 is sending this report. |
| 3 | `HU.EOD.MESSAGE.SOURCE` | `HugiroEndofdayReport_MessageSource` |  |  |  |
| 4 | `HU.EOD.SESSION.NUMBER` | `HugiroEndofdayReport_SessionNumber` | TField |  | It is the session number for which IG2 is preparing the report. 1 is for the first session, 2 for the second etc. |
| 5 | `HU.EOD.HCT.ACCEPTED.NUMBER` | `HugiroEndofdayReport_HctAcceptedNumber` | TField |  | It is the total number of HCTs accepted during the whole day |
| 6 | `HU.EOD.HCT.ACCEPTED.AMOUNT` | `HugiroEndofdayReport_HctAcceptedAmount` | TField |  | It is the total sum of HCTs accepted during the whole day |
| 7 | `HU.EOD.HCT.REJECTED.NUMBER` | `HugiroEndofdayReport_HctRejectedNumber` | TField |  | It is the total number of HCTs rejected during the whole day |
| 8 | `HU.EOD.HCT.REJECTED.AMOUNT` | `HugiroEndofdayReport_HctRejectedAmount` | TField |  | total sum of HCTs rejected during the whole day |
| 9 | `HU.EOD.HCT.SENTCLEARED.NUMBER` | `HugiroEndofdayReport_HctSentclearedNumber` | TField |  | It is thetotal number of sent, cleared HCTs during the whole day |
| 10 | `HU.EOD.HCT.SENTCLEARED.AMOUNT` | `HugiroEndofdayReport_HctSentclearedAmount` | TField |  | It is the total amount of sent, cleared HCTs during the whole day |
| 11 | `HU.EOD.HCT.RECEIVEDCLEARED.NUMBER` | `HugiroEndofdayReport_HctReceivedclearedNumber` | TField |  | It is the total number of received, cleared HCTs during the whole day |
| 12 | `HU.EOD.HCT.RECEIVEDCLEARED.AMT` | `HugiroEndofdayReport_HctReceivedclearedAmt` | TField |  | It is the total amount of received, cleared HCTs during the whole day |
| 13 | `HU.EOD.CT.DELETED.NUMBER` | `HugiroEndofdayReport_CtDeletedNumber` | TField |  | It is the total number and amount of CTs and RCTs deleted by IG2 |
| 14 | `HU.EOD.CT.DELETED.AMOUNT` | `HugiroEndofdayReport_CtDeletedAmount` | TField |  | It is the total number and amount of CTs and RCTs deleted by IG2 |
| 15 | `HU.EOD.HCT.ROLLEDOVER.NUMBER` | `HugiroEndofdayReport_HctRolledoverNumber` | TField |  | It is the total number of uncovered HCTs rolled over to the next day |
| 16 | `HU.EOD.HCT.ROLLEDOVER.AMOUNT` | `HugiroEndofdayReport_HctRolledoverAmount` | TField |  | It is the total amount of uncovered HCTs rolled over to the next day |
| 17 | `HU.EOD.RECALS.NUMBER` | `HugiroEndofdayReport_RecalsNumber` | TField |  | It is the total number and amount of (executed+forwarded) recalls and NAK�d recalls (camt.029) during the whole day |
| 18 | `HU.EOD.RECALS.AMOUNT` | `HugiroEndofdayReport_RecalsAmount` | TField |  | It is the total number and amount of (executed+forwarded) recalls and NAK�d recalls (camt.029) during the whole day |
| 19 | `HU.EOD.RECALS.EXECUTED.NUMBER` | `HugiroEndofdayReport_RecalsExecutedNumber` | TField |  | It is the total number of recalls executed during the whole day |
| 20 | `HU.EOD.RECALS.CT.TOTALAMOUNT` | `HugiroEndofdayReport_RecalsCtTotalamount` | TField |  | It is the total amount of recalled CTs during the whole day |
| 21 | `HU.EOD.RECALS.FORWARDED.NUMBER` | `HugiroEndofdayReport_RecalsForwardedNumber` | TField |  | It is the total number of recalls (camt.056) and NAK�d recalls (camt.029) forwarded during the whole day |
| 22 | `HU.EOD.RECALS.FORWARDED.AMOUNT` | `HugiroEndofdayReport_RecalsForwardedAmount` | TField |  | It is the total amount of fields Undrlyg/TxInf/OrgnlIntrBkSttlmAmt of forwarded camt.056 recalls during the whole day. |
