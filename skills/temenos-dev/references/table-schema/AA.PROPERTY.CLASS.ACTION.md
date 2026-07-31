# AA.PROPERTY.CLASS.ACTION — Table Schema

> Source: `INSERTS/I_F.AA.PROPERTY.CLASS.ACTION` in `AA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PCA.FULL.DESCRIPTION` | `AaPropertyClassAction_FullDescription` |  |  |  |
| 2 | `AA.PCA.SHORT.DESC` | `AaPropertyClassAction_ShortDesc` |  |  |  |
| 3 | `AA.PCA.PRODUCT.LINE` | `AaPropertyClassAction_ProductLine` |  |  |  |
| 4 | `AA.PCA.ACCOUNTING` | `AaPropertyClassAction_Accounting` |  |  |  |
| 5 | `AA.PCA.PROPERTY.CLASS` | `AaPropertyClassAction_PropertyClass` | TField |  | Contains the Property class of ID component |
| 6 | `AA.PCA.ACTION` | `AaPropertyClassAction_Action` | TField |  | An Action is performed on a property of the specified class as part of a business Activity. The actions that comprise an activity will depend upon the property, product line and type of business event being processed. Examples of ACTIONS are ACCRUE, CALCULATE, CHANGE, DECREASE, DISBURSE, DRAW, INCREASE and UPDATE. The actions available will depend on the property class and its behaviour. |
| 7 | `AA.PCA.RESERVED.10` | `AaPropertyClassAction_Reserved10` | TField |  |  |
| 8 | `AA.PCA.RESERVED.9` | `AaPropertyClassAction_Reserved9` | TField |  |  |
| 9 | `AA.PCA.RESERVED.8` | `AaPropertyClassAction_Reserved8` | TField |  |  |
| 10 | `AA.PCA.RESERVED.7` | `AaPropertyClassAction_Reserved7` | TField |  |  |
| 11 | `AA.PCA.RESERVED.6` | `AaPropertyClassAction_Reserved6` | TField |  |  |
| 12 | `AA.PCA.RESERVED.5` | `AaPropertyClassAction_Reserved5` | TField |  |  |
| 13 | `AA.PCA.RESERVED.4` | `AaPropertyClassAction_Reserved4` | TField |  |  |
| 14 | `AA.PCA.PARTICIPANT.PROCESS` | `AaPropertyClassAction_ParticipantProcess` | TField |  |  |
| 15 | `AA.PCA.ENABLE.GUARD.METHOD` | `AaPropertyClassAction_EnableGuardMethod` | TField |  | If the flag is set, then before executing an action system will trigger a guard method which will indicate to the system that whether we need to execute this particular action or not. This will be used to trigger an action only if it is need. Released and maintained by Temenos. |
| 16 | `AA.PCA.OVERRIDE` | `AaPropertyClassAction_Override` |  |  |  |
| 17 | `AA.PCA.RECORD.STATUS` | `AaPropertyClassAction_RecordStatus` | String |  |  |
| 18 | `AA.PCA.CURR.NO` | `AaPropertyClassAction_CurrNo` | String |  |  |
| 19 | `AA.PCA.INPUTTER` | `AaPropertyClassAction_Inputter` |  |  |  |
| 20 | `AA.PCA.DATE.TIME` | `AaPropertyClassAction_DateTime` |  |  |  |
| 21 | `AA.PCA.AUTHORISER` | `AaPropertyClassAction_Authoriser` | String |  |  |
| 22 | `AA.PCA.CO.CODE` | `AaPropertyClassAction_CoCode` | String |  |  |
| 23 | `AA.PCA.DEPT.CODE` | `AaPropertyClassAction_DeptCode` | String |  |  |
| 24 | `AA.PCA.AUDITOR.CODE` | `AaPropertyClassAction_AuditorCode` | String |  |  |
| 25 | `AA.PCA.AUDIT.DATE.TIME` | `AaPropertyClassAction_AuditDateTime` | String |  |  |
