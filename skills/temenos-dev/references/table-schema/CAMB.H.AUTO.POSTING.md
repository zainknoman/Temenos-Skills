# CAMB.H.AUTO.POSTING — Table Schema

> Source: `INSERTS/I_F.CAMB.H.AUTO.POSTING` in `CAVLTT_ValueAddedTeller.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.APP.DESCRIPTION` | `CambHAutoPosting_Description` |  |  |  |
| 2 | `CAMB.APP.AC.INWARD.ID` | `CambHAutoPosting_AcInwardId` |  |  |  |
| 3 | `CAMB.APP.REVERSAL.Y.N` | `CambHAutoPosting_ReversalYN` |  |  |  |
| 4 | `CAMB.APP.PAY.Y.N` | `CambHAutoPosting_PayYN` |  |  |  |
| 5 | `CAMB.APP.RSP.Y.N` | `CambHAutoPosting_RspYN` |  |  |  |
| 6 | `CAMB.APP.LEND.OPS.Y.N` | `CambHAutoPosting_LendOpsYN` |  |  |  |
| 7 | `CAMB.APP.PAYMT.OPS.Y.N` | `CambHAutoPosting_PaymtOpsYN` |  |  |  |
| 8 | `CAMB.APP.ATM.OPS.Y.N` | `CambHAutoPosting_AtmOpsYN` |  |  |  |
| 9 | `CAMB.APP.INVMT.OPS.Y.N` | `CambHAutoPosting_InvmtOpsYN` |  |  |  |
| 10 | `CAMB.APP.FIN.OPS.Y.N` | `CambHAutoPosting_FinOpsYN` |  |  |  |
| 11 | `CAMB.APP.FILE.NAME` | `CambHAutoPosting_FileName` |  |  |  |
| 12 | `CAMB.APP.BALANCED.Y.N` | `CambHAutoPosting_BalancedYN` |  |  |  |
| 13 | `CAMB.APP.NO.OF.TXNS` | `CambHAutoPosting_NoOfTxns` |  |  |  |
| 14 | `CAMB.APP.ACCOUNT.NUMBER` | `CambHAutoPosting_AccountNumber` |  |  |  |
| 15 | `CAMB.APP.AMOUNT` | `CambHAutoPosting_Amount` |  |  |  |
| 16 | `CAMB.APP.CURRENCY` | `CambHAutoPosting_Currency` |  |  |  |
| 17 | `CAMB.APP.VAL.DATE` | `CambHAutoPosting_ValDate` |  |  |  |
| 18 | `CAMB.APP.SIGN` | `CambHAutoPosting_Sign` |  |  |  |
| 19 | `CAMB.APP.NARRATIVE` | `CambHAutoPosting_Narrative` |  |  |  |
| 20 | `CAMB.APP.TOTAL.CREDIT` | `CambHAutoPosting_TotalCredit` |  |  |  |
| 21 | `CAMB.APP.TOTAL.DEBIT` | `CambHAutoPosting_TotalDebit` |  |  |  |
| 22 | `CAMB.APP.NET.AMOUNT` | `CambHAutoPosting_NetAmount` |  |  |  |
| 23 | `CAMB.APP.LOCAL.REF` | `CambHAutoPosting_LocalRef` |  |  |  |
| 24 | `CAMB.APP.UPLOADED.FILES` | `CambHAutoPosting_UploadedFiles` |  |  |  |
| 25 | `CAMB.APP.DISPLAY.LOG` | `CambHAutoPosting_DisplayLog` |  |  |  |
| 26 | `CAMB.APP.RESERVED.2` | `CambHAutoPosting_Reserved2` |  |  |  |
| 27 | `CAMB.APP.RESERVED.1` | `CambHAutoPosting_Reserved1` |  |  |  |
| 28 | `CAMB.APP.RECORD.STATUS` | `CambHAutoPosting_RecordStatus` |  |  |  |
| 29 | `CAMB.APP.CURR.NO` | `CambHAutoPosting_CurrNo` |  |  |  |
| 30 | `CAMB.APP.INPUTTER` | `CambHAutoPosting_Inputter` |  |  |  |
| 31 | `CAMB.APP.DATE.TIME` | `CambHAutoPosting_DateTime` |  |  |  |
| 32 | `CAMB.APP.AUTHORISER` | `CambHAutoPosting_Authoriser` |  |  |  |
| 33 | `CAMB.APP.CO.CODE` | `CambHAutoPosting_CoCode` |  |  |  |
| 34 | `CAMB.APP.DEPT.CODE` | `CambHAutoPosting_DeptCode` |  |  |  |
| 35 | `CAMB.APP.AUDITOR.CODE` | `CambHAutoPosting_AuditorCode` |  |  |  |
| 36 | `CAMB.APP.AUDIT.DATE.TIME` | `CambHAutoPosting_AuditDateTime` |  |  |  |
