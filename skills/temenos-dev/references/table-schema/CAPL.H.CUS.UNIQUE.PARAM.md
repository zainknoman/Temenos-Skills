# CAPL.H.CUS.UNIQUE.PARAM — Table Schema

> Source: `INSERTS/I_F.CAPL.H.CUS.UNIQUE.PARAM` in `CABASE_CustomerRelation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.CUP.DESCRIPTION` | `CaplHCusUniqueParam_Description` |  |  |  |
| 2 | `CAPL.CUP.CUS.TYPE` | `CaplHCusUniqueParam_CusType` | TField |  |  |
| 3 | `CAPL.CUP.UNIQUE.FIELD` | `CaplHCusUniqueParam_UniqueField` | TField |  | This field is used to validate field of customer record.NOCHANGE fieldDefault validation is based on SIN.NO |
| 4 | `CAPL.CUP.CUS.REL.CODE` | `CaplHCusUniqueParam_CusRelCode` |  |  |  |
| 5 | `CAPL.CUP.CUS.RELATION` | `CaplHCusUniqueParam_CusRelation` |  |  |  |
| 6 | `CAPL.CUP.CUS.UNIQUE.MESS.TYPE` | `CaplHCusUniqueParam_CusUniqueMessType` | TField |  | The purpose fo the field is used to define the message type as error or override.Allowed values are Eb.error/OverrideIf Eb.error is selected then the message will be thrown as an error.If Override is selected then the message will be thrown as an override. |
| 7 | `CAPL.CUP.UNIQUE.MESSAGE.ID` | `CaplHCusUniqueParam_UniqueMessageId` | TField |  | This field is used to configure the override to be used if any uniqueness exists.Valide record from OVERRIDES table.E.g. CP-CU.PERS.CUS.DUP.SIN |
| 8 | `CAPL.CUP.CUS.UNIQUE.ROUTINE` | `CaplHCusUniqueParam_CusUniqueRoutine` | TField |  | This field is used to define the routine which does the duplicate validation.Valid record from EB.API |
| 9 | `CAPL.CUP.DUP.CHECK.FLD` | `CaplHCusUniqueParam_DupCheckFld` |  |  |  |
| 10 | `CAPL.CUP.CONV.API` | `CaplHCusUniqueParam_ConvApi` |  |  |  |
| 11 | `CAPL.CUP.EX.CUS.STATUS` | `CaplHCusUniqueParam_ExCusStatus` |  |  |  |
| 12 | `CAPL.CUP.RESERVED.7` | `CaplHCusUniqueParam_Reserved7` | TField |  |  |
| 13 | `CAPL.CUP.RESERVED.6` | `CaplHCusUniqueParam_Reserved6` | TField |  |  |
| 14 | `CAPL.CUP.RESERVED.5` | `CaplHCusUniqueParam_Reserved5` | TField |  |  |
| 15 | `CAPL.CUP.RESERVED.4` | `CaplHCusUniqueParam_Reserved4` | TField |  |  |
| 16 | `CAPL.CUP.RESERVED.3` | `CaplHCusUniqueParam_Reserved3` | TField |  |  |
| 17 | `CAPL.CUP.RESERVED.2` | `CaplHCusUniqueParam_Reserved2` | TField |  |  |
| 18 | `CAPL.CUP.RESERVED.1` | `CaplHCusUniqueParam_Reserved1` | TField |  |  |
| 19 | `CAPL.CUP.LOCAL.REF` | `CaplHCusUniqueParam_LocalRef` |  |  |  |
| 20 | `CAPL.CUP.OVERRIDE` | `CaplHCusUniqueParam_Override` |  |  |  |
| 21 | `CAPL.CUP.RECORD.STATUS` | `CaplHCusUniqueParam_RecordStatus` | String |  |  |
| 22 | `CAPL.CUP.CURR.NO` | `CaplHCusUniqueParam_CurrNo` | String |  |  |
| 23 | `CAPL.CUP.INPUTTER` | `CaplHCusUniqueParam_Inputter` |  |  |  |
| 24 | `CAPL.CUP.DATE.TIME` | `CaplHCusUniqueParam_DateTime` |  |  |  |
| 25 | `CAPL.CUP.AUTHORISER` | `CaplHCusUniqueParam_Authoriser` | String |  |  |
| 26 | `CAPL.CUP.CO.CODE` | `CaplHCusUniqueParam_CoCode` | String |  |  |
| 27 | `CAPL.CUP.DEPT.CODE` | `CaplHCusUniqueParam_DeptCode` | String |  |  |
| 28 | `CAPL.CUP.AUDITOR.CODE` | `CaplHCusUniqueParam_AuditorCode` | String |  |  |
| 29 | `CAPL.CUP.AUDIT.DATE.TIME` | `CaplHCusUniqueParam_AuditDateTime` | String |  |  |
