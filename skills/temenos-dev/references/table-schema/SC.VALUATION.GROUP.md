# SC.VALUATION.GROUP — Table Schema

> Source: `INSERTS/I_F.SC.VALUATION.GROUP` in `SC_ScvValuationUpdates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SVG.CHILD.PORTFOLIO` | `ScValuationGroup_ChildPortfolio` |  |  |  |
| 2 | `SC.SVG.LINK.TYPE` | `ScValuationGroup_LinkType` |  |  |  |
| 3 | `SC.SVG.PLEDGE.PCT` | `ScValuationGroup_PledgePct` |  |  |  |
| 4 | `SC.SVG.PLEDGE.AMT` | `ScValuationGroup_PledgeAmt` |  |  |  |
| 5 | `SC.SVG.GLOBAL.LIMIT` | `ScValuationGroup_GlobalLimit` | TField |  | To specify the global limit (i.e. In format 10000.xxx). Enquiry for limit utilization will pick the right limit reference by prefixing customer of portfolio based on the query run (group, individual portfolio, etc.) |
| 6 | `SC.SVG.STATUS` | `ScValuationGroup_Status` | TField |  | To denote whether valuation has to be performed. In case of valuation has to be stopped for master portfolio, STATUS field has to be set as INACTIVE. This field will be automatically updated if master portfolio is set as closure in SEC.ACC.MASTER. |
| 7 | `SC.SVG.RUN.VALUATION` | `ScValuationGroup_RunValuation` | TField |  | Field to request for online valuation of master portfolio. Must be set as YES. Cannot be set as YES if STATUS field is INACTIVE. |
| 8 | `SC.SVG.CHILD.VALUATION` | `ScValuationGroup_ChildValuation` |  |  |  |
| 9 | `SC.SVG.LAST.VALUATION.RUN` | `ScValuationGroup_LastValuationRun` | TField |  | Date and time of online valuation run on request of online valuation. No input field |
| 10 | `SC.SVG.MASTER.PORTFOLIO` | `ScValuationGroup_MasterPortfolio` |  |  |  |
| 11 | `SC.SVG.RESERVED.9` | `ScValuationGroup_Reserved9` | TField |  |  |
| 12 | `SC.SVG.RESERVED.8` | `ScValuationGroup_Reserved8` | TField |  |  |
| 13 | `SC.SVG.RESERVED.7` | `ScValuationGroup_Reserved7` | TField |  |  |
| 14 | `SC.SVG.RESERVED.6` | `ScValuationGroup_Reserved6` | TField |  |  |
| 15 | `SC.SVG.RESERVED.5` | `ScValuationGroup_Reserved5` | TField |  |  |
| 16 | `SC.SVG.RESERVED.4` | `ScValuationGroup_Reserved4` | TField |  |  |
| 17 | `SC.SVG.RESERVED.3` | `ScValuationGroup_Reserved3` | TField |  |  |
| 18 | `SC.SVG.RESERVED.2` | `ScValuationGroup_Reserved2` | TField |  |  |
| 19 | `SC.SVG.RESERVED.1` | `ScValuationGroup_Reserved1` | TField |  |  |
| 20 | `SC.SVG.LOCAL.REF` | `ScValuationGroup_LocalRef` |  |  |  |
| 21 | `SC.SVG.RECORD.STATUS` | `ScValuationGroup_RecordStatus` | String |  |  |
| 22 | `SC.SVG.CURR.NO` | `ScValuationGroup_CurrNo` | String |  |  |
| 23 | `SC.SVG.INPUTTER` | `ScValuationGroup_Inputter` |  |  |  |
| 24 | `SC.SVG.DATE.TIME` | `ScValuationGroup_DateTime` |  |  |  |
| 25 | `SC.SVG.AUTHORISER` | `ScValuationGroup_Authoriser` | String |  |  |
| 26 | `SC.SVG.CO.CODE` | `ScValuationGroup_CoCode` | String |  |  |
| 27 | `SC.SVG.DEPT.CODE` | `ScValuationGroup_DeptCode` | String |  |  |
| 28 | `SC.SVG.AUDITOR.CODE` | `ScValuationGroup_AuditorCode` | String |  |  |
| 29 | `SC.SVG.AUDIT.DATE.TIME` | `ScValuationGroup_AuditDateTime` | String |  |  |
