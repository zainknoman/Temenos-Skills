# UKDDMP.DD.COLLECTION.DETAILS — Table Schema

> Source: `INSERTS/I_F.UKDDMP.DD.COLLECTION.DETAILS` in `UKDDMP_Lodgements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DD.COLL.DET.AMOUNT` | `UkddmpDdCollectionDetails_Amount` |  |  |  |
| 2 | `DD.COLL.DET.CREDITOR.ID` | `UkddmpDdCollectionDetails_CreditorId` |  |  |  |
| 3 | `DD.COLL.DET.TRANSACTION.ID` | `UkddmpDdCollectionDetails_TransactionId` |  |  |  |
| 4 | `DD.COLL.DET.STATUS.CODE` | `UkddmpDdCollectionDetails_StatusCode` |  |  |  |
| 5 | `DD.COLL.DET.LOCAL.REF` | `UkddmpDdCollectionDetails_LocalRef` |  |  |  |
| 6 | `DD.COLL.DET.RESERVED.1` | `UkddmpDdCollectionDetails_Reserved1` |  |  |  |
| 7 | `DD.COLL.DET.RESERVED.2` | `UkddmpDdCollectionDetails_Reserved2` |  |  |  |
| 8 | `DD.COLL.DET.RESERVED.3` | `UkddmpDdCollectionDetails_Reserved3` |  |  |  |
| 9 | `DD.COLL.DET.RESERVED.4` | `UkddmpDdCollectionDetails_Reserved4` |  |  |  |
| 10 | `DD.COLL.DET.RESERVED.5` | `UkddmpDdCollectionDetails_Reserved5` |  |  |  |
| 11 | `DD.COLL.DET.RESERVED.6` | `UkddmpDdCollectionDetails_Reserved6` |  |  |  |
| 12 | `DD.COLL.DET.RESERVED.7` | `UkddmpDdCollectionDetails_Reserved7` |  |  |  |
| 13 | `DD.COLL.DET.RESERVED.8` | `UkddmpDdCollectionDetails_Reserved8` |  |  |  |
| 14 | `DD.COLL.DET.RESERVED.9` | `UkddmpDdCollectionDetails_Reserved9` |  |  |  |
| 15 | `DD.COLL.DET.RESERVED.10` | `UkddmpDdCollectionDetails_Reserved10` |  |  |  |
| 16 | `DD.COLL.DET.OVERRIDE` | `UkddmpDdCollectionDetails_Override` |  |  |  |
