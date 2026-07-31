# FISTLN.KELA.DETAILS — Table Schema

> Source: `INSERTS/I_F.FISTLN.KELA.DETAILS` in `FISTLN_StudentLoan.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `KELA.DETAILS.KELA.SEND.DATE` | `FistlnKelaDetails_KelaSendDate` |  |  |  |
| 2 | `KELA.DETAILS.CONFIRMATION.RECEIVED` | `FistlnKelaDetails_ConfirmationReceived` |  |  |  |
| 3 | `KELA.DETAILS.CONFIRMATION.DATE` | `FistlnKelaDetails_ConfirmationDate` |  |  |  |
| 4 | `KELA.DETAILS.PROCESSED` | `FistlnKelaDetails_Processed` |  |  |  |
| 5 | `KELA.DETAILS.RESERVED.10` | `FistlnKelaDetails_Reserved10` |  |  |  |
| 6 | `KELA.DETAILS.RESERVED.9` | `FistlnKelaDetails_Reserved9` |  |  |  |
| 7 | `KELA.DETAILS.SERVICE.DATE` | `FistlnKelaDetails_ServiceDate` |  |  |  |
| 8 | `KELA.DETAILS.ERROR` | `FistlnKelaDetails_Error` |  |  |  |
| 9 | `KELA.DETAILS.LOCAL.REF` | `FistlnKelaDetails_LocalRef` |  |  |  |
| 10 | `KELA.DETAILS.RESERVED.8` | `FistlnKelaDetails_Reserved8` | TField |  |  |
| 11 | `KELA.DETAILS.RESERVED.7` | `FistlnKelaDetails_Reserved7` | TField |  |  |
| 12 | `KELA.DETAILS.RESERVED.6` | `FistlnKelaDetails_Reserved6` | TField |  |  |
| 13 | `KELA.DETAILS.RESERVED.5` | `FistlnKelaDetails_Reserved5` | TField |  |  |
| 14 | `KELA.DETAILS.RESERVED.4` | `FistlnKelaDetails_Reserved4` | TField |  |  |
| 15 | `KELA.DETAILS.RESERVED.3` | `FistlnKelaDetails_Reserved3` | TField |  |  |
| 16 | `KELA.DETAILS.RESERVED.2` | `FistlnKelaDetails_Reserved2` | TField |  |  |
| 17 | `KELA.DETAILS.RESERVED.1` | `FistlnKelaDetails_Reserved1` | TField |  |  |
| 18 | `KELA.DETAILS.OVERRIDE` | `FistlnKelaDetails_Override` |  |  |  |
| 19 | `KELA.DETAILS.RECORD.STATUS` | `FistlnKelaDetails_RecordStatus` | String |  |  |
| 20 | `KELA.DETAILS.CURR.NO` | `FistlnKelaDetails_CurrNo` | String |  |  |
| 21 | `KELA.DETAILS.INPUTTER` | `FistlnKelaDetails_Inputter` |  |  |  |
| 22 | `KELA.DETAILS.DATE.TIME` | `FistlnKelaDetails_DateTime` |  |  |  |
| 23 | `KELA.DETAILS.AUTHORISER` | `FistlnKelaDetails_Authoriser` | String |  |  |
| 24 | `KELA.DETAILS.CO.CODE` | `FistlnKelaDetails_CoCode` | String |  |  |
| 25 | `KELA.DETAILS.DEPT.CODE` | `FistlnKelaDetails_DeptCode` | String |  |  |
| 26 | `KELA.DETAILS.AUDITOR.CODE` | `FistlnKelaDetails_AuditorCode` | String |  |  |
| 27 | `KELA.DETAILS.AUDIT.DATE.TIME` | `FistlnKelaDetails_AuditDateTime` | String |  |  |
