# FSCS.LOG.DEPOSITOR — Table Schema

> Source: `INSERTS/I_F.FSCS.LOG.DEPOSITOR` in `UKFSCS_Reporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FSCS.DEPOSITOR.SCV.NUMBER` | `FscsLogDepositor_ScvNumber` | TField |  | PRA Firm Registration Number (FRN) prefix followed by unique customer number. |
| 2 | `FSCS.DEPOSITOR.CUSTOMER` | `FscsLogDepositor_Customer` | TField |  | Customer Id Validation Rule: Valid CUSTOMER id |
| 3 | `FSCS.DEPOSITOR.DATE.TIME` | `FscsLogDepositor_DateTime` |  |  |  |
| 4 | `FSCS.DEPOSITOR.EXCLUSION` | `FscsLogDepositor_Exclusion` | TField |  | Exclusion File Validation Rule: Y or N |
| 5 | `FSCS.DEPOSITOR.FFSTP` | `FscsLogDepositor_Ffstp` | TField |  | Fit For Straight Through Payout Validation Rule: Y or N |
| 6 | `FSCS.DEPOSITOR.TITLE` | `FscsLogDepositor_Title` | TField |  | Title, only applicable for Individuals. Where the customer is not an individual, this field should be left blank. |
| 7 | `FSCS.DEPOSITOR.CUS.FIRST.NAME` | `FscsLogDepositor_CusFirstName` | TField |  | First name of the customer, only applicable for Individuals. Where the customer is not an individual, this fieldshould be left blank. Please note that firms will always be expected to hold the customer's first name, where thatcustomer is an individual. |
| 8 | `FSCS.DEPOSITOR.CUS.SECOND.NAME` | `FscsLogDepositor_CusSecondName` | TField |  | Second name of the customer, only applicable for Individuals to help distinguish between claimants with the samefirst name and surname Where the customer is not an individual, this field should be left blank. Where no suchinformation is held, deposit takers should leave blank. |
| 9 | `FSCS.DEPOSITOR.CUS.THIRD.NAME` | `FscsLogDepositor_CusThirdName` | TField |  | Third forename of the customer, only applicable for Individuals. |
| 10 | `FSCS.DEPOSITOR.SUR.NAME` | `FscsLogDepositor_SurName` | TField |  | Surname [or company name or name of account holder]. |
| 11 | `FSCS.DEPOSITOR.PREVIOUS.NAME` | `FscsLogDepositor_PreviousName` | TField |  | Any former name of the account holder, only applicable for Individuals. Where the customer is not an individual,this field should be left blank. |
| 12 | `FSCS.DEPOSITOR.NINO` | `FscsLogDepositor_Nino` | TField |  | Only applicable for Individuals. Where the customer is not an individual, this field should be left blank. |
| 13 | `FSCS.DEPOSITOR.PASSPORT.NO` | `FscsLogDepositor_PassportNo` | TField |  | Only applicable for Individuals. Where the customer is not an individual, this field should be left blank. |
| 14 | `FSCS.DEPOSITOR.OTHER.NATIONAL` | `FscsLogDepositor_OtherNational` | TField |  | Only applicable for Individuals. Where the customer is not an individual, this field should be left blank. NID � National ID DL � Driving Licence O � Other or Unknown |
| 15 | `FSCS.DEPOSITOR.OTHER.NATIONAL.NO` | `FscsLogDepositor_OtherNationalNo` | TField |  | National identity number, of the type listed in the Other national identity field. Only applicable forIndividuals. Where the customer is not an individual, this field should be left blank. |
| 16 | `FSCS.DEPOSITOR.COMPANY` | `FscsLogDepositor_Company` | TField |  | Company registration number or other business registration number [if applicable]. Only applicable for Companies.Where the customer is not a Company, this field should be left blank. |
| 17 | `FSCS.DEPOSITOR.DOB` | `FscsLogDepositor_Dob` | TField |  | Date of birth in DDMMYYYY format. Only applicable for Individuals. Where the customer is not an individual, thisfield should be left blank. |
| 18 | `FSCS.DEPOSITOR.ADDRESS.LINE1` | `FscsLogDepositor_AddressLine1` | TField |  | Lines of address should be provided in consecutive address line fields. |
| 19 | `FSCS.DEPOSITOR.ADDRESS.LINE2` | `FscsLogDepositor_AddressLine2` | TField |  | Lines of address should be provided in consecutive address line fields. |
| 20 | `FSCS.DEPOSITOR.ADDRESS.LINE3` | `FscsLogDepositor_AddressLine3` | TField |  | Lines of address should be provided in consecutive address line fields. |
| 21 | `FSCS.DEPOSITOR.ADDRESS.LINE4` | `FscsLogDepositor_AddressLine4` | TField |  | Lines of address should be provided in consecutive address line fields. |
| 22 | `FSCS.DEPOSITOR.ADDRESS.LINE5` | `FscsLogDepositor_AddressLine5` | TField |  | Lines of address should be provided in consecutive address line fields. |
| 23 | `FSCS.DEPOSITOR.ADDRESS.LINE6` | `FscsLogDepositor_AddressLine6` | TField |  | Lines of address should be provided in consecutive address line fields. |
| 24 | `FSCS.DEPOSITOR.POSTCODE` | `FscsLogDepositor_Postcode` | TField |  | Required as minimum address details for UK address only. |
| 25 | `FSCS.DEPOSITOR.COUNTRY` | `FscsLogDepositor_Country` | TField |  | Required as minimum address details for non-UK address only.Blank country field indicates UK address. |
| 26 | `FSCS.DEPOSITOR.EMAIL.ADD` | `FscsLogDepositor_EmailAdd` | TField |  | Email address |
| 27 | `FSCS.DEPOSITOR.MAIN.PHONE.NO` | `FscsLogDepositor_MainPhoneNo` | TField |  | Phone number 1 |
| 28 | `FSCS.DEPOSITOR.EVE.PHONE.NO` | `FscsLogDepositor_EvePhoneNo` | TField |  | Phone number 2 |
| 29 | `FSCS.DEPOSITOR.MOBILE.PHONE` | `FscsLogDepositor_MobilePhone` | TField |  | Phone number 3 |
| 30 | `FSCS.DEPOSITOR.AGG.BALANCE` | `FscsLogDepositor_AggBalance` | TField |  | Aggregated balance in sterling (GBP) over all (deposit) accounts and contracts of the customer. If the aggregatedbalance is negative, the field value should contain zero ('0.00'). Do not include any non-numeric symbols such as commas or currency symbols (e.g. �). All balances must be roundedup to two decimal places. |
| 31 | `FSCS.DEPOSITOR.COMP.AMOUNT` | `FscsLogDepositor_CompAmount` | TField |  | The amount to be compensated subject to the limit check that must be performed by the firm pursuant to DepositorProtection Rule 12.7(2) (this could be lower than the aggregate balance across all accounts if this exceeds thecompensation limit).For beneficiary accounts provided in the Exclusions View file, it may not be possible tocalculate this amount, as thebeneficiary/beneficiaries may be unknown and this field may be left blank.Do notinclude any non-numeric symbols such as commas or currency symbols (e.g. �). All balances must be rounded upto twodecimal places.Should the compensable amount be negative, this field should be recorded as 0.00. |
| 32 | `FSCS.DEPOSITOR.RESERVED.10` | `FscsLogDepositor_Reserved10` | TField |  |  |
| 33 | `FSCS.DEPOSITOR.RESERVED.9` | `FscsLogDepositor_Reserved9` | TField |  |  |
| 34 | `FSCS.DEPOSITOR.RESERVED.8` | `FscsLogDepositor_Reserved8` | TField |  |  |
| 35 | `FSCS.DEPOSITOR.RESERVED.7` | `FscsLogDepositor_Reserved7` | TField |  |  |
| 36 | `FSCS.DEPOSITOR.RESERVED.6` | `FscsLogDepositor_Reserved6` | TField |  |  |
| 37 | `FSCS.DEPOSITOR.RESERVED.5` | `FscsLogDepositor_Reserved5` | TField |  |  |
| 38 | `FSCS.DEPOSITOR.RESERVED.4` | `FscsLogDepositor_Reserved4` | TField |  |  |
| 39 | `FSCS.DEPOSITOR.RESERVED.3` | `FscsLogDepositor_Reserved3` | TField |  |  |
| 40 | `FSCS.DEPOSITOR.RESERVED.2` | `FscsLogDepositor_Reserved2` | TField |  |  |
| 41 | `FSCS.DEPOSITOR.RESERVED.1` | `FscsLogDepositor_Reserved1` | TField |  |  |
