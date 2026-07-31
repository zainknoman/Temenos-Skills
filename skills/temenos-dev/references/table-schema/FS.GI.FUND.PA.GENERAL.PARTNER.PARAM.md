# FS.GI.FUND.PA.GENERAL.PARTNER.PARAM — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.PA.GENERAL.PARTNER.PARAM` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.PARENT.REF.ID` | `FsGiFundPaGeneralPartnerParam_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.ORA.ROWID` | `FsGiFundPaGeneralPartnerParam_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.TA.FUND.ID` | `FsGiFundPaGeneralPartnerParam_TaFundId` | TField |  | Fund internal ID. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.REGISTER.ID` | `FsGiFundPaGeneralPartnerParam_RegisterId` | TField |  | General parternal register internal id. Multifonds DB Column is NREGISTER. |
| 5 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.FUND.ID` | `FsGiFundPaGeneralPartnerParam_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 6 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.CLASS.CURRENCY` | `FsGiFundPaGeneralPartnerParam_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 7 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.RESERVED10` | `FsGiFundPaGeneralPartnerParam_Reserved10` | TField |  |  |
| 8 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.RESERVED9` | `FsGiFundPaGeneralPartnerParam_Reserved9` | TField |  |  |
| 9 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.RESERVED8` | `FsGiFundPaGeneralPartnerParam_Reserved8` | TField |  |  |
| 10 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.RESERVED7` | `FsGiFundPaGeneralPartnerParam_Reserved7` | TField |  |  |
| 11 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.RESERVED6` | `FsGiFundPaGeneralPartnerParam_Reserved6` | TField |  |  |
| 12 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.RESERVED5` | `FsGiFundPaGeneralPartnerParam_Reserved5` | TField |  |  |
| 13 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.RESERVED4` | `FsGiFundPaGeneralPartnerParam_Reserved4` | TField |  |  |
| 14 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.RESERVED3` | `FsGiFundPaGeneralPartnerParam_Reserved3` | TField |  |  |
| 15 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.RESERVED2` | `FsGiFundPaGeneralPartnerParam_Reserved2` | TField |  |  |
| 16 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.RESERVED1` | `FsGiFundPaGeneralPartnerParam_Reserved1` | TField |  |  |
| 17 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.LOCAL.REF` | `FsGiFundPaGeneralPartnerParam_LocalRef` |  |  |  |
| 18 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.OVERRIDE` | `FsGiFundPaGeneralPartnerParam_Override` |  |  |  |
| 19 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.RECORD.STATUS` | `FsGiFundPaGeneralPartnerParam_RecordStatus` | String |  |  |
| 20 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.CURR.NO` | `FsGiFundPaGeneralPartnerParam_CurrNo` | String |  |  |
| 21 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.INPUTTER` | `FsGiFundPaGeneralPartnerParam_Inputter` |  |  |  |
| 22 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.DATE.TIME` | `FsGiFundPaGeneralPartnerParam_DateTime` |  |  |  |
| 23 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.AUTHORISER` | `FsGiFundPaGeneralPartnerParam_Authoriser` | String |  |  |
| 24 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.CO.CODE` | `FsGiFundPaGeneralPartnerParam_CoCode` | String |  |  |
| 25 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.DEPT.CODE` | `FsGiFundPaGeneralPartnerParam_DeptCode` | String |  |  |
| 26 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.AUDITOR.CODE` | `FsGiFundPaGeneralPartnerParam_AuditorCode` | String |  |  |
| 27 | `FS.GI.FUND.PA.GENERAL.PARTNER.PARAM.AUDIT.DATE.TIME` | `FsGiFundPaGeneralPartnerParam_AuditDateTime` | String |  |  |
