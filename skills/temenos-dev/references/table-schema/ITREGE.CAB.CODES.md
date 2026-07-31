# ITREGE.CAB.CODES — Table Schema

> Source: `INSERTS/I_F.ITREGE.CAB.CODES` in `ITREGE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAB.CODE.FROM.DATE` | `ItregeCabCodes_FromDate` |  |  |  |
| 2 | `CAB.CODE.TO.DATE` | `ItregeCabCodes_ToDate` |  |  |  |
| 3 | `CAB.CODE.TOWN` | `ItregeCabCodes_Town` |  |  |  |
| 4 | `CAB.CODE.CAB.CODE` | `ItregeCabCodes_CabCode` |  |  |  |
| 5 | `CAB.CODE.CAB.OTHER.CODE` | `ItregeCabCodes_CabOtherCode` |  |  |  |
