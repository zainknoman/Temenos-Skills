# CAPL.CARD.GEN.MSG — Table Schema

> Source: `INSERTS/I_F.CAPL.CARD.GEN.MSG` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CRD.MSG.CHANNEL` | `CaplCardGenMsg_Channel` |  |  |  |
| 2 | `CRD.MSG.REQUEST` | `CaplCardGenMsg_Request` |  |  |  |
| 3 | `CRD.MSG.ONLINE.UPD` | `CaplCardGenMsg_OnlineUpd` |  |  |  |
| 4 | `CRD.MSG.LOCAL.PIN.EXP.TIME` | `CaplCardGenMsg_LocalPinExpTime` | TField |  | This field is used to define the pin expirt time for PIN update. Based on the time defined here PIN window will remain open until that time.Valid record from EB.LOOKUP table.Ex. CAPL.PIN.EXP.TIME*1H Validation Rules: Length 35 Type Any |
| 5 | `CRD.MSG.WINDOW.EXPIRY` | `CaplCardGenMsg_WindowExpiry` | TField |  | The purpose of this field is used to store the pin expiry winodw.Allowed values are 35 alphanumeric characters.Ex. 2021-05-27 13:03 Validation Rules: Length 35 Type Any |
| 6 | `CRD.MSG.PIN.EXP.TIM` | `CaplCardGenMsg_PinExpTim` | TField |  | TThis field will be updated upond defining the time in LOCAL.PIN.EXP.TIME field.Allowed values are 5 alphanumeric characters.Ex. 1H Validation Rules: Length 5 Type Alphanumeric |
| 7 | `CRD.MSG.PRE.EXP.TIM` | `CaplCardGenMsg_PreExpTim` | TField |  | This field will capture the pre expiry time for the pin expiry time. This will store the remaining time of pin windo expiry time.Allowed value are 5 alphanumeric characters.Ex. 10S Validation Rules: Length 5 Type Alphanumeric |
| 8 | `CRD.MSG.PIN.MSG` | `CaplCardGenMsg_PinMsg` | TField |  | This field will capture the pin message.Allowed value are 60 alphanumeric characters.Ex. 10S Validation Rules: Length 60 Type Alphanumeric |
| 9 | `CRD.MSG.UPD.DATE.TIME` | `CaplCardGenMsg_UpdDateTime` |  |  |  |
| 10 | `CRD.MSG.NOTES` | `CaplCardGenMsg_Notes` | TField |  | The purpose of this field is used to define the additional information during the PIN window updation. This information will he sent as notes in the FHm message during the PIN window updation.Allowed values are 60 alphanumeric charactersEx. ATM PIN CHANGE Validation Rules: Length 60 Type Alphanumeric |
| 11 | `CRD.MSG.RESERVED.4` | `CaplCardGenMsg_Reserved4` | TField |  |  |
| 12 | `CRD.MSG.RESERVED.3` | `CaplCardGenMsg_Reserved3` | TField |  |  |
| 13 | `CRD.MSG.RESERVED.2` | `CaplCardGenMsg_Reserved2` | TField |  |  |
| 14 | `CRD.MSG.RESERVED.1` | `CaplCardGenMsg_Reserved1` | TField |  |  |
| 15 | `CRD.MSG.LOCAL.REF` | `CaplCardGenMsg_LocalRef` |  |  |  |
| 16 | `CRD.MSG.OVERRIDE` | `CaplCardGenMsg_Override` |  |  |  |
| 17 | `CRD.MSG.RECORD.STATUS` | `CaplCardGenMsg_RecordStatus` | String |  |  |
| 18 | `CRD.MSG.CURR.NO` | `CaplCardGenMsg_CurrNo` | String |  |  |
| 19 | `CRD.MSG.INPUTTER` | `CaplCardGenMsg_Inputter` |  |  |  |
| 20 | `CRD.MSG.DATE.TIME` | `CaplCardGenMsg_DateTime` |  |  |  |
| 21 | `CRD.MSG.AUTHORISER` | `CaplCardGenMsg_Authoriser` | String |  |  |
| 22 | `CRD.MSG.CO.CODE` | `CaplCardGenMsg_CoCode` | String |  |  |
| 23 | `CRD.MSG.DEPT.CODE` | `CaplCardGenMsg_DeptCode` | String |  |  |
| 24 | `CRD.MSG.AUDITOR.CODE` | `CaplCardGenMsg_AuditorCode` | String |  |  |
| 25 | `CRD.MSG.AUDIT.DATE.TIME` | `CaplCardGenMsg_AuditDateTime` | String |  |  |
