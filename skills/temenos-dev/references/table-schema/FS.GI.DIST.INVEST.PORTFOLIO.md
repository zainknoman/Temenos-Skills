# FS.GI.DIST.INVEST.PORTFOLIO — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.INVEST.PORTFOLIO` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.INVEST.PORTFOLIO.PARENT.REF.ID` | `FsGiDistInvestPortfolio_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.INVEST.PORTFOLIO.ORA.ROWID` | `FsGiDistInvestPortfolio_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.INVEST.PORTFOLIO.REGISTER.ID` | `FsGiDistInvestPortfolio_RegisterId` | TField |  | Register internal ID. Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.DIST.INVEST.PORTFOLIO.INVEST.PORTFOLIO.ID` | `FsGiDistInvestPortfolio_InvestPortfolioId` | TField |  | Investment portfolio ID to which register will be assigned. Multifonds DB Column is NPORTFOLIO_INVEST. |
| 5 | `FS.GI.DIST.INVEST.PORTFOLIO.RESERVED10` | `FsGiDistInvestPortfolio_Reserved10` | TField |  |  |
| 6 | `FS.GI.DIST.INVEST.PORTFOLIO.RESERVED9` | `FsGiDistInvestPortfolio_Reserved9` | TField |  |  |
| 7 | `FS.GI.DIST.INVEST.PORTFOLIO.RESERVED8` | `FsGiDistInvestPortfolio_Reserved8` | TField |  |  |
| 8 | `FS.GI.DIST.INVEST.PORTFOLIO.RESERVED7` | `FsGiDistInvestPortfolio_Reserved7` | TField |  |  |
| 9 | `FS.GI.DIST.INVEST.PORTFOLIO.RESERVED6` | `FsGiDistInvestPortfolio_Reserved6` | TField |  |  |
| 10 | `FS.GI.DIST.INVEST.PORTFOLIO.RESERVED5` | `FsGiDistInvestPortfolio_Reserved5` | TField |  |  |
| 11 | `FS.GI.DIST.INVEST.PORTFOLIO.RESERVED4` | `FsGiDistInvestPortfolio_Reserved4` | TField |  |  |
| 12 | `FS.GI.DIST.INVEST.PORTFOLIO.RESERVED3` | `FsGiDistInvestPortfolio_Reserved3` | TField |  |  |
| 13 | `FS.GI.DIST.INVEST.PORTFOLIO.RESERVED2` | `FsGiDistInvestPortfolio_Reserved2` | TField |  |  |
| 14 | `FS.GI.DIST.INVEST.PORTFOLIO.RESERVED1` | `FsGiDistInvestPortfolio_Reserved1` | TField |  |  |
| 15 | `FS.GI.DIST.INVEST.PORTFOLIO.LOCAL.REF` | `FsGiDistInvestPortfolio_LocalRef` |  |  |  |
| 16 | `FS.GI.DIST.INVEST.PORTFOLIO.OVERRIDE` | `FsGiDistInvestPortfolio_Override` |  |  |  |
| 17 | `FS.GI.DIST.INVEST.PORTFOLIO.RECORD.STATUS` | `FsGiDistInvestPortfolio_RecordStatus` | String |  |  |
| 18 | `FS.GI.DIST.INVEST.PORTFOLIO.CURR.NO` | `FsGiDistInvestPortfolio_CurrNo` | String |  |  |
| 19 | `FS.GI.DIST.INVEST.PORTFOLIO.INPUTTER` | `FsGiDistInvestPortfolio_Inputter` |  |  |  |
| 20 | `FS.GI.DIST.INVEST.PORTFOLIO.DATE.TIME` | `FsGiDistInvestPortfolio_DateTime` |  |  |  |
| 21 | `FS.GI.DIST.INVEST.PORTFOLIO.AUTHORISER` | `FsGiDistInvestPortfolio_Authoriser` | String |  |  |
| 22 | `FS.GI.DIST.INVEST.PORTFOLIO.CO.CODE` | `FsGiDistInvestPortfolio_CoCode` | String |  |  |
| 23 | `FS.GI.DIST.INVEST.PORTFOLIO.DEPT.CODE` | `FsGiDistInvestPortfolio_DeptCode` | String |  |  |
| 24 | `FS.GI.DIST.INVEST.PORTFOLIO.AUDITOR.CODE` | `FsGiDistInvestPortfolio_AuditorCode` | String |  |  |
| 25 | `FS.GI.DIST.INVEST.PORTFOLIO.AUDIT.DATE.TIME` | `FsGiDistInvestPortfolio_AuditDateTime` | String |  |  |
