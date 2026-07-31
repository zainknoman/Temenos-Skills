# CR.CAMPAIGN.STATISTICS — Table Schema

> Source: `INSERTS/I_F.CR.CAMPAIGN.STATISTICS` in `CR_ModelBank.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CR.CAMP.STAT.BANK.ID` | `CrCampaignStatistics_BankId` | TField |  | This field stores ID of the master company. |
| 2 | `CR.CAMP.STAT.CAMPAIGN.ID` | `CrCampaignStatistics_CampaignId` | TField |  | This field stores the campaign generator ID. It can be STFD.CAMPAIGN for Short Term Deposit or ARCIB.ACCESS.CAMPAIGN for ARC&#160;IB&#160;access. |
| 3 | `CR.CAMP.STAT.START.DATE` | `CrCampaignStatistics_StartDate` | TField |  | This field specifies start date of the campaign. |
| 4 | `CR.CAMP.STAT.END.DATE` | `CrCampaignStatistics_EndDate` | TField |  | This field specifies end date of the campaign. |
| 5 | `CR.CAMP.STAT.LENGTH.IN.DAYS` | `CrCampaignStatistics_LengthInDays` | TField |  | This field stores the period of the campaign based on Start Date and the End Date. |
| 6 | `CR.CAMP.STAT.COMPANY` | `CrCampaignStatistics_Company` |  |  |  |
| 7 | `CR.CAMP.STAT.STATUS` | `CrCampaignStatistics_Status` |  |  |  |
| 8 | `CR.CAMP.STAT.OPP.COUNT` | `CrCampaignStatistics_OppCount` |  |  |  |
| 9 | `CR.CAMP.STAT.LEAD.COMPANY` | `CrCampaignStatistics_LeadCompany` |  |  |  |
| 10 | `CR.CAMP.STAT.COMP.TOTAL.OPP` | `CrCampaignStatistics_CompTotalOpp` |  |  |  |
| 11 | `CR.CAMP.STAT.CHANNEL` | `CrCampaignStatistics_Channel` |  |  |  |
| 12 | `CR.CAMP.STAT.CH.STATUS` | `CrCampaignStatistics_ChStatus` |  |  |  |
| 13 | `CR.CAMP.STAT.CH.OPP.COUNT` | `CrCampaignStatistics_ChOppCount` |  |  |  |
| 14 | `CR.CAMP.STAT.CH.TOTAL.OPP` | `CrCampaignStatistics_ChTotalOpp` |  |  |  |
| 15 | `CR.CAMP.STAT.TOTAL.BANK.OPP` | `CrCampaignStatistics_TotalBankOpp` | TField |  | This specifies the total opportunities created for the bank/ Master company under different branch companies. |
| 16 | `CR.CAMP.STAT.LAST.UPDATED.ON` | `CrCampaignStatistics_LastUpdatedOn` | TField |  |  |
| 17 | `CR.CAMP.STAT.RESERVED.10` | `CrCampaignStatistics_Reserved10` | TField |  |  |
| 18 | `CR.CAMP.STAT.RESERVED.9` | `CrCampaignStatistics_Reserved9` | TField |  |  |
| 19 | `CR.CAMP.STAT.RESERVED.8` | `CrCampaignStatistics_Reserved8` | TField |  |  |
| 20 | `CR.CAMP.STAT.RESERVED.7` | `CrCampaignStatistics_Reserved7` | TField |  |  |
| 21 | `CR.CAMP.STAT.RESERVED.6` | `CrCampaignStatistics_Reserved6` | TField |  |  |
| 22 | `CR.CAMP.STAT.RESERVED.5` | `CrCampaignStatistics_Reserved5` | TField |  |  |
| 23 | `CR.CAMP.STAT.RESERVED.4` | `CrCampaignStatistics_Reserved4` | TField |  |  |
| 24 | `CR.CAMP.STAT.RESERVED.3` | `CrCampaignStatistics_Reserved3` | TField |  |  |
| 25 | `CR.CAMP.STAT.RESERVED.2` | `CrCampaignStatistics_Reserved2` | TField |  |  |
| 26 | `CR.CAMP.STAT.RESERVED.1` | `CrCampaignStatistics_Reserved1` | TField |  |  |
