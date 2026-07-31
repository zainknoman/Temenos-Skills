# HUWRNT.QUEUE.ITEMS — Table Schema

> Source: `INSERTS/I_F.HUWRNT.QUEUE.ITEMS` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUWRQI.QUEUE.REFERENCE` | `HuwrntQueueItems_QueueReference` |  |  |  |
| 2 | `HUWRQI.QUEUED.DATE` | `HuwrntQueueItems_QueuedDate` |  |  |  |
| 3 | `HUWRQI.QUEUE.TYPE.CODE` | `HuwrntQueueItems_QueueTypeCode` |  |  |  |
| 4 | `HUWRQI.QUEUE.TYPE.PRIORITY` | `HuwrntQueueItems_QueueTypePriority` |  |  |  |
| 5 | `HUWRQI.CLC.EFFECTIVE.DATE` | `HuwrntQueueItems_ClcEffectiveDate` |  |  |  |
| 6 | `HUWRQI.EXPIRY.DATE` | `HuwrntQueueItems_ExpiryDate` |  |  |  |
| 7 | `HUWRQI.QUEUE.CONFIRMATION` | `HuwrntQueueItems_QueueConfirmation` |  |  |  |
| 8 | `HUWRQI.PAYMENT.CCY` | `HuwrntQueueItems_PaymentCcy` |  |  |  |
| 9 | `HUWRQI.PAYMENT.AMT` | `HuwrntQueueItems_PaymentAmt` |  |  |  |
| 10 | `HUWRQI.TOTAL.LOCKED.AMOUNT` | `HuwrntQueueItems_TotalLockedAmount` |  |  |  |
| 11 | `HUWRQI.ACTIVE.FIELD` | `HuwrntQueueItems_ActiveField` |  |  |  |
| 12 | `HUWRQI.ACTIVE.DATE` | `HuwrntQueueItems_ActiveDate` |  |  |  |
| 13 | `HUWRQI.CUST.LIQU.STATUS` | `HuwrntQueueItems_CustLiquStatus` |  |  |  |
| 14 | `HUWRQI.NAME.NUMBER.MISMATCH` | `HuwrntQueueItems_NameNumberMismatch` |  |  |  |
| 15 | `HUWRQI.NEW.PAYER.ACCOUNT.NO` | `HuwrntQueueItems_NewPayerAccountNo` |  |  |  |
| 16 | `HUWRQI.PENDING.AMOUNT` | `HuwrntQueueItems_PendingAmount` |  |  |  |
| 17 | `HUWRQI.AUTO.SETTLE` | `HuwrntQueueItems_AutoSettle` |  |  |  |
| 18 | `HUWRQI.SETTLEMENT.INDICATOR` | `HuwrntQueueItems_SettlementIndicator` |  |  |  |
| 19 | `HUWRQI.COMPLETED.DATE` | `HuwrntQueueItems_CompletedDate` |  |  |  |
| 20 | `HUWRQI.COMPLETED.REASON` | `HuwrntQueueItems_CompletedReason` |  |  |  |
| 21 | `HUWRQI.READY.FOR.SETTLEMENT` | `HuwrntQueueItems_ReadyForSettlement` |  |  |  |
| 22 | `HUWRQI.SUSPENDED.DATE` | `HuwrntQueueItems_SuspendedDate` |  |  |  |
| 23 | `HUWRQI.UOD.LAST.ACTIVE.SEQUENCE` | `HuwrntQueueItems_UodLastActiveSequence` | TField |  | Contains the last active sequence number of the UOD processed. |
| 24 | `HUWRQI.RESERVED.12` | `HuwrntQueueItems_Reserved12` | TField |  | Reserved for future use. |
| 25 | `HUWRQI.RESERVED.11` | `HuwrntQueueItems_Reserved11` | TField |  | Reserved for future use. |
| 26 | `HUWRQI.RESERVED.10` | `HuwrntQueueItems_Reserved10` | TField |  | Reserved for future use. |
| 27 | `HUWRQI.RESERVED.9` | `HuwrntQueueItems_Reserved9` | TField |  | Reserved for future use. |
| 28 | `HUWRQI.RESERVED.8` | `HuwrntQueueItems_Reserved8` | TField |  | Reserved for future use. |
| 29 | `HUWRQI.RESERVED.7` | `HuwrntQueueItems_Reserved7` | TField |  | Reserved for future use. |
| 30 | `HUWRQI.RESERVED.6` | `HuwrntQueueItems_Reserved6` | TField |  | Reserved for future use. |
| 31 | `HUWRQI.RESERVED.5` | `HuwrntQueueItems_Reserved5` | TField |  | Reserved for future use. |
| 32 | `HUWRQI.RESERVED.4` | `HuwrntQueueItems_Reserved4` | TField |  | Reserved for future use. |
| 33 | `HUWRQI.RESERVED.3` | `HuwrntQueueItems_Reserved3` | TField |  | Reserved for future use. |
| 34 | `HUWRQI.RESERVED.2` | `HuwrntQueueItems_Reserved2` | TField |  | Reserved for future use. |
| 35 | `HUWRQI.RESERVED.1` | `HuwrntQueueItems_Reserved1` | TField |  | Reserved for future use. |
| 36 | `HUWRQI.LOCAL.REF` | `HuwrntQueueItems_LocalRef` |  |  |  |
| 37 | `HUWRQI.OVERRIDE` | `HuwrntQueueItems_Override` |  |  |  |
| 38 | `HUWRQI.RECORD.STATUS` | `HuwrntQueueItems_RecordStatus` | String |  |  |
| 39 | `HUWRQI.CURR.NO` | `HuwrntQueueItems_CurrNo` | String |  |  |
| 40 | `HUWRQI.INPUTTER` | `HuwrntQueueItems_Inputter` |  |  |  |
| 41 | `HUWRQI.DATE.TIME` | `HuwrntQueueItems_DateTime` |  |  |  |
| 42 | `HUWRQI.AUTHORISER` | `HuwrntQueueItems_Authoriser` | String |  |  |
| 43 | `HUWRQI.CO.CODE` | `HuwrntQueueItems_CoCode` | String |  |  |
| 44 | `HUWRQI.DEPT.CODE` | `HuwrntQueueItems_DeptCode` | String |  |  |
| 45 | `HUWRQI.AUDITOR.CODE` | `HuwrntQueueItems_AuditorCode` | String |  |  |
| 46 | `HUWRQI.AUDIT.DATE.TIME` | `HuwrntQueueItems_AuditDateTime` | String |  |  |
