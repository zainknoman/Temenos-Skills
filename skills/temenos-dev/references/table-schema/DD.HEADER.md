# DD.HEADER — Table Schema

> Source: `INSERTS/I_F.DD.HEADER` in `DD_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DD.HDR.DIRECTION` | `DdHeader_Direction` |  |  |  |
| 2 | `DD.HDR.CLEARING.SYSTEM` | `DdHeader_ClearingSystem` |  |  |  |
| 3 | `DD.HDR.SYS.DATE.TIME` | `DdHeader_SysDateTime` |  |  |  |
| 4 | `DD.HDR.OPERATOR` | `DdHeader_Operator` |  |  |  |
| 5 | `DD.HDR.RECORD.ID` | `DdHeader_RecordId` |  |  |  |
| 6 | `DD.HDR.NO.RECORDS` | `DdHeader_NoRecords` |  |  |  |
| 7 | `DD.HDR.TOT.AMOUNT` | `DdHeader_TotAmount` |  |  |  |
| 8 | `DD.HDR.DELIVERY.REF.ID` | `DdHeader_DeliveryRefId` |  |  |  |
| 9 | `DD.HDR.RESERVED.1` | `DdHeader_Reserved1` |  |  |  |
