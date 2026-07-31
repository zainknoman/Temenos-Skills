# POLICY.PARAMETER — Table Schema

> Source: `INSERTS/I_F.POLICY.PARAMETER` in `SC_SctModelling.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PLC.MODEL.DESC` | `PolicyParameter_ModelDesc` | TField |  | This is a description of the portfolio model. Validation Rules: 35 characters free format text. |
| 2 | `SC.PLC.MODEL.LEVEL` | `PolicyParameter_ModelLevel` | TField |  | Indicates the detail level of the model. Validation Rules: Input allowed - C (Country) S (Security) |
| 3 | `SC.PLC.ASSET.TYPE` | `PolicyParameter_AssetType` |  |  |  |
| 4 | `SC.PLC.ASSET.COU` | `PolicyParameter_AssetCou` |  |  |  |
| 5 | `SC.PLC.ASSET.SEC.NO` | `PolicyParameter_AssetSecNo` |  |  |  |
| 6 | `SC.PLC.ASSET.CCY` | `PolicyParameter_AssetCcy` |  |  |  |
| 7 | `SC.PLC.ASSET.PCNT` | `PolicyParameter_AssetPcnt` |  |  |  |
| 8 | `SC.PLC.ASSET.MAX.TL` | `PolicyParameter_AssetMaxTl` |  |  |  |
| 9 | `SC.PLC.ASSET.MIN.TL` | `PolicyParameter_AssetMinTl` |  |  |  |
| 10 | `SC.PLC.ASSET.FROM` | `PolicyParameter_AssetFrom` |  |  |  |
| 11 | `SC.PLC.ASSET.TO` | `PolicyParameter_AssetTo` |  |  |  |
| 12 | `SC.PLC.SUB.ASSET.TYPE` | `PolicyParameter_SubAssetType` |  |  |  |
| 13 | `SC.PLC.SUB.ASS.COU` | `PolicyParameter_SubAssCou` |  |  |  |
| 14 | `SC.PLC.SUB.ASS.SCNO` | `PolicyParameter_SubAssScno` |  |  |  |
| 15 | `SC.PLC.SUB.ASS.CCY` | `PolicyParameter_SubAssCcy` |  |  |  |
| 16 | `SC.PLC.SUB.ASS.PCNT` | `PolicyParameter_SubAssPcnt` |  |  |  |
| 17 | `SC.PLC.SUB.ASS.MXTL` | `PolicyParameter_SubAssMxtl` |  |  |  |
| 18 | `SC.PLC.SUB.ASS.MNTL` | `PolicyParameter_SubAssMntl` |  |  |  |
| 19 | `SC.PLC.SUB.ASS.FROM` | `PolicyParameter_SubAssFrom` |  |  |  |
| 20 | `SC.PLC.SUB.ASS.TO` | `PolicyParameter_SubAssTo` |  |  |  |
| 21 | `SC.PLC.IND.CODE` | `PolicyParameter_IndCode` |  |  |  |
| 22 | `SC.PLC.IND.PCNT` | `PolicyParameter_IndPcnt` |  |  |  |
| 23 | `SC.PLC.IND.VARI` | `PolicyParameter_IndVari` |  |  |  |
| 24 | `SC.PLC.EXCL.ASS.TYPE` | `PolicyParameter_ExclAssType` |  |  |  |
| 25 | `SC.PLC.EXCL.SEC.NO` | `PolicyParameter_ExclSecNo` |  |  |  |
| 26 | `SC.PLC.EXCL.COUNTRY` | `PolicyParameter_ExclCountry` |  |  |  |
| 27 | `SC.PLC.EXCL.SUB.ASS` | `PolicyParameter_ExclSubAss` |  |  |  |
| 28 | `SC.PLC.EXCL.SEC` | `PolicyParameter_ExclSec` |  |  |  |
| 29 | `SC.PLC.EXCL.COU` | `PolicyParameter_ExclCou` |  |  |  |
| 30 | `SC.PLC.REBUILD.MODEL` | `PolicyParameter_RebuildModel` | TField |  | Determines whether the portfolio model is re-built when the record is authorised. Validation Rules: Input allowed: YES NO (the default if field left blank) |
| 31 | `SC.PLC.RESERVED.9` | `PolicyParameter_Reserved9` | TField |  |  |
| 32 | `SC.PLC.RESERVED.8` | `PolicyParameter_Reserved8` | TField |  |  |
| 33 | `SC.PLC.RESERVED.7` | `PolicyParameter_Reserved7` | TField |  |  |
| 34 | `SC.PLC.RESERVED.6` | `PolicyParameter_Reserved6` | TField |  |  |
| 35 | `SC.PLC.RESERVED.5` | `PolicyParameter_Reserved5` | TField |  |  |
| 36 | `SC.PLC.RESERVED.4` | `PolicyParameter_Reserved4` | TField |  |  |
| 37 | `SC.PLC.RESERVED.3` | `PolicyParameter_Reserved3` | TField |  |  |
| 38 | `SC.PLC.RESERVED.2` | `PolicyParameter_Reserved2` | TField |  |  |
| 39 | `SC.PLC.RESERVED.1` | `PolicyParameter_Reserved1` | TField |  |  |
| 40 | `SC.PLC.LOCAL.REF` | `PolicyParameter_LocalRef` |  |  |  |
| 41 | `SC.PLC.RECORD.STATUS` | `PolicyParameter_RecordStatus` | String |  |  |
| 42 | `SC.PLC.CURR.NO` | `PolicyParameter_CurrNo` | String |  |  |
| 43 | `SC.PLC.INPUTTER` | `PolicyParameter_Inputter` |  |  |  |
| 44 | `SC.PLC.DATE.TIME` | `PolicyParameter_DateTime` |  |  |  |
| 45 | `SC.PLC.AUTHORISER` | `PolicyParameter_Authoriser` | String |  |  |
| 46 | `SC.PLC.CO.CODE` | `PolicyParameter_CoCode` | String |  |  |
| 47 | `SC.PLC.DEPT.CODE` | `PolicyParameter_DeptCode` | String |  |  |
| 48 | `SC.PLC.AUDITOR.CODE` | `PolicyParameter_AuditorCode` | String |  |  |
| 49 | `SC.PLC.AUDIT.DATE.TIME` | `PolicyParameter_AuditDateTime` | String |  |  |
