# FS.GI.FUND.COMMISSION.GROUP — Table Schema

> Source: `INSERTS/I_F.FS.GI.FUND.COMMISSION.GROUP` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.FUND.COMMISSION.GROUP.PARENT.REF.ID` | `FsGiFundCommissionGroup_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.FUND.COMMISSION.GROUP.ORA.ROWID` | `FsGiFundCommissionGroup_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.FUND.COMMISSION.GROUP.TA.FUND.ID` | `FsGiFundCommissionGroup_TaFundId` | TField |  | Fund internal Id. Multifonds DB Column is NPTF. |
| 4 | `FS.GI.FUND.COMMISSION.GROUP.AGENT.CODE.FOR.COMM.GROUP` | `FsGiFundCommissionGroup_AgentCodeForCommGroup` | TField |  | Type of the commission agent designated for Investors. For example 0001-Retail, 0002-Institutional etc., Multifonds DB Column is OUTLET_GRP. |
| 5 | `FS.GI.FUND.COMMISSION.GROUP.COMMISSION.GROUP` | `FsGiFundCommissionGroup_CommissionGroup` | TField |  | Linkings the fund commissiong roup in order to calcualte the commission for the fund. Multifonds DB Column is CGROUP. |
| 6 | `FS.GI.FUND.COMMISSION.GROUP.OLD.AGENT.GROUP` | `FsGiFundCommissionGroup_OldAgentGroup` | TField |  | Historical type of the commission agent designated for Investors. Multifonds DB Column is OUTLET_GRP_OLD. |
| 7 | `FS.GI.FUND.COMMISSION.GROUP.REP.NUMBER` | `FsGiFundCommissionGroup_RepNumber` | TField |  | Internal refernece number. Multifonds DB Column is REP_NR. |
| 8 | `FS.GI.FUND.COMMISSION.GROUP.FUND.ID` | `FsGiFundCommissionGroup_FundId` | TField |  | Fund Master internal Identification. Multifonds DB Column is MULTIFONDS_ID. |
| 9 | `FS.GI.FUND.COMMISSION.GROUP.CLASS.CURRENCY` | `FsGiFundCommissionGroup_ClassCurrency` | TField |  | Fund Share Class Currency. Multifonds DB Column is CLASS_CURRENCY. |
| 10 | `FS.GI.FUND.COMMISSION.GROUP.RESERVED10` | `FsGiFundCommissionGroup_Reserved10` | TField |  |  |
| 11 | `FS.GI.FUND.COMMISSION.GROUP.RESERVED9` | `FsGiFundCommissionGroup_Reserved9` | TField |  |  |
| 12 | `FS.GI.FUND.COMMISSION.GROUP.RESERVED8` | `FsGiFundCommissionGroup_Reserved8` | TField |  |  |
| 13 | `FS.GI.FUND.COMMISSION.GROUP.RESERVED7` | `FsGiFundCommissionGroup_Reserved7` | TField |  |  |
| 14 | `FS.GI.FUND.COMMISSION.GROUP.RESERVED6` | `FsGiFundCommissionGroup_Reserved6` | TField |  |  |
| 15 | `FS.GI.FUND.COMMISSION.GROUP.RESERVED5` | `FsGiFundCommissionGroup_Reserved5` | TField |  |  |
| 16 | `FS.GI.FUND.COMMISSION.GROUP.RESERVED4` | `FsGiFundCommissionGroup_Reserved4` | TField |  |  |
| 17 | `FS.GI.FUND.COMMISSION.GROUP.RESERVED3` | `FsGiFundCommissionGroup_Reserved3` | TField |  |  |
| 18 | `FS.GI.FUND.COMMISSION.GROUP.RESERVED2` | `FsGiFundCommissionGroup_Reserved2` | TField |  |  |
| 19 | `FS.GI.FUND.COMMISSION.GROUP.RESERVED1` | `FsGiFundCommissionGroup_Reserved1` | TField |  |  |
| 20 | `FS.GI.FUND.COMMISSION.GROUP.LOCAL.REF` | `FsGiFundCommissionGroup_LocalRef` |  |  |  |
| 21 | `FS.GI.FUND.COMMISSION.GROUP.OVERRIDE` | `FsGiFundCommissionGroup_Override` |  |  |  |
| 22 | `FS.GI.FUND.COMMISSION.GROUP.RECORD.STATUS` | `FsGiFundCommissionGroup_RecordStatus` | String |  |  |
| 23 | `FS.GI.FUND.COMMISSION.GROUP.CURR.NO` | `FsGiFundCommissionGroup_CurrNo` | String |  |  |
| 24 | `FS.GI.FUND.COMMISSION.GROUP.INPUTTER` | `FsGiFundCommissionGroup_Inputter` |  |  |  |
| 25 | `FS.GI.FUND.COMMISSION.GROUP.DATE.TIME` | `FsGiFundCommissionGroup_DateTime` |  |  |  |
| 26 | `FS.GI.FUND.COMMISSION.GROUP.AUTHORISER` | `FsGiFundCommissionGroup_Authoriser` | String |  |  |
| 27 | `FS.GI.FUND.COMMISSION.GROUP.CO.CODE` | `FsGiFundCommissionGroup_CoCode` | String |  |  |
| 28 | `FS.GI.FUND.COMMISSION.GROUP.DEPT.CODE` | `FsGiFundCommissionGroup_DeptCode` | String |  |  |
| 29 | `FS.GI.FUND.COMMISSION.GROUP.AUDITOR.CODE` | `FsGiFundCommissionGroup_AuditorCode` | String |  |  |
| 30 | `FS.GI.FUND.COMMISSION.GROUP.AUDIT.DATE.TIME` | `FsGiFundCommissionGroup_AuditDateTime` | String |  |  |
