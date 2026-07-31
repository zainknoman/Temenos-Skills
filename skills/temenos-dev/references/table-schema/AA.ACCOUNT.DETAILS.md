# AA.ACCOUNT.DETAILS — Table Schema

> Source: `INSERTS/I_F.AA.ACCOUNT.DETAILS` in `AA_PaymentSchedule.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.AD.CONTRACT.DATE` | `AaAccountDetails_ContractDate` |  |  |  |
| 2 | `AA.AD.VALUE.DATE` | `AaAccountDetails_ValueDate` | TField | Yes | This field identifies the start date of the Arrangement contract and is updated only for Account based products, i.e. where Product Line constituents Account property class as mandatory. The effective date of the "New" arrangement activity would be updated as start date of the Arrangement in this field. |
| 3 | `AA.AD.START.DATE` | `AaAccountDetails_StartDate` | TField |  | This Field denotes the drawdown date of the arrangement. This Field is updated when a first disbursement activity is triggered for the lending product line. |
| 4 | `AA.AD.DRAWDOWN.END.DATE` | `AaAccountDetails_DrawdownEndDate` | TField |  | Reserved for future use. |
| 5 | `AA.AD.PAYMENT.START.DATE` | `AaAccountDetails_PaymentStartDate` | TField |  | This field identifies the first payment date for the Arrangement contract based on the definition in Payment Schedule property class. |
| 6 | `AA.AD.MATURITY.DATE` | `AaAccountDetails_MaturityDate` | TField |  |  |
| 7 | `AA.AD.ARR.AGE.STATUS` | `AaAccountDetails_ArrAgeStatus` | TField |  | This field identifies the overall deliquent status of an Arrangement contract. It would indicate the worst status of all the bills. |
| 8 | `AA.AD.RENEWAL.DATE` | `AaAccountDetails_RenewalDate` | TField |  |  |
| 9 | `AA.AD.COOLING.DATE` | `AaAccountDetails_CoolingDate` | TField |  |  |
| 10 | `AA.AD.CANCEL.DATE` | `AaAccountDetails_CancelDate` | TField |  | The date on which the contract would get cancelled. Linked to the CANCEL.PERIOD stated in TERM.AMOUNT property. When the deposit is not funded/loan is not disbursed before this date, then the arrangement would be automatically cancelled. Would not be populated if CANCEL.PERIOD is not used. |
| 11 | `AA.AD.BASE.DATE` | `AaAccountDetails_BaseDate` | TField |  | This field denotes the Base date of the arrangement. This field is updated when a new arrangement is created for the lending product line. |
| 12 | `AA.AD.BILL.PAY.DATE` | `AaAccountDetails_BillPayDate` |  |  |  |
| 13 | `AA.AD.BILL.ID` | `AaAccountDetails_BillId` |  |  |  |
| 14 | `AA.AD.ACTIVITY.REF` | `AaAccountDetails_ActivityRef` |  |  |  |
| 15 | `AA.AD.BILL.DATE` | `AaAccountDetails_BillDate` |  |  |  |
| 16 | `AA.AD.DEFER.DATE` | `AaAccountDetails_DeferDate` |  |  |  |
| 17 | `AA.AD.EXPIRY.DATE` | `AaAccountDetails_ExpiryDate` |  |  |  |
| 18 | `AA.AD.BILL.TYPE` | `AaAccountDetails_BillType` |  |  |  |
| 19 | `AA.AD.PAY.METHOD` | `AaAccountDetails_PayMethod` |  |  |  |
| 20 | `AA.AD.BILL.STATUS` | `AaAccountDetails_BillStatus` |  |  |  |
| 21 | `AA.AD.SET.STATUS` | `AaAccountDetails_SetStatus` |  |  |  |
| 22 | `AA.AD.AGING.STATUS` | `AaAccountDetails_AgingStatus` |  |  |  |
| 23 | `AA.AD.NXT.AGE.DATE` | `AaAccountDetails_NxtAgeDate` |  |  |  |
| 24 | `AA.AD.CHASER.DATE` | `AaAccountDetails_ChaserDate` |  |  |  |
| 25 | `AA.AD.ALL.AGE.STATUS` | `AaAccountDetails_AllAgeStatus` | TField |  | This field is set to "YES" when the aging status of a bill results in setting aging status of all the bills to this status. In Overdue property class if AGE.ALL.BILLS is flagged for an associated status, on reaching this status for a bill the status of all the bills would be moved to this status and ALL.AGE.STATUS would be set to "YES" to indicate all the bills moved status because of AGE.ALL.BILLS setting and not through normal deliquent processing. |
| 26 | `AA.AD.SUSPENDED` | `AaAccountDetails_Suspended` | TField |  | This field is updated as "YES" when the contract reaches the deliquent status when the interest accrued / earned on the contract is to be suspended, i.e. P&amp;L reversed and posted as suspense. |
| 27 | `AA.AD.REPORT.END.DATE` | `AaAccountDetails_ReportEndDate` | TField |  | REPORT.END.DATE This field will be updated by the system in the following order: 1) If Renewal Date (CHANGE.DATE or converted CHANGE.PERIOD of CHANGE.PRODUCT property class) is present then this value will be used. 2) If MATURITY.DATE is present then this value will be used. 3) If neither of the above then a NULL value will be assigned indicating a call notice contract. For reporting purpose this field will be utilized in the building of CONSOLIDATE.ASST.LIAB keys. |
| 28 | `AA.AD.SCHEDULE.TYPE` | `AaAccountDetails_ScheduleType` |  |  |  |
| 29 | `AA.AD.NUM.PAYMENTS` | `AaAccountDetails_NumPayments` |  |  |  |
| 30 | `AA.AD.PAYMENT.DATE` | `AaAccountDetails_PaymentDate` |  |  |  |
| 31 | `AA.AD.ACT.PAY.DATE` | `AaAccountDetails_ActPayDate` |  |  |  |
| 32 | `AA.AD.FIN.PAY.DATE` | `AaAccountDetails_FinPayDate` |  |  |  |
| 33 | `AA.AD.INTERIM.DATE` | `AaAccountDetails_InterimDate` |  |  |  |
| 34 | `AA.AD.TAKEOVER.ARR` | `AaAccountDetails_TakeoverArr` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 35 | `AA.AD.REPAY.REFERENCE` | `AaAccountDetails_RepayReference` |  |  |  |
| 36 | `AA.AD.RPY.BILL.ID` | `AaAccountDetails_RpyBillId` |  |  |  |
| 37 | `AA.AD.RPY.BILL.ID.BANK` | `AaAccountDetails_RpyBillIdBank` |  |  |  |
| 38 | `AA.AD.SUSP.STATUS` | `AaAccountDetails_SuspStatus` |  |  |  |
| 39 | `AA.AD.SUSP.DATE` | `AaAccountDetails_SuspDate` |  |  |  |
| 40 | `AA.AD.LAST.RENEW.DATE` | `AaAccountDetails_LastRenewDate` |  |  |  |
| 41 | `AA.AD.PAYMENT.END.DATE` | `AaAccountDetails_PaymentEndDate` | TField |  | The final date on which scheduled payments happen. This is computed from the Payment schedule definition of the frequency and is also governed by the tenor of the contract. Would not be populated if schedules are not involved. |
| 42 | `AA.AD.BILLS.SETTLED.CNT` | `AaAccountDetails_BillsSettledCnt` | TField |  | This field denotes the number of settled bills (Bills with BILL.STATUS = SETTLED and CAPITALISE) and it is used by AA bill processing to trigger archival process. The number of bills to be maintained in live file (AA.ACCOUNT.DETAILS and AA.BILL.DETAILS) has to be mentioned in I_AA.ARCHIVE.COMMON. When the bills settled count breaches twice the threshold value, system will trigger archival process. This count would be incremented for each bill that gets SETTLED or CAPITALISED and would be recalculated if bills are archived. |
| 43 | `AA.AD.STATIC.UPDATE` | `AaAccountDetails_StaticUpdate` | TField |  | This field is updated when system process any static changes |
| 44 | `AA.AD.FACILITY.TYPE` | `AaAccountDetails_FacilityType` | TField |  |  |
| 45 | `AA.AD.RPY.REFERENCE` | `AaAccountDetails_RpyReference` |  |  |  |
| 46 | `AA.AD.RESERVED.4` | `AaAccountDetails_Reserved4` |  |  |  |
| 47 | `AA.AD.RESERVED.3` | `AaAccountDetails_Reserved3` |  |  |  |
| 48 | `AA.AD.RPY.ACTUAL.DATE` | `AaAccountDetails_RpyActualDate` |  |  |  |
| 49 | `AA.AD.WOF.ACTIVITY.REF` | `AaAccountDetails_WofActivityRef` |  |  |  |
| 50 | `AA.AD.WOF.BILL.REF` | `AaAccountDetails_WofBillRef` |  |  |  |
| 51 | `AA.AD.WOF.PROPERTY` | `AaAccountDetails_WofProperty` |  |  |  |
| 52 | `AA.AD.WOF.BALANCE.NAME` | `AaAccountDetails_WofBalanceName` |  |  |  |
| 53 | `AA.AD.WOF.AMOUNT` | `AaAccountDetails_WofAmount` |  |  |  |
| 54 | `AA.AD.CHARGEOFF.DATE` | `AaAccountDetails_ChargeoffDate` | TField |  | This field denotes the charge off date of the arrangement. It is updated when user triggers the increase charge off activity. It will be effective date of activity. |
| 55 | `AA.AD.CHARGEOFF.REFERENCE` | `AaAccountDetails_ChargeoffReference` |  |  |  |
| 56 | `AA.AD.CHARGEOFF.BILL.ID` | `AaAccountDetails_ChargeoffBillId` |  |  |  |
| 57 | `AA.AD.ADJUST.INT.PROP` | `AaAccountDetails_AdjustIntProp` |  |  |  |
| 58 | `AA.AD.CHARGEOFF.TYPE` | `AaAccountDetails_ChargeoffType` | TField |  | This field identifies the date when the next chaser advice is scheduled for the bill associated. |
| 59 | `AA.AD.OVERDRAFT.STATUS` | `AaAccountDetails_OverdraftStatus` | TField |  | This field is updated with the current overdraft status of the arrangement |
| 60 | `AA.AD.RESERVED.OD` | `AaAccountDetails_ReservedOd` | TField |  |  |
| 61 | `AA.AD.PRIMARY.OD.DATE` | `AaAccountDetails_PrimaryOdDate` | TField |  | This field is updated with the date arrangement contract moved to overdraft |
| 62 | `AA.AD.ACTUAL.RENEW.DATE` | `AaAccountDetails_ActualRenewDate` |  |  |  |
| 63 | `AA.AD.HOL.PAYMENT.TYPE` | `AaAccountDetails_HolPaymentType` |  |  |  |
| 64 | `AA.AD.HOL.BILL.TYPE` | `AaAccountDetails_HolBillType` |  |  |  |
| 65 | `AA.AD.HOL.START.DATE` | `AaAccountDetails_HolStartDate` |  |  |  |
| 66 | `AA.AD.HOLIDAY.DATE` | `AaAccountDetails_HolidayDate` |  |  |  |
| 67 | `AA.AD.HOL.NEW.PAYMENT.AMOUNT` | `AaAccountDetails_HolNewPaymentAmount` |  |  |  |
| 68 | `AA.AD.ORG.PAYMENT.AMOUNT` | `AaAccountDetails_OrgPaymentAmount` |  |  |  |
| 69 | `AA.AD.ONLINE.CAPITALISE` | `AaAccountDetails_OnlineCapitalise` | TField |  | This field would get update whenever we set or reset the field ONLINE.CAPITALISE in PAYMENT.SCHEDULE condition. When this field is set to YES, capitalise bill would be created online as part of online service. However the accounting for the capitalise amount would still be raised during scheduled capitalise activity processing during COB. |
| 70 | `AA.AD.ARR.DORMANCY.STATUS` | `AaAccountDetails_ArrDormancyStatus` | TField |  | This field contains the current dormancy status of the arrangement |
| 71 | `AA.AD.DORMANCY.STATUS` | `AaAccountDetails_DormancyStatus` |  |  |  |
| 72 | `AA.AD.DORMANCY.DATE` | `AaAccountDetails_DormancyDate` |  |  |  |
| 73 | `AA.AD.DORMANCY.PROCESS` | `AaAccountDetails_DormancyProcess` |  |  |  |
| 74 | `AA.AD.INT.STATEMENT.TYPE` | `AaAccountDetails_IntStatementType` |  |  |  |
| 75 | `AA.AD.LAST.STATEMENT.DATE` | `AaAccountDetails_LastStatementDate` |  |  |  |
| 76 | `AA.AD.PENDING.ADJUSTMENT.DATE` | `AaAccountDetails_PendingAdjustmentDate` | TField |  | If any backdated transactions having ADJUSTMENT.OPTION in accounting property class as NEXT.CAP is triggered, reverse and replay will not happen online instead we store the date in this field and during next capitalisation date, reverse and replay will happen from this Pending adjustment date. When multiple adjustments are there then this field will hold the least adjustment date. |
| 77 | `AA.AD.BRANCH` | `AaAccountDetails_Branch` | TField |  | Shows the branch that this arrangement belongs to. |
| 78 | `AA.AD.LINE.OF.BUSINESS` | `AaAccountDetails_LineOfBusiness` | TField |  | Represents the business category that product belongs to. |
| 79 | `AA.AD.SUSPENDED.BY` | `AaAccountDetails_SuspendedBy` |  |  |  |
| 80 | `AA.AD.DEFER.CLOSURE.DATE` | `AaAccountDetails_DeferClosureDate` | TField |  |  |
| 81 | `AA.AD.FULL.CHARGEOFF` | `AaAccountDetails_FullChargeoff` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 82 | `AA.AD.BASE.CCY.RATE` | `AaAccountDetails_BaseCcyRate` | TField |  | Field to capture the rate with which conversion happens for a Drawing of cross-currency. The value is updated when the currency of a Drawing is different from that of the Facility. This is the rate used to perform conversion for any activity that updates Facility utilisation. This field does not get updated when the currencies of drawing and facility are same. |
| 83 | `AA.AD.BASE.CCY.AMOUNT` | `AaAccountDetails_BaseCcyAmount` | TField |  | Field to capture the utilisation amount of the Drawings in Facility currency. This field gets updated as and when a utilisation update happens for a Facility. This field gets updated in the following way: 1. For UPDATE.COMMT.ON.CAP as Current And Overdraw, this field records the sum of UTL and OVD TERM.AMOUNT balances in Facility Currency. 2. For UPDATE.COMMT.ON.CAP as Overdraw, this field records the UTL TERM.AMOUNT balance alone in Facility currency. This field does not get updated when the currencies of drawing and facility are same. |
| 84 | `AA.AD.CUR.RESTRUCTURE.STATUS` | `AaAccountDetails_CurRestructureStatus` | TField |  | The date on which customer will see this bill in his statement. This will be normally 'X' days after the original cycled date of the Bill. On this date, the actual Make due/Capitalise activity is going to happen for the bill. |
| 85 | `AA.AD.RISK.STAGE` | `AaAccountDetails_RiskStage` | TField |  | This field specifies the current stage of the overdraft accounts and Arrangement Loans under Ifrs9 Accounting. This field holds value as 1 or 2 or 3 as updated in EB.CASHFLOW record Here 1,2,3 stage classification is done based on the credit risk involved Initially contract will be kept under stage 1, as the credit risk increases contract is moved to stage 2 and on further increase in credit risk moves the contract to stage 3 This field gets updated on configuring RISK.STAGE as a key variable in CONSOLIDATE.COND and running IFRS.CONTRACT.STAGE.UPDATE job. IFRS.CONTRACT.STAGE.UPDATE is an Adhoc job run in between AA.EOD.PROCESS and AA.SOD.PROCESS . |
| 86 | `AA.AD.RULE.EFFECTIVE.DATE` | `AaAccountDetails_RuleEffectiveDate` |  |  |  |
| 87 | `AA.AD.RULE.STATUS.TYPE` | `AaAccountDetails_RuleStatusType` |  |  |  |
| 88 | `AA.AD.RULE.STATUS` | `AaAccountDetails_RuleStatus` |  |  |  |
| 89 | `AA.AD.RESERVED.14` | `AaAccountDetails_Reserved14` |  |  |  |
| 90 | `AA.AD.RESERVED.13` | `AaAccountDetails_Reserved13` |  |  |  |
| 91 | `AA.AD.RESERVED.12` | `AaAccountDetails_Reserved12` |  |  |  |
| 92 | `AA.AD.RESERVED.11` | `AaAccountDetails_Reserved11` |  |  |  |
| 93 | `AA.AD.PROPERTY` | `AaAccountDetails_Property` |  |  |  |
| 94 | `AA.AD.ACTION` | `AaAccountDetails_Action` |  |  |  |
| 95 | `AA.AD.RESERVED.10` | `AaAccountDetails_Reserved10` |  |  |  |
| 96 | `AA.AD.EFFECTIVE.DATE` | `AaAccountDetails_EffectiveDate` |  |  |  |
| 97 | `AA.AD.RESERVED.9` | `AaAccountDetails_Reserved9` |  |  |  |
| 98 | `AA.AD.RESERVED.8` | `AaAccountDetails_Reserved8` |  |  |  |
| 99 | `AA.AD.RESERVED.7` | `AaAccountDetails_Reserved7` |  |  |  |
| 100 | `AA.AD.RESERVED.6` | `AaAccountDetails_Reserved6` |  |  |  |
| 101 | `AA.AD.BASE.CCY.OVD.AMOUNT` | `AaAccountDetails_BaseCcyOvdAmount` | TField |  | Field to capture the over-utilisation amount of the Drawings in Facility currency. This gets updated as and when a utilisation update happens for a Facility. For UPDATE.COMMT.ON.CAP as Overdraw, this field records the OVD TERM.AMOUNT balance alone in Facility currency. This field does not get updated when the currencies of drawing and facility are same. |
| 102 | `AA.AD.COMMT.EXPIRY.DATE` | `AaAccountDetails_CommtExpiryDate` | TField |  | This field denotes the expiry date of the arrangement. It represents the last date after which new drawings cannot be created under the facility or further disbursement cannot be made under lending arrangements, including Forward dated activities. When the Expiry date is a relative date, it gets adjusted with the change in the respective base date. |
| 103 | `AA.AD.COMMITMENT.STATUS` | `AaAccountDetails_CommitmentStatus` | TField |  | This field specifies the commitment status of an arrangement. It gets updated as 'EXPIRED' after the commitment expiry date. |
| 104 | `AA.AD.MANUAL.AGEING` | `AaAccountDetails_ManualAgeing` | TField |  |  |
| 105 | `AA.AD.MANUAL.AGE.BILL.TYPE` | `AaAccountDetails_ManualAgeBillType` |  |  |  |
| 106 | `AA.AD.RFR.INT.PROPERTIES` | `AaAccountDetails_RfrIntProperties` |  |  |  |
| 107 | `AA.AD.BASE.CCY.TOT.AMOUNT` | `AaAccountDetails_BaseCcyTotAmount` | TField |  | This field specifies the total commitment amount of the Facility in Deal currency. This gets updated as and when a total commitment update activity happens for a deal. This field does not get updated for facility in same currency as that of a deal. |
| 108 | `AA.AD.BASE.CCY.CUR.AMOUNT` | `AaAccountDetails_BaseCcyCurAmount` | TField |  | This field specifies the available commitment amount of the Facility in Deal currency. This gets updated as and when a total commitment update activity happens for a deal. This field does not get updated for facility in same currency as that of a deal. |
| 109 | `AA.AD.OFFER.DATE` | `AaAccountDetails_OfferDate` | TField |  | The field contains the date on which the offer was created. |
| 110 | `AA.AD.AGE.EVENT.DATE` | `AaAccountDetails_AgeEventDate` |  |  |  |
| 111 | `AA.AD.AGE.EVENT.STATUS` | `AaAccountDetails_AgeEventStatus` |  |  |  |
| 112 | `AA.AD.AGE.ALL.DATE` | `AaAccountDetails_AgeAllDate` |  |  |  |
| 113 | `AA.AD.AGE.ALL.BILL.TYPE` | `AaAccountDetails_AgeAllBillType` |  |  |  |
| 114 | `AA.AD.AGE.ALL.STATUS` | `AaAccountDetails_AgeAllStatus` |  |  |  |
| 115 | `AA.AD.ROLLOVER.STATUS` | `AaAccountDetails_RolloverStatus` | TField |  | This field specifies the status of the rollover of the source as a result of the splits/merges/rollover activity. Stored Values are : PENDING - The arrangement is captured as the source and the capture activity is authorized but not yet processed by the service BNK/AA.SPLITS.MERGES.SERVICE INITIATED � The source is processed by the service BNK/AA.SPLITS.MERGES.SERVICE COMPLETED � The rollover of the source is completed and the arrangement is settled |
| 116 | `AA.AD.CONTRACT.PERIOD` | `AaAccountDetails_ContractPeriod` | TField |  |  |
| 117 | `AA.AD.RENEWAL.PERIOD` | `AaAccountDetails_RenewalPeriod` | TField |  | The field uniquely identifies the repayment references made against the Arrangement contract, it is maintained as the combination of activity reference (Id) and the activity effective date. |
| 118 | `AA.AD.PERIODIC.PERIOD` | `AaAccountDetails_PeriodicPeriod` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 119 | `AA.AD.REVOLVING` | `AaAccountDetails_Revolving` | TField |  | Defines the revolving term amounts for lending products. The effect of a revolving product is to increase the available amount from which a customer may drawdown as a result of certain payments. The options are: NO - the available amount will not increase when any payments are made. PAYMENT - any payment against the outstanding amount(due or not due) will result in the available amount increasing PREPAYMENT - only repayments against the outstanding amount (balance not yet due) will result in the available amount increasing |
| 120 | `AA.AD.EB.ACCRUAL.ID` | `AaAccountDetails_EbAccrualId` |  |  |  |
| 121 | `AA.AD.IAS.CLASSIFICATION` | `AaAccountDetails_IasClassification` | TField |  | Attribute stores the BUSINESS MODEL for the IFRS contract |
| 122 | `AA.AD.HOL.REPAY.OPTION` | `AaAccountDetails_HolRepayOption` |  |  |  |
| 123 | `AA.AD.ADJUST.PROPERTY` | `AaAccountDetails_AdjustProperty` |  |  |  |
| 124 | `AA.AD.HOL.DEF.INTEREST` | `AaAccountDetails_HolDefInterest` |  |  |  |
| 125 | `AA.AD.TOT.NUM.PAYMENTS` | `AaAccountDetails_TotNumPayments` |  |  |  |
| 126 | `AA.AD.SECURITISATION.POOL.ID` | `AaAccountDetails_SecuritisationPoolId` |  |  |  |
| 127 | `AA.AD.FUNDING.METHOD` | `AaAccountDetails_FundingMethod` | TField |  |  |
| 128 | `AA.AD.LAST.ACTIVE.TXN.DATE` | `AaAccountDetails_LastActiveTxnDate` | TField |  | System maintained field.The last activity date or last qualifying activity date which is updated at the time of each dormancy evaluation processed by the system. |
| 129 | `AA.AD.ROLLOVER.AMOUNT` | `AaAccountDetails_RolloverAmount` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 130 | `AA.AD.SOURCE.ARRANGEMENT` | `AaAccountDetails_SourceArrangement` |  |  |  |
| 131 | `AA.AD.ACCRUAL.ID` | `AaAccountDetails_AccrualId` |  |  |  |
| 132 | `AA.AD.UNAMORT.AMOUNT` | `AaAccountDetails_UnamortAmount` |  |  |  |
| 133 | `AA.AD.TARGET.UNAMORT.AMOUNT` | `AaAccountDetails_TargetUnamortAmount` |  |  |  |
