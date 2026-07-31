# CP.CAMPAIGN.STATUS — Table Schema

> Source: `INSERTS/I_F.CP.CAMPAIGN.STATUS` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.CPG.STS.DESCRIPTION` | `CpCampaignStatus_Description` |  |  |  |
| 2 | `CP.CPG.STS.FLOW.VALIDATION` | `CpCampaignStatus_FlowValidation` | TField |  | This field stores the direction of the flow when a campaigns is moved in the given status. The values in the list of values available to choose from are: START, NEXT, BACK, END. |
| 3 | `CP.CPG.STS.TYPE` | `CpCampaignStatus_Type` | TField |  | This field stores the type of the campaign status. The values in the list of values available to choose from are: RUNNING, TESTING, NORMAL. |
| 4 | `CP.CPG.STS.BUTTON.LABEL` | `CpCampaignStatus_ButtonLabel` | TField |  | This field stores the label of the button that has to be clicked by the business Marketing role in order to move the campaign to the given status. |
| 5 | `CP.CPG.STS.SEARCH.TITLE` | `CpCampaignStatus_SearchTitle` | TField |  | This field stores the Campaign Management User Agent Interface Dashboard tab labels. |
| 6 | `CP.CPG.STS.NEXT.STATUS` | `CpCampaignStatus_NextStatus` | TField |  | This field stores the next (forward) status, on the approval flow, a campaign can be moved to by the Marketing role. The Admin user picks this value from a dropdown list containing the available campaign statuses defined in the new CP.CAMPAIGN.STATUS table. |
| 7 | `CP.CPG.STS.BACK.STATUS` | `CpCampaignStatus_BackStatus` | TField |  | This field stores the back (backward) status, on the approval flow, a campaign can be moved to by the Marketing role. The Admin user picks this value from a dropdown list containing the available campaign statuses defined in the new CP.CAMPAIGN.STATUS table. |
| 8 | `CP.CPG.STS.AUTO.VERSION.STATUS` | `CpCampaignStatus_AutoVersionStatus` |  |  |  |
| 9 | `CP.CPG.STS.USER.ROLE` | `CpCampaignStatus_UserRole` | TField |  | This field stores the business Marketing role which can see and interact with the campaign in a given status. The Admin user picks this value from a dropdown list containing the available user roles defined in the USER.SMS.GROUP table. |
| 10 | `CP.CPG.STS.APP.EDITABLE` | `CpCampaignStatus_AppEditable` | TField |  | Y/N values. The values indicate whether or not the campaign is editable in the given status. |
| 11 | `CP.CPG.STS.NO.OF.AUTHORISATIONS` | `CpCampaignStatus_NoOfAuthorisations` |  |  |  |
| 12 | `CP.CPG.STS.RESERVED.10` | `CpCampaignStatus_Reserved10` | TField |  |  |
| 13 | `CP.CPG.STS.RESERVED.9` | `CpCampaignStatus_Reserved9` | TField |  |  |
| 14 | `CP.CPG.STS.RESERVED.8` | `CpCampaignStatus_Reserved8` | TField |  |  |
| 15 | `CP.CPG.STS.RESERVED.7` | `CpCampaignStatus_Reserved7` | TField |  |  |
| 16 | `CP.CPG.STS.RESERVED.6` | `CpCampaignStatus_Reserved6` | TField |  |  |
| 17 | `CP.CPG.STS.RESERVED.5` | `CpCampaignStatus_Reserved5` | TField |  |  |
| 18 | `CP.CPG.STS.RESERVED.4` | `CpCampaignStatus_Reserved4` | TField |  |  |
| 19 | `CP.CPG.STS.RESERVED.3` | `CpCampaignStatus_Reserved3` | TField |  |  |
| 20 | `CP.CPG.STS.RESERVED.2` | `CpCampaignStatus_Reserved2` | TField |  |  |
| 21 | `CP.CPG.STS.RESERVED.1` | `CpCampaignStatus_Reserved1` | TField |  |  |
| 22 | `CP.CPG.STS.LOCAL.REF` | `CpCampaignStatus_LocalRef` |  |  |  |
| 23 | `CP.CPG.STS.OVERRIDE` | `CpCampaignStatus_Override` |  |  |  |
| 24 | `CP.CPG.STS.RECORD.STATUS` | `CpCampaignStatus_RecordStatus` | String |  |  |
| 25 | `CP.CPG.STS.CURR.NO` | `CpCampaignStatus_CurrNo` | String |  |  |
| 26 | `CP.CPG.STS.INPUTTER` | `CpCampaignStatus_Inputter` |  |  |  |
| 27 | `CP.CPG.STS.DATE.TIME` | `CpCampaignStatus_DateTime` |  |  |  |
| 28 | `CP.CPG.STS.AUTHORISER` | `CpCampaignStatus_Authoriser` | String |  |  |
| 29 | `CP.CPG.STS.CO.CODE` | `CpCampaignStatus_CoCode` | String |  |  |
| 30 | `CP.CPG.STS.DEPT.CODE` | `CpCampaignStatus_DeptCode` | String |  |  |
| 31 | `CP.CPG.STS.AUDITOR.CODE` | `CpCampaignStatus_AuditorCode` | String |  |  |
| 32 | `CP.CPG.STS.AUDIT.DATE.TIME` | `CpCampaignStatus_AuditDateTime` | String |  |  |
