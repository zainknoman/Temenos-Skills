# LKPVCO.OVERDRAFT.DETAILS — Table Schema

> Source: `INSERTS/I_F.LKPVCO.OVERDRAFT.DETAILS` in `LKPVCO_ProvisioningandCollateral.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OVE.DET.CUMULATIVE.OD.DAYS` | `LkpvcoOverdraftDetails_CumulativeOdDays` | TField |  | To store the cumilative OD days based on account overdue. |
| 2 | `OVE.DET.LOCAL.REF` | `LkpvcoOverdraftDetails_LocalRef` |  |  |  |
| 3 | `OVE.DET.CUST.OD.STATUS` | `LkpvcoOverdraftDetails_CustOdStatus` | TField |  | Valid status as per EB.LOOKUP>AA.OVERDRAFT.STATUS |
| 4 | `70.STATUS` | `70Status` |  |  |  |
| 5 | `OVE.DET.CURR.OD.START.DATE` | `LkpvcoOverdraftDetails_CurrOdStartDate` | TField |  | This field defines the start date of overdraft at customer assert level. |
| 6 | `OVE.DET.OD.CLASS.DATE` | `LkpvcoOverdraftDetails_OdClassDate` | TField |  | To stores todays date if MULTI.OD.CLASSICIATION happens today for specific customer. |
