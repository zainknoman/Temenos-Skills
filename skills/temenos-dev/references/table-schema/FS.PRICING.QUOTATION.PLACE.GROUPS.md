# FS.PRICING.QUOTATION.PLACE.GROUPS — Table Schema

> Source: `INSERTS/I_F.FS.PRICING.QUOTATION.PLACE.GROUPS` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.PRICING.QUOTATION.PLACE.GROUPS.DESCRIPTION` | `FsPricingQuotationPlaceGroups_Description` |  |  |  |
| 2 | `FS.PRICING.QUOTATION.PLACE.GROUPS.FILTER.KEY` | `FsPricingQuotationPlaceGroups_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.PRICING.QUOTATION.PLACE.GROUPS.RECORD.ID` | `FsPricingQuotationPlaceGroups_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.PRICING.QUOTATION.PLACE.GROUPS.RESERVED10` | `FsPricingQuotationPlaceGroups_Reserved10` | TField |  |  |
| 5 | `FS.PRICING.QUOTATION.PLACE.GROUPS.RESERVED9` | `FsPricingQuotationPlaceGroups_Reserved9` | TField |  |  |
| 6 | `FS.PRICING.QUOTATION.PLACE.GROUPS.RESERVED8` | `FsPricingQuotationPlaceGroups_Reserved8` | TField |  |  |
| 7 | `FS.PRICING.QUOTATION.PLACE.GROUPS.RESERVED7` | `FsPricingQuotationPlaceGroups_Reserved7` | TField |  |  |
| 8 | `FS.PRICING.QUOTATION.PLACE.GROUPS.RESERVED6` | `FsPricingQuotationPlaceGroups_Reserved6` | TField |  |  |
| 9 | `FS.PRICING.QUOTATION.PLACE.GROUPS.RESERVED5` | `FsPricingQuotationPlaceGroups_Reserved5` | TField |  |  |
| 10 | `FS.PRICING.QUOTATION.PLACE.GROUPS.RESERVED4` | `FsPricingQuotationPlaceGroups_Reserved4` | TField |  |  |
| 11 | `FS.PRICING.QUOTATION.PLACE.GROUPS.RESERVED3` | `FsPricingQuotationPlaceGroups_Reserved3` | TField |  |  |
| 12 | `FS.PRICING.QUOTATION.PLACE.GROUPS.RESERVED2` | `FsPricingQuotationPlaceGroups_Reserved2` | TField |  |  |
| 13 | `FS.PRICING.QUOTATION.PLACE.GROUPS.RESERVED1` | `FsPricingQuotationPlaceGroups_Reserved1` | TField |  |  |
| 14 | `FS.PRICING.QUOTATION.PLACE.GROUPS.LOCAL.REF` | `FsPricingQuotationPlaceGroups_LocalRef` |  |  |  |
| 15 | `FS.PRICING.QUOTATION.PLACE.GROUPS.OVERRIDE` | `FsPricingQuotationPlaceGroups_Override` |  |  |  |
| 16 | `FS.PRICING.QUOTATION.PLACE.GROUPS.RECORD.STATUS` | `FsPricingQuotationPlaceGroups_RecordStatus` | String |  |  |
| 17 | `FS.PRICING.QUOTATION.PLACE.GROUPS.CURR.NO` | `FsPricingQuotationPlaceGroups_CurrNo` | String |  |  |
| 18 | `FS.PRICING.QUOTATION.PLACE.GROUPS.INPUTTER` | `FsPricingQuotationPlaceGroups_Inputter` |  |  |  |
| 19 | `FS.PRICING.QUOTATION.PLACE.GROUPS.DATE.TIME` | `FsPricingQuotationPlaceGroups_DateTime` |  |  |  |
| 20 | `FS.PRICING.QUOTATION.PLACE.GROUPS.AUTHORISER` | `FsPricingQuotationPlaceGroups_Authoriser` | String |  |  |
| 21 | `FS.PRICING.QUOTATION.PLACE.GROUPS.CO.CODE` | `FsPricingQuotationPlaceGroups_CoCode` | String |  |  |
| 22 | `FS.PRICING.QUOTATION.PLACE.GROUPS.DEPT.CODE` | `FsPricingQuotationPlaceGroups_DeptCode` | String |  |  |
| 23 | `FS.PRICING.QUOTATION.PLACE.GROUPS.AUDITOR.CODE` | `FsPricingQuotationPlaceGroups_AuditorCode` | String |  |  |
| 24 | `FS.PRICING.QUOTATION.PLACE.GROUPS.AUDIT.DATE.TIME` | `FsPricingQuotationPlaceGroups_AuditDateTime` | String |  |  |
