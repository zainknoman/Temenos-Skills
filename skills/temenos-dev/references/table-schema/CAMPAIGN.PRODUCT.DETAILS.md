# CAMPAIGN.PRODUCT.DETAILS — Table Schema

> Source: `INSERTS/I_F.CAMPAIGN.PRODUCT.DETAILS` in `HKDEPO_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMP.PROD.SUBSCRIPTION.TOTAL` | `CampaignProductDetails_SubscriptionTotal` | TField |  | Field to store the running balance and currency of subscription amount received under the plan. Validation Rules : This is a NOINPUT field |
| 2 | `CAMP.PROD.ORG.MATURITY.DATE` | `CampaignProductDetails_OrgMaturityDate` | TField |  | Original Maturity date. Will be auto defaulted when terminating a contract for information purposes A valid date in the format YYYYMMDD. |
| 3 | `CAMP.PROD.TERMINATION.DATE` | `CampaignProductDetails_TerminationDate` | TField |  | Indicated the date input by the bank user for terminating the plan before actual maturity A valid date in the format YYYYMMDD. |
| 4 | `CAMP.PROD.TERMINATED` | `CampaignProductDetails_Terminated` | TField |  | Field to indicate if a deposit plan is terminated. Will be updated by batch routine once all the deposits under the plan is marked for redemption. Validation Rules : This is a NOINPUT field |
| 5 | `CAMP.PROD.LOCAL.REF` | `CampaignProductDetails_LocalRef` |  |  |  |
| 6 | `CAMP.PROD.RESERVED.1` | `CampaignProductDetails_Reserved1` | TField |  |  |
| 7 | `CAMP.PROD.RESERVED.2` | `CampaignProductDetails_Reserved2` | TField |  |  |
| 8 | `CAMP.PROD.RESERVED.3` | `CampaignProductDetails_Reserved3` | TField |  |  |
| 9 | `CAMP.PROD.RESERVED.4` | `CampaignProductDetails_Reserved4` | TField |  |  |
| 10 | `CAMP.PROD.RESERVED.5` | `CampaignProductDetails_Reserved5` | TField |  |  |
| 11 | `CAMP.PROD.RESERVED.6` | `CampaignProductDetails_Reserved6` | TField |  |  |
| 12 | `CAMP.PROD.RESERVED.7` | `CampaignProductDetails_Reserved7` | TField |  |  |
| 13 | `CAMP.PROD.RESERVED.8` | `CampaignProductDetails_Reserved8` | TField |  |  |
| 14 | `CAMP.PROD.RESERVED.9` | `CampaignProductDetails_Reserved9` | TField |  |  |
| 15 | `CAMP.PROD.RESERVED.10` | `CampaignProductDetails_Reserved10` | TField |  |  |
| 16 | `CAMP.PROD.OVERRIDE` | `CampaignProductDetails_Override` |  |  |  |
| 17 | `CAMP.PROD.RECORD.STATUS` | `CampaignProductDetails_RecordStatus` | String |  |  |
| 18 | `CAMP.PROD.CURR.NO` | `CampaignProductDetails_CurrNo` | String |  |  |
| 19 | `CAMP.PROD.INPUTTER` | `CampaignProductDetails_Inputter` |  |  |  |
| 20 | `CAMP.PROD.DATE.TIME` | `CampaignProductDetails_DateTime` |  |  |  |
| 21 | `CAMP.PROD.AUTHORISER` | `CampaignProductDetails_Authoriser` | String |  |  |
| 22 | `CAMP.PROD.CO.CODE` | `CampaignProductDetails_CoCode` | String |  |  |
| 23 | `CAMP.PROD.DEPT.CODE` | `CampaignProductDetails_DeptCode` | String |  |  |
| 24 | `CAMP.PROD.AUDITOR.CODE` | `CampaignProductDetails_AuditorCode` | String |  |  |
| 25 | `CAMP.PROD.AUDIT.DATE.TIME` | `CampaignProductDetails_AuditDateTime` | String |  |  |
