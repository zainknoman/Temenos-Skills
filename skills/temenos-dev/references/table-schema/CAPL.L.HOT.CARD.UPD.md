# CAPL.L.HOT.CARD.UPD — Table Schema

> Source: `INSERTS/I_F.CAPL.L.HOT.CARD.UPD` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.CARD.HOT.PAN.NO` | `CaplLHotCardUpd_HotPanNo` | TField |  |  |
| 2 | `CP.CARD.HOT.CUSTOMER` | `CaplLHotCardUpd_HotCustomer` | TField |  |  |
| 3 | `CP.CARD.HOT.NAME` | `CaplLHotCardUpd_HotName` | TField |  |  |
| 4 | `CP.CARD.HOT.STATUS` | `CaplLHotCardUpd_HotStatus` | TField |  |  |
| 5 | `CP.CARD.HOT.ERROR` | `CaplLHotCardUpd_HotError` | TField |  |  |
| 6 | `CP.CARD.RESERVED.10` | `CaplLHotCardUpd_Reserved10` | TField |  |  |
| 7 | `CP.CARD.RESERVED.9` | `CaplLHotCardUpd_Reserved9` | TField |  |  |
| 8 | `CP.CARD.RESERVED.8` | `CaplLHotCardUpd_Reserved8` | TField |  |  |
| 9 | `CP.CARD.RESERVED.7` | `CaplLHotCardUpd_Reserved7` | TField |  |  |
| 10 | `CP.CARD.RESERVED.6` | `CaplLHotCardUpd_Reserved6` | TField |  |  |
| 11 | `CP.CARD.RESERVED.5` | `CaplLHotCardUpd_Reserved5` | TField |  |  |
| 12 | `CP.CARD.RESERVED.4` | `CaplLHotCardUpd_Reserved4` | TField |  |  |
| 13 | `CP.CARD.RESERVED.3` | `CaplLHotCardUpd_Reserved3` | TField |  |  |
| 14 | `CP.CARD.RESERVED.2` | `CaplLHotCardUpd_Reserved2` | TField |  |  |
| 15 | `CP.CARD.RESERVED.1` | `CaplLHotCardUpd_Reserved1` | TField |  |  |
| 16 | `CP.CARD.LOCAL.REF` | `CaplLHotCardUpd_LocalRef` |  |  |  |
| 17 | `CP.CARD.OVERRIDE` | `CaplLHotCardUpd_Override` |  |  |  |
