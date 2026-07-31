# CBVTMS.SERIAL.NUMBER — Table Schema

> Source: `INSERTS/I_F.CBVTMS.SERIAL.NUMBER` in `CBVTMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `VTMS.RESERVED.1` | `CbvtmsSerialNumber_Reserved1` | TField |  | The Request ID which has been raised to the printers. |
| 2 | `VTMS.RESERVED.2` | `CbvtmsSerialNumber_Reserved2` |  |  |  |
| 3 | `VTMS.RESERVED.3` | `CbvtmsSerialNumber_Reserved3` |  |  |  |
| 4 | `VTMS.RESERVED.4` | `CbvtmsSerialNumber_Reserved4` |  |  |  |
| 5 | `VTMS.LOCAL.REF` | `CbvtmsSerialNumber_LocalRef` |  |  |  |
| 6 | `VTMS.RECEIPT.DATE` | `CbvtmsSerialNumber_ReceiptDate` |  |  |  |
| 7 | `VTMS.RECEIPT.FIXED.SERIAL` | `CbvtmsSerialNumber_ReceiptFixedSerial` |  |  |  |
| 8 | `VTMS.RECEIPT.FROM.SERIAL` | `CbvtmsSerialNumber_ReceiptFromSerial` |  |  |  |
| 9 | `VTMS.RECEIPT.TO.SERIAL` | `CbvtmsSerialNumber_ReceiptToSerial` |  |  |  |
| 10 | `VTMS.ISSUE.DATE` | `CbvtmsSerialNumber_IssueDate` |  |  |  |
| 11 | `VTMS.OVERRIDE` | `CbvtmsSerialNumber_Override` |  |  |  |
| 12 | `VTMS.RECORD.STATUS` | `CbvtmsSerialNumber_RecordStatus` | String |  |  |
| 13 | `VTMS.CURR.NO` | `CbvtmsSerialNumber_CurrNo` | String |  |  |
| 14 | `VTMS.INPUTTER` | `CbvtmsSerialNumber_Inputter` |  |  |  |
| 15 | `VTMS.DATE.TIME` | `CbvtmsSerialNumber_DateTime` |  |  |  |
| 16 | `VTMS.AUTHORISER` | `CbvtmsSerialNumber_Authoriser` | String |  |  |
| 17 | `VTMS.CO.CODE` | `CbvtmsSerialNumber_CoCode` | String |  |  |
| 18 | `VTMS.DEPT.CODE` | `CbvtmsSerialNumber_DeptCode` | String |  |  |
| 19 | `VTMS.AUDITOR.CODE` | `CbvtmsSerialNumber_AuditorCode` | String |  |  |
| 20 | `VTMS.AUDIT.DATE.TIME` | `CbvtmsSerialNumber_AuditDateTime` | String |  |  |
| 21 | `VTMS.ISSUE.FIXED.SERIAL` | `CbvtmsSerialNumber_IssueFixedSerial` |  |  |  |
| 22 | `VTMS.ISSUE.FROM.SERIAL` | `CbvtmsSerialNumber_IssueFromSerial` |  |  |  |
| 23 | `VTMS.ISSUE.TO.SERIAL` | `CbvtmsSerialNumber_IssueToSerial` |  |  |  |
