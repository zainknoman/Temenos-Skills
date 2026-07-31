# TAM.PRL.ASSET.DOWNLOAD — Table Schema

> Source: `INSERTS/I_F.TAM.PRL.ASSET.DOWNLOAD` in `CAPLND_ProlenderInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PRL.AST.REQ` | `TamPrlAssetDownload_Req` |  |  |  |
| 2 | `PRL.AST.DESCRIPTION` | `TamPrlAssetDownload_Description` |  |  |  |
| 3 | `PRL.AST.CUID` | `TamPrlAssetDownload_Cuid` |  |  |  |
| 4 | `PRL.AST.USERID` | `TamPrlAssetDownload_Userid` |  |  |  |
| 5 | `PRL.AST.PASSWORD` | `TamPrlAssetDownload_Password` |  |  |  |
| 6 | `PRL.AST.REQUEST.ID` | `TamPrlAssetDownload_RequestId` |  |  |  |
| 7 | `PRL.AST.TIME.STAMP` | `TamPrlAssetDownload_TimeStamp` |  |  |  |
| 8 | `PRL.AST.STATUS.CODE` | `TamPrlAssetDownload_StatusCode` |  |  |  |
| 9 | `PRL.AST.ENTITY.TYPE` | `TamPrlAssetDownload_EntityType` |  |  |  |
| 10 | `PRL.AST.MESSAGE.CODE` | `TamPrlAssetDownload_MessageCode` |  |  |  |
| 11 | `PRL.AST.MESSAGE.TEXT` | `TamPrlAssetDownload_MessageText` |  |  |  |
| 12 | `PRL.AST.MEMBER.SIN.NO` | `TamPrlAssetDownload_MemberSinNo` |  |  |  |
| 13 | `PRL.AST.SPOUSE.SIN.NO` | `TamPrlAssetDownload_SpouseSinNo` |  |  |  |
| 14 | `PRL.AST.CIF.NO` | `TamPrlAssetDownload_CifNo` |  |  |  |
| 15 | `PRL.AST.ASSET.TYPE` | `TamPrlAssetDownload_AssetType` |  |  |  |
| 16 | `PRL.AST.ASSET.DESC` | `TamPrlAssetDownload_AssetDesc` |  |  |  |
| 17 | `PRL.AST.ACCOUNT.NO` | `TamPrlAssetDownload_AccountNo` |  |  |  |
| 18 | `PRL.AST.MATURITY.DATE` | `TamPrlAssetDownload_MaturityDate` |  |  |  |
| 19 | `PRL.AST.LEDGER.BALANCE` | `TamPrlAssetDownload_LedgerBalance` |  |  |  |
| 20 | `PRL.AST.PURCHASE.PRICE` | `TamPrlAssetDownload_PurchasePrice` |  |  |  |
| 21 | `PRL.AST.MKT.VALUE` | `TamPrlAssetDownload_MktValue` |  |  |  |
| 22 | `PRL.AST.MKT.VALUE.SOURCE` | `TamPrlAssetDownload_MktValueSource` |  |  |  |
| 23 | `PRL.AST.MKT.VALUE.DATE` | `TamPrlAssetDownload_MktValueDate` |  |  |  |
| 24 | `PRL.AST.REGISTERED.OWNER1` | `TamPrlAssetDownload_RegisteredOwner1` |  |  |  |
| 25 | `PRL.AST.REGISTERED.OWNER2` | `TamPrlAssetDownload_RegisteredOwner2` |  |  |  |
| 26 | `PRL.AST.REGISTERED.OWNER3` | `TamPrlAssetDownload_RegisteredOwner3` |  |  |  |
| 27 | `PRL.AST.NOMINAL.RATE` | `TamPrlAssetDownload_NominalRate` |  |  |  |
| 28 | `PRL.AST.HOLD.AMOUNT` | `TamPrlAssetDownload_HoldAmount` |  |  |  |
| 29 | `PRL.AST.RECORD.STATUS` | `TamPrlAssetDownload_RecordStatus` |  |  |  |
| 30 | `PRL.AST.CURR.NO` | `TamPrlAssetDownload_CurrNo` |  |  |  |
| 31 | `PRL.AST.INPUTTER` | `TamPrlAssetDownload_Inputter` |  |  |  |
| 32 | `PRL.AST.DATE.TIME` | `TamPrlAssetDownload_DateTime` |  |  |  |
| 33 | `PRL.AST.AUTHORISER` | `TamPrlAssetDownload_Authoriser` |  |  |  |
| 34 | `PRL.AST.CO.CODE` | `TamPrlAssetDownload_CoCode` |  |  |  |
| 35 | `PRL.AST.DEPT.CODE` | `TamPrlAssetDownload_DeptCode` |  |  |  |
| 36 | `PRL.AST.AUDITOR.CODE` | `TamPrlAssetDownload_AuditorCode` |  |  |  |
| 37 | `PRL.AST.AUDIT.DATE.TIME` | `TamPrlAssetDownload_AuditDateTime` |  |  |  |
