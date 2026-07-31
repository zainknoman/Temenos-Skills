# MD.INVOCATION.HIST — Table Schema

> Source: `INSERTS/I_F.MD.INVOCATION.HIST` in `MD_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MD.INV.INV.STATUS` | `MdInvocationHist_InvStatus` |  |  |  |
| 2 | `MD.INV.AMOUNT` | `MdInvocationHist_Amount` |  |  |  |
| 3 | `MD.INV.DR.ACCOUNT` | `MdInvocationHist_DrAccount` |  |  |  |
| 4 | `MD.INV.DR.VALUE.DATE` | `MdInvocationHist_DrValueDate` |  |  |  |
| 5 | `MD.INV.SETTLE.ACCOUNT` | `MdInvocationHist_SettleAccount` |  |  |  |
| 6 | `MD.INV.EXCH.RATE` | `MdInvocationHist_ExchRate` |  |  |  |
| 7 | `MD.INV.PAY.VALUE.DATE` | `MdInvocationHist_PayValueDate` |  |  |  |
| 8 | `MD.INV.BNK.OP.CODE` | `MdInvocationHist_BnkOpCode` |  |  |  |
| 9 | `MD.INV.OUR.COR.BNK` | `MdInvocationHist_OurCorBnk` |  |  |  |
| 10 | `MD.INV.RE.COR.BNK` | `MdInvocationHist_ReCorBnk` |  |  |  |
| 11 | `MD.INV.INT.BNK` | `MdInvocationHist_IntBnk` |  |  |  |
| 12 | `MD.INV.AC.WITH.BNK` | `MdInvocationHist_AcWithBnk` |  |  |  |
| 13 | `MD.INV.REC.BNK` | `MdInvocationHist_RecBnk` |  |  |  |
| 14 | `MD.INV.BENEFICIARY` | `MdInvocationHist_Beneficiary` |  |  |  |
| 15 | `MD.INV.CHRG.DET` | `MdInvocationHist_ChrgDet` |  |  |  |
| 16 | `MD.INV.DEMAND.TYPE` | `MdInvocationHist_DemandType` |  |  |  |
| 17 | `MD.INV.REQ.NEW.EXPIRY.DATE` | `MdInvocationHist_ReqNewExpiryDate` |  |  |  |
| 18 | `MD.INV.REASON.FOR.REFUSAL` | `MdInvocationHist_ReasonForRefusal` |  |  |  |
| 19 | `MD.INV.DISP.OF.DOCS` | `MdInvocationHist_DispOfDocs` |  |  |  |
| 20 | `MD.INV.MT786.SEND.RECV.INFO` | `MdInvocationHist_MtSevEigSixSendRecvInfo` |  |  |  |
| 21 | `MD.INV.MT765.ADDL.AMT.INFO` | `MdInvocationHist_MtSevSixFivAddlAmtInfo` |  |  |  |
| 22 | `MD.INV.DEMAND.STMT.CODE` | `MdInvocationHist_DemandStmtCode` |  |  |  |
| 23 | `MD.INV.DEMAND.STMT.NARR` | `MdInvocationHist_DemandStmtNarr` |  |  |  |
| 24 | `MD.INV.PRESENT.COMP.DETS` | `MdInvocationHist_PresentCompDets` |  |  |  |
| 25 | `MD.INV.INV.REGISTER.DATE` | `MdInvocationHist_InvRegisterDate` |  |  |  |
| 26 | `MD.INV.MT765.SEND.RECV.INFO` | `MdInvocationHist_MtSevSixFivSendRecvInfo` |  |  |  |
| 27 | `MD.INV.PRESENTATION.FOR.CLAIM` | `MdInvocationHist_PresentationForClaim` |  |  |  |
| 28 | `MD.INV.MKT.EXCG.PROFIT` | `MdInvocationHist_MktExcgProfit` |  |  |  |
| 29 | `MD.INV.LOC.NEW.EXP.DT` | `MdInvocationHist_LocNewExpDt` |  |  |  |
