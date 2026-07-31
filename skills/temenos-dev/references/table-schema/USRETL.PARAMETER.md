# USRETL.PARAMETER — Table Schema

> Source: `INSERTS/I_F.USRETL.PARAMETER` in `USRETL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USRETL.PARAM.HANDLING.METHOD` | `UsretlParameter_HandlingMethod` | TField |  | This field is used to define the positive pay handling ways whether it is a Direct handling or Third party handling. Positive Pay handling method can have values DIRECT or INDIRECT Rule: Field length - 8 Character type AAA. |
| 2 | `USRETL.PARAM.POSPAY.CUTOFF` | `UsretlParameter_PospayCutoff` | TField |  |  |
| 3 | `USRETL.PARAM.RESERVED.4` | `UsretlParameter_Reserved4` |  |  |  |
| 4 | `USRETL.PARAM.STATEMENT.PATH` | `UsretlParameter_StatementPath` | TField |  | This field holds the path where combined statements are generated. |
| 5 | `USRETL.PARAM.ACC.INT.PROP` | `UsretlParameter_AccIntProp` |  |  |  |
| 6 | `USRETL.PARAM.ACC.INTTAX.PROP` | `UsretlParameter_AccInttaxProp` |  |  |  |
| 7 | `USRETL.PARAM.DEP.INT.PROP` | `UsretlParameter_DepIntProp` |  |  |  |
| 8 | `USRETL.PARAM.DEP.INTTAX.PROP` | `UsretlParameter_DepInttaxProp` |  |  |  |
| 9 | `USRETL.PARAM.ACC.PERDIEM.PROP` | `UsretlParameter_AccPerdiemProp` |  |  |  |
| 10 | `USRETL.PARAM.DEP.PERDIEM.PROP` | `UsretlParameter_DepPerdiemProp` |  |  |  |
| 11 | `USRETL.PARAM.DEP.CHECK.ACCOUNT` | `UsretlParameter_DepCheckAccount` | TField |  | To parametrize suspense account used for pay by check option provided in deposit settlement instructions. This suspense account will be used as a PAY.OUT account if user chooses PAY.BY.CHECK option. |
| 12 | `USRETL.PARAM.ESCHEAT.PATH` | `UsretlParameter_EscheatPath` | TField |  |  |
| 13 | `USRETL.PARAM.DORMANT.PATH` | `UsretlParameter_DormantPath` | TField |  |  |
| 14 | `USRETL.PARAM.LOAN.CHECK.ACCOUNT` | `UsretlParameter_LoanCheckAccount` | TField |  |  |
| 15 | `USRETL.PARAM.ATTRIBUTES` | `UsretlParameter_Attributes` |  |  |  |
| 16 | `USRETL.PARAM.AC.THRESHOLD.OFFSET.ACCT` | `UsretlParameter_AcThresholdOffsetAcct` | TField |  |  |
| 17 | `USRETL.PARAM.RESERVED.2` | `UsretlParameter_Reserved2` |  |  |  |
| 18 | `USRETL.PARAM.RESERVED.1` | `UsretlParameter_Reserved1` |  |  |  |
| 19 | `USRETL.PARAM.RECORD.STATUS` | `UsretlParameter_RecordStatus` | String |  |  |
| 20 | `USRETL.PARAM.CURR.NO` | `UsretlParameter_CurrNo` | String |  |  |
| 21 | `USRETL.PARAM.INPUTTER` | `UsretlParameter_Inputter` |  |  |  |
| 22 | `USRETL.PARAM.DATE.TIME` | `UsretlParameter_DateTime` |  |  |  |
| 23 | `USRETL.PARAM.AUTHORISER` | `UsretlParameter_Authoriser` | String |  |  |
| 24 | `USRETL.PARAM.CO.CODE` | `UsretlParameter_CoCode` | String |  |  |
| 25 | `USRETL.PARAM.DEPT.CODE` | `UsretlParameter_DeptCode` | String |  |  |
| 26 | `USRETL.PARAM.AUDITOR.CODE` | `UsretlParameter_AuditorCode` | String |  |  |
| 27 | `USRETL.PARAM.AUDIT.DATE.TIME` | `UsretlParameter_AuditDateTime` | String |  |  |
| 28 | `USRETL.PARAM.AC.CLOSE.POST.REST` | `UsretlParameter_AcClosePostRest` | TField |  | Restriction to be used on account during the pre-closure account process. |
| 29 | `USRETL.PARAM.AC.CLOSE.THRESHOLD.BAL` | `UsretlParameter_AcCloseThresholdBal` | TField |  | Balance to control the threshold for ChexSystems reporting / RMS extract during the Auto closure process. |
| 30 | `USRETL.PARAM.AC.CLOSE.CUS.STATUS` | `UsretlParameter_AcCloseCusStatus` | TField |  | Status that the Customer of the account will have at the end of the Auto-Closure process. |
| 31 | `USRETL.PARAM.NSF.OFFSET.ACCT` | `UsretlParameter_NsfOffsetAcct` | TField |  | Account Class to place the NSF/OD fees waived during the Auto closure process. The account class must contain only one category; if more than one category available then system will consider first category. |
| 32 | `USRETL.PARAM.CHGOFF.OFFSET.ACCT` | `UsretlParameter_ChgoffOffsetAcct` | TField |  | Account Class to place the Charge Off amount Calculated during the Auto Closure process. The account class must contain only one category; if more than one category available then system will consider first category. |
| 33 | `USRETL.PARAM.AC.CLOSE.STATUS` | `UsretlParameter_AcCloseStatus` | TField |  | Final status of the account after the Auto-Close Process. |
| 34 | `USRETL.PARAM.AC.CLOSE.MAX.ATTEMPTS` | `UsretlParameter_AcCloseMaxAttempts` | TField |  | Maximum number of attempts allowed for Auto-Close Process. |
| 35 | `USRETL.PARAM.DEP.PAYOUT.ACTIVITY` | `UsretlParameter_DepPayoutActivity` | TField |  |  |
