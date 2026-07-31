# HUWRNT.QUEUE.REFERENCE.ACCOUNT — Table Schema

> Source: `INSERTS/I_F.HUWRNT.QUEUE.REFERENCE.ACCOUNT` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUWQRA.ACCOUNT.NUMBER` | `HuwrntQueueReferenceAccount_AccountNumber` | TField |  | Payer account number associated with that queue reference. |
| 2 | `HUWQRA.CLASSIFICATION` | `HuwrntQueueReferenceAccount_Classification` | TField |  | Classification of the queue reference. |
| 3 | `HUWQRA.CLC.EFFECTIVE.DATE` | `HuwrntQueueReferenceAccount_ClcEffectiveDate` | TField |  | Date on which CLC will be effective for the queue reference. |
| 4 | `HUWQRA.ACTIVE.FIELD` | `HuwrntQueueReferenceAccount_ActiveField` | TField |  | The field which update during creation of queue. |
| 5 | `HUWQRA.EXTENSION` | `HuwrntQueueReferenceAccount_Extension` | TField |  | The field which update during extension. |
| 6 | `HUWQRA.RESERVED.13` | `HuwrntQueueReferenceAccount_Reserved13` | TField |  | Reserved for future use. |
| 7 | `HUWQRA.RESERVED.12` | `HuwrntQueueReferenceAccount_Reserved12` | TField |  | Reserved for future use. |
| 8 | `HUWQRA.RESERVED.11` | `HuwrntQueueReferenceAccount_Reserved11` | TField |  | Reserved for future use. |
| 9 | `HUWQRA.RESERVED.10` | `HuwrntQueueReferenceAccount_Reserved10` | TField |  | Reserved for future use. |
| 10 | `HUWQRA.RESERVED.9` | `HuwrntQueueReferenceAccount_Reserved9` | TField |  | Reserved for future use. |
| 11 | `HUWQRA.RESERVED.8` | `HuwrntQueueReferenceAccount_Reserved8` | TField |  | Reserved for future use. |
| 12 | `HUWQRA.RESERVED.7` | `HuwrntQueueReferenceAccount_Reserved7` | TField |  | Reserved for future use. |
| 13 | `HUWQRA.RESERVED.6` | `HuwrntQueueReferenceAccount_Reserved6` | TField |  | Reserved for future use. |
| 14 | `HUWQRA.RESERVED.5` | `HuwrntQueueReferenceAccount_Reserved5` | TField |  | Reserved for future use. |
| 15 | `HUWQRA.RESERVED.4` | `HuwrntQueueReferenceAccount_Reserved4` | TField |  | Reserved for future use. |
| 16 | `HUWQRA.RESERVED.3` | `HuwrntQueueReferenceAccount_Reserved3` | TField |  | Reserved for future use. |
| 17 | `HUWQRA.RESERVED.2` | `HuwrntQueueReferenceAccount_Reserved2` | TField |  | Reserved for future use. |
| 18 | `HUWQRA.RESERVED.1` | `HuwrntQueueReferenceAccount_Reserved1` | TField |  | Reserved for future use. |
| 19 | `HUWQRA.LOCAL.REF` | `HuwrntQueueReferenceAccount_LocalRef` |  |  |  |
