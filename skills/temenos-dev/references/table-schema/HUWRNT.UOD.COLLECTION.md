# HUWRNT.UOD.COLLECTION — Table Schema

> Source: `INSERTS/I_F.HUWRNT.UOD.COLLECTION` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUWRNT.UODCOL.ACCOUNT.NO` | `HuwrntUodCollection_AccountNo` |  |  |  |
| 2 | `HUWRNT.UODCOL.DATE` | `HuwrntUodCollection_Date` |  |  |  |
| 3 | `HUWRNT.UODCOL.AMOUNT.COLLECTED` | `HuwrntUodCollection_AmountCollected` |  |  |  |
| 4 | `HUWRNT.UODCOL.FORCED.COLL.AVL.AMT` | `HuwrntUodCollection_ForcedCollAvlAmt` |  |  |  |
| 5 | `HUWRNT.UODCOL.QUEUE.REFERENCE` | `HuwrntUodCollection_QueueReference` |  |  |  |
| 6 | `HUWRNT.UODCOL.ACC.NO.COLL` | `HuwrntUodCollection_AccNoColl` |  |  |  |
| 7 | `HUWRNT.UODCOL.DATE.COLLECTED` | `HuwrntUodCollection_DateCollected` |  |  |  |
| 8 | `HUWRNT.UODCOL.ACC.COLLECTED.AMT` | `HuwrntUodCollection_AccCollectedAmt` |  |  |  |
| 9 | `HUWRNT.UODCOL.RESERVED.11` | `HuwrntUodCollection_Reserved11` | TField |  | Reserved for future use. |
| 10 | `HUWRNT.UODCOL.RESERVED.10` | `HuwrntUodCollection_Reserved10` | TField |  | Reserved for future use. |
| 11 | `HUWRNT.UODCOL.RESERVED.9` | `HuwrntUodCollection_Reserved9` | TField |  | Reserved for future use. |
| 12 | `HUWRNT.UODCOL.RESERVED.8` | `HuwrntUodCollection_Reserved8` | TField |  | Reserved for future use. |
| 13 | `HUWRNT.UODCOL.RESERVED.7` | `HuwrntUodCollection_Reserved7` | TField |  | Reserved for future use. |
| 14 | `HUWRNT.UODCOL.RESERVED.6` | `HuwrntUodCollection_Reserved6` | TField |  | Reserved for future use. |
| 15 | `HUWRNT.UODCOL.RESERVED.5` | `HuwrntUodCollection_Reserved5` | TField |  | Reserved for future use. |
| 16 | `HUWRNT.UODCOL.RESERVED.4` | `HuwrntUodCollection_Reserved4` | TField |  | Reserved for future use. |
| 17 | `HUWRNT.UODCOL.RESERVED.3` | `HuwrntUodCollection_Reserved3` | TField |  | Reserved for future use. |
| 18 | `HUWRNT.UODCOL.RESERVED.2` | `HuwrntUodCollection_Reserved2` | TField |  | Reserved for future use. |
| 19 | `HUWRNT.UODCOL.RESERVED.1` | `HuwrntUodCollection_Reserved1` | TField |  | Reserved for future use. |
| 20 | `HUWRNT.UODCOL.LOCAL.REF` | `HuwrntUodCollection_LocalRef` |  |  |  |
