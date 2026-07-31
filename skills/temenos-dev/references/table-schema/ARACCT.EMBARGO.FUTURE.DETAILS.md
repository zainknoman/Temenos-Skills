# ARACCT.EMBARGO.FUTURE.DETAILS — Table Schema

> Source: `INSERTS/I_F.ARACCT.EMBARGO.FUTURE.DETAILS` in `ARACCT_AccountAlias.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARACCT.CUSTOMER` | `AracctEmbargoFutureDetails_Customer` | TField |  | Customer value of the current request |
| 2 | `ARACCT.PENDING.SEIZURE.AMOUNT` | `AracctEmbargoFutureDetails_PendingSeizureAmount` | TField |  | Pending amount that need seized |
| 3 | `ARACCT.ACCOUNTS` | `AracctEmbargoFutureDetails_Accounts` |  |  |  |
| 4 | `ARACCT.EMBARGO.REQUEST` | `AracctEmbargoFutureDetails_EmbargoRequest` |  |  |  |
| 5 | `ARACCT.REQUEST.TYPE` | `AracctEmbargoFutureDetails_RequestType` | TField |  | Type of request Online/Batch |
| 6 | `ARACCT.REFERENCE.ID` | `AracctEmbargoFutureDetails_ReferenceId` | TField |  | Reference Id of the original request |
| 7 | `ARACCT.RESERVATION.ID` | `AracctEmbargoFutureDetails_ReservationId` |  |  |  |
| 8 | `ARACCT.REQUEST.DATE` | `AracctEmbargoFutureDetails_RequestDate` | TField |  |  |
| 9 | `ARACCT.RELEASE.REQUEST` | `AracctEmbargoFutureDetails_ReleaseRequest` | TField |  | Holds the value as yes if Lift of seizure request is received |
