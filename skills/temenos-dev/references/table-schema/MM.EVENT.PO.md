# MM.EVENT.PO — Table Schema

> Source: `INSERTS/I_F.MM.EVENT.PO` in `MM_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `Mmp.ACTIVITY.DATE` | `MmEventPo_ActivityDate` |  |  |  |
| 2 | `Mmp.TYPE` | `MmEventPo_Type` |  |  |  |
| 3 | `Mmp.EVENT.DATE` | `MmEventPo_EventDate` |  |  |  |
| 4 | `Mmp.PO.REFERENCE` | `MmEventPo_PoReference` |  |  |  |
| 5 | `Mmp.RESERVED.9` | `MmEventPo_Reserved9` |  |  |  |
| 6 | `Mmp.RESERVED.8` | `MmEventPo_Reserved8` |  |  |  |
| 7 | `Mmp.RESERVED.7` | `MmEventPo_Reserved7` |  |  |  |
| 8 | `Mmp.RESERVED.6` | `MmEventPo_Reserved6` |  |  |  |
| 9 | `Mmp.FUT.PRIN.DUE.DATE` | `MmEventPo_FutPrinDueDate` |  |  |  |
| 10 | `Mmp.PO.GENERATED.DATE` | `MmEventPo_PoGeneratedDate` |  |  |  |
| 11 | `Mmp.RESERVED.3` | `MmEventPo_Reserved3` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 12 | `Mmp.RESERVED.2` | `MmEventPo_Reserved2` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 13 | `Mmp.RESERVED.1` | `MmEventPo_Reserved1` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 14 | `Mmp.LOCAL.REF` | `MmEventPo_LocalRef` |  |  |  |
