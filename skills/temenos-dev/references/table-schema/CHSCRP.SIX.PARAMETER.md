# CHSCRP.SIX.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CHSCRP.SIX.PARAMETER` in `CHSCRP_SixReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CHSCSIX.EUREX` | `ChscrpSixParameter_Eurex` |  |  |  |
| 2 | `CHSCSIX.ALT.ID` | `ChscrpSixParameter_AltId` | TField |  | User to input the alternate indicator id to be checked to get the ISIN from DX.CONTRACT.MASTER application to be compared with the SIX received file. |
| 3 | `CHSCSIX.ALT.ISIN` | `ChscrpSixParameter_AltIsin` | TField |  | User to input the alternate indicator id to be considered to get the ISIN from SECURITY.MASTER application to be compared with the SIX received file. |
| 4 | `CHSCSIX.CFI.CODE` | `ChscrpSixParameter_CfiCode` | TField |  | User to parameterize the alternate indicate name of the CFI code, for the system to identify and report in SIX files for DX instruments. |
| 5 | `CHSCSIX.SUB.ASSET.TYPE` | `ChscrpSixParameter_SubAssetType` |  |  |  |
| 6 | `CHSCSIX.LOCAL.REF` | `ChscrpSixParameter_LocalRef` |  |  |  |
| 7 | `CHSCSIX.IND.SECTOR` | `ChscrpSixParameter_IndSector` |  |  |  |
| 8 | `CHSCSIX.ROLE` | `ChscrpSixParameter_Role` |  |  |  |
| 9 | `CHSCSIX.DOCUMENT.NAME` | `ChscrpSixParameter_DocumentName` |  |  |  |
| 10 | `CHSCSIX.RESERVED.2` | `ChscrpSixParameter_Reserved2` | TField |  | Reserved field for future use. |
| 11 | `CHSCSIX.RESERVED.1` | `ChscrpSixParameter_Reserved1` | TField |  | Reserved field for future use. |
| 12 | `CHSCSIX.OVERRIDE` | `ChscrpSixParameter_Override` |  |  |  |
| 13 | `CHSCSIX.RECORD.STATUS` | `ChscrpSixParameter_RecordStatus` | String |  |  |
| 14 | `CHSCSIX.CURR.NO` | `ChscrpSixParameter_CurrNo` | String |  |  |
| 15 | `CHSCSIX.INPUTTER` | `ChscrpSixParameter_Inputter` |  |  |  |
| 16 | `CHSCSIX.DATE.TIME` | `ChscrpSixParameter_DateTime` |  |  |  |
| 17 | `CHSCSIX.AUTHORISER` | `ChscrpSixParameter_Authoriser` | String |  |  |
| 18 | `CHSCSIX.CO.CODE` | `ChscrpSixParameter_CoCode` | String |  |  |
| 19 | `CHSCSIX.DEPT.CODE` | `ChscrpSixParameter_DeptCode` | String |  |  |
| 20 | `CHSCSIX.AUDITOR.CODE` | `ChscrpSixParameter_AuditorCode` | String |  |  |
| 21 | `CHSCSIX.AUDIT.DATE.TIME` | `ChscrpSixParameter_AuditDateTime` | String |  |  |
