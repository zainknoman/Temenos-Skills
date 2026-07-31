# AZ.ACCT.BAL.HIST — Table Schema

> Source: `INSERTS/I_F.AZ.ACCT.BAL.HIST` in `AZ_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AZ.ACCT.HIST.CURRENCY` | `AzAcctBalHist_Currency` | TField |  | Please refer the helptext section of AZ.ACCT.BAl |
| 2 | `AZ.ACCT.HIST.DATE` | `AzAcctBalHist_Date` |  |  |  |
| 3 | `AZ.ACCT.HIST.PRINCIPAL` | `AzAcctBalHist_Principal` |  |  |  |
| 4 | `AZ.ACCT.HIST.INTEREST` | `AzAcctBalHist_Interest` |  |  |  |
| 5 | `AZ.ACCT.HIST.CHARGES` | `AzAcctBalHist_Charges` |  |  |  |
| 6 | `AZ.ACCT.HIST.TYPE.B` | `AzAcctBalHist_TypeB` |  |  |  |
| 7 | `AZ.ACCT.HIST.SUB.ACCT` | `AzAcctBalHist_SubAcct` |  |  |  |
| 8 | `AZ.ACCT.HIST.TYPE.N` | `AzAcctBalHist_TypeN` |  |  |  |
| 9 | `AZ.ACCT.HIST.TYPE.A` | `AzAcctBalHist_TypeA` |  |  |  |
| 10 | `AZ.ACCT.HIST.IRA.AMOUNT` | `AzAcctBalHist_IraAmount` |  |  |  |
| 11 | `AZ.ACCT.HIST.CHG.AMOUNT` | `AzAcctBalHist_ChgAmount` |  |  |  |
| 12 | `AZ.ACCT.HIST.CHG.LIQ.ACCT` | `AzAcctBalHist_ChgLiqAcct` |  |  |  |
| 13 | `AZ.ACCT.HIST.CHG.CODE` | `AzAcctBalHist_ChgCode` |  |  |  |
| 14 | `AZ.ACCT.HIST.INT.ADJ.AMT` | `AzAcctBalHist_IntAdjAmt` |  |  |  |
| 15 | `AZ.ACCT.HIST.RESERVED2` | `AzAcctBalHist_Reserved2` |  |  |  |
| 16 | `AZ.ACCT.HIST.RESERVED1` | `AzAcctBalHist_Reserved1` |  |  |  |
| 17 | `AZ.ACCT.HIST.CONSOL.BAL` | `AzAcctBalHist_ConsolBal` | TField |  | Please refer the helptext section of AZ.ACCT.BAl |
| 18 | `AZ.ACCT.HIST.CURR.HIST.NO` | `AzAcctBalHist_CurrHistNo` | TField |  | Please refer the helptext section of AZ.ACCT.BAl |
| 19 | `AZ.ACCT.HIST.PEN.DATE` | `AzAcctBalHist_PenDate` |  |  |  |
| 20 | `AZ.ACCT.HIST.PEN.CHG.CODE` | `AzAcctBalHist_PenChgCode` |  |  |  |
| 21 | `AZ.ACCT.HIST.PEN.CHG.AMT` | `AzAcctBalHist_PenChgAmt` |  |  |  |
| 22 | `AZ.ACCT.HIST.RESERVED.6` | `AzAcctBalHist_Reserved6` | TField |  |  |
| 23 | `AZ.ACCT.HIST.RESERVED.5` | `AzAcctBalHist_Reserved5` | TField |  | Please refer the helptext section of AZ.ACCT.BAl |
| 24 | `AZ.ACCT.HIST.RESERVED.4` | `AzAcctBalHist_Reserved4` | TField |  | Please refer the helptext section of AZ.ACCT.BAl |
| 25 | `AZ.ACCT.HIST.RESERVED.3` | `AzAcctBalHist_Reserved3` | TField |  | Please refer the helptext section of AZ.ACCT.BAl |
| 26 | `AZ.ACCT.HIST.RESERVED.2` | `AzAcctBalHist_Reserved2` |  |  |  |
| 27 | `AZ.ACCT.HIST.RESERVED.1` | `AzAcctBalHist_Reserved1` |  |  |  |
| 28 | `AZ.ACCT.HIST.NOTES` | `AzAcctBalHist_Notes` | TField |  | Holds the FREE Text to indicate the reason for updating AZ.ACCT.BAL to this history file. Free text can be like 'DEPOSIT ROLLED OVER' etc. |
| 29 | `AZ.ACCT.HIST.RECORD.STATUS` | `AzAcctBalHist_RecordStatus` | String |  |  |
| 30 | `AZ.ACCT.HIST.CURR.NO` | `AzAcctBalHist_CurrNo` | String |  |  |
| 31 | `AZ.ACCT.HIST.INPUTTER` | `AzAcctBalHist_Inputter` |  |  |  |
| 32 | `AZ.ACCT.HIST.DATE.TIME` | `AzAcctBalHist_DateTime` |  |  |  |
| 33 | `AZ.ACCT.HIST.AUTHORISER` | `AzAcctBalHist_Authoriser` | String |  |  |
| 34 | `AZ.ACCT.HIST.CO.CODE` | `AzAcctBalHist_CoCode` | String |  |  |
| 35 | `AZ.ACCT.HIST.DEPT.CODE` | `AzAcctBalHist_DeptCode` | String |  |  |
| 36 | `AZ.ACCT.HIST.AUDITOR.CODE` | `AzAcctBalHist_AuditorCode` | String |  |  |
| 37 | `AZ.ACCT.HIST.AUDIT.DATE.TIME` | `AzAcctBalHist_AuditDateTime` | String |  |  |
