# EB.EXTERNAL.USER — Table Schema

> Source: `INSERTS/I_F.EB.EXTERNAL.USER` in `EB_ARC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.XU.NAME` | `EbExternalUser_Name` | TField |  | The user's name |
| 2 | `EB.XU.CUSTOMER` | `EbExternalUser_Customer` | TField |  | The customer the user can access. This is a NOCHANGE field |
| 3 | `EB.XU.PASSWORD.REVIEW` | `EbExternalUser_PasswordReview` | TField |  | The duration in which the password is to be reviewed by the user |
| 4 | `EB.XU.COMPANY` | `EbExternalUser_Company` | TField |  | The companies the user can access |
| 5 | `EB.XU.CHANNEL` | `EbExternalUser_Channel` |  |  |  |
| 6 | `EB.XU.STATUS` | `EbExternalUser_Status` |  |  |  |
| 7 | `EB.XU.STATUS.CHANGE.REASON` | `EbExternalUser_StatusChangeReason` |  |  |  |
| 8 | `EB.XU.T.C.ACCEPTED` | `EbExternalUser_TCAccepted` |  |  |  |
| 9 | `EB.XU.PRODUCT.LINE` | `EbExternalUser_ProductLine` |  |  |  |
| 10 | `EB.XU.ARRANGEMENT` | `EbExternalUser_Arrangement` |  |  |  |
| 11 | `EB.XU.ALLOWED.CUSTOMER` | `EbExternalUser_AllowedCustomer` |  |  |  |
| 12 | `EB.XU.CHANNEL.PERMISSION` | `EbExternalUser_ChannelPermission` |  |  |  |
| 13 | `EB.XU.START.DATE` | `EbExternalUser_StartDate` |  |  |  |
| 14 | `EB.XU.END.DATE` | `EbExternalUser_EndDate` |  |  |  |
| 15 | `EB.XU.START.TIME` | `EbExternalUser_StartTime` |  |  |  |
| 16 | `EB.XU.END.TIME` | `EbExternalUser_EndTime` |  |  |  |
| 17 | `EB.XU.DATE.LAST.USE` | `EbExternalUser_DateLastUse` |  |  |  |
| 18 | `EB.XU.USE.DURATION` | `EbExternalUser_UseDuration` |  |  |  |
| 19 | `EB.XU.TIME.LAST.USE` | `EbExternalUser_TimeLastUse` |  |  |  |
| 20 | `EB.XU.USER.TYPE` | `EbExternalUser_UserType` |  |  |  |
| 21 | `EB.XU.EXTERNAL.REFERENCE` | `EbExternalUser_ExternalReference` |  |  |  |
| 22 | `EB.XU.LOGIN.METHOD` | `EbExternalUser_LoginMethod` |  |  |  |
| 23 | `EB.XU.MEMORABLE.DATA` | `EbExternalUser_MemorableData` | TField |  | Encrypted memorable data of the user |
| 24 | `EB.XU.AUT.UPD.SERVER` | `EbExternalUser_AutUpdServer` | TField |  | When selected, will create a user record in the Authentication server User id will be same as EB.EXTERNAL.USER id in the Authentication Server. Eg.: 4TRESS |
| 25 | `EB.XU.AUT.UPD.STATUS` | `EbExternalUser_AutUpdStatus` | TField |  | Holds a numeric value between 0 to 4 indicating the status of the user record creation in Authentication Server 0 - user record created successfully in Authentication server 1 - user record not created in Authentication Server 2 - Communication does not exist between Authentication server and T24 3 - Internal Error |
| 26 | `EB.XU.AUT.UPD.DATE` | `EbExternalUser_AutUpdDate` | TField |  | Field will be updated by T24 on creation of a external user in T24. Field will hold T24 date as the value. It is a no input field. |
| 27 | `EB.XU.AUTHENTICATION.TYPE` | `EbExternalUser_AuthenticationType` | TField |  | The type of authentication for this external user. Valid values are :- External - External authentication via an authentication services such as 4Tress. User Maintained - Maintained by the user with a simpla user name and password. |
| 28 | `EB.XU.PASSWORD` | `EbExternalUser_Password` | TField |  | The password set for the user's login |
| 29 | `EB.XU.PASSW.CHANGE.DATE` | `EbExternalUser_PasswChangeDate` | TField |  | The date when the password was changed |
| 30 | `EB.XU.ATTEMPTS.SINCE` | `EbExternalUser_AttemptsSince` | TField |  | Counter of the number of consecutive incorrect passwords the user has actually entered, since last entering a correct password. |
| 31 | `EB.XU.LDAP.ID` | `EbExternalUser_LdapId` | TField |  | Field takes the EB.LDAP.PARAMETER record id as the value |
| 32 | `EB.XU.LDAP.DN` | `EbExternalUser_LdapDn` | TField |  | Field takes any value . Value should be prefixed with CN= &lt;anyname&gt; |
| 33 | `EB.XU.UPDATE.AUTH.PIN` | `EbExternalUser_UpdateAuthPin` | TField |  | Reset the PIN of the EXTERNAL user in the Authentication Server. Move the PIN status in the Authentication Server to PENDING. |
| 34 | `EB.XU.UPDATE.AUTH.PW` | `EbExternalUser_UpdateAuthPw` | TField |  | Reset the Password of the EXTERNAL user in Authentication Server Move the PASSWORD status in the Authentication Server to PENDING |
| 35 | `EB.XU.UPDATE.CUST.DATA` | `EbExternalUser_UpdateCustData` | TField |  | Updates the customer information in Authentication server when any change is made to the existing customer records. E.g. NAME,ADDRESS,CITY,COUNTRY,POSTCODE |
| 36 | `EB.XU.AUTH.SERV.USER.ID` | `EbExternalUser_AuthServUserId` | TField |  | Change the USER.ID of the EXTERNAL user with this value in Authentication Server |
| 37 | `EB.XU.ATTRIBUTES` | `EbExternalUser_Attributes` |  |  |  |
| 38 | `EB.XU.TXN.SIGN` | `EbExternalUser_TxnSign` | TField |  | This field determines the Type of Transaction Signing. Valid settings in this field are; SMS : One Time Password (OTP) will be sent to the Mail or Mobile as configured in the Authentication server Token : User will use the token given to generate One Time Password(OTP) |
| 39 | `EB.XU.SALT` | `EbExternalUser_Salt` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 40 | `EB.XU.SIGN.ON.RTN` | `EbExternalUser_SignOnRtn` |  |  |  |
| 41 | `EB.XU.LANGUAGE` | `EbExternalUser_Language` | TField | Yes | Indicates the Language in which the System should communicate with this User. All messages, instructions, Help Text etc. will be displayed when possible in the Language indicated by this definition. LANGUAGE is mandatory field. |
| 42 | `EB.XU.DATE.FORMAT` | `EbExternalUser_DateFormat` | TField | Yes | DATE.FORMAT field is used for deciding in which format the dates are to be displayed for a user. Validation Rules Valid values are 1, 2, 3 and 4. (dd) (month)(year) (DD)/(MM)/(YYYY) (YYYY)/(MM)/(DD YYYYMMDD DATE.FORMAT is mandatory field. |
| 43 | `EB.XU.RESERVED.05` | `EbExternalUser_Reserved05` | TField |  |  |
| 44 | `EB.XU.RESERVED.04` | `EbExternalUser_Reserved04` | TField |  |  |
| 45 | `EB.XU.RESERVED.03` | `EbExternalUser_Reserved03` | TField |  |  |
| 46 | `EB.XU.RESERVED.02` | `EbExternalUser_Reserved02` | TField |  |  |
| 47 | `EB.XU.RESERVED.01` | `EbExternalUser_Reserved01` | TField |  |  |
| 48 | `EB.XU.LOCAL.REF` | `EbExternalUser_LocalRef` |  |  |  |
| 49 | `EB.XU.OVERRIDE` | `EbExternalUser_Override` |  |  |  |
| 50 | `EB.XU.RECORD.STATUS` | `EbExternalUser_RecordStatus` | String |  |  |
| 51 | `EB.XU.CURR.NO` | `EbExternalUser_CurrNo` | String |  |  |
| 52 | `EB.XU.INPUTTER` | `EbExternalUser_Inputter` |  |  |  |
| 53 | `EB.XU.DATE.TIME` | `EbExternalUser_DateTime` |  |  |  |
| 54 | `EB.XU.AUTHORISER` | `EbExternalUser_Authoriser` | String |  |  |
| 55 | `EB.XU.CO.CODE` | `EbExternalUser_CoCode` | String |  |  |
| 56 | `EB.XU.DEPT.CODE` | `EbExternalUser_DeptCode` | String |  |  |
| 57 | `EB.XU.AUDITOR.CODE` | `EbExternalUser_AuditorCode` | String |  |  |
| 58 | `EB.XU.AUDIT.DATE.TIME` | `EbExternalUser_AuditDateTime` | String |  |  |
| 59 | `EB.XU.SUB.ARRANGEMENT` | `EbExternalUser_SubArrangement` |  |  |  |
