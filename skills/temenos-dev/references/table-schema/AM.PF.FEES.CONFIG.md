# AM.PF.FEES.CONFIG — Table Schema

> Source: `INSERTS/I_F.AM.PF.FEES.CONFIG` in `AM_PerformanceFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.PFC.PL.CATEGORY` | `AmPfFeesConfig_PlCategory` | TField | Yes | This field should accept a valid PL category (ie. 50000 - 69999), all PL entries posted against performance fees should be posted against this category It is a Mandatory Field |
| 2 | `AM.PFC.ACCRUAL.CATEGORY` | `AmPfFeesConfig_AccrualCategory` | TField |  | This field should accept a valid internal account category (ie. 10000- 19999) This category is used for storing the accrual during a fee period, |
| 3 | `AM.PFC.PRODUCT.CATEGORY` | `AmPfFeesConfig_ProductCategory` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `AM.PFC.CR.TXN.CODE` | `AmPfFeesConfig_CrTxnCode` | TField | Yes | This field should accept a valid CREDIT transaction code Mandatory field Use for raising entry related to Performance fees |
| 5 | `AM.PFC.DR.TXN.CODE` | `AmPfFeesConfig_DrTxnCode` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 6 | `AM.PFC.ACCRUAL` | `AmPfFeesConfig_Accrual` | TField |  | Can be Daily or Monthly or None.Fee accrual can be stopped any day by choosing None. When it is changed to Daily, fees would be accrued daily from the date of change. If it is changed to Monthly from Daily during mid month, fees would be accrued on month end for remining non accrued days in the month. Validation Rules: Valid Inputs - Daily_Monthly_None |
| 7 | `AM.PFC.COMPANY.WIDE` | `AmPfFeesConfig_CompanyWide` | TField |  | This field is used for setting company wide frequency for all portfolios belong to the company Validation Rules: Valid Inputs - Yes or Null |
| 8 | `AM.PFC.FREQUENCY` | `AmPfFeesConfig_Frequency` | TField | Yes | if company wide is set to Yes , this becomes an Mandatory field. It determines the fee period frequency Validation Rules: It should be a valid T24 FQU field. |
| 9 | `AM.PFC.COB.POSTING` | `AmPfFeesConfig_CobPosting` | TField |  | Can be Yes or Null. If Yes, generated fees would be automatically posted during COB after posting window Validation Rules: Valid inputs - Yes_'' |
| 10 | `AM.PFC.POSTING.WINDOW` | `AmPfFeesConfig_PostingWindow` | TField |  | This field determines the number of days fees would be available in calculation stage for review (from calculation date of fee record) before it gets automatically posted. Validation Rules: Should accept a valid formula to increment number of days from fees calculation date. Say, +01W or +10W or +02C. For eg: If it is +10W, the fees would be available for the user to review for 10 calender days after that it is automatically posted if COB.POSTING is set to Yes. If it is +10C, the fees would be available for the user to review for 10 working days after that it is automatically posted if COB.POSTING is set to Yes. Maximum days(calender or working) allowed in the date formula is 30 |
| 11 | `AM.PFC.VALUE.DATE` | `AmPfFeesConfig_ValueDate` | TField |  | This field determines the value date for the accounting entries in automatic fee posting during COB. Validation Rules: Should accept a valid formula to increment number of days from fees calculation date. Say, +01W or +10W or +02C. For eg: If it is +01C, the value date of the accounting entry would be one calender day after posting date If it is +01W, the value date of the accounting entry would be one working day after posting date Maximum days(calender or working) allowed in the date formula is 30 |
| 12 | `AM.PFC.CARRY.LOSS` | `AmPfFeesConfig_CarryLoss` | TField |  | Can be Yes or Null. If yes, the accumulated loss are carried forward to next fee period. Validation Rules: valid inputs : YES_'' |
| 13 | `AM.PFC.ADJUST.ACCRUAL` | `AmPfFeesConfig_AdjustAccrual` | TField |  | Can be Yes or Null. If yes, the difference in actual fees and accrued fees would be posted during fees posting. Validation Rules: Valid input - Yes_'' |
| 14 | `AM.PFC.ACCRUAL.DIFF` | `AmPfFeesConfig_AccrualDiff` | TField |  | If yes, accrual difference is posted. Otherwise, previous accruals are reversed and new accraul is rebooked. Validation Rules: valid inputs - Yes_'' |
| 15 | `AM.PFC.ACCR.REV.XRATE` | `AmPfFeesConfig_AccrRevXrate` | TField | Yes | Mandatory if ACCRUAL.DIFF is not Yes. If previous, the previous accruals are reversed at the same rate. Otherwise, previous accruals are reversed at current mid reval rate. Default is current. Validation Rules: valid inputs - Previous_Current |
| 16 | `AM.PFC.RESERVED.10` | `AmPfFeesConfig_Reserved10` | TField |  | For future use |
| 17 | `AM.PFC.RESERVED.9` | `AmPfFeesConfig_Reserved9` | TField |  | For future use |
| 18 | `AM.PFC.RESERVED.8` | `AmPfFeesConfig_Reserved8` | TField |  | For future use |
| 19 | `AM.PFC.RESERVED.7` | `AmPfFeesConfig_Reserved7` | TField |  | For future use |
| 20 | `AM.PFC.RESERVED.6` | `AmPfFeesConfig_Reserved6` | TField |  | For future use |
| 21 | `AM.PFC.RESERVED.5` | `AmPfFeesConfig_Reserved5` | TField |  | For future use |
| 22 | `AM.PFC.RESERVED.4` | `AmPfFeesConfig_Reserved4` | TField |  | For future use |
| 23 | `AM.PFC.RESERVED.3` | `AmPfFeesConfig_Reserved3` | TField |  | For future use |
| 24 | `AM.PFC.RESERVED.2` | `AmPfFeesConfig_Reserved2` | TField |  | For future use |
| 25 | `AM.PFC.RESERVED.1` | `AmPfFeesConfig_Reserved1` | TField |  | For future use |
| 26 | `AM.PFC.OVERRIDE` | `AmPfFeesConfig_Override` |  |  |  |
| 27 | `AM.PFC.RECORD.STATUS` | `AmPfFeesConfig_RecordStatus` | String |  |  |
| 28 | `AM.PFC.CURR.NO` | `AmPfFeesConfig_CurrNo` | String |  |  |
| 29 | `AM.PFC.INPUTTER` | `AmPfFeesConfig_Inputter` |  |  |  |
| 30 | `AM.PFC.DATE.TIME` | `AmPfFeesConfig_DateTime` |  |  |  |
| 31 | `AM.PFC.AUTHORISER` | `AmPfFeesConfig_Authoriser` | String |  |  |
| 32 | `AM.PFC.CO.CODE` | `AmPfFeesConfig_CoCode` | String |  |  |
| 33 | `AM.PFC.DEPT.CODE` | `AmPfFeesConfig_DeptCode` | String |  |  |
| 34 | `AM.PFC.AUDITOR.CODE` | `AmPfFeesConfig_AuditorCode` | String |  |  |
| 35 | `AM.PFC.AUDIT.DATE.TIME` | `AmPfFeesConfig_AuditDateTime` | String |  |  |
