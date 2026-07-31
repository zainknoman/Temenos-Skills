# ST.CDM.MONITOR — Table Schema

> Source: `INSERTS/I_F.ST.CDM.MONITOR` in `ST_DormancyMonitor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.CDM.AUTO.DORM.STATUS` | `StCdmMonitor_AutoDormStatus` | TField |  | This field holds the system calculated dormancy status for a customer. User input is restricted Auto dormancy status is updated by ST.CDM.SERVICE |
| 2 | `ST.CDM.DATE.OF.DORMANCY` | `StCdmMonitor_DateOfDormancy` | TField |  | This field holds the date on which AUTO.DORM.STATUS is updated . User input is restricted When dormancy is reset manually, this field will be cleared. |
| 3 | `ST.CDM.MANUAL.DORM.STATUS` | `StCdmMonitor_ManualDormStatus` | TField |  | Dormancy status defined by user. The status defined here will preside over the AUTO.DORM.STATUS. When dormancy is reset manually, this field will be cleared. Validation Rule: Should match the dormancy status configured in ST.CDM.PARAMETER. |
| 4 | `ST.CDM.MANUAL.STATUS.DATE` | `StCdmMonitor_ManualStatusDate` | TField |  | Date on which MANUAL.DORM.STATUS is defined. This will be defaulted by the system during each amendment of MANUAL.DORM.STATUS. When the MANUAL.DORM.STATUS is removed the value captured here will be removed . |
| 5 | `ST.CDM.CURRENT.DORM.STATUS` | `StCdmMonitor_CurrentDormStatus` | TField |  | Current status of the customer, will be updated based on the presence of AUTO.DORM.STATUS and MANUAL.DORM.STATUS.This field will be defaulted with AUTO.DORM.STATUS if only AUTO.DORM.STATUS is available or will be defaulted with MANUAL.DORM.STATUS if both AUTO.DORM.STATUS and MANUAL.DORM.STATUS exist. During dormancy reset this field will be cleared off indicating that the customer is not dormant anymore.User input is restricted. |
| 6 | `ST.CDM.MANUAL.RESET.ACTIVE` | `StCdmMonitor_ManualResetActive` | TField |  | Option to reset the dormancy status manually. If set to yes all dormancy related fields will be cleared, indicating that the customer is not dormant anymore. LAST.ACTIVITY.DATE will be captured based on the further activity the customer performs with the bank. Validation Rule: Allowed options : YES .This indicates the customer is not dormant anymore. |
| 7 | `ST.CDM.DATE.OF.REMOVAL` | `StCdmMonitor_DateOfRemoval` | TField |  | The date on which dormancy reset is triggered is captured here and will be cleared off once the customer becomes dormant. User input is restricted. |
| 8 | `ST.CDM.RESET.COMMENTS` | `StCdmMonitor_ResetComments` | TField |  | The reason for reset is to captured here. Allowed for user input. If not defined will be updated as "Reset done by User" during manual reset and "Reset done by System" during system initiated reset. Will be cleared off when the customer's status becomes dormant. |
| 9 | `ST.CDM.DORMANCY.REMOVED.BY` | `StCdmMonitor_DormancyRemovedBy` | TField |  | This field indicates whether the dormancy reset is triggered by system or user. Allowed for user input. If not defined will be updated as "Reset done by User" during manual reset and "Reset done by System" during system initiated reset. Will be cleared off when the customer's status becomes dormant. |
| 10 | `ST.CDM.PRODUCT.ID` | `StCdmMonitor_ProductId` |  |  |  |
| 11 | `ST.CDM.AUTO.PRODUCT.STATUS` | `StCdmMonitor_AutoProductStatus` |  |  |  |
| 12 | `ST.CDM.LAST.ACTIVITY.DATE` | `StCdmMonitor_LastActivityDate` | TField |  | The last activity date recorded in the system for the customer AUTO - will be updated when a new product is made ACTIVE or an existing product is modified from ACTIVE to INACTIVE status for the customer UNMONITORED - will be obtained from ST.CUSTOMER.ACTIVITY during contract creation, amendment and maturity MONITORED - will be obtained from ST.CUSTOMER.ACTIVITY for MONITORED applications as per ST.CDM.PARAMETER definition EXTERNAL - will be obtained from ST.CDM.EXT.ACT.CAPTURE application User input is restricted. |
| 13 | `ST.CDM.LAST.ACT.GRACE.DATE` | `StCdmMonitor_LastActGraceDate` | TField |  |  |
| 14 | `ST.CDM.NEXT.CHECK.DATE` | `StCdmMonitor_NextCheckDate` | TField |  | Date on which dormancy check has to be triggered for a customer. Will be derived as LAST.ACT.GRACE.DATE + DORMANCY.PERIOD (against first MV set in ST.CDM.PARAMETER) during first update. Once this date is reached and when all the products remain INACTIVE the status form where the period is picked for NEXT.CHECK.DATE calculation will be updated in AUTO.DORM.STATUS and date will be cycled as NEXT.CHECK.DATE + DORMANCY.PERIOD of next status. User input is restricted. |
| 15 | `ST.CDM.RESERVED.05` | `StCdmMonitor_Reserved05` | TField |  |  |
| 16 | `ST.CDM.RESERVED.04` | `StCdmMonitor_Reserved04` | TField |  |  |
| 17 | `ST.CDM.RESERVED.03` | `StCdmMonitor_Reserved03` | TField |  |  |
| 18 | `ST.CDM.RESERVED.02` | `StCdmMonitor_Reserved02` | TField |  |  |
| 19 | `ST.CDM.RESERVED.01` | `StCdmMonitor_Reserved01` | TField |  |  |
| 20 | `ST.CDM.LOCAL.REF` | `StCdmMonitor_LocalRef` |  |  |  |
| 21 | `ST.CDM.OVERRIDE` | `StCdmMonitor_Override` |  |  |  |
| 22 | `ST.CDM.RECORD.STATUS` | `StCdmMonitor_RecordStatus` | String |  |  |
| 23 | `ST.CDM.CURR.NO` | `StCdmMonitor_CurrNo` | String |  |  |
| 24 | `ST.CDM.INPUTTER` | `StCdmMonitor_Inputter` |  |  |  |
| 25 | `ST.CDM.DATE.TIME` | `StCdmMonitor_DateTime` |  |  |  |
| 26 | `ST.CDM.AUTHORISER` | `StCdmMonitor_Authoriser` | String |  |  |
| 27 | `ST.CDM.CO.CODE` | `StCdmMonitor_CoCode` | String |  |  |
| 28 | `ST.CDM.DEPT.CODE` | `StCdmMonitor_DeptCode` | String |  |  |
| 29 | `ST.CDM.AUDITOR.CODE` | `StCdmMonitor_AuditorCode` | String |  |  |
| 30 | `ST.CDM.AUDIT.DATE.TIME` | `StCdmMonitor_AuditDateTime` | String |  |  |
