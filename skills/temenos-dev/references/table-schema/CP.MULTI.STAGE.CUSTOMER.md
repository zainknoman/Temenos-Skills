# CP.MULTI.STAGE.CUSTOMER — Table Schema

> Source: `INSERTS/I_F.CP.MULTI.STAGE.CUSTOMER` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.MSC.MS.ORIGINAL.ID` | `CpMultiStageCustomer_MsOriginalId` | TField |  |  |
| 2 | `CP.MSC.CUSTOMER.ID` | `CpMultiStageCustomer_CustomerId` | TField |  | This field stores the customer ID. |
| 3 | `CP.MSC.RUNNING.STATE` | `CpMultiStageCustomer_RunningState` | TField |  | This field stores the Running State of Multi Stage |
| 4 | `CP.MSC.LAST.CAMPAIGN.TRIGGERED` | `CpMultiStageCustomer_LastCampaignTriggered` | TField |  | This field stores the id of the last campaign that was triggered inside the multi stage campaign. |
| 5 | `CP.MSC.LAST.IN.MS.CHAIN` | `CpMultiStageCustomer_LastInMsChain` | TField |  | This field stores true or false based on the position of the campaign in the multi stage. |
| 6 | `CP.MSC.DELAY.EVENT` | `CpMultiStageCustomer_DelayEvent` | TField |  | This field stores the delay event. |
| 7 | `CP.MSC.EVENT.START` | `CpMultiStageCustomer_EventStart` | TField |  | This field stores info about event start. |
| 8 | `CP.MSC.CHANNEL.TYPE` | `CpMultiStageCustomer_ChannelType` | TField |  | This field stores the next followup campaign channel type. |
| 9 | `CP.MSC.RESERVED.20` | `CpMultiStageCustomer_Reserved20` | TField |  |  |
| 10 | `CP.MSC.RESERVED.19` | `CpMultiStageCustomer_Reserved19` | TField |  |  |
| 11 | `CP.MSC.RESERVED.18` | `CpMultiStageCustomer_Reserved18` | TField |  |  |
| 12 | `CP.MSC.RESERVED.17` | `CpMultiStageCustomer_Reserved17` | TField |  |  |
| 13 | `CP.MSC.RESERVED.16` | `CpMultiStageCustomer_Reserved16` | TField |  |  |
| 14 | `CP.MSC.RESERVED.15` | `CpMultiStageCustomer_Reserved15` | TField |  |  |
| 15 | `CP.MSC.RESERVED.14` | `CpMultiStageCustomer_Reserved14` | TField |  |  |
| 16 | `CP.MSC.RESERVED.13` | `CpMultiStageCustomer_Reserved13` | TField |  |  |
| 17 | `CP.MSC.RESERVED.12` | `CpMultiStageCustomer_Reserved12` | TField |  |  |
| 18 | `CP.MSC.RESERVED.11` | `CpMultiStageCustomer_Reserved11` | TField |  |  |
| 19 | `CP.MSC.RESERVED.10` | `CpMultiStageCustomer_Reserved10` | TField |  |  |
| 20 | `CP.MSC.RESERVED.9` | `CpMultiStageCustomer_Reserved9` | TField |  |  |
| 21 | `CP.MSC.RESERVED.8` | `CpMultiStageCustomer_Reserved8` | TField |  |  |
| 22 | `CP.MSC.RESERVED.7` | `CpMultiStageCustomer_Reserved7` | TField |  |  |
| 23 | `CP.MSC.RESERVED.6` | `CpMultiStageCustomer_Reserved6` | TField |  |  |
| 24 | `CP.MSC.RESERVED.5` | `CpMultiStageCustomer_Reserved5` | TField |  |  |
| 25 | `CP.MSC.RESERVED.4` | `CpMultiStageCustomer_Reserved4` | TField |  |  |
| 26 | `CP.MSC.RESERVED.3` | `CpMultiStageCustomer_Reserved3` | TField |  |  |
| 27 | `CP.MSC.RESERVED.2` | `CpMultiStageCustomer_Reserved2` | TField |  |  |
| 28 | `CP.MSC.RESERVED.1` | `CpMultiStageCustomer_Reserved1` | TField |  |  |
| 29 | `CP.MSC.LOCAL.REF` | `CpMultiStageCustomer_LocalRef` |  |  |  |
| 30 | `CP.MSC.OVERRIDE` | `CpMultiStageCustomer_Override` |  |  |  |
| 31 | `CP.MSC.RECORD.STATUS` | `CpMultiStageCustomer_RecordStatus` | String |  |  |
| 32 | `CP.MSC.CURR.NO` | `CpMultiStageCustomer_CurrNo` | String |  |  |
| 33 | `CP.MSC.INPUTTER` | `CpMultiStageCustomer_Inputter` |  |  |  |
| 34 | `CP.MSC.DATE.TIME` | `CpMultiStageCustomer_DateTime` |  |  |  |
| 35 | `CP.MSC.AUTHORISER` | `CpMultiStageCustomer_Authoriser` | String |  |  |
| 36 | `CP.MSC.CO.CODE` | `CpMultiStageCustomer_CoCode` | String |  |  |
| 37 | `CP.MSC.DEPT.CODE` | `CpMultiStageCustomer_DeptCode` | String |  |  |
| 38 | `CP.MSC.AUDITOR.CODE` | `CpMultiStageCustomer_AuditorCode` | String |  |  |
| 39 | `CP.MSC.AUDIT.DATE.TIME` | `CpMultiStageCustomer_AuditDateTime` | String |  |  |
