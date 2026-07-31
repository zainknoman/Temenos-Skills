# ACH.ORIGIN.ENTRY.LINK — Table Schema

> Source: `INSERTS/I_F.ACH.ORIGIN.ENTRY.LINK` in `ACHFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACHORIG.LINK.ORIGINATOR.ID` | `AchOriginEntryLink_OriginatorId` |  |  |  |
| 2 | `ACHORIG.LINK.WAREHOUSE.ID` | `AchOriginEntryLink_WarehouseId` |  |  |  |
| 3 | `ACHORIG.LINK.RET.WAREHOUSE.ID` | `AchOriginEntryLink_RetWarehouseId` |  |  |  |
| 4 | `ACHORIG.LINK.ORIGIN.SOURCE.REF` | `AchOriginEntryLink_OriginatingSourceRef` |  |  |  |
| 5 | `ACHORIG.LINK.TPH.REFERENCE` | `AchOriginEntryLink_TphReference` |  |  |  |
| 6 | `ACHORIG.LINK.EFFECTIVE.DATE` | `AchOriginEntryLink_EffectiveDate` |  |  |  |
| 7 | `ACHORIG.LINK.RESERVED.17` | `AchOriginEntryLink_Reserved17` |  |  |  |
| 8 | `ACHORIG.LINK.RESERVED.16` | `AchOriginEntryLink_Reserved16` |  |  |  |
| 9 | `ACHORIG.LINK.RESERVED.15` | `AchOriginEntryLink_Reserved15` |  |  |  |
| 10 | `ACHORIG.LINK.RESERVED.14` | `AchOriginEntryLink_Reserved14` |  |  |  |
| 11 | `ACHORIG.LINK.RESERVED.13` | `AchOriginEntryLink_Reserved13` |  |  |  |
| 12 | `ACHORIG.LINK.RESERVED.12` | `AchOriginEntryLink_Reserved12` | TField |  |  |
| 13 | `ACHORIG.LINK.RESERVED.11` | `AchOriginEntryLink_Reserved11` | TField |  |  |
| 14 | `ACHORIG.LINK.RESERVED.10` | `AchOriginEntryLink_Reserved10` | TField |  |  |
| 15 | `ACHORIG.LINK.RESERVED.9` | `AchOriginEntryLink_Reserved9` | TField |  |  |
| 16 | `ACHORIG.LINK.RESERVED.8` | `AchOriginEntryLink_Reserved8` | TField |  |  |
| 17 | `ACHORIG.LINK.RESERVED.7` | `AchOriginEntryLink_Reserved7` | TField |  |  |
| 18 | `ACHORIG.LINK.RESERVED.6` | `AchOriginEntryLink_Reserved6` | TField |  |  |
| 19 | `ACHORIG.LINK.RESERVED.5` | `AchOriginEntryLink_Reserved5` | TField |  |  |
| 20 | `ACHORIG.LINK.RESERVED.4` | `AchOriginEntryLink_Reserved4` | TField |  |  |
| 21 | `ACHORIG.LINK.RESERVED.3` | `AchOriginEntryLink_Reserved3` | TField |  |  |
| 22 | `ACHORIG.LINK.RESERVED.2` | `AchOriginEntryLink_Reserved2` | TField |  |  |
| 23 | `ACHORIG.LINK.RESERVED.1` | `AchOriginEntryLink_Reserved1` | TField |  |  |
| 24 | `ACHORIG.LINK.LOCAL.REF` | `AchOriginEntryLink_LocalRef` |  |  |  |
