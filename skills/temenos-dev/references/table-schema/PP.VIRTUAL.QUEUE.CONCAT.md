# PP.VIRTUAL.QUEUE.CONCAT — Table Schema

> Source: `INSERTS/I_F.PP.VIRTUAL.QUEUE.CONCAT` in `PP_InquiryGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.QC.QUEUE.NAME` | `PpVirtualQueueConcat_QueueName` | TField |  |  |
| 2 | `PP.QC.QUEUE.DESCRIPTION` | `PpVirtualQueueConcat_QueueDescription` | TField |  |  |
| 3 | `PP.QC.QUEUE.COMPANY` | `PpVirtualQueueConcat_QueueCompany` |  |  |  |
| 4 | `PP.QC.NO.OF.RECORDS` | `PpVirtualQueueConcat_NoOfRecords` |  |  |  |
| 5 | `PP.QC.RECORD.IDS` | `PpVirtualQueueConcat_RecordIds` |  |  |  |
| 6 | `PP.QC.TIMESTAMP` | `PpVirtualQueueConcat_Timestamp` | TField |  |  |
