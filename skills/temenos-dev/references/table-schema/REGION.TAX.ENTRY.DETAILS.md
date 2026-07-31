# REGION.TAX.ENTRY.DETAILS — Table Schema

> Source: `INSERTS/I_F.REGION.TAX.ENTRY.DETAILS` in `CALEND_Taxes.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `REG.TAX.ENT.DR.INTERNAL.AC` | `RegionTaxEntryDetails_DrInternalAc` | TField |  | Internal account to which the tax amount was credited. |
| 2 | `REG.TAX.ENT.CURRENCY` | `RegionTaxEntryDetails_Currency` | TField |  | Currency of the internal account tax amount is credited. |
| 3 | `REG.TAX.ENT.TAX.AMOUNT` | `RegionTaxEntryDetails_TaxAmount` | TField |  | Tax amount collected along with the charge. the rate to be used for computation of taxation for the associated Prvince and Charge Property. |
| 4 | `REG.TAX.ENT.PROVINCE.ACCOUNT` | `RegionTaxEntryDetails_ProvinceAccount` | TField |  | Category Account for respective TAX code defined for the Province. |
| 5 | `REG.TAX.ENT.ARRANGEMENT.ID` | `RegionTaxEntryDetails_ArrangementId` | TField |  | @ID of the arrangement for which tax has been applied. |
| 6 | `REG.TAX.ENT.CHARGE.TYPE` | `RegionTaxEntryDetails_ChargeType` | TField |  | Charge property for which tax was computed. |
| 7 | `REG.TAX.ENT.CHARGE.AMOUNT` | `RegionTaxEntryDetails_ChargeAmount` | TField |  | Charge Amount on which tax is computed. |
| 8 | `REG.TAX.ENT.STATUS` | `RegionTaxEntryDetails_Status` | TField |  | Status of the entry details record. PLACED - Initial update during Activity generation, updated during charge Make due activity. POSTED - Once tax amount has been moved to respective province account, updated in COB REVERSED - Underlying Activity has been reversed, updated online REV.POSTED - Once tax amount has been moved back to respective internal account, updated in COB |
| 9 | `REG.TAX.ENT.PROVINCE.NAME` | `RegionTaxEntryDetails_ProvinceName` | TField |  | Province to which tax is collected. |
| 10 | `REG.TAX.ENT.ENTRY.DATE` | `RegionTaxEntryDetails_EntryDate` | TField |  | Date in which tax amount has been moved to the province account. |
| 11 | `REG.TAX.ENT.TRANSACTION.REF` | `RegionTaxEntryDetails_TransactionRef` | TField |  | FT reference through which the tax amount has been moved to the Province Account. |
| 12 | `REG.TAX.ENT.REVERSAL.DATE` | `RegionTaxEntryDetails_ReversalDate` | TField |  | Date in which tax amount has been moved back from the province account to the internal account. |
| 13 | `REG.TAX.ENT.REVERSAL.REF` | `RegionTaxEntryDetails_ReversalRef` | TField |  | FT reference through which the tax amount has been moved back from the province account to the internal account. |
| 14 | `REG.TAX.ENT.RESERVED.10` | `RegionTaxEntryDetails_Reserved10` | TField |  |  |
| 15 | `REG.TAX.ENT.RESERVED.9` | `RegionTaxEntryDetails_Reserved9` | TField |  |  |
| 16 | `REG.TAX.ENT.RESERVED.8` | `RegionTaxEntryDetails_Reserved8` | TField |  |  |
| 17 | `REG.TAX.ENT.RESERVED.7` | `RegionTaxEntryDetails_Reserved7` | TField |  |  |
| 18 | `REG.TAX.ENT.RESERVED.6` | `RegionTaxEntryDetails_Reserved6` | TField |  |  |
| 19 | `REG.TAX.ENT.RESERVED.5` | `RegionTaxEntryDetails_Reserved5` | TField |  |  |
| 20 | `REG.TAX.ENT.RESERVED.4` | `RegionTaxEntryDetails_Reserved4` | TField |  |  |
| 21 | `REG.TAX.ENT.RESERVED.3` | `RegionTaxEntryDetails_Reserved3` | TField |  |  |
| 22 | `REG.TAX.ENT.RESERVED.2` | `RegionTaxEntryDetails_Reserved2` | TField |  |  |
| 23 | `REG.TAX.ENT.RESERVED.1` | `RegionTaxEntryDetails_Reserved1` | TField |  |  |
