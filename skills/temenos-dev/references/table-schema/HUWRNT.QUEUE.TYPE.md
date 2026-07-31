# HUWRNT.QUEUE.TYPE — Table Schema

> Source: `INSERTS/I_F.HUWRNT.QUEUE.TYPE` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUWRNT.QTYPE.DESCRIPTION` | `HuwrntQueueType_Description` |  |  |  |
| 2 | `HUWRNT.QTYPE.TYPE.CLASSIFICATION` | `HuwrntQueueType_TypeClassification` | TField |  | Specifies the type of collection. |
| 3 | `HUWRNT.QTYPE.TYPE.PRIORITY` | `HuwrntQueueType_TypePriority` | TField |  | Specifies the priority among the type codes from collection point of view. |
| 4 | `HUWRNT.QTYPE.PARTIAL.PAYMENT` | `HuwrntQueueType_PartialPayment` | TField |  | Specifies whether partial payment is allowed or not for the queue type. |
| 5 | `HUWRNT.QTYPE.CLC.REQUIRED` | `HuwrntQueueType_ClcRequired` | TField |  | Specifies whether CLC is required or not. |
| 6 | `HUWRNT.QTYPE.CLC.START.DAYS` | `HuwrntQueueType_ClcStartDays` | TField |  | Specifies from which date, CLC is to be triggered after a payment item is queued. |
| 7 | `HUWRNT.QTYPE.SETTLEMENT.INDICATOR` | `HuwrntQueueType_SettlementIndicator` | TField |  | Specifies whether the settlement type is Immediate, Expiry, Manual or No Settlement. |
| 8 | `HUWRNT.QTYPE.DEFAULT.QUEUE.PERIOD` | `HuwrntQueueType_DefaultQueuePeriod` | TField |  | Specifies the standard queue period for warrant as per regulation. |
| 9 | `HUWRNT.QTYPE.ALLOW.EXEMPT.AMOUNT` | `HuwrntQueueType_AllowExemptAmount` | TField |  | Specifies whether exempt amount needs to be calculated. |
| 10 | `HUWRNT.QTYPE.AUTO.SETTLE` | `HuwrntQueueType_AutoSettle` | TField |  | Specifies whether settlement is allowed or not. |
| 11 | `HUWRNT.QTYPE.MIN.PAYMENT.AMT.CHECK` | `HuwrntQueueType_MinPaymentAmtCheck` | TField |  | Specifies whether during partial settlement of a warrant, the minimum threshold amount defined for partial settlement is required or not |
| 12 | `HUWRNT.QTYPE.UOD.REVERSAL.ALLOWED` | `HuwrntQueueType_UodReversalAllowed` | TField |  | Specifies whether UOD reversal is allowed or not |
| 13 | `HUWRNT.QTYPE.ALLOW.EXPIRY.DATE.CHANGE` | `HuwrntQueueType_AllowExpiryDateChange` | TField |  | Specifies whether expiry date change is allowed or not |
| 14 | `HUWRNT.QTYPE.SUB.TYPE.CLASSIFICATION` | `HuwrntQueueType_SubTypeClassification` | TField |  | Specifies the Sub Type classification for the queue item. |
| 15 | `HUWRNT.QTYPE.CHARGES.APPLICABLE` | `HuwrntQueueType_ChargesApplicable` | TField |  | Specifies if the queue handling fee should be calculated or not. |
| 16 | `HUWRNT.QTYPE.RESERVED.7` | `HuwrntQueueType_Reserved7` |  |  |  |
| 17 | `HUWRNT.QTYPE.RESERVED.6` | `HuwrntQueueType_Reserved6` | TField |  | Reserved for Future Use. |
| 18 | `HUWRNT.QTYPE.RESERVED.5` | `HuwrntQueueType_Reserved5` | TField |  | Reserved for Future Use. |
| 19 | `HUWRNT.QTYPE.RESERVED.4` | `HuwrntQueueType_Reserved4` | TField |  | Reserved for Future Use. |
| 20 | `HUWRNT.QTYPE.RESERVED.3` | `HuwrntQueueType_Reserved3` | TField |  | Reserved for Future Use. |
| 21 | `HUWRNT.QTYPE.RESERVED.2` | `HuwrntQueueType_Reserved2` | TField |  | Reserved for Future Use. |
| 22 | `HUWRNT.QTYPE.RESERVED.1` | `HuwrntQueueType_Reserved1` | TField |  | Reserved for Future Use. |
| 23 | `HUWRNT.QTYPE.LOCAL.REF` | `HuwrntQueueType_LocalRef` |  |  |  |
| 24 | `HUWRNT.QTYPE.OVERRIDE` | `HuwrntQueueType_Override` |  |  |  |
| 25 | `HUWRNT.QTYPE.RECORD.STATUS` | `HuwrntQueueType_RecordStatus` | String |  |  |
| 26 | `HUWRNT.QTYPE.CURR.NO` | `HuwrntQueueType_CurrNo` | String |  |  |
| 27 | `HUWRNT.QTYPE.INPUTTER` | `HuwrntQueueType_Inputter` |  |  |  |
| 28 | `HUWRNT.QTYPE.DATE.TIME` | `HuwrntQueueType_DateTime` |  |  |  |
| 29 | `HUWRNT.QTYPE.AUTHORISER` | `HuwrntQueueType_Authoriser` | String |  |  |
| 30 | `HUWRNT.QTYPE.CO.CODE` | `HuwrntQueueType_CoCode` | String |  |  |
| 31 | `HUWRNT.QTYPE.DEPT.CODE` | `HuwrntQueueType_DeptCode` | String |  |  |
| 32 | `HUWRNT.QTYPE.AUDITOR.CODE` | `HuwrntQueueType_AuditorCode` | String |  |  |
| 33 | `HUWRNT.QTYPE.AUDIT.DATE.TIME` | `HuwrntQueueType_AuditDateTime` | String |  |  |
