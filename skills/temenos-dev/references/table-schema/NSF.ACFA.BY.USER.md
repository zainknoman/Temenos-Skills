# NSF.ACFA.BY.USER — Table Schema

> Source: `INSERTS/I_F.NSF.ACFA.BY.USER` in `NSFDES_Alerts.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NSF.USER.ALERT.LEVEL` | `NsfAcfaByUser_AlertLevel` | TField |  | This can be between 1 to 9. This is decided based on Alert Parameter and the time the select had happened. |
| 2 | `NSF.USER.BRANCH` | `NsfAcfaByUser_Branch` |  |  |  |
| 3 | `NSF.USER.NSF.DESK` | `NsfAcfaByUser_NsfDesk` |  |  |  |
| 4 | `NSF.USER.NSF.PENDING` | `NsfAcfaByUser_NsfPending` |  |  |  |
| 5 | `NSF.USER.NSF.PENDING.AMT` | `NsfAcfaByUser_NsfPendingAmt` |  |  |  |
| 6 | `NSF.USER.INFO.ONLY.COUNT` | `NsfAcfaByUser_InfoOnlyCount` |  |  |  |
| 7 | `NSF.USER.INFO.ONLY.AMT` | `NsfAcfaByUser_InfoOnlyAmt` |  |  |  |
| 8 | `NSF.USER.BRANCH.DESK` | `NsfAcfaByUser_BranchDesk` |  |  |  |
| 9 | `NSF.USER.RESERVED.4` | `NsfAcfaByUser_Reserved4` |  |  |  |
| 10 | `NSF.USER.RESERVED.3` | `NsfAcfaByUser_Reserved3` |  |  |  |
| 11 | `NSF.USER.RESERVED.2` | `NsfAcfaByUser_Reserved2` |  |  |  |
| 12 | `NSF.USER.RESERVED.1` | `NsfAcfaByUser_Reserved1` |  |  |  |
