# INACCT.SCHEDULED.INTEREST.INFO — Table Schema

> Source: `INSERTS/I_F.INACCT.SCHEDULED.INTEREST.INFO` in `INACCT_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INACCT.SCH.INT.INTEREST.PROPERTY` | `InacctScheduledInterestInfo_InterestProperty` |  |  |  |
| 2 | `INACCT.SCH.INT.INTEREST.DUE.DATE` | `InacctScheduledInterestInfo_InterestDueDate` |  |  |  |
| 3 | `INACCT.SCH.INT.INTEREST.CURRENCY` | `InacctScheduledInterestInfo_InterestCurrency` |  |  |  |
| 4 | `INACCT.SCH.INT.INTEREST.AMOUNT` | `InacctScheduledInterestInfo_InterestAmount` |  |  |  |
| 5 | `INACCT.SCH.INT.RESERVED.10` | `InacctScheduledInterestInfo_Reserved10` | TField |  | Reserved for future purpose |
| 6 | `INACCT.SCH.INT.RESERVED.9` | `InacctScheduledInterestInfo_Reserved9` | TField |  | Reserved for future purpose |
| 7 | `INACCT.SCH.INT.RESERVED.8` | `InacctScheduledInterestInfo_Reserved8` | TField |  | Reserved for future purpose |
| 8 | `INACCT.SCH.INT.RESERVED.7` | `InacctScheduledInterestInfo_Reserved7` | TField |  | Reserved for future purpose |
| 9 | `INACCT.SCH.INT.RESERVED.6` | `InacctScheduledInterestInfo_Reserved6` | TField |  | Reserved for future purpose |
| 10 | `INACCT.SCH.INT.RESERVED.5` | `InacctScheduledInterestInfo_Reserved5` | TField |  | Reserved for future purpose |
| 11 | `INACCT.SCH.INT.RESERVED.4` | `InacctScheduledInterestInfo_Reserved4` | TField |  | Reserved for future purpose |
| 12 | `INACCT.SCH.INT.RESERVED.3` | `InacctScheduledInterestInfo_Reserved3` | TField |  | Reserved for future purpose |
| 13 | `INACCT.SCH.INT.RESERVED.2` | `InacctScheduledInterestInfo_Reserved2` | TField |  | Reserved for future purpose |
| 14 | `INACCT.SCH.INT.RESERVED.1` | `InacctScheduledInterestInfo_Reserved1` | TField |  | Reserved for future purpose |
