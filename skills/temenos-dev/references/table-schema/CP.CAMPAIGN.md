# CP.CAMPAIGN — Table Schema

> Source: `INSERTS/I_F.CP.CAMPAIGN` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.CPG.DESCRIPTION` | `CpCampaign_Description` |  |  |  |
| 2 | `CP.CPG.NAME` | `CpCampaign_Name` | TField | Yes | Name of the Campaign. This is Mandatory text field. It allows up to 50 any characters. |
| 3 | `CP.CPG.OBJECTIVE` | `CpCampaign_Objective` | TField |  | Objective of the Campaign. Links to the ID of CP.OBJECTIVE table. |
| 4 | `CP.CPG.TARGET.COSTS` | `CpCampaign_TargetCosts` | TField |  | Planned cost for the Campaign. This is an amount/numeric field. |
| 5 | `CP.CPG.ACTUAL.COSTS` | `CpCampaign_ActualCosts` | TField |  | Actual cost for the Campaign. This is an amount/numeric field. |
| 6 | `CP.CPG.PLANNED.START.DATE` | `CpCampaign_PlannedStartDate` | TField |  | Planned start date for the new Campaign. This is a date type field. |
| 7 | `CP.CPG.ACTUAL.START.DATE` | `CpCampaign_ActualStartDate` | TField |  | Actual start date for the new Campaign. This is a date type field. |
| 8 | `CP.CPG.PLANNED.END.DATE` | `CpCampaign_PlannedEndDate` | TField |  | Planned end date for the new Campaign. This is a date type field. |
| 9 | `CP.CPG.ACTUAL.END.DATE` | `CpCampaign_ActualEndDate` | TField |  | Actual end date for the new Campaign. This is a date type field. |
| 10 | `CP.CPG.TARGET.RSP.RATES` | `CpCampaign_TargetRspRates` | TField |  | Planned response rate to the Campaign. This is an amount/numeric field, and the value inserted here should be a percent. |
| 11 | `CP.CPG.ACTUAL.RSP.RATES` | `CpCampaign_ActualRspRates` | TField |  | Actual response rate to the Campaign. This is an amount/numeric field, and the value inserted here should be a percent. |
| 12 | `CP.CPG.TARGET.ROI` | `CpCampaign_TargetRoi` | TField |  | Planned return on investment rate for the Campaign. This is an amount/numeric field. |
| 13 | `CP.CPG.ACTUAL.ROI` | `CpCampaign_ActualRoi` | TField |  | Actual return on investment rate for the Campaign. This is an amount/numeric field. |
| 14 | `CP.CPG.PRODUCT` | `CpCampaign_Product` |  |  |  |
| 15 | `CP.CPG.PRODUCT.GROUP` | `CpCampaign_ProductGroup` |  |  |  |
| 16 | `CP.CPG.OWNER` | `CpCampaign_Owner` | TField | Yes | The user who defines the Campaign. Links to the ID of USER table and it is Mandatory. |
| 17 | `CP.CPG.CAMPAIGN.STATUS` | `CpCampaign_CampaignStatus` | TField | Yes | The status of the Campaign. Links to the ID of CP.CAMPAIGN.STATUS table and it is Mandatory. |
| 18 | `CP.CPG.WORKFLOW.ID` | `CpCampaign_WorkflowId` | TField |  | The ID of the workflow which indicates the state of the Campaign. |
| 19 | `CP.CPG.PROGRAM.ID` | `CpCampaign_ProgramId` | TField |  | The ID of the program which contains the Campaign. Links to the ID of CP.PROGRAM table. |
| 20 | `CP.CPG.CHANNEL` | `CpCampaign_Channel` |  |  |  |
| 21 | `CP.CPG.OFFLINE.TEMPLATE` | `CpCampaign_OfflineTemplate` |  |  |  |
| 22 | `CP.CPG.CONTENT.TITLE` | `CpCampaign_ContentTitle` |  |  |  |
| 23 | `CP.CPG.CHOSEN.CONTENT` | `CpCampaign_ChosenContent` |  |  |  |
| 24 | `CP.CPG.USE.RESOURCE` | `CpCampaign_UseResource` |  |  |  |
| 25 | `CP.CPG.RESOURCE` | `CpCampaign_Resource` |  |  |  |
| 26 | `CP.CPG.CONTENT.EXTRA` | `CpCampaign_ContentExtra` |  |  |  |
| 27 | `CP.CPG.CONTENT.LOCATION` | `CpCampaign_ContentLocation` |  |  |  |
| 28 | `CP.CPG.ON.CLICK.URL` | `CpCampaign_OnClickUrl` |  |  |  |
| 29 | `CP.CPG.PROFILE` | `CpCampaign_Profile` |  |  |  |
| 30 | `CP.CPG.RATIO.HANDLER` | `CpCampaign_RatioHandler` |  |  |  |
| 31 | `CP.CPG.REQUIRED.DATA.CONTEXT` | `CpCampaign_RequiredDataContext` |  |  |  |
| 32 | `CP.CPG.BANK.TRIGGERS` | `CpCampaign_BankTriggers` |  |  |  |
| 33 | `CP.CPG.ONLINE.CHANNEL` | `CpCampaign_OnlineChannel` |  |  |  |
| 34 | `CP.CPG.CHANNEL.NAME` | `CpCampaign_ChannelName` |  |  |  |
| 35 | `CP.CPG.FRONTEND.TRIGGERS` | `CpCampaign_FrontendTriggers` |  |  |  |
| 36 | `CP.CPG.PRIORITY` | `CpCampaign_Priority` | TField |  | The priority of the campaign which is used to orchestrated the execution of the campaigns. This is an amount/numeric field. |
| 37 | `CP.CPG.NUMBER.IMPRESSIONS` | `CpCampaign_NumberImpressions` | TField |  | The number of times a customer is targeted by a campaign. This is a numeric field. |
| 38 | `CP.CPG.METRICS.PROVIDER` | `CpCampaign_MetricsProvider` |  |  |  |
| 39 | `CP.CPG.METRICS.TYPE` | `CpCampaign_MetricsType` |  |  |  |
| 40 | `CP.CPG.BUDGET.TYPE` | `CpCampaign_BudgetType` |  |  |  |
| 41 | `CP.CPG.BUDGET.PLANNED` | `CpCampaign_BudgetPlanned` |  |  |  |
| 42 | `CP.CPG.BUDGET.RESULT` | `CpCampaign_BudgetResult` |  |  |  |
| 43 | `CP.CPG.BUDGET.CALCULATION` | `CpCampaign_BudgetCalculation` |  |  |  |
| 44 | `CP.CPG.USE.TEMPLATES` | `CpCampaign_UseTemplates` | TField |  | Should contain Y/N values to indicate if the Marketing Inputter would like to use an already saved template for a communication. |
| 45 | `CP.CPG.CHANNEL.DATA` | `CpCampaign_ChannelData` |  |  |  |
| 46 | `CP.CPG.RULE.EVAL.TYPE` | `CpCampaign_RuleEvalType` | TField |  | Rule evaluation type. This is a text field and it allows up to 30 any characters. |
| 47 | `CP.CPG.USE.VARIANTS` | `CpCampaign_UseVariants` | TField |  | Should contain Y/N values to indicate if the user would like to define variants (tests) for the defined campaign. |
| 48 | `CP.CPG.VARIANT.SELECTION` | `CpCampaign_VariantSelection` | TField |  | The ID of the Variant selection which is a means of splitting the targeted audience identified via a profile. This field links the CP.CAMPAIGN table to CP.VARIANT.SELECTION one. |
| 49 | `CP.CPG.VARIANT` | `CpCampaign_Variant` |  |  |  |
| 50 | `CP.CPG.ORIGINAL.ID` | `CpCampaign_OriginalId` | TField |  | If a campaign has been versioned this field stores the ID of the Original campaign. |
| 51 | `CP.CPG.EDITABLE` | `CpCampaign_Editable` | TField |  | A flag which indicates that the campaign can be versioned - Y/N values. |
| 52 | `CP.CPG.VERSION` | `CpCampaign_Version` | TField |  | If a campaign is edited by a Marketing Inputter and it is in status Testing or Running, the solution will create a version of that campaign. This numeric field will store the number of that version. |
| 53 | `CP.CPG.TEST.START.DATE` | `CpCampaign_TestStartDate` | TField |  | This is an editable date type field where the Marketing Inputter will be able to define the start date for the Test. |
| 54 | `CP.CPG.TEST.END.DATE` | `CpCampaign_TestEndDate` | TField |  | This is an editable date type field where the Marketing Inputter will be able to define the end date for the Test. |
| 55 | `CP.CPG.TEST.SAMPLE` | `CpCampaign_TestSample` | TField |  | These are random group of customers who are eligible for a specific campaign. The campaign is launched only for these customers for test purposes. When the campaign is executed for the full set of targeted audience, the test cell will not be included again. This is an amount/numeric field. |
| 56 | `CP.CPG.TEST.COST.K.CUST` | `CpCampaign_TestCostKCust` | TField |  | This is an editable field where the Marketing Inputter will be able to fill in the cost for the campaign per 1000 customers. This is an amount/numeric field. |
| 57 | `CP.CPG.TEST.TRG.AUD.SIZE` | `CpCampaign_TestTrgAudSize` | TField |  | This will be a calculated field by the Insight. Test cell size=Test cell*total targeted audience for the campaign. These customers are linked to the campaign tested on them. Test cell customers must not be included in the Hold out cell for that campaign. This is an amount/numeric field. |
| 58 | `CP.CPG.TEST.TOTAL.COST` | `CpCampaign_TestTotalCost` | TField |  | The Insight will calculate the total cost of the tested campaign. Total Cost for test = test cell size*cost per 1000cust /1000. This is an amount/numeric field. |
| 59 | `CP.CPG.NO.CUST.BREAK.EVNT` | `CpCampaign_NoCustBreakEvnt` | TField |  | The solution will calculate the number of customers the bank needs to respond to the campaign, so that it reaches break even. It represents the number of customers that have to buy the campaigned product so that the campaign costs are covered. BE=Total cost of the test/cost per customer. This is an amount/numeric field. |
| 60 | `CP.CPG.TEST.TRG.RSP.RATE` | `CpCampaign_TestTrgRspRate` | TField |  | This is an editable field where the Marketing Inputter will fill in the targeted response rate for the test. This is an amount/numeric field. |
| 61 | `CP.CPG.ACTUAL.NO.TEST.RSP` | `CpCampaign_ActualNoTestRsp` | TField |  | The solution will capture and analyse the customers' responses. Example for an Internet Banking Campaign: The are 4 possibilities: 1. The customer will ignore the Campaign message. 2. The customer will click on the banner and take no action further. 3. The customer will click on the banner but will abandon. 4. The customer will click on the banner and will apply for the overdraft facility. � The solution will fill in this field based on the customers responses to the test. If Campaign Test state is any other than Finish, this field will not be shown. This is an amount/numeric field. |
| 62 | `CP.CPG.TEST.ACTUAL.RSP.RATE` | `CpCampaign_TestActualRspRate` | TField |  | Insight will calculate the Actual response rate. Actual Response rate = actual no. test respondents/ test cell size. This is an amount/numeric field. |
| 63 | `CP.CPG.TEST.TOT.GROSMARGIN` | `CpCampaign_TestTotGrosmargin` | TField |  | Insight will calculate the total gross margin by multiplying the number of actual responders/sales by the gross margin per sale. Total gross margin = actual number of respondents*gross margin per sale. This is an amount/numeric field. |
| 64 | `CP.CPG.TEST.NET.PROFMARGIN` | `CpCampaign_TestNetProfmargin` | TField |  | Insight will calculate the net profit margin by subtracting the test costs from the total gross margin. Total gross margin = actual number of respondents*gross margin per sale. This is an amount/numeric field. |
| 65 | `CP.CPG.TEST.ROI` | `CpCampaign_TestRoi` | TField |  | Insight will calculate the ROI by dividing the net profit margin by the total cost of the test. ROI=Net profit margin/Total cost for test. This is an amount/numeric field. |
| 66 | `CP.CPG.GROSMARGIN.PER.SALE` | `CpCampaign_GrosmarginPerSale` | TField |  | Gross margin per sale. This is an amount/numeric field. |
| 67 | `CP.CPG.PLANNED.COST.CUST` | `CpCampaign_PlannedCostCust` | TField |  | Planned cost per customer. This is an amount/numeric field. |
| 68 | `CP.CPG.ACTUAL.COST.CUST` | `CpCampaign_ActualCostCust` | TField |  | Actual cost per customer. This is an amount/numeric field. |
| 69 | `CP.CPG.VERSION.FLAG` | `CpCampaign_VersionFlag` | TField |  | This is a field which receives a set of values from edgeConnect based on which the solution decides if the campaign needs to be versioned. |
| 70 | `CP.CPG.CONTENT.TYPE` | `CpCampaign_ContentType` | TField |  | This filed stores the type of the content used for the definition of the reusable resource. |
| 71 | `CP.CPG.CONTENT.TYPE.DATA` | `CpCampaign_ContentTypeData` |  |  |  |
| 72 | `CP.CPG.LAST.UPDATE` | `CpCampaign_LastUpdate` | TField |  | This field stores the date of the last comment made for this record. |
| 73 | `CP.CPG.SUSPEND.REASON.ID` | `CpCampaign_SuspendReasonId` | TField |  | This field stores the SUSPEND.REASON record ID. If this field has a SuspendReasonId -> the record has suspended values on it. It can't be used until they are approved or removed from the record.While there is a value in SuspendReasonId, the campaign can't be moved in a next stage |
| 74 | `CP.CPG.TESTING.TYPE` | `CpCampaign_TestingType` | TField |  | This field stores the Testing type selected for the campaign (AB Testing, Count or left blank for no testing) |
| 75 | `CP.CPG.SEL.VARIANT.OUTPUT` | `CpCampaign_SelVariantOutput` | TField |  | This field is used to flag the winner for the AB testing. Yes - the campaign will run with the channel output from the attached variant; No - the campaign will run with the channel output from the campaign. |
| 76 | `CP.CPG.NEW.VERSION` | `CpCampaign_NewVersion` | TField |  | Specifies if the campaign testing has started (YES value, if true). |
| 77 | `CP.CPG.HOLD.OUT.CELL` | `CpCampaign_HoldOutCell` | TField |  | Percentage of Customers from the target audience who will not receive the campaign communication because their activity will be tracked independently of the campaign. |
| 78 | `CP.CPG.NO.EXCLUDED.CUSTOMERS` | `CpCampaign_NoExcludedCustomers` | TField |  | Number of Customers from the target audience who will not receive the campaign communication because their activity will be tracked independently of the campaign. |
| 79 | `CP.CPG.NO.CONTROL.CUSTOMERS` | `CpCampaign_NoControlCustomers` | TField |  | Specifies the number of Customers who triggered the campaign and received the control. |
| 80 | `CP.CPG.TEST.PLAN.START.DATE` | `CpCampaign_TestPlanStartDate` | TField |  | This field is used to specify the planned date to start the campaign testing. |
| 81 | `CP.CPG.TEST.PLAN.END.DATE` | `CpCampaign_TestPlanEndDate` | TField |  | This field is used to specify the planned date to end the campaign testing. |
| 82 | `CP.CPG.MULTI.STAGE.ID` | `CpCampaign_MultiStageId` | TField |  | This field is used to specify the id of the multi stage campaign. |
| 83 | `CP.CPG.MULTI.STAGE.ORIGINAL.ID` | `CpCampaign_MultiStageOriginalId` | TField |  | This field is used to specify the original id of the multi stage campaign. |
| 84 | `CP.CPG.CAMPAIGN.TYPE` | `CpCampaign_CampaignType` | TField |  | This field is used to specify the campaign type based on EB.LOOKUP values CP.CAMPAIGN.TYPE (MULTI, SINGLE, FOLLOWUP) |
| 85 | `CP.CPG.FOLLOW.UP.CONDITION` | `CpCampaign_FollowUpCondition` | TField |  | This field contains a multi value list of followup campaigns id. |
| 86 | `CP.CPG.FOLLOW.UP.CAMPAIGN` | `CpCampaign_FollowUpCampaign` |  |  |  |
| 87 | `CP.CPG.FW.CONDITION.RESPONSE` | `CpCampaign_FwConditionResponse` |  |  |  |
| 88 | `CP.CPG.DELAY.EVENT` | `CpCampaign_DelayEvent` | TField |  | This field is used to specify the delay event id. |
| 89 | `CP.CPG.START.SUSPEND.DATE` | `CpCampaign_StartSuspendDate` |  |  |  |
| 90 | `CP.CPG.SUSPEND.TIME` | `CpCampaign_SuspendTime` |  |  |  |
| 91 | `CP.CPG.MINIMAL.DETAILS.FLAG` | `CpCampaign_MinimalDetailsFlag` | TField |  | This field represents a flag with y/n in order to check if minimal details have been provided to Campaign. |
| 92 | `CP.CPG.RESERVED.12` | `CpCampaign_Reserved12` |  |  |  |
| 93 | `CP.CPG.RESERVED.11` | `CpCampaign_Reserved11` | TField |  |  |
| 94 | `CP.CPG.RESERVED.10` | `CpCampaign_Reserved10` | TField |  |  |
| 95 | `CP.CPG.RESERVED.9` | `CpCampaign_Reserved9` | TField |  |  |
| 96 | `CP.CPG.RESERVED.8` | `CpCampaign_Reserved8` | TField |  |  |
| 97 | `CP.CPG.RESERVED.7` | `CpCampaign_Reserved7` | TField |  |  |
| 98 | `CP.CPG.RESERVED.6` | `CpCampaign_Reserved6` | TField |  |  |
| 99 | `CP.CPG.RESERVED.5` | `CpCampaign_Reserved5` | TField |  |  |
| 100 | `CP.CPG.RESERVED.4` | `CpCampaign_Reserved4` | TField |  |  |
| 101 | `CP.CPG.RESERVED.3` | `CpCampaign_Reserved3` | TField |  |  |
| 102 | `CP.CPG.RESERVED.2` | `CpCampaign_Reserved2` | TField |  |  |
| 103 | `CP.CPG.RESERVED.1` | `CpCampaign_Reserved1` | TField |  |  |
| 104 | `CP.CPG.LOCAL.REF` | `CpCampaign_LocalRef` |  |  |  |
| 105 | `CP.CPG.OVERRIDE` | `CpCampaign_Override` |  |  |  |
| 106 | `CP.CPG.RECORD.STATUS` | `CpCampaign_RecordStatus` | String |  |  |
| 107 | `CP.CPG.CURR.NO` | `CpCampaign_CurrNo` | String |  |  |
| 108 | `CP.CPG.INPUTTER` | `CpCampaign_Inputter` |  |  |  |
| 109 | `CP.CPG.DATE.TIME` | `CpCampaign_DateTime` |  |  |  |
| 110 | `CP.CPG.AUTHORISER` | `CpCampaign_Authoriser` | String |  |  |
| 111 | `CP.CPG.CO.CODE` | `CpCampaign_CoCode` | String |  |  |
| 112 | `CP.CPG.DEPT.CODE` | `CpCampaign_DeptCode` | String |  |  |
| 113 | `CP.CPG.AUDITOR.CODE` | `CpCampaign_AuditorCode` | String |  |  |
| 114 | `CP.CPG.AUDIT.DATE.TIME` | `CpCampaign_AuditDateTime` | String |  |  |
