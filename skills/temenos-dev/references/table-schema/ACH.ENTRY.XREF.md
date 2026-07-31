# ACH.ENTRY.XREF — Table Schema

> Source: `INSERTS/I_F.ACH.ENTRY.XREF` in `ACHFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACH.XREF.ENTRY.ID` | `AchEntryXref_EntryId` | TField |  | To capture the relevant ACH entries id. |
| 2 | `ACH.XREF.POSTING.DATE` | `AchEntryXref_PostingDate` | TField |  | To capture the transaction posting date. |
| 3 | `ACH.XREF.RESERVED.20` | `AchEntryXref_Reserved20` | TField |  |  |
| 4 | `ACH.XREF.RESERVED.19` | `AchEntryXref_Reserved19` | TField |  |  |
| 5 | `ACH.XREF.RESERVED.18` | `AchEntryXref_Reserved18` | TField |  |  |
| 6 | `ACH.XREF.RESERVED.17` | `AchEntryXref_Reserved17` | TField |  |  |
| 7 | `ACH.XREF.RESERVED.16` | `AchEntryXref_Reserved16` | TField |  |  |
| 8 | `ACH.XREF.RESERVED.15` | `AchEntryXref_Reserved15` | TField |  |  |
| 9 | `ACH.XREF.RESERVED.14` | `AchEntryXref_Reserved14` | TField |  |  |
| 10 | `ACH.XREF.RESERVED.13` | `AchEntryXref_Reserved13` | TField |  |  |
| 11 | `ACH.XREF.RESERVED.12` | `AchEntryXref_Reserved12` | TField |  |  |
| 12 | `ACH.XREF.RESERVED.11` | `AchEntryXref_Reserved11` | TField |  |  |
| 13 | `ACH.XREF.RESERVED.10` | `AchEntryXref_Reserved10` | TField |  |  |
| 14 | `ACH.XREF.RESERVED.9` | `AchEntryXref_Reserved9` | TField |  |  |
| 15 | `ACH.XREF.RESERVED.8` | `AchEntryXref_Reserved8` | TField |  |  |
| 16 | `ACH.XREF.RESERVED.7` | `AchEntryXref_Reserved7` | TField |  |  |
| 17 | `ACH.XREF.RESERVED.6` | `AchEntryXref_Reserved6` | TField |  |  |
| 18 | `ACH.XREF.RESERVED.5` | `AchEntryXref_Reserved5` | TField |  |  |
| 19 | `ACH.XREF.RESERVED.4` | `AchEntryXref_Reserved4` | TField |  |  |
| 20 | `ACH.XREF.RESERVED.3` | `AchEntryXref_Reserved3` | TField |  |  |
| 21 | `ACH.XREF.RESERVED.2` | `AchEntryXref_Reserved2` | TField |  |  |
| 22 | `ACH.XREF.RESERVED.1` | `AchEntryXref_Reserved1` | TField |  |  |
