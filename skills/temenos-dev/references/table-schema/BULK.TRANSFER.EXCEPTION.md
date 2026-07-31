# BULK.TRANSFER.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.BULK.TRANSFER.EXCEPTION` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BLK.TRANS.EXCEP.CUSTOMER.NO` | `BulkTransferException_CustomerNo` | TField |  | Customer Number for the arrangement |
| 2 | `BLK.TRANS.EXCEP.AGENT.NUMBER` | `BulkTransferException_AgentNumber` | TField |  | Agent ID involved in Bulk Transfer |
| 3 | `BLK.TRANS.EXCEP.AGENT.ARR.ID` | `BulkTransferException_AgentArrId` | TField |  | Agent Arrangement involved in Bulk Transfer |
| 4 | `BLK.TRANS.EXCEP.ERROR.MESSAGE` | `BulkTransferException_ErrorMessage` | TField |  | Error Message to display the error |
| 5 | `BLK.TRANS.EXCEP.RESERVED.2` | `BulkTransferException_Reserved2` | TField |  |  |
| 6 | `BLK.TRANS.EXCEP.RESERVED.3` | `BulkTransferException_Reserved3` | TField |  |  |
| 7 | `BLK.TRANS.EXCEP.RESERVED.4` | `BulkTransferException_Reserved4` | TField |  |  |
| 8 | `BLK.TRANS.EXCEP.RESERVED.5` | `BulkTransferException_Reserved5` | TField |  |  |
| 9 | `BLK.TRANS.EXCEP.RESERVED.6` | `BulkTransferException_Reserved6` | TField |  |  |
| 10 | `BLK.TRANS.EXCEP.RESERVED.7` | `BulkTransferException_Reserved7` | TField |  |  |
| 11 | `BLK.TRANS.EXCEP.RESERVED.8` | `BulkTransferException_Reserved8` | TField |  |  |
| 12 | `BLK.TRANS.EXCEP.RESERVED.9` | `BulkTransferException_Reserved9` | TField |  |  |
| 13 | `BLK.TRANS.EXCEP.RESERVED.10` | `BulkTransferException_Reserved10` | TField |  |  |
| 14 | `BLK.TRANS.EXCEP.LOCAL.REF` | `BulkTransferException_LocalRef` |  |  |  |
| 15 | `BLK.TRANS.EXCEP.OVERRIDE` | `BulkTransferException_Override` |  |  |  |
