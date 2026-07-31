# ASSET.ENTITY — Table Schema

> Source: `INSERTS/I_F.ASSET.ENTITY` in `FIXAMT_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AST.ENT.SHORT.DESCRIPTION` | `AssetEntity_ShortDescription` | TField |  | Short Description of the Organisation Unit to be used for enrichment purpose. |
| 2 | `AST.ENT.AUTO.OPEN.FA.ACCT` | `AssetEntity_AutoOpenFaAcct` | TField |  | If this field is set to Yes, then Internal Accounts will be automatically opened for maintaining various balances of the Asset. The choices are either Yes or No. |
| 3 | `AST.ENT.AUTO.ACCT.SEQUENCE` | `AssetEntity_AutoAcctSequence` | TField |  | Numeric Value between 0001 - 9999. Sequence Number used in automatic opening of accounts. |
| 4 | `AST.ENT.AUTO.ACCOUNT.DAO` | `AssetEntity_AutoAccountDao` | TField |  | It is a reference to DAO table and used in automatic opening of Internal Accounts. |
| 5 | `AST.ENT.ASSET.CLASS` | `AssetEntity_AssetClass` |  |  |  |
| 6 | `AST.ENT.ASSET.ACCT.NUM` | `AssetEntity_AssetAcctNum` |  |  |  |
| 7 | `AST.ENT.PROV.ACCT.NUM` | `AssetEntity_ProvAcctNum` |  |  |  |
| 8 | `AST.ENT.WRITEOFF.ACCT.NUM` | `AssetEntity_WriteoffAcctNum` |  |  |  |
| 9 | `AST.ENT.CWIP.ACCT.NUM` | `AssetEntity_CwipAcctNum` |  |  |  |
| 10 | `AST.ENT.PAYABLE.ACCT.NUM` | `AssetEntity_PayableAcctNum` |  |  |  |
| 11 | `AST.ENT.RECEIVABLE.ACCT.NUM` | `AssetEntity_ReceivableAcctNum` |  |  |  |
| 12 | `AST.ENT.PROFIT.CATEGORY` | `AssetEntity_ProfitCategory` |  |  |  |
| 13 | `AST.ENT.LOSS.CATEGORY` | `AssetEntity_LossCategory` |  |  |  |
| 14 | `AST.ENT.RESERVED.8` | `AssetEntity_Reserved8` |  |  |  |
| 15 | `AST.ENT.RESERVED.7` | `AssetEntity_Reserved7` | TField |  |  |
| 16 | `AST.ENT.RESERVED.6` | `AssetEntity_Reserved6` | TField |  |  |
| 17 | `AST.ENT.RESERVED.5` | `AssetEntity_Reserved5` | TField |  |  |
| 18 | `AST.ENT.RESERVED.4` | `AssetEntity_Reserved4` | TField |  |  |
| 19 | `AST.ENT.RESERVED.3` | `AssetEntity_Reserved3` | TField |  |  |
| 20 | `AST.ENT.RESERVED.2` | `AssetEntity_Reserved2` | TField |  |  |
| 21 | `AST.ENT.RESERVED.1` | `AssetEntity_Reserved1` | TField |  |  |
| 22 | `AST.ENT.LOCAL.REF` | `AssetEntity_LocalRef` |  |  |  |
| 23 | `AST.ENT.OVERRIDE` | `AssetEntity_Override` |  |  |  |
| 24 | `AST.ENT.RECORD.STATUS` | `AssetEntity_RecordStatus` | String |  |  |
| 25 | `AST.ENT.CURR.NO` | `AssetEntity_CurrNo` | String |  |  |
| 26 | `AST.ENT.INPUTTER` | `AssetEntity_Inputter` |  |  |  |
| 27 | `AST.ENT.DATE.TIME` | `AssetEntity_DateTime` |  |  |  |
| 28 | `AST.ENT.AUTHORISER` | `AssetEntity_Authoriser` | String |  |  |
| 29 | `AST.ENT.CO.CODE` | `AssetEntity_CoCode` | String |  |  |
| 30 | `AST.ENT.DEPT.CODE` | `AssetEntity_DeptCode` | String |  |  |
| 31 | `AST.ENT.AUDITOR.CODE` | `AssetEntity_AuditorCode` | String |  |  |
| 32 | `AST.ENT.AUDIT.DATE.TIME` | `AssetEntity_AuditDateTime` | String |  |  |
