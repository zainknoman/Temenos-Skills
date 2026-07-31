# NZOBRS.FUNDS — Table Schema

> Source: `INSERTS/I_F.NZOBRS.FUNDS` in `NZOBRS_OpenBankResolution.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NZOBRS.FUNDS.OBR.RECORD.TYPE` | `NzobrsFunds_ObrRecordType` | TField |  | System will update this field as "Freeze" the first time a record is created, then system will update this field as "Unfreeze" for every subsequent record. Unfreeze records can be created until the percentage of funds already released becomes 0 for all product groups and product exceptions, until that time another freeze instruction cannot be created. |
| 2 | `NZOBRS.FUNDS.PRODUCT.GROUP` | `NzobrsFunds_ProductGroup` |  |  |  |
| 3 | `NZOBRS.FUNDS.EXCLUDE.PG` | `NzobrsFunds_ExcludePg` |  |  |  |
| 4 | `NZOBRS.FUNDS.PG.DE.MINIMIS.AMT` | `NzobrsFunds_PgDeMinimisAmt` |  |  |  |
| 5 | `NZOBRS.FUNDS.CUMULATIVE.PG.FREEZE` | `NzobrsFunds_CumulativePgFreeze` |  |  |  |
| 6 | `NZOBRS.FUNDS.PG.PREV.FREEZE` | `NzobrsFunds_PgPrevFreeze` |  |  |  |
| 7 | `NZOBRS.FUNDS.PG.FREEZE.ADJUST` | `NzobrsFunds_PgFreezeAdjust` |  |  |  |
| 8 | `NZOBRS.FUNDS.PG.RELEASED.PERCENT` | `NzobrsFunds_PgReleasedPercent` |  |  |  |
| 9 | `NZOBRS.FUNDS.PG.UNFREEZE.PERCENT` | `NzobrsFunds_PgUnfreezePercent` |  |  |  |
| 10 | `NZOBRS.FUNDS.PG.UNFREEZE.INT.RATE` | `NzobrsFunds_PgUnfreezeIntRate` |  |  |  |
| 11 | `NZOBRS.FUNDS.EXCLUDE.PRODUCT` | `NzobrsFunds_ExcludeProduct` |  |  |  |
| 12 | `NZOBRS.FUNDS.PRODUCT.EXCEPTION` | `NzobrsFunds_ProductException` |  |  |  |
| 13 | `NZOBRS.FUNDS.PR.DE.MINIMIS.AMT` | `NzobrsFunds_PrDeMinimisAmt` |  |  |  |
| 14 | `NZOBRS.FUNDS.CUMULATIVE.PR.FREEZE` | `NzobrsFunds_CumulativePrFreeze` |  |  |  |
| 15 | `NZOBRS.FUNDS.PR.PREV.FREEZE` | `NzobrsFunds_PrPrevFreeze` |  |  |  |
| 16 | `NZOBRS.FUNDS.PR.FREEZE.ADJUST` | `NzobrsFunds_PrFreezeAdjust` |  |  |  |
| 17 | `NZOBRS.FUNDS.PR.RELEASED.PERCENT` | `NzobrsFunds_PrReleasedPercent` |  |  |  |
| 18 | `NZOBRS.FUNDS.PR.UNFREEZE.PERCENT` | `NzobrsFunds_PrUnfreezePercent` |  |  |  |
| 19 | `NZOBRS.FUNDS.PR.UNFREEZE.INT.RATE` | `NzobrsFunds_PrUnfreezeIntRate` |  |  |  |
| 20 | `NZOBRS.FUNDS.OBR.COMPLETED` | `NzobrsFunds_ObrCompleted` | TField |  | This field will indicate whether the OBR is still ongoing or completed in the last unfreeze record. This field will be displayed in the Unfreeze screen. 'No'(Default Value) indicates OBR is still ongoing.'Yes' indicates OBR has completed. System updates this flag as 'Yes' when the frozen funds have been released fully (100%) from all the deposits. No new unfreeze requests can be placed after this flag is updated as 'Yes', unless a fresh OBR freeze is initiated. |
| 21 | `NZOBRS.FUNDS.RESERVED.10` | `NzobrsFunds_Reserved10` |  |  |  |
| 22 | `NZOBRS.FUNDS.RESERVED.9` | `NzobrsFunds_Reserved9` | TField |  |  |
| 23 | `NZOBRS.FUNDS.RESERVED.8` | `NzobrsFunds_Reserved8` | TField |  |  |
| 24 | `NZOBRS.FUNDS.RESERVED.7` | `NzobrsFunds_Reserved7` | TField |  |  |
| 25 | `NZOBRS.FUNDS.RESERVED.6` | `NzobrsFunds_Reserved6` | TField |  |  |
| 26 | `NZOBRS.FUNDS.RESERVED.5` | `NzobrsFunds_Reserved5` | TField |  |  |
| 27 | `NZOBRS.FUNDS.RESERVED.4` | `NzobrsFunds_Reserved4` | TField |  |  |
| 28 | `NZOBRS.FUNDS.RESERVED.3` | `NzobrsFunds_Reserved3` | TField |  |  |
| 29 | `NZOBRS.FUNDS.RESERVED.2` | `NzobrsFunds_Reserved2` | TField |  |  |
| 30 | `NZOBRS.FUNDS.RESERVED.1` | `NzobrsFunds_Reserved1` | TField |  |  |
| 31 | `NZOBRS.FUNDS.LOCAL.REF` | `NzobrsFunds_LocalRef` |  |  |  |
| 32 | `NZOBRS.FUNDS.OVERRIDE` | `NzobrsFunds_Override` |  |  |  |
| 33 | `NZOBRS.FUNDS.RECORD.STATUS` | `NzobrsFunds_RecordStatus` | String |  | Indicates the record status |
| 34 | `NZOBRS.FUNDS.CURR.NO` | `NzobrsFunds_CurrNo` | String |  | Indicates the number of time record is modified and saved |
| 35 | `NZOBRS.FUNDS.INPUTTER` | `NzobrsFunds_Inputter` |  |  |  |
| 36 | `NZOBRS.FUNDS.DATE.TIME` | `NzobrsFunds_DateTime` |  |  |  |
| 37 | `NZOBRS.FUNDS.AUTHORISER` | `NzobrsFunds_Authoriser` | String |  |  |
| 38 | `NZOBRS.FUNDS.CO.CODE` | `NzobrsFunds_CoCode` | String |  |  |
| 39 | `NZOBRS.FUNDS.DEPT.CODE` | `NzobrsFunds_DeptCode` | String |  |  |
| 40 | `NZOBRS.FUNDS.AUDITOR.CODE` | `NzobrsFunds_AuditorCode` | String |  |  |
| 41 | `NZOBRS.FUNDS.AUDIT.DATE.TIME` | `NzobrsFunds_AuditDateTime` | String |  |  |
