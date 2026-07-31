# FS.GA.WEM.PARAMETERS — Table Schema

> Source: `INSERTS/I_F.FS.GA.WEM.PARAMETERS` in `FS_WemSetupConfiguration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.WEM.PARAMETERS.AUTO.VALIDATION` | `FsGaWemParameters_AutoValidation` | TField |  | To define the auto validation of breaks/exceptions functionality Multifonds DB Column is EM_AUTO_VAL,AUVL. |
| 2 | `FS.GA.WEM.PARAMETERS.HARD.RESET.NAV` | `FsGaWemParameters_HardResetNav` | TField |  | To define the hard reset nav functionality Multifonds DB Column is HARD_RESET_NAV,HRNAV. |
| 3 | `FS.GA.WEM.PARAMETERS.BYGROUP.EMAIL.SENDER` | `FsGaWemParameters_BygroupEmailSender` | TField |  | Mention the email ID of the sender Multifonds DB Column is BYGROUP_EMAIL,SENDER. |
| 4 | `FS.GA.WEM.PARAMETERS.BYGROUP.EMAIL.SUBJECT` | `FsGaWemParameters_BygroupEmailSubject` | TField |  | Subject of the mail being sent by the system is to be defined in this field. Multifonds DB Column is BYGROUP_EMAIL,SUB. |
| 5 | `FS.GA.WEM.PARAMETERS.BYGROUP.EMAIL.MESSAGE` | `FsGaWemParameters_BygroupEmailMessage` | TField |  | Format of the message when step is completed will be defined in this field Multifonds DB Column is BYGROUP_EMAIL,MSG. |
| 6 | `FS.GA.WEM.PARAMETERS.BYGROUP.EMAIL.RESET.MESSAGE` | `FsGaWemParameters_BygroupEmailResetMessage` | TField |  | Format of the message when step is reset will be defined in this field Multifonds DB Column is BYGROUP_EMAIL,RESET_MSG. |
| 7 | `FS.GA.WEM.PARAMETERS.ALERT.SENDER` | `FsGaWemParameters_AlertSender` | TField |  | Mention the email ID of the sender for the alert mail Multifonds DB Column is EM_ALERT,SENDER. |
| 8 | `FS.GA.WEM.PARAMETERS.ALERT.SUBJECT` | `FsGaWemParameters_AlertSubject` | TField |  | Mention the subject for the alert mail Multifonds DB Column is EM_ALERT,SUB. |
| 9 | `FS.GA.WEM.PARAMETERS.ALERT.MESSAGE` | `FsGaWemParameters_AlertMessage` | TField |  | Format of the message for the alert mail Multifonds DB Column is EM_ALERT,MSG. |
| 10 | `FS.GA.WEM.PARAMETERS.FILE.SAVING.PATH` | `FsGaWemParameters_FileSavingPath` | TField |  | Set the file saving path Multifonds DB Column is MF_EM,EXUP. |
| 11 | `FS.GA.WEM.PARAMETERS.MANDATORY.JUSTIFICATION` | `FsGaWemParameters_MandatoryJustification` | TField | Yes | Define whether mandatory justification is required or not for exceptions Multifonds DB Column is MF_EM,WNEX. |
| 12 | `FS.GA.WEM.PARAMETERS.EXCEPTION.CATEGORY` | `FsGaWemParameters_ExceptionCategory` | TField |  | Define the option to manage exception category Multifonds DB Column is MF_EM,EXCT. |
| 13 | `FS.GA.WEM.PARAMETERS.FILTER.BY.NAV.GROUP` | `FsGaWemParameters_FilterByNavGroup` | TField |  | To filter the records based on NAV group Multifonds DB Column is NAV_GROUP_FILTER,NAV_GRP. |
| 14 | `FS.GA.WEM.PARAMETERS.RESET.TRACKING` | `FsGaWemParameters_ResetTracking` | TField |  | to track the reset of steps Multifonds DB Column is RESET_DONE,RESET_DONE. |
| 15 | `FS.GA.WEM.PARAMETERS.EXCEPTION.STATUS.WARNING` | `FsGaWemParameters_ExceptionStatusWarning` | TField |  | Define if 4 eyes is required for warning exceptions Multifonds DB Column is EXP_STS,W. |
| 16 | `FS.GA.WEM.PARAMETERS.EXCEPTION.STATUS.FATAL` | `FsGaWemParameters_ExceptionStatusFatal` | TField |  | Define if 4 eyes is required for fatal exceptions Multifonds DB Column is EXP_STS,F. |
| 17 | `FS.GA.WEM.PARAMETERS.EXCEPTION.STATUS.SEC.ID1` | `FsGaWemParameters_ExceptionStatusSecId1` | TField |  | Which type of sec Id should be displayed in the Exception screen for the exception linked to security, the system will display the available code based on the order display in this screen Multifonds DB Column is EXP_STS,SECID1. |
| 18 | `FS.GA.WEM.PARAMETERS.EXCEPTION.STATUS.SEC.ID2` | `FsGaWemParameters_ExceptionStatusSecId2` | TField |  | Which type of sec Id should be displayed in the Exception screen for the exception linked to security, the system will display the available code based on the order display in this screen Multifonds DB Column is EXP_STS,SECID2. |
| 19 | `FS.GA.WEM.PARAMETERS.EXCEPTION.STATUS.SEC.ID3` | `FsGaWemParameters_ExceptionStatusSecId3` | TField |  | Which type of sec Id should be displayed in the Exception screen for the exception linked to security, the system will display the available code based on the order display in this screen Multifonds DB Column is EXP_STS,SECID3. |
| 20 | `FS.GA.WEM.PARAMETERS.DISABLE.AUTO.REFRESH` | `FsGaWemParameters_DisableAutoRefresh` | TField |  | To disable or enable auto refresh of screens Multifonds DB Column is BYGROUP_BYSTREAM_JOBS,PROGRESS_BAR. |
| 21 | `FS.GA.WEM.PARAMETERS.RESERVED10` | `FsGaWemParameters_Reserved10` | TField |  |  |
| 22 | `FS.GA.WEM.PARAMETERS.RESERVED9` | `FsGaWemParameters_Reserved9` | TField |  |  |
| 23 | `FS.GA.WEM.PARAMETERS.RESERVED8` | `FsGaWemParameters_Reserved8` | TField |  |  |
| 24 | `FS.GA.WEM.PARAMETERS.RESERVED7` | `FsGaWemParameters_Reserved7` | TField |  |  |
| 25 | `FS.GA.WEM.PARAMETERS.RESERVED6` | `FsGaWemParameters_Reserved6` | TField |  |  |
| 26 | `FS.GA.WEM.PARAMETERS.RESERVED5` | `FsGaWemParameters_Reserved5` | TField |  |  |
| 27 | `FS.GA.WEM.PARAMETERS.RESERVED4` | `FsGaWemParameters_Reserved4` | TField |  |  |
| 28 | `FS.GA.WEM.PARAMETERS.RESERVED3` | `FsGaWemParameters_Reserved3` | TField |  |  |
| 29 | `FS.GA.WEM.PARAMETERS.RESERVED2` | `FsGaWemParameters_Reserved2` | TField |  |  |
| 30 | `FS.GA.WEM.PARAMETERS.RESERVED1` | `FsGaWemParameters_Reserved1` | TField |  |  |
| 31 | `FS.GA.WEM.PARAMETERS.LOCAL.REF` | `FsGaWemParameters_LocalRef` |  |  |  |
| 32 | `FS.GA.WEM.PARAMETERS.OVERRIDE` | `FsGaWemParameters_Override` |  |  |  |
| 33 | `FS.GA.WEM.PARAMETERS.RECORD.STATUS` | `FsGaWemParameters_RecordStatus` | String |  |  |
| 34 | `FS.GA.WEM.PARAMETERS.CURR.NO` | `FsGaWemParameters_CurrNo` | String |  |  |
| 35 | `FS.GA.WEM.PARAMETERS.INPUTTER` | `FsGaWemParameters_Inputter` |  |  |  |
| 36 | `FS.GA.WEM.PARAMETERS.DATE.TIME` | `FsGaWemParameters_DateTime` |  |  |  |
| 37 | `FS.GA.WEM.PARAMETERS.AUTHORISER` | `FsGaWemParameters_Authoriser` | String |  |  |
| 38 | `FS.GA.WEM.PARAMETERS.CO.CODE` | `FsGaWemParameters_CoCode` | String |  |  |
| 39 | `FS.GA.WEM.PARAMETERS.DEPT.CODE` | `FsGaWemParameters_DeptCode` | String |  |  |
| 40 | `FS.GA.WEM.PARAMETERS.AUDITOR.CODE` | `FsGaWemParameters_AuditorCode` | String |  |  |
| 41 | `FS.GA.WEM.PARAMETERS.AUDIT.DATE.TIME` | `FsGaWemParameters_AuditDateTime` | String |  |  |
