# AA.EVENT.MAPPING — Table Schema

> Source: `INSERTS/I_F.AA.EVENT.MAPPING` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.EVM.DESCRIPTION` | `AaEventMapping_Description` |  |  |  |
| 2 | `AA.EVM.LONG.DESCRIPTION` | `AaEventMapping_LongDescription` |  |  |  |
| 3 | `AA.EVM.DEFAULT.EVENT.CHARGE` | `AaEventMapping_DefaultEventCharge` | TField | Yes | Default charge that would be used in the event if no specific mapping is found in the Property name set. This is not a mandatory field. If this field is not set, then the original charge that was raised would be sent across in the event. |
| 4 | `AA.EVM.DEFAULT.EVENT.INTEREST` | `AaEventMapping_DefaultEventInterest` | TField | Yes | Default interest that would be used in the event if no specific mapping is found in the name set This is not a mandatory field. If this field is not set, then the original interest that was raised would be sent across in the event |
| 5 | `AA.EVM.DEFAULT.EVENT.PERIODIC.CHARGE` | `AaEventMapping_DefaultEventPeriodicCharge` | TField | Yes | Default periodic charge that would be used in the event if no specific mapping is found in the Property/Event Property name set. This is not a mandatory field If this field is not set, then the original periodic charge that was raised would be sent across in the event. |
| 6 | `AA.EVM.DEFAULT.EVENT.NAME` | `AaEventMapping_DefaultEventName` | TField |  |  |
| 7 | `AA.EVM.DEFAULT.BALANCE.NAME` | `AaEventMapping_DefaultBalanceName` | TField | Yes | Default Balance name that would be used in the event if no specific mapping is found in the Balance/Event Balance name set. This is not a mandatory field. If this field is not set, then the original balance that was raised would be sent across in the event |
| 8 | `AA.EVM.DEFAULT.CHARGE` | `AaEventMapping_DefaultCharge` | TField |  | Default charge that would be used for raising charge bill/accounting entries when system. It is expected that the charges raised in EPP have proper mapping against individual charge name in the IN.EVENT.PROPERTY.NAME set. In case, if a charge is not configured, system would raise entries against this charge. |
| 9 | `AA.EVM.DEFAULT.INTEREST` | `AaEventMapping_DefaultInterest` | TField | Yes | It is expected that the interest raised in EPP have proper mapping against individual interest name in the IN.EVENT.PROPERTY.NAME set. In case, if an interest is not configured, system would record the rate against this property. Mandatory field.Should be a valid INTEREST property. |
| 10 | `AA.EVM.DEFAULT.PERIODIC.CHARGE` | `AaEventMapping_DefaultPeriodicCharge` | TField | Yes | Default Periodic charge that would be used for recording periodic charge when system cannot map the incoming periodic charge property in IN.EVENT.PROPERTY.NAME/IN.PROPERTY.NAME set. It is expected that the Periodic charge raised in EPP have proper mapping against individual Periodic charge name in the IN.EVENT.PROPERTY.NAME set. In case, if a periodic charge is not configured, system would record the rate against this property. Mandatory field.Should be a valid PERIODIC.CHARGE property. |
| 11 | `AA.EVM.ACTIVITY.NAME` | `AaEventMapping_ActivityName` |  |  |  |
| 12 | `AA.EVM.ACTIVITY.CLASS` | `AaEventMapping_ActivityClass` |  |  |  |
| 13 | `AA.EVM.MS.EVENT` | `AaEventMapping_MsEvent` |  |  |  |
| 14 | `AA.EVM.EVENT.NAME` | `AaEventMapping_EventName` |  |  |  |
| 15 | `AA.EVM.PROPERTY.NAME` | `AaEventMapping_PropertyName` |  |  |  |
| 16 | `AA.EVM.PROPERTY.CLASS` | `AaEventMapping_PropertyClass` |  |  |  |
| 17 | `AA.EVM.EVENT.PROPERTY.NAME` | `AaEventMapping_EventPropertyName` |  |  |  |
| 18 | `AA.EVM.BALANCE.NAME` | `AaEventMapping_BalanceName` |  |  |  |
| 19 | `AA.EVM.EVENT.BALANCE.NAME` | `AaEventMapping_EventBalanceName` |  |  |  |
| 20 | `AA.EVM.CONTEXT.NAME` | `AaEventMapping_ContextName` |  |  |  |
| 21 | `AA.EVM.EVENT.CONTEXT.NAME` | `AaEventMapping_EventContextName` |  |  |  |
| 22 | `AA.EVM.ROLE` | `AaEventMapping_Role` |  |  |  |
| 23 | `AA.EVM.EVENT.ROLE` | `AaEventMapping_EventRole` |  |  |  |
| 24 | `AA.EVM.IN.EVENT.PROPERTY.NAME` | `AaEventMapping_InEventPropertyName` |  |  |  |
| 25 | `AA.EVM.IN.PROPERTY.NAME` | `AaEventMapping_InPropertyName` |  |  |  |
| 26 | `AA.EVM.RECORD.STATUS` | `AaEventMapping_RecordStatus` | String |  |  |
| 27 | `AA.EVM.CURR.NO` | `AaEventMapping_CurrNo` | String |  |  |
| 28 | `AA.EVM.INPUTTER` | `AaEventMapping_Inputter` |  |  |  |
| 29 | `AA.EVM.DATE.TIME` | `AaEventMapping_DateTime` |  |  |  |
| 30 | `AA.EVM.AUTHORISER` | `AaEventMapping_Authoriser` | String |  |  |
| 31 | `AA.EVM.CO.CODE` | `AaEventMapping_CoCode` | String |  |  |
| 32 | `AA.EVM.DEPT.CODE` | `AaEventMapping_DeptCode` | String |  |  |
| 33 | `AA.EVM.AUDITOR.CODE` | `AaEventMapping_AuditorCode` | String |  |  |
| 34 | `AA.EVM.AUDIT.DATE.TIME` | `AaEventMapping_AuditDateTime` | String |  |  |
| 35 | `AA.EVM.DEFAULT.CASHBACK` | `AaEventMapping_DefaultCashback` | TField |  |  |
| 36 | `AA.EVM.DEFAULT.CREDIT.INTEREST` | `AaEventMapping_DefaultCreditInterest` | TField |  |  |
