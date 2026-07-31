# TY.PARAMETER — Table Schema

> Source: `INSERTS/I_F.TY.PARAMETER` in `TY_Parameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TY.PARAM.DESCRIPTION` | `TyParameter_Description` |  |  |  |
| 2 | `TY.PARAM.RATE.SOURCE` | `TyParameter_RateSource` | TField |  | Defines the Rate Source to be used for all rate request from TFO. Validation Rules: Options Allowed: CURRENCY and MARKET.RATE. Default option is CURRENCY |
| 3 | `TY.PARAM.RATE.PROVIDER` | `TyParameter_RateProvider` | TField | Yes | Defines the Rate provider to be used for all rate request from TFO when the Rate source is defined as 'MARKET.RATE'. Validation Rules: Must be a valid record in TY.RATE.PROVIDER. Mandatory input when the RATE.SOURCE is defined as 'MARKET.RATE' |
| 4 | `TY.PARAM.REVAL.CCY` | `TyParameter_RevalCcy` | TField | Yes | Defines the currency in which the Outstanding Positions and Profit and Loss to be represented in TFO. When left blank, the default currency is consider as local currency. Validation Rules: Non-Mandatory field. Must be a valid record in CURRENCY. Meaning description for the definition for the current company. Multivalued Language specific field |
| 5 | `TY.PARAM.EXCEPTION.WORKFLOW` | `TyParameter_ExceptionWorkflow` | TField | No | This field is to indicate whether the bank has opted for exception workflow or not. If set to Y, any exceptions arising from a deal will require an approval from the exception handler before going to the back office. Validation Rules: Optional input. Default value is null. Allowed value is &quot;Y&quot; |
| 6 | `TY.PARAM.DEALER.EQV` | `TyParameter_DealerEqv` | TField | Yes | This field captures the dealer participant. The Dealers pertaining to an input of the deal capture are grouped in PW.PARTICIPANT. The naming of the group in PW.PARTICIPANT for dealers has to be specified here. Validation Rules: Must be a valid record in PW.PARTICIPANT. Mandatory input when EXCEPTION.WORKFLOW is opted by the bank. |
| 7 | `TY.PARAM.CHIEF.DEALER.EQV` | `TyParameter_ChiefDealerEqv` | TField | Yes | This field capture the chief dealer participant. Chief Dealer participant acts as an Exception handler and specifies actions to be executed in response to exceptions. Validation Rules: Must be a valid record in PW.PARTICIPANT. Mandatory input when EXCEPTION.WORKFLOW is turned on. |
| 8 | `TY.PARAM.WHATIF.UPDATE` | `TyParameter_WhatIfUpdate` |  |  |  |
| 9 | `TY.PARAM.RESERVED.6` | `TyParameter_Reserved6` | TField |  | Reserved for future use |
| 10 | `TY.PARAM.RESERVED.5` | `TyParameter_Reserved5` | TField |  | Reserved for future use |
| 11 | `TY.PARAM.RESERVED.4` | `TyParameter_Reserved4` | TField |  | Reserved for future use |
| 12 | `TY.PARAM.RESERVED.3` | `TyParameter_Reserved3` | TField |  | Reserved for future use |
| 13 | `TY.PARAM.RESERVED.2` | `TyParameter_Reserved2` | TField |  | Reserved for future use |
| 14 | `TY.PARAM.RESERVED.1` | `TyParameter_Reserved1` | TField |  | Reserved for future use |
| 15 | `TY.PARAM.LOCAL.REF` | `TyParameter_LocalRef` |  |  |  |
| 16 | `TY.PARAM.OVERRIDE` | `TyParameter_Override` |  |  |  |
| 17 | `TY.PARAM.RECORD.STATUS` | `TyParameter_RecordStatus` | String |  |  |
| 18 | `TY.PARAM.CURR.NO` | `TyParameter_CurrNo` | String |  |  |
| 19 | `TY.PARAM.INPUTTER` | `TyParameter_Inputter` |  |  |  |
| 20 | `TY.PARAM.DATE.TIME` | `TyParameter_DateTime` |  |  |  |
| 21 | `TY.PARAM.AUTHORISER` | `TyParameter_Authoriser` | String |  |  |
| 22 | `TY.PARAM.CO.CODE` | `TyParameter_CoCode` | String |  |  |
| 23 | `TY.PARAM.DEPT.CODE` | `TyParameter_DeptCode` | String |  |  |
| 24 | `TY.PARAM.AUDITOR.CODE` | `TyParameter_AuditorCode` | String |  |  |
| 25 | `TY.PARAM.AUDIT.DATE.TIME` | `TyParameter_AuditDateTime` | String |  |  |
