# ARGNPV.CUSTOMER.RECLASSIFICATION — Table Schema

> Source: `INSERTS/I_F.ARGNPV.CUSTOMER.RECLASSIFICATION` in `ARGNPV_CustomerReclassification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARGNPV.CLASS.IDENTIFICATION.TYPE` | `ArgnpvCustomerReclassification_IdentificationType` | TField |  | The type of identification 11 will be used to inform CUIT/CUIL or CDI. Types of identification "98" and "99" will be used for resident debtors abroad that are legal entities and individuals respectively, that do not meet the fiscal identification key. |
| 2 | `ARGNPV.CLASS.IDENTIFICATION.NUMBER` | `ArgnpvCustomerReclassification_IdentificationNumber` | TField |  | ID number ( CUIT,CUIL or CDI) |
| 3 | `ARGNPV.CLASS.DENOMINATION` | `ArgnpvCustomerReclassification_Denomination` | TField |  | To store the Denomination description from the Moros file |
| 4 | `ARGNPV.CLASS.ENTITY.CODE` | `ArgnpvCustomerReclassification_EntityCode` |  |  |  |
| 5 | `ARGNPV.CLASS.INFORMATION.DATE` | `ArgnpvCustomerReclassification_InformationDate` |  |  |  |
| 6 | `ARGNPV.CLASS.ECONOMIC.ACTIVITY` | `ArgnpvCustomerReclassification_EconomicActivity` |  |  |  |
| 7 | `ARGNPV.CLASS.SITUATION` | `ArgnpvCustomerReclassification_Situation` |  |  |  |
| 8 | `ARGNPV.CLASS.TOTAL.LOANS` | `ArgnpvCustomerReclassification_TotalLoans` |  |  |  |
| 9 | `ARGNPV.CLASS.PARTICIPATIONS` | `ArgnpvCustomerReclassification_Participations` |  |  |  |
| 10 | `ARGNPV.CLASS.LOANS.GRANTED` | `ArgnpvCustomerReclassification_LoansGranted` |  |  |  |
| 11 | `ARGNPV.CLASS.OTHER.CONCEPTS` | `ArgnpvCustomerReclassification_OtherConcepts` |  |  |  |
| 12 | `ARGNPV.CLASS.PREFERRED.LOANS.A` | `ArgnpvCustomerReclassification_PreferredLoansA` |  |  |  |
| 13 | `ARGNPV.CLASS.PREFERRED.LOANS.B` | `ArgnpvCustomerReclassification_PreferredLoansB` |  |  |  |
| 14 | `ARGNPV.CLASS.NO.PREFERRED.LOANS` | `ArgnpvCustomerReclassification_NoPreferredLoans` |  |  |  |
| 15 | `ARGNPV.CLASS.COUNTER.LOANS.A` | `ArgnpvCustomerReclassification_CounterLoansA` |  |  |  |
| 16 | `ARGNPV.CLASS.COUNTER.LOANS.B` | `ArgnpvCustomerReclassification_CounterLoansB` |  |  |  |
| 17 | `ARGNPV.CLASS.NO.COUNTER.LOANS` | `ArgnpvCustomerReclassification_NoCounterLoans` |  |  |  |
| 18 | `ARGNPV.CLASS.FORECAST` | `ArgnpvCustomerReclassification_Forecast` |  |  |  |
| 19 | `ARGNPV.CLASS.DEBT.COVERED` | `ArgnpvCustomerReclassification_DebtCovered` |  |  |  |
| 20 | `ARGNPV.CLASS.JUDICIAL.REVIEW` | `ArgnpvCustomerReclassification_JudicialReview` |  |  |  |
| 21 | `ARGNPV.CLASS.REFINANCES` | `ArgnpvCustomerReclassification_Refinances` |  |  |  |
| 22 | `ARGNPV.CLASS.MANDATORY.CATEGORIZATION` | `ArgnpvCustomerReclassification_MandatoryCategorization` |  |  |  |
| 23 | `ARGNPV.CLASS.LEGAL.SITUATION` | `ArgnpvCustomerReclassification_LegalSituation` |  |  |  |
| 24 | `ARGNPV.CLASS.UNRECOVERABLE.PROVISION` | `ArgnpvCustomerReclassification_UnrecoverableProvision` |  |  |  |
| 25 | `ARGNPV.CLASS.DELAY.DAYS` | `ArgnpvCustomerReclassification_DelayDays` |  |  |  |
| 26 | `ARGNPV.CLASS.RESERVED.10` | `ArgnpvCustomerReclassification_Reserved10` | TField |  | Reserved for Future use. |
| 27 | `ARGNPV.CLASS.RESERVED.9` | `ArgnpvCustomerReclassification_Reserved9` | TField |  | Reserved for Future use. |
| 28 | `ARGNPV.CLASS.RESERVED.8` | `ArgnpvCustomerReclassification_Reserved8` | TField |  | Reserved for Future use. |
| 29 | `ARGNPV.CLASS.RESERVED.7` | `ArgnpvCustomerReclassification_Reserved7` | TField |  | Reserved for Future use. |
| 30 | `ARGNPV.CLASS.RESERVED.6` | `ArgnpvCustomerReclassification_Reserved6` | TField |  | Reserved for Future use. |
| 31 | `ARGNPV.CLASS.RESERVED.5` | `ArgnpvCustomerReclassification_Reserved5` | TField |  | Reserved for Future use. |
| 32 | `ARGNPV.CLASS.RESERVED.4` | `ArgnpvCustomerReclassification_Reserved4` | TField |  | Reserved for Future use. |
| 33 | `ARGNPV.CLASS.RESERVED.3` | `ArgnpvCustomerReclassification_Reserved3` | TField |  | Reserved for Future use. |
| 34 | `ARGNPV.CLASS.RESERVED.2` | `ArgnpvCustomerReclassification_Reserved2` | TField |  | Reserved for Future use. |
| 35 | `ARGNPV.CLASS.RESERVED.1` | `ArgnpvCustomerReclassification_Reserved1` | TField |  | Reserved for Future use. |
