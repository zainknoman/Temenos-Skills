# ARACCT.FX.BLACKLIST.LOG — Table Schema

> Source: `INSERTS/I_F.ARACCT.FX.BLACKLIST.LOG` in `ARACCT_FXBlacklistLimitValidation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARACCT.FXBL.CUSTOMER.NUMBER` | `AracctFxBlacklistLog_CustomerNumber` | TField |  | Must be a valid record from CUSTOMER table, existing data on ARACCT.FX.BLACKLIST. |
| 2 | `ARACCT.FXBL.DATE.ATTEMPT` | `AracctFxBlacklistLog_DateAttempt` | TField |  | Indicates the system date when the customer attempt to do a FX transaction. Standard T24 date format. |
| 3 | `ARACCT.FXBL.TIME.ATTEMPT` | `AracctFxBlacklistLog_TimeAttempt` | TField |  | Indicates the system time when the customer attempt to do a FX transaction. Standard T24 time format. |
| 4 | `ARACCT.FXBL.BCRA.REFERENCE` | `AracctFxBlacklistLog_BcraReference` |  |  |  |
| 5 | `ARACCT.FXBL.BLACKLISTED.FROM` | `AracctFxBlacklistLog_BlacklistedFrom` | TField |  | Date that store the starting date of the period of blacklist, existing data on ARACCT.FX.BLACKLIST. |
| 6 | `ARACCT.FXBL.BLACKLISTED.TO` | `AracctFxBlacklistLog_BlacklistedTo` | TField |  | Date that store the ending date of the period of blacklist, existing data on ARACCT.FX.BLACKLIST. |
| 7 | `ARACCT.FXBL.MANUAL.INPUT` | `AracctFxBlacklistLog_ManualInput` | TField |  | Indicate if the record has been uploaded through a file or it has been input manually by the user, existing data on ARACCT.FX.BLACKLIST. |
| 8 | `ARACCT.FXBL.FAILED.TRANSACTION.REF` | `AracctFxBlacklistLog_FailedTransactionRef` | TField |  | Indicate the system failed transaction reference AA activity, PO Id or ATM reference. |
