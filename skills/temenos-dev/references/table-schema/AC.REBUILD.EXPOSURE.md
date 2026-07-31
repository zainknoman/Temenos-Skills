# AC.REBUILD.EXPOSURE — Table Schema

> Source: `INSERTS/I_F.AC.REBUILD.EXPOSURE` in `AC_CashFlow.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.EX.CREDIT.ACCT.NO` | `AcRebuildExposure_CreditAcctNo` | TField |  | ID of the Account that requires adjustment of exposure dates Validation Rules: Must be a valid record in account application |
| 2 | `AC.EX.ACTION.NOTES` | `AcRebuildExposure_ActionNotes` |  |  |  |
| 3 | `AC.EX.ADJUST.METHOD` | `AcRebuildExposure_AdjustMethod` | TField |  | Defines the way adjustment has to be happen Options are 1.Redefine Ladder, 2.Adjust Dates. Redefine Ladder Use when exposure date as well as clearing amount has to be changed. Sum of redefined amount must match the difference of OnlineActual and OnlineCleared balances of the account Example: An account has two entries, �2000 to clear on 20th of this month and �400 to clear on 25th of this month, when customer requests to clear �2200 on 15th then to we need to change both these entries getting cleared in different dates so, use REDEFINE.LADDER and ExposureDate:1=15, AmountToClear:1=2200, ExposureDate:2=25, AmountToClear:2=200 Adjust Dates Use when only the clearing date has to be modified. Sum of all the entries due to clear on the specified date will be moved to new date. Example: An account has two entries, �2000 to clear on 20th of this month and �400 to clear on 25th of this month, when customer requests to clear �2000 on 15th then to we need to change only first entry's clearing date so, use ADJUST.DATES and OrigExpDate=20, NewExpDate=15 Validation Rules: Can take either of two options REDEFINE.LADDER or ADJUST.DATES |
| 4 | `AC.EX.EXP.DATE` | `AcRebuildExposure_ExpDate` |  |  |  |
| 5 | `AC.EX.AMT.TO.CLEAR` | `AcRebuildExposure_AmtToClear` |  |  |  |
| 6 | `AC.EX.ORG.EXP.DATE` | `AcRebuildExposure_OrgExpDate` |  |  |  |
| 7 | `AC.EX.NEW.EXP.DATE` | `AcRebuildExposure_NewExpDate` |  |  |  |
| 8 | `AC.EX.ONLINE.ACTUAL.BAL` | `AcRebuildExposure_OnlineActualBal` | TField |  | Actual account balance at the time of making the adjustment. Validation Rules: Standard amount format. No Inputtable Field |
| 9 | `AC.EX.ONLINE.CLEAR.BAL` | `AcRebuildExposure_OnlineClearBal` | TField |  | Cleared account balance at the time of making the adjustment. Validation Rules: Standard amount format. No Inputtable Field |
| 10 | `AC.EX.RESERVED.5` | `AcRebuildExposure_Reserved5` | TField |  |  |
| 11 | `AC.EX.RESERVED.4` | `AcRebuildExposure_Reserved4` | TField |  |  |
| 12 | `AC.EX.RESERVED.3` | `AcRebuildExposure_Reserved3` | TField |  |  |
| 13 | `AC.EX.RESERVED.2` | `AcRebuildExposure_Reserved2` | TField |  |  |
| 14 | `AC.EX.RESERVED.1` | `AcRebuildExposure_Reserved1` | TField |  |  |
| 15 | `AC.EX.RECORD.STATUS` | `AcRebuildExposure_RecordStatus` | String |  |  |
| 16 | `AC.EX.CURR.NO` | `AcRebuildExposure_CurrNo` | String |  |  |
| 17 | `AC.EX.INPUTTER` | `AcRebuildExposure_Inputter` |  |  |  |
| 18 | `AC.EX.DATE.TIME` | `AcRebuildExposure_DateTime` |  |  |  |
| 19 | `AC.EX.AUTHORISER` | `AcRebuildExposure_Authoriser` | String |  |  |
| 20 | `AC.EX.CO.CODE` | `AcRebuildExposure_CoCode` | String |  |  |
| 21 | `AC.EX.DEPT.CODE` | `AcRebuildExposure_DeptCode` | String |  |  |
| 22 | `AC.EX.AUDITOR.CODE` | `AcRebuildExposure_AuditorCode` | String |  |  |
| 23 | `AC.EX.AUDIT.DATE.TIME` | `AcRebuildExposure_AuditDateTime` | String |  |  |
| 24 | `AC.EX.STMT.NOS` | `AcRebuildExposure_StmtNos` |  |  |  |
| 25 | `AC.EX.OVERRIDE` | `AcRebuildExposure_Override` |  |  |  |
