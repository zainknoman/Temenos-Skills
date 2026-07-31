# FS.GA.BLENDED.TAX.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.BLENDED.TAX.EXCEPTION` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.BLENDED.TAX.EXCEPTION.PARENT.REF.ID` | `FsGaBlendedTaxException_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.BLENDED.TAX.EXCEPTION.ORA.ROWID` | `FsGaBlendedTaxException_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.BLENDED.TAX.EXCEPTION.FUND.ID` | `FsGaBlendedTaxException_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.BLENDED.TAX.EXCEPTION.OPERATION.CODE` | `FsGaBlendedTaxException_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 5 | `FS.GA.BLENDED.TAX.EXCEPTION.DEFAULT.CODE` | `FsGaBlendedTaxException_DefaultCode` | TField |  | Default Coper Identifier Multifonds DB Column is FLG_BT. |
| 6 | `FS.GA.BLENDED.TAX.EXCEPTION.RESERVED10` | `FsGaBlendedTaxException_Reserved10` | TField |  |  |
| 7 | `FS.GA.BLENDED.TAX.EXCEPTION.RESERVED9` | `FsGaBlendedTaxException_Reserved9` | TField |  |  |
| 8 | `FS.GA.BLENDED.TAX.EXCEPTION.RESERVED8` | `FsGaBlendedTaxException_Reserved8` | TField |  |  |
| 9 | `FS.GA.BLENDED.TAX.EXCEPTION.RESERVED7` | `FsGaBlendedTaxException_Reserved7` | TField |  |  |
| 10 | `FS.GA.BLENDED.TAX.EXCEPTION.RESERVED6` | `FsGaBlendedTaxException_Reserved6` | TField |  |  |
| 11 | `FS.GA.BLENDED.TAX.EXCEPTION.RESERVED5` | `FsGaBlendedTaxException_Reserved5` | TField |  |  |
| 12 | `FS.GA.BLENDED.TAX.EXCEPTION.RESERVED4` | `FsGaBlendedTaxException_Reserved4` | TField |  |  |
| 13 | `FS.GA.BLENDED.TAX.EXCEPTION.RESERVED3` | `FsGaBlendedTaxException_Reserved3` | TField |  |  |
| 14 | `FS.GA.BLENDED.TAX.EXCEPTION.RESERVED2` | `FsGaBlendedTaxException_Reserved2` | TField |  |  |
| 15 | `FS.GA.BLENDED.TAX.EXCEPTION.RESERVED1` | `FsGaBlendedTaxException_Reserved1` | TField |  |  |
| 16 | `FS.GA.BLENDED.TAX.EXCEPTION.LOCAL.REF` | `FsGaBlendedTaxException_LocalRef` |  |  |  |
| 17 | `FS.GA.BLENDED.TAX.EXCEPTION.OVERRIDE` | `FsGaBlendedTaxException_Override` |  |  |  |
| 18 | `FS.GA.BLENDED.TAX.EXCEPTION.RECORD.STATUS` | `FsGaBlendedTaxException_RecordStatus` | String |  |  |
| 19 | `FS.GA.BLENDED.TAX.EXCEPTION.CURR.NO` | `FsGaBlendedTaxException_CurrNo` | String |  |  |
| 20 | `FS.GA.BLENDED.TAX.EXCEPTION.INPUTTER` | `FsGaBlendedTaxException_Inputter` |  |  |  |
| 21 | `FS.GA.BLENDED.TAX.EXCEPTION.DATE.TIME` | `FsGaBlendedTaxException_DateTime` |  |  |  |
| 22 | `FS.GA.BLENDED.TAX.EXCEPTION.AUTHORISER` | `FsGaBlendedTaxException_Authoriser` | String |  |  |
| 23 | `FS.GA.BLENDED.TAX.EXCEPTION.CO.CODE` | `FsGaBlendedTaxException_CoCode` | String |  |  |
| 24 | `FS.GA.BLENDED.TAX.EXCEPTION.DEPT.CODE` | `FsGaBlendedTaxException_DeptCode` | String |  |  |
| 25 | `FS.GA.BLENDED.TAX.EXCEPTION.AUDITOR.CODE` | `FsGaBlendedTaxException_AuditorCode` | String |  |  |
| 26 | `FS.GA.BLENDED.TAX.EXCEPTION.AUDIT.DATE.TIME` | `FsGaBlendedTaxException_AuditDateTime` | String |  |  |
