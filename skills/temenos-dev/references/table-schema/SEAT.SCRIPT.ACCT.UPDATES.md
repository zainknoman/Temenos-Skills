# SEAT.SCRIPT.ACCT.UPDATES — Table Schema

> Source: `INSERTS/I_F.SEAT.SCRIPT.ACCT.UPDATES` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.SAU.DESCRIPT` | `SeatScriptAcctUpdates_Descript` |  |  |  |
| 2 | `EB.SAU.APPLICATION` | `SeatScriptAcctUpdates_Application` |  |  |  |
| 3 | `EB.SAU.TRANSACTION.ID` | `SeatScriptAcctUpdates_TransactionId` |  |  |  |
| 4 | `EB.SAU.ENTRY.TYPE` | `SeatScriptAcctUpdates_EntryType` |  |  |  |
| 5 | `EB.SAU.ENTRY.TARGET` | `SeatScriptAcctUpdates_EntryTarget` |  |  |  |
| 6 | `EB.SAU.ENTRY.CCY` | `SeatScriptAcctUpdates_EntryCcy` |  |  |  |
| 7 | `EB.SAU.ENTRY.LCY.AMT` | `SeatScriptAcctUpdates_EntryLcyAmt` |  |  |  |
| 8 | `EB.SAU.ENTRY.FCY.AMT` | `SeatScriptAcctUpdates_EntryFcyAmt` |  |  |  |
| 9 | `EB.SAU.ENTRY.TXN.CODE` | `SeatScriptAcctUpdates_EntryTxnCode` |  |  |  |
| 10 | `EB.SAU.ENTRY.COMPANY` | `SeatScriptAcctUpdates_EntryCompany` |  |  |  |
| 11 | `EB.SAU.ENTRY.VAL.DATE` | `SeatScriptAcctUpdates_EntryValDate` |  |  |  |
| 12 | `EB.SAU.TYPE.SYSDATE` | `SeatScriptAcctUpdates_TypeSysdate` |  |  |  |
| 13 | `EB.SAU.MAT.DATE` | `SeatScriptAcctUpdates_MatDate` |  |  |  |
| 14 | `EB.SAU.OPEN.BALANCE` | `SeatScriptAcctUpdates_OpenBalance` |  |  |  |
| 15 | `EB.SAU.OPEN.BAL.LCL` | `SeatScriptAcctUpdates_OpenBalLcl` |  |  |  |
| 16 | `EB.SAU.CREDIT.MVMT` | `SeatScriptAcctUpdates_CreditMvmt` |  |  |  |
| 17 | `EB.SAU.CR.MVMT.LCL` | `SeatScriptAcctUpdates_CrMvmtLcl` |  |  |  |
| 18 | `EB.SAU.DEBIT.MVMT` | `SeatScriptAcctUpdates_DebitMvmt` |  |  |  |
| 19 | `EB.SAU.DB.MVMT.LCL` | `SeatScriptAcctUpdates_DbMvmtLcl` |  |  |  |
| 20 | `EB.SAU.CURR.ASSET.TYPE` | `SeatScriptAcctUpdates_CurrAssetType` |  |  |  |
| 21 | `EB.SAU.POSS.SIGN.CHANGE` | `SeatScriptAcctUpdates_PossSignChange` |  |  |  |
| 22 | `EB.SAU.RESULT` | `SeatScriptAcctUpdates_Result` |  |  |  |
| 23 | `EB.SAU.RESERVED.8` | `SeatScriptAcctUpdates_Reserved8` |  |  |  |
| 24 | `EB.SAU.RESERVED.7` | `SeatScriptAcctUpdates_Reserved7` |  |  |  |
| 25 | `EB.SAU.RESERVED.6` | `SeatScriptAcctUpdates_Reserved6` |  |  |  |
| 26 | `EB.SAU.RESERVED.5` | `SeatScriptAcctUpdates_Reserved5` |  |  |  |
| 27 | `EB.SAU.RESERVED.4` | `SeatScriptAcctUpdates_Reserved4` |  |  |  |
| 28 | `EB.SAU.RESERVED.3` | `SeatScriptAcctUpdates_Reserved3` |  |  |  |
| 29 | `EB.SAU.RESERVED.2` | `SeatScriptAcctUpdates_Reserved2` |  |  |  |
| 30 | `EB.SAU.RESERVED.1` | `SeatScriptAcctUpdates_Reserved1` |  |  |  |
| 31 | `EB.SAU.LOCAL.REF` | `SeatScriptAcctUpdates_LocalRef` |  |  |  |
| 32 | `EB.SAU.OVERRIDE` | `SeatScriptAcctUpdates_Override` |  |  |  |
| 33 | `EB.SAU.RECORD.STATUS` | `SeatScriptAcctUpdates_RecordStatus` |  |  |  |
| 34 | `EB.SAU.CURR.NO` | `SeatScriptAcctUpdates_CurrNo` |  |  |  |
| 35 | `EB.SAU.INPUTTER` | `SeatScriptAcctUpdates_Inputter` |  |  |  |
| 36 | `EB.SAU.DATE.TIME` | `SeatScriptAcctUpdates_DateTime` |  |  |  |
| 37 | `EB.SAU.AUTHORISER` | `SeatScriptAcctUpdates_Authoriser` |  |  |  |
| 38 | `EB.SAU.CO.CODE` | `SeatScriptAcctUpdates_CoCode` |  |  |  |
| 39 | `EB.SAU.DEPT.CODE` | `SeatScriptAcctUpdates_DeptCode` |  |  |  |
| 40 | `EB.SAU.AUDITOR.CODE` | `SeatScriptAcctUpdates_AuditorCode` |  |  |  |
| 41 | `EB.SAU.AUDIT.DATE.TIME` | `SeatScriptAcctUpdates_AuditDateTime` |  |  |  |
