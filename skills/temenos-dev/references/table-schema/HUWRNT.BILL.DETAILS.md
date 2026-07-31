# HUWRNT.BILL.DETAILS — Table Schema

> Source: `INSERTS/I_F.HUWRNT.BILL.DETAILS` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUBILL.QUEUE.REFERENCE` | `HuwrntBillDetails_QueueReference` |  |  |  |
| 2 | `HUBILL.BILL.ID` | `HuwrntBillDetails_BillId` |  |  |  |
| 3 | `HUBILL.BILL.DATE` | `HuwrntBillDetails_BillDate` |  |  |  |
| 4 | `HUBILL.BILL.AMOUNT` | `HuwrntBillDetails_BillAmount` |  |  |  |
| 5 | `HUBILL.LOCAL.REF` | `HuwrntBillDetails_LocalRef` |  |  |  |
