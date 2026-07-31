# CP.DYNAMIC.OPPORTUNITY — Table Schema

> Source: `INSERTS/I_F.CP.DYNAMIC.OPPORTUNITY` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.OPP.CUSTOMER` | `CpDynamicOpportunity_Customer` | TField | Yes | This field stores the name the ID of the customer who has been targeted. Validation Rules: Mandatory field, any 150 characters. |
| 2 | `CP.OPP.OPP.TYPE` | `CpDynamicOpportunity_OppType` | TField | Yes | The value contained by this field is an indication of the type of the campaign for which the opportunity record was created. The type could be Control campaign or Test campaign. This field is used in relation with the A/B Testing functionality. Validation Rules: Mandatory field, any 50 characters. |
| 3 | `CP.OPP.CAMPAIGN` | `CpDynamicOpportunity_Campaign` | TField | Yes | The ID of the campaign that has been selected for the customer. Linked to CP.CAMPAIGN table. Validation Rules: Mandatory field, any 150 characters. |
| 4 | `CP.OPP.TEST.ID` | `CpDynamicOpportunity_TestId` | TField |  | The ID of the Test campaign associated with the Control campaign. Linked to CP.VARIANT table. Validation Rules: Any 150 characters. |
| 5 | `CP.OPP.PROGRAM` | `CpDynamicOpportunity_Program` |  |  |  |
| 6 | `CP.OPP.OUTPUT.CHANNEL` | `CpDynamicOpportunity_OutputChannel` | TField | Yes | The ID of the output channel. Linked to the CP.CHANNEL table. Validation Rules: Mandatory field, any 150 characters. |
| 7 | `CP.OPP.CONTENT.LOCATION` | `CpDynamicOpportunity_ContentLocation` | TField |  | If OUTPUT.CHANNEL is an online one then this represents the location where the campaign is being output. Linked to the CP.CHANNEL.OUTPUT table. Any 150 characters. |
| 8 | `CP.OPP.CAMPAIGN.BANK.TRIGGER` | `CpDynamicOpportunity_CampaignBankTrigger` | TField |  | The ID of the trigger for the campaign. Linked to the CP.BANK.TRIGGER table. Validation Rules: Any 150 characters. |
| 9 | `CP.OPP.CAMPAIGN.CHANNEL.TRIGGER` | `CpDynamicOpportunity_CampaignChannelTrigger` | TField |  | The ID of the trigger for the campaign. Linked to the CP.CHANNEL.TRIGGER table. Any 150 characters. |
| 10 | `CP.OPP.PRODUCT.GROUP` | `CpDynamicOpportunity_ProductGroup` | TField |  | The ID of the associated product group that is being promoted by the campaign. Any 150 characters. |
| 11 | `CP.OPP.PRODUCT` | `CpDynamicOpportunity_Product` | TField |  | The ID of the associated product that is being promoted by the campaign. Any 150 characters. |
| 12 | `CP.OPP.PROFILE` | `CpDynamicOpportunity_Profile` |  |  |  |
| 13 | `CP.OPP.PROFILE.CONDITION` | `CpDynamicOpportunity_ProfileCondition` |  |  |  |
| 14 | `CP.OPP.CONDITION.EVALUATION` | `CpDynamicOpportunity_ConditionEvaluation` |  |  |  |
| 15 | `CP.OPP.TAKEUP.CHANNEL` | `CpDynamicOpportunity_TakeupChannel` | TField |  | Take-up channel for any sales made through the campaign. Any 200 characters. |
| 16 | `CP.OPP.START.DATETIME` | `CpDynamicOpportunity_StartDatetime` | TField |  | The date and time that the campaign was targeted to the customer. Any 50 characters. |
| 17 | `CP.OPP.LAST.UPDATE.DATETIME` | `CpDynamicOpportunity_LastUpdateDatetime` | TField |  | The last date and time an interaction was performed on the opportunity. Any 50 characters. |
| 18 | `CP.OPP.NUMBER.VIEWS` | `CpDynamicOpportunity_NumberViews` | TField |  | The count of the number of times the opportunity has been viewed by the customer. Numeric value. |
| 19 | `CP.OPP.VIEWS.DATETIME` | `CpDynamicOpportunity_ViewsDatetime` |  |  |  |
| 20 | `CP.OPP.NUMBER.CLICKS` | `CpDynamicOpportunity_NumberClicks` | TField |  | The count of the number of times the opportunity has been viewed by the customer. Numeric value. |
| 21 | `CP.OPP.CLICKS.DATETIME` | `CpDynamicOpportunity_ClicksDatetime` |  |  |  |
| 22 | `CP.OPP.STATUS` | `CpDynamicOpportunity_Status` | TField |  | Status of the opportunity. Any 50 characters. |
| 23 | `CP.OPP.CAMPAIGN.ORIGINAL.ID` | `CpDynamicOpportunity_CampaignOriginalId` | TField |  | The ID of the original Campaign that triggered the opportunity. Any 35 characters. |
| 24 | `CP.OPP.STATUS.TYPE` | `CpDynamicOpportunity_StatusType` | TField |  | Represents what type of opportunity it is, based on campaign workflow running/testing. |
| 25 | `CP.OPP.BWS.DISCUSSED` | `CpDynamicOpportunity_BwsDiscussed` |  |  |  |
| 26 | `CP.OPP.BWS.NARRATIVE` | `CpDynamicOpportunity_BwsNarrative` |  |  |  |
| 27 | `CP.OPP.BWS.TELLER` | `CpDynamicOpportunity_BwsTeller` |  |  |  |
| 28 | `CP.OPP.BWS.DATETIME.DISCUSSION` | `CpDynamicOpportunity_BwsDatetimeDiscussion` |  |  |  |
| 29 | `CP.OPP.BWS.BRANCH` | `CpDynamicOpportunity_BwsBranch` |  |  |  |
| 30 | `CP.OPP.BWS.TALK.PRODUCT.AGAIN` | `CpDynamicOpportunity_BwsTalkProductAgain` | TField |  | Y or N flag that indicates if the customer wants to hear/talk about the product again. Any 3 characters. |
| 31 | `CP.OPP.NAV.TYPE` | `CpDynamicOpportunity_NavType` | TField |  | This field stores how the page to which the customer is redirected will be displayed. Possible values below. New Window Same Window Temenos UXP Navigation Top Level System Browser |
| 32 | `CP.OPP.CLICK.URL` | `CpDynamicOpportunity_ClickUrl` | TField |  | This field stores the URL a customer is redirected in case s/he decides to click on the content attached to the message which was communicated by the bank as part of marketing campaign. |
| 33 | `CP.OPP.DELAY.TRIGGER` | `CpDynamicOpportunity_DelayTrigger` | TField |  | The ID of the delay trigger for the multistage campaign. Linked to the CP.DELAY.EVENT.DETAILS table. |
| 34 | `CP.OPP.CUSTOMER.SOURCE` | `CpDynamicOpportunity_CustomerSource` | TField |  | This field stores the source where a customer is registered: Internal (T24) or External (other core banking system) |
| 35 | `CP.OPP.CR.CONTACT.LOG.ID` | `CpDynamicOpportunity_CrContactLogId` | TField |  | This field stores the id from CR.CONTACT.LOG that was generated when this opportunity was first created |
| 36 | `CP.OPP.RESERVED.57` | `CpDynamicOpportunity_Reserved57` | TField |  |  |
| 37 | `CP.OPP.RESERVED.56` | `CpDynamicOpportunity_Reserved56` | TField |  |  |
| 38 | `CP.OPP.RESERVED.55` | `CpDynamicOpportunity_Reserved55` | TField |  |  |
| 39 | `CP.OPP.RESERVED.54` | `CpDynamicOpportunity_Reserved54` | TField |  |  |
| 40 | `CP.OPP.RESERVED.53` | `CpDynamicOpportunity_Reserved53` | TField |  |  |
| 41 | `CP.OPP.RESERVED.52` | `CpDynamicOpportunity_Reserved52` | TField |  |  |
| 42 | `CP.OPP.RESERVED.51` | `CpDynamicOpportunity_Reserved51` | TField |  |  |
| 43 | `CP.OPP.RESERVED.50` | `CpDynamicOpportunity_Reserved50` | TField |  |  |
| 44 | `CP.OPP.RESERVED.49` | `CpDynamicOpportunity_Reserved49` | TField |  |  |
| 45 | `CP.OPP.RESERVED.48` | `CpDynamicOpportunity_Reserved48` | TField |  |  |
| 46 | `CP.OPP.RESERVED.47` | `CpDynamicOpportunity_Reserved47` | TField |  |  |
| 47 | `CP.OPP.RESERVED.46` | `CpDynamicOpportunity_Reserved46` | TField |  |  |
| 48 | `CP.OPP.RESERVED.45` | `CpDynamicOpportunity_Reserved45` | TField |  |  |
| 49 | `CP.OPP.RESERVED.44` | `CpDynamicOpportunity_Reserved44` | TField |  |  |
| 50 | `CP.OPP.RESERVED.43` | `CpDynamicOpportunity_Reserved43` | TField |  |  |
| 51 | `CP.OPP.RESERVED.42` | `CpDynamicOpportunity_Reserved42` | TField |  |  |
| 52 | `CP.OPP.RESERVED.41` | `CpDynamicOpportunity_Reserved41` | TField |  |  |
| 53 | `CP.OPP.RESERVED.40` | `CpDynamicOpportunity_Reserved40` | TField |  |  |
| 54 | `CP.OPP.RESERVED.39` | `CpDynamicOpportunity_Reserved39` | TField |  |  |
| 55 | `CP.OPP.RESERVED.38` | `CpDynamicOpportunity_Reserved38` | TField |  |  |
| 56 | `CP.OPP.RESERVED.37` | `CpDynamicOpportunity_Reserved37` | TField |  |  |
| 57 | `CP.OPP.RESERVED.36` | `CpDynamicOpportunity_Reserved36` | TField |  |  |
| 58 | `CP.OPP.RESERVED.35` | `CpDynamicOpportunity_Reserved35` | TField |  |  |
| 59 | `CP.OPP.RESERVED.34` | `CpDynamicOpportunity_Reserved34` | TField |  |  |
| 60 | `CP.OPP.RESERVED.33` | `CpDynamicOpportunity_Reserved33` | TField |  |  |
| 61 | `CP.OPP.RESERVED.32` | `CpDynamicOpportunity_Reserved32` | TField |  |  |
| 62 | `CP.OPP.RESERVED.31` | `CpDynamicOpportunity_Reserved31` | TField |  |  |
| 63 | `CP.OPP.RESERVED.30` | `CpDynamicOpportunity_Reserved30` | TField |  |  |
| 64 | `CP.OPP.RESERVED.29` | `CpDynamicOpportunity_Reserved29` | TField |  |  |
| 65 | `CP.OPP.RESERVED.28` | `CpDynamicOpportunity_Reserved28` | TField |  |  |
| 66 | `CP.OPP.RESERVED.27` | `CpDynamicOpportunity_Reserved27` | TField |  |  |
| 67 | `CP.OPP.RESERVED.26` | `CpDynamicOpportunity_Reserved26` | TField |  |  |
| 68 | `CP.OPP.RESERVED.25` | `CpDynamicOpportunity_Reserved25` | TField |  |  |
| 69 | `CP.OPP.RESERVED.24` | `CpDynamicOpportunity_Reserved24` | TField |  |  |
| 70 | `CP.OPP.RESERVED.23` | `CpDynamicOpportunity_Reserved23` | TField |  |  |
| 71 | `CP.OPP.RESERVED.22` | `CpDynamicOpportunity_Reserved22` | TField |  |  |
| 72 | `CP.OPP.RESERVED.21` | `CpDynamicOpportunity_Reserved21` | TField |  |  |
| 73 | `CP.OPP.RESERVED.20` | `CpDynamicOpportunity_Reserved20` | TField |  |  |
| 74 | `CP.OPP.RESERVED.19` | `CpDynamicOpportunity_Reserved19` | TField |  |  |
| 75 | `CP.OPP.RESERVED.18` | `CpDynamicOpportunity_Reserved18` | TField |  |  |
| 76 | `CP.OPP.RESERVED.17` | `CpDynamicOpportunity_Reserved17` | TField |  |  |
| 77 | `CP.OPP.RESERVED.16` | `CpDynamicOpportunity_Reserved16` | TField |  |  |
| 78 | `CP.OPP.RESERVED.15` | `CpDynamicOpportunity_Reserved15` | TField |  |  |
| 79 | `CP.OPP.RESERVED.14` | `CpDynamicOpportunity_Reserved14` | TField |  |  |
| 80 | `CP.OPP.RESERVED.13` | `CpDynamicOpportunity_Reserved13` | TField |  |  |
| 81 | `CP.OPP.RESERVED.12` | `CpDynamicOpportunity_Reserved12` | TField |  |  |
| 82 | `CP.OPP.RESERVED.11` | `CpDynamicOpportunity_Reserved11` | TField |  |  |
| 83 | `CP.OPP.RESERVED.10` | `CpDynamicOpportunity_Reserved10` | TField |  |  |
| 84 | `CP.OPP.RESERVED.9` | `CpDynamicOpportunity_Reserved9` | TField |  |  |
| 85 | `CP.OPP.RESERVED.8` | `CpDynamicOpportunity_Reserved8` | TField |  |  |
| 86 | `CP.OPP.RESERVED.7` | `CpDynamicOpportunity_Reserved7` | TField |  |  |
| 87 | `CP.OPP.RESERVED.6` | `CpDynamicOpportunity_Reserved6` | TField |  |  |
| 88 | `CP.OPP.RESERVED.5` | `CpDynamicOpportunity_Reserved5` | TField |  |  |
| 89 | `CP.OPP.RESERVED.4` | `CpDynamicOpportunity_Reserved4` | TField |  |  |
| 90 | `CP.OPP.RESERVED.3` | `CpDynamicOpportunity_Reserved3` | TField |  |  |
| 91 | `CP.OPP.RESERVED.2` | `CpDynamicOpportunity_Reserved2` | TField |  |  |
| 92 | `CP.OPP.RESERVED.1` | `CpDynamicOpportunity_Reserved1` | TField |  |  |
| 93 | `CP.OPP.LOCAL.REF` | `CpDynamicOpportunity_LocalRef` |  |  |  |
| 94 | `CP.OPP.OVERRIDE` | `CpDynamicOpportunity_Override` |  |  |  |
| 95 | `CP.OPP.RECORD.STATUS` | `CpDynamicOpportunity_RecordStatus` | String |  |  |
| 96 | `CP.OPP.CURR.NO` | `CpDynamicOpportunity_CurrNo` | String |  |  |
| 97 | `CP.OPP.INPUTTER` | `CpDynamicOpportunity_Inputter` |  |  |  |
| 98 | `CP.OPP.DATE.TIME` | `CpDynamicOpportunity_DateTime` |  |  |  |
| 99 | `CP.OPP.AUTHORISER` | `CpDynamicOpportunity_Authoriser` | String |  |  |
| 100 | `CP.OPP.CO.CODE` | `CpDynamicOpportunity_CoCode` | String |  |  |
| 101 | `CP.OPP.DEPT.CODE` | `CpDynamicOpportunity_DeptCode` | String |  |  |
| 102 | `CP.OPP.AUDITOR.CODE` | `CpDynamicOpportunity_AuditorCode` | String |  |  |
| 103 | `CP.OPP.AUDIT.DATE.TIME` | `CpDynamicOpportunity_AuditDateTime` | String |  |  |
