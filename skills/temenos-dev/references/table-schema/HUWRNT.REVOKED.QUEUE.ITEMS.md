# HUWRNT.REVOKED.QUEUE.ITEMS — Table Schema

> Source: `INSERTS/I_F.HUWRNT.REVOKED.QUEUE.ITEMS` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUWRRI.QUEUE.REFERENCE` | `HuwrntRevokedQueueItems_QueueReference` |  |  |  |
| 2 | `HUWRRI.QUEUED.DATE` | `HuwrntRevokedQueueItems_QueuedDate` |  |  |  |
| 3 | `HUWRRI.QUEUE.TYPE.CODE` | `HuwrntRevokedQueueItems_QueueTypeCode` |  |  |  |
| 4 | `HUWRRI.QUEUE.TYPE.PRIORITY` | `HuwrntRevokedQueueItems_QueueTypePriority` |  |  |  |
| 5 | `HUWRRI.CLC.EFFECTIVE.DATE` | `HuwrntRevokedQueueItems_ClcEffectiveDate` |  |  |  |
| 6 | `HUWRRI.EXPIRY.DATE` | `HuwrntRevokedQueueItems_ExpiryDate` |  |  |  |
| 7 | `HUWRRI.QUEUE.CONFIRMATION` | `HuwrntRevokedQueueItems_QueueConfirmation` |  |  |  |
| 8 | `HUWRRI.PAYMENT.CCY` | `HuwrntRevokedQueueItems_PaymentCcy` |  |  |  |
| 9 | `HUWRRI.PAYMENT.AMT` | `HuwrntRevokedQueueItems_PaymentAmt` |  |  |  |
| 10 | `HUWRRI.TOTAL.LOCKED.AMOUNT` | `HuwrntRevokedQueueItems_TotalLockedAmount` |  |  |  |
| 11 | `HUWRRI.ACTIVE.FIELD` | `HuwrntRevokedQueueItems_ActiveField` |  |  |  |
| 12 | `HUWRRI.ACTIVE.DATE` | `HuwrntRevokedQueueItems_ActiveDate` |  |  |  |
| 13 | `HUWRRI.CUST.LIQU.STATUS` | `HuwrntRevokedQueueItems_CustLiquStatus` |  |  |  |
| 14 | `HUWRRI.NAME.NUMBER.MISMATCH` | `HuwrntRevokedQueueItems_NameNumberMismatch` |  |  |  |
| 15 | `HUWRRI.NEW.PAYER.ACCOUNT.NO` | `HuwrntRevokedQueueItems_NewPayerAccountNo` |  |  |  |
| 16 | `HUWRRI.PENDING.AMOUNT` | `HuwrntRevokedQueueItems_PendingAmount` |  |  |  |
| 17 | `HUWRRI.AUTO.SETTLE` | `HuwrntRevokedQueueItems_AutoSettle` |  |  |  |
| 18 | `HUWRRI.SETTLEMENT.INDICATOR` | `HuwrntRevokedQueueItems_SettlementIndicator` |  |  |  |
| 19 | `HUWRRI.COMPLETED.DATE` | `HuwrntRevokedQueueItems_CompletedDate` |  |  |  |
| 20 | `HUWRRI.COMPLETED.REASON` | `HuwrntRevokedQueueItems_CompletedReason` |  |  |  |
| 21 | `HUWRRI.READY.FOR.SETTLEMENT` | `HuwrntRevokedQueueItems_ReadyForSettlement` |  |  |  |
| 22 | `HUWRRI.SUSPENDED.DATE` | `HuwrntRevokedQueueItems_SuspendedDate` |  |  |  |
| 23 | `HUWRRI.PAYER.NAME` | `HuwrntRevokedQueueItems_PayerName` |  |  |  |
| 24 | `HUWRRI.VALUE.DATE.PCS` | `HuwrntRevokedQueueItems_ValueDatePcs` |  |  |  |
| 25 | `HUWRRI.BE.CHECK.ID` | `HuwrntRevokedQueueItems_BeCheckId` |  |  |  |
| 26 | `HUWRRI.COLLECTION.TYPE` | `HuwrntRevokedQueueItems_CollectionType` |  |  |  |
| 27 | `HUWRRI.DATE.TIME.PCS` | `HuwrntRevokedQueueItems_DateTimePcs` |  |  |  |
| 28 | `HUWRRI.DATE.TIME.SYSTEM` | `HuwrntRevokedQueueItems_DateTimeSystem` |  |  |  |
| 29 | `HUWRRI.BEN.ACCOUNT.NO` | `HuwrntRevokedQueueItems_BenAccountNo` |  |  |  |
| 30 | `HUWRRI.BEN.NAME` | `HuwrntRevokedQueueItems_BenName` |  |  |  |
| 31 | `HUWRRI.NARRATIVE` | `HuwrntRevokedQueueItems_Narrative` |  |  |  |
| 32 | `HUWRRI.PROCESS.CHANNEL` | `HuwrntRevokedQueueItems_ProcessChannel` |  |  |  |
| 33 | `HUWRRI.PREVIOUS.SETTLED.AMOUNT` | `HuwrntRevokedQueueItems_PreviousSettledAmount` |  |  |  |
| 34 | `HUWRRI.NUM.OF.PAYMENTS.MADE` | `HuwrntRevokedQueueItems_NumOfPaymentsMade` |  |  |  |
| 35 | `HUWRRI.MIGRATED.WARRANT` | `HuwrntRevokedQueueItems_MigratedWarrant` |  |  |  |
| 36 | `HUWRRI.UOD.LAST.ACTIVE.SEQUENCE` | `HuwrntRevokedQueueItems_UodLastActiveSequence` | TField |  | Contains the last active sequence number of the UOD processed. |
| 37 | `HUWRRI.RESERVED.10` | `HuwrntRevokedQueueItems_Reserved10` | TField |  | Reserved for future use. |
| 38 | `HUWRRI.RESERVED.9` | `HuwrntRevokedQueueItems_Reserved9` | TField |  | Reserved for future use. |
| 39 | `HUWRRI.RESERVED.8` | `HuwrntRevokedQueueItems_Reserved8` | TField |  | Reserved for future use. |
| 40 | `HUWRRI.RESERVED.7` | `HuwrntRevokedQueueItems_Reserved7` | TField |  | Reserved for future use. |
| 41 | `HUWRRI.RESERVED.6` | `HuwrntRevokedQueueItems_Reserved6` | TField |  | Reserved for future use. |
| 42 | `HUWRRI.RESERVED.5` | `HuwrntRevokedQueueItems_Reserved5` | TField |  | Reserved for future use. |
| 43 | `HUWRRI.RESERVED.4` | `HuwrntRevokedQueueItems_Reserved4` | TField |  | Reserved for future use. |
| 44 | `HUWRRI.RESERVED.3` | `HuwrntRevokedQueueItems_Reserved3` | TField |  | Reserved for future use. |
| 45 | `HUWRRI.RESERVED.2` | `HuwrntRevokedQueueItems_Reserved2` | TField |  | Reserved for future use. |
| 46 | `HUWRRI.RESERVED.1` | `HuwrntRevokedQueueItems_Reserved1` | TField |  | Reserved for future use. |
| 47 | `HUWRRI.LOCAL.REF` | `HuwrntRevokedQueueItems_LocalRef` |  |  |  |
