# CP.PROGRAM.STATUS — Table Schema

> Source: `INSERTS/I_F.CP.PROGRAM.STATUS` in `CP_Campaign.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CP.PRG.DESCRIPTION` | `CpProgramStatus_Description` |  |  |  |
| 2 | `CP.PRG.FLOW.VALIDATION` | `CpProgramStatus_FlowValidation` | TField |  | This field stores the direction of the flow when a program is moved in the given status. The values in the list of values available to choose from are: START, NEXT, BACK, END. |
| 3 | `CP.PRG.TYPE` | `CpProgramStatus_Type` | TField |  | This field stores the type of the program status. The values in the list of values available to choose from are: RUNNING, TESTING, NORMAL. |
| 4 | `CP.PRG.BUTTON.LABEL` | `CpProgramStatus_ButtonLabel` | TField |  | This field stores the label of the button that has to be clicked by the Marketing role in order to move the program to the given status. |
| 5 | `CP.PRG.SEARCH.TITLE` | `CpProgramStatus_SearchTitle` | TField |  | This field stores the Campaign Management User Agent Interface Dashboard tab labels. |
| 6 | `CP.PRG.NEXT.STATUS` | `CpProgramStatus_NextStatus` | TField |  | This field stores the next (forward) status, on the approval flow, a program can be moved to by the Marketing role. The Admin user picks this value from a dropdown list containing the available program statuses defined in the new CP.PROGRAM.STATUS table. |
| 7 | `CP.PRG.BACK.STATUS` | `CpProgramStatus_BackStatus` | TField |  | This field stores the back (backward) status, on the approval flow, a program can be moved to by the Marketing role. The Admin user picks this value from a dropdown list containing the available program statuses defined in the new CP.PROGRAM.STATUS table. |
| 8 | `CP.PRG.AUTO.VERSION.STS` | `CpProgramStatus_AutoVersionSts` | TField |  | This field stores the business Marketing role which can see and interact with the program in a given status. The Admin user picks this value from a dropdown list containing the available user roles defined in the USER.SMS.GROUP table. |
| 9 | `CP.PRG.USER.ROLE` | `CpProgramStatus_UserRole` | TField |  | This field contains the status of a program when it is auto versioned. |
| 10 | `CP.PRG.APP.EDITABLE` | `CpProgramStatus_AppEditable` | TField |  | Y/N values. The values indicate whether or not the program is editable in the given status. |
| 11 | `CP.PRG.NO.AUTHORISATIONS` | `CpProgramStatus_NoAuthorisations` | TField |  | No of authorisers |
| 12 | `CP.PRG.RESERVED.10` | `CpProgramStatus_Reserved10` | TField |  |  |
| 13 | `CP.PRG.RESERVED.9` | `CpProgramStatus_Reserved9` | TField |  |  |
| 14 | `CP.PRG.RESERVED.8` | `CpProgramStatus_Reserved8` | TField |  |  |
| 15 | `CP.PRG.RESERVED.7` | `CpProgramStatus_Reserved7` | TField |  |  |
| 16 | `CP.PRG.RESERVED.6` | `CpProgramStatus_Reserved6` | TField |  |  |
| 17 | `CP.PRG.RESERVED.5` | `CpProgramStatus_Reserved5` | TField |  |  |
| 18 | `CP.PRG.RESERVED.4` | `CpProgramStatus_Reserved4` | TField |  |  |
| 19 | `CP.PRG.RESERVED.3` | `CpProgramStatus_Reserved3` | TField |  |  |
| 20 | `CP.PRG.RESERVED.2` | `CpProgramStatus_Reserved2` | TField |  |  |
| 21 | `CP.PRG.RESERVED.1` | `CpProgramStatus_Reserved1` | TField |  |  |
| 22 | `CP.PRG.LOCAL.REF` | `CpProgramStatus_LocalRef` |  |  |  |
| 23 | `CP.PRG.OVERRIDE` | `CpProgramStatus_Override` |  |  |  |
| 24 | `CP.PRG.RECORD.STATUS` | `CpProgramStatus_RecordStatus` | String |  |  |
| 25 | `CP.PRG.CURR.NO` | `CpProgramStatus_CurrNo` | String |  |  |
| 26 | `CP.PRG.INPUTTER` | `CpProgramStatus_Inputter` |  |  |  |
| 27 | `CP.PRG.DATE.TIME` | `CpProgramStatus_DateTime` |  |  |  |
| 28 | `CP.PRG.AUTHORISER` | `CpProgramStatus_Authoriser` | String |  |  |
| 29 | `CP.PRG.CO.CODE` | `CpProgramStatus_CoCode` | String |  |  |
| 30 | `CP.PRG.DEPT.CODE` | `CpProgramStatus_DeptCode` | String |  |  |
| 31 | `CP.PRG.AUDITOR.CODE` | `CpProgramStatus_AuditorCode` | String |  |  |
| 32 | `CP.PRG.AUDIT.DATE.TIME` | `CpProgramStatus_AuditDateTime` | String |  |  |
