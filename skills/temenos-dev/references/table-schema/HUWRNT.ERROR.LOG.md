# HUWRNT.ERROR.LOG — Table Schema

> Source: `INSERTS/I_F.HUWRNT.ERROR.LOG` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUWERR.ERROR.DATE.TIME` | `HuwrntErrorLog_ErrorDateTime` |  |  |  |
| 2 | `HUWERR.AMOUNT` | `HuwrntErrorLog_Amount` |  |  |  |
| 3 | `HUWERR.ERROR.REASON` | `HuwrntErrorLog_ErrorReason` |  |  |  |
| 4 | `HUWERR.RESERVED.15` | `HuwrntErrorLog_Reserved15` |  |  |  |
| 5 | `HUWERR.RESERVED.14` | `HuwrntErrorLog_Reserved14` | TField |  | Reserved for future use. |
| 6 | `HUWERR.RESERVED.13` | `HuwrntErrorLog_Reserved13` | TField |  | Reserved for future use. |
| 7 | `HUWERR.RESERVED.12` | `HuwrntErrorLog_Reserved12` | TField |  | Reserved for future use. |
| 8 | `HUWERR.RESERVED.11` | `HuwrntErrorLog_Reserved11` | TField |  | Reserved for future use. |
| 9 | `HUWERR.RESERVED.10` | `HuwrntErrorLog_Reserved10` | TField |  | Reserved for future use. |
| 10 | `HUWERR.RESERVED.9` | `HuwrntErrorLog_Reserved9` | TField |  | Reserved for future use. |
| 11 | `HUWERR.RESERVED.8` | `HuwrntErrorLog_Reserved8` | TField |  | Reserved for future use. |
| 12 | `HUWERR.RESERVED.7` | `HuwrntErrorLog_Reserved7` | TField |  | Reserved for future use. |
| 13 | `HUWERR.RESERVED.6` | `HuwrntErrorLog_Reserved6` | TField |  | Reserved for future use. |
| 14 | `HUWERR.RESERVED.5` | `HuwrntErrorLog_Reserved5` | TField |  | Reserved for future use. |
| 15 | `HUWERR.RESERVED.4` | `HuwrntErrorLog_Reserved4` | TField |  | Reserved for future use. |
| 16 | `HUWERR.RESERVED.3` | `HuwrntErrorLog_Reserved3` | TField |  | Reserved for future use. |
| 17 | `HUWERR.RESERVED.2` | `HuwrntErrorLog_Reserved2` | TField |  | Reserved for future use. |
| 18 | `HUWERR.RESERVED.1` | `HuwrntErrorLog_Reserved1` | TField |  | Reserved for future use. |
