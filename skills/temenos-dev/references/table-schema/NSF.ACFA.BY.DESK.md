# NSF.ACFA.BY.DESK — Table Schema

> Source: `INSERTS/I_F.NSF.ACFA.BY.DESK` in `NSFDES_Alerts.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NSF.DESK.ALERT.LEVEL` | `NsfAcfaByDesk_AlertLevel` | TField |  | This can be between 1 to 9. This is decided based on Alert Parameter and the time the select had happened. |
| 2 | `NSF.DESK.BRANCH` | `NsfAcfaByDesk_Branch` |  |  |  |
| 3 | `NSF.DESK.NSF.PENDING` | `NsfAcfaByDesk_NsfPending` |  |  |  |
| 4 | `NSF.DESK.NSF.PENDING.AMT` | `NsfAcfaByDesk_NsfPendingAmt` |  |  |  |
| 5 | `NSF.DESK.INFO.ONLY.COUNT` | `NsfAcfaByDesk_InfoOnlyCount` |  |  |  |
| 6 | `NSF.DESK.INFO.ONLY.AMT` | `NsfAcfaByDesk_InfoOnlyAmt` |  |  |  |
| 7 | `NSF.DESK.RESERVED.4` | `NsfAcfaByDesk_Reserved4` |  |  |  |
| 8 | `NSF.DESK.RESERVED.3` | `NsfAcfaByDesk_Reserved3` |  |  |  |
| 9 | `NSF.DESK.RESERVED.2` | `NsfAcfaByDesk_Reserved2` |  |  |  |
| 10 | `NSF.DESK.RESERVED.1` | `NsfAcfaByDesk_Reserved1` |  |  |  |
