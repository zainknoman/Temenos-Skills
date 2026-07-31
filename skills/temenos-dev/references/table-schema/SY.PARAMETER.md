# SY.PARAMETER — Table Schema

> Source: `INSERTS/I_F.SY.PARAMETER` in `SY_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SY.PA.WASH.CATEGORY` | `SyParameter_WashCategory` | TField |  | This is a NOINPUT field for internal use only. This field is populated at runtime based on the CATEGORY setup in ACCOUNT.CLASS "SYFUND" record. This will always be blank. |
| 2 | `SY.PA.CR.TXN` | `SyParameter_CrTxn` | TField |  | The transaction code against which the system will process internal credit wash-through accounting entries for structured products. Must be a TRANSACTION code |
| 3 | `SY.PA.DB.TXN` | `SyParameter_DbTxn` | TField |  | The transaction code against which the system will process internal debit wash-through accounting entries for structured products. Must be a TRANSACTION code |
| 4 | `SY.PA.OFS.SOURCE` | `SyParameter_OfsSource` | TField |  | The OFS.SOURCE record to be used for processing all OFS messages within the Structured Products module. Must be a valid record in OFS.SOURCE |
| 5 | `SY.PA.RESERVED.14` | `SyParameter_Reserved14` | TField |  |  |
| 6 | `SY.PA.PRODUCT.CATEGORY` | `SyParameter_ProductCategory` | TField |  | This field holds a generic category id which degfines the category of the product. This information is defaulted to the SY.PRODUCT.DEFINITION. |
| 7 | `SY.PA.RESERVED.13` | `SyParameter_Reserved13` | TField |  |  |
| 8 | `SY.PA.SUB.ASSET.TYPE` | `SyParameter_SubAssetType` | TField |  | Should be a valid SUB.ASSET.TYPE code. Sets defaulting of SUB.ASSET.TYPE into SY.PRODUCT.DEFINITION records. At product level, this is the Sub Asset Type that the deals for that product will belong to. |
| 9 | `SY.PA.SWEEP.ON.OFF` | `SyParameter_SweepOnOff` | TField |  | Acts as a 'Master switch' for sweeping from segregated account during COB. Accepts values 'On' or 'Off' |
| 10 | `SY.PA.DEF.SWEEP.ACCT` | `SyParameter_DefSweepAcct` | TField |  | Controls sweeping from segregated account during COB. Accepts values 'Yes' or 'No' Sets defaulting of SWEEP.ACCT into SY.PRODUCT.DEFINITION records. At product level, this flag defines whether or not the sweeping should take place for that product. |
| 11 | `SY.PA.DEF.SWEEP.TXN` | `SyParameter_DefSweepTxn` |  |  |  |
| 12 | `SY.PA.DEPOSIT` | `SyParameter_Deposit` | TField |  | The default value to be used for the DEPOSIT field in new SY.PRODUCT.DEFINITION records. Accepts values 'Yes' or 'No' |
| 13 | `SY.PA.RESERVED.11` | `SyParameter_Reserved11` | TField |  |  |
| 14 | `SY.PA.SY.ID.FIELD` | `SyParameter_SyIdField` | TField |  | A local reference to hold an SY.TRANSACTION ID on each TABLE Should be a valid record in LOCAL.TABLE whose field definition matches that of the SY.TRANSACTION.ID The 'Maximum Char' field should be set to '15' The 'Char Type' field should be set to 'A' Should not be the same record as that defined in SY.UNIT.FIELD |
| 15 | `SY.PA.SY.UNIT.FIELD` | `SyParameter_SyUnitField` | TField |  | A local reference to hold an SY.UNIT ID on each TABLE Should be a valid record in LOCAL.TABLE whose field definition matches that of the SY.UNIT ID The 'Maximum Char' field should be set to '52' The 'Char Type' field should be set to 'A' Should not be the same record as that defined in SY.ID.FIELD |
| 16 | `SY.PA.SY.EXCL.VAL.FIELD` | `SyParameter_SyExclValField` | TField |  | A local reference to hold a YES or NO field on each TABLE to indicate whether the application should be excluded from valuation. Should be a valid record in LOCAL.TABLE whose field definition is Maximum size : 3 Field Type : A And should have entries YES and NO in the VETTING.TABLE field |
| 17 | `SY.PA.SY.EXCLUDE.VALUATION` | `SyParameter_SyExcludeValuation` | TField |  | This field sets the default value for inclusion/exclusion of SY underlying deals in the valuation and customer position reporting. If set to "YES" this will only report the SY deal otherwise all transactions created by the SY product along with the SY deal will be displayed. |
| 18 | `SY.PA.RESERVED.8` | `SyParameter_Reserved8` | TField |  |  |
| 19 | `SY.PA.TABLE` | `SyParameter_Table` |  |  |  |
| 20 | `SY.PA.AA.PRODUCT.GROUP` | `SyParameter_AaProductGroup` | TField |  | The group that will be used when publishing products in the AA Product Catalogue. Must be a valid record in AA.PRODUCT.GROUP |
| 21 | `SY.PA.RESERVED.7` | `SyParameter_Reserved7` | TField |  |  |
| 22 | `SY.PA.RESERVED.6` | `SyParameter_Reserved6` | TField |  |  |
| 23 | `SY.PA.CURRENCY.MARKET` | `SyParameter_CurrencyMarket` | TField |  | The currency market that is to be used for SY deals. Must be a valid record in CURRENCY.MARKET |
| 24 | `SY.PA.POSITION.TYPE` | `SyParameter_PositionType` | TField |  | The position type that is to be used for SY deals. Defaults to "TR" This field is a NOINPUT field |
| 25 | `SY.PA.RESERVED.3` | `SyParameter_Reserved3` | TField |  |  |
| 26 | `SY.PA.RESERVED.2` | `SyParameter_Reserved2` | TField |  |  |
| 27 | `SY.PA.RESERVED.1` | `SyParameter_Reserved1` | TField |  |  |
| 28 | `SY.PA.LOCAL.REF` | `SyParameter_LocalRef` |  |  |  |
| 29 | `SY.PA.OVERRIDE` | `SyParameter_Override` |  |  |  |
| 30 | `SY.PA.RECORD.STATUS` | `SyParameter_RecordStatus` | String |  |  |
| 31 | `SY.PA.CURR.NO` | `SyParameter_CurrNo` | String |  |  |
| 32 | `SY.PA.INPUTTER` | `SyParameter_Inputter` |  |  |  |
| 33 | `SY.PA.DATE.TIME` | `SyParameter_DateTime` |  |  |  |
| 34 | `SY.PA.AUTHORISER` | `SyParameter_Authoriser` | String |  |  |
| 35 | `SY.PA.CO.CODE` | `SyParameter_CoCode` | String |  |  |
| 36 | `SY.PA.DEPT.CODE` | `SyParameter_DeptCode` | String |  |  |
| 37 | `SY.PA.AUDITOR.CODE` | `SyParameter_AuditorCode` | String |  |  |
| 38 | `SY.PA.AUDIT.DATE.TIME` | `SyParameter_AuditDateTime` | String |  |  |
