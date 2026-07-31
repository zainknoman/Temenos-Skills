# MI.PARAMETER — Table Schema

> Source: `INSERTS/I_F.MI.PARAMETER` in `MI_Entries.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MI.PARAM.RETENTION` | `MiParameter_Retention` | TField |  | The retention period sets the number of months for which MI information is stored. Records older than this will be purged next time the appropriate job is run. Records from the following files are eligable to be purged; MI.ENTRY MI.AUTO.ENTRY MI.BUDGET MI.BUDGET.LINE MI.DATA... (ie all MI databases.) The date on the MI record which determines whether it is to be removed is the MI period it falls into, not the creation date. Thus if you have RETENTION set to 18 months, and you regenerate 2 years of an MI database, the first 6 months of the database will be purged when the next EOD is run. Validation Rules: Must be between 0 and 999 |
| 2 | `MI.PARAM.SELECTION` | `MiParameter_Selection` |  |  |  |
| 3 | `MI.PARAM.OPERAND` | `MiParameter_Operand` |  |  |  |
| 4 | `MI.PARAM.MI.CR.INT.KEY` | `MiParameter_MiCrIntKey` |  |  |  |
| 5 | `MI.PARAM.MI.CR.INT.MGN` | `MiParameter_MiCrIntMgn` |  |  |  |
| 6 | `MI.PARAM.MI.DR.INT.KEY` | `MiParameter_MiDrIntKey` |  |  |  |
| 7 | `MI.PARAM.MI.DR.INT.MGN` | `MiParameter_MiDrIntMgn` |  |  |  |
| 8 | `MI.PARAM.FUNDING.DEPT` | `MiParameter_FundingDept` |  |  |  |
| 9 | `MI.PARAM.ADD.COF.TYPE` | `MiParameter_AddCofType` |  |  |  |
| 10 | `MI.PARAM.COF.RATE.CR` | `MiParameter_CofRateCr` |  |  |  |
| 11 | `MI.PARAM.COF.RATE.DR` | `MiParameter_CofRateDr` |  |  |  |
| 12 | `MI.PARAM.ADD.COF.DEPT` | `MiParameter_AddCofDept` |  |  |  |
| 13 | `MI.PARAM.TRANS.CODE.DR` | `MiParameter_TransCodeDr` | TField | Yes | This field is used to hold the transaction code which will be used on the refinancing entries produced on the MI.COF.ENTRIES file to populate the debit transaction code field. When the MI.AUTO.ENTRY records are created, this transaction should be used as the transaction code for the debitting entry. Validation Rules: Must be the key to a valid record on the TRANSACTION file. Mandatory |
| 14 | `MI.PARAM.TRANS.CODE.CR` | `MiParameter_TransCodeCr` | TField | Yes | This field is used to hold the transaction code which will be used on the refinancing entries produced on the MI.COF.ENTRIES file to populate the credit transaction code field. When the MI.AUTO.ENTRY records are created, this transaction should be used as the transaction code for the creditting entry. Validation Rules: Must be the key to a valid record on the TRANSACTION file. Mandatory |
| 15 | `MI.PARAM.RESERVED.1` | `MiParameter_Reserved1` | TField |  |  |
| 16 | `MI.PARAM.APPLICATION` | `MiParameter_Application` |  |  |  |
| 17 | `MI.PARAM.SOURCE.FIELD.CR` | `MiParameter_SourceFieldCr` |  |  |  |
| 18 | `MI.PARAM.SOURCE.FIELD.DR` | `MiParameter_SourceFieldDr` |  |  |  |
| 19 | `MI.PARAM.ENTRY.TYPE.CR` | `MiParameter_EntryTypeCr` | TField |  | The entry type which will be assigned to the credit cost of funds entry on the MI.COF.ENTRIES file is held in this field. Validation Rules: Must be the key to a valid record on the MI.ENTRY.TYPE file. |
| 20 | `MI.PARAM.ENTRY.TYPE.DR` | `MiParameter_EntryTypeDr` | TField |  | The entry type which will be assigned to the debit cost of funds entry on the MI.COF.ENTRIES file is held in this field. Validation Rules: Must be the key to a valid record on the MI.ENTRY.TYPE file. |
| 21 | `MI.PARAM.BASE.CURRENCY` | `MiParameter_BaseCurrency` | TField |  | This field is used to specify the base currency of the MI system, and is used in each company, regardless of local currency, as the base currency. This allows multiple companies, with differing local currencies, to produce meaningful figures in the base currency which may be included within the database. This is the currency which will be used to perform the conversion where a COLUMN.TYPE of ACCUM.BCY or INT.ACCR.BCY is specified on the MI.COLUMN record. Validation Rules: Must be the key to a valid CURRENCY record. Defaults to Local Currency. |
| 22 | `MI.PARAM.START.OF.WEEK.DAY` | `MiParameter_StartOfWeekDay` | TField |  | The calendar day for the start of the week. Used when MI databases have a frequency of weekly. Default is MONDAY. Validation Rules: Must be a valid weekday: MONDAY (default) TUESDAY WEDNESDAY THURSDAY FRIDAY SATURDAY SUNDAY |
| 23 | `MI.PARAM.COMPANY` | `MiParameter_Company` |  |  |  |
| 24 | `MI.PARAM.DEFLT.FUND.DEPT` | `MiParameter_DefltFundDept` |  |  |  |
| 25 | `MI.PARAM.BUILD.PL.ENTRIES` | `MiParameter_BuildPlEntries` | TField |  | Specifies whether the CATEG.ENTRY records are to be consolidated in MI Database by BOOKING.DATE or ACCOUNTING.DATE. ACCOUNTING.DATE for CATEG.ENTRY records could be specified only for records generated by entries input through DATA.CAPTURE application, provided the POST CLOSING module is installed. If an ACCOUNTING.DATE is specified in CATEG.ENTRY records, consolidation would depend on the date of the earliest Post Closing (PC) Database updated (i.e. earliest PC.PERIOD.END in the entries, provided the field PC.APPLIED=Y). Validation Rules: Allowed values are BOOKING and ACCOUNTING. Default value is Null when the CATEG.ENTRY records would be consolidated in MI Database based on BOOKING.DATE. Change of value not allowed from ACCOUNTING. |
| 26 | `MI.PARAM.BUILD.BD.BALANCES` | `MiParameter_BuildBdBalances` | TField |  | Specifies whether Book-Date related fields in BALANCE.MOVMENT (Fields: OPEN.BD.BALANCE to BK.AVG.BAL.CAL) records of Accounts have to be populated or not. When the field value is set to YES, Book-Date related fields of BALANCE.MOVEMENT records of Accounts would be populated based on the BOOKING.DATE in STMT.ENTRY records. If the STMT.ENTRY records specify an ACCOUNTING.DATE (when the Post Closing Module is installed), then these fields would be updated based on the earliest PC.PERIOD in STMT.ENTRY records, provided the entries have been applied to Post Closing Database. When the field value is set to NO, Book-Date related fields of BALANCE.MOVEMENT records would not be populated. Validation Rules: Allowed values are YES and NO. Default value is Null equivalent to NO. Once the value is set to YES, it cannot be changed. |
| 27 | `MI.PARAM.POST.DATE.BAL.UPD` | `MiParameter_PostDateBalUpd` | TField |  | Specifies whether the POST Average Balance fields need to be updated in BALANCE.MOVEMENT. Validation Rules: Valid values are YES/NO. Atleast one of the fields POST.DATE.BAL.UPD, ADJ.DATE.BAL.UPD, VAL.DATE.BAL.UPD should have a value. |
| 28 | `MI.PARAM.ADJ.DATE.BAL.UPD` | `MiParameter_AdjDateBalUpd` | TField |  | Specifies whether the ADJ Average Balance fields need to be updated in BALANCE.MOVEMENT. Validation Rules: Valid values are YES/NO. Atleast one of the fields POST.DATE.BAL.UPD, ADJ.DATE.BAL.UPD, VAL.DATE.BAL.UPD should have a value. |
| 29 | `MI.PARAM.VAL.DATE.BAL.UPD` | `MiParameter_ValDateBalUpd` | TField |  | Specifies whether the Value date Average Balance fields need to be updated in BALANCE.MOVEMENT. Validation Rules: Valid values are YES/NO. Atleast one of the fields POST.DATE.BAL.UPD, ADJ.DATE.BAL.UPD, VAL.DATE.BAL.UPD should have a value. |
| 30 | `MI.PARAM.BAL.MVMT.APPS` | `MiParameter_BalMvmtApps` |  |  |  |
| 31 | `MI.PARAM.LOCAL.REF` | `MiParameter_LocalRef` |  |  |  |
| 32 | `MI.PARAM.GL.BAL.REPORT` | `MiParameter_GlBalReport` |  |  |  |
| 33 | `MI.PARAM.PL.CATEGORY.ASST` | `MiParameter_PlCategoryAsst` | TField |  |  |
| 34 | `MI.PARAM.PL.CATEGORY.LIAB` | `MiParameter_PlCategoryLiab` | TField |  |  |
| 35 | `MI.PARAM.UOF.PL.CURR.MONTH` | `MiParameter_UofPlCurrMonth` | TField |  |  |
| 36 | `MI.PARAM.UOF.PL.PREV.MONTH` | `MiParameter_UofPlPrevMonth` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 37 | `MI.PARAM.UOF.PL.PREV.YEAR` | `MiParameter_UofPlPrevYear` | TField |  |  |
| 38 | `MI.PARAM.COF.PL.CURR.MONTH` | `MiParameter_CofPlCurrMonth` | TField |  |  |
| 39 | `MI.PARAM.COF.PL.PREV.MONTH` | `MiParameter_CofPlPrevMonth` | TField |  |  |
| 40 | `MI.PARAM.COF.PL.PREV.YEAR` | `MiParameter_CofPlPrevYear` | TField |  |  |
| 41 | `MI.PARAM.POST.BACK.VALUE` | `MiParameter_PostBackValue` | TField |  |  |
| 42 | `MI.PARAM.BM.FOR.INT.ACC` | `MiParameter_BmForIntAcc` | TField |  |  |
| 43 | `MI.PARAM.TP.POSTING.STYLE` | `MiParameter_TpPostingStyle` | TField |  |  |
| 44 | `MI.PARAM.TP.POSTING.METHOD` | `MiParameter_TpPostingMethod` | TField |  |  |
| 45 | `MI.PARAM.BOOK.MARKET` | `MiParameter_BookMarket` | TField | Yes | Accepts BOOK.COST/MARKET.VALUE based on which cost of funds is arrived for own book and customer portfolio. If this field holds MARKET.VALUE, by default CURR.MARKET.VALUE is used as SOURCE.FIELD. If this field holds BOOK.COST, SOURCE.FIELD defined in SOURCE.FIELD.DR and SOURCE.FIELD.CR is considered when calculated cost of funds. Mandatory inpuut if any of the APPLICATION multi value field holds SC |
| 46 | `MI.PARAM.RECORD.STATUS` | `MiParameter_RecordStatus` | String |  |  |
| 47 | `MI.PARAM.CURR.NO` | `MiParameter_CurrNo` | String |  |  |
| 48 | `MI.PARAM.INPUTTER` | `MiParameter_Inputter` |  |  |  |
| 49 | `MI.PARAM.DATE.TIME` | `MiParameter_DateTime` |  |  |  |
| 50 | `MI.PARAM.AUTHORISER` | `MiParameter_Authoriser` | String |  |  |
| 51 | `MI.PARAM.CO.CODE` | `MiParameter_CoCode` | String |  |  |
| 52 | `MI.PARAM.DEPT.CODE` | `MiParameter_DeptCode` | String |  |  |
| 53 | `MI.PARAM.AUDITOR.CODE` | `MiParameter_AuditorCode` | String |  |  |
| 54 | `MI.PARAM.AUDIT.DATE.TIME` | `MiParameter_AuditDateTime` | String |  |  |
