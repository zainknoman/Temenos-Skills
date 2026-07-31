# CMBASE.ALTERNATE.ID.PARAM — Table Schema

> Source: `INSERTS/I_F.CMBASE.ALTERNATE.ID.PARAM` in `CMBASE_AccountClabe.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ID.PARAM.ALTERNATE.ID` | `CmbaseAlternateIdParam_AlternateId` |  |  |  |
| 2 | `ID.PARAM.BASE.APP.NAME` | `CmbaseAlternateIdParam_BaseAppName` |  |  |  |
| 3 | `ID.PARAM.ALGORITHM` | `CmbaseAlternateIdParam_Algorithm` |  |  |  |
| 4 | `ID.PARAM.FIELD.NAME` | `CmbaseAlternateIdParam_FieldName` |  |  |  |
| 5 | `ID.PARAM.FIELD.FORMAT` | `CmbaseAlternateIdParam_FieldFormat` |  |  |  |
| 6 | `ID.PARAM.ACTIVITY` | `CmbaseAlternateIdParam_Activity` |  |  |  |
| 7 | `ID.PARAM.MODIFY` | `CmbaseAlternateIdParam_Modify` |  |  |  |
| 8 | `ID.PARAM.LOCK.KEYWORD` | `CmbaseAlternateIdParam_LockKeyword` |  |  |  |
| 9 | `ID.PARAM.AC.START.RANGE` | `CmbaseAlternateIdParam_AccStartRange` |  |  |  |
| 10 | `ID.PARAM.AC.END.RANGE` | `CmbaseAlternateIdParam_AccEndRange` |  |  |  |
| 11 | `ID.PARAM.AC.CHECK.DIGIT` | `CmbaseAlternateIdParam_AcCheckDigit` | TField |  | Based on the value in this field, system generates the check digit to be appended to the generate alternate number using Mod10 logic. The number of digits in the Alternate Account Number will be maintained at a maximum of 9 digits if the check digit option is selected. This is because if the check digit option is selected, the number picked up from the range for MOD10 calculation will consist only of 8 digits irrespective of the length of the number maintained. So it is advisable that if the check digit option is selected, the number that is maintained between the start and the end ranges should not exceed 8 digits. If AC.CHECK.DIGIT = "No", then no Check Digit will be appended to the generated number. If AC.CHECK.DIGIT = "Yes", then a MOD10 resultant Check Digit that will be appended to the end of the generated number thus forming the complete Account Number. |
| 12 | `ID.PARAM.RESERVED.5` | `CmbaseAlternateIdParam_Reserved5` | TField |  |  |
| 13 | `ID.PARAM.RESERVED.6` | `CmbaseAlternateIdParam_Reserved6` | TField |  |  |
| 14 | `ID.PARAM.RESERVED.7` | `CmbaseAlternateIdParam_Reserved7` | TField |  |  |
| 15 | `ID.PARAM.RESERVED.8` | `CmbaseAlternateIdParam_Reserved8` | TField |  |  |
| 16 | `ID.PARAM.RESERVED.9` | `CmbaseAlternateIdParam_Reserved9` | TField |  |  |
| 17 | `ID.PARAM.RESERVED.10` | `CmbaseAlternateIdParam_Reserved10` | TField |  |  |
| 18 | `ID.PARAM.RESERVED.11` | `CmbaseAlternateIdParam_Reserved11` | TField |  |  |
| 19 | `ID.PARAM.RESERVED.12` | `CmbaseAlternateIdParam_Reserved12` | TField |  |  |
| 20 | `ID.PARAM.RESERVED.13` | `CmbaseAlternateIdParam_Reserved13` | TField |  |  |
| 21 | `ID.PARAM.RESERVED.14` | `CmbaseAlternateIdParam_Reserved14` | TField |  |  |
| 22 | `ID.PARAM.RESERVED.15` | `CmbaseAlternateIdParam_Reserved15` | TField |  |  |
| 23 | `ID.PARAM.OVERRIDE` | `CmbaseAlternateIdParam_Override` |  |  |  |
| 24 | `ID.PARAM.RECORD.STATUS` | `CmbaseAlternateIdParam_RecordStatus` | String |  | Indicates the record status |
| 25 | `ID.PARAM.CURR.NO` | `CmbaseAlternateIdParam_CurrNo` | String |  | Indicates the number of time record is modified and saved |
| 26 | `ID.PARAM.INPUTTER` | `CmbaseAlternateIdParam_Inputter` |  |  |  |
| 27 | `ID.PARAM.DATE.TIME` | `CmbaseAlternateIdParam_DateTime` |  |  |  |
| 28 | `ID.PARAM.AUTHORISER` | `CmbaseAlternateIdParam_Authoriser` | String |  |  |
| 29 | `ID.PARAM.CO.CODE` | `CmbaseAlternateIdParam_CoCode` | String |  |  |
| 30 | `ID.PARAM.DEPT.CODE` | `CmbaseAlternateIdParam_DeptCode` | String |  |  |
| 31 | `ID.PARAM.AUDITOR.CODE` | `CmbaseAlternateIdParam_AuditorCode` | String |  |  |
| 32 | `ID.PARAM.AUDIT.DATE.TIME` | `CmbaseAlternateIdParam_AuditDateTime` | String |  |  |
