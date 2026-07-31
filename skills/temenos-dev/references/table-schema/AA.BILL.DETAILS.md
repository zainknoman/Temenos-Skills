# AA.BILL.DETAILS — Table Schema

> Source: `INSERTS/I_F.AA.BILL.DETAILS` in `AA_PaymentSchedule.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.BD.ARRANGEMENT.ID` | `AaBillDetails_ArrangementId` | TField |  | This field denotes the arrangement id for which the bill is generated |
| 2 | `AA.BD.PAYMENT.DATE` | `AaBillDetails_PaymentDate` | TField |  | This field represents the payment date. Standard T24 date field |
| 3 | `AA.BD.ACTUAL.PAY.DATE` | `AaBillDetails_ActualPayDate` | TField |  | This field represent the actual payment date. The payments dates can be calendar days or can be cycled forward or backward if the payment date happens to be a holiday. This is determined by the field DATE.CONVENTION in PAYMENT.SCHEDULE property Standard T24 date field |
| 4 | `AA.BD.FINANCIAL.DATE` | `AaBillDetails_FinancialDate` | TField |  | This field represents the financial date of the payment. This field represents the value date of the accounting entries raised during the payment. This date can be cycled forward or backward to the next working day if the payment date falls on a holiday. This depends on the fields DATE.CONVENTION and DATE.ADJUSTMENT in the PAYMENT.SCHEDULE property. Standard T24 date field |
| 5 | `AA.BD.DEFER.DATE` | `AaBillDetails_DeferDate` | TField |  | The date on which customer will see this bill in his statement. This will be normally ?X? days after the original cycled date of the Bill. On this date, the actual Make due/Capitalise activity is going to happen for the bill. |
| 6 | `AA.BD.EXPIRY.DATE` | `AaBillDetails_ExpiryDate` | TField |  | Stores the date after which Tranche amount will not be available for disbursements. This gets updated for all of the disbubrsement bills for which TRANCH.END.DATE is specified. |
| 7 | `AA.BD.CURRENCY` | `AaBillDetails_Currency` | TField |  | This field represents the currency of the arrangement. |
| 8 | `AA.BD.OR.TOTAL.AMOUNT` | `AaBillDetails_OrTotalAmount` | TField |  | This field represents the total original amount of the bill . Standard T24 amount field |
| 9 | `AA.BD.OR.TOTAL.AMT.LCY` | `AaBillDetails_OrTotalAmtLcy` | TField |  | Local currency equivalent for amount in OR.TOTAL.AMT |
| 10 | `AA.BD.DELIN.OS.AMT` | `AaBillDetails_DelinOsAmt` | TField |  | This field represents the delinquent outstanding amount. If the value in the field BILL.SETTLEMENT is BILL.TOTAL, the total outstanding amount is updated in the field DELIN.OS.AMT during aging. During repayment, the repayment amount is compared with the total outstanding amount of the selected bill and the difference is updated in the field. If the repayment amount happens to be greater than or equal to total outstanding amount, the bill is deemed to be settled. |
| 11 | `AA.BD.DELIN.OS.AMT.LCY` | `AaBillDetails_DelinOsAmtLcy` | TField |  | Local currency equivalent for amount in DELIN.OS.AMT |
| 12 | `AA.BD.OS.TOTAL.AMOUNT` | `AaBillDetails_OsTotalAmount` | TField |  | This field represents the total outstanding amount of the bill .Standard T24 amount field. |
| 13 | `AA.BD.OS.TOTAL.AMT.LCY` | `AaBillDetails_OsTotalAmtLcy` | TField |  | Local currency equivalent for amount in OS.TOTAL.AMT. Currently this particular field is not applicable to be fetched in any reports. |
| 14 | `AA.BD.OS.TOTAL.ADJ.AMT` | `AaBillDetails_OsTotalAdjAmt` | TField |  | This field represents the total outstanding adjusted amount of the bill .Standard T24 amount field |
| 15 | `AA.BD.OS.TOTAL.ADJ.AMT.LCY` | `AaBillDetails_OsTotalAdjAmtLcy` | TField |  | Local currency equivalent for amount in OS.TOTAL.ADJ.AMT |
| 16 | `AA.BD.OR.TOT.AMOUNT.BNK` | `AaBillDetails_OrTotAmountBnk` | TField |  | This field represents the total BANK original amount of the bill. Standard T24 amount field. |
| 17 | `AA.BD.RESERVED.16` | `AaBillDetails_Reserved16` | TField |  |  |
| 18 | `AA.BD.OS.TOT.AMOUNT.BNK` | `AaBillDetails_OsTotAmountBnk` | TField |  | This field represents the total BANK outstanding amount of the bill .Standard T24 amount field. Standard T24 amount field. |
| 19 | `AA.BD.RESERVED.15` | `AaBillDetails_Reserved15` | TField |  |  |
| 20 | `AA.BD.OS.TOT.ADJ.AMT.BNK` | `AaBillDetails_OsTotAdjAmtBnk` | TField |  | This field represents the total BANK outstanding adjusted amount of the bill. Standard T24 amount field. |
| 21 | `AA.BD.LINKED.SKIM.PORTFOLIO.ID` | `AaBillDetails_LinkedSkimPortfolioId` |  |  |  |
| 22 | `AA.BD.PROPERTY` | `AaBillDetails_Property` |  |  |  |
| 23 | `AA.BD.OR.PROP.AMOUNT` | `AaBillDetails_OrPropAmount` |  |  |  |
| 24 | `AA.BD.OR.PROP.AMT.LCY` | `AaBillDetails_OrPropAmtLcy` |  |  |  |
| 25 | `AA.BD.OS.PROP.AMOUNT` | `AaBillDetails_OsPropAmount` |  |  |  |
| 26 | `AA.BD.OS.PROP.AMT.LCY` | `AaBillDetails_OsPropAmtLcy` |  |  |  |
| 27 | `AA.BD.OS.ADJ.PROP.AMT` | `AaBillDetails_OsAdjPropAmt` |  |  |  |
| 28 | `AA.BD.OS.ADJ.PROP.AMT.LCY` | `AaBillDetails_OsAdjPropAmtLcy` |  |  |  |
| 29 | `AA.BD.SUS.PROP.AMOUNT` | `AaBillDetails_SusPropAmount` |  |  |  |
| 30 | `AA.BD.SUS.PROP.AMT.LCY` | `AaBillDetails_SusPropAmtLcy` |  |  |  |
| 31 | `AA.BD.OR.PROP.AMT.BNK` | `AaBillDetails_OrPropAmtBnk` |  |  |  |
| 32 | `AA.BD.RESERVED.13` | `AaBillDetails_Reserved13` |  |  |  |
| 33 | `AA.BD.OS.PROP.AMT.BNK` | `AaBillDetails_OsPropAmtBnk` |  |  |  |
| 34 | `AA.BD.RESERVED.12` | `AaBillDetails_Reserved12` |  |  |  |
| 35 | `AA.BD.OS.ADJ.PROP.BNK` | `AaBillDetails_OsAdjPropBnk` |  |  |  |
| 36 | `AA.BD.RESERVED.11` | `AaBillDetails_Reserved11` |  |  |  |
| 37 | `AA.BD.SUS.PROP.BNK` | `AaBillDetails_SusPropBnk` |  |  |  |
| 38 | `AA.BD.PROP.PAYMENT.INDICATOR` | `AaBillDetails_PropPaymentIndicator` |  |  |  |
| 39 | `AA.BD.WAIVE.PROP.AMOUNT` | `AaBillDetails_WaivePropAmount` |  |  |  |
| 40 | `AA.BD.WAIVE.PROP.AMT.LCY` | `AaBillDetails_WaivePropAmtLcy` |  |  |  |
| 41 | `AA.BD.REPAY.REF` | `AaBillDetails_RepayRef` |  |  |  |
| 42 | `AA.BD.REPAY.AMOUNT` | `AaBillDetails_RepayAmount` |  |  |  |
| 43 | `AA.BD.REPAY.AMT.LCY` | `AaBillDetails_RepayAmtLcy` |  |  |  |
| 44 | `AA.BD.REPAY.BNK` | `AaBillDetails_RepayBnk` |  |  |  |
| 45 | `AA.BD.RESERVED.9` | `AaBillDetails_Reserved9` |  |  |  |
| 46 | `AA.BD.CHARGEOFF.REF` | `AaBillDetails_ChargeoffRef` |  |  |  |
| 47 | `AA.BD.CHARGEOFF.AMOUNT` | `AaBillDetails_ChargeoffAmount` |  |  |  |
| 48 | `AA.BD.ADJUST.REF` | `AaBillDetails_AdjustRef` |  |  |  |
| 49 | `AA.BD.ADJUST.AMT` | `AaBillDetails_AdjustAmt` |  |  |  |
| 50 | `AA.BD.ADJUST.AMT.LCY` | `AaBillDetails_AdjustAmtLcy` |  |  |  |
| 51 | `AA.BD.ADJ.AMT.BNK` | `AaBillDetails_AdjAmtBnk` |  |  |  |
| 52 | `AA.BD.RESERVED.8` | `AaBillDetails_Reserved8` |  |  |  |
| 53 | `AA.BD.WRITEOFF.REF` | `AaBillDetails_WriteoffRef` |  |  |  |
| 54 | `AA.BD.WRITEOFF.AMT` | `AaBillDetails_WriteoffAmt` |  |  |  |
| 55 | `AA.BD.WRITEOFF.AMT.LCY` | `AaBillDetails_WriteoffAmtLcy` |  |  |  |
| 56 | `AA.BD.WRITEOFF.BNK` | `AaBillDetails_WriteoffBnk` |  |  |  |
| 57 | `AA.BD.RESERVED.7` | `AaBillDetails_Reserved7` |  |  |  |
| 58 | `AA.BD.BILL.STATUS` | `AaBillDetails_BillStatus` |  |  |  |
| 59 | `AA.BD.BILL.ST.CHG.DT` | `AaBillDetails_BillStChgDt` |  |  |  |
| 60 | `AA.BD.PAYMENT.DATE.HIST.REF` | `AaBillDetails_BdPaymentDateHistRef` |  |  |  |
| 61 | `AA.BD.PAYMENT.DATE.HIST` | `AaBillDetails_BdPaymentDateHist` |  |  |  |
| 62 | `AA.BD.SETTLE.STATUS` | `AaBillDetails_SettleStatus` |  |  |  |
| 63 | `AA.BD.SET.ST.CHG.DT` | `AaBillDetails_SetStChgDt` |  |  |  |
| 64 | `AA.BD.RESERVED.21` | `AaBillDetails_Reserved21` |  |  |  |
| 65 | `AA.BD.RESERVED.22` | `AaBillDetails_Reserved22` |  |  |  |
| 66 | `AA.BD.AGING.STATUS` | `AaBillDetails_AgingStatus` |  |  |  |
| 67 | `AA.BD.AGING.ST.CHG.DT` | `AaBillDetails_AgingStChgDt` |  |  |  |
| 68 | `AA.BD.RESERVED.17` | `AaBillDetails_Reserved17` |  |  |  |
| 69 | `AA.BD.RESERVED.18` | `AaBillDetails_Reserved18` |  |  |  |
| 70 | `AA.BD.PAYMENT.TYPE` | `AaBillDetails_PaymentType` |  |  |  |
| 71 | `AA.BD.BILL.DATE` | `AaBillDetails_BillDate` |  |  |  |
| 72 | `AA.BD.BILL.TYPE` | `AaBillDetails_BillType` |  |  |  |
| 73 | `AA.BD.BILL.FINAL.DATE` | `AaBillDetails_BillFinalDate` |  |  |  |
| 74 | `AA.BD.PAYMENT.METHOD` | `AaBillDetails_PaymentMethod` |  |  |  |
| 75 | `AA.BD.PAYMENT.AMOUNT` | `AaBillDetails_PaymentAmount` |  |  |  |
| 76 | `AA.BD.PAYMENT.AMT.LCY` | `AaBillDetails_PaymentAmtLcy` |  |  |  |
| 77 | `AA.BD.PAYMENT.AMT.BNK` | `AaBillDetails_PaymentAmtBnk` |  |  |  |
| 78 | `AA.BD.RESERVED.6` | `AaBillDetails_Reserved6` |  |  |  |
| 79 | `AA.BD.PAY.PROPERTY` | `AaBillDetails_PayProperty` |  |  |  |
| 80 | `AA.BD.OR.PR.AMT` | `AaBillDetails_OrPrAmt` |  |  |  |
| 81 | `AA.BD.OR.PR.AMT.LCY` | `AaBillDetails_OrPrAmtLcy` |  |  |  |
| 82 | `AA.BD.OS.PR.AMT` | `AaBillDetails_OsPrAmt` |  |  |  |
| 83 | `AA.BD.OS.PR.AMT.LCY` | `AaBillDetails_OsPrAmtLcy` |  |  |  |
| 84 | `AA.BD.SUS.PR.AMT` | `AaBillDetails_SusPrAmt` |  |  |  |
| 85 | `AA.BD.SUS.PR.AMT.LCY` | `AaBillDetails_SusPrAmtLcy` |  |  |  |
| 86 | `AA.BD.OS.AD.PR.AMT` | `AaBillDetails_OsAdPrAmt` |  |  |  |
| 87 | `AA.BD.OS.AD.PR.AMT.LCY` | `AaBillDetails_OsAdPrAmtLcy` |  |  |  |
| 88 | `AA.BD.OR.PR.BNK` | `AaBillDetails_OrPrBnk` |  |  |  |
| 89 | `AA.BD.RESERVED.5` | `AaBillDetails_Reserved5` |  |  |  |
| 90 | `AA.BD.OS.PR.BNK` | `AaBillDetails_OsPrBnk` |  |  |  |
| 91 | `AA.BD.RESERVED.3` | `AaBillDetails_Reserved3` |  |  |  |
| 92 | `AA.BD.SUS.PR.BNK` | `AaBillDetails_SusPrBnk` |  |  |  |
| 93 | `AA.BD.RESERVED.2` | `AaBillDetails_Reserved2` |  |  |  |
| 94 | `AA.BD.OS.ADJ.PR.BNK` | `AaBillDetails_OsAdjPrBnk` |  |  |  |
| 95 | `AA.BD.RESERVED.1` | `AaBillDetails_Reserved1` |  |  |  |
| 96 | `AA.BD.WAIVE.PR.AMT` | `AaBillDetails_WaivePrAmt` |  |  |  |
| 97 | `AA.BD.WAIVE.PR.AMT.LCY` | `AaBillDetails_WaivePrAmtLcy` |  |  |  |
| 98 | `AA.BD.INFO.PAY.TYPE` | `AaBillDetails_InfoPayType` |  |  |  |
| 99 | `AA.BD.INFO.PAY.PRP` | `AaBillDetails_InfoPayPrp` |  |  |  |
| 100 | `AA.BD.INFO.PR.AMT` | `AaBillDetails_InfoPrAmt` |  |  |  |
| 101 | `AA.BD.INFO.PR.AMT.LCY` | `AaBillDetails_InfoPrAmtLcy` |  |  |  |
| 102 | `AA.BD.ADVANCE.PAYMENT` | `AaBillDetails_AdvancePayment` | TField |  | This field represents the advance payment made on the arrangement |
| 103 | `AA.BD.LAST.UPDATE.DATE` | `AaBillDetails_LastUpdateDate` | TField |  | This field represents the last date or the recent date when the bill was last updated. Standard T24 date field |
| 104 | `AA.BD.DELIN.REP.REF` | `AaBillDetails_DelinRepRef` |  |  |  |
| 105 | `AA.BD.DELIN.AMT` | `AaBillDetails_DelinAmt` |  |  |  |
| 106 | `AA.BD.AGING.REF` | `AaBillDetails_AgingRef` |  |  |  |
| 107 | `AA.BD.ADVANCE.BILL` | `AaBillDetails_AdvanceBill` | TField |  | This field denotes if this bill is raised through a advance payment, this field can hold value &apos;YES&apos;. |
| 108 | `AA.BD.DUE.REFERENCE` | `AaBillDetails_DueReference` | TField |  | This field denotes the make due reference. |
| 109 | `AA.BD.DEFER.REFERENCE` | `AaBillDetails_DeferReference` | TField |  | The arrangement activity reference of the DEFER.MAKEDUE/DEFER.CAPITALISE activity that happened on the original cycled date. |
| 110 | `AA.BD.PAYMENT.INDICATOR` | `AaBillDetails_PaymentIndicator` | TField |  | This field is updated with either credit or debit indicator based on the property of the bill |
| 111 | `AA.BD.CAPTURE.PROPERTY` | `AaBillDetails_CaptureProperty` |  |  |  |
| 112 | `AA.BD.CAPTURE.PROPERTY.AMT` | `AaBillDetails_CapturePropertyAmt` |  |  |  |
| 113 | `AA.BD.MASTER.ARR.ID` | `AaBillDetails_MasterArrId` | TField |  | Non-Financila arrangement Standard T24 date field |
| 114 | `AA.BD.MASTER.ISSUE.BILL.REF` | `AaBillDetails_MasterIssueBillRef` | TField |  | Non-Financial arrangement issue bill activity reference. It is AA.ARRANGMENT.ACTIVITY ID |
| 115 | `AA.BD.MASTER.DEFER.REF` | `AaBillDetails_MasterDeferRef` | TField |  | Non-Financial arrangement defer activity reference. It is AA.ARRANGMENT.ACTIVITY ID |
| 116 | `AA.BD.MASTER.DUE.REF` | `AaBillDetails_MasterDueRef` | TField |  | Non-Financial arrangement due activity reference. It is AA.ARRANGMENT.ACTIVITY ID |
| 117 | `AA.BD.BILL.PROPERTY` | `AaBillDetails_BillProperty` |  |  |  |
| 118 | `AA.BD.CONSOL.PROPERTY` | `AaBillDetails_ConsolProperty` |  |  |  |
| 119 | `AA.BD.CONSOL.PROP.AMT` | `AaBillDetails_ConsolPropAmt` |  |  |  |
| 120 | `AA.BD.LINKED.ARR.ID` | `AaBillDetails_LinkedArrId` |  |  |  |
| 121 | `AA.BD.LINKED.BILL.ID` | `AaBillDetails_LinkedBillId` |  |  |  |
| 122 | `AA.BD.LINKED.PARTICIPANTS` | `AaBillDetails_LinkedParticipants` |  |  |  |
| 123 | `AA.BD.FINALISE.DATE` | `AaBillDetails_FinaliseDate` | TField |  | Holds the finalise date on which a bill needs to be finalised. When the finalisation date is reached,system does not allow changes to the total bill amount |
| 124 | `AA.BD.FINALISE.REFERENCE` | `AaBillDetails_FinaliseReference` | TField |  | This field denotes the finalise reference when a bill is finalised |
| 125 | `AA.BD.PARTICIPANT.INDICATOR` | `AaBillDetails_ParticipantIndicator` | TField |  | This field identifies whether the overall bill has a debit or credit indicator. For E.g., when there is a charge calculated for 300 USD where the sum of the participant share is 450 USD, greater than the calculated charge, the excess amount is considered as skim, i.e. 150 USD. When the skim amount is greater than the book's share, then the overall indicator is considered as CREDIT. In a similar case, if the skim amount is lesser than the book's share, then the overall indicator is considered as DEBIT. |
| 126 | `AA.BD.POS.PROP.AMOUNT` | `AaBillDetails_PosPropAmount` |  |  |  |
| 127 | `AA.BD.NEG.PROP.AMOUNT` | `AaBillDetails_NegPropAmount` |  |  |  |
| 128 | `AA.BD.PROMOTIONS.ARR.ID` | `AaBillDetails_PromotionsArrId` | TField |  |  |
| 129 | `AA.BD.NOTICE.REFERENCE` | `AaBillDetails_NoticeReference` | TField |  | Field to retain the link to the notice withdrawal bill during replay of change/cancel activity. |
| 130 | `AA.BD.OR.TOTAL.AMOUNT.REC` | `AaBillDetails_OrTotalAmountRec` | TField |  |  |
| 131 | `AA.BD.OR.TOTAL.AMT.REC.LCY` | `AaBillDetails_OrTotalAmtRecLcy` | TField |  |  |
| 132 | `AA.BD.OS.TOTAL.AMOUNT.REC` | `AaBillDetails_OsTotalAmountRec` | TField |  |  |
| 133 | `AA.BD.OS.TOTAL.AMT.REC.LCY` | `AaBillDetails_OsTotalAmtRecLcy` | TField |  |  |
| 134 | `AA.BD.OS.TOTAL.ADJ.AMT.REC` | `AaBillDetails_OsTotalAdjAmtRec` | TField |  |  |
| 135 | `AA.BD.OS.TOTAL.ADJ.AMT.REC.LCY` | `AaBillDetails_OsTotalAdjAmtRecLcy` | TField |  |  |
| 136 | `AA.BD.OR.PROP.AMOUNT.REC` | `AaBillDetails_OrPropAmountRec` |  |  |  |
| 137 | `AA.BD.OR.PROP.AMT.REC.LCY` | `AaBillDetails_OrPropAmtRecLcy` |  |  |  |
| 138 | `AA.BD.OS.PROP.AMOUNT.REC` | `AaBillDetails_OsPropAmountRec` |  |  |  |
| 139 | `AA.BD.OS.PROP.AMT.REC.LCY` | `AaBillDetails_OsPropAmtRecLcy` |  |  |  |
| 140 | `AA.BD.OS.ADJ.PROP.AMT.REC` | `AaBillDetails_OsAdjPropAmtRec` |  |  |  |
| 141 | `AA.BD.OS.ADJ.PROP.AMT.REC.LCY` | `AaBillDetails_OsAdjPropAmtRecLcy` |  |  |  |
| 142 | `AA.BD.SUS.PROP.AMOUNT.REC` | `AaBillDetails_SusPropAmountRec` |  |  |  |
| 143 | `AA.BD.SUS.PROP.AMT.REC.LCY` | `AaBillDetails_SusPropAmtRecLcy` |  |  |  |
| 144 | `AA.BD.WAIVE.PROP.AMOUNT.REC` | `AaBillDetails_WaivePropAmountRec` |  |  |  |
| 145 | `AA.BD.WAIVE.PROP.AMT.REC.LCY` | `AaBillDetails_WaivePropAmtRecLcy` |  |  |  |
| 146 | `AA.BD.RESERVED.23` | `AaBillDetails_Reserved23` |  |  |  |
| 147 | `AA.BD.RESERVED.24` | `AaBillDetails_Reserved24` |  |  |  |
| 148 | `AA.BD.RESERVED.25` | `AaBillDetails_Reserved25` |  |  |  |
| 149 | `AA.BD.RESERVED.26` | `AaBillDetails_Reserved26` |  |  |  |
| 150 | `AA.BD.RESERVED.27` | `AaBillDetails_Reserved27` |  |  |  |
| 151 | `AA.BD.RESERVED.28` | `AaBillDetails_Reserved28` |  |  |  |
| 152 | `AA.BD.PAYMENT.AMOUNT.REC` | `AaBillDetails_PaymentAmountRec` |  |  |  |
| 153 | `AA.BD.PAYMENT.AMT.REC.LCY` | `AaBillDetails_PaymentAmtRecLcy` |  |  |  |
| 154 | `AA.BD.OR.PR.AMT.REC` | `AaBillDetails_OrPrAmtRec` |  |  |  |
| 155 | `AA.BD.OR.PR.AMT.REC.LCY` | `AaBillDetails_OrPrAmtRecLcy` |  |  |  |
| 156 | `AA.BD.OS.PR.AMT.REC` | `AaBillDetails_OsPrAmtRec` |  |  |  |
| 157 | `AA.BD.OS.PR.AMT.REC.LCY` | `AaBillDetails_OsPrAmtRecLcy` |  |  |  |
| 158 | `AA.BD.SUS.PR.AMT.REC` | `AaBillDetails_SusPrAmtRec` |  |  |  |
| 159 | `AA.BD.SUS.PR.AMT.REC.LCY` | `AaBillDetails_SusPrAmtRecLcy` |  |  |  |
| 160 | `AA.BD.OS.AD.PR.AMT.REC` | `AaBillDetails_OsAdPrAmtRec` |  |  |  |
| 161 | `AA.BD.OS.AD.PR.AMT.REC.LCY` | `AaBillDetails_OsAdPrAmtRecLcy` |  |  |  |
| 162 | `AA.BD.WAIVE.PR.AMT.REC` | `AaBillDetails_WaivePrAmtRec` |  |  |  |
| 163 | `AA.BD.WAIVE.PR.AMT.REC.LCY` | `AaBillDetails_WaivePrAmtRecLcy` |  |  |  |
| 164 | `AA.BD.REPAY.REF.REC` | `AaBillDetails_RepayRefRec` |  |  |  |
| 165 | `AA.BD.REPAY.AMOUNT.REC` | `AaBillDetails_RepayAmountRec` |  |  |  |
| 166 | `AA.BD.REPAY.AMT.REC.LCY` | `AaBillDetails_RepayAmtRecLcy` |  |  |  |
| 167 | `AA.BD.ADJUST.REF.REC` | `AaBillDetails_BdAdjustRefRec` |  |  |  |
| 168 | `AA.BD.ADJUST.AMT.REC` | `AaBillDetails_AdjustAmtRec` |  |  |  |
| 169 | `AA.BD.ADJUST.AMT.REC.LCY` | `AaBillDetails_AdjustAmtRecLcy` |  |  |  |
| 170 | `AA.BD.WRITEOFF.REF.REC` | `AaBillDetails_BdWriteoffRefRec` |  |  |  |
| 171 | `AA.BD.WRITEOFF.AMT.REC` | `AaBillDetails_WriteoffAmtRec` |  |  |  |
| 172 | `AA.BD.WRITEOFF.AMT.REC.LCY` | `AaBillDetails_WriteoffAmtRecLcy` |  |  |  |
