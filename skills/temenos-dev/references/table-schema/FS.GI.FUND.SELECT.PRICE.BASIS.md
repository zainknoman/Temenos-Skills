# FS.GI.FUND.SELECT.PRICE.BASIS — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.SELECT.PRICE.BASIS` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.SELECT.PRICE.BASIS.PARENT.REF.ID` | `FsGiFundSelectPriceBasis_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.SELECT.PRICE.BASIS.ORA.ROWID` | `FsGiFundSelectPriceBasis_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.SELECT.PRICE.BASIS.FUND.ID` | `FsGiFundSelectPriceBasis_FundId` | TField |  | Fund Internal Id. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.SELECT.PRICE.BASIS.OPERATION.CODE` | `FsGiFundSelectPriceBasis_OperationCode` | TField |  | Operation code for which the selected price basis is applicable. Multifonds DB Column is COPERATION. |
| 5 | `FS.GI.FUND.SELECT.PRICE.BASIS.SELECTED.PRICE` | `FsGiFundSelectPriceBasis_SelectedPrice` | TField |  | Selected price method applicable for the transaction. The available options are 0001-Mid Price, 0002- Offier and 0003-Bid price. Multifonds DB Column is SELECT_PRICE. |
| 6 | `FS.GI.FUND.SELECT.PRICE.BASIS.RESERVED10` | `FsGiFundSelectPriceBasis_Reserved10` | TField |  |  |
| 7 | `FS.GI.FUND.SELECT.PRICE.BASIS.RESERVED9` | `FsGiFundSelectPriceBasis_Reserved9` | TField |  |  |
| 8 | `FS.GI.FUND.SELECT.PRICE.BASIS.RESERVED8` | `FsGiFundSelectPriceBasis_Reserved8` | TField |  |  |
| 9 | `FS.GI.FUND.SELECT.PRICE.BASIS.RESERVED7` | `FsGiFundSelectPriceBasis_Reserved7` | TField |  |  |
| 10 | `FS.GI.FUND.SELECT.PRICE.BASIS.RESERVED6` | `FsGiFundSelectPriceBasis_Reserved6` | TField |  |  |
| 11 | `FS.GI.FUND.SELECT.PRICE.BASIS.RESERVED5` | `FsGiFundSelectPriceBasis_Reserved5` | TField |  |  |
| 12 | `FS.GI.FUND.SELECT.PRICE.BASIS.RESERVED4` | `FsGiFundSelectPriceBasis_Reserved4` | TField |  |  |
| 13 | `FS.GI.FUND.SELECT.PRICE.BASIS.RESERVED3` | `FsGiFundSelectPriceBasis_Reserved3` | TField |  |  |
| 14 | `FS.GI.FUND.SELECT.PRICE.BASIS.RESERVED2` | `FsGiFundSelectPriceBasis_Reserved2` | TField |  |  |
| 15 | `FS.GI.FUND.SELECT.PRICE.BASIS.RESERVED1` | `FsGiFundSelectPriceBasis_Reserved1` | TField |  |  |
| 16 | `FS.GI.FUND.SELECT.PRICE.BASIS.LOCAL.REF` | `FsGiFundSelectPriceBasis_LocalRef` |  |  |  |
| 17 | `FS.GI.FUND.SELECT.PRICE.BASIS.OVERRIDE` | `FsGiFundSelectPriceBasis_Override` |  |  |  |
| 18 | `FS.GI.FUND.SELECT.PRICE.BASIS.RECORD.STATUS` | `FsGiFundSelectPriceBasis_RecordStatus` | String |  |  |
| 19 | `FS.GI.FUND.SELECT.PRICE.BASIS.CURR.NO` | `FsGiFundSelectPriceBasis_CurrNo` | String |  |  |
| 20 | `FS.GI.FUND.SELECT.PRICE.BASIS.INPUTTER` | `FsGiFundSelectPriceBasis_Inputter` |  |  |  |
| 21 | `FS.GI.FUND.SELECT.PRICE.BASIS.DATE.TIME` | `FsGiFundSelectPriceBasis_DateTime` |  |  |  |
| 22 | `FS.GI.FUND.SELECT.PRICE.BASIS.AUTHORISER` | `FsGiFundSelectPriceBasis_Authoriser` | String |  |  |
| 23 | `FS.GI.FUND.SELECT.PRICE.BASIS.CO.CODE` | `FsGiFundSelectPriceBasis_CoCode` | String |  |  |
| 24 | `FS.GI.FUND.SELECT.PRICE.BASIS.DEPT.CODE` | `FsGiFundSelectPriceBasis_DeptCode` | String |  |  |
| 25 | `FS.GI.FUND.SELECT.PRICE.BASIS.AUDITOR.CODE` | `FsGiFundSelectPriceBasis_AuditorCode` | String |  |  |
| 26 | `FS.GI.FUND.SELECT.PRICE.BASIS.AUDIT.DATE.TIME` | `FsGiFundSelectPriceBasis_AuditDateTime` | String |  |  |
