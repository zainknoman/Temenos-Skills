# LENREN.RENEWAL.REJECT.PARAM — Table Schema

> Source: `INSERTS/I_F.LENREN.RENEWAL.REJECT.PARAM` in `LENREN_Renewal.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `REJ.PARAM.DESCRIPTION` | `LenrenRenewalRejectParam_Description` | TField |  | This field Holds the some valid description for the record created. |
| 2 | `REJ.PARAM.APPLICATION` | `LenrenRenewalRejectParam_Application` |  |  |  |
| 3 | `REJ.PARAM.APPL.ID` | `LenrenRenewalRejectParam_ApplId` |  |  |  |
| 4 | `REJ.PARAM.AA.CONDITION` | `LenrenRenewalRejectParam_AaCondition` |  |  |  |
| 5 | `REJ.PARAM.FLD.NAME` | `LenrenRenewalRejectParam_FldName` |  |  |  |
| 6 | `REJ.PARAM.FLD.OPERAND` | `LenrenRenewalRejectParam_FldOperand` |  |  |  |
| 7 | `REJ.PARAM.FLD.VALUE` | `LenrenRenewalRejectParam_FldValue` |  |  |  |
| 8 | `REJ.PARAM.RESERVED.15` | `LenrenRenewalRejectParam_Reserved15` |  |  |  |
| 9 | `REJ.PARAM.RESERVED.14` | `LenrenRenewalRejectParam_Reserved14` |  |  |  |
| 10 | `REJ.PARAM.RESERVED.13` | `LenrenRenewalRejectParam_Reserved13` |  |  |  |
| 11 | `REJ.PARAM.RESERVED.12` | `LenrenRenewalRejectParam_Reserved12` |  |  |  |
| 12 | `REJ.PARAM.RESERVED.11` | `LenrenRenewalRejectParam_Reserved11` |  |  |  |
| 13 | `REJ.PARAM.CONNECTOR` | `LenrenRenewalRejectParam_Connector` |  |  |  |
| 14 | `REJ.PARAM.CONV.ROUTINE` | `LenrenRenewalRejectParam_ConvRoutine` | TField |  | This field accepts a user-defined subroutine or an EB.API record of type METHOD which implements an interface defined in the EB.API record LENREN.RENEWAL.REJ.PAR.CNV.RTN.HOOK.Using this rourine , the Value(Boolean value 1 or 0) derived the routine will be considered for Rejection or pricing scenario generationA jBC subroutine name:The routine has single argument acting as both Incoming and outgoing, Arrangement id will passed as incoming and system expects outgoing as 1 or 0 boolean valueFor java implementations: An EB.API record id with a source type of HOOK which implements an interface defined in the EB.API record LENREN.RENEWAL.REJ.PAR.CNV.RTN.HOOK.The LoanRenewal class is in the hook.countrymodelbank.canada.LoanRenewal package which is in LENREN_LoanRenewalHook.jar shipped with T24.Incoming argument - loan account numberOutgoing argument - Boolean value of 1 or 01 - Pricing scenarios will not be generated0 - Pricing scenarios will be generatedValidation Rules:The routine entered should exist in EB.API record with type as 'BASIC' or of type METHOD |
| 15 | `REJ.PARAM.TRIGGER.ACTIVITY` | `LenrenRenewalRejectParam_TriggerActivity` | TField |  | Field is used to trigger an activity an primary purpose is for Buyback of loan in case of securitized loan.Validation: Activity triggers whenever an update activity happened based on LENREN.AUTO.RENEW.PARAMApplicable for Securitized Loans.Note: Effective date of the activity is based on DATE.TO.APPLY field in LENREN.AUTO.RENEW.PARAM. This activity will trigger for each update in LENREN.AUTO.RENEW.PARAMValidation: Records from AA.ACTIVITY |
| 16 | `REJ.PARAM.RESERVED.10` | `LenrenRenewalRejectParam_Reserved10` | TField |  |  |
| 17 | `REJ.PARAM.RESERVED.9` | `LenrenRenewalRejectParam_Reserved9` | TField |  |  |
| 18 | `REJ.PARAM.RESERVED.8` | `LenrenRenewalRejectParam_Reserved8` | TField |  |  |
| 19 | `REJ.PARAM.RESERVED.7` | `LenrenRenewalRejectParam_Reserved7` | TField |  |  |
| 20 | `REJ.PARAM.RESERVED.6` | `LenrenRenewalRejectParam_Reserved6` | TField |  |  |
| 21 | `REJ.PARAM.RESERVED.5` | `LenrenRenewalRejectParam_Reserved5` | TField |  |  |
| 22 | `REJ.PARAM.RESERVED.4` | `LenrenRenewalRejectParam_Reserved4` | TField |  |  |
| 23 | `REJ.PARAM.RESERVED.3` | `LenrenRenewalRejectParam_Reserved3` | TField |  |  |
| 24 | `REJ.PARAM.RESERVED.2` | `LenrenRenewalRejectParam_Reserved2` | TField |  |  |
| 25 | `REJ.PARAM.RESERVED.1` | `LenrenRenewalRejectParam_Reserved1` | TField |  |  |
| 26 | `REJ.PARAM.LOCAL.REF` | `LenrenRenewalRejectParam_LocalRef` |  |  |  |
| 27 | `REJ.PARAM.OVERRIDE` | `LenrenRenewalRejectParam_Override` |  |  |  |
| 28 | `REJ.PARAM.RECORD.STATUS` | `LenrenRenewalRejectParam_RecordStatus` | String |  |  |
| 29 | `REJ.PARAM.CURR.NO` | `LenrenRenewalRejectParam_CurrNo` | String |  |  |
| 30 | `REJ.PARAM.INPUTTER` | `LenrenRenewalRejectParam_Inputter` |  |  |  |
| 31 | `REJ.PARAM.DATE.TIME` | `LenrenRenewalRejectParam_DateTime` |  |  |  |
| 32 | `REJ.PARAM.AUTHORISER` | `LenrenRenewalRejectParam_Authoriser` | String |  |  |
| 33 | `REJ.PARAM.CO.CODE` | `LenrenRenewalRejectParam_CoCode` | String |  |  |
| 34 | `REJ.PARAM.DEPT.CODE` | `LenrenRenewalRejectParam_DeptCode` | String |  |  |
| 35 | `REJ.PARAM.AUDITOR.CODE` | `LenrenRenewalRejectParam_AuditorCode` | String |  |  |
| 36 | `REJ.PARAM.AUDIT.DATE.TIME` | `LenrenRenewalRejectParam_AuditDateTime` | String |  |  |
