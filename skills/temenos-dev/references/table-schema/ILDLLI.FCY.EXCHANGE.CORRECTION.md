# ILDLLI.FCY.EXCHANGE.CORRECTION — Table Schema

> Source: `INSERTS/I_F.ILDLLI.FCY.EXCHANGE.CORRECTION` in `ILDLLI_CpiFcyLinkedInterest.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FCY.ECH.ACCURAL.DATE` | `IldlliFcyExchangeCorrection_AccuralDate` |  |  |  |
| 2 | `FCY.ECH.DAILY.CORRECTION.AMOUNT` | `IldlliFcyExchangeCorrection_DailyCorrectionAmount` |  |  |  |
| 3 | `FCY.ECH.TOTAL.CORRECTION.AMOUNT` | `IldlliFcyExchangeCorrection_TotalCorrectionAmount` | TField |  | This field holds the total correct amount for the schedule period. |
| 4 | `FCY.ECH.RESERVED.10` | `IldlliFcyExchangeCorrection_Reserved10` | TField |  |  |
| 5 | `FCY.ECH.RESERVED.9` | `IldlliFcyExchangeCorrection_Reserved9` | TField |  |  |
| 6 | `FCY.ECH.RESERVED.8` | `IldlliFcyExchangeCorrection_Reserved8` | TField |  |  |
| 7 | `FCY.ECH.RESERVED.7` | `IldlliFcyExchangeCorrection_Reserved7` | TField |  |  |
| 8 | `FCY.ECH.RESERVED.6` | `IldlliFcyExchangeCorrection_Reserved6` | TField |  |  |
| 9 | `FCY.ECH.RESERVED.5` | `IldlliFcyExchangeCorrection_Reserved5` | TField |  |  |
| 10 | `FCY.ECH.RESERVED.4` | `IldlliFcyExchangeCorrection_Reserved4` | TField |  |  |
| 11 | `FCY.ECH.RESERVED.3` | `IldlliFcyExchangeCorrection_Reserved3` | TField |  |  |
| 12 | `FCY.ECH.RESERVED.2` | `IldlliFcyExchangeCorrection_Reserved2` | TField |  |  |
| 13 | `FCY.ECH.RESERVED.1` | `IldlliFcyExchangeCorrection_Reserved1` | TField |  |  |
