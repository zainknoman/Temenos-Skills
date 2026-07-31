# FS.GA.NAV.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.GROUP` in `FS_Processing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.GROUP.PARENT.REF.ID` | `FsGaNavGroup_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAV.GROUP.ORA.ROWID` | `FsGaNavGroup_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAV.GROUP.NAV.GROUP.CODE` | `FsGaNavGroup_NavGroupCode` | TField |  | The NAV group code is the list of funds grouped together for NAV processing, reporting etc Multifonds DB Column is NAV_GROUP. |
| 4 | `FS.GA.NAV.GROUP.FUND.ID` | `FsGaNavGroup_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 5 | `FS.GA.NAV.GROUP.ACCOUNTING.DATE.CONTROL.EXCEP` | `FsGaNavGroup_AccountingDateControlExcep` | TField |  | Accounting Date Control Exception. Multifonds DB Column is ACC_DT_CTRL_EXC. |
| 6 | `FS.GA.NAV.GROUP.MIG.FUND` | `FsGaNavGroup_MigFund` | TField |  | Mig. Fund Identifier Multifonds DB Column is FLG_MIG_FUND. |
| 7 | `FS.GA.NAV.GROUP.LEVEL` | `FsGaNavGroup_Level` | TField |  | Level Code Multifonds DB Column is LVL. |
| 8 | `FS.GA.NAV.GROUP.BV.NAV.PRICE.TYPE` | `FsGaNavGroup_BvNavPriceType` | TField |  | The price to be used in Back value NAV like Mid, Bid of Offer price Multifonds DB Column is BV_PRICE_TYPE. |
| 9 | `FS.GA.NAV.GROUP.VALUATION.TYPE` | `FsGaNavGroup_ValuationType` | TField |  | Type of NAV like O for Official, U for Unofficial, I for Intraday etc Multifonds DB Column is TYP_TRT. |
| 10 | `FS.GA.NAV.GROUP.DEALING.COST.GROUP.EXCEPTION` | `FsGaNavGroup_DealingCostGroupException` | TField |  | Fund can have exception on dealing cost group attach to the NAV group. Multifonds DB Column is DC_GRP_EXCEP. |
| 11 | `FS.GA.NAV.GROUP.ATTACH.DEALING.COST.GROUP` | `FsGaNavGroup_AttachDealingCostGroup` | TField |  | Dealing cost group can be attached to the fund. Multifonds DB Column is FLG_DC_CHK. |
| 12 | `FS.GA.NAV.GROUP.DC.GROUP` | `FsGaNavGroup_DcGroup` | TField |  | DC Group Multifonds DB Column is DC_GRP. |
| 13 | `FS.GA.NAV.GROUP.CGT.REGIME` | `FsGaNavGroup_CgtRegime` | TField |  | CGT Regime. Multifonds DB Column is CGT_REGIME. |
| 14 | `FS.GA.NAV.GROUP.PA.PORTFOLIO.GROUP` | `FsGaNavGroup_PaPortfolioGroup` | TField |  | If set, fund will be considered as portfolio accounting fund. Multifonds DB Column is PA_FUND_FLG. |
| 15 | `FS.GA.NAV.GROUP.RESERVED10` | `FsGaNavGroup_Reserved10` | TField |  |  |
| 16 | `FS.GA.NAV.GROUP.RESERVED9` | `FsGaNavGroup_Reserved9` | TField |  |  |
| 17 | `FS.GA.NAV.GROUP.RESERVED8` | `FsGaNavGroup_Reserved8` | TField |  |  |
| 18 | `FS.GA.NAV.GROUP.RESERVED7` | `FsGaNavGroup_Reserved7` | TField |  |  |
| 19 | `FS.GA.NAV.GROUP.RESERVED6` | `FsGaNavGroup_Reserved6` | TField |  |  |
| 20 | `FS.GA.NAV.GROUP.RESERVED5` | `FsGaNavGroup_Reserved5` | TField |  |  |
| 21 | `FS.GA.NAV.GROUP.RESERVED4` | `FsGaNavGroup_Reserved4` | TField |  |  |
| 22 | `FS.GA.NAV.GROUP.RESERVED3` | `FsGaNavGroup_Reserved3` | TField |  |  |
| 23 | `FS.GA.NAV.GROUP.RESERVED2` | `FsGaNavGroup_Reserved2` | TField |  |  |
| 24 | `FS.GA.NAV.GROUP.RESERVED1` | `FsGaNavGroup_Reserved1` | TField |  |  |
| 25 | `FS.GA.NAV.GROUP.LOCAL.REF` | `FsGaNavGroup_LocalRef` |  |  |  |
| 26 | `FS.GA.NAV.GROUP.OVERRIDE` | `FsGaNavGroup_Override` |  |  |  |
| 27 | `FS.GA.NAV.GROUP.RECORD.STATUS` | `FsGaNavGroup_RecordStatus` | String |  |  |
| 28 | `FS.GA.NAV.GROUP.CURR.NO` | `FsGaNavGroup_CurrNo` | String |  |  |
| 29 | `FS.GA.NAV.GROUP.INPUTTER` | `FsGaNavGroup_Inputter` |  |  |  |
| 30 | `FS.GA.NAV.GROUP.DATE.TIME` | `FsGaNavGroup_DateTime` |  |  |  |
| 31 | `FS.GA.NAV.GROUP.AUTHORISER` | `FsGaNavGroup_Authoriser` | String |  |  |
| 32 | `FS.GA.NAV.GROUP.CO.CODE` | `FsGaNavGroup_CoCode` | String |  |  |
| 33 | `FS.GA.NAV.GROUP.DEPT.CODE` | `FsGaNavGroup_DeptCode` | String |  |  |
| 34 | `FS.GA.NAV.GROUP.AUDITOR.CODE` | `FsGaNavGroup_AuditorCode` | String |  |  |
| 35 | `FS.GA.NAV.GROUP.AUDIT.DATE.TIME` | `FsGaNavGroup_AuditDateTime` | String |  |  |
