# HUWRNT.QUEUE.INFO — Table Schema

> Source: `INSERTS/I_F.HUWRNT.QUEUE.INFO` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUWQIN.PAYER.ACCOUNT.NO` | `HuwrntQueueInfo_PayerAccountNo` |  |  |  |
| 2 | `HUWQIN.QUEUE.REFERENCE` | `HuwrntQueueInfo_QueueReference` |  |  |  |
| 3 | `HUWQIN.LOCK.REFERENCE` | `HuwrntQueueInfo_LockReference` |  |  |  |
| 4 | `HUWQIN.RESERVED.15` | `HuwrntQueueInfo_Reserved15` | TField |  | Reserved for future use. |
| 5 | `HUWQIN.RESERVED.14` | `HuwrntQueueInfo_Reserved14` | TField |  | Reserved for future use. |
| 6 | `HUWQIN.RESERVED.13` | `HuwrntQueueInfo_Reserved13` | TField |  | Reserved for future use. |
| 7 | `HUWQIN.RESERVED.12` | `HuwrntQueueInfo_Reserved12` | TField |  | Reserved for future use. |
| 8 | `HUWQIN.RESERVED.11` | `HuwrntQueueInfo_Reserved11` | TField |  | Reserved for future use. |
| 9 | `HUWQIN.RESERVED.10` | `HuwrntQueueInfo_Reserved10` | TField |  | Reserved for future use. |
| 10 | `HUWQIN.RESERVED.9` | `HuwrntQueueInfo_Reserved9` | TField |  | Reserved for future use. |
| 11 | `HUWQIN.RESERVED.8` | `HuwrntQueueInfo_Reserved8` | TField |  | Reserved for future use. |
| 12 | `HUWQIN.RESERVED.7` | `HuwrntQueueInfo_Reserved7` | TField |  | Reserved for future use. |
| 13 | `HUWQIN.RESERVED.6` | `HuwrntQueueInfo_Reserved6` | TField |  | Reserved for future use. |
| 14 | `HUWQIN.RESERVED.5` | `HuwrntQueueInfo_Reserved5` | TField |  | Reserved for future use. |
| 15 | `HUWQIN.RESERVED.4` | `HuwrntQueueInfo_Reserved4` | TField |  | Reserved for future use. |
| 16 | `HUWQIN.RESERVED.3` | `HuwrntQueueInfo_Reserved3` | TField |  | Reserved for future use. |
| 17 | `HUWQIN.RESERVED.2` | `HuwrntQueueInfo_Reserved2` | TField |  | Reserved for future use. |
| 18 | `HUWQIN.RESERVED.1` | `HuwrntQueueInfo_Reserved1` | TField |  | Reserved for future use. |
| 19 | `HUWQIN.LOCAL.REF` | `HuwrntQueueInfo_LocalRef` |  |  |  |
