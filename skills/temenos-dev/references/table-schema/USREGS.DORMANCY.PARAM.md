# USREGS.DORMANCY.PARAM — Table Schema

> Source: `INSERTS/I_F.USREGS.DORMANCY.PARAM` in `USREGS_Escheat.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DORM.PRM.DESCRIPTION` | `UsregsDormancyParam_Description` |  |  |  |
| 2 | `DORM.PRM.DEFAULT.STATE` | `UsregsDormancyParam_DefaultState` | TField |  |  |
| 3 | `DORM.PRM.ESCHEATMENT.PERIOD` | `UsregsDormancyParam_EscheatmentPeriod` | TField |  | This attribute will allow the escheatment period in days, months and years. The escheatment evaluation would be performed depending on the value defined in this field. In case the account do not have any account related activities on any of the accounts or deposits of the primary customer or joint customers the account will be flagged as pending escheatment account . The account will also be added to the list to be evaluated on the cut-off date. |
| 4 | `DORM.PRM.CUTOFF.DATE` | `UsregsDormancyParam_CutoffDate` | TField |  | This field accepts the cut-off date of escheatment in the format 'MMDD'. All pending escheatment accounts / deposits will be again evaluated on the cut-off date to check if the account/deposit is still eligible for escheatment. In case there is any customer contact or account activity in any of the related accounts of the customers of this account, the account will be moved to the earlier dormancy status. In case the account is still eligible for escheatment then filing date for the state is arrived and then the final escheatment evaluation is scheduled. |
| 5 | `DORM.PRM.FILING.DATE` | `UsregsDormancyParam_FilingDate` | TField |  | This field will accepts the filing date of escheated account / Deposits in the format 'MMDD'. The funds will be moved to the state on this date. The format of the date entered here will be MMDD. On the filing date the evaluation will be again performed to check if the account can be escheated. In case there is any customer contact or account activity in any of the related accounts of the customers of this account , the account will be moved to the earlier dormancy status .If the account is still eligible for escheatment then the funds will be moved the offset account specified in the default record in dormancy parameter. |
| 6 | `DORM.PRM.AUTO.CLOSE.IND` | `UsregsDormancyParam_AutoCloseInd` | TField |  | This will be a 'Y' or blank. In case the value is 'Y' then the account will be set to auto close on the filing date after the funds have been transferred to the offset account. |
| 7 | `DORM.PRM.OFFSET.ACCOUNT` | `UsregsDormancyParam_OffsetAccount` | TField | Conditional | Optional for product line .This field will be mandatory when the AUTO.CLOSE.IND is set to 'Y'. This is the account that will be credited with the money when escheated account is auto closed. |
| 8 | `DORM.PRM.ACTIVITY.CLASS` | `UsregsDormancyParam_ActivityClass` |  |  |  |
| 9 | `DORM.PRM.ACTIVITY.NAME` | `UsregsDormancyParam_ActivityName` |  |  |  |
| 10 | `DORM.PRM.INCLUDE.INDICATOR` | `UsregsDormancyParam_IncludeIndicator` |  |  |  |
| 11 | `DORM.PRM.OVERRIDE.RTN` | `UsregsDormancyParam_OverrideRtn` |  |  |  |
| 12 | `DORM.PRM.RESERVED.20` | `UsregsDormancyParam_Reserved20` |  |  |  |
| 13 | `DORM.PRM.RESERVED.19` | `UsregsDormancyParam_Reserved19` |  |  |  |
| 14 | `DORM.PRM.STATUS` | `UsregsDormancyParam_Status` |  |  |  |
| 15 | `DORM.PRM.EXCEPTION.RULE` | `UsregsDormancyParam_ExceptionRule` |  |  |  |
| 16 | `DORM.PRM.EXCEPTION.API` | `UsregsDormancyParam_ExceptionApi` |  |  |  |
| 17 | `DORM.PRM.PERIOD` | `UsregsDormancyParam_Period` |  |  |  |
| 18 | `DORM.PRM.RESERVED.17` | `UsregsDormancyParam_Reserved17` |  |  |  |
| 19 | `DORM.PRM.RESERVED.16` | `UsregsDormancyParam_Reserved16` |  |  |  |
| 20 | `DORM.PRM.ALLOW.ACTIVITY` | `UsregsDormancyParam_AllowActivity` |  |  |  |
| 21 | `DORM.PRM.ALLOW.ACTIVITY.CLASS` | `UsregsDormancyParam_AllowActivityClass` |  |  |  |
| 22 | `DORM.PRM.WAIVE.DORMANT.CHARGE` | `UsregsDormancyParam_WaiveDormantCharge` | TField |  | Field to indicate whether the dormant charge is applied for that state. Valid values are Y &lt; null. If the value is Y then system will waive dormancy charge. |
| 23 | `DORM.PRM.RENEW.CD.ESCHEAT.PRD` | `UsregsDormancyParam_RenewCdEscheatPrd` | TField |  |  |
| 24 | `DORM.PRM.DEATH.ESCHEAT.PRD` | `UsregsDormancyParam_DeathEscheatPrd` | TField |  |  |
| 25 | `DORM.PRM.BAD.ADDRESS.CHK` | `UsregsDormancyParam_BadAddressChk` | TField |  |  |
| 26 | `DORM.PRM.CEASE.BENEFITS` | `UsregsDormancyParam_CeaseBenefits` | TField |  |  |
| 27 | `DORM.PRM.MAJORITY.AGE` | `UsregsDormancyParam_MajorityAge` | TField |  | This field defines age of majority in the state. Numeric, 2 digit. |
| 28 | `DORM.PRM.MINOR.ESCHEAT.RULE` | `UsregsDormancyParam_MinorEscheatRule` | TField | Yes | Allowed values: YES/NO. If Yes is selected, it indicates that special pre-escheatment scheduling for minors is required in the state. If MINOR.ESCHEAT.RULE equals Yes then MINOR.ESCHEAT.PERIOD becomes a mandatory field. |
| 29 | `DORM.PRM.MINOR.ESCHEAT.PERIOD` | `UsregsDormancyParam_MinorEscheatPeriod` | TField | Yes | This field defines escheatment period that needs to be used for scheduling pre-escheatment evaluation of minor accounts It becomes mandatory if MINOR.ESCHEAT.RULE equals Yes. Field allows escheatment period definition in days, months and years |
| 30 | `DORM.PRM.CUSTODIAN.ROLE` | `UsregsDormancyParam_CustodianRole` | TField |  | This field is used to define guardian's role for the states customer's role that which guardian's/custodian's "bad" address processing is required. It has a dropdown attached listing records available in AA.CUSTOMER.ROLE, Attached dropdown also has NULL value, which once selected indicates that "bad" address processing is not required. If this field is left blank and MINOR.ESCHEAT.RULE equals Yes, then system will generate an override message. |
| 31 | `DORM.PRM.RELOCATION.TRACKING` | `UsregsDormancyParam_RelocationTracking` | TField | Yes | This field is used to distinguish if particular state in case of customer's move to such state honours age of majority of the state, which account was opened in or if it follows its' own age of majority. Allowed values:PREVIOUS.STATE, CURRENT.RESIDENCE Previous State: age of majority � if it selected then it will indicate that in case of minor customer's move to such state, system should consider age of majority of the state, which account was opened in. Current Residence: age of majority - if it selected then it will indicate that in case of minor customer's move to such state, system should consider age of majority of new residence None: It becomes mandatory if MINOR.ESCHEAT.RULE equals Yes. |
| 32 | `DORM.PRM.RESERVED.5` | `UsregsDormancyParam_Reserved5` | TField |  |  |
| 33 | `DORM.PRM.RESERVED.4` | `UsregsDormancyParam_Reserved4` | TField |  |  |
| 34 | `DORM.PRM.RESERVED.3` | `UsregsDormancyParam_Reserved3` | TField |  |  |
| 35 | `DORM.PRM.RESERVED.2` | `UsregsDormancyParam_Reserved2` | TField |  |  |
| 36 | `DORM.PRM.RESERVED.1` | `UsregsDormancyParam_Reserved1` | TField |  |  |
| 37 | `DORM.PRM.LOCAL.REF` | `UsregsDormancyParam_LocalRef` |  |  |  |
| 38 | `DORM.PRM.OVERRIDE` | `UsregsDormancyParam_Override` |  |  |  |
| 39 | `DORM.PRM.RECORD.STATUS` | `UsregsDormancyParam_RecordStatus` | String |  |  |
| 40 | `DORM.PRM.CURR.NO` | `UsregsDormancyParam_CurrNo` | String |  |  |
| 41 | `DORM.PRM.INPUTTER` | `UsregsDormancyParam_Inputter` |  |  |  |
| 42 | `DORM.PRM.DATE.TIME` | `UsregsDormancyParam_DateTime` |  |  |  |
| 43 | `DORM.PRM.AUTHORISER` | `UsregsDormancyParam_Authoriser` | String |  |  |
| 44 | `DORM.PRM.CO.CODE` | `UsregsDormancyParam_CoCode` | String |  |  |
| 45 | `DORM.PRM.DEPT.CODE` | `UsregsDormancyParam_DeptCode` | String |  |  |
| 46 | `DORM.PRM.AUDITOR.CODE` | `UsregsDormancyParam_AuditorCode` | String |  |  |
| 47 | `DORM.PRM.AUDIT.DATE.TIME` | `UsregsDormancyParam_AuditDateTime` | String |  |  |
