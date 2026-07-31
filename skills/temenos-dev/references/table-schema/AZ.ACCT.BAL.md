# AZ.ACCT.BAL — Table Schema

> Source: `INSERTS/I_F.AZ.ACCT.BAL` in `AZ_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AZ.ACCT.CURRENCY` | `AzAcctBal_Currency` | TField |  | This field holds the currency of the AZ account for which this record is created. |
| 2 | `AZ.ACCT.DATE` | `AzAcctBal_Date` |  |  |  |
| 3 | `AZ.ACCT.PRINCIPAL` | `AzAcctBal_Principal` |  |  |  |
| 4 | `AZ.ACCT.INTEREST` | `AzAcctBal_Interest` |  |  |  |
| 5 | `AZ.ACCT.CHARGES` | `AzAcctBal_Charges` |  |  |  |
| 6 | `AZ.ACCT.TYPE.B` | `AzAcctBal_TypeB` |  |  |  |
| 7 | `AZ.ACCT.SUB.ACCT` | `AzAcctBal_SubAcct` |  |  |  |
| 8 | `AZ.ACCT.TYPE.N` | `AzAcctBal_TypeN` |  |  |  |
| 9 | `AZ.ACCT.TYPE.A` | `AzAcctBal_TypeA` |  |  |  |
| 10 | `AZ.ACCT.IRA.AMOUNT` | `AzAcctBal_IraAmount` |  |  |  |
| 11 | `AZ.ACCT.CHG.AMOUNT` | `AzAcctBal_ChgAmount` |  |  |  |
| 12 | `AZ.ACCT.CHG.LIQ.ACCT` | `AzAcctBal_ChgLiqAcct` |  |  |  |
| 13 | `AZ.ACCT.CHG.CODE` | `AzAcctBal_ChgCode` |  |  |  |
| 14 | `AZ.ACCT.INT.ADJ.AMT` | `AzAcctBal_IntAdjAmt` |  |  |  |
| 15 | `AZ.ACCT.RESERVED2` | `AzAcctBal_Reserved2` |  |  |  |
| 16 | `AZ.ACCT.RESERVED1` | `AzAcctBal_Reserved1` |  |  |  |
| 17 | `AZ.ACCT.CONSOL.BAL` | `AzAcctBal_ConsolBal` | TField |  | "This field holds the amount which is the sum of the principal, interest and charge amounts repaid in this AZ account. The amounts from the fields PRINCIPAL, INTEREST and CHARGES of this record are used to arrive at this consolidated balance. " |
| 18 | `AZ.ACCT.CURR.HIST.NO` | `AzAcctBal_CurrHistNo` | TField |  | This field holds the details of the record in AZ.ACCT.BAL.HIST file. Whenever a record is moved to AZ.ACCT.BAL.HIST file, this field will be updated with the date of the movement and sequence number. . |
| 19 | `AZ.ACCT.PEN.DATE` | `AzAcctBal_PenDate` |  |  |  |
| 20 | `AZ.ACCT.PEN.CHG.CODE` | `AzAcctBal_PenChgCode` |  |  |  |
| 21 | `AZ.ACCT.PEN.CHG.AMT` | `AzAcctBal_PenChgAmt` |  |  |  |
| 22 | `AZ.ACCT.RESERVED.6` | `AzAcctBal_Reserved6` | TField |  |  |
| 23 | `AZ.ACCT.RESERVED.5` | `AzAcctBal_Reserved5` | TField |  |  |
| 24 | `AZ.ACCT.RESERVED.4` | `AzAcctBal_Reserved4` | TField |  |  |
| 25 | `AZ.ACCT.RESERVED.3` | `AzAcctBal_Reserved3` | TField |  |  |
| 26 | `AZ.ACCT.RESERVED.2` | `AzAcctBal_Reserved2` |  |  |  |
| 27 | `AZ.ACCT.RESERVED.1` | `AzAcctBal_Reserved1` |  |  |  |
| 28 | `AZ.ACCT.RECORD.STATUS` | `AzAcctBal_RecordStatus` | String |  |  |
| 29 | `AZ.ACCT.CURR.NO` | `AzAcctBal_CurrNo` | String |  |  |
| 30 | `AZ.ACCT.INPUTTER` | `AzAcctBal_Inputter` |  |  |  |
| 31 | `AZ.ACCT.DATE.TIME` | `AzAcctBal_DateTime` |  |  |  |
| 32 | `AZ.ACCT.AUTHORISER` | `AzAcctBal_Authoriser` | String |  |  |
| 33 | `AZ.ACCT.CO.CODE` | `AzAcctBal_CoCode` | String |  |  |
| 34 | `AZ.ACCT.DEPT.CODE` | `AzAcctBal_DeptCode` | String |  |  |
| 35 | `AZ.ACCT.AUDITOR.CODE` | `AzAcctBal_AuditorCode` | String |  |  |
| 36 | `AZ.ACCT.AUDIT.DATE.TIME` | `AzAcctBal_AuditDateTime` | String |  |  |
