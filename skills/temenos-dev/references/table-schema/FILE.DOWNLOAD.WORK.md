# FILE.DOWNLOAD.WORK — Table Schema

> Source: `INSERTS/I_F.FILE.DOWNLOAD.WORK` in `CACLRC_ClearingCentralOne.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FDW.DESCRIPTION` | `FileDownloadWork_Description` |  |  |  |
| 2 | `FDW.CREATION.NO` | `FileDownloadWork_CreationNo` |  |  |  |
| 3 | `FDW.CREATION.DTIME` | `FileDownloadWork_CreationDtime` |  |  |  |
| 4 | `FDW.NO.DR.TXN` | `FileDownloadWork_NoDrTxn` |  |  |  |
| 5 | `FDW.TOT.DR.AMT` | `FileDownloadWork_TotDrAmt` |  |  |  |
| 6 | `FDW.NO.CR.TXN` | `FileDownloadWork_NoCrTxn` |  |  |  |
| 7 | `FDW.TOT.CR.AMT` | `FileDownloadWork_TotCrAmt` |  |  |  |
| 8 | `FDW.INTR.BNK.STTL.DT` | `FileDownloadWork_IntrBnkSttlDt` |  |  |  |
| 9 | `FDW.STTL.METHOD` | `FileDownloadWork_SttlMethod` |  |  |  |
| 10 | `FDW.RECORD.ID` | `FileDownloadWork_RecordId` |  |  |  |
| 11 | `FDW.TRACE.NO` | `FileDownloadWork_TraceNo` |  |  |  |
| 12 | `FDW.SERIAL.NO` | `FileDownloadWork_SerialNo` |  |  |  |
| 13 | `FDW.REDEPOSIT.STAT` | `FileDownloadWork_RedepositStat` |  |  |  |
| 14 | `FDW.ANCILLARY.FLAG` | `FileDownloadWork_AncillaryFlag` |  |  |  |
| 15 | `FDW.INTR.BNK.STTL.AMT` | `FileDownloadWork_IntrBnkSttlAmt` |  |  |  |
| 16 | `FDW.ADJUSTMENT.DT` | `FileDownloadWork_AdjustmentDt` |  |  |  |
| 17 | `FDW.AMOUNT` | `FileDownloadWork_Amount` |  |  |  |
| 18 | `FDW.CURRENCY` | `FileDownloadWork_Currency` |  |  |  |
| 19 | `FDW.CRG.BEARER` | `FileDownloadWork_CrgBearer` |  |  |  |
| 20 | `FDW.CRG.BACK.CODE` | `FileDownloadWork_CrgBackCode` |  |  |  |
| 21 | `FDW.CXLID` | `FileDownloadWork_Cxlid` |  |  |  |
| 22 | `FDW.ORG.TRACE.NO` | `FileDownloadWork_OrgTraceNo` |  |  |  |
| 23 | `FDW.ORG.MSG.NAME` | `FileDownloadWork_OrgMsgName` |  |  |  |
| 24 | `FDW.ORG.TXN.ID` | `FileDownloadWork_OrgTxnId` |  |  |  |
| 25 | `FDW.ORG.CAP.DATE` | `FileDownloadWork_OrgCapDate` |  |  |  |
| 26 | `FDW.ORG.INST.ID` | `FileDownloadWork_OrgInstId` |  |  |  |
| 27 | `FDW.BK.PTY.ID` | `FileDownloadWork_BkPtyId` |  |  |  |
| 28 | `FDW.NM` | `FileDownloadWork_Nm` |  |  |  |
| 29 | `FDW.RTR.ID` | `FileDownloadWork_RtrId` |  |  |  |
| 30 | `FDW.RVSL.ID` | `FileDownloadWork_RvslId` |  |  |  |
| 31 | `FDW.CREDITOR` | `FileDownloadWork_Creditor` |  |  |  |
| 32 | `FDW.CREDITOR.AGENT` | `FileDownloadWork_CreditorAgent` |  |  |  |
| 33 | `FDW.CREDIT.REF` | `FileDownloadWork_CreditRef` |  |  |  |
| 34 | `FDW.DEBITOR` | `FileDownloadWork_Debitor` |  |  |  |
| 35 | `FDW.ACCOUNT.NO` | `FileDownloadWork_AccountNo` |  |  |  |
| 36 | `FDW.CHARTER.BRANCH` | `FileDownloadWork_CharterBranch` |  |  |  |
| 37 | `FDW.CLEARING.TRANS.CODE` | `FileDownloadWork_ClearingTransCode` |  |  |  |
| 38 | `FDW.CRG.BACK.REASON.CD.1` | `FileDownloadWork_CrgBackReasonCd1` |  |  |  |
| 39 | `FDW.CRG.BACK.REASON.CD.2` | `FileDownloadWork_CrgBackReasonCd2` |  |  |  |
| 40 | `FDW.REQ.COLLT.DT` | `FileDownloadWork_ReqColltDt` |  |  |  |
| 41 | `FDW.COMMENTS` | `FileDownloadWork_Comments` |  |  |  |
| 42 | `FDW.IQA.FLAG` | `FileDownloadWork_IqaFlag` |  |  |  |
| 43 | `FDW.MICR.FLAG` | `FileDownloadWork_MicrFlag` |  |  |  |
| 44 | `FDW.STRD.TXN.TYPE` | `FileDownloadWork_StrdTxnType` |  |  |  |
| 45 | `FDW.ORG.MSG.ID` | `FileDownloadWork_OrgMsgId` |  |  |  |
| 46 | `FDW.ORG.MSG.FMT` | `FileDownloadWork_OrgMsgFmt` |  |  |  |
| 47 | `FDW.ORG.LONG.NM` | `FileDownloadWork_OrgLongNm` |  |  |  |
| 48 | `FDW.ORG.SHORT.NM` | `FileDownloadWork_OrgShortNm` |  |  |  |
| 49 | `FDW.ORG.DRCL.UID` | `FileDownloadWork_OrgDrclUid` |  |  |  |
| 50 | `FDW.INS.AC.RET` | `FileDownloadWork_InsAcRet` |  |  |  |
| 51 | `FDW.INS.ID.RET` | `FileDownloadWork_InsIdRet` |  |  |  |
| 52 | `FDW.RET.REF.NO` | `FileDownloadWork_RetRefNo` |  |  |  |
| 53 | `FDW.PAYEE.NAME` | `FileDownloadWork_PayeeName` |  |  |  |
| 54 | `FDW.PAYOR.NAME` | `FileDownloadWork_PayorName` |  |  |  |
| 55 | `FDW.UPDATE.FLAG` | `FileDownloadWork_UpdateFlag` |  |  |  |
| 56 | `FDW.TXN.CNT.ERR` | `FileDownloadWork_TxnCntErr` |  |  |  |
| 57 | `FDW.RESERVED.9` | `FileDownloadWork_Reserved9` |  |  |  |
| 58 | `FDW.RESERVED.8` | `FileDownloadWork_Reserved8` |  |  |  |
| 59 | `FDW.RESERVED.7` | `FileDownloadWork_Reserved7` |  |  |  |
| 60 | `FDW.RESERVED.6` | `FileDownloadWork_Reserved6` |  |  |  |
| 61 | `FDW.RESERVED.5` | `FileDownloadWork_Reserved5` |  |  |  |
| 62 | `FDW.RESERVED.4` | `FileDownloadWork_Reserved4` |  |  |  |
| 63 | `FDW.RESERVED.3` | `FileDownloadWork_Reserved3` |  |  |  |
| 64 | `FDW.RESERVED.2` | `FileDownloadWork_Reserved2` |  |  |  |
| 65 | `FDW.RESERVED.1` | `FileDownloadWork_Reserved1` |  |  |  |
| 66 | `FDW.LOCAL.REF` | `FileDownloadWork_LocalRef` |  |  |  |
| 67 | `FDW.OVERRIDE` | `FileDownloadWork_Override` |  |  |  |
| 68 | `FDW.RECORD.STATUS` | `FileDownloadWork_RecordStatus` |  |  |  |
| 69 | `FDW.CURR.NO` | `FileDownloadWork_CurrNo` |  |  |  |
| 70 | `FDW.INPUTTER` | `FileDownloadWork_Inputter` |  |  |  |
| 71 | `FDW.DATE.TIME` | `FileDownloadWork_DateTime` |  |  |  |
| 72 | `FDW.AUTHORISER` | `FileDownloadWork_Authoriser` |  |  |  |
| 73 | `FDW.CO.CODE` | `FileDownloadWork_CoCode` |  |  |  |
| 74 | `FDW.DEPT.CODE` | `FileDownloadWork_DeptCode` |  |  |  |
| 75 | `FDW.AUDITOR.CODE` | `FileDownloadWork_AuditorCode` |  |  |  |
| 76 | `FDW.AUDIT.DATE.TIME` | `FileDownloadWork_AuditDateTime` |  |  |  |
