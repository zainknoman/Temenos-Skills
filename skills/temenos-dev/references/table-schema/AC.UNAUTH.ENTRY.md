# AC.UNAUTH.ENTRY — Table Schema

> Source: `INSERTS/I_F.AC.UNAUTH.ENTRY` in `AC_BalanceUpdates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.AUE.ENTRY.KEY` | `AcUnauthEntry_EntryKey` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
