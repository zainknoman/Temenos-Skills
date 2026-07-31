# POR.PARTYDEBIT — Table Schema

> Source: `INSERTS/I_F.POR.PARTYDEBIT` in `PP_DebitPartyDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPPD.CompanyID` | `PorPartydebit_Companyid` |  |  |  |
| 2 | `PPPPD.FTNumber` | `PorPartydebit_Ftnumber` |  |  |  |
| 3 | `PPPPD.DebitPartyRole` | `PorPartydebit_Debitpartyrole` |  |  |  |
| 4 | `PPPPD.DebitPartyRoleIndicator` | `PorPartydebit_Debitpartyroleindicator` |  |  |  |
| 5 | `PPPPD.DebitPartyInformationTag` | `PorPartydebit_Debitpartyinformationtag` |  |  |  |
| 6 | `PPPPD.DebitPartyNationalId` | `PorPartydebit_Debitpartynationalid` |  |  |  |
| 7 | `PPPPD.DebitPartyIdentifierCode` | `PorPartydebit_Debitpartyidentifiercode` |  |  |  |
| 8 | `PPPPD.DebitPartyAccountLine` | `PorPartydebit_Debitpartyaccountline` |  |  |  |
| 9 | `PPPPD.DebitPartyFreeLine1` | `PorPartydebit_Debitpartyfreeline1` |  |  |  |
| 10 | `PPPPD.DebitPartyFreeLine2` | `PorPartydebit_Debitpartyfreeline2` |  |  |  |
| 11 | `PPPPD.DebitPartyFreeLine3` | `PorPartydebit_Debitpartyfreeline3` |  |  |  |
| 12 | `PPPPD.DebitPartyFreeLine4` | `PorPartydebit_Debitpartyfreeline4` |  |  |  |
| 13 | `PPPPD.DebitPartyName` | `PorPartydebit_Debitpartyname` |  |  |  |
| 14 | `PPPPD.DebitPartyCountry` | `PorPartydebit_Debitpartycountry` |  |  |  |
| 15 | `PPPPD.DebitPartyAddressLine1` | `PorPartydebit_Debitpartyaddressline1` |  |  |  |
| 16 | `PPPPD.DebitPartyAddressLine2` | `PorPartydebit_Debitpartyaddressline2` |  |  |  |
| 17 | `PPPPD.DebitPartyOrgIdOtherId` | `PorPartydebit_Debitpartyorgidotherid` |  |  |  |
| 18 | `PPPPD.DebitPartyOrgIdOtherSchCode` | `PorPartydebit_Debitpartyorgidotherschcode` |  |  |  |
| 19 | `PPPPD.DebitPartyOrgIdOtherSchProp` | `PorPartydebit_Debitpartyorgidotherschprop` |  |  |  |
| 20 | `PPPPD.DebitPartyOrgIdOtherIssuer` | `PorPartydebit_Debitpartyorgidotherissuer` |  |  |  |
| 21 | `PPPPD.DebitPartyBirthDate` | `PorPartydebit_Debitpartybirthdate` |  |  |  |
| 22 | `PPPPD.DebitPartyProvinceOfBirth` | `PorPartydebit_Debitpartyprovinceofbirth` |  |  |  |
| 23 | `PPPPD.DebitPartyCityOfBirth` | `PorPartydebit_Debitpartycityofbirth` |  |  |  |
| 24 | `PPPPD.DebitPartyCountryOfBirth` | `PorPartydebit_Debitpartycountryofbirth` |  |  |  |
| 25 | `PPPPD.DebitPartyPrvIdOtherId` | `PorPartydebit_Debitpartyprvidotherid` |  |  |  |
| 26 | `PPPPD.DebitPartyPrvIdOtherSchCode` | `PorPartydebit_Debitpartyprvidotherschcode` |  |  |  |
| 27 | `PPPPD.DebitPartyPrvIdOtherSchProp` | `PorPartydebit_Debitpartyprvidotherschprop` |  |  |  |
| 28 | `PPPPD.DebitPartyPrvIdOtherIssuer` | `PorPartydebit_Debitpartyprvidotherissuer` |  |  |  |
