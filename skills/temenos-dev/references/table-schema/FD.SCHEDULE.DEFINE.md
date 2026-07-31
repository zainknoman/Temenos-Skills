# FD.SCHEDULE.DEFINE — Table Schema

> Source: `INSERTS/I_F.FD.SCHEDULE.DEFINE` in `FD_Schedules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FD.SCHDEF.FID.BANK` | `FdScheduleDefine_FidBank` | TField |  | This field holds the FidBank in Fiduciary Validation Rules: NoInput Field |
| 2 | `FD.SCHDEF.FID.BANK.REF` | `FdScheduleDefine_FidBankRef` | TField |  | This field is used to hold the reference given by the FidBank |
| 3 | `FD.SCHDEF.ORDER.ID` | `FdScheduleDefine_OrderId` | TField |  | This field holds the FID.ORDER Id of the Fiduciary Validation Rules: NoInput Field |
| 4 | `FD.SCHDEF.INT.RATE` | `FdScheduleDefine_IntRate` | TField |  | This field holds the Interest Rate in Fiduciary Validation Rules: NoInput Field |
| 5 | `FD.SCHDEF.INT.FREQUENCY` | `FdScheduleDefine_IntFrequency` | TField |  | This field holds the Interest Frequency in Fiduciary Validation Rules: NoInput Field |
| 6 | `FD.SCHDEF.SYS.INT.DATE` | `FdScheduleDefine_SysIntDate` |  |  |  |
| 7 | `FD.SCHDEF.SYS.INTEREST.AMT` | `FdScheduleDefine_SysInterestAmt` |  |  |  |
| 8 | `FD.SCHDEF.SYS.WHT.TAX` | `FdScheduleDefine_SysWhtTax` |  |  |  |
| 9 | `FD.SCHDEF.FID.BANK.INT.DATE` | `FdScheduleDefine_FidBankIntDate` |  |  |  |
| 10 | `FD.SCHDEF.FID.BANK.INT.AMT` | `FdScheduleDefine_FidBankIntAmt` |  |  |  |
| 11 | `FD.SCHDEF.FID.BANK.WHT.TAX` | `FdScheduleDefine_FidBankWhtTax` |  |  |  |
| 12 | `FD.SCHDEF.INTEREST.AMT` | `FdScheduleDefine_InterestAmt` |  |  |  |
| 13 | `FD.SCHDEF.TOTAL.INTEREST` | `FdScheduleDefine_TotalInterest` | TField |  | This field is holds the sum of Interest amount to be credited to the customer on FID.BANK.INT.DATE Validation Rules: NoInput field |
| 14 | `FD.SCHDEF.MATURITY.DATE` | `FdScheduleDefine_MaturityDate` | TField |  | This field holds the Maturity date of the contract. Early maturity date will be updated when Early maturing the contract Validation Rules: NoInput field |
| 15 | `FD.SCHDEF.MATURITY.AMT` | `FdScheduleDefine_MaturityAmt` | TField |  | This field holds the principal amount of the contract. Early maturity amount will be updated when Early maturing the contract Validation Rules: NoInput field |
| 16 | `FD.SCHDEF.MAT.AMT.RECD.DATE` | `FdScheduleDefine_MatAmtRecdDate` | TField |  | This field will be input by the user when the Maturity or Early Maturity amount of the contract is actuallyreceived from FidBank.Customer will receive credit on this date. Till then the credit will lie in the internal account defined in FD.PARAMETER Validation Rules: Input Date must be after the actual payment is raised to the Interenal Category account |
| 17 | `FD.SCHDEF.LOCAL.REF` | `FdScheduleDefine_LocalRef` |  |  |  |
| 18 | `FD.SCHDEF.OVERRIDE` | `FdScheduleDefine_Override` |  |  |  |
| 19 | `FD.SCHDEF.RECORD.STATUS` | `FdScheduleDefine_RecordStatus` | String |  |  |
| 20 | `FD.SCHDEF.CURR.NO` | `FdScheduleDefine_CurrNo` | String |  |  |
| 21 | `FD.SCHDEF.INPUTTER` | `FdScheduleDefine_Inputter` |  |  |  |
| 22 | `FD.SCHDEF.DATE.TIME` | `FdScheduleDefine_DateTime` |  |  |  |
| 23 | `FD.SCHDEF.AUTHORISER` | `FdScheduleDefine_Authoriser` | String |  |  |
| 24 | `FD.SCHDEF.CO.CODE` | `FdScheduleDefine_CoCode` | String |  |  |
| 25 | `FD.SCHDEF.DEPT.CODE` | `FdScheduleDefine_DeptCode` | String |  |  |
| 26 | `FD.SCHDEF.AUDITOR.CODE` | `FdScheduleDefine_AuditorCode` | String |  |  |
| 27 | `FD.SCHDEF.AUDIT.DATE.TIME` | `FdScheduleDefine_AuditDateTime` | String |  |  |
