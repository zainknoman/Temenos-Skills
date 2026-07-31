# FS.GI.USERS.MANAGEMENT — Table Schema

> Source: `INSERTS/I_F.FS.GI.USERS.MANAGEMENT` in `FS_UsersManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.USERS.MANAGEMENT.PARENT.REF.ID` | `FsGiUsersManagement_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.USERS.MANAGEMENT.ORA.ROWID` | `FsGiUsersManagement_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.USERS.MANAGEMENT.USER.ID` | `FsGiUsersManagement_UserId` | TField |  | Unique identification for a particular user. Multifonds DB Column is CUTIL. |
| 4 | `FS.GI.USERS.MANAGEMENT.USER.NAME` | `FsGiUsersManagement_UserName` | TField |  | Name of the user. Multifonds DB Column is NOM. |
| 5 | `FS.GI.USERS.MANAGEMENT.OPERATIONS.CENTRE` | `FsGiUsersManagement_OperationsCentre` | TField |  | Give user access rights for a particular operation center. Mainly used in connection with Multifonds dashboard. Multifonds DB Column is OPERATIONS_CENTRE. |
| 6 | `FS.GI.USERS.MANAGEMENT.DATE.FORMAT` | `FsGiUsersManagement_DateFormat` | TField |  | User date format. Multifonds DB Column is DFORMAT. |
| 7 | `FS.GI.USERS.MANAGEMENT.DEFAULT.FUND` | `FsGiUsersManagement_DefaultFund` | TField |  | A default fund may be defined for a user so that in most of the versions, this fund will be pre selected by default. Multifonds DB Column is CFOND. |
| 8 | `FS.GI.USERS.MANAGEMENT.START.DATE` | `FsGiUsersManagement_StartDate` | TField |  | User start date. Multifonds DB Column is START_DATE. |
| 9 | `FS.GI.USERS.MANAGEMENT.EXPIRY.DATE` | `FsGiUsersManagement_ExpiryDate` | TField |  | User expiry date. User should not be allowed to user the application after this date and an error message will be displayed. Multifonds DB Column is EXPIRY_DATE. |
| 10 | `FS.GI.USERS.MANAGEMENT.LANGUAGE` | `FsGiUsersManagement_Language` | TField |  | Enter the default language code for the user. Multifonds DB Column is CLANGUE. |
| 11 | `FS.GI.USERS.MANAGEMENT.EMAIL.ADDRESS` | `FsGiUsersManagement_EmailAddress` | TField |  | Email Address of the user. Multifonds DB Column is EMAIL1. |
| 12 | `FS.GI.USERS.MANAGEMENT.USER.TIMEZONE` | `FsGiUsersManagement_UserTimezone` | TField |  | Select the appropriate time zone from the list of values. Multifonds DB Column is USER_TIMEZONE. |
| 13 | `FS.GI.USERS.MANAGEMENT.MAX.USER.SESSIONS` | `FsGiUsersManagement_MaxUserSessions` | TField |  | Max User Sessions Multifonds DB Column is MAX_USER_TA. |
| 14 | `FS.GI.USERS.MANAGEMENT.GTA.ACCESS` | `FsGiUsersManagement_GtaAccess` | TField |  | GTA Access for the user. Multifonds DB Column is GTA_ACCESS. |
| 15 | `FS.GI.USERS.MANAGEMENT.AMS.ACCESS` | `FsGiUsersManagement_AmsAccess` | TField |  | If selected Yes, then user has the rights to access core application Multifonds DB Column is AMS_ACCESS. |
| 16 | `FS.GI.USERS.MANAGEMENT.ALL.FUNDS` | `FsGiUsersManagement_AllFunds` | TField |  | If selected Yes then user has access to all funds in the database. If selected No, then user only has access to dedicated funds. These funds need to be specifically defined in the Rights on Funds screen. Multifonds DB Column is ALL_NPTF. |
| 17 | `FS.GI.USERS.MANAGEMENT.FUND.ACCESS` | `FsGiUsersManagement_FundAccess` | TField |  | Fund Access for the user. Multifonds DB Column is FND_ACCESS. |
| 18 | `FS.GI.USERS.MANAGEMENT.CCL.ACCESS` | `FsGiUsersManagement_CclAccess` | TField |  | Ccl Access for the user. Multifonds DB Column is CCL_ACCESS. |
| 19 | `FS.GI.USERS.MANAGEMENT.QUERY.USER` | `FsGiUsersManagement_QueryUser` | TField |  | Query User for the user. Multifonds DB Column is QUERY_USER. |
| 20 | `FS.GI.USERS.MANAGEMENT.EXTERNAL.USER.ID` | `FsGiUsersManagement_ExternalUserId` | TField |  | Refers to external user identification Multifonds DB Column is EXTERNAL_USER_ID. |
| 21 | `FS.GI.USERS.MANAGEMENT.USER.ID.SSO` | `FsGiUsersManagement_UserIdSso` | TField |  | User ID for SSO. Multifonds DB Column is USERID_SSO. |
| 22 | `FS.GI.USERS.MANAGEMENT.TYPE.ACCOUNT.STATUS` | `FsGiUsersManagement_TypeAccountStatus` | TField |  | Status of the Account. Multifonds DB Column is TYPE_ACC. |
| 23 | `FS.GI.USERS.MANAGEMENT.RESERVED10` | `FsGiUsersManagement_Reserved10` | TField |  |  |
| 24 | `FS.GI.USERS.MANAGEMENT.RESERVED9` | `FsGiUsersManagement_Reserved9` | TField |  |  |
| 25 | `FS.GI.USERS.MANAGEMENT.RESERVED8` | `FsGiUsersManagement_Reserved8` | TField |  |  |
| 26 | `FS.GI.USERS.MANAGEMENT.RESERVED7` | `FsGiUsersManagement_Reserved7` | TField |  |  |
| 27 | `FS.GI.USERS.MANAGEMENT.RESERVED6` | `FsGiUsersManagement_Reserved6` | TField |  |  |
| 28 | `FS.GI.USERS.MANAGEMENT.RESERVED5` | `FsGiUsersManagement_Reserved5` | TField |  |  |
| 29 | `FS.GI.USERS.MANAGEMENT.RESERVED4` | `FsGiUsersManagement_Reserved4` | TField |  |  |
| 30 | `FS.GI.USERS.MANAGEMENT.RESERVED3` | `FsGiUsersManagement_Reserved3` | TField |  |  |
| 31 | `FS.GI.USERS.MANAGEMENT.RESERVED2` | `FsGiUsersManagement_Reserved2` | TField |  |  |
| 32 | `FS.GI.USERS.MANAGEMENT.RESERVED1` | `FsGiUsersManagement_Reserved1` | TField |  |  |
| 33 | `FS.GI.USERS.MANAGEMENT.LOCAL.REF` | `FsGiUsersManagement_LocalRef` |  |  |  |
| 34 | `FS.GI.USERS.MANAGEMENT.OVERRIDE` | `FsGiUsersManagement_Override` |  |  |  |
| 35 | `FS.GI.USERS.MANAGEMENT.RECORD.STATUS` | `FsGiUsersManagement_RecordStatus` | String |  |  |
| 36 | `FS.GI.USERS.MANAGEMENT.CURR.NO` | `FsGiUsersManagement_CurrNo` | String |  |  |
| 37 | `FS.GI.USERS.MANAGEMENT.INPUTTER` | `FsGiUsersManagement_Inputter` |  |  |  |
| 38 | `FS.GI.USERS.MANAGEMENT.DATE.TIME` | `FsGiUsersManagement_DateTime` |  |  |  |
| 39 | `FS.GI.USERS.MANAGEMENT.AUTHORISER` | `FsGiUsersManagement_Authoriser` | String |  |  |
| 40 | `FS.GI.USERS.MANAGEMENT.CO.CODE` | `FsGiUsersManagement_CoCode` | String |  |  |
| 41 | `FS.GI.USERS.MANAGEMENT.DEPT.CODE` | `FsGiUsersManagement_DeptCode` | String |  |  |
| 42 | `FS.GI.USERS.MANAGEMENT.AUDITOR.CODE` | `FsGiUsersManagement_AuditorCode` | String |  |  |
| 43 | `FS.GI.USERS.MANAGEMENT.AUDIT.DATE.TIME` | `FsGiUsersManagement_AuditDateTime` | String |  |  |
