# ST.CDM.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ST.CDM.PARAMETER` in `ST_DormancyMonitor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.CDP.DESCRIPTION` | `StCdmParameter_Description` | TField |  |  |
| 2 | `ST.CDP.DORMANCY.STATUS` | `StCdmParameter_DormancyStatus` |  |  |  |
| 3 | `ST.CDP.DORMANCY.PERIOD` | `StCdmParameter_DormancyPeriod` |  |  |  |
| 4 | `ST.CDP.CUSTOMER.FILTER.RULE` | `StCdmParameter_CustomerFilterRule` | TField |  | Rule to decide upon the customer's eligibility for dormancy processing. Validation Rule: Should be a valid ID of EB.RULE.GATEWAY. |
| 5 | `ST.CDP.CUSTOMER.FILTER.API` | `StCdmParameter_CustomerFilterApi` | TField |  | API to decide upon the customer's eligibility for dormancy processing . Validation Rule: Should be a valid ID of EB.API. |
| 6 | `ST.CDP.PRODUCT` | `StCdmParameter_Product` |  |  |  |
| 7 | `ST.CDP.PRODUCT.CLASS` | `StCdmParameter_ProductClass` |  |  |  |
| 8 | `ST.CDP.PRD.RESERVED.5` | `StCdmParameter_PrdReserved5` |  |  |  |
| 9 | `ST.CDP.PRD.RESERVED.4` | `StCdmParameter_PrdReserved4` |  |  |  |
| 10 | `ST.CDP.PRD.RESERVED.3` | `StCdmParameter_PrdReserved3` |  |  |  |
| 11 | `ST.CDP.PRD.RESERVED.2` | `StCdmParameter_PrdReserved2` |  |  |  |
| 12 | `ST.CDP.PRD.RESERVED.1` | `StCdmParameter_PrdReserved1` |  |  |  |
| 13 | `ST.CDP.MONITORED.PRD.APPLN` | `StCdmParameter_MonitoredPrdAppln` |  |  |  |
| 14 | `ST.CDP.ALLOW.EXTERNAL.PRD` | `StCdmParameter_AllowExternalPrd` | TField |  | An options field which decides upon whether the external products recorded through ST.CDM.CONTACT.LOG should be considered for dormancy processing. Validation Rule: Allowed Value : Y - If set , ST.CDM.EXT.ACT.CAPTURE records can be created. |
| 15 | `ST.CDP.PRODUCT.GRACE.PERIOD` | `StCdmParameter_ProductGracePeriod` | TField |  | Allowed period before marking the customer as dormant. The period defined is applicable only for Monitored and external products, the dormancy check will be triggered once this period is reached. Validation Rule: Vaild format - D, M, Y. |
| 16 | `ST.CDP.PRODUCT.FILTER.RULE` | `StCdmParameter_ProductFilterRule` | TField |  | Rule to decide upon the contract's/product's eligibility for dormancy processing. Validation Rule: Should be a valid ID of EB.RULE.GATEWAY. |
| 17 | `ST.CDP.PRODUCT.FILTER.API` | `StCdmParameter_ProductFilterApi` | TField |  | Api to decide upon the contract's/product's eligibility for dormancy processing. Validation Rule: Should be a valid ID of EB.API. |
| 18 | `ST.CDP.TAKEOVER.COMPLETED` | `StCdmParameter_TakeoverCompleted` | TField |  | This field indicates if ST.CDM.TAKEOVER.SERVICE is run. Validation Rule: Allowed Values : YES - If set , then Takeover service can not be run again. |
| 19 | `ST.CDP.MONITORED.RESET.RULE` | `StCdmParameter_MonitoredResetRule` | TField |  | Rule to decide upon the monitored contract's/product's reset eligibility for dormancy processing. Validation Rule: Should be a valid ID of EB.RULE.GATEWAY. |
| 20 | `ST.CDP.MONITORED.RESET.API` | `StCdmParameter_MonitoredResetApi` | TField |  | Api to decide upon the monitored contract's/product's reset eligibility for dormancy processing. Validation Rule: Should be a valid ID of EB.API. |
| 21 | `ST.CDP.MIGRATE.LAST.ACTIVITY.DETAILS` | `StCdmParameter_MigrateLastActivityDetails` | TField |  | Field to indicate the status of migration of Last Activity Date details of Customer from legacy system. Validation Rule: Options field. Field Input enabled only when system migration is completed - indicated by field TAKEOVER.COMPLETED as YES Allowed Options: INPROGRESS - Indicates system is currently in process of manual migration of last activity date details using ST.CDM.EXT.ACT.CAPTURE. This options allows the user to overwrite the system dervied Last Activity date during take over process. COMPLETED - Indicates the manual migration is completed. Once updated with this value, field becomes disabled for further user inputs. |
| 22 | `ST.CDP.RESERVED.2` | `StCdmParameter_Reserved2` | TField |  |  |
| 23 | `ST.CDP.RESERVED.1` | `StCdmParameter_Reserved1` | TField |  |  |
| 24 | `ST.CDP.LOCAL.REF` | `StCdmParameter_LocalRef` |  |  |  |
| 25 | `ST.CDP.OVERRIDE` | `StCdmParameter_Override` |  |  |  |
| 26 | `ST.CDP.RECORD.STATUS` | `StCdmParameter_RecordStatus` | String |  |  |
| 27 | `ST.CDP.CURR.NO` | `StCdmParameter_CurrNo` | String |  |  |
| 28 | `ST.CDP.INPUTTER` | `StCdmParameter_Inputter` |  |  |  |
| 29 | `ST.CDP.DATE.TIME` | `StCdmParameter_DateTime` |  |  |  |
| 30 | `ST.CDP.AUTHORISER` | `StCdmParameter_Authoriser` | String |  |  |
| 31 | `ST.CDP.CO.CODE` | `StCdmParameter_CoCode` | String |  |  |
| 32 | `ST.CDP.DEPT.CODE` | `StCdmParameter_DeptCode` | String |  |  |
| 33 | `ST.CDP.AUDITOR.CODE` | `StCdmParameter_AuditorCode` | String |  |  |
| 34 | `ST.CDP.AUDIT.DATE.TIME` | `StCdmParameter_AuditDateTime` | String |  |  |
