# CUSTOMER.ADDRESS.HIST — Table Schema

> Source: `INSERTS/I_F.CUSTOMER.ADDRESS.HIST` in `ST_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAH.VALID.UNTIL` | `CustomerAddressHist_ValidUntil` |  |  |  |
| 2 | `CAH.STREET` | `CustomerAddressHist_Street` |  |  |  |
| 3 | `CAH.ADDRESS` | `CustomerAddressHist_Address` |  |  |  |
| 4 | `CAH.TOWN.COUNTRY` | `CustomerAddressHist_TownCountry` |  |  |  |
| 5 | `CAH.POST.CODE` | `CustomerAddressHist_PostCode` |  |  |  |
| 6 | `CAH.COUNTRY` | `CustomerAddressHist_Country` |  |  |  |
| 7 | `CAH.ADDRESS.COUNTRY` | `CustomerAddressHist_AddressCountry` |  |  |  |
| 8 | `CAH.ADDRESS.TYPE` | `CustomerAddressHist_AddressType` |  |  |  |
| 9 | `CAH.ADDRESS.PURPOSE` | `CustomerAddressHist_AddressPurpose` |  |  |  |
| 10 | `CAH.BUILDING.NUMBER` | `CustomerAddressHist_BuildingNumber` |  |  |  |
| 11 | `CAH.BUILDING.NAME` | `CustomerAddressHist_BuildingName` |  |  |  |
| 12 | `CAH.FLAT.NUMBER` | `CustomerAddressHist_FlatNumber` |  |  |  |
| 13 | `CAH.PO.BOX.NUMBER` | `CustomerAddressHist_PoBoxNumber` |  |  |  |
| 14 | `CAH.COUNTRY.SUBDIVISION` | `CustomerAddressHist_CountrySubdivision` |  |  |  |
| 15 | `CAH.ADDRESS.ITEM1` | `CustomerAddressHist_AddressItem1` |  |  |  |
| 16 | `CAH.ADDRESS.ITEM2` | `CustomerAddressHist_AddressItem2` |  |  |  |
| 17 | `CAH.LOCAL.REF` | `CustomerAddressHist_LocalRef` |  |  |  |
| 18 | `CAH.OVERRIDE` | `CustomerAddressHist_Override` |  |  |  |
| 19 | `CAH.RECORD.STATUS` | `CustomerAddressHist_RecordStatus` | String |  |  |
| 20 | `CAH.CURR.NO` | `CustomerAddressHist_CurrNo` | String |  |  |
| 21 | `CAH.INPUTTER` | `CustomerAddressHist_Inputter` |  |  |  |
| 22 | `CAH.DATE.TIME` | `CustomerAddressHist_DateTime` |  |  |  |
| 23 | `CAH.AUTHORISER` | `CustomerAddressHist_Authoriser` | String |  |  |
| 24 | `CAH.CO.CODE` | `CustomerAddressHist_CoCode` | String |  |  |
| 25 | `CAH.DEPT.CODE` | `CustomerAddressHist_DeptCode` | String |  |  |
| 26 | `CAH.AUDITOR.CODE` | `CustomerAddressHist_AuditorCode` | String |  |  |
| 27 | `CAH.AUDIT.DATE.TIME` | `CustomerAddressHist_AuditDateTime` | String |  |  |
| 28 | `CAH.ADDRESS.VALIDATED.BY` | `CustomerAddressHist_AddressValidatedBy` |  |  |  |
| 29 | `CAH.DEPARTMENT` | `CustomerAddressHist_Department` |  |  |  |
| 30 | `CAH.SUB.DEPARTMENT` | `CustomerAddressHist_SubDepartment` |  |  |  |
| 31 | `CAH.FLOOR` | `CustomerAddressHist_Floor` |  |  |  |
| 32 | `CAH.TOWN.LOCATION.NAME` | `CustomerAddressHist_TownLocationName` |  |  |  |
| 33 | `CAH.DISTRICT.NAME` | `CustomerAddressHist_DistrictName` |  |  |  |
