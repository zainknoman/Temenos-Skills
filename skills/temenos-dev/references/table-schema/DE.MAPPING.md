# DE.MAPPING — Table Schema

> Source: `INSERTS/I_F.DE.MAPPING` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.MAP.DESCRIPTION` | `DeMapping_Description` |  |  |  |
| 2 | `DE.MAP.INPUT.REC.NO` | `DeMapping_InputRecNo` |  |  |  |
| 3 | `DE.MAP.INPUT.REC.DESC` | `DeMapping_InputRecDesc` |  |  |  |
| 4 | `DE.MAP.INPUT.FILE` | `DeMapping_InputFile` |  |  |  |
| 5 | `DE.MAP.INPUT.POSITION` | `DeMapping_InputPosition` |  |  |  |
| 6 | `DE.MAP.INPUT.NAME` | `DeMapping_InputName` |  |  |  |
| 7 | `DE.MAP.FIELD.DESCR` | `DeMapping_FieldDescr` |  |  |  |
| 8 | `DE.MAP.FIELD.NAME` | `DeMapping_FieldName` |  |  |  |
| 9 | `DE.MAP.HEADER.NAME` | `DeMapping_HeaderName` |  |  |  |
| 10 | `DE.MAP.USR.INPUT.POS` | `DeMapping_UsrInputPos` |  |  |  |
| 11 | `DE.MAP.USR.INPUT.NAME` | `DeMapping_UsrInputName` |  |  |  |
| 12 | `DE.MAP.USR.FLD.DESC` | `DeMapping_UsrFldDesc` |  |  |  |
| 13 | `DE.MAP.USR.FLD.NAME` | `DeMapping_UsrFldName` |  |  |  |
| 14 | `DE.MAP.RESERVED.11` | `DeMapping_Reserved11` |  |  |  |
| 15 | `DE.MAP.HEADER.POSITION` | `DeMapping_HeaderPosition` |  |  |  |
| 16 | `DE.MAP.ROUTINE` | `DeMapping_Routine` | TField |  | This field is used to call a user defined routine/method to map additional data which is not normally available for the message type. The routine is passed all nine of the handoff records in a DIMensioned array and the MAPPING.KEY as the tenth element of the DIMensioned array as the first argument and a null in the second argument, which is used as a return error message. If there is a value in the second value on return from the routine the mapping does not proceed and the error message is handed back to the calling application. If all the records are blanked by the call to the user routine the mapping process does not proceed and an error returned to the calling application. Specify either a jBC subroutine name or a valid java method must have a entry on EB.API with source type as METHOD which implements an interface defined in the EB.API record HOOK.DE.MAPPING.ROUTINE. See the EB.API record HOOK.DE.MAPPING.ROUTINE for the list of supported interface. Initially DE.DeliveryHook.mapAdditionalDataToMessageType interface provided to support this functionality in java. For example there is a routine DE.DISP.MSG which does a "Print Preview" of the Printed and Swift message on the screen and can be set up in the DE.MAPPING record in case the user wishes to see the printed and Swift output prior to committing the transaction. Validation Rules: If local development has to do with the JBC Implementation: i)Up to 30 alphanumeric characters, of which the first must be an '@' character. ii)The routine must be cataloged and in the UniVerse VOC file. The routine itself should be specified as : EXAMPLE.ROUTINE(MAT EXAMPLE.REC, ERR.MSG) If local development has to do with the Java Implementation: i) Valid java method must have a entry on EB.API with source type METHOD which implements an interface. |
| 17 | `DE.MAP.AC.FIELD` | `DeMapping_AcField` |  |  |  |
| 18 | `DE.MAP.AC.CURRENCY` | `DeMapping_AcCurrency` |  |  |  |
| 19 | `DE.MAP.AC.AMOUNT` | `DeMapping_AcAmount` |  |  |  |
| 20 | `DE.MAP.ERI.CODE` | `DeMapping_EriCode` |  |  |  |
| 21 | `DE.MAP.RECORD.NAME.LOC` | `DeMapping_RecordNameLoc` | TField |  | The location of the record name in the raw message data passed to delivery |
| 22 | `DE.MAP.RESERVED.7` | `DeMapping_Reserved7` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 23 | `DE.MAP.RESERVED.6` | `DeMapping_Reserved6` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 24 | `DE.MAP.RESERVED.5` | `DeMapping_Reserved5` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 25 | `DE.MAP.RESERVED.4` | `DeMapping_Reserved4` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 26 | `DE.MAP.RESERVED.3` | `DeMapping_Reserved3` | TField |  | This field is reserved for future expansion. Validation Rules: This is a NOINPUT field. |
| 27 | `DE.MAP.LOCAL.REF` | `DeMapping_LocalRef` |  |  |  |
| 28 | `DE.MAP.OVERRIDE` | `DeMapping_Override` |  |  |  |
| 29 | `DE.MAP.RECORD.STATUS` | `DeMapping_RecordStatus` | String |  |  |
| 30 | `DE.MAP.CURR.NO` | `DeMapping_CurrNo` | String |  |  |
| 31 | `DE.MAP.INPUTTER` | `DeMapping_Inputter` |  |  |  |
| 32 | `DE.MAP.DATE.TIME` | `DeMapping_DateTime` |  |  |  |
| 33 | `DE.MAP.AUTHORISER` | `DeMapping_Authoriser` | String |  |  |
| 34 | `DE.MAP.CO.CODE` | `DeMapping_CoCode` | String |  |  |
| 35 | `DE.MAP.DEPT.CODE` | `DeMapping_DeptCode` | String |  |  |
| 36 | `DE.MAP.AUDITOR.CODE` | `DeMapping_AuditorCode` | String |  |  |
| 37 | `DE.MAP.AUDIT.DATE.TIME` | `DeMapping_AuditDateTime` | String |  |  |
| 38 | `DE.MAP.GEN.HDR.META.DATA` | `DeMapping_GenHdrMetaData` |  |  |  |
| 39 | `DE.MAP.BUS.HDR.META.DATA` | `DeMapping_BusHdrMetaData` |  |  |  |
| 40 | `DE.MAP.INPUT.MDAL.METHOD` | `DeMapping_InputMdalMethod` |  |  |  |
| 41 | `DE.MAP.INPUT.MDAL.ARGUMENTS` | `DeMapping_InputMdalArguments` |  |  |  |
