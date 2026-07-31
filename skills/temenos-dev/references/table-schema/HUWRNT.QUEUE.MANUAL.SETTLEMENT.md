# HUWRNT.QUEUE.MANUAL.SETTLEMENT — Table Schema

> Source: `INSERTS/I_F.HUWRNT.QUEUE.MANUAL.SETTLEMENT` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUWQMS.TYPE.CLASSIFICATION` | `HuwrntQueueManualSettlement_TypeClassification` | TField |  | Specifies the type of collection.Mapped to field, HUWRNT.QUEUE.TYPE > TYPE.CLASSIFICATION = WARRANTS |
| 2 | `HUWQMS.ACTIVE.FIELD` | `HuwrntQueueManualSettlement_ActiveField` | TField |  | Lists out only those queue items under warrants classification which are active currently |
| 3 | `HUWQMS.PAYMENT.CCY` | `HuwrntQueueManualSettlement_PaymentCcy` | TField |  | Specifies the currency in which warrant has been issued |
| 4 | `HUWQMS.PENDING.AMOUNT` | `HuwrntQueueManualSettlement_PendingAmount` | TField |  | Specifies pending amount to be collected which is the total locked amount |
| 5 | `HUWQMS.ACCOUNT.NUMBER` | `HuwrntQueueManualSettlement_AccountNumber` |  |  |  |
| 6 | `HUWQMS.CURRENCY` | `HuwrntQueueManualSettlement_Currency` |  |  |  |
| 7 | `HUWQMS.AVAILABLE.EXEMPT.AMOUNT` | `HuwrntQueueManualSettlement_AvailableExemptAmount` |  |  |  |
| 8 | `HUWQMS.EQUIVALENT.EXEMPT.AMOUNT` | `HuwrntQueueManualSettlement_EquivalentExemptAmount` |  |  |  |
| 9 | `HUWQMS.AMOUNT.PAY` | `HuwrntQueueManualSettlement_AmountPay` |  |  |  |
| 10 | `HUWQMS.RESERVED.15` | `HuwrntQueueManualSettlement_Reserved15` |  |  |  |
| 11 | `HUWQMS.RESERVED.14` | `HuwrntQueueManualSettlement_Reserved14` |  |  |  |
| 12 | `HUWQMS.RESERVED.13` | `HuwrntQueueManualSettlement_Reserved13` |  |  |  |
| 13 | `HUWQMS.RESERVED.12` | `HuwrntQueueManualSettlement_Reserved12` | TField |  | Reserved for future use. |
| 14 | `HUWQMS.RESERVED.11` | `HuwrntQueueManualSettlement_Reserved11` | TField |  | Reserved for future use. |
| 15 | `HUWQMS.RESERVED.10` | `HuwrntQueueManualSettlement_Reserved10` | TField |  | Reserved for future use. |
| 16 | `HUWQMS.RESERVED.9` | `HuwrntQueueManualSettlement_Reserved9` | TField |  | Reserved for future use. |
| 17 | `HUWQMS.RESERVED.8` | `HuwrntQueueManualSettlement_Reserved8` | TField |  | Reserved for future use. |
| 18 | `HUWQMS.RESERVED.7` | `HuwrntQueueManualSettlement_Reserved7` | TField |  | Reserved for future use. |
| 19 | `HUWQMS.RESERVED.6` | `HuwrntQueueManualSettlement_Reserved6` | TField |  | Reserved for future use. |
| 20 | `HUWQMS.RESERVED.5` | `HuwrntQueueManualSettlement_Reserved5` | TField |  | Reserved for future use. |
| 21 | `HUWQMS.RESERVED.4` | `HuwrntQueueManualSettlement_Reserved4` | TField |  | Reserved for future use. |
| 22 | `HUWQMS.RESERVED.3` | `HuwrntQueueManualSettlement_Reserved3` | TField |  | Reserved for future use. |
| 23 | `HUWQMS.RESERVED.2` | `HuwrntQueueManualSettlement_Reserved2` | TField |  | Reserved for future use. |
| 24 | `HUWQMS.RESERVED.1` | `HuwrntQueueManualSettlement_Reserved1` | TField |  | Reserved for future use. |
| 25 | `HUWQMS.LOCAL.REF` | `HuwrntQueueManualSettlement_LocalRef` |  |  |  |
| 26 | `HUWQMS.OVERRIDE` | `HuwrntQueueManualSettlement_Override` |  |  |  |
| 27 | `HUWQMS.RECORD.STATUS` | `HuwrntQueueManualSettlement_RecordStatus` | String |  |  |
| 28 | `HUWQMS.CURR.NO` | `HuwrntQueueManualSettlement_CurrNo` | String |  |  |
| 29 | `HUWQMS.INPUTTER` | `HuwrntQueueManualSettlement_Inputter` |  |  |  |
| 30 | `HUWQMS.DATE.TIME` | `HuwrntQueueManualSettlement_DateTime` |  |  |  |
| 31 | `HUWQMS.AUTHORISER` | `HuwrntQueueManualSettlement_Authoriser` | String |  |  |
| 32 | `HUWQMS.CO.CODE` | `HuwrntQueueManualSettlement_CoCode` | String |  |  |
| 33 | `HUWQMS.DEPT.CODE` | `HuwrntQueueManualSettlement_DeptCode` | String |  |  |
| 34 | `HUWQMS.AUDITOR.CODE` | `HuwrntQueueManualSettlement_AuditorCode` | String |  |  |
| 35 | `HUWQMS.AUDIT.DATE.TIME` | `HuwrntQueueManualSettlement_AuditDateTime` | String |  |  |
