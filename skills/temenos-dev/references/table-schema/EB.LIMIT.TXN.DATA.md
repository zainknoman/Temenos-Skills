# EB.LIMIT.TXN.DATA — Table Schema

> Source: `INSERTS/I_F.EB.LIMIT.TXN.DATA` in `BF_LimitExtTxn.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.LIM.NAU.DATA` | `EbLimitTxnData_NauData` |  |  |  |
| 2 | `EB.LIM.AUT.DATA` | `EbLimitTxnData_AutData` |  |  |  |
| 3 | `EB.LIM.NAU.LIMIT.ACTION` | `EbLimitTxnData_NauLimitAction` |  |  |  |
