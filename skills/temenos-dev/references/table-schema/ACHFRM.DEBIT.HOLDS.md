# ACHFRM.DEBIT.HOLDS — Table Schema

> Source: `INSERTS/I_F.ACHFRM.DEBIT.HOLDS` in `ACHFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACH.DR.HOLDS.LOCK.ID` | `AchfrmDebitHolds_LockId` | TField |  | Holds the id of AC.LOCKED.EVENTS |
| 2 | `ACH.DR.HOLDS.EXPIRY.DATE` | `AchfrmDebitHolds_ExpiryDate` | TField |  | The expiry date of locked event. The date in which the funds will be released |
| 3 | `ACH.DR.HOLDS.LOCKED.AMOUNT` | `AchfrmDebitHolds_LockedAmount` | TField |  | The amount of funds that will be locked in the account |
| 4 | `ACH.DR.HOLDS.RESERVED.5` | `AchfrmDebitHolds_Reserved5` | TField |  |  |
| 5 | `ACH.DR.HOLDS.RESERVED.4` | `AchfrmDebitHolds_Reserved4` | TField |  |  |
| 6 | `ACH.DR.HOLDS.RESERVED.3` | `AchfrmDebitHolds_Reserved3` | TField |  |  |
| 7 | `ACH.DR.HOLDS.RESERVED.2` | `AchfrmDebitHolds_Reserved2` | TField |  |  |
| 8 | `ACH.DR.HOLDS.RESERVED.1` | `AchfrmDebitHolds_Reserved1` | TField |  |  |
