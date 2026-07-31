# VERSION.CONTROL — Table Schema

> Source: `INSERTS/I_F.VERSION.CONTROL` in `EB_Versions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.VER.CTRL.AUTO.FIELD.NAME` | `VersionControl_AutoFieldName` |  |  |  |
| 2 | `EB.VER.CTRL.AUTO.OLD.CONT` | `VersionControl_AutoOldCont` |  |  |  |
| 3 | `EB.VER.CTRL.AUTO.FIELD.RTN` | `VersionControl_AutoFieldRtn` |  |  |  |
| 4 | `EB.VER.CTRL.FIELD.NAME` | `VersionControl_FieldName` |  |  |  |
| 5 | `EB.VER.CTRL.VALIDATION.RTN` | `VersionControl_ValidationRtn` |  |  |  |
| 6 | `EB.VER.CTRL.INPUT.RTN` | `VersionControl_InputRtn` |  |  |  |
| 7 | `EB.VER.CTRL.AUTH.RTN` | `VersionControl_AuthRtn` |  |  |  |
| 8 | `EB.VER.CTRL.ID.RTN` | `VersionControl_IdRtn` |  |  |  |
| 9 | `EB.VER.CTRL.CHECK.REC.RTN` | `VersionControl_CheckRecRtn` |  |  |  |
| 10 | `EB.VER.CTRL.AFTER.UNAU.RTN` | `VersionControl_AfterUnauRtn` |  |  |  |
| 11 | `EB.VER.CTRL.BEFORE.AUTH.RTN` | `VersionControl_BeforeAuthRtn` |  |  |  |
| 12 | `EB.VER.CTRL.NON.VERSION.RUN` | `VersionControl_NonVersionRun` | TField |  | To make the routines execute for bare application or not. YES to execute the routines for bare application NO to execute the routines only for versions and not for bare application. Validation Rules: A maximum of 1 characters may be entered. The following values are permitted: Y N |
| 13 | `EB.VER.CTRL.FLD.CHECK.VALUE` | `VersionControl_FldCheckValue` |  |  |  |
| 14 | `EB.VER.CTRL.FLD.CHECK.TYPE` | `VersionControl_FldCheckType` |  |  |  |
| 15 | `EB.VER.CTRL.FLD.NAME` | `VersionControl_FldName` |  |  |  |
| 16 | `EB.VER.CTRL.FLD.INC.EXC` | `VersionControl_FldIncExc` |  |  |  |
| 17 | `EB.VER.CTRL.NOINPUT.VALUE` | `VersionControl_NoinputValue` |  |  |  |
| 18 | `EB.VER.CTRL.NOINPUT.TYPE` | `VersionControl_NoinputType` |  |  |  |
| 19 | `EB.VER.CTRL.NOINPUT.FLD` | `VersionControl_NoinputFld` |  |  |  |
| 20 | `EB.VER.CTRL.NOINP.INC.EX` | `VersionControl_NoinpIncEx` |  |  |  |
| 21 | `EB.VER.CTRL.NO.CHG.VALUE` | `VersionControl_NoChgValue` |  |  |  |
| 22 | `EB.VER.CTRL.NO.CHG.TYPE` | `VersionControl_NoChgType` |  |  |  |
| 23 | `EB.VER.CTRL.NO.CHG.FLD` | `VersionControl_NoChgFld` |  |  |  |
| 24 | `EB.VER.CTRL.NO.CHG.IN.EX` | `VersionControl_NoChgInEx` |  |  |  |
| 25 | `EB.VER.CTRL.REKEY.VALUE` | `VersionControl_RekeyValue` |  |  |  |
| 26 | `EB.VER.CTRL.REKEY.TYPE` | `VersionControl_RekeyType` |  |  |  |
| 27 | `EB.VER.CTRL.REKEY.FLD` | `VersionControl_RekeyFld` |  |  |  |
| 28 | `EB.VER.CTRL.REKEY.INC.EX` | `VersionControl_RekeyIncEx` |  |  |  |
| 29 | `EB.VER.CTRL.AUTOM.VALUE` | `VersionControl_AutomValue` |  |  |  |
| 30 | `EB.VER.CTRL.AUTOM.TYPE` | `VersionControl_AutomType` |  |  |  |
| 31 | `EB.VER.CTRL.AUT.FLD.NO` | `VersionControl_AutFldNo` |  |  |  |
| 32 | `EB.VER.CTRL.AUT.OLD.CONT` | `VersionControl_AutOldCont` |  |  |  |
| 33 | `EB.VER.CTRL.AUT.NEW.CONT` | `VersionControl_AutNewCont` |  |  |  |
| 34 | `EB.VER.CTRL.AUTOM.INC.EX` | `VersionControl_AutomIncEx` |  |  |  |
| 35 | `EB.VER.CTRL.MAND.VALUE` | `VersionControl_MandValue` |  |  |  |
| 36 | `EB.VER.CTRL.MAND.TYPE` | `VersionControl_MandType` |  |  |  |
| 37 | `EB.VER.CTRL.MAND.FLD` | `VersionControl_MandFld` |  |  |  |
| 38 | `EB.VER.CTRL.MAND.INC.EXC` | `VersionControl_MandIncExc` |  |  |  |
| 39 | `EB.VER.CTRL.D.SLIP.VALUE` | `VersionControl_DSlipValue` |  |  |  |
| 40 | `EB.VER.CTRL.D.SLIP.TYPE` | `VersionControl_DSlipType` |  |  |  |
| 41 | `EB.VER.CTRL.D.SLIP.FMT` | `VersionControl_DSlipFmt` |  |  |  |
| 42 | `EB.VER.CTRL.D.SLIP.FUNC` | `VersionControl_DSlipFunc` |  |  |  |
| 43 | `EB.VER.CTRL.D.SLIP.IN.EX` | `VersionControl_DSlipInEx` |  |  |  |
| 44 | `EB.VER.CTRL.GTS.VALUE` | `VersionControl_GtsValue` |  |  |  |
| 45 | `EB.VER.CTRL.GTS.TYPE` | `VersionControl_GtsType` |  |  |  |
| 46 | `EB.VER.CTRL.GTS.CONTROL` | `VersionControl_GtsControl` |  |  |  |
| 47 | `EB.VER.CTRL.GTS.INC.EXC` | `VersionControl_GtsIncExc` |  |  |  |
| 48 | `EB.VER.CTRL.COMPANY.ACCESS` | `VersionControl_CompanyAccess` | TField | No | This field is used to define whether a VERSION can be restricted to being run only in a users initial sign on company, and can only be input when the multi branch product is installed. Multi branch indicates that the MB product is installed, the term Multi Book can also be used. This product basically allows financial level data to be stored in the same database table for all companies, as opposed to Multi Company where the data is stored in a separate table for each company. Validation Rules: Optional input only when the MB product is installed Can be set to OWN to indicate that the version can only be run in the users initial sign on company, i.e. the users own branch |
| 49 | `EB.VER.CTRL.BUSINESS.DAY` | `VersionControl_BusinessDay` | TField | No | This field indicates on what type of business day the VERSION can be run. This is based on the value of the CURRENT.DAY field on the DATES record. NORMAL the branch is open on an official working day RESTRICTED the branch is open on an official holiday, e.g. a weekend or public holiday CLOSED the branch is closed i.e. the holiday table for the branch indicates a non working day, or the day corresponds to a value on the BRNACH.CLOSED field for the company For example some business activities can only take place on an official working day such as certain clearing transactions, whereas others e.g. closing a customer account can take place if the branch is open. If this field is left blank then there will be no check as to whether the version can be run. Validation Rules: Optional input NORMAL indicates the version can only be run on a normal business day, e.g. only on an official working day for the local country RESTRICTED indicates that the version can be run on a normal or restricted working day e.g. the branch is open CLOSED indicates that the version can be run at any time |
| 50 | `EB.VER.CTRL.AUTO.COMP.CHANGE` | `VersionControl_AutoCompChange` | TField | No | This field is used to define in a multi branch system whether the user can directly access a record in another company, without having to manually exit the application, sign in to the other company and invoke the application. Multi branch indicates that the MB product is installed, the term Multi Book can also be used. This product basically allows financial level data to be stored in the same database table for all companies, as opposed to Multi Company where the data is stored in a separate table for each company. If this field is set to YES then the user can enter access a record in another company to perform a transaction. The user must have access to the other company via the OTH.BOOK.ACCESS or OTH.BOOK.BLOCK fields of their USER record. The user does not need to have the ability to sing in to the other company. An SMS check will be applied for the current application and function before the new company is loaded automatically. An example would be when a customer wishes to close an account in a branch other than their own, in this case the teller would enter the account number, the system would then switch companies and the account can be closed. If this field is left blank then in a multi branch environment the user will not be allowed to directly access records in other branches, but must be signed in to that company. Validation Rules: Optional input of YES only when the MB product is installed. |
| 51 | `EB.VER.CTRL.SYS.MSG.SUPPRESS` | `VersionControl_SysMsgSuppress` | TField |  | This field in VERSION.CONTROL record or VERSION.CONTROL SYSTEM record along with a similar field in SYSTEM.OVERRIDE table set to YES will suppress the system override message. Any messages that have not been flagged in the System Override Message Table will not be suppressed, even when a VERSION or VERSION.CONTROL (including 'SYSTEM') record is set for suppression. The default for SYS.MSG.SUPPRESS field in both the System Override Message Table and the VERSION/VERSION.CONTROL will be no suppression. A record 'SYSTEM' in VERSION.CONTROL can be used to define criteria (including message suppression) at global system level as opposed to just application level, so will define version defaults for all versions of all applications. The following routines can be defaulted for all versions of all applications (apart from message suppression) using the VERSION.CONTROL SYSTEM record. 1. INPUT.RTN 2. AUTH.RTN 3. ID.RTN 4. CHECK.REC.RTN 5. AFTER.UNAU.RTN 6. BEFORE.AUTH.RTN Display or suppression of a system override message will depend on the following flag settings VERSION Msg Suppress VERSION.CONTROL&gt;application Msg Suppress VERSION.CONTROL&gt;SYSTEM Msg Suppress System Override Msg Table Msg Suppress Suppress Message Yes/No Null Null Null Yes No Yes Null Null Yes Yes Yes Null Null No No No Null Null No No No Yes Null Yes No No Yes Null No No Null Yes Null Yes Yes Null Yes Null No No Null No Null Yes No Null No Null No No Null No Yes No No Null Null Yes Yes Yes Null Null Yes No No Null Null No Yes No Null Null No No No Null Null Null No No Validation Rules: YES or NO or NULL (Blank) |
| 52 | `EB.VER.CTRL.D.SLIP.STYLE.SHEET` | `VersionControl_DSlipStyleSheet` | TField |  | Contains the name of an XSLT stylesheet to be used when displaying a Deal Slip in T24 Browser. This field is only used for the T24 Browser product. |
| 53 | `EB.VER.CTRL.ATT.FLD.NAME` | `VersionControl_AttFldName` |  |  |  |
| 54 | `EB.VER.CTRL.DISPLAY.TYPE` | `VersionControl_DisplayType` |  |  |  |
| 55 | `EB.VER.CTRL.ATTRIBS` | `VersionControl_Attribs` |  |  |  |
| 56 | `EB.VER.CTRL.WEB.VAL.RTN` | `VersionControl_WebValRtn` | TField |  | Contains the name of a Java EB.API record routine that will be called on the T24 Web Server to validate the fields marked as Web Validate. This field is only used for the T24 Browser product. |
| 57 | `EB.VER.CTRL.LANGUAGE.CODE` | `VersionControl_LanguageCode` |  |  |  |
| 58 | `EB.VER.CTRL.AUTO.OVERRIDES` | `VersionControl_AutoOverrides` | TField |  | If this field is set to "YES", during OFS transaction each Override encountered will be checked to see if it can be considered for automatic validation. Validation Rules: "YES" or "NO" |
| 59 | `EB.VER.CTRL.DEFAULT.ROUTINE` | `VersionControl_DefaultRoutine` |  |  |  |
| 60 | `EB.VER.CTRL.LINK.ACTIVATION` | `VersionControl_LinkActivation` | TField |  | Activation link will be enabled for the version if this field is set Any transaction done using this Version will update ACTIVATION.FILE based on the configurations maintained in EB.VERSION.ACTIVATION.LINK application Link Activation can be enabled either in VERSION or VERSION.CONTROL Disabling Link Activation can be done only if no record available for VERSION/VERSION.CONTROL in EB.VERSION.ACTIVATION.LINK application |
| 61 | `EB.VER.CTRL.RESERVED.3` | `VersionControl_Reserved3` | TField |  |  |
| 62 | `EB.VER.CTRL.RESERVED.2` | `VersionControl_Reserved2` | TField |  |  |
| 63 | `EB.VER.CTRL.RESERVED.1` | `VersionControl_Reserved1` | TField |  |  |
| 64 | `EB.VER.CTRL.RECORD.STATUS` | `VersionControl_RecordStatus` | String |  |  |
| 65 | `EB.VER.CTRL.CURR.NO` | `VersionControl_CurrNo` | String |  |  |
| 66 | `EB.VER.CTRL.INPUTTER` | `VersionControl_Inputter` |  |  |  |
| 67 | `EB.VER.CTRL.DATE.TIME` | `VersionControl_DateTime` |  |  |  |
| 68 | `EB.VER.CTRL.AUTHORISER` | `VersionControl_Authoriser` | String |  |  |
| 69 | `EB.VER.CTRL.CO.CODE` | `VersionControl_CoCode` | String |  |  |
| 70 | `EB.VER.CTRL.DEPT.CODE` | `VersionControl_DeptCode` | String |  |  |
| 71 | `EB.VER.CTRL.AUDITOR.CODE` | `VersionControl_AuditorCode` | String |  |  |
| 72 | `EB.VER.CTRL.AUDIT.DATE.TIME` | `VersionControl_AuditDateTime` | String |  |  |
