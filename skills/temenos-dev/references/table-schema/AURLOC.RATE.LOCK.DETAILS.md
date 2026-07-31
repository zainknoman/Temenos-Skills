# AURLOC.RATE.LOCK.DETAILS — Table Schema

> Source: `INSERTS/I_F.AURLOC.RATE.LOCK.DETAILS` in `AURLOC_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RL.RL.INTEREST.RATE` | `AurlocRateLockDetails_RlInterestRate` | TField |  | This field contains the rate lock interest rate. |
| 2 | `RL.RL.FIX.TERM.EXP` | `AurlocRateLockDetails_RlFixTermExp` | TField |  | This field contains the expiry date of the fixed term of the rate lock interest rate. |
| 3 | `RL.LOCAL.REF` | `AurlocRateLockDetails_LocalRef` |  |  |  |
