# FD.GROUP.PAYMENT — Table Schema

> Source: `INSERTS/I_F.FD.GROUP.PAYMENT` in `FD_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FD.GP.DESCRIPTION` | `FdGroupPayment_Description` |  |  |  |
| 2 | `FD.GP.CURRENT.INT.RATE` | `FdGroupPayment_CurrentIntRate` | TField | Yes | The current interest rate applicable. The current interest rate is held in this field. This must be entered for a new record, and cannot be changedonce input. Interest rate changes should be entered using the NEW.INT.RATE and NEW.RATE.EFF fields. TheCURRENT.INT.RATE will be updated at the NEW.RATE.EFF date during the Fiduciary end of day. Validation Rules: 1-11 numeric rate type. (Mandatory field) |
| 3 | `FD.GP.INTEREST.RATE` | `FdGroupPayment_InterestRate` |  |  |  |
| 4 | `FD.GP.RATE.EFF.DATE` | `FdGroupPayment_RateEffDate` |  |  |  |
| 5 | `FD.GP.NEW.INT.RATE` | `FdGroupPayment_NewIntRate` |  |  |  |
| 6 | `FD.GP.NEW.RATE.EFF` | `FdGroupPayment_NewRateEff` |  |  |  |
| 7 | `FD.GP.DAYS.PRIOR.CONF` | `FdGroupPayment_DaysPriorConf` | TField | No | The number of days prior to a new interest rate effective date, for a rate change confirmation to be sent. The default value for the number of days is taken from the FD.PARAMETER file in the field DEF.RATE.NOTICE. Validation Rules: 0-99 number of days (Optional input) Input not allowed when Term is given as part of ID |
| 8 | `FD.GP.AUTO.CHG.RATE` | `FdGroupPayment_AutoChgRate` | TField |  | Defines if automatic allocation of INTEREST.RATE since END.OF.DAY is used to calculate the new interest rate ofNotice Deposit. Only for inside group notice deposit, and by bank . Validation Rules: A maximum of 4 characters may be entered The following values are permitted: YES, NO Input not allowed when Term is given as part of ID |
| 9 | `FD.GP.FORWARD.BACKWARD` | `FdGroupPayment_ForwardBackward` | TField | No | This field indicates the method that will be followed if the cycled interest settlement date is a non working dayin the relative currency. The following provides an explanation of the various input values for this field: Null = Calendar The sysem will use the same date irrespective of whether dates cycled are working days or not. 1 = Forward The system will cycle forward to the next available working day. 2 = Backward The system will cycle to the previous working day. 3 = Fwd Same Month The system will cycle forward unless the next working day unless it falls in the next month.In this case, it will cycle to the previous working day. Validation A single numeric value in the range 1-3 or Null. Null = Calendar 1 = Forward 2 = Backward 3 = Forward same month Single Value Optional input |
| 10 | `FD.GP.INT.SETTLE.DATE` | `FdGroupPayment_IntSettleDate` | TField | No | The date and optional frequency for the interest settlement for all linked placement contracts. The interest settlement date may be announced by the fiduciary bank as a one off payment date, or on a regularfrequency. When multiple NOTICE orders are pooled onto a single placement, and an order is being reimbursed, the interestfor this order will be paid on the date held in this field, regardless of the date on which the order was reducedto zero principal. Validation Rules: 8-character standard date input followed by 5-character standard frequency (Optional input) Must be after the LAST.INT.SET.DATE. |
| 11 | `FD.GP.LAST.INT.SET.DATE` | `FdGroupPayment_LastIntSetDate` | TField |  | The date of the last interest settlement. When an interest settlement date is reached, the interest are written to the FD.GROUP.PAYMENT.HIST file with thekey, of Fid Bank . Currency . Days Notice . Settlement date and the settlement date will be recorded on in this field. Validation Rules: 8 standard date characters This is a NOINPUT field. |
| 12 | `FD.GP.LAST.RATE.APPLIED` | `FdGroupPayment_LastRateApplied` | TField |  | The last interest rate applied at the LAST.INT.SET.DATE. Validation Rules: 1-11 numeric rate This is a NOINPUT field. |
| 13 | `FD.GP.OVERRIDE` | `FdGroupPayment_Override` |  |  |  |
| 14 | `FD.GP.RECORD.STATUS` | `FdGroupPayment_RecordStatus` | String |  |  |
| 15 | `FD.GP.CURR.NO` | `FdGroupPayment_CurrNo` | String |  |  |
| 16 | `FD.GP.INPUTTER` | `FdGroupPayment_Inputter` |  |  |  |
| 17 | `FD.GP.DATE.TIME` | `FdGroupPayment_DateTime` |  |  |  |
| 18 | `FD.GP.AUTHORISER` | `FdGroupPayment_Authoriser` | String |  |  |
| 19 | `FD.GP.CO.CODE` | `FdGroupPayment_CoCode` | String |  |  |
| 20 | `FD.GP.DEPT.CODE` | `FdGroupPayment_DeptCode` | String |  |  |
| 21 | `FD.GP.AUDITOR.CODE` | `FdGroupPayment_AuditorCode` | String |  |  |
| 22 | `FD.GP.AUDIT.DATE.TIME` | `FdGroupPayment_AuditDateTime` | String |  |  |
| 23 | `FD.GP.INT.DAY.BASIS` | `FdGroupPayment_IntDayBasis` | TField |  | The Interest day basis to be used for Interest calculation. Allowed only for FIXED type of contracts where Termis part of the FD.GROUP.PAYMENT. Validation Rules: Allowed Values: A,B,E,F) A 360/360 B 366/360 E 366/365 F 360/365 |
| 24 | `FD.GP.HOLIDAY.CALENDAR` | `FdGroupPayment_HolidayCalendar` | TField |  | This field accepts any calendar including region value The interest payment dates and maturity dates for Fixed term deposits will be calculated using this calendar. The interest payment dates and maturity dates should be working days in this calender. Else, using the nearestworking day will be calculated using FORWARD.BACKWARD field value Validation Rules: Valid Holiday Calendar name or Valid Region Field is available to input only when Term is given as part of FD.GROUP.PAYMENT id |
| 25 | `FD.GP.VAL.DATE.OFFSET` | `FdGroupPayment_ValDateOffset` | TField |  | The value in this field will be added to Order date to default the value date of Fixed FD.FID.ORDER Validation Rules: Allowed Values: 1-10 Field is available to input only when Term is given as part of FD.GROUP.PAYMENT id |
