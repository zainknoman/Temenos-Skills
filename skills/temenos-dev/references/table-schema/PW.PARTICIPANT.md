# PW.PARTICIPANT — Table Schema

> Source: `INSERTS/I_F.PW.PARTICIPANT` in `PW_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PW.PART.DESCRIPTION` | `PwParticipant_Description` |  |  |  |
| 2 | `PW.PART.SHORT.DESC` | `PwParticipant_ShortDesc` |  |  |  |
| 3 | `PW.PART.ACCT.OFFICER` | `PwParticipant_AcctOfficer` |  |  |  |
| 4 | `PW.PART.USER` | `PwParticipant_User` |  |  |  |
| 5 | `PW.PART.LAST.USER` | `PwParticipant_LastUser` | TField |  | PW.PARTICIPANT LAST.USER Indicates the last USER from the multi-value list of USERs that was assigned to a PW.ACTIVITY.TXN. Automatically populated with each new PW.ACTIVITY.TXN record that has been created. Validation Rules: No input field. Automatically populated. |
| 6 | `PW.PART.LAST.DAO` | `PwParticipant_LastDao` | TField |  | PW.PARTICIPANT LAST.DAO Indicates the last DEPT.ACCT.OFFICER from the multi-value list of ACCT.OFFICERs that was assigned to a PW.ACTIVITY.TXN. Automatically populated with each new PW.ACTIVITY.TXN record that has been created. Validation Rules: No input field. Automatically populated. |
| 7 | `PW.PART.ALLOW.EXT.USR` | `PwParticipant_AllowExtUsr` | TField |  | Field to indicate if the activity can be assigned to an external user. |
| 8 | `PW.PART.RESERVED.9` | `PwParticipant_Reserved9` | TField |  |  |
| 9 | `PW.PART.RESERVED.8` | `PwParticipant_Reserved8` | TField |  |  |
| 10 | `PW.PART.RESERVED.7` | `PwParticipant_Reserved7` | TField |  |  |
| 11 | `PW.PART.RESERVED.6` | `PwParticipant_Reserved6` | TField |  |  |
| 12 | `PW.PART.RESERVED.5` | `PwParticipant_Reserved5` | TField |  |  |
| 13 | `PW.PART.RESERVED.4` | `PwParticipant_Reserved4` | TField |  |  |
| 14 | `PW.PART.RESERVED.3` | `PwParticipant_Reserved3` | TField |  |  |
| 15 | `PW.PART.RESERVED.2` | `PwParticipant_Reserved2` | TField |  |  |
| 16 | `PW.PART.RESERVED.1` | `PwParticipant_Reserved1` | TField |  |  |
| 17 | `PW.PART.LOCAL.REF` | `PwParticipant_LocalRef` |  |  |  |
| 18 | `PW.PART.OVERRIDE` | `PwParticipant_Override` |  |  |  |
| 19 | `PW.PART.RECORD.STATUS` | `PwParticipant_RecordStatus` | String |  |  |
| 20 | `PW.PART.CURR.NO` | `PwParticipant_CurrNo` | String |  |  |
| 21 | `PW.PART.INPUTTER` | `PwParticipant_Inputter` |  |  |  |
| 22 | `PW.PART.DATE.TIME` | `PwParticipant_DateTime` |  |  |  |
| 23 | `PW.PART.AUTHORISER` | `PwParticipant_Authoriser` | String |  |  |
| 24 | `PW.PART.CO.CODE` | `PwParticipant_CoCode` | String |  |  |
| 25 | `PW.PART.DEPT.CODE` | `PwParticipant_DeptCode` | String |  |  |
| 26 | `PW.PART.AUDITOR.CODE` | `PwParticipant_AuditorCode` | String |  |  |
| 27 | `PW.PART.AUDIT.DATE.TIME` | `PwParticipant_AuditDateTime` | String |  |  |
| 28 | `PW.PART.PARTICIPANT.STATUS` | `PwParticipant_ParticipantStatus` | TField |  | PW.PARTICIPANT PARTICIPANT.STATUS Describes the PW.PARTICIPANT status when Load balancer is set to YES in the PW.PARAMETER table Validation Rules: Either Active or Inactive The field will expect a value if Load Balancer is set to YES in the PW.PARAMETER table |
| 29 | `PW.PART.PARTICIPANT.THRESHOLD` | `PwParticipant_ParticipantThreshold` | TField |  | PW.PARTICIPANT PARTICIPANT.THRESHOLD Defines the PW.PARTICIPANT threshold when Load Balancer is set to YES in the PW.PARAMETER table. This value is considered as the common threshold for Users or DAOs at the PW.PARTICIPANT level. Validation Rules: Numeric character |
| 30 | `PW.PART.ACCT.OFFICER.STATUS` | `PwParticipant_AcctOfficerStatus` |  |  |  |
| 31 | `PW.PART.ACCT.OFFICER.THRESHOLD` | `PwParticipant_AcctOfficerThreshold` |  |  |  |
| 32 | `PW.PART.USER.STATUS` | `PwParticipant_UserStatus` |  |  |  |
| 33 | `PW.PART.USER.THRESHOLD` | `PwParticipant_UserThreshold` |  |  |  |
| 34 | `PW.PART.ACCT.OFFICER.ADMIN` | `PwParticipant_AcctOfficerAdmin` |  |  |  |
| 35 | `PW.PART.ADMIN.USER` | `PwParticipant_AdminUser` |  |  |  |
