# INT.MOVEMENT.PARAM — Table Schema

> Source: `INSERTS/I_F.INT.MOVEMENT.PARAM` in `AC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.IMP.DESCRIPTION` | `IntMovementParam_Description` |  |  |  |
| 2 | `AC.IMP.TAX.YEAR.START` | `IntMovementParam_TaxYearStart` | TField |  | Defines the date from which the Tax year starts. The date input in this field is checked when the Interest and Tax movements are extracted. Any Interest or Tax movement that is dated prior to this date will not be extracted into the INT.MOVEMENT file. Validation Rules: Any valid date is allowed. |
| 3 | `AC.IMP.TAX.YEAR.END` | `IntMovementParam_TaxYearEnd` | TField |  | Defines the date on which the Tax year ends. The date input in this field is used to determine if an Interest or Tax entry is to be extracted into the file F.INT.MOVEMENT. Validation Rules: Any valid date is allowed. |
| 4 | `AC.IMP.PURGE.DATE` | `IntMovementParam_PurgeDate` | TField |  | Specifies the date after which data from the INT.MOVEMENT file will be purged. Any Interest or Tax entry in the file F.INT.MOVEMENT that is prior to the date in this field will be purged by the system. Validation Rules: Any valid date is allowed. |
| 5 | `AC.IMP.DATE.TO.USE` | `IntMovementParam_DateToUse` | TField | Yes | Defines if the Booking Date ot the Value date is to be used as the key of the extracted information. The details of Interest and Tax movements are extracted and stored in the file F.INT.MOVEMENT with a Key of "Deal ID - Date". The "date" on this Key can be either the Booking date or the Value date of the entry depending on the Value of this field. When the Tax returns are produced the date in the Key of the file INT.MOVEMENT is used to determine if that record has to be included in the returns or not. Validation Rules: Mandatory field. Can have the value "BOOKING.DATE" or "VALUE.DATE". The contents of this field can not be changed after authorisation. |
| 6 | `AC.IMP.SYSTEM.ID` | `IntMovementParam_SystemId` |  |  |  |
| 7 | `AC.IMP.GROSS.NET.INT` | `IntMovementParam_GrossNetInt` |  |  |  |
| 8 | `AC.IMP.DR.INT.CODES` | `IntMovementParam_DrIntCodes` |  |  |  |
| 9 | `AC.IMP.DR.ENT.TYPE` | `IntMovementParam_DrEntType` |  |  |  |
| 10 | `AC.IMP.DR.INT.PL` | `IntMovementParam_DrIntPl` |  |  |  |
| 11 | `AC.IMP.CR.INT.CODES` | `IntMovementParam_CrIntCodes` |  |  |  |
| 12 | `AC.IMP.CR.ENT.TYPE` | `IntMovementParam_CrEntType` |  |  |  |
| 13 | `AC.IMP.CR.INT.PL` | `IntMovementParam_CrIntPl` |  |  |  |
| 14 | `AC.IMP.TAX.CODES` | `IntMovementParam_TaxCodes` |  |  |  |
| 15 | `AC.IMP.ADJ.CODES` | `IntMovementParam_AdjCodes` |  |  |  |
| 16 | `AC.IMP.CRF.TXN.CODE` | `IntMovementParam_CrfTxnCode` |  |  |  |
| 17 | `AC.IMP.RESERVED.4` | `IntMovementParam_Reserved4` |  |  |  |
| 18 | `AC.IMP.RESERVED.3` | `IntMovementParam_Reserved3` |  |  |  |
| 19 | `AC.IMP.RESERVED.2` | `IntMovementParam_Reserved2` |  |  |  |
| 20 | `AC.IMP.RESERVED.1` | `IntMovementParam_Reserved1` |  |  |  |
| 21 | `AC.IMP.TAX.LAST.RUN` | `IntMovementParam_TaxLastRun` |  |  |  |
| 22 | `AC.IMP.MVMT.BY.COMP` | `IntMovementParam_MvmtByComp` | TField |  | This field is to specify whether company mnemonic should be added to the ID or not for the files INT.MOVEMENT, TX.INT.MOVEMENT.DATE &amp; TX.SEC.TXN.LIST Validation Rules: A maximum of 3 characters may be entered. The following values are permitted: YES NO |
| 23 | `AC.IMP.RESERVED5` | `IntMovementParam_Reserved5` | TField |  |  |
| 24 | `AC.IMP.RESERVED4` | `IntMovementParam_Reserved4` |  |  |  |
| 25 | `AC.IMP.RESERVED3` | `IntMovementParam_Reserved3` |  |  |  |
| 26 | `AC.IMP.LOCAL.REF` | `IntMovementParam_LocalRef` |  |  |  |
| 27 | `AC.IMP.OVERRIDE` | `IntMovementParam_Override` |  |  |  |
| 28 | `AC.IMP.RECORD.STATUS` | `IntMovementParam_RecordStatus` | String |  |  |
| 29 | `AC.IMP.CURR.NO` | `IntMovementParam_CurrNo` | String |  |  |
| 30 | `AC.IMP.INPUTTER` | `IntMovementParam_Inputter` |  |  |  |
| 31 | `AC.IMP.DATE.TIME` | `IntMovementParam_DateTime` |  |  |  |
| 32 | `AC.IMP.AUTHORISER` | `IntMovementParam_Authoriser` | String |  |  |
| 33 | `AC.IMP.CO.CODE` | `IntMovementParam_CoCode` | String |  |  |
| 34 | `AC.IMP.DEPT.CODE` | `IntMovementParam_DeptCode` | String |  |  |
| 35 | `AC.IMP.AUDITOR.CODE` | `IntMovementParam_AuditorCode` | String |  |  |
| 36 | `AC.IMP.AUDIT.DATE.TIME` | `IntMovementParam_AuditDateTime` | String |  |  |
