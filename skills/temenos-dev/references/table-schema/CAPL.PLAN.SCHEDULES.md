# CAPL.PLAN.SCHEDULES — Table Schema

> Source: `INSERTS/I_F.CAPL.PLAN.SCHEDULES` in `CARGPL_RegisteredPlans.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.PLN.SCHED.DESCRIPTION` | `CaplPlanSchedules_Description` | TField |  |  |
| 2 | `CAPL.PLN.SCHED.TAX.METHOD` | `CaplPlanSchedules_TaxMethod` | TField | Yes | Field to indicate the method of calculating tax.Possible values are "ABSOLUTE" or "AVERAGE". For "AVERAGE" the tax rates are calculated from T24 TAX tables; for "ABSOLUTE" the tax rates are taken from the fields PROV.ACT.TAX.RATE, FED.ACT.TAX.RATE and NR.ACT.TAX.RATE defined in this application.Mandatory field. |
| 3 | `CAPL.PLN.SCHED.PROV.ACT.TAX.RATE` | `CaplPlanSchedules_ProvActTaxRate` | TField |  | Field to store the provincial rate to be used in case tax method is "ABSOLUTE" |
| 4 | `CAPL.PLN.SCHED.FED.ACT.TAX.RATE` | `CaplPlanSchedules_FedActTaxRate` | TField |  | Field to store the federal rate to be used in case tax method is "ABSOLUTE" |
| 5 | `CAPL.PLN.SCHED.NR.ACT.TAX.RATE` | `CaplPlanSchedules_NrActTaxRate` | TField |  | Field to store the tax rate to be calculated for non resident.ValidationThe non resident rate to be used in case tax method is "ABSOLUTE" |
| 6 | `CAPL.PLN.SCHED.USER.FIX.PROV.TAX` | `CaplPlanSchedules_UserFixProvTax` | TField |  | Field to store the user provincial tax amount to be used for each payment. If the calculated provincial tax amount is greater than this field amount then the calculated tax amount will be used instead.Validation:No negative amounts should be allowed |
| 7 | `CAPL.PLN.SCHED.USER.FIX.FED.TAX` | `CaplPlanSchedules_UserFixFedTax` | TField |  | Field to store the user federal tax amount to be used for each payment. If the calculated federal tax amount is greater than this field amount then the calculated tax amount will be used instead.Validation:No negative amounts should be allowed. |
| 8 | `CAPL.PLN.SCHED.USER.FIX.NR.TAX` | `CaplPlanSchedules_UserFixNrTax` | TField |  | Field to store the non resident tax amount to be used for each payment. If the calculated non resident tax amount is greater than this field amount then the calculated tax amount will be used instead.Validation:No negative amounts should be allowed. |
| 9 | `CAPL.PLN.SCHED.CHECK.AVERAGE.TAXES` | `CaplPlanSchedules_CheckAverageTaxes` | TField |  | Field to Indicate if Taxe rate is calculated based on Average or notValid option Yes or No fieldif Yes- Tax rate will be on average method. not sure |
| 10 | `CAPL.PLN.SCHED.SYS.YEARLY.MINIMUM` | `CaplPlanSchedules_SysYearlyMinimum` | TField |  | Field to store the amount to keep the yearly minimum amount calculated by the system at the start of the year. A batch job that runs at year end updates this field. It is a no input field.This field defines the yearly minimum amount that can be withdrawn from a RRIF plan without paying taxes. |
| 11 | `CAPL.PLN.SCHED.SYS.YEARLY.MAXIMUM` | `CaplPlanSchedules_SysYearlyMaximum` | TField |  | Field to store the amount to keep the yearly maximum amount calculated by the system at the start of the year.A batch job that runs at year end updates this field.It is a no input field.This field defines the yearly maximum amount that can be withdrawn from a locked RRIF plan. |
| 12 | `CAPL.PLN.SCHED.USER.YEARLY.MINIMUM` | `CaplPlanSchedules_UserYearlyMinimum` | TField |  | This is to override the system yearly minimum. If this field is inputted by the user then the system will use this field value instead of SYS.YEARLY.MINIMUM for controls and validations. No negative amounts should be allowed.&lt;/p&gt; |
| 13 | `CAPL.PLN.SCHED.USER.YEARLY.MAXIMUM` | `CaplPlanSchedules_UserYearlyMaximum` | TField |  | This is to override the system yearly maximum. If this field is inputted by the user then the system will use this field value instead of SYS.YEARLY.MAXIMUM for controls and validations. No negative amounts should be allowed.&lt;/p&gt; |
| 14 | `CAPL.PLN.SCHED.SOY.PLAN.VALUE` | `CaplPlanSchedules_SoyPlanValue` | TField |  | Field to store the Plan value at start of year.It is a no input field.System update field. |
| 15 | `CAPL.PLN.SCHED.EOY.PLAN.VALUE` | `CaplPlanSchedules_EoyPlanValue` | TField |  | Field to store the plan value at end of year. It is a no input field.System update field. |
| 16 | `CAPL.PLN.SCHED.PAYMENT.METHOD` | `CaplPlanSchedules_PaymentMethod` | TField | Yes | Field to store the method by which the payment towards the plan to be considered.The possible values are "TRANSFER", "CHEQUE" or "EFT". This field defines the payment method; payment by crediting a non tax shelter account (TRANSFER), payment by official cheque (CHEQUE) or payment by electronic transfer (EFT). Mandatory field. |
| 17 | `CAPL.PLN.SCHED.PAY.CREDIT.ACCT` | `CaplPlanSchedules_PayCreditAcct` | TField |  | This field defines the credit account in case payment method is "TRANSFER". It should be a valid T24 account number. Link to application ACCOUNT.&lt;/p&gt;&lt;/desc&gt; |
| 18 | `CAPL.PLN.SCHED.INST.ID.NO` | `CaplPlanSchedules_InstIdNo` | TField |  |  |
| 19 | `CAPL.PLN.SCHED.TRANSIT.NO` | `CaplPlanSchedules_TransitNo` | TField |  | Field to store the transit number.Applicable - When payment method is "EFT" |
| 20 | `CAPL.PLN.SCHED.PAYOR.AC.NO` | `CaplPlanSchedules_PayorAcNo` | TField |  | Field which stores account number in the institution in field INST.ID.NO. Applicable - when payment method is "EFT" |
| 21 | `CAPL.PLN.SCHED.PAY.MAXIMUM` | `CaplPlanSchedules_PayMaximum` | TField |  | Field to Indicate, if the Maximum Amount to be paid for locking in plan or notPossible values are "YES" or "NO". Allowed to be inputted only for locked plans. not sure |
| 22 | `CAPL.PLN.SCHED.YEARLY.INSTALL.AMT` | `CaplPlanSchedules_YearlyInstallAmt` | TField |  | Field to store the amount to be paid yearly.Validation:The amount asked to be paid for the year including the excess amount. No negative amounts should be allowed. |
| 23 | `CAPL.PLN.SCHED.YEARLY.EXCESS.AMT` | `CaplPlanSchedules_YearlyExcessAmt` | TField |  | Field to store the amount which is paid in excess in addition to the yearly minimum amount.It is a no input field |
| 24 | `CAPL.PLN.SCHED.USER.EXCESS.AMT` | `CaplPlanSchedules_UserExcessAmt` | TField |  | Field to store the yearly excess amount requested by the client.Validation -No negative amounts should be allowed. |
| 25 | `CAPL.PLN.SCHED.MINIMUM.AMTS.PAID` | `CaplPlanSchedules_MinimumAmtsPaid` | TField |  |  |
| 26 | `CAPL.PLN.SCHED.EXCESS.AMTS.PAID` | `CaplPlanSchedules_ExcessAmtsPaid` | TField |  |  |
| 27 | `CAPL.PLN.SCHED.LUMPSUM.AMTS.PAID` | `CaplPlanSchedules_LumpsumAmtsPaid` | TField |  |  |
| 28 | `CAPL.PLN.SCHED.STOP.SCHED.PAYM` | `CaplPlanSchedules_StopSchedPaym` | TField |  | Field to indicate whether further scheduled payments to be stopped or not.Possible values are "YES" or "NO". This field will be used to cancel future scheduled payments. The status of cancelled scheduled payments will be "CAN". |
| 29 | `CAPL.PLN.SCHED.PAYMENT.FREQUENCY` | `CaplPlanSchedules_PaymentFrequency` | TField | Yes | Field to store the start date and frequency to create the payment schedules.This is a date and frequency type field.Mandatory field. |
| 30 | `CAPL.PLN.SCHED.PAYM.SECOND.FREQ` | `CaplPlanSchedules_PaymSecondFreq` | TField | No | This is to define a second frequency to be able to setup semi-monthly frequencies. Optional |
| 31 | `CAPL.PLN.SCHED.SCHED.DATES` | `CaplPlanSchedules_SchedDates` |  |  |  |
| 32 | `CAPL.PLN.SCHED.SCHED.RESIDENCE` | `CaplPlanSchedules_SchedResidence` |  |  |  |
| 33 | `CAPL.PLN.SCHED.SCHED.PROVINCE` | `CaplPlanSchedules_SchedProvince` |  |  |  |
| 34 | `CAPL.PLN.SCHED.SCHED.MIN.AMT` | `CaplPlanSchedules_SchedMinAmt` |  |  |  |
| 35 | `CAPL.PLN.SCHED.SCHED.EXC.AMT` | `CaplPlanSchedules_SchedExcAmt` |  |  |  |
| 36 | `CAPL.PLN.SCHED.SCHED.PROV.TAX` | `CaplPlanSchedules_SchedProvTax` |  |  |  |
| 37 | `CAPL.PLN.SCHED.SCHED.FED.TAX` | `CaplPlanSchedules_SchedFedTax` |  |  |  |
| 38 | `CAPL.PLN.SCHED.SCHED.NR.TAX` | `CaplPlanSchedules_SchedNrTax` |  |  |  |
| 39 | `CAPL.PLN.SCHED.SCHED.TOT.AMT` | `CaplPlanSchedules_SchedTotAmt` |  |  |  |
| 40 | `CAPL.PLN.SCHED.SCHED.NET.AMT` | `CaplPlanSchedules_SchedNetAmt` |  |  |  |
| 41 | `CAPL.PLN.SCHED.SCHED.TXN.NO` | `CaplPlanSchedules_SchedTxnNo` |  |  |  |
| 42 | `CAPL.PLN.SCHED.SCHED.TXN.REF` | `CaplPlanSchedules_SchedTxnRef` |  |  |  |
| 43 | `CAPL.PLN.SCHED.SCHED.STATUS` | `CaplPlanSchedules_SchedStatus` |  |  |  |
| 44 | `CAPL.PLN.SCHED.LOCAL.REF` | `CaplPlanSchedules_LocalRef` |  |  |  |
| 45 | `CAPL.PLN.SCHED.SCH.PAY.PO.BENE` | `CaplPlanSchedules_SchPayPoBene` | TField |  |  |
| 46 | `CAPL.PLN.SCHED.SCH.PAY.PO.PRODUCT` | `CaplPlanSchedules_SchPayPoProduct` | TField |  |  |
| 47 | `CAPL.PLN.SCHED.RESERVED.8` | `CaplPlanSchedules_Reserved8` | TField |  |  |
| 48 | `CAPL.PLN.SCHED.RESERVED.7` | `CaplPlanSchedules_Reserved7` | TField |  |  |
| 49 | `CAPL.PLN.SCHED.RESERVED.6` | `CaplPlanSchedules_Reserved6` | TField |  |  |
| 50 | `CAPL.PLN.SCHED.RESERVED.5` | `CaplPlanSchedules_Reserved5` | TField |  |  |
| 51 | `CAPL.PLN.SCHED.RESERVED.4` | `CaplPlanSchedules_Reserved4` | TField |  |  |
| 52 | `CAPL.PLN.SCHED.RESERVED.3` | `CaplPlanSchedules_Reserved3` | TField |  |  |
| 53 | `CAPL.PLN.SCHED.RESERVED.2` | `CaplPlanSchedules_Reserved2` | TField |  |  |
| 54 | `CAPL.PLN.SCHED.RESERVED.1` | `CaplPlanSchedules_Reserved1` | TField |  |  |
| 55 | `CAPL.PLN.SCHED.OVERRIDE` | `CaplPlanSchedules_Override` |  |  |  |
| 56 | `CAPL.PLN.SCHED.RECORD.STATUS` | `CaplPlanSchedules_RecordStatus` | String |  |  |
| 57 | `CAPL.PLN.SCHED.CURR.NO` | `CaplPlanSchedules_CurrNo` | String |  |  |
| 58 | `CAPL.PLN.SCHED.INPUTTER` | `CaplPlanSchedules_Inputter` |  |  |  |
| 59 | `CAPL.PLN.SCHED.DATE.TIME` | `CaplPlanSchedules_DateTime` |  |  |  |
| 60 | `CAPL.PLN.SCHED.AUTHORISER` | `CaplPlanSchedules_Authoriser` | String |  |  |
| 61 | `CAPL.PLN.SCHED.CO.CODE` | `CaplPlanSchedules_CoCode` | String |  |  |
| 62 | `CAPL.PLN.SCHED.DEPT.CODE` | `CaplPlanSchedules_DeptCode` | String |  |  |
| 63 | `CAPL.PLN.SCHED.AUDITOR.CODE` | `CaplPlanSchedules_AuditorCode` | String |  |  |
| 64 | `CAPL.PLN.SCHED.AUDIT.DATE.TIME` | `CaplPlanSchedules_AuditDateTime` | String |  |  |
