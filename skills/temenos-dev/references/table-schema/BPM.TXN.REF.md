# BPM.TXN.REF — Table Schema

> Source: `INSERTS/I_F.BPM.TXN.REF` in `JP_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `JP.BPM.TXN.REF` | `BpmTxnRef_TxnRef` | TField |  | BPM.TXN.REF TXN.REF The system creates the Transaction Reference id for each activity when they are committed Validation Rules System Maintained. No-input. |
| 2 | `JP.BPM.TASK.TARGET` | `BpmTxnRef_TaskTarget` | TField |  | BPM.TXN.REF TASK.TARGET This field holds the T24 Application/Version/Enquiry and Function which should be presented to the USER upon the execution of the Activity i.e. the Application/version/Enquiry associated with the Activity. Validation Rules System Maintained. No-input. |
| 3 | `JP.BPM.TASK.STATUS` | `BpmTxnRef_TaskStatus` | TField |  | PW.ACTIVITY SHORT.DESC This field indicates the status of the activity executed Validation Rules System Maintained. No-input. |
| 4 | `JP.BPM.PROCESS.NO` | `BpmTxnRef_ProcessNo` | TField |  |  |
| 5 | `JP.BPM.RESERVED.5` | `BpmTxnRef_Reserved5` | TField |  |  |
| 6 | `JP.BPM.RESERVED.4` | `BpmTxnRef_Reserved4` | TField |  |  |
| 7 | `JP.BPM.RESERVED.3` | `BpmTxnRef_Reserved3` | TField |  |  |
| 8 | `JP.BPM.RESERVED.2` | `BpmTxnRef_Reserved2` | TField |  |  |
| 9 | `JP.BPM.RESERVED.1` | `BpmTxnRef_Reserved1` | TField |  |  |
