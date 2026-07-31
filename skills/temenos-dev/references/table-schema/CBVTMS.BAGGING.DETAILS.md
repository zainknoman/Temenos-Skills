# CBVTMS.BAGGING.DETAILS — Table Schema

> Source: `INSERTS/I_F.CBVTMS.BAGGING.DETAILS` in `CBVTMS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `VTMS.REFERENCE.BAG.ID` | `CbvtmsBaggingDetails_ReferenceBagId` | TField |  | The reference bag ID which the bank wants to capture apart from the system generated bag ID |
| 2 | `VTMS.ENTITY.ID` | `CbvtmsBaggingDetails_EntityId` | TField |  | The customer ID of the commercial bank |
| 3 | `VTMS.CREATION.DATE` | `CbvtmsBaggingDetails_CreationDate` | TField |  | The date on which the bag is created |
| 4 | `VTMS.CURRENCY` | `CbvtmsBaggingDetails_Currency` | TField |  | The currency of denomination in the bag |
| 5 | `VTMS.TOTAL.VALUE` | `CbvtmsBaggingDetails_TotalValue` | TField |  | The total value in the bag |
| 6 | `VTMS.CARTON.DETAILS` | `CbvtmsBaggingDetails_CartonDetails` |  |  |  |
| 7 | `VTMS.NO.OF.CARTON` | `CbvtmsBaggingDetails_NoOfCarton` |  |  |  |
| 8 | `VTMS.DENOMINATION` | `CbvtmsBaggingDetails_Denomination` |  |  |  |
| 9 | `VTMS.UNITS` | `CbvtmsBaggingDetails_Units` |  |  |  |
| 10 | `VTMS.CURRENCY.STATUS` | `CbvtmsBaggingDetails_CurrencyStatus` | TField |  | The status of the currency |
| 11 | `VTMS.BAG.STATUS` | `CbvtmsBaggingDetails_BagStatus` | TField |  | The status of the bag |
| 12 | `VTMS.BAG.LOCATION` | `CbvtmsBaggingDetails_BagLocation` | TField |  | The location of the bag |
| 13 | `VTMS.LOCATION.DESCRIPTION` | `CbvtmsBaggingDetails_LocationDescription` | TField |  | The description of the location where the bag is present |
| 14 | `VTMS.LOCAL.REF` | `CbvtmsBaggingDetails_LocalRef` |  |  |  |
| 15 | `VTMS.CCY.PROCESSING.DATE` | `CbvtmsBaggingDetails_CcyProcessingDate` | TField |  | The date on which the currency processing happens |
| 16 | `VTMS.REQUEST.ID` | `CbvtmsBaggingDetails_RequestId` | TField |  | Currency Request ID |
| 17 | `VTMS.RESERVED.8` | `CbvtmsBaggingDetails_Reserved8` | TField |  | Reserved field for future use |
| 18 | `VTMS.RESERVED.7` | `CbvtmsBaggingDetails_Reserved7` | TField |  | Reserved field for future use |
| 19 | `VTMS.RESERVED.6` | `CbvtmsBaggingDetails_Reserved6` | TField |  | Reserved field for future use |
| 20 | `VTMS.RESERVED.5` | `CbvtmsBaggingDetails_Reserved5` | TField |  | Reserved field for future use |
| 21 | `VTMS.RESERVED.4` | `CbvtmsBaggingDetails_Reserved4` | TField |  | Reserved field for future use |
| 22 | `VTMS.RESERVED.3` | `CbvtmsBaggingDetails_Reserved3` | TField |  | Reserved field for future use |
| 23 | `VTMS.RESERVED.2` | `CbvtmsBaggingDetails_Reserved2` | TField |  | Reserved field for future use |
| 24 | `VTMS.RESERVED.1` | `CbvtmsBaggingDetails_Reserved1` | TField |  | Reserved field for future use |
| 25 | `VTMS.OVERRIDE` | `CbvtmsBaggingDetails_Override` |  |  |  |
| 26 | `VTMS.RECORD.STATUS` | `CbvtmsBaggingDetails_RecordStatus` | String |  |  |
| 27 | `VTMS.CURR.NO` | `CbvtmsBaggingDetails_CurrNo` | String |  |  |
| 28 | `VTMS.INPUTTER` | `CbvtmsBaggingDetails_Inputter` |  |  |  |
| 29 | `VTMS.DATE.TIME` | `CbvtmsBaggingDetails_DateTime` |  |  |  |
| 30 | `VTMS.AUTHORISER` | `CbvtmsBaggingDetails_Authoriser` | String |  |  |
| 31 | `VTMS.CO.CODE` | `CbvtmsBaggingDetails_CoCode` | String |  |  |
| 32 | `VTMS.DEPT.CODE` | `CbvtmsBaggingDetails_DeptCode` | String |  |  |
| 33 | `VTMS.AUDITOR.CODE` | `CbvtmsBaggingDetails_AuditorCode` | String |  |  |
| 34 | `VTMS.AUDIT.DATE.TIME` | `CbvtmsBaggingDetails_AuditDateTime` | String |  |  |
