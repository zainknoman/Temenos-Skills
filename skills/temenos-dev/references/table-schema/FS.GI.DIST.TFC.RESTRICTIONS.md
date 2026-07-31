# FS.GI.DIST.TFC.RESTRICTIONS — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.TFC.RESTRICTIONS` in `FS_InvestorAccountStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.TFC.RESTRICTIONS.PARENT.REF.ID` | `FsGiDistTfcRestrictions_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.TFC.RESTRICTIONS.ORA.ROWID` | `FsGiDistTfcRestrictions_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.TFC.RESTRICTIONS.REGISTER.ID` | `FsGiDistTfcRestrictions_RegisterId` | TField |  | Register internal ID. Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.DIST.TFC.RESTRICTIONS.LEGAL.ENTITY.ID` | `FsGiDistTfcRestrictions_LegalEntityId` | TField |  | Legal Entity ID in which the register is allowed to place deal. Multifonds DB Column is NTFC. |
| 5 | `FS.GI.DIST.TFC.RESTRICTIONS.TA.FUND.ID` | `FsGiDistTfcRestrictions_TaFundId` | TField |  | Fund internal ID in which the register is allowed to place deal. Multifonds DB Column is NPTF. |
| 6 | `FS.GI.DIST.TFC.RESTRICTIONS.SHARE.CLASS.CODE` | `FsGiDistTfcRestrictions_ShareClassCode` | TField |  | Fund share class in which the register is allowed to place deal. Multifonds DB Column is TPART. |
| 7 | `FS.GI.DIST.TFC.RESTRICTIONS.FUND.ID` | `FsGiDistTfcRestrictions_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 8 | `FS.GI.DIST.TFC.RESTRICTIONS.CLASS.CURRENCY` | `FsGiDistTfcRestrictions_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 9 | `FS.GI.DIST.TFC.RESTRICTIONS.RESERVED10` | `FsGiDistTfcRestrictions_Reserved10` | TField |  |  |
| 10 | `FS.GI.DIST.TFC.RESTRICTIONS.RESERVED9` | `FsGiDistTfcRestrictions_Reserved9` | TField |  |  |
| 11 | `FS.GI.DIST.TFC.RESTRICTIONS.RESERVED8` | `FsGiDistTfcRestrictions_Reserved8` | TField |  |  |
| 12 | `FS.GI.DIST.TFC.RESTRICTIONS.RESERVED7` | `FsGiDistTfcRestrictions_Reserved7` | TField |  |  |
| 13 | `FS.GI.DIST.TFC.RESTRICTIONS.RESERVED6` | `FsGiDistTfcRestrictions_Reserved6` | TField |  |  |
| 14 | `FS.GI.DIST.TFC.RESTRICTIONS.RESERVED5` | `FsGiDistTfcRestrictions_Reserved5` | TField |  |  |
| 15 | `FS.GI.DIST.TFC.RESTRICTIONS.RESERVED4` | `FsGiDistTfcRestrictions_Reserved4` | TField |  |  |
| 16 | `FS.GI.DIST.TFC.RESTRICTIONS.RESERVED3` | `FsGiDistTfcRestrictions_Reserved3` | TField |  |  |
| 17 | `FS.GI.DIST.TFC.RESTRICTIONS.RESERVED2` | `FsGiDistTfcRestrictions_Reserved2` | TField |  |  |
| 18 | `FS.GI.DIST.TFC.RESTRICTIONS.RESERVED1` | `FsGiDistTfcRestrictions_Reserved1` | TField |  |  |
| 19 | `FS.GI.DIST.TFC.RESTRICTIONS.LOCAL.REF` | `FsGiDistTfcRestrictions_LocalRef` |  |  |  |
| 20 | `FS.GI.DIST.TFC.RESTRICTIONS.OVERRIDE` | `FsGiDistTfcRestrictions_Override` |  |  |  |
| 21 | `FS.GI.DIST.TFC.RESTRICTIONS.RECORD.STATUS` | `FsGiDistTfcRestrictions_RecordStatus` | String |  |  |
| 22 | `FS.GI.DIST.TFC.RESTRICTIONS.CURR.NO` | `FsGiDistTfcRestrictions_CurrNo` | String |  |  |
| 23 | `FS.GI.DIST.TFC.RESTRICTIONS.INPUTTER` | `FsGiDistTfcRestrictions_Inputter` |  |  |  |
| 24 | `FS.GI.DIST.TFC.RESTRICTIONS.DATE.TIME` | `FsGiDistTfcRestrictions_DateTime` |  |  |  |
| 25 | `FS.GI.DIST.TFC.RESTRICTIONS.AUTHORISER` | `FsGiDistTfcRestrictions_Authoriser` | String |  |  |
| 26 | `FS.GI.DIST.TFC.RESTRICTIONS.CO.CODE` | `FsGiDistTfcRestrictions_CoCode` | String |  |  |
| 27 | `FS.GI.DIST.TFC.RESTRICTIONS.DEPT.CODE` | `FsGiDistTfcRestrictions_DeptCode` | String |  |  |
| 28 | `FS.GI.DIST.TFC.RESTRICTIONS.AUDITOR.CODE` | `FsGiDistTfcRestrictions_AuditorCode` | String |  |  |
| 29 | `FS.GI.DIST.TFC.RESTRICTIONS.AUDIT.DATE.TIME` | `FsGiDistTfcRestrictions_AuditDateTime` | String |  |  |
