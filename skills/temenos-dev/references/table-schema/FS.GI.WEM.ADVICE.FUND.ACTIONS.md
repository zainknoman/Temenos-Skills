# FS.GI.WEM.ADVICE.FUND.ACTIONS — Table Schema

> Source: `INSERTS/I_F.FS.GI.WEM.ADVICE.FUND.ACTIONS` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ADVICE.FUND.ACTIONS.FUND.GROUP` | `FsGiWemAdviceFundActions_FundGroup` | TField |  |  |
| 2 | `ADVICE.FUND.ACTIONS.TRADE.DATE` | `FsGiWemAdviceFundActions_TradeDate` | TField |  |  |
| 3 | `ADVICE.FUND.ACTIONS.ACCOUNTING.DATE` | `FsGiWemAdviceFundActions_AccountingDate` | TField |  |  |
| 4 | `ADVICE.FUND.ACTIONS.FUND` | `FsGiWemAdviceFundActions_Fund` | TField |  |  |
| 5 | `ADVICE.FUND.ACTIONS.ACTION` | `FsGiWemAdviceFundActions_Action` | TField |  |  |
| 6 | `ADVICE.FUND.ACTIONS.RESERVED5` | `FsGiWemAdviceFundActions_Reserved5` | TField |  |  |
| 7 | `ADVICE.FUND.ACTIONS.RESERVED4` | `FsGiWemAdviceFundActions_Reserved4` | TField |  |  |
| 8 | `ADVICE.FUND.ACTIONS.RESERVED3` | `FsGiWemAdviceFundActions_Reserved3` | TField |  |  |
| 9 | `ADVICE.FUND.ACTIONS.RESERVED2` | `FsGiWemAdviceFundActions_Reserved2` | TField |  |  |
| 10 | `ADVICE.FUND.ACTIONS.RESERVED1` | `FsGiWemAdviceFundActions_Reserved1` | TField |  |  |
| 11 | `ADVICE.FUND.ACTIONS.LOCAL.REF` | `FsGiWemAdviceFundActions_LocalRef` |  |  |  |
| 12 | `ADVICE.FUND.ACTIONS.OVERRIDE` | `FsGiWemAdviceFundActions_Override` |  |  |  |
| 13 | `ADVICE.FUND.ACTIONS.RECORD.STATUS` | `FsGiWemAdviceFundActions_RecordStatus` | String |  |  |
| 14 | `ADVICE.FUND.ACTIONS.CURR.NO` | `FsGiWemAdviceFundActions_CurrNo` | String |  |  |
| 15 | `ADVICE.FUND.ACTIONS.INPUTTER` | `FsGiWemAdviceFundActions_Inputter` |  |  |  |
| 16 | `ADVICE.FUND.ACTIONS.DATE.TIME` | `FsGiWemAdviceFundActions_DateTime` |  |  |  |
| 17 | `ADVICE.FUND.ACTIONS.AUTHORISER` | `FsGiWemAdviceFundActions_Authoriser` | String |  |  |
| 18 | `ADVICE.FUND.ACTIONS.CO.CODE` | `FsGiWemAdviceFundActions_CoCode` | String |  |  |
| 19 | `ADVICE.FUND.ACTIONS.DEPT.CODE` | `FsGiWemAdviceFundActions_DeptCode` | String |  |  |
| 20 | `ADVICE.FUND.ACTIONS.AUDITOR.CODE` | `FsGiWemAdviceFundActions_AuditorCode` | String |  |  |
| 21 | `ADVICE.FUND.ACTIONS.AUDIT.DATE.TIME` | `FsGiWemAdviceFundActions_AuditDateTime` | String |  |  |
