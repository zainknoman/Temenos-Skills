# CBCRRT.DEPOSIT.CAPTURE — Table Schema

> Source: `INSERTS/I_F.CBCRRT.DEPOSIT.CAPTURE` in `CBCRRT_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CBCRRT.TERM.DEPOSIT.AMOUNT` | `CbcrrtDepositCapture_TermDepositAmount` |  |  |  |
| 2 | `CBCRRT.NON.TERM.DEPOSIT.AMOUNT` | `CbcrrtDepositCapture_NonTermDepositAmount` |  |  |  |
| 3 | `CBCRRT.OVERSEAS.DEPOSIT` | `CbcrrtDepositCapture_OverseasDeposit` |  |  |  |
| 4 | `CBCRRT.AVERAGE.TERM.DEPOSIT.AMT` | `CbcrrtDepositCapture_AverageTermDepositAmt` | TField |  | Average term deposit balance. |
| 5 | `CBCRRT.AVG.NON.TERM.DEPOSIT.AMOUNT` | `CbcrrtDepositCapture_AvgNonTermDepositAmount` | TField |  |  |
| 6 | `CBCRRT.AVG.OVERSEAS.DEPOSIT.AMOUNT` | `CbcrrtDepositCapture_AvgOverseasDepositAmount` | TField |  |  |
| 7 | `CBCRRT.REQUIRED.CRR.AMT` | `CbcrrtDepositCapture_RequiredCrrAmt` | TField |  | Required CRR amount |
| 8 | `CBCRRT.ACTIVITY.ID` | `CbcrrtDepositCapture_ActivityId` | TField |  | Activity Id of the Interest change activity |
| 9 | `CBCRRT.OFS.STATUS` | `CbcrrtDepositCapture_OfsStatus` | TField |  | Success/ Failure field to define if interest change activity and penalty balance update action is done. |
| 10 | `CBCRRT.ERROR.REASON` | `CbcrrtDepositCapture_ErrorReason` |  |  |  |
| 11 | `CBCRRT.RESERVED.1` | `CbcrrtDepositCapture_Reserved1` | TField |  | This field is reserved for future use |
| 12 | `CBCRRT.RESERVED.2` | `CbcrrtDepositCapture_Reserved2` | TField |  | This field is reserved for future use |
| 13 | `CBCRRT.RESERVED.3` | `CbcrrtDepositCapture_Reserved3` | TField |  | This field is reserved for future use |
| 14 | `CBCRRT.RESERVED.4` | `CbcrrtDepositCapture_Reserved4` | TField |  | This field is reserved for future use |
| 15 | `CBCRRT.RESERVED.5` | `CbcrrtDepositCapture_Reserved5` | TField |  | This field is reserved for future use |
| 16 | `CBCRRT.LOCAL.REF` | `CbcrrtDepositCapture_LocalRef` |  |  |  |
| 17 | `CBCRRT.OVERRIDE` | `CbcrrtDepositCapture_Override` |  |  |  |
| 18 | `CBCRRT.RECORD.STATUS` | `CbcrrtDepositCapture_RecordStatus` | String |  |  |
| 19 | `CBCRRT.CURR.NO` | `CbcrrtDepositCapture_CurrNo` | String |  |  |
| 20 | `CBCRRT.INPUTTER` | `CbcrrtDepositCapture_Inputter` |  |  |  |
| 21 | `CBCRRT.DATE.TIME` | `CbcrrtDepositCapture_DateTime` |  |  |  |
| 22 | `CBCRRT.AUTHORISER` | `CbcrrtDepositCapture_Authoriser` | String |  |  |
| 23 | `CBCRRT.CO.CODE` | `CbcrrtDepositCapture_CoCode` | String |  |  |
| 24 | `CBCRRT.DEPT.CODE` | `CbcrrtDepositCapture_DeptCode` | String |  |  |
| 25 | `CBCRRT.AUDITOR.CODE` | `CbcrrtDepositCapture_AuditorCode` | String |  |  |
| 26 | `CBCRRT.AUDIT.DATE.TIME` | `CbcrrtDepositCapture_AuditDateTime` | String |  |  |
