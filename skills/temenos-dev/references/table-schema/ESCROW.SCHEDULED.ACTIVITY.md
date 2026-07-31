# ESCROW.SCHEDULED.ACTIVITY — Table Schema

> Source: `INSERTS/I_F.ESCROW.SCHEDULED.ACTIVITY` in `ESCROW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESCROW.SA.ACTIVITY.NAME` | `EscrowScheduledActivity_ActivityName` |  |  |  |
| 2 | `ESCROW.SA.PAYEE.ID` | `EscrowScheduledActivity_PayeeId` |  |  |  |
| 3 | `ESCROW.SA.PAYEE.REF.NO` | `EscrowScheduledActivity_PayeeRefNo` |  |  |  |
| 4 | `ESCROW.SA.LAST.DATE` | `EscrowScheduledActivity_LastDate` |  |  |  |
| 5 | `ESCROW.SA.NEXT.DATE` | `EscrowScheduledActivity_NextDate` |  |  |  |
| 6 | `ESCROW.SA.RESERVED.10` | `EscrowScheduledActivity_Reserved10` |  |  |  |
| 7 | `ESCROW.SA.RESERVED.9` | `EscrowScheduledActivity_Reserved9` |  |  |  |
| 8 | `ESCROW.SA.RESERVED.8` | `EscrowScheduledActivity_Reserved8` |  |  |  |
| 9 | `ESCROW.SA.RESERVED.7` | `EscrowScheduledActivity_Reserved7` |  |  |  |
| 10 | `ESCROW.SA.RESERVED.6` | `EscrowScheduledActivity_Reserved6` |  |  |  |
| 11 | `ESCROW.SA.NEXT.RUN.DATE` | `EscrowScheduledActivity_NextRunDate` | TField |  | Date on which the immediate next activity is scheduled This date is derived from the lowest value of NEXT.DATE |
| 12 | `ESCROW.SA.RESERVED.5` | `EscrowScheduledActivity_Reserved5` | TField |  |  |
| 13 | `ESCROW.SA.RESERVED.4` | `EscrowScheduledActivity_Reserved4` | TField |  |  |
| 14 | `ESCROW.SA.RESERVED.3` | `EscrowScheduledActivity_Reserved3` | TField |  |  |
| 15 | `ESCROW.SA.RESERVED.2` | `EscrowScheduledActivity_Reserved2` | TField |  |  |
| 16 | `ESCROW.SA.RESERVED.1` | `EscrowScheduledActivity_Reserved1` | TField |  |  |
