# CL.COLLECTION.ITEM — Table Schema

> Source: `INSERTS/I_F.CL.COLLECTION.ITEM` in `CL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CL.CIT.HOME.PHONE` | `ClCollectionItem_HomePhone` | TField |  | Home phone of Customer(Populated from CUSTOMER table). |
| 2 | `CL.CIT.WORK.PHONE` | `ClCollectionItem_WorkPhone` | TField |  | Work phone of customer(Populated from CUSTOMER table). |
| 3 | `CL.CIT.MOBILE.PHONE` | `ClCollectionItem_MobilePhone` | TField |  | Mobile Number of customer(Populated from CUSTOMER table). |
| 4 | `CL.CIT.CUSTOMER.EMPLOYER` | `ClCollectionItem_CustomerEmployer` | TField |  | Employer name of customer(Populated from CUSTOMER table). |
| 5 | `CL.CIT.UL.CONTRACT.REF` | `ClCollectionItem_UlContractRef` |  |  |  |
| 6 | `CL.CIT.COMPANY.MNE` | `ClCollectionItem_CompanyMne` |  |  |  |
| 7 | `CL.CIT.DUE.REFERENCE` | `ClCollectionItem_DueReference` |  |  |  |
| 8 | `CL.CIT.OD.START.DATE` | `ClCollectionItem_OdStartDate` |  |  |  |
| 9 | `CL.CIT.OD.CURRENCY` | `ClCollectionItem_OdCurrency` |  |  |  |
| 10 | `CL.CIT.OD.AMOUNT` | `ClCollectionItem_OdAmount` |  |  |  |
| 11 | `CL.CIT.OD.STATUS` | `ClCollectionItem_OdStatus` |  |  |  |
| 12 | `CL.CIT.UL.OS.AMOUNT` | `ClCollectionItem_UlOsAmount` |  |  |  |
| 13 | `CL.CIT.UL.LOAN.SECURED` | `ClCollectionItem_UlLoanSecured` |  |  |  |
| 14 | `CL.CIT.TOT.OVERDUE.AMT` | `ClCollectionItem_TotOverdueAmt` | TField |  | sum of the OD.AMOUNT field. |
| 15 | `CL.CIT.TOT.OUTSTDING.AMT` | `ClCollectionItem_TotOutstdingAmt` | TField |  | sum of the UL.OS.AMOUNT field. |
| 16 | `CL.CIT.TOTAL.AMOUNT` | `ClCollectionItem_TotalAmount` | TField |  | Sum of the TOT.OVERDUE.AMT and TOT.OUTSTDING.AMT. |
| 17 | `CL.CIT.PREV.NO.OF.DAYS.PD` | `ClCollectionItem_PrevNoOfDaysPd` | TField |  | Populated from the field NO.OF.DAYS.PD. |
| 18 | `CL.CIT.PREV.BUCKET` | `ClCollectionItem_PrevBucket` | TField |  | Populated from field BUCKET. |
| 19 | `CL.CIT.NO.OF.DAYS.PD` | `ClCollectionItem_NoOfDaysPd` | TField |  | This field contains the number of days difference between the oldest payment date of the customer's arrangement loan and the T24 system date. It will not be updated if there is no activity triggered for the day. The most recent value can be viewed by executing the enquiry CL.COLL.ITEM.REP. |
| 20 | `CL.CIT.BUCKET` | `ClCollectionItem_Bucket` | TField |  | This field holds the bucket number to which this item belongs. |
| 21 | `CL.CIT.NO.OF.BPTP` | `ClCollectionItem_NoOfBptp` | TField |  | Customer has No.Of.Times broken the promise to pay. |
| 22 | `CL.CIT.FIRST.PAYMENT.FLG` | `ClCollectionItem_FirstPaymentFlg` | TField |  | This field will get populated as "FT". |
| 23 | `CL.CIT.QUEUE` | `ClCollectionItem_Queue` | TField |  | Should be an entry in the QUEUE record. |
| 24 | `CL.CIT.QUEUE.DATE` | `ClCollectionItem_QueueDate` | TField |  | Date when the QUEUE field was updated for the last time. |
| 25 | `CL.CIT.PREVIOUS.QUEUE` | `ClCollectionItem_PreviousQueue` | TField |  | Update automatically with the old value of the field QUEUE whenever the later changes. |
| 26 | `CL.CIT.PRE.QUEUE.DATE` | `ClCollectionItem_PreQueueDate` | TField |  | Update automatically with the old value of the field QUEUE DATE whenever the later changes. |
| 27 | `CL.CIT.ACTION.CODE` | `ClCollectionItem_ActionCode` | TField |  | Action performed by the collector. |
| 28 | `CL.CIT.OUTCOME.CODE` | `ClCollectionItem_OutcomeCode` | TField |  | Outcome of the action mentioned in the previous field. |
| 29 | `CL.CIT.OUTCOME.DUE.DATE` | `ClCollectionItem_OutcomeDueDate` | TField |  | Outcome due date will be entered here. |
| 30 | `CL.CIT.OUTCOME.DUE.AMT` | `ClCollectionItem_OutcomeDueAmt` | TField |  | Due amount will be entered in this field. |
| 31 | `CL.CIT.PTP.DATE` | `ClCollectionItem_PtpDate` |  |  |  |
| 32 | `CL.CIT.PTP.AMT` | `ClCollectionItem_PtpAmt` |  |  |  |
| 33 | `CL.CIT.PTP.COLLECTOR` | `ClCollectionItem_PtpCollector` |  |  |  |
| 34 | `CL.CIT.PTP.PAID.AMT` | `ClCollectionItem_PtpPaidAmt` |  |  |  |
| 35 | `CL.CIT.COLLECTOR` | `ClCollectionItem_Collector` | TField |  | Updated online automatically with the current collector ID whenever he enters an action code and outcome code. |
| 36 | `CL.CIT.ACTION.DATE` | `ClCollectionItem_ActionDate` | TField |  | Date when the ACTION field was updated for the last time. |
| 37 | `CL.CIT.ACTION.TIME` | `ClCollectionItem_ActionTime` | TField |  | Time when the ACTION field was updated for the last time. |
| 38 | `CL.CIT.NOTES` | `ClCollectionItem_Notes` |  |  |  |
| 39 | `CL.CIT.PREV.ACTION.CODE` | `ClCollectionItem_PrevActionCode` | TField |  | Populated automatically from the field ACTION CODE every time the record is accessed in input mode. |
| 40 | `CL.CIT.PREV.OUTCOME.CODE` | `ClCollectionItem_PrevOutcomeCode` | TField |  | Populated automatically from the field OUTCOME CODE every time the record is accessed in input mode. |
| 41 | `CL.CIT.PREV.OUT.DUE.DATE` | `ClCollectionItem_PrevOutDueDate` | TField |  | Populated automatically from the field OUTCOME DUE DATE every time the record is accessed in input mode. |
| 42 | `CL.CIT.PREV.OUT.DUE.AMT` | `ClCollectionItem_PrevOutDueAmt` | TField |  | Populated automatically from the field OUTCOME DUE AMOUNT every time the record is accessed in input mode. |
| 43 | `CL.CIT.PREV.COLLECTOR` | `ClCollectionItem_PrevCollector` | TField |  | Populated automatically from the field COLLECTOR every time the record is accessed in input mode. |
| 44 | `CL.CIT.PREV.ACTION.DATE` | `ClCollectionItem_PrevActionDate` | TField |  |  |
| 45 | `CL.CIT.PREV.ACTION.TIME` | `ClCollectionItem_PrevActionTime` | TField |  |  |
| 46 | `CL.CIT.PREVIOUS.NOTES` | `ClCollectionItem_PreviousNotes` |  |  |  |
| 47 | `CL.CIT.CREATION.DATE` | `ClCollectionItem_CreationDate` | TField |  |  |
| 48 | `CL.CIT.UPDATE.DATE` | `ClCollectionItem_UpdateDate` | TField |  | Date when the record was updated for the last time through the end of day batch. |
| 49 | `CL.CIT.GENDER` | `ClCollectionItem_Gender` | TField |  | Gender of Customer. (Populated from CUSTOMER table). |
| 50 | `CL.CIT.CUS.SECTOR` | `ClCollectionItem_CusSector` | TField |  | Customer Sector. (Populated from CUSTOMER table). |
| 51 | `CL.CIT.SEGMENT.FLG` | `ClCollectionItem_SegmentFlg` | TField |  | Not in used. |
| 52 | `CL.CIT.CUS.STATUS` | `ClCollectionItem_CusStatus` | TField |  | Status of Customer. (Populated from CUSTOMER table). |
| 53 | `CL.CIT.WEIGHT` | `ClCollectionItem_Weight` | TField |  | Weightage of the collection item. |
| 54 | `CL.CIT.INT.EXT.QUEUE` | `ClCollectionItem_IntExtQueue` | TField |  | Whether the item is in an internal or external queue. |
| 55 | `CL.CIT.SELECTION` | `ClCollectionItem_Selection` | TField |  | Whether the item is in a selection based queue or not. |
| 56 | `CL.CIT.BLACK.LIST` | `ClCollectionItem_BlackList` | TField |  |  |
| 57 | `CL.CIT.CL.ACTIVITY.ID` | `ClCollectionItem_ClActivityId` | TField |  | It will be stored lastest action activity .Id Should be Collection Item Id with Sequence No. |
| 58 | `CL.CIT.DAO` | `ClCollectionItem_Dao` | TField |  | DAO Officer of Customer. (Populated from CUSTOMER table). |
| 59 | `CL.CIT.REGION` | `ClCollectionItem_Region` | TField |  | Residence Region of the customer (Populated from CUSTOMER table). |
| 60 | `CL.CIT.ITEM.STATUS` | `ClCollectionItem_ItemStatus` | TField |  | Status of the PD record as updated in the field PD STATUS for the collection item in specific. |
| 61 | `CL.CIT.CHECK.COLLECTOR` | `ClCollectionItem_CheckCollector` | TField |  | This field act as supervisor,when the field is having "N" then only system can reassign the queue and Collector. |
| 62 | `CL.CIT.OVERDUE.REASON` | `ClCollectionItem_OverdueReason` | TField |  | Update the Overdue Reason if OVERDUE.REASON field set as "Y" in CL.OUTCOME. |
| 63 | `CL.CIT.ACCESS.TIME` | `ClCollectionItem_AccessTime` | TField |  |  |
| 64 | `CL.CIT.NEW.QUEUE` | `ClCollectionItem_NewQueue` | TField |  | If the Queue is reassigned, corresponding new QUEUE will be populated here. |
| 65 | `CL.CIT.TRN.FLAG` | `ClCollectionItem_TrnFlag` | TField |  | This field will be desired whether collector field holds existing value or New Collector |
| 66 | `CL.CIT.INACTIVE.DAYS` | `ClCollectionItem_InactiveDays` | TField |  | Holds the No.of days after which an item is marked as inactive. |
| 67 | `CL.CIT.INACTIVE.OUTCOME` | `ClCollectionItem_InactiveOutcome` | TField |  | Holds the Outcome come to be used when marking item as inactive. |
| 68 | `CL.CIT.MV.RESERVED8` | `ClCollectionItem_MvReserved8` | TField |  |  |
| 69 | `CL.CIT.MV.RESERVED7` | `ClCollectionItem_MvReserved7` | TField |  |  |
| 70 | `CL.CIT.MV.RESERVED6` | `ClCollectionItem_MvReserved6` | TField |  |  |
| 71 | `CL.CIT.MV.RESERVED5` | `ClCollectionItem_MvReserved5` | TField |  |  |
| 72 | `CL.CIT.MV.RESERVED4` | `ClCollectionItem_MvReserved4` | TField |  |  |
| 73 | `CL.CIT.MV.RESERVED3` | `ClCollectionItem_MvReserved3` | TField |  |  |
| 74 | `CL.CIT.MV.RESERVED2` | `ClCollectionItem_MvReserved2` | TField |  |  |
| 75 | `CL.CIT.MV.RESERVED1` | `ClCollectionItem_MvReserved1` | TField |  |  |
| 76 | `CL.CIT.RESERVED5` | `ClCollectionItem_Reserved5` | TField |  |  |
| 77 | `CL.CIT.RESERVED4` | `ClCollectionItem_Reserved4` | TField |  |  |
| 78 | `CL.CIT.RESERVED3` | `ClCollectionItem_Reserved3` | TField |  |  |
| 79 | `CL.CIT.RESERVED2` | `ClCollectionItem_Reserved2` | TField |  |  |
| 80 | `CL.CIT.RESERVED1` | `ClCollectionItem_Reserved1` | TField |  |  |
| 81 | `CL.CIT.LOCAL.REF` | `ClCollectionItem_LocalRef` |  |  |  |
| 82 | `CL.CIT.OVERRIDE` | `ClCollectionItem_Override` |  |  |  |
| 83 | `CL.CIT.RECORD.STATUS` | `ClCollectionItem_RecordStatus` | String |  |  |
| 84 | `CL.CIT.CURR.NO` | `ClCollectionItem_CurrNo` | String |  |  |
| 85 | `CL.CIT.INPUTTER` | `ClCollectionItem_Inputter` |  |  |  |
| 86 | `CL.CIT.DATE.TIME` | `ClCollectionItem_DateTime` |  |  |  |
| 87 | `CL.CIT.AUTHORISER` | `ClCollectionItem_Authoriser` | String |  |  |
| 88 | `CL.CIT.CO.CODE` | `ClCollectionItem_CoCode` | String |  |  |
| 89 | `CL.CIT.DEPT.CODE` | `ClCollectionItem_DeptCode` | String |  |  |
| 90 | `CL.CIT.AUDITOR.CODE` | `ClCollectionItem_AuditorCode` | String |  |  |
| 91 | `CL.CIT.AUDIT.DATE.TIME` | `ClCollectionItem_AuditDateTime` | String |  |  |
| 92 | `CL.CIT.LCY.OD.AMOUNT` | `ClCollectionItem_LcyOdAmount` |  |  |  |
| 93 | `CL.CIT.LCY.OS.AMOUNT` | `ClCollectionItem_LcyOsAmount` |  |  |  |
| 94 | `CL.CIT.ACCOUNT.NUMBER` | `ClCollectionItem_AccountNumber` |  |  |  |
| 95 | `CL.CIT.APPROVED.LIMIT` | `ClCollectionItem_ApprovedLimit` |  |  |  |
| 96 | `CL.CIT.AVAILABLE.LIMIT` | `ClCollectionItem_AvailableLimit` |  |  |  |
| 97 | `CL.CIT.POSTING.RESTRICTION.CODE` | `ClCollectionItem_PostingRestrictionCode` |  |  |  |
| 98 | `CL.CIT.SUSPENSION.OF.INTEREST` | `ClCollectionItem_SuspensionOfInterest` |  |  |  |
| 99 | `CL.CIT.AMT.EX.RATE` | `ClCollectionItem_AmtExRate` |  |  |  |
| 100 | `CL.CIT.OUTCOME.DUE.CCY` | `ClCollectionItem_OutcomeDueCcy` | TField |  | Outcome due currency indicates currency in which repayment have been committed to be settled If user does not specify outcome due currency, then by default it will be local currency |
| 101 | `CL.CIT.OUTCOME.DUE.AMT.LCY` | `ClCollectionItem_OutcomeDueAmtLcy` | TField |  | This field indicates outcome due amount in Local Currency. |
| 102 | `CL.CIT.OUT.EX.RATE` | `ClCollectionItem_OutExRate` | TField |  | This field indicates Exchange rate used to convert the Outcome Due Amount to Local currency |
| 103 | `CL.CIT.PTP.AMT.CCY` | `ClCollectionItem_PtpAmtCcy` |  |  |  |
| 104 | `CL.CIT.PTP.AMT.LCY` | `ClCollectionItem_PtpAmtLcy` |  |  |  |
| 105 | `CL.CIT.PTP.PAID.AMT.LCY` | `ClCollectionItem_PtpPaidAmtLcy` |  |  |  |
| 106 | `CL.CIT.PREV.OUT.AMT.CCY` | `ClCollectionItem_PrevOutAmtCcy` | TField |  | This indicates the Previous Outcome Due Amount Currency |
| 107 | `CL.CIT.PREV.OUT.DUE.AMT.LCY` | `ClCollectionItem_PrevOutDueAmtLcy` | TField |  | Previous Outcome Due Amount in Local Currency Populated automatically from the field OUTCOME.DUE.AMOUNT.LCY every time the record is accessed in input mode. |
