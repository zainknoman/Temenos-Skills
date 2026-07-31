# ILIPOA.IPO.METHOD.TYPE — Table Schema

> Source: `INSERTS/I_F.ILIPOA.IPO.METHOD.TYPE` in `ILIPOA_Allocation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ILIPOA.CLOSING.PRICE` | `IlipoaIpoMethodType_ClosingPrice` | TField |  | Yes / No field to indicate if closing price is applicable for the IPO. |
| 2 | `ILIPOA.AVERAGE.PRICE` | `IlipoaIpoMethodType_AveragePrice` | TField |  | Yes / No field to indicate if average price is applicable for the IPO. |
| 3 | `ILIPOA.CLOSING.PRICE.ALLOC.RATE` | `IlipoaIpoMethodType_ClosingPriceAllocationRate` |  |  |  |
| 4 | `ILIPOA.AVG.PRICE.ACCEPTANCE.RATE` | `IlipoaIpoMethodType_AvgPriceAcceptanceRate` | TField |  | Yes / No field to indicate if average price allocation is applicable for the IPO. |
| 5 | `ILIPOA.ALLOTMENT.RATE` | `IlipoaIpoMethodType_AllotmentRate` | TField |  | Yes / No field to indicate if allotment rate is applicable for the IPO. |
| 6 | `ILIPOA.TOTAL.ALLOCATION.RATE` | `IlipoaIpoMethodType_TotalAllocationRate` | TField |  | Yes / No field to indicate if total allotment rate is applicable for the IPO. |
| 7 | `ILIPOA.SORT.TYPE` | `IlipoaIpoMethodType_SortType` | TField |  | Low to High / High to Low/ None are the possible fields. This is to indicate the sorting type for current allocation type. |
| 8 | `ILIPOA.ALLOCATION.ROUTINE` | `IlipoaIpoMethodType_AllocationRoutine` | TField |  | Specify: An EB.API record id with a source type of METHOD which implements an interface defined in the EB.API record ILIPOA.IPO.METHOD.TYPE.ALLOC.HOOK. This field supports the InitialPublicOffering.getSecurityAllocation() method. The InitialPublicOffering class is in the com.temenos.t24.api.hook.countrymodelbank.israel package which is in ILIPOA_InitialPublicOfferingHook.jar shipped with T24. |
| 9 | `ILIPOA.RESERVED.10` | `IlipoaIpoMethodType_Reserved10` | TField |  | Reserved for future use |
| 10 | `ILIPOA.RESERVED.9` | `IlipoaIpoMethodType_Reserved9` | TField |  | Reserved for future use |
| 11 | `ILIPOA.RESERVED.8` | `IlipoaIpoMethodType_Reserved8` | TField |  | Reserved for future use |
| 12 | `ILIPOA.RESERVED.7` | `IlipoaIpoMethodType_Reserved7` | TField |  | Reserved for future use |
| 13 | `ILIPOA.RESERVED.6` | `IlipoaIpoMethodType_Reserved6` | TField |  | Reserved for future use |
| 14 | `ILIPOA.RESERVED.5` | `IlipoaIpoMethodType_Reserved5` | TField |  | Reserved for future use |
| 15 | `ILIPOA.RESERVED.4` | `IlipoaIpoMethodType_Reserved4` | TField |  | Reserved for future use |
| 16 | `ILIPOA.RESERVED.3` | `IlipoaIpoMethodType_Reserved3` | TField |  | Reserved for future use |
| 17 | `ILIPOA.RESERVED.2` | `IlipoaIpoMethodType_Reserved2` | TField |  | Reserved for future use |
| 18 | `ILIPOA.RESERVED.1` | `IlipoaIpoMethodType_Reserved1` | TField |  | Reserved for future use |
| 19 | `ILIPOA.LOCAL.REF` | `IlipoaIpoMethodType_LocalRef` |  |  |  |
| 20 | `ILIPOA.OVERRIDE` | `IlipoaIpoMethodType_Override` |  |  |  |
| 21 | `ILIPOA.RECORD.STATUS` | `IlipoaIpoMethodType_RecordStatus` | String |  |  |
| 22 | `ILIPOA.CURR.NO` | `IlipoaIpoMethodType_CurrNo` | String |  |  |
| 23 | `ILIPOA.INPUTTER` | `IlipoaIpoMethodType_Inputter` |  |  |  |
| 24 | `ILIPOA.DATE.TIME` | `IlipoaIpoMethodType_DateTime` |  |  |  |
| 25 | `ILIPOA.AUTHORISER` | `IlipoaIpoMethodType_Authoriser` | String |  |  |
| 26 | `ILIPOA.CO.CODE` | `IlipoaIpoMethodType_CoCode` | String |  |  |
| 27 | `ILIPOA.DEPT.CODE` | `IlipoaIpoMethodType_DeptCode` | String |  |  |
| 28 | `ILIPOA.AUDITOR.CODE` | `IlipoaIpoMethodType_AuditorCode` | String |  |  |
| 29 | `ILIPOA.AUDIT.DATE.TIME` | `IlipoaIpoMethodType_AuditDateTime` | String |  |  |
