# EB.ACCRUAL — Table Schema

> Source: `INSERTS/I_F.EB.ACCRUAL` in `AC_Fees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.ACC.CHARGE.NO` | `EbAccrual_ChargeNo` | TField |  | A charge identifier provided by the source application. For example from generic charges on accounts it would be the IC.CHARGE key followed by the IC.CHARGE.PRODUCT |
| 2 | `EB.ACC.APPLICATION` | `EbAccrual_Application` | TField |  | The source application e.g. an account, contract or portfolio. |
| 3 | `EB.ACC.SYSTEM.ID` | `EbAccrual_SystemId` | TField |  | The system @id related to the source application and picked up from the accounting entry. |
| 4 | `EB.ACC.CUSTOMER` | `EbAccrual_Customer` | TField |  | The customer of the source contract account or portfolio. |
| 5 | `EB.ACC.PRODUCT.CATEGORY` | `EbAccrual_ProductCategory` | TField |  | The product category of the source contract account or portfolio. |
| 6 | `EB.ACC.ACCOUNT.OFFICER` | `EbAccrual_AccountOfficer` | TField |  | The department account officer from the accounting entry. |
| 7 | `EB.ACC.CO.CODE` | `EbAccrual_CoCode` | String |  | The company code of the source account or contract. Derived from the accounting entry. |
| 8 | `EB.ACC.FT.COMM` | `EbAccrual_FtComm` | TField |  | The key to the FT.COMMISSION.TYPE record used to calculate the charge amount |
| 9 | `EB.ACC.CHARGE.CCY` | `EbAccrual_ChargeCcy` | TField |  | The currency of the amount being accrued. |
| 10 | `EB.ACC.CHARGE.AMT.FCY` | `EbAccrual_ChargeAmtFcy` | TField |  | The amount to accrue or amortise in foregin currency. |
| 11 | `EB.ACC.CHARGE.AMT.LCY` | `EbAccrual_ChargeAmtLcy` | TField |  | The amount to accrue or amortise in local currency. |
| 12 | `EB.ACC.START.DATE` | `EbAccrual_StartDate` | TField |  | The start date of the accrual period. |
| 13 | `EB.ACC.END.DATE` | `EbAccrual_EndDate` | TField |  | The end date of the accrual or amortisation process. |
| 14 | `EB.ACC.PERIOD` | `EbAccrual_Period` | TField |  | This is for information only and retains the period derived from FT.COMMISSION.TYPE for applications that use this to derive the end date of the accrual or maotisation process. |
| 15 | `EB.ACC.FREQUENCY` | `EbAccrual_Frequency` | TField |  | The accrual frequency, D = daily M = monthly |
| 16 | `EB.ACC.PL.CATEGORY` | `EbAccrual_PlCategory` | TField |  | The P&amp;L category that the acruals are booked to. THis will normally correspond to the pl category on the FT.COMMISSION.TYPE record. |
| 17 | `EB.ACC.TXN.DR` | `EbAccrual_TxnDr` | TField |  | The debit transaction code derived from FT.COMMISSION.TYPE |
| 18 | `EB.ACC.TXN.CR` | `EbAccrual_TxnCr` | TField |  | The credit transaction code derived from FT.COMMISSION.TYPE |
| 19 | `EB.ACC.EB.ACCRUAL.PARAM` | `EbAccrual_EbAccrualParam` | TField |  | If non standard accruals methids are required this can be passed by the source applciation to indicate how accruals and rounding are to take place. |
| 20 | `EB.ACC.ACTION` | `EbAccrual_Action` | TField |  | Can be set by a calling application to indicate that the end.date, charge amount has changed or that accruals need to be reversed. This field is updated as 'STOP' when accruals/amortisation for the charge is stopped |
| 21 | `EB.ACC.ACCR.AMORT` | `EbAccrual_AccrAmort` | TField |  | Indicates whether the charge amount is being accrued or amortised. A indicates accrual M indicates amortisation. |
| 22 | `EB.ACC.CONTRACT.BAL.ID` | `EbAccrual_ContractBalId` | TField |  | The contract balance @id. When amortise in local is set this will be the original contract balance @id suffixed with �LOCAL ; for applications that do not interface to EB.CONTRACT.BALANCES this will be the customer debit account _LOCAL |
| 23 | `EB.ACC.SUSPENSE` | `EbAccrual_Suspense` | TField |  | Indicates that for charges being accrued on accounts that the account is currently in suspense. |
| 24 | `EB.ACC.ACCR.FROM.DATE` | `EbAccrual_AccrFromDate` |  |  |  |
| 25 | `EB.ACC.ACCR.TO.DATE` | `EbAccrual_AccrToDate` |  |  |  |
| 26 | `EB.ACC.ACCR.DAYS` | `EbAccrual_AccrDays` |  |  |  |
| 27 | `EB.ACC.ACCR.AMT` | `EbAccrual_AccrAmt` |  |  |  |
| 28 | `EB.ACC.ACCR.ACT.AMT` | `EbAccrual_AccrActAmt` |  |  |  |
| 29 | `EB.ACC.ACCR.AMT.LCY` | `EbAccrual_AccrAmtLcy` |  |  |  |
| 30 | `EB.ACC.ACCR.ACT.AMT.LCY` | `EbAccrual_AccrActAmtLcy` |  |  |  |
| 31 | `EB.ACC.OTS.AMOUNT` | `EbAccrual_OtsAmount` | TField |  | The total amount accrued to date in foreign currency, Normally the accrued amounts are split by month. |
| 32 | `EB.ACC.OTS.AMOUNT.LCY` | `EbAccrual_OtsAmountLcy` | TField |  | The total amount accrued to date in local currency. |
| 33 | `EB.ACC.ORIGINAL.RATE` | `EbAccrual_OriginalRate` | TField |  | When maortise in local is active for a foregin currency amount both the original foreign currency amount and local currency amounts are amortised, in other words the original exchange rate at teh time off booking the charge is retained. This original rate is used to populate the exhange rate field of the P&amp;L amortisation entries |
| 34 | `EB.ACC.ACC.EFF.DATE` | `EbAccrual_AccEffDate` |  |  |  |
| 35 | `EB.ACC.ACC.AMT.FCY` | `EbAccrual_AccAmtFcy` |  |  |  |
| 36 | `EB.ACC.ACC.AMT.LCY` | `EbAccrual_AccAmtLcy` |  |  |  |
| 37 | `EB.ACC.ACC.AMT.CHG` | `EbAccrual_AccAmtChg` |  |  |  |
| 38 | `EB.ACC.ACC.OTS.DATE` | `EbAccrual_AccOtsDate` | TField |  | This no-input field is part of a set which is populated by applications with a daily, non-linear accrual method such as Securities Safekeeping, Management/Advisory and Trailer Fees. The set illustrates the status of the accrual to date. This field shows the system date up to which T24 has accrued. |
| 39 | `EB.ACC.ACC.OTS.AMT` | `EbAccrual_AccOtsAmt` | TField |  | This no-input field is part of a set which is populated by applications with a daily, non-linear accrual method such as Securities Safekeeping, Management/Advisory and Trailer Fees. The set illustrates the status of the accrual to date. This field shows the rounded Foreign Currency Amount which has been accrued. |
| 40 | `EB.ACC.ACC.OTS.AMT.LCY` | `EbAccrual_AccOtsAmtLcy` | TField |  | This no-input field is part of a set which is populated by applications with a daily, non-linear accrual method such as Securities Safekeeping, Management/Advisory and Trailer Fees. The set illustrates the status of the accrual to date. This field shows the rounded Local Currency Amount which has been accrued. |
| 41 | `EB.ACC.ACCR.OTS.AMT` | `EbAccrual_AccrOtsAmt` | TField |  | This no-input field is part of a set which is populated by applications with a daily, non-linear accrual method such as Securities Safekeeping, Management/Advisory and Trailer Fees. The set illustrates the status of the accrual to date. This field shows the unrounded Foreign Currency Amount which has been accrued. |
| 42 | `EB.ACC.ACCR.OTS.AMT.LCY` | `EbAccrual_AccrOtsAmtLcy` | TField |  | This no-input field is part of a set which is populated by applications with a daily, non-linear accrual method such as Securities Safekeeping, Management/Advisory and Trailer Fees. The set illustrates the status of the accrual to date. This field shows the unrounded Local Currency Amount which has been accrued. |
| 43 | `EB.ACC.DEALER.DESK` | `EbAccrual_DealerDesk` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 44 | `EB.ACC.CRF.TYPE` | `EbAccrual_CrfType` | TField |  | Normally accruals are booked to CAL (CRF or CONSOLIDATE.ASST.LIAB) and to P&amp;L using the P&amp;L category code, i.e the CAL asset type is the same as the P&amp;L category code. For Arrangement Architecture accruals the CAL entry can be booked using an asset type that differs from the P&amp;L category code. This field will hold the asset type for AA accruals and if it is not populated the CRF accruals will be booked using the P&amp;L code. |
| 45 | `EB.ACC.AMORT.TYPE` | `EbAccrual_AmortType` | TField |  |  |
| 46 | `EB.ACC.AMORT.DIFF.PL` | `EbAccrual_AmortDiffPl` | TField |  |  |
| 47 | `EB.ACC.AMORT.DIF.CTG.ACCT` | `EbAccrual_AmortDifCtgAcct` | TField |  | This is a system updated field. Defaulted to "" or END or SPECIAL based on ic.charge application |
| 48 | `EB.ACC.AMORT.RMN.CTG.ACCT` | `EbAccrual_AmortRmnCtgAcct` | TField |  | This is a system updated field Defaulted to "" or END or SPECIAL based on ic.charge application. |
| 49 | `EB.ACC.AMORT.ADJUST` | `EbAccrual_AmortAdjust` | TField |  | This is a system updated field. Defaulted from ic.charge record. |
| 50 | `EB.ACC.NEW.AMOUNT.FCY` | `EbAccrual_NewAmountFcy` |  |  |  |
| 51 | `EB.ACC.NEW.AMOUNT.LCY` | `EbAccrual_NewAmountLcy` |  |  |  |
| 52 | `EB.ACC.NEW.END.DATE` | `EbAccrual_NewEndDate` |  |  |  |
| 53 | `EB.ACC.PREV.AMT.FCY` | `EbAccrual_PrevAmtFcy` |  |  |  |
| 54 | `EB.ACC.PREV.AMT.LCY` | `EbAccrual_PrevAmtLcy` |  |  |  |
| 55 | `EB.ACC.PREV.END.DATE` | `EbAccrual_PrevEndDate` |  |  |  |
| 56 | `EB.ACC.CHANGE.DATE` | `EbAccrual_ChangeDate` |  |  |  |
| 57 | `EB.ACC.AMORT.DIFF.PL.CAT` | `EbAccrual_AmortDiffPlCat` | TField |  |  |
| 58 | `EB.ACC.CALC.START.DATE` | `EbAccrual_CalcStartDate` | TField |  | Date Type Field Contains Accrual Calculation Start date based on the Cancel Period CALC.START.DATE = Charge Make Due Date + Cancel Period |
| 59 | `EB.ACC.CR.ACCOUNT` | `EbAccrual_CrAccount` | TField | Yes | Value in this field is system updated. Internal account is updated in this field based on the category passed by applications to core eb accrual processing When this field value is not null, amortization credits this internal account instead of P and L. TXN.DR and TXN.CR are mandatory when the profit is booked against an internal account instead of P and L account |
| 60 | `EB.ACC.ACTIVITY.NAME` | `EbAccrual_ActivityName` |  |  |  |
| 61 | `EB.ACC.ACTIVITY.FROM.DATE` | `EbAccrual_ActivityFromDate` |  |  |  |
| 62 | `EB.ACC.ACTIVITY.TO.DATE` | `EbAccrual_ActivityToDate` |  |  |  |
| 63 | `EB.ACC.ACTIVITY.AMOUNT` | `EbAccrual_ActivityAmount` |  |  |  |
| 64 | `EB.ACC.ADJUSTMENT.DATE` | `EbAccrual_AdjustmentDate` |  |  |  |
| 65 | `EB.ACC.ADJUSTMENT.AMOUNT` | `EbAccrual_AdjustmentAmount` |  |  |  |
| 66 | `EB.ACC.SPRD.ACCR.AMT` | `EbAccrual_SprdAccrAmt` |  |  |  |
| 67 | `EB.ACC.SPRD.ACCR.ACT.AMT` | `EbAccrual_SprdAccrActAmt` |  |  |  |
