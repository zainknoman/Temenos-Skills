# CL.AGENCY.COMMISSION — Table Schema

> Source: `INSERTS/I_F.CL.AGENCY.COMMISSION` in `CL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CL.AGCOMM.APAY.NUMBER` | `ClAgencyCommission_ApayNumber` | TField |  | Number of payments received through the external agency during the month. |
| 2 | `CL.AGCOMM.APAY.AMT` | `ClAgencyCommission_ApayAmt` | TField |  | Total amount of payments received through the external agency during the month. |
| 3 | `CL.AGCOMM.APAY.COMMISSION` | `ClAgencyCommission_ApayCommission` | TField |  | This is the monthly commission to pay to the external agency for the payments received through it. |
| 4 | `CL.AGCOMM.ASAL.NUMBER` | `ClAgencyCommission_AsalNumber` | TField |  | Number of salary assignment obtained through the external agency during the month. |
| 5 | `CL.AGCOMM.ASAL.OSTANDING.AMT` | `ClAgencyCommission_AsalOstandingAmt` | TField |  | Total outstanding amount for the salary assignment obtained through the external agency during the month. |
| 6 | `CL.AGCOMM.ASAL.COMMISSION` | `ClAgencyCommission_AsalCommission` | TField |  | This is the monthly commission to pay to the external agency for the assignment of salary obtained through it. |
| 7 | `CL.AGCOMM.TOT.COMMISSION` | `ClAgencyCommission_TotCommission` | TField |  | sum of the APAY and ASAL commissions. |
| 8 | `CL.AGCOMM.AGENCY.NO` | `ClAgencyCommission_AgencyNo` | TField |  | First component of the ID. |
| 9 | `CL.AGCOMM.RESERVED.5` | `ClAgencyCommission_Reserved5` | TField |  |  |
| 10 | `CL.AGCOMM.RESERVED.4` | `ClAgencyCommission_Reserved4` | TField |  |  |
| 11 | `CL.AGCOMM.RESERVED.3` | `ClAgencyCommission_Reserved3` | TField |  |  |
| 12 | `CL.AGCOMM.RESERVED.2` | `ClAgencyCommission_Reserved2` | TField |  |  |
| 13 | `CL.AGCOMM.RESERVED.1` | `ClAgencyCommission_Reserved1` | TField |  |  |
