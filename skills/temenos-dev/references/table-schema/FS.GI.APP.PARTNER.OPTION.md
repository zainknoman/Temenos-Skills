# FS.GI.APP.PARTNER.OPTION — Table Schema

> Source: `INSERTS/I_F.FS.GI.APP.PARTNER.OPTION` in `FS_LimitedPartnershipStaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.APP.PARTNER.OPTION.PARENT.REF.ID` | `FsGiAppPartnerOption_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.APP.PARTNER.OPTION.ORA.ROWID` | `FsGiAppPartnerOption_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.APP.PARTNER.OPTION.REGISTER.ID` | `FsGiAppPartnerOption_RegisterId` | TField |  | Register ID linked to the partnership management. Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.APP.PARTNER.OPTION.TA.FUND.ID` | `FsGiAppPartnerOption_TaFundId` | TField |  | Fund internal ID. Fund ID which was defined with management type as partnership fund. Multifonds DB Column is NPTF. |
| 5 | `FS.GI.APP.PARTNER.OPTION.SHARE.CLASS.CODE` | `FsGiAppPartnerOption_ShareClassCode` | TField |  | Fund share class linked to the partnership fund. Multifonds DB Column is TPART. |
| 6 | `FS.GI.APP.PARTNER.OPTION.INCEPTION.DATE` | `FsGiAppPartnerOption_InceptionDate` | TField |  | Inception Date of the Partnership. Multifonds DB Column is INCEPTION_DATE. |
| 7 | `FS.GI.APP.PARTNER.OPTION.CONVERSION.DATE` | `FsGiAppPartnerOption_ConversionDate` | TField |  | Migration Date of the Partnership. Multifonds DB Column is CONVERSION_DATE. |
| 8 | `FS.GI.APP.PARTNER.OPTION.HOT.ISSUE` | `FsGiAppPartnerOption_HotIssue` | TField |  | Hot issue eligibility percentage which will be used by the income allocation process. Multifonds DB Column is HOT_ISSUE. |
| 9 | `FS.GI.APP.PARTNER.OPTION.INCOME.DIST.PREF` | `FsGiAppPartnerOption_IncomeDistPref` | TField |  | Income distribution preference which will be used by the income allocation process. Multifonds DB Column is INCOME_DIST_PREF. |
| 10 | `FS.GI.APP.PARTNER.OPTION.CHANGED.FLAG` | `FsGiAppPartnerOption_ChangedFlag` | TField |  | Flag indicates the change in the partnership record. Multifonds DB Column is FLG_CHANGED. |
| 11 | `FS.GI.APP.PARTNER.OPTION.AUTO.FLAG` | `FsGiAppPartnerOption_AutoFlag` | TField |  | flag indicates the Auto insertion of partnership record at time of order creation for register in fund share class. Multifonds DB Column is FLG_AUTO. |
| 12 | `FS.GI.APP.PARTNER.OPTION.GENERAL.PARTNER.FLAG` | `FsGiAppPartnerOption_GeneralPartnerFlag` | TField |  | Flag to mention the register is a general partner Multifonds DB Column is FLG_GEN_PARTNER. |
| 13 | `FS.GI.APP.PARTNER.OPTION.FUND.ID` | `FsGiAppPartnerOption_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 14 | `FS.GI.APP.PARTNER.OPTION.CLASS.CURRENCY` | `FsGiAppPartnerOption_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 15 | `FS.GI.APP.PARTNER.OPTION.RESERVED10` | `FsGiAppPartnerOption_Reserved10` | TField |  |  |
| 16 | `FS.GI.APP.PARTNER.OPTION.RESERVED9` | `FsGiAppPartnerOption_Reserved9` | TField |  |  |
| 17 | `FS.GI.APP.PARTNER.OPTION.RESERVED8` | `FsGiAppPartnerOption_Reserved8` | TField |  |  |
| 18 | `FS.GI.APP.PARTNER.OPTION.RESERVED7` | `FsGiAppPartnerOption_Reserved7` | TField |  |  |
| 19 | `FS.GI.APP.PARTNER.OPTION.RESERVED6` | `FsGiAppPartnerOption_Reserved6` | TField |  |  |
| 20 | `FS.GI.APP.PARTNER.OPTION.RESERVED5` | `FsGiAppPartnerOption_Reserved5` | TField |  |  |
| 21 | `FS.GI.APP.PARTNER.OPTION.RESERVED4` | `FsGiAppPartnerOption_Reserved4` | TField |  |  |
| 22 | `FS.GI.APP.PARTNER.OPTION.RESERVED3` | `FsGiAppPartnerOption_Reserved3` | TField |  |  |
| 23 | `FS.GI.APP.PARTNER.OPTION.RESERVED2` | `FsGiAppPartnerOption_Reserved2` | TField |  |  |
| 24 | `FS.GI.APP.PARTNER.OPTION.RESERVED1` | `FsGiAppPartnerOption_Reserved1` | TField |  |  |
| 25 | `FS.GI.APP.PARTNER.OPTION.LOCAL.REF` | `FsGiAppPartnerOption_LocalRef` |  |  |  |
| 26 | `FS.GI.APP.PARTNER.OPTION.OVERRIDE` | `FsGiAppPartnerOption_Override` |  |  |  |
| 27 | `FS.GI.APP.PARTNER.OPTION.RECORD.STATUS` | `FsGiAppPartnerOption_RecordStatus` | String |  |  |
| 28 | `FS.GI.APP.PARTNER.OPTION.CURR.NO` | `FsGiAppPartnerOption_CurrNo` | String |  |  |
| 29 | `FS.GI.APP.PARTNER.OPTION.INPUTTER` | `FsGiAppPartnerOption_Inputter` |  |  |  |
| 30 | `FS.GI.APP.PARTNER.OPTION.DATE.TIME` | `FsGiAppPartnerOption_DateTime` |  |  |  |
| 31 | `FS.GI.APP.PARTNER.OPTION.AUTHORISER` | `FsGiAppPartnerOption_Authoriser` | String |  |  |
| 32 | `FS.GI.APP.PARTNER.OPTION.CO.CODE` | `FsGiAppPartnerOption_CoCode` | String |  |  |
| 33 | `FS.GI.APP.PARTNER.OPTION.DEPT.CODE` | `FsGiAppPartnerOption_DeptCode` | String |  |  |
| 34 | `FS.GI.APP.PARTNER.OPTION.AUDITOR.CODE` | `FsGiAppPartnerOption_AuditorCode` | String |  |  |
| 35 | `FS.GI.APP.PARTNER.OPTION.AUDIT.DATE.TIME` | `FsGiAppPartnerOption_AuditDateTime` | String |  |  |
