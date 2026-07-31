# FS.GA.HOLDING.PERIOD.DEFINITION — Table Schema

> Source: `INSERTS/I_F.FS.GA.HOLDING.PERIOD.DEFINITION` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.HOLDING.PERIOD.DEFINITION.PARENT.REF.ID` | `FsGaHoldingPeriodDefinition_ParentRefId` |  |  |  |
| 2 | `FS.GA.HOLDING.PERIOD.DEFINITION.ORA.ROWID` | `FsGaHoldingPeriodDefinition_OraRowid` |  |  |  |
| 3 | `FS.GA.HOLDING.PERIOD.DEFINITION.CURRENCY.CODE` | `FsGaHoldingPeriodDefinition_CurrencyCode` |  |  |  |
| 4 | `FS.GA.HOLDING.PERIOD.DEFINITION.TAX.DOMICILE` | `FsGaHoldingPeriodDefinition_TaxDomicile` |  |  |  |
| 5 | `FS.GA.HOLDING.PERIOD.DEFINITION.TAX.SECURITY.TYPE` | `FsGaHoldingPeriodDefinition_TaxSecurityType` |  |  |  |
| 6 | `FS.GA.HOLDING.PERIOD.DEFINITION.TAX.REGIME` | `FsGaHoldingPeriodDefinition_TaxRegime` |  |  |  |
| 7 | `FS.GA.HOLDING.PERIOD.DEFINITION.ENTITLEMENT.DATE` | `FsGaHoldingPeriodDefinition_EntitlementDate` |  |  |  |
| 8 | `FS.GA.HOLDING.PERIOD.DEFINITION.TAX.CODE` | `FsGaHoldingPeriodDefinition_TaxCode` |  |  |  |
| 9 | `FS.GA.HOLDING.PERIOD.DEFINITION.GTI.CODE` | `FsGaHoldingPeriodDefinition_GtiCode` |  |  |  |
| 10 | `FS.GA.HOLDING.PERIOD.DEFINITION.QUOTATION.PLACE` | `FsGaHoldingPeriodDefinition_QuotationPlace` |  |  |  |
| 11 | `FS.GA.HOLDING.PERIOD.DEFINITION.ACCOUNTING.METHOD` | `FsGaHoldingPeriodDefinition_AccountingMethod` |  |  |  |
| 12 | `FS.GA.HOLDING.PERIOD.DEFINITION.TYPE.OF.DURATION` | `FsGaHoldingPeriodDefinition_TypeOfDuration` |  |  |  |
| 13 | `FS.GA.HOLDING.PERIOD.DEFINITION.DURATION` | `FsGaHoldingPeriodDefinition_Duration` |  |  |  |
| 14 | `FS.GA.HOLDING.PERIOD.DEFINITION.TAXABLE.INCOME.PERCENTAGE` | `FsGaHoldingPeriodDefinition_TaxableIncomePercentage` |  |  |  |
| 15 | `FS.GA.HOLDING.PERIOD.DEFINITION.BOND.MARKET.TYPE` | `FsGaHoldingPeriodDefinition_BondMarketType` |  |  |  |
| 16 | `FS.GA.HOLDING.PERIOD.DEFINITION.RESERVED10` | `FsGaHoldingPeriodDefinition_Reserved10` |  |  |  |
| 17 | `FS.GA.HOLDING.PERIOD.DEFINITION.RESERVED9` | `FsGaHoldingPeriodDefinition_Reserved9` |  |  |  |
| 18 | `FS.GA.HOLDING.PERIOD.DEFINITION.RESERVED8` | `FsGaHoldingPeriodDefinition_Reserved8` |  |  |  |
| 19 | `FS.GA.HOLDING.PERIOD.DEFINITION.RESERVED7` | `FsGaHoldingPeriodDefinition_Reserved7` |  |  |  |
| 20 | `FS.GA.HOLDING.PERIOD.DEFINITION.RESERVED6` | `FsGaHoldingPeriodDefinition_Reserved6` |  |  |  |
| 21 | `FS.GA.HOLDING.PERIOD.DEFINITION.RESERVED5` | `FsGaHoldingPeriodDefinition_Reserved5` |  |  |  |
| 22 | `FS.GA.HOLDING.PERIOD.DEFINITION.RESERVED4` | `FsGaHoldingPeriodDefinition_Reserved4` |  |  |  |
| 23 | `FS.GA.HOLDING.PERIOD.DEFINITION.RESERVED3` | `FsGaHoldingPeriodDefinition_Reserved3` |  |  |  |
| 24 | `FS.GA.HOLDING.PERIOD.DEFINITION.RESERVED2` | `FsGaHoldingPeriodDefinition_Reserved2` |  |  |  |
| 25 | `FS.GA.HOLDING.PERIOD.DEFINITION.RESERVED1` | `FsGaHoldingPeriodDefinition_Reserved1` |  |  |  |
| 26 | `FS.GA.HOLDING.PERIOD.DEFINITION.LOCAL.REF` | `FsGaHoldingPeriodDefinition_LocalRef` |  |  |  |
| 27 | `FS.GA.HOLDING.PERIOD.DEFINITION.OVERRIDE` | `FsGaHoldingPeriodDefinition_Override` |  |  |  |
| 28 | `FS.GA.HOLDING.PERIOD.DEFINITION.RECORD.STATUS` | `FsGaHoldingPeriodDefinition_RecordStatus` |  |  |  |
| 29 | `FS.GA.HOLDING.PERIOD.DEFINITION.CURR.NO` | `FsGaHoldingPeriodDefinition_CurrNo` |  |  |  |
| 30 | `FS.GA.HOLDING.PERIOD.DEFINITION.INPUTTER` | `FsGaHoldingPeriodDefinition_Inputter` |  |  |  |
| 31 | `FS.GA.HOLDING.PERIOD.DEFINITION.DATE.TIME` | `FsGaHoldingPeriodDefinition_DateTime` |  |  |  |
| 32 | `FS.GA.HOLDING.PERIOD.DEFINITION.AUTHORISER` | `FsGaHoldingPeriodDefinition_Authoriser` |  |  |  |
| 33 | `FS.GA.HOLDING.PERIOD.DEFINITION.CO.CODE` | `FsGaHoldingPeriodDefinition_CoCode` |  |  |  |
| 34 | `FS.GA.HOLDING.PERIOD.DEFINITION.DEPT.CODE` | `FsGaHoldingPeriodDefinition_DeptCode` |  |  |  |
| 35 | `FS.GA.HOLDING.PERIOD.DEFINITION.AUDITOR.CODE` | `FsGaHoldingPeriodDefinition_AuditorCode` |  |  |  |
| 36 | `FS.GA.HOLDING.PERIOD.DEFINITION.AUDIT.DATE.TIME` | `FsGaHoldingPeriodDefinition_AuditDateTime` |  |  |  |
