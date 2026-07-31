# AM.PF.FEES.POST.REQUEST — Table Schema

> Source: `INSERTS/I_F.AM.PF.FEES.POST.REQUEST` in `AM_PerformanceFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.PFP.PORTFOLIO.NO` | `AmPfFeesPostRequest_PortfolioNo` |  |  |  |
| 2 | `AM.PFP.ACCOUNT.OFFICER` | `AmPfFeesPostRequest_AccountOfficer` | TField |  | Valid DEPT.ACCT.OFFICER. All portfolios belonging to this account officer would be selected to post performance fees online. |
| 3 | `AM.PFP.ALL.PORTFOLIO` | `AmPfFeesPostRequest_AllPortfolio` | TField |  | Contains the value as Yes or No. Validation Rules If it is Yes, then all the portfolios are selected to post the performance fees online. |
| 4 | `AM.PFP.VALUE.DATE` | `AmPfFeesPostRequest_ValueDate` | TField |  | Specifies the VALUE.DATE of accounting entries. |
| 5 | `AM.PFP.STATUS` | `AmPfFeesPostRequest_Status` | TField |  | Defines the status: Awaiting or Running or Processed. When the record is authorised then the status will be moved to Awaiting. While running, the service before posting the status will be moved to Running. After posting the fees, the status will be moved to Processed. The record is amended only during Awaiting status. |
| 6 | `AM.PFP.RESERVED.5` | `AmPfFeesPostRequest_Reserved5` | TField |  |  |
| 7 | `AM.PFP.RESERVED.4` | `AmPfFeesPostRequest_Reserved4` | TField |  |  |
| 8 | `AM.PFP.RESERVED.3` | `AmPfFeesPostRequest_Reserved3` | TField |  |  |
| 9 | `AM.PFP.RESERVED.2` | `AmPfFeesPostRequest_Reserved2` | TField |  |  |
| 10 | `AM.PFP.RESERVED.1` | `AmPfFeesPostRequest_Reserved1` | TField |  |  |
| 11 | `AM.PFP.RECORD.STATUS` | `AmPfFeesPostRequest_RecordStatus` | String |  |  |
| 12 | `AM.PFP.CURR.NO` | `AmPfFeesPostRequest_CurrNo` | String |  |  |
| 13 | `AM.PFP.INPUTTER` | `AmPfFeesPostRequest_Inputter` |  |  |  |
| 14 | `AM.PFP.DATE.TIME` | `AmPfFeesPostRequest_DateTime` |  |  |  |
| 15 | `AM.PFP.AUTHORISER` | `AmPfFeesPostRequest_Authoriser` | String |  |  |
| 16 | `AM.PFP.CO.CODE` | `AmPfFeesPostRequest_CoCode` | String |  |  |
| 17 | `AM.PFP.DEPT.CODE` | `AmPfFeesPostRequest_DeptCode` | String |  |  |
| 18 | `AM.PFP.AUDITOR.CODE` | `AmPfFeesPostRequest_AuditorCode` | String |  |  |
| 19 | `AM.PFP.AUDIT.DATE.TIME` | `AmPfFeesPostRequest_AuditDateTime` | String |  |  |
