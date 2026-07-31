# DD.MANDATE.RECEIVED.CONCAT — Table Schema

> Source: `INSERTS/I_F.DD.MANDATE.RECEIVED.CONCAT` in `DD_MandateMapping.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DD.MRC.FILE.STATUS` | `DdMandateReceivedConcat_FileStatus` | TField |  |  |
| 2 | `DD.MRC.BULKREF` | `DdMandateReceivedConcat_Bulkref` |  |  |  |
| 3 | `DD.MRC.BULK.STATUS` | `DdMandateReceivedConcat_BulkStatus` |  |  |  |
| 4 | `DD.MRC.RECEIVED.TXN` | `DdMandateReceivedConcat_ReceivedTxn` |  |  |  |
| 5 | `DD.MRC.TXN.STATUS` | `DdMandateReceivedConcat_TxnStatus` |  |  |  |
