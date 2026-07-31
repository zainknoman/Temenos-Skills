# HUGIRO.ENDOFSESSION.REPORT — Table Schema

> Source: `INSERTS/I_F.HUGIRO.ENDOFSESSION.REPORT` in `HUGIRO_IG2SettlementReports.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HU.EOS.CREATION.DATE.TIME` | `HugiroEndofsessionReport_CreationDateTime` |  |  |  |
| 2 | `HU.EOS.SETTLEMENT.DATE` | `HugiroEndofsessionReport_SettlementDate` | TField |  | It is the settlement date for which IG2 is sending this report. |
| 3 | `HU.EOS.MESSAGE.SOURCE` | `HugiroEndofsessionReport_MessageSource` |  |  |  |
| 4 | `HU.EOS.SESSION.NUMBER` | `HugiroEndofsessionReport_SessionNumber` | TField |  | It is the session number for which IG2 is preparing the report. 1 is for the first session, 2 for the second etc. |
| 5 | `HU.EOS.SESSION.ID` | `HugiroEndofsessionReport_SessionId` | TField |  | It is the session ID |
| 6 | `HU.EOS.RECEIVED.BIC` | `HugiroEndofsessionReport_ReceivedBic` | TField |  | It is the SWIFT BIC of the direct clearing member that receives this report. |
| 7 | `HU.EOS.RECEIVED.BANK.CODE` | `HugiroEndofsessionReport_ReceivedBankCode` | TField |  | It is the bank code of the direct clearing member that receives this report. |
| 8 | `HU.EOS.SENT.ACCEPT.NO` | `HugiroEndofsessionReport_SentAcceptNo` | TField |  | It is the total number of HCTs sent and accepted (CTs, RCTs, RFCs, RAKs, RNKs) |
| 9 | `HU.EOS.SENT.ACCEPT.AMT` | `HugiroEndofsessionReport_SentAcceptAmt` | TField |  | It is the total sum of HCTs accepted (CTs, RCTs, RAKs) |
| 10 | `HU.EOS.SENT.REJECT.ERRCODE` | `HugiroEndofsessionReport_SentRejectErrcode` | TField |  | It is the error code of sent and rejected HCTs |
| 11 | `HU.EOS.SENT.REJECT.NO` | `HugiroEndofsessionReport_SentRejectNo` | TField |  | It is the total number of HCTs sent and rejected by |
| 12 | `HU.EOS.ERROR.CODE` | `HugiroEndofsessionReport_ErrorCode` | TField |  | It is the the error code for above |
| 13 | `HU.EOS.SENT.REJECT.AMT` | `HugiroEndofsessionReport_SentRejectAmt` | TField |  | It is the total sum of HCTs rejected by the error code above |
| 14 | `HU.EOS.SESSION.REJECT.NO` | `HugiroEndofsessionReport_SessionRejectNo` | TField |  | It is the number of all HCTs rejected in the session |
| 15 | `HU.EOS.SESSION.REJECT.AMT` | `HugiroEndofsessionReport_SessionRejectAmt` | TField |  | It is the sum of all HCTs rejected in the session |
| 16 | `HU.EOS.SESSION.SENT.NO` | `HugiroEndofsessionReport_SessionSentNo` | TField |  | It is the number of all HCTs sent in this session |
| 17 | `HU.EOS.SESSION.SENT.AMT` | `HugiroEndofsessionReport_SessionSentAmt` | TField |  | It is the amount of all HCTs sent in this session |
| 18 | `HU.EOS.HCT.TO.CLEAR.NO` | `HugiroEndofsessionReport_HctToClearNo` | TField |  | It is the number of HCTs planned to be cleared |
| 19 | `HU.EOS.HCT.TO.CLEAR.AMT` | `HugiroEndofsessionReport_HctToClearAmt` | TField |  | It is the sum of HCTs planned to be cleared |
| 20 | `HU.EOS.OPENING.BALANCE` | `HugiroEndofsessionReport_OpeningBalance` | TField |  | It is the DP�s opening balance (?0) |
| 21 | `HU.EOS.CLOSING.BALANCE` | `HugiroEndofsessionReport_ClosingBalance` | TField |  | It is the DP�s closing balance (? 0) |
| 22 | `HU.EOS.HCT.SENT.CLEAR.NO` | `HugiroEndofsessionReport_HctSentClearNo` | TField |  | It is the number of sent, cleared HCTs |
| 23 | `HU.EOS.HCT.SENT.CLEAR.AMT` | `HugiroEndofsessionReport_HctSentClearAmt` | TField |  | It is the amount of received, cleared HCTs |
| 24 | `HU.EOS.HCT.RCV.CLEAR.NO` | `HugiroEndofsessionReport_HctRcvClearNo` | TField |  | It is the number of received, cleared HCTs |
| 25 | `HU.EOS.HCT.RCV.CLEAR.AMT` | `HugiroEndofsessionReport_HctRcvClearAmt` | TField |  | It is the amount of received, cleared HCTs |
| 26 | `HU.EOS.HCT.RLDOVR.NXTSSN.NO` | `HugiroEndofsessionReport_HctRldovrNxtssnNo` | TField |  | It is the number of HCTs rolled over to next session |
| 27 | `HU.EOS.HCT.RLDOVR.NXTSSN.AMT` | `HugiroEndofsessionReport_HctRldovrNxtssnAmt` | TField |  | It is the amount of HCTs rolled over to next session |
| 28 | `HU.EOS.DELETE.CT.NO` | `HugiroEndofsessionReport_DeleteCtNo` | TField |  | It is the number of deleted CTs and RCTs |
| 29 | `HU.EOS.DELETE.CT.AMT` | `HugiroEndofsessionReport_DeleteCtAmt` | TField |  | It is the amount of deleted CTs and RCT |
| 30 | `HU.EOS.CT.RLDOVR.NXTDAY.NO` | `HugiroEndofsessionReport_CtRldovrNxtdayNo` | TField |  | It is the number of uncovered CTs and RCTs rolled over to the next day |
| 31 | `HU.EOS.CT.RLDOVR.NXTDAY.AMT` | `HugiroEndofsessionReport_CtRldovrNxtdayAmt` | TField |  | It is the amount of uncovered CTs and RCTs rolled over to the next day |
| 32 | `HU.EOS.NET.POS.PLANNED` | `HugiroEndofsessionReport_NetPosPlanned` | TField |  | It is the sum of HCTs planned to receive |
| 33 | `HU.EOS.NET.POS.ACTUAL` | `HugiroEndofsessionReport_NetPosActual` | TField |  | It is the sum of HCTs received (ClrdRcvdAmt) � (minus) sum of sent HCTs cleared (ClrdSntAmt) |
| 34 | `HU.EOS.RECALL.HCT.NO` | `HugiroEndofsessionReport_RecallHctNo` | TField |  | It is the number of recalling / recalled HCTs |
| 35 | `HU.EOS.RECALL.HCT.AMT` | `HugiroEndofsessionReport_RecallHctAmt` | TField |  | It is the amount of recalling / recalled HCTs |
| 36 | `HU.EOS.RECALL.HCT.EXC.NO` | `HugiroEndofsessionReport_RecallHctExcNo` | TField |  | It is the number of recalling HCTs executed |
| 37 | `HU.EOS.RECALL.HCT.EXC.AMT` | `HugiroEndofsessionReport_RecallHctExcAmt` | TField |  | It is the amount of recalling HCTs executed |
| 38 | `HU.EOS.RECALL.HCT.FWD.NO` | `HugiroEndofsessionReport_RecallHctFwdNo` | TField |  | It is the number of recalling HCTs forwarded |
| 39 | `HU.EOS.RECALL.HCT.FWD.AMT` | `HugiroEndofsessionReport_RecallHctFwdAmt` | TField |  | It is the amount of recalling HCTs forwarded |
