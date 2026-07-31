# NSF.ACCT.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.NSF.ACCT.ACTIVITY` in `NSFDES_Queue.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AcctAct.DAY.NO` | `NsfAcctActivity_DayNo` |  |  |  |
| 2 | `AcctAct.SYSPAY.CNT` | `NsfAcctActivity_SyspayCnt` |  |  |  |
| 3 | `AcctAct.SYSPAY.FEE` | `NsfAcctActivity_SyspayFee` |  |  |  |
| 4 | `AcctAct.SYSPAY.SYSWAIVE.CNT` | `NsfAcctActivity_SyspaySyswaiveCnt` |  |  |  |
| 5 | `AcctAct.SYSPAY.SYSWAIVE.FEE` | `NsfAcctActivity_SyspaySyswaiveFee` |  |  |  |
| 6 | `AcctAct.SYSPAY.USRWAIVE.CNT` | `NsfAcctActivity_SyspayUsrwaiveCnt` |  |  |  |
| 7 | `AcctAct.SYSPAY.USRWAIVE.FEE` | `NsfAcctActivity_SyspayUsrwaiveFee` |  |  |  |
| 8 | `AcctAct.USRPAY.CNT` | `NsfAcctActivity_UsrpayCnt` |  |  |  |
| 9 | `AcctAct.USRPAY.FEE` | `NsfAcctActivity_UsrpayFee` |  |  |  |
| 10 | `AcctAct.USRPAY.SYSWAIVE.CNT` | `NsfAcctActivity_UsrpaySyswaiveCnt` |  |  |  |
| 11 | `AcctAct.USRPAY.SYSWAIVE.FEE` | `NsfAcctActivity_UsrpaySyswaiveFee` |  |  |  |
| 12 | `AcctAct.USRPAY.USRWAIVE.CNT` | `NsfAcctActivity_UsrpayUsrwaiveCnt` |  |  |  |
| 13 | `AcctAct.USRPAY.USRWAIVE.FEE` | `NsfAcctActivity_UsrpayUsrwaiveFee` |  |  |  |
| 14 | `AcctAct.SYSRET.CNT` | `NsfAcctActivity_SysretCnt` |  |  |  |
| 15 | `AcctAct.SYSRET.FEE` | `NsfAcctActivity_SysretFee` |  |  |  |
| 16 | `AcctAct.SYSRET.SYSWAIVE.CNT` | `NsfAcctActivity_SysretSyswaiveCnt` |  |  |  |
| 17 | `AcctAct.SYSRET.SYSWAIVE.FEE` | `NsfAcctActivity_SysretSyswaiveFee` |  |  |  |
| 18 | `AcctAct.SYSRET.USRWAIVE.CNT` | `NsfAcctActivity_SysretUsrwaiveCnt` |  |  |  |
| 19 | `AcctAct.SYSRET.USRWAIVE.FEE` | `NsfAcctActivity_SysretUsrwaiveFee` |  |  |  |
| 20 | `AcctAct.USRRET.CNT` | `NsfAcctActivity_UsrretCnt` |  |  |  |
| 21 | `AcctAct.USRRET.FEE` | `NsfAcctActivity_UsrretFee` |  |  |  |
| 22 | `AcctAct.USRRET.SYSWAIVE.CNT` | `NsfAcctActivity_UsrretSyswaiveCnt` |  |  |  |
| 23 | `AcctAct.USRRET.SYSWAIVE.FEE` | `NsfAcctActivity_UsrretSyswaiveFee` |  |  |  |
| 24 | `AcctAct.USRRET.USRWAIVE.CNT` | `NsfAcctActivity_UsrretUsrwaiveCnt` |  |  |  |
| 25 | `AcctAct.USRRET.USRWAIVE.FEE` | `NsfAcctActivity_UsrretUsrwaiveFee` |  |  |  |
| 26 | `AcctAct.SYSPAYREF.CNT` | `NsfAcctActivity_SyspayrefCnt` |  |  |  |
| 27 | `AcctAct.SYSPAYREF.FEE` | `NsfAcctActivity_SyspayrefFee` |  |  |  |
| 28 | `AcctAct.SYSRETREF.CNT` | `NsfAcctActivity_SysretrefCnt` |  |  |  |
| 29 | `AcctAct.SYSRETREF.FEE` | `NsfAcctActivity_SysretrefFee` |  |  |  |
| 30 | `AcctAct.USRPAYREF.CNT` | `NsfAcctActivity_UsrpayrefCnt` |  |  |  |
| 31 | `AcctAct.USRPAYREF.FEE` | `NsfAcctActivity_UsrpayrefFee` |  |  |  |
| 32 | `AcctAct.USRRETREF.CNT` | `NsfAcctActivity_UsrretrefCnt` |  |  |  |
| 33 | `AcctAct.USRRETREF.FEE` | `NsfAcctActivity_UsrretrefFee` |  |  |  |
| 34 | `AcctAct.RETURN.CODE` | `NsfAcctActivity_ReturnCode` |  |  |  |
| 35 | `AcctAct.RETURN.COUNT` | `NsfAcctActivity_ReturnCount` |  |  |  |
| 36 | `AcctAct.OD.COUNT` | `NsfAcctActivity_OdCount` |  |  |  |
