# POR.BALANCECHECKRESPONSE — Table Schema

> Source: `INSERTS/I_F.POR.BALANCECHECKRESPONSE` in `PP_BalanceCheckService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `POBCR.CompanyID` | `PorBalancecheckresponse_Companyid` |  |  |  |
| 2 | `POBCR.FTNumber` | `PorBalancecheckresponse_Ftnumber` |  |  |  |
| 3 | `POBCR.ReservationKey` | `PorBalancecheckresponse_Reservationkey` |  |  |  |
| 4 | `POBCR.ReturnCode` | `PorBalancecheckresponse_Returncode` |  |  |  |
| 5 | `POBCR.ReturnReasonDescription` | `PorBalancecheckresponse_Returnreasondescription` |  |  |  |
| 6 | `POBCR.ErrorCode` | `PorBalancecheckresponse_Errorcode` |  |  |  |
| 7 | `POBCR.ErrorDetails` | `PorBalancecheckresponse_Errordetails` |  |  |  |
| 8 | `POBCR.Indicator` | `PorBalancecheckresponse_Indicator` |  |  |  |
| 9 | `POBCR.AccountNumber` | `PorBalancecheckresponse_Accountnumber` |  |  |  |
