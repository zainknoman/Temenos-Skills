# DD.MANDATE.BULK.OUT.CONCAT — Table Schema

> Source: `INSERTS/I_F.DD.MANDATE.BULK.OUT.CONCAT` in `DD_MandateMapping.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DD.MBC.SEQUENCE.NUMBER` | `DdMandateBulkOutConcat_SequenceNumber` | TField |  |  |
| 2 | `DD.MBC.BUSINESS.DATE` | `DdMandateBulkOutConcat_BusinessDate` | TField |  |  |
| 3 | `DD.MBC.MESSAGE.TYPE` | `DdMandateBulkOutConcat_MessageType` |  |  |  |
| 4 | `DD.MBC.SENT.TXN.ID` | `DdMandateBulkOutConcat_SentTxnId` |  |  |  |
