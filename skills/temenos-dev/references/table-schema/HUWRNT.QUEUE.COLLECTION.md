# HUWRNT.QUEUE.COLLECTION — Table Schema

> Source: `INSERTS/I_F.HUWRNT.QUEUE.COLLECTION` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUWRNT.QUEUEITEMS.QUEUE.ITEM.REFERENCE` | `HuwrntQueueCollection_QueueItemReference` |  |  |  |
| 2 | `HUWRNT.QUEUEITEMS.PAYMENT.AMOUNT` | `HuwrntQueueCollection_PaymentAmount` |  |  |  |
| 3 | `HUWRNT.QUEUEITEMS.AMT.COLLECTED` | `HuwrntQueueCollection_AmtCollected` |  |  |  |
| 4 | `HUWRNT.QUEUEITEMS.DATE.COLLECTED` | `HuwrntQueueCollection_DateCollected` |  |  |  |
| 5 | `HUWRNT.QUEUEITEMS.STATUS` | `HuwrntQueueCollection_Status` |  |  |  |
| 6 | `HUWRNT.QUEUEITEMS.NO.OF.PAYMENTS` | `HuwrntQueueCollection_NoOfPayments` |  |  |  |
| 7 | `HUWRNT.QUEUEITEMS.STMT.NOS` | `HuwrntQueueCollection_StmtNos` |  |  |  |
| 8 | `HUWRNT.QUEUEITEMS.RESERVED.13` | `HuwrntQueueCollection_Reserved13` | TField |  | Reserved for Future Use. |
| 9 | `HUWRNT.QUEUEITEMS.RESERVED.12` | `HuwrntQueueCollection_Reserved12` | TField |  | Reserved for Future Use. |
| 10 | `HUWRNT.QUEUEITEMS.RESERVED.11` | `HuwrntQueueCollection_Reserved11` | TField |  | Reserved for Future Use. |
| 11 | `HUWRNT.QUEUEITEMS.RESERVED.10` | `HuwrntQueueCollection_Reserved10` | TField |  | Reserved for Future Use. |
| 12 | `HUWRNT.QUEUEITEMS.RESERVED.9` | `HuwrntQueueCollection_Reserved9` | TField |  | Reserved for Future Use. |
| 13 | `HUWRNT.QUEUEITEMS.RESERVED.8` | `HuwrntQueueCollection_Reserved8` | TField |  | Reserved for Future Use. |
| 14 | `HUWRNT.QUEUEITEMS.RESERVED.7` | `HuwrntQueueCollection_Reserved7` | TField |  | Reserved for Future Use. |
| 15 | `HUWRNT.QUEUEITEMS.RESERVED.6` | `HuwrntQueueCollection_Reserved6` | TField |  | Reserved for Future Use. |
| 16 | `HUWRNT.QUEUEITEMS.RESERVED.5` | `HuwrntQueueCollection_Reserved5` | TField |  | Reserved for Future Use. |
| 17 | `HUWRNT.QUEUEITEMS.RESERVED.4` | `HuwrntQueueCollection_Reserved4` | TField |  | Reserved for Future Use. |
| 18 | `HUWRNT.QUEUEITEMS.RESERVED.3` | `HuwrntQueueCollection_Reserved3` | TField |  | Reserved for Future Use. |
| 19 | `HUWRNT.QUEUEITEMS.RESERVED.2` | `HuwrntQueueCollection_Reserved2` | TField |  | Reserved for Future Use. |
| 20 | `HUWRNT.QUEUEITEMS.RESERVED.1` | `HuwrntQueueCollection_Reserved1` | TField |  | Reserved for Future Use. |
