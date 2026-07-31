# AC.IN.EVENT.DATA — Table Schema

> Source: `INSERTS/I_F.AC.IN.EVENT.DATA` in `INCMMS_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.INE.MESSAGE.ID` | `AcInEventData_MessageId` | TField |  | In Message ID. |
| 2 | `AC.INE.IN.MESSAGE.TYPE` | `AcInEventData_InMessageType` | TField |  | In Message Type. |
| 3 | `AC.INE.INSTITUTION` | `AcInEventData_Institution` | TField |  |  |
| 4 | `AC.INE.DISPOSITION` | `AcInEventData_Disposition` | TField |  |  |
| 5 | `AC.INE.FROM.ADDRESS` | `AcInEventData_FromAddress` | TField |  | Address Fields. |
| 6 | `AC.INE.TO.ADDRESS` | `AcInEventData_ToAddress` | TField |  | Address Fields |
| 7 | `AC.INE.CREATION.DT.TIME` | `AcInEventData_CreationDtTime` | TField |  | Date and time of the message creation as set by the sender of the message.. |
| 8 | `AC.INE.DE.I.HEADER.ID` | `AcInEventData_DeIHeaderId` | TField |  | DE.I.HEADER id. |
| 9 | `AC.INE.STATUS` | `AcInEventData_Status` | TField |  | Status of Received Incomming message. |
| 10 | `AC.INE.ERROR.CODE` | `AcInEventData_ErrorCode` | TField |  |  |
| 11 | `AC.INE.ADD.FIELD.NAMES` | `AcInEventData_AddFieldNames` | TField |  | Field names to be mapped from MS to AC.IN.MAPPED.DATA. Eg:RequestedReport:VM:AccountCurrency:AccountOwner:DRFloorLimit:CRFloorLimit. |
| 12 | `AC.INE.ADD.FIELD.VALUES` | `AcInEventData_AddFieldValues` | TField |  | Field values to be mapped from MS to AC.IN.MAPPED.DATA. Eg:CAMT054:VM:USD. |
| 13 | `AC.INE.RESERVED.10` | `AcInEventData_Reserved10` | TField |  |  |
| 14 | `AC.INE.RESERVED.9` | `AcInEventData_Reserved9` | TField |  |  |
| 15 | `AC.INE.RESERVED.8` | `AcInEventData_Reserved8` | TField |  |  |
| 16 | `AC.INE.RESERVED.7` | `AcInEventData_Reserved7` | TField |  |  |
| 17 | `AC.INE.RESERVED.6` | `AcInEventData_Reserved6` | TField |  |  |
| 18 | `AC.INE.RESERVED.5` | `AcInEventData_Reserved5` | TField |  |  |
| 19 | `AC.INE.RESERVED.4` | `AcInEventData_Reserved4` | TField |  |  |
| 20 | `AC.INE.RESERVED.3` | `AcInEventData_Reserved3` | TField |  |  |
| 21 | `AC.INE.RESERVED.2` | `AcInEventData_Reserved2` | TField |  |  |
| 22 | `AC.INE.RESERVED.1` | `AcInEventData_Reserved1` | TField |  |  |
| 23 | `AC.INE.OVERRIDE` | `AcInEventData_Override` |  |  |  |
| 24 | `AC.INE.RECORD.STATUS` | `AcInEventData_RecordStatus` | String |  |  |
| 25 | `AC.INE.CURR.NO` | `AcInEventData_CurrNo` | String |  |  |
| 26 | `AC.INE.INPUTTER` | `AcInEventData_Inputter` |  |  |  |
| 27 | `AC.INE.DATE.TIME` | `AcInEventData_DateTime` |  |  |  |
| 28 | `AC.INE.AUTHORISER` | `AcInEventData_Authoriser` | String |  |  |
| 29 | `AC.INE.CO.CODE` | `AcInEventData_CoCode` | String |  |  |
| 30 | `AC.INE.DEPT.CODE` | `AcInEventData_DeptCode` | String |  |  |
| 31 | `AC.INE.AUDITOR.CODE` | `AcInEventData_AuditorCode` | String |  |  |
| 32 | `AC.INE.AUDIT.DATE.TIME` | `AcInEventData_AuditDateTime` | String |  |  |
