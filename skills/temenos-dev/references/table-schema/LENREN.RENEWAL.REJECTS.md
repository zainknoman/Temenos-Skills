# LENREN.RENEWAL.REJECTS — Table Schema

> Source: `INSERTS/I_F.LENREN.RENEWAL.REJECTS` in `LENREN_Renewal.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `REN.REJ.CUSTOMER` | `LenrenRenewalRejects_Customer` | TField |  | This field is to capture the customer id for the renewal reject.Valid CUSTOMER record is stored. |
| 2 | `REN.REJ.ACCOUNT` | `LenrenRenewalRejects_Account` | TField |  | Field stores the corresponding account number of the customer.Valid ACCOUNT number is stored here. |
| 3 | `REN.REJ.RENEWAL.DATE` | `LenrenRenewalRejects_RenewalDate` | TField |  | Field is to capture the renewal date.Valid date to be stored. |
| 4 | `REN.REJ.REASON` | `LenrenRenewalRejects_Reason` |  |  |  |
| 5 | `REN.REJ.RESERVED.10` | `LenrenRenewalRejects_Reserved10` | TField |  |  |
| 6 | `REN.REJ.RESERVED.9` | `LenrenRenewalRejects_Reserved9` | TField |  |  |
| 7 | `REN.REJ.RESERVED.8` | `LenrenRenewalRejects_Reserved8` | TField |  |  |
| 8 | `REN.REJ.RESERVED.7` | `LenrenRenewalRejects_Reserved7` | TField |  |  |
| 9 | `REN.REJ.RESERVED.6` | `LenrenRenewalRejects_Reserved6` | TField |  |  |
| 10 | `REN.REJ.RESERVED.5` | `LenrenRenewalRejects_Reserved5` | TField |  |  |
| 11 | `REN.REJ.RESERVED.4` | `LenrenRenewalRejects_Reserved4` | TField |  |  |
| 12 | `REN.REJ.RESERVED.3` | `LenrenRenewalRejects_Reserved3` | TField |  |  |
| 13 | `REN.REJ.RESERVED.2` | `LenrenRenewalRejects_Reserved2` | TField |  |  |
| 14 | `REN.REJ.RESERVED.1` | `LenrenRenewalRejects_Reserved1` | TField |  |  |
