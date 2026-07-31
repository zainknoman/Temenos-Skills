# RC.RETRY.TRIGGER — Table Schema

> Source: `INSERTS/I_F.RC.RETRY.TRIGGER` in `RC_TransactionCycler.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RC.TRIG.TRIGGER.REF` | `RcRetryTrigger_TriggerRef` | TField |  | Specifies the refernce fo the trigger Specifies the terminal no,Date and Time of trigger The format is 'TerminalNo:"*":CurrentDate:"*":CurrentTime' System updated field |
| 2 | `RC.TRIG.TRIGGER.TYPE` | `RcRetryTrigger_TriggerType` | TField |  | Specifies what has triggered the online retry Like posting of credit entry, removing posting restrictions, unblocking of funds on the settlement account This is a valid override record Displays language specific trigger type System updated field |
| 3 | `RC.TRIG.LOCAL.REF` | `RcRetryTrigger_LocalRef` |  |  |  |
| 4 | `RC.TRIG.RESERVED.10` | `RcRetryTrigger_Reserved10` | TField |  |  |
| 5 | `RC.TRIG.RESERVED.09` | `RcRetryTrigger_Reserved09` | TField |  |  |
| 6 | `RC.TRIG.RESERVED.08` | `RcRetryTrigger_Reserved08` | TField |  |  |
| 7 | `RC.TRIG.RESERVED.07` | `RcRetryTrigger_Reserved07` | TField |  |  |
| 8 | `RC.TRIG.RESERVED.06` | `RcRetryTrigger_Reserved06` | TField |  |  |
| 9 | `RC.TRIG.RESERVED.05` | `RcRetryTrigger_Reserved05` | TField |  |  |
| 10 | `RC.TRIG.RESERVED.04` | `RcRetryTrigger_Reserved04` | TField |  |  |
| 11 | `RC.TRIG.RESERVED.03` | `RcRetryTrigger_Reserved03` | TField |  |  |
| 12 | `RC.TRIG.RESERVED.02` | `RcRetryTrigger_Reserved02` | TField |  |  |
| 13 | `RC.TRIG.RESERVED.01` | `RcRetryTrigger_Reserved01` | TField |  |  |
