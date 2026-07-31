# POR.PARTYCREDIT — Table Schema

> Source: `INSERTS/I_F.POR.PARTYCREDIT` in `PP_CreditPartyDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPPPC.CompanyID` | `PorPartycredit_Companyid` |  |  |  |
| 2 | `PPPPC.FTNumber` | `PorPartycredit_Ftnumber` |  |  |  |
| 3 | `PPPPC.CreditPartyRole` | `PorPartycredit_Creditpartyrole` |  |  |  |
| 4 | `PPPPC.CreditPartyRoleIndicator` | `PorPartycredit_Creditpartyroleindicator` |  |  |  |
| 5 | `PPPPC.CreditPartyInformationTag` | `PorPartycredit_Creditpartyinformationtag` |  |  |  |
| 6 | `PPPPC.CreditPartyNationalId` | `PorPartycredit_Creditpartynationalid` |  |  |  |
| 7 | `PPPPC.CreditPartyIdentifierCode` | `PorPartycredit_Creditpartyidentifiercode` |  |  |  |
| 8 | `PPPPC.CreditPartyAccountLine` | `PorPartycredit_Creditpartyaccountline` |  |  |  |
| 9 | `PPPPC.CreditPartyFreeLine1` | `PorPartycredit_Creditpartyfreeline1` |  |  |  |
| 10 | `PPPPC.CreditPartyFreeLine2` | `PorPartycredit_Creditpartyfreeline2` |  |  |  |
| 11 | `PPPPC.CreditPartyFreeLine3` | `PorPartycredit_Creditpartyfreeline3` |  |  |  |
| 12 | `PPPPC.CreditPartyFreeLine4` | `PorPartycredit_Creditpartyfreeline4` |  |  |  |
| 13 | `PPPPC.DirectPaymentFlag` | `PorPartycredit_Directpaymentflag` |  |  |  |
| 14 | `PPPPC.CreditPartyName` | `PorPartycredit_Creditpartyname` |  |  |  |
| 15 | `PPPPC.CreditPartyCountry` | `PorPartycredit_Creditpartycountry` |  |  |  |
| 16 | `PPPPC.CreditPartyAddressLine1` | `PorPartycredit_Creditpartyaddressline1` |  |  |  |
| 17 | `PPPPC.CreditPartyAddressLine2` | `PorPartycredit_Creditpartyaddressline2` |  |  |  |
| 18 | `PPPPC.CreditPartyOrgIdOtherId` | `PorPartycredit_Creditpartyorgidotherid` |  |  |  |
| 19 | `PPPPC.CdtPartyOrgIdOtherSchCode` | `PorPartycredit_Cdtpartyorgidotherschcode` |  |  |  |
| 20 | `PPPPC.CdtPartyOrgIdOtherSchProp` | `PorPartycredit_Cdtpartyorgidotherschprop` |  |  |  |
| 21 | `PPPPC.CreditPartyOrgIdOtherIssuer` | `PorPartycredit_Creditpartyorgidotherissuer` |  |  |  |
| 22 | `PPPPC.CreditPartyBirthDate` | `PorPartycredit_Creditpartybirthdate` |  |  |  |
| 23 | `PPPPC.CreditPartyProvinceOfBirth` | `PorPartycredit_Creditpartyprovinceofbirth` |  |  |  |
| 24 | `PPPPC.CreditPartyCityOfBirth` | `PorPartycredit_Creditpartycityofbirth` |  |  |  |
| 25 | `PPPPC.CreditPartyCountryOfBirth` | `PorPartycredit_Creditpartycountryofbirth` |  |  |  |
| 26 | `PPPPC.CreditPartyPrvIdOtherId` | `PorPartycredit_Creditpartyprvidotherid` |  |  |  |
| 27 | `PPPPC.CdtPartyPrvIdOtherSchCode` | `PorPartycredit_Cdtpartyprvidotherschcode` |  |  |  |
| 28 | `PPPPC.CdtPartyPrvIdOtherSchProp` | `PorPartycredit_Cdtpartyprvidotherschprop` |  |  |  |
| 29 | `PPPPC.CreditPartyPrvIdOtherIssuer` | `PorPartycredit_Creditpartyprvidotherissuer` |  |  |  |
