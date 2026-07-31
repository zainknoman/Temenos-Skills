# CZ.CDP.PDD.SEARCH.RESULTS — Table Schema

> Source: `INSERTS/I_F.CZ.CDP.PDD.SEARCH.RESULTS` in `CZ_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CZ.CPRES.PRODUCT.ID` | `CzCdpPddSearchResults_ProductId` | TField |  | This field denotes the product to which the table belongs. Validation Rule: It is NOINPUT field and is a valid ID from EB.PRODUCT |
| 2 | `CZ.CPRES.REQUEST.ID` | `CzCdpPddSearchResults_RequestId` |  |  |  |
| 3 | `CZ.CPRES.DATE.TIME.OF.SEARCH` | `CzCdpPddSearchResults_DateTimeOfSearch` |  |  |  |
| 4 | `CZ.CPRES.FIELD.NAME` | `CzCdpPddSearchResults_FieldName` |  |  |  |
| 5 | `CZ.CPRES.EXISTING.PDD.ITEM` | `CzCdpPddSearchResults_ExistingPddItem` |  |  |  |
| 6 | `CZ.CPRES.CONFIRM.AS.PDD` | `CzCdpPddSearchResults_ConfirmAsPdd` |  |  |  |
| 7 | `CZ.CPRES.FIELD.ATTRIBUTES` | `CzCdpPddSearchResults_FieldAttributes` |  |  |  |
| 8 | `CZ.CPRES.PURPOSE` | `CzCdpPddSearchResults_Purpose` |  |  |  |
| 9 | `CZ.CPRES.ACCESSIBILITY` | `CzCdpPddSearchResults_Accessibility` |  |  |  |
| 10 | `CZ.CPRES.ERASE.OPTIONS` | `CzCdpPddSearchResults_EraseOptions` |  |  |  |
| 11 | `CZ.CPRES.RESERVED.20` | `CzCdpPddSearchResults_Reserved20` | TField |  |  |
| 12 | `CZ.CPRES.RESERVED.19` | `CzCdpPddSearchResults_Reserved19` | TField |  |  |
| 13 | `CZ.CPRES.RESERVED.18` | `CzCdpPddSearchResults_Reserved18` | TField |  |  |
| 14 | `CZ.CPRES.RESERVED.17` | `CzCdpPddSearchResults_Reserved17` | TField |  |  |
| 15 | `CZ.CPRES.RESERVED.16` | `CzCdpPddSearchResults_Reserved16` | TField |  |  |
| 16 | `CZ.CPRES.RESERVED.15` | `CzCdpPddSearchResults_Reserved15` | TField |  |  |
| 17 | `CZ.CPRES.RESERVED.14` | `CzCdpPddSearchResults_Reserved14` | TField |  |  |
| 18 | `CZ.CPRES.RESERVED.13` | `CzCdpPddSearchResults_Reserved13` | TField |  |  |
| 19 | `CZ.CPRES.RESERVED.12` | `CzCdpPddSearchResults_Reserved12` | TField |  |  |
| 20 | `CZ.CPRES.RESERVED.11` | `CzCdpPddSearchResults_Reserved11` | TField |  |  |
| 21 | `CZ.CPRES.RESERVED.10` | `CzCdpPddSearchResults_Reserved10` | TField |  |  |
| 22 | `CZ.CPRES.RESERVED.09` | `CzCdpPddSearchResults_Reserved09` | TField |  |  |
| 23 | `CZ.CPRES.RESERVED.08` | `CzCdpPddSearchResults_Reserved08` | TField |  |  |
| 24 | `CZ.CPRES.RESERVED.07` | `CzCdpPddSearchResults_Reserved07` | TField |  |  |
| 25 | `CZ.CPRES.RESERVED.06` | `CzCdpPddSearchResults_Reserved06` | TField |  |  |
| 26 | `CZ.CPRES.RESERVED.05` | `CzCdpPddSearchResults_Reserved05` | TField |  |  |
| 27 | `CZ.CPRES.RESERVED.04` | `CzCdpPddSearchResults_Reserved04` | TField |  |  |
| 28 | `CZ.CPRES.RESERVED.03` | `CzCdpPddSearchResults_Reserved03` | TField |  |  |
| 29 | `CZ.CPRES.RESERVED.02` | `CzCdpPddSearchResults_Reserved02` | TField |  |  |
| 30 | `CZ.CPRES.RESERVED.01` | `CzCdpPddSearchResults_Reserved01` | TField |  |  |
| 31 | `CZ.CPRES.LOCAL.REF` | `CzCdpPddSearchResults_LocalRef` |  |  |  |
| 32 | `CZ.CPRES.RECORD.STATUS` | `CzCdpPddSearchResults_RecordStatus` | String |  |  |
| 33 | `CZ.CPRES.CURR.NO` | `CzCdpPddSearchResults_CurrNo` | String |  |  |
| 34 | `CZ.CPRES.INPUTTER` | `CzCdpPddSearchResults_Inputter` |  |  |  |
| 35 | `CZ.CPRES.DATE.TIME` | `CzCdpPddSearchResults_DateTime` |  |  |  |
| 36 | `CZ.CPRES.AUTHORISER` | `CzCdpPddSearchResults_Authoriser` | String |  |  |
| 37 | `CZ.CPRES.CO.CODE` | `CzCdpPddSearchResults_CoCode` | String |  |  |
| 38 | `CZ.CPRES.DEPT.CODE` | `CzCdpPddSearchResults_DeptCode` | String |  |  |
| 39 | `CZ.CPRES.AUDITOR.CODE` | `CzCdpPddSearchResults_AuditorCode` | String |  |  |
| 40 | `CZ.CPRES.AUDIT.DATE.TIME` | `CzCdpPddSearchResults_AuditDateTime` | String |  |  |
