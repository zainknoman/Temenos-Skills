# ESFUND.ORDER.REPORT — Table Schema

> Source: `INSERTS/I_F.ESFUND.ORDER.REPORT` in `ESFUND_DailyBrokerOrderReport.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ES.EOR.TYPE.OF.REGISTRATION` | `EsfundOrderReport_TypeOfRegistration` | TField |  |  |
| 2 | `ES.EOR.IDENTIFICATION.CODE` | `EsfundOrderReport_IdentificationCode` | TField |  |  |
| 3 | `ES.EOR.ORDER.NO` | `EsfundOrderReport_OrderNo` | TField |  |  |
| 4 | `ES.EOR.ALT.ORDER.NO` | `EsfundOrderReport_AltOrderNo` | TField |  |  |
| 5 | `ES.EOR.OWNERSHIP.ORDER.SEQ` | `EsfundOrderReport_OwnershipOrderSeq` | TField |  |  |
| 6 | `ES.EOR.DOCUMENT` | `EsfundOrderReport_Document` | TField |  |  |
| 7 | `ES.EOR.DOCUMENT.TYPE` | `EsfundOrderReport_DocumentType` | TField |  |  |
| 8 | `ES.EOR.PERSON.TYPE` | `EsfundOrderReport_PersonType` | TField |  |  |
| 9 | `ES.EOR.FULL.NAME` | `EsfundOrderReport_FullName` |  |  |  |
| 10 | `ES.EOR.ADDRESS` | `EsfundOrderReport_Address` |  |  |  |
| 11 | `ES.EOR.FISCAL.ADDRESS` | `EsfundOrderReport_FiscalAddress` |  |  |  |
| 12 | `ES.EOR.POSTAL.ADDRESS` | `EsfundOrderReport_PostalAddress` |  |  |  |
| 13 | `ES.EOR.NATIONALITY` | `EsfundOrderReport_Nationality` |  |  |  |
| 14 | `ES.EOR.HOLDER.ROLE` | `EsfundOrderReport_HolderRole` | TField |  |  |
| 15 | `ES.EOR.OWNERSHIP.PERCENT` | `EsfundOrderReport_OwnershipPercent` | TField |  |  |
| 16 | `ES.EOR.STOCK.EXCHANGE` | `EsfundOrderReport_StockExchange` | TField |  |  |
| 17 | `ES.EOR.CCV` | `EsfundOrderReport_Ccv` | TField |  |  |
| 18 | `ES.EOR.DATE.OF.BIRTH` | `EsfundOrderReport_DateOfBirth` | TField |  |  |
| 19 | `ES.EOR.NATIONALITY.TYPE` | `EsfundOrderReport_NationalityType` | TField |  |  |
| 20 | `ES.EOR.LOCAL.REF` | `EsfundOrderReport_LocalRef` |  |  |  |
| 21 | `ES.EOR.RESERVED.1` | `EsfundOrderReport_Reserved1` |  |  |  |
| 22 | `ES.EOR.RESERVED.2` | `EsfundOrderReport_Reserved2` | TField |  |  |
| 23 | `ES.EOR.RESERVED.3` | `EsfundOrderReport_Reserved3` | TField |  |  |
| 24 | `ES.EOR.RESERVED.4` | `EsfundOrderReport_Reserved4` | TField |  |  |
| 25 | `ES.EOR.RESERVED.5` | `EsfundOrderReport_Reserved5` | TField |  |  |
| 26 | `ES.EOR.RESERVED.6` | `EsfundOrderReport_Reserved6` | TField |  |  |
| 27 | `ES.EOR.RESERVED.7` | `EsfundOrderReport_Reserved7` | TField |  |  |
| 28 | `ES.EOR.RESERVED.8` | `EsfundOrderReport_Reserved8` | TField |  |  |
| 29 | `ES.EOR.RESERVED.9` | `EsfundOrderReport_Reserved9` | TField |  |  |
| 30 | `ES.EOR.RESERVED.10` | `EsfundOrderReport_Reserved10` | TField |  |  |
| 31 | `ES.EOR.OVERRIDE` | `EsfundOrderReport_Override` |  |  |  |
