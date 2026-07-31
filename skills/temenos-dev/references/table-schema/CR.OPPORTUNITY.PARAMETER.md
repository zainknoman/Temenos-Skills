# CR.OPPORTUNITY.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CR.OPPORTUNITY.PARAMETER` in `CR_Operational.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CR.OP.PARAM.PROP.OVERWRITE` | `CrOpportunityParameter_PropOverwrite` |  |  |  |
| 2 | `CR.OP.PARAM.PROP.PRIOR.OP.STATUS` | `CrOpportunityParameter_PropPriorOpStatus` |  |  |  |
| 3 | `CR.OP.PARAM.PROP.ACTION` | `CrOpportunityParameter_PropAction` |  |  |  |
| 4 | `CR.OP.PARAM.CAMP.OVERWRITE` | `CrOpportunityParameter_CampOverwrite` |  |  |  |
| 5 | `CR.OP.PARAM.CAMP.PRIOR.OP.STATUS` | `CrOpportunityParameter_CampPriorOpStatus` |  |  |  |
| 6 | `CR.OP.PARAM.CAMP.ACTION` | `CrOpportunityParameter_CampAction` |  |  |  |
| 7 | `CR.OP.PARAM.REJECTED.PERIOD` | `CrOpportunityParameter_RejectedPeriod` | TField |  | For this source of opportunity, period during which the customer should not have a new opportunity raised, even if they have a propensity or are a suitable candidate for a campaign, if a previous opportunity for the same product has already been declined . Validation Rules :Standard Duration values : a numeric, 1-99, followed by :C = Calendar DaysD = Working DaysW = WeeksM = Months |
| 8 | `CR.OP.PARAM.PERIOD` | `CrOpportunityParameter_Period` |  |  |  |
| 9 | `CR.OP.PARAM.MAX.OB.OPPOR` | `CrOpportunityParameter_MaxObOppor` |  |  |  |
| 10 | `CR.OP.PARAM.OPPOR.STATUS` | `CrOpportunityParameter_OpporStatus` |  |  |  |
| 11 | `CR.OP.PARAM.DAYS.PAST.EXPIRY` | `CrOpportunityParameter_DaysPastExpiry` |  |  |  |
| 12 | `CR.OP.PARAM.APPLICATION` | `CrOpportunityParameter_Application` |  |  |  |
| 13 | `CR.OP.PARAM.VERSION` | `CrOpportunityParameter_Version` |  |  |  |
| 14 | `CR.OP.PARAM.CUSTOMER.FIELD` | `CrOpportunityParameter_CustomerField` |  |  |  |
| 15 | `CR.OP.PARAM.ACCOUNT.FIELD` | `CrOpportunityParameter_AccountField` |  |  |  |
| 16 | `CR.OP.PARAM.OPPOR.ID` | `CrOpportunityParameter_OpporId` |  |  |  |
| 17 | `CR.OP.PARAM.RESERVED.4` | `CrOpportunityParameter_Reserved4` |  |  |  |
| 18 | `CR.OP.PARAM.RESERVED.3` | `CrOpportunityParameter_Reserved3` |  |  |  |
| 19 | `CR.OP.PARAM.RT.OPP.COS` | `CrOpportunityParameter_RtOppCos` | TField | Yes | Name of Composite screen to be displayed when the real-time opportunities are generated. Validation Rules Mandatory for Real Time |
| 20 | `CR.OP.PARAM.BLOCK.CR.ITEMS` | `CrOpportunityParameter_BlockCrItems` |  |  |  |
| 21 | `CR.OP.PARAM.UNBLOCK.CR.ITEM` | `CrOpportunityParameter_UnblockCrItem` |  |  |  |
| 22 | `CR.OP.PARAM.LOCAL.REF` | `CrOpportunityParameter_LocalRef` |  |  |  |
| 23 | `CR.OP.PARAM.RECORD.STATUS` | `CrOpportunityParameter_RecordStatus` | String |  |  |
| 24 | `CR.OP.PARAM.CURR.NO` | `CrOpportunityParameter_CurrNo` | String |  |  |
| 25 | `CR.OP.PARAM.INPUTTER` | `CrOpportunityParameter_Inputter` |  |  |  |
| 26 | `CR.OP.PARAM.DATE.TIME` | `CrOpportunityParameter_DateTime` |  |  |  |
| 27 | `CR.OP.PARAM.AUTHORISER` | `CrOpportunityParameter_Authoriser` | String |  |  |
| 28 | `CR.OP.PARAM.CO.CODE` | `CrOpportunityParameter_CoCode` | String |  |  |
| 29 | `CR.OP.PARAM.DEPT.CODE` | `CrOpportunityParameter_DeptCode` | String |  |  |
| 30 | `CR.OP.PARAM.AUDITOR.CODE` | `CrOpportunityParameter_AuditorCode` | String |  |  |
| 31 | `CR.OP.PARAM.AUDIT.DATE.TIME` | `CrOpportunityParameter_AuditDateTime` | String |  |  |
