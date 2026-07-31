# TNCUIN.LOCK.DETAILS — Table Schema

> Source: `INSERTS/I_F.TNCUIN.LOCK.DETAILS` in `TNCUIN_Garnishment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TNCUIN.LOCK.DET.LOCK.ID` | `TncuinLockDetails_LockId` |  |  |  |
| 2 | `TNCUIN.LOCK.DET.LOCAL.REF` | `TncuinLockDetails_LocalRef` |  |  |  |
| 3 | `TNCUIN.LOCK.DET.GARNISH.BALANCE` | `TncuinLockDetails_GarnishBalance` | TField |  | This field stores the balance of the Garnishment amount which is not locked |
| 4 | `TNCUIN.LOCK.DET.RESERVED.4` | `TncuinLockDetails_Reserved4` | TField |  | Reserved field for future use |
| 5 | `TNCUIN.LOCK.DET.RESERVED.3` | `TncuinLockDetails_Reserved3` | TField |  | Reserved field for future use |
| 6 | `TNCUIN.LOCK.DET.RESERVED.2` | `TncuinLockDetails_Reserved2` | TField |  | Reserved field for future use |
| 7 | `TNCUIN.LOCK.DET.RESERVED.1` | `TncuinLockDetails_Reserved1` | TField |  | Reserved field for future use |
