# USREGS.FDIC.PARAMETER — Table Schema

> Source: `INSERTS/I_F.USREGS.FDIC.PARAMETER` in `USREGS_FDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FDIC.PARM.DESCRIPTION` | `UsregsFdicParameter_Description` |  |  |  |
| 2 | `FDIC.PARM.FDIC.HOLD.TYPE` | `UsregsFdicParameter_FdicHoldType` | TField |  | The bank must select FDIC Hold as the type of hold to identify each AC.LOCKED.EVENT record where an FDIC Provisional Hold is required. A Valid record must be created in USCORE.HOLD.PARAMETER table in order to list as drop down in this field. |
| 3 | `FDIC.PARM.DIR.PATH` | `UsregsFdicParameter_DirPath` | TField |  | The System/Network directory (path) where the FDIC Incoming Files are will be stored for importing and processing. |
| 4 | `FDIC.PARM.RESERVED.32` | `UsregsFdicParameter_Reserved30` |  |  |  |
| 5 | `FDIC.PARM.RESERVED.31` | `UsregsFdicParameter_Reserved30` |  |  |  |
| 6 | `FDIC.PARM.DEFAULT.FTTC` | `UsregsFdicParameter_DefaultFttc` |  |  |  |
| 7 | `FDIC.PARM.DEFAULT.SETTLE.TYPE` | `UsregsFdicParameter_DefaultSettleType` |  |  |  |
| 8 | `FDIC.PARM.DEFAULT.SETTLE.CATEG` | `UsregsFdicParameter_DefaultSettleCateg` |  |  |  |
| 9 | `FDIC.PARM.RESERVED.28` | `UsregsFdicParameter_Reserved28` |  |  |  |
| 10 | `FDIC.PARM.RESERVED.27` | `UsregsFdicParameter_Reserved27` |  |  |  |
| 11 | `FDIC.PARM.RESERVED.26` | `UsregsFdicParameter_Reserved26` |  |  |  |
| 12 | `FDIC.PARM.CATEGORY` | `UsregsFdicParameter_Category` |  |  |  |
| 13 | `FDIC.PARM.ACCOUNT.CLASS` | `UsregsFdicParameter_AccountClass` |  |  |  |
| 14 | `FDIC.PARM.CURRENCY` | `UsregsFdicParameter_Currency` |  |  |  |
| 15 | `FDIC.PARM.BALANCE.THRESHOLD` | `UsregsFdicParameter_BalanceThreshold` |  |  |  |
| 16 | `FDIC.PARM.HOLD.PERCENTAGE` | `UsregsFdicParameter_HoldPercentage` |  |  |  |
| 17 | `FDIC.PARM.CAT.SETTLEMENT.ACCT` | `UsregsFdicParameter_CatSettlementAcct` |  |  |  |
| 18 | `FDIC.PARM.CAT.FTTC` | `UsregsFdicParameter_CatFttc` |  |  |  |
| 19 | `FDIC.PARM.RESERVED.25` | `UsregsFdicParameter_Reserved25` |  |  |  |
| 20 | `FDIC.PARM.RESERVED.24` | `UsregsFdicParameter_Reserved24` |  |  |  |
| 21 | `FDIC.PARM.RESERVED.23` | `UsregsFdicParameter_Reserved23` |  |  |  |
| 22 | `FDIC.PARM.RESERVED.22` | `UsregsFdicParameter_Reserved22` |  |  |  |
| 23 | `FDIC.PARM.RESERVED.21` | `UsregsFdicParameter_Reserved21` |  |  |  |
| 24 | `FDIC.PARM.AA.PRODUCT.GROUP` | `UsregsFdicParameter_AaProductGroup` |  |  |  |
| 25 | `FDIC.PARM.AA.PG.PRODUCT` | `UsregsFdicParameter_AaPgProduct` |  |  |  |
| 26 | `FDIC.PARM.RESERVED.30` | `UsregsFdicParameter_Reserved30` |  |  |  |
| 27 | `FDIC.PARM.AA.PG.BALANCE.THRESHOLD` | `UsregsFdicParameter_AaPgBalanceThreshold` |  |  |  |
| 28 | `FDIC.PARM.AA.PG.HOLD.PERCENTAGE` | `UsregsFdicParameter_AaPgHoldPercentage` |  |  |  |
| 29 | `FDIC.PARM.AA.PG.SETTLEMENT.ACCT` | `UsregsFdicParameter_AaPgSettlementAcct` |  |  |  |
| 30 | `FDIC.PARM.AA.FTTC` | `UsregsFdicParameter_AaFttc` |  |  |  |
| 31 | `FDIC.PARM.RESERVED.20` | `UsregsFdicParameter_Reserved20` |  |  |  |
| 32 | `FDIC.PARM.RESERVED.19` | `UsregsFdicParameter_Reserved19` |  |  |  |
| 33 | `FDIC.PARM.RESERVED.18` | `UsregsFdicParameter_Reserved18` |  |  |  |
| 34 | `FDIC.PARM.RESERVED.17` | `UsregsFdicParameter_Reserved17` |  |  |  |
| 35 | `FDIC.PARM.RESERVED.16` | `UsregsFdicParameter_Reserved16` |  |  |  |
| 36 | `FDIC.PARM.RESERVED.15` | `UsregsFdicParameter_Reserved15` |  |  |  |
| 37 | `FDIC.PARM.RESERVED.14` | `UsregsFdicParameter_Reserved14` |  |  |  |
| 38 | `FDIC.PARM.RESERVED.13` | `UsregsFdicParameter_Reserved13` | TField |  |  |
| 39 | `FDIC.PARM.RESERVED.12` | `UsregsFdicParameter_Reserved12` | TField |  |  |
| 40 | `FDIC.PARM.RESERVED.11` | `UsregsFdicParameter_Reserved11` | TField |  |  |
| 41 | `FDIC.PARM.RESERVED.10` | `UsregsFdicParameter_Reserved10` | TField |  |  |
| 42 | `FDIC.PARM.RESERVED.9` | `UsregsFdicParameter_Reserved9` | TField |  |  |
| 43 | `FDIC.PARM.RESERVED.8` | `UsregsFdicParameter_Reserved8` | TField |  |  |
| 44 | `FDIC.PARM.RESERVED.7` | `UsregsFdicParameter_Reserved7` | TField |  |  |
| 45 | `FDIC.PARM.RESERVED.6` | `UsregsFdicParameter_Reserved6` | TField |  |  |
| 46 | `FDIC.PARM.RESERVED.5` | `UsregsFdicParameter_Reserved5` | TField |  |  |
| 47 | `FDIC.PARM.RESERVED.4` | `UsregsFdicParameter_Reserved4` | TField |  |  |
| 48 | `FDIC.PARM.RESERVED.3` | `UsregsFdicParameter_Reserved3` | TField |  |  |
| 49 | `FDIC.PARM.RESERVED.2` | `UsregsFdicParameter_Reserved2` | TField |  |  |
| 50 | `FDIC.PARM.RESERVED.1` | `UsregsFdicParameter_Reserved1` | TField |  |  |
| 51 | `FDIC.PARM.LOCAL.REF` | `UsregsFdicParameter_LocalRef` |  |  |  |
| 52 | `FDIC.PARM.OVERRIDE` | `UsregsFdicParameter_Override` |  |  |  |
| 53 | `FDIC.PARM.RECORD.STATUS` | `UsregsFdicParameter_RecordStatus` | String |  |  |
| 54 | `FDIC.PARM.CURR.NO` | `UsregsFdicParameter_CurrNo` | String |  |  |
| 55 | `FDIC.PARM.INPUTTER` | `UsregsFdicParameter_Inputter` |  |  |  |
| 56 | `FDIC.PARM.DATE.TIME` | `UsregsFdicParameter_DateTime` |  |  |  |
| 57 | `FDIC.PARM.AUTHORISER` | `UsregsFdicParameter_Authoriser` | String |  |  |
| 58 | `FDIC.PARM.CO.CODE` | `UsregsFdicParameter_CoCode` | String |  |  |
| 59 | `FDIC.PARM.DEPT.CODE` | `UsregsFdicParameter_DeptCode` | String |  |  |
| 60 | `FDIC.PARM.AUDITOR.CODE` | `UsregsFdicParameter_AuditorCode` | String |  |  |
| 61 | `FDIC.PARM.AUDIT.DATE.TIME` | `UsregsFdicParameter_AuditDateTime` | String |  |  |
