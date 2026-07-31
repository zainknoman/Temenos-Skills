# HUWRNT.QUEUE.EXEMPT.AMOUNT — Table Schema

> Source: `INSERTS/I_F.HUWRNT.QUEUE.EXEMPT.AMOUNT` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUWQEM.ACCOUNT.NUMBER` | `HuwrntQueueExemptAmount_AccountNumber` |  |  |  |
| 2 | `HUWQEM.CURRENCY` | `HuwrntQueueExemptAmount_Currency` |  |  |  |
| 3 | `HUWQEM.EXEMPT.AMOUNT` | `HuwrntQueueExemptAmount_ExemptAmount` |  |  |  |
| 4 | `HUWQEM.EQUIVALENT.EXEMPT.AMOUNT` | `HuwrntQueueExemptAmount_EquivalentExemptAmount` |  |  |  |
| 5 | `HUWQEM.CUMULATIVE.EXEMPT.AMOUNT` | `HuwrntQueueExemptAmount_CumulativeExemptAmount` | TField |  | Specifies cumulative exempt amount calculated and made available for captioned reference number. |
| 6 | `HUWQEM.RESERVED.15` | `HuwrntQueueExemptAmount_Reserved15` | TField |  | Reserved for future use. |
| 7 | `HUWQEM.RESERVED.14` | `HuwrntQueueExemptAmount_Reserved14` | TField |  | Reserved for future use. |
| 8 | `HUWQEM.RESERVED.13` | `HuwrntQueueExemptAmount_Reserved13` | TField |  | Reserved for future use. |
| 9 | `HUWQEM.RESERVED.12` | `HuwrntQueueExemptAmount_Reserved12` | TField |  | Reserved for future use. |
| 10 | `HUWQEM.RESERVED.11` | `HuwrntQueueExemptAmount_Reserved11` | TField |  | Reserved for future use. |
| 11 | `HUWQEM.RESERVED.10` | `HuwrntQueueExemptAmount_Reserved10` | TField |  | Reserved for future use. |
| 12 | `HUWQEM.RESERVED.9` | `HuwrntQueueExemptAmount_Reserved9` | TField |  | Reserved for future use. |
| 13 | `HUWQEM.RESERVED.8` | `HuwrntQueueExemptAmount_Reserved8` | TField |  | Reserved for future use. |
| 14 | `HUWQEM.RESERVED.7` | `HuwrntQueueExemptAmount_Reserved7` | TField |  | Reserved for future use. |
| 15 | `HUWQEM.RESERVED.6` | `HuwrntQueueExemptAmount_Reserved6` | TField |  | Reserved for future use. |
| 16 | `HUWQEM.RESERVED.5` | `HuwrntQueueExemptAmount_Reserved5` | TField |  | Reserved for future use. |
| 17 | `HUWQEM.RESERVED.4` | `HuwrntQueueExemptAmount_Reserved4` | TField |  | Reserved for future use. |
| 18 | `HUWQEM.RESERVED.3` | `HuwrntQueueExemptAmount_Reserved3` | TField |  | Reserved for future use. |
| 19 | `HUWQEM.RESERVED.2` | `HuwrntQueueExemptAmount_Reserved2` | TField |  | Reserved for future use. |
| 20 | `HUWQEM.RESERVED.1` | `HuwrntQueueExemptAmount_Reserved1` | TField |  | Reserved for future use. |
| 21 | `HUWQEM.LOCAL.REF` | `HuwrntQueueExemptAmount_LocalRef` |  |  |  |
