# PI.PS.MAPPING.RULE — Table Schema

> Source: `INSERTS/I_F.PI.PS.MAPPING.RULE` in `PI_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `POM.DESCRIPTION` | `PiPsMappingRule_Description` |  |  |  |
| 2 | `POM.PAYMENT.SYSTEM` | `PiPsMappingRule_PaymentSystem` |  |  |  |
| 3 | `POM.PS.MAPPING.RULE` | `PiPsMappingRule_PsMappingRule` |  |  |  |
| 4 | `POM.PS.MAP.RULE.API` | `PiPsMappingRule_PsMapRuleApi` |  |  |  |
| 5 | `POM.RESULT.OPTION` | `PiPsMappingRule_ResultOption` |  |  |  |
| 6 | `POM.PS.MAPPING.RECORD` | `PiPsMappingRule_PsMappingRecord` |  |  |  |
| 7 | `POM.PS.MAPPING.API` | `PiPsMappingRule_PsMappingApi` |  |  |  |
| 8 | `POM.PS.VERSION` | `PiPsMappingRule_PsVersion` |  |  |  |
| 9 | `POM.EB.ACTIVITY` | `PiPsMappingRule_EbActivity` |  |  |  |
| 10 | `POM.DELIVERY.OPTIONS` | `PiPsMappingRule_DeliveryOptions` |  |  |  |
| 11 | `POM.RESERVED.13` | `PiPsMappingRule_Reserved13` |  |  |  |
| 12 | `POM.RESERVED.12` | `PiPsMappingRule_Reserved12` |  |  |  |
| 13 | `POM.RESERVED.11` | `PiPsMappingRule_Reserved11` |  |  |  |
| 14 | `POM.DEFAULT.RESULT` | `PiPsMappingRule_DefaultResult` |  |  |  |
| 15 | `POM.DEFAULT.MAPPING.RECORD` | `PiPsMappingRule_DefaultMappingRecord` |  |  |  |
| 16 | `POM.DEFAULT.MAPPING.API` | `PiPsMappingRule_DefaultMappingApi` |  |  |  |
| 17 | `POM.DEFAULT.VERSION` | `PiPsMappingRule_DefaultVersion` |  |  |  |
| 18 | `POM.DEFAULT.EB.ACTIVITY` | `PiPsMappingRule_DefaultEbActivity` |  |  |  |
| 19 | `POM.DEFAULT.DELIVERY.OPTIONS` | `PiPsMappingRule_DefaultDeliveryOptions` |  |  |  |
| 20 | `POM.RESERVED.8` | `PiPsMappingRule_Reserved8` |  |  |  |
| 21 | `POM.RESERVED.7` | `PiPsMappingRule_Reserved7` |  |  |  |
| 22 | `POM.RESERVED.6` | `PiPsMappingRule_Reserved6` |  |  |  |
| 23 | `POM.SOURCE.SYSTEM` | `PiPsMappingRule_SourceSystem` |  |  |  |
| 24 | `POM.SOURCE.MAPPING.RULE` | `PiPsMappingRule_SourceMappingRule` |  |  |  |
| 25 | `POM.SOURCE.MAP.RULE.API` | `PiPsMappingRule_SourceMapRuleApi` |  |  |  |
| 26 | `POM.SOURCE.RESULT.OPTION` | `PiPsMappingRule_SourceResultOption` |  |  |  |
| 27 | `POM.SOURCE.MAPPING.API` | `PiPsMappingRule_SourceMappingApi` |  |  |  |
| 28 | `POM.LOCAL.REF` | `PiPsMappingRule_LocalRef` |  |  |  |
| 29 | `POM.OVERRIDE` | `PiPsMappingRule_Override` |  |  |  |
| 30 | `POM.RECORD.STATUS` | `PiPsMappingRule_RecordStatus` | String |  |  |
| 31 | `POM.CURR.NO` | `PiPsMappingRule_CurrNo` | String |  |  |
| 32 | `POM.INPUTTER` | `PiPsMappingRule_Inputter` |  |  |  |
| 33 | `POM.DATE.TIME` | `PiPsMappingRule_DateTime` |  |  |  |
| 34 | `POM.AUTHORISER` | `PiPsMappingRule_Authoriser` | String |  |  |
| 35 | `POM.CO.CODE` | `PiPsMappingRule_CoCode` | String |  |  |
| 36 | `POM.DEPT.CODE` | `PiPsMappingRule_DeptCode` | String |  |  |
| 37 | `POM.AUDITOR.CODE` | `PiPsMappingRule_AuditorCode` | String |  |  |
| 38 | `POM.AUDIT.DATE.TIME` | `PiPsMappingRule_AuditDateTime` | String |  |  |
| 39 | `POM.SOURCE.MAP.RULE.STATUS` | `PiPsMappingRule_SourceMapRuleStatus` |  |  |  |
