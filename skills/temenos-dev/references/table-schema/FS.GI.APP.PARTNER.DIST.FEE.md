# FS.GI.APP.PARTNER.DIST.FEE — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.PARTNER.DIST.FEE` in `FS_LimitedPartnershipStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.PARTNER.DIST.FEE.PARENT.REF.ID` | `FsGiAppPartnerDistFee_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.PARTNER.DIST.FEE.ORA.ROWID` | `FsGiAppPartnerDistFee_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.PARTNER.DIST.FEE.REGISTER.ID` | `FsGiAppPartnerDistFee_RegisterId` | TField |  | Register ID linked to the partnership management. Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.APP.PARTNER.DIST.FEE.TA.FUND.ID` | `FsGiAppPartnerDistFee_TaFundId` | TField |  | Fund internal ID. Fund ID which was defined with management type as partnership fund. Multifonds DB Column is NPTF. |
| 5 | `FS.GI.APP.PARTNER.DIST.FEE.SHARE.CLASS.CODE` | `FsGiAppPartnerDistFee_ShareClassCode` | TField |  | Fund share class linked to the partnership fund. Multifonds DB Column is TPART. |
| 6 | `FS.GI.APP.PARTNER.DIST.FEE.FEE.TYPE` | `FsGiAppPartnerDistFee_FeeType` | TField |  | Asset based fee type to be netted out before income distribution for the register parternship in the fund share class. Multifonds DB Column is FEE_TYPES. |
| 7 | `FS.GI.APP.PARTNER.DIST.FEE.FUND.ID` | `FsGiAppPartnerDistFee_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 8 | `FS.GI.APP.PARTNER.DIST.FEE.CLASS.CURRENCY` | `FsGiAppPartnerDistFee_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 9 | `FS.GI.APP.PARTNER.DIST.FEE.RESERVED10` | `FsGiAppPartnerDistFee_Reserved10` | TField |  |  |
| 10 | `FS.GI.APP.PARTNER.DIST.FEE.RESERVED9` | `FsGiAppPartnerDistFee_Reserved9` | TField |  |  |
| 11 | `FS.GI.APP.PARTNER.DIST.FEE.RESERVED8` | `FsGiAppPartnerDistFee_Reserved8` | TField |  |  |
| 12 | `FS.GI.APP.PARTNER.DIST.FEE.RESERVED7` | `FsGiAppPartnerDistFee_Reserved7` | TField |  |  |
| 13 | `FS.GI.APP.PARTNER.DIST.FEE.RESERVED6` | `FsGiAppPartnerDistFee_Reserved6` | TField |  |  |
| 14 | `FS.GI.APP.PARTNER.DIST.FEE.RESERVED5` | `FsGiAppPartnerDistFee_Reserved5` | TField |  |  |
| 15 | `FS.GI.APP.PARTNER.DIST.FEE.RESERVED4` | `FsGiAppPartnerDistFee_Reserved4` | TField |  |  |
| 16 | `FS.GI.APP.PARTNER.DIST.FEE.RESERVED3` | `FsGiAppPartnerDistFee_Reserved3` | TField |  |  |
| 17 | `FS.GI.APP.PARTNER.DIST.FEE.RESERVED2` | `FsGiAppPartnerDistFee_Reserved2` | TField |  |  |
| 18 | `FS.GI.APP.PARTNER.DIST.FEE.RESERVED1` | `FsGiAppPartnerDistFee_Reserved1` | TField |  |  |
| 19 | `FS.GI.APP.PARTNER.DIST.FEE.LOCAL.REF` | `FsGiAppPartnerDistFee_LocalRef` |  |  |  |
| 20 | `FS.GI.APP.PARTNER.DIST.FEE.OVERRIDE` | `FsGiAppPartnerDistFee_Override` |  |  |  |
| 21 | `FS.GI.APP.PARTNER.DIST.FEE.RECORD.STATUS` | `FsGiAppPartnerDistFee_RecordStatus` | String |  |  |
| 22 | `FS.GI.APP.PARTNER.DIST.FEE.CURR.NO` | `FsGiAppPartnerDistFee_CurrNo` | String |  |  |
| 23 | `FS.GI.APP.PARTNER.DIST.FEE.INPUTTER` | `FsGiAppPartnerDistFee_Inputter` |  |  |  |
| 24 | `FS.GI.APP.PARTNER.DIST.FEE.DATE.TIME` | `FsGiAppPartnerDistFee_DateTime` |  |  |  |
| 25 | `FS.GI.APP.PARTNER.DIST.FEE.AUTHORISER` | `FsGiAppPartnerDistFee_Authoriser` | String |  |  |
| 26 | `FS.GI.APP.PARTNER.DIST.FEE.CO.CODE` | `FsGiAppPartnerDistFee_CoCode` | String |  |  |
| 27 | `FS.GI.APP.PARTNER.DIST.FEE.DEPT.CODE` | `FsGiAppPartnerDistFee_DeptCode` | String |  |  |
| 28 | `FS.GI.APP.PARTNER.DIST.FEE.AUDITOR.CODE` | `FsGiAppPartnerDistFee_AuditorCode` | String |  |  |
| 29 | `FS.GI.APP.PARTNER.DIST.FEE.AUDIT.DATE.TIME` | `FsGiAppPartnerDistFee_AuditDateTime` | String |  |  |
