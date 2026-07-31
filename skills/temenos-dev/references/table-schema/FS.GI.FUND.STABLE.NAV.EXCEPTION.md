# FS.GI.FUND.STABLE.NAV.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.STABLE.NAV.EXCEPTION` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.PARENT.REF.ID` | `FsGiFundStableNavException_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.ORA.ROWID` | `FsGiFundStableNavException_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.TA.FUND.ID` | `FsGiFundStableNavException_TaFundId` | TField |  | Fund internal Id. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.FUND.MASTER.CCY` | `FsGiFundStableNavException_FundMasterCcy` | TField |  | Fund currency (in 3 letter ISO format, eg: &apos;USD&apos;). Multifonds DB Column is CMONREF. |
| 5 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.SHARE.CLASS.CODE` | `FsGiFundStableNavException_ShareClassCode` | TField |  | Fund share class code. Multifonds DB Column is TPART. |
| 6 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.STABLE.NAV` | `FsGiFundStableNavException_StableNav` | TField |  | Stable NAV price for money market fund. Multifonds DB Column is PRICE_STABLE_NAV. |
| 7 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.FUND.ID` | `FsGiFundStableNavException_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 8 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.CLASS.CURRENCY` | `FsGiFundStableNavException_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 9 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.RESERVED10` | `FsGiFundStableNavException_Reserved10` | TField |  |  |
| 10 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.RESERVED9` | `FsGiFundStableNavException_Reserved9` | TField |  |  |
| 11 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.RESERVED8` | `FsGiFundStableNavException_Reserved8` | TField |  |  |
| 12 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.RESERVED7` | `FsGiFundStableNavException_Reserved7` | TField |  |  |
| 13 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.RESERVED6` | `FsGiFundStableNavException_Reserved6` | TField |  |  |
| 14 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.RESERVED5` | `FsGiFundStableNavException_Reserved5` | TField |  |  |
| 15 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.RESERVED4` | `FsGiFundStableNavException_Reserved4` | TField |  |  |
| 16 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.RESERVED3` | `FsGiFundStableNavException_Reserved3` | TField |  |  |
| 17 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.RESERVED2` | `FsGiFundStableNavException_Reserved2` | TField |  |  |
| 18 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.RESERVED1` | `FsGiFundStableNavException_Reserved1` | TField |  |  |
| 19 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.LOCAL.REF` | `FsGiFundStableNavException_LocalRef` |  |  |  |
| 20 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.OVERRIDE` | `FsGiFundStableNavException_Override` |  |  |  |
| 21 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.RECORD.STATUS` | `FsGiFundStableNavException_RecordStatus` | String |  |  |
| 22 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.CURR.NO` | `FsGiFundStableNavException_CurrNo` | String |  |  |
| 23 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.INPUTTER` | `FsGiFundStableNavException_Inputter` |  |  |  |
| 24 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.DATE.TIME` | `FsGiFundStableNavException_DateTime` |  |  |  |
| 25 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.AUTHORISER` | `FsGiFundStableNavException_Authoriser` | String |  |  |
| 26 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.CO.CODE` | `FsGiFundStableNavException_CoCode` | String |  |  |
| 27 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.DEPT.CODE` | `FsGiFundStableNavException_DeptCode` | String |  |  |
| 28 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.AUDITOR.CODE` | `FsGiFundStableNavException_AuditorCode` | String |  |  |
| 29 | `FS.GI.FUND.STABLE.NAV.EXCEPTION.AUDIT.DATE.TIME` | `FsGiFundStableNavException_AuditDateTime` | String |  |  |
