# PP.CHATS.DIRECTORY — Table Schema

> Source: `INSERTS/I_F.PP.CHATS.DIRECTORY` in `PP_RoutingAndSettlementService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.TCD.CompanyID` | `PpChatsDirectory_Companyid` | TField |  | Indicates the Financial Table Descriptive(FTD) company for which the record is created. This is NoInput field It gets autopopulated after validation Example : BNK,GB1 |
| 2 | `PP.TCD.MemberIdentifierBIC` | `PpChatsDirectory_Memberidentifierbic` | TField | Yes | BIC Code of the CHATS member bank. Validation Rules: Input is mandatory for this field Can accept upto 35 alphanumeric characters. |
| 3 | `PP.TCD.ClearingCode` | `PpChatsDirectory_Clearingcode` | TField | Yes | Holds the Clearing code for which this record is created. Validation Rules: Accepts upto 10 alpha characters.Input to this field is mandatory. |
| 4 | `PP.TCD.CurrencyCode` | `PpChatsDirectory_Currencycode` | TField | Yes | Holds the Clearing Currency for which this CHATS directory record is created. Possible Values: HKD(HongKong Dollar) CNY(Chinese Yuan) EUR(Euro) USD(US Dollar) Validation Rules: Input is mandatory for this field |
| 5 | `PP.TCD.TargetBankBIC` | `PpChatsDirectory_Targetbankbic` | TField |  | BIC Code of the bank to be reached. Validation Rules: Can accept upto 35 alphanumeric characters. |
| 6 | `PP.TCD.InstitutionName` | `PpChatsDirectory_Institutionname` | TField | Yes | Holds name of the institution. Validation Rules: Input is mandatory for this field Can accept upto 105 alphanumeric characters. |
| 7 | `PP.TCD.ParticipationType` | `PpChatsDirectory_Participationtype` | TField | Yes | Holds the type of relationship the member bank holds with CHATS clearing. Possible Values: DP - Direct Participant IP - Indirect Participant ICU - Indirect Chart User Validation Rules: Input to this field is mandatory. |
| 8 | `PP.TCD.DirectParticipantIdentifier` | `PpChatsDirectory_Directparticipantidentifier` | TField | Yes | Holds the BIC Code of the Direct Participant If the member identifier is a DP then this BIC is the same as the Member Identifier If the member identifier is a IP or ICU then this BIC corresponds to the BIC of the Direct Participant. Validation Rules: Input is mandatory for this field Can accept upto 35 alphanumeric characters. |
| 9 | `PP.TCD.ClearingCodeTargetBank` | `PpChatsDirectory_Clearingcodetargetbank` | TField |  | Holds the Clearing code for the Bank to be reached. Validation Rules: Accepts upto 11 alphanumeric characters |
| 10 | `PP.TCD.ClearingCodeMemberBank` | `PpChatsDirectory_Clearingcodememberbank` | TField |  | Holds the Clearing code for the Member Bank. Validation Rules: Accepts upto 11 alphanumeric characters |
| 11 | `PP.TCD.OverrideThroughUpload` | `PpChatsDirectory_Overridethroughupload` | TField | Yes | Controls the record entry through automatic upload process. Possible Values Y � The entry is manually updated and can be overridden by the upload process. N � The entry is manual updated and the upload process should not override it. Validation Rules: Input to this field is mandatory. |
| 12 | `PP.TCD.StartDate` | `PpChatsDirectory_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. Validation Rules: No Input Field If the start date is given in ID then it gets populated from the id Or else start date gets populated from the field TODAY in the table DATES |
| 13 | `PP.TCD.EndDate` | `PpChatsDirectory_Enddate` | TField | Yes | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. Validation Rules: Input is mandatory for this field |
| 14 | `PP.TCD.RESERVED.5` | `PpChatsDirectory_Reserved5` | TField |  |  |
| 15 | `PP.TCD.RESERVED.4` | `PpChatsDirectory_Reserved4` | TField |  |  |
| 16 | `PP.TCD.RESERVED.3` | `PpChatsDirectory_Reserved3` | TField |  |  |
| 17 | `PP.TCD.RESERVED.2` | `PpChatsDirectory_Reserved2` | TField |  |  |
| 18 | `PP.TCD.RESERVED.1` | `PpChatsDirectory_Reserved1` | TField |  |  |
| 19 | `PP.TCD.LOCAL.REF` | `PpChatsDirectory_LocalRef` |  |  |  |
| 20 | `PP.TCD.LinkID` | `PpChatsDirectory_Linkid` | TField |  |  |
| 21 | `PP.TCD.OVERRIDE` | `PpChatsDirectory_Override` |  |  |  |
| 22 | `PP.TCD.RECORD.STATUS` | `PpChatsDirectory_RecordStatus` | String |  |  |
| 23 | `PP.TCD.CURR.NO` | `PpChatsDirectory_CurrNo` | String |  |  |
| 24 | `PP.TCD.INPUTTER` | `PpChatsDirectory_Inputter` |  |  |  |
| 25 | `PP.TCD.DATE.TIME` | `PpChatsDirectory_DateTime` |  |  |  |
| 26 | `PP.TCD.AUTHORISER` | `PpChatsDirectory_Authoriser` | String |  |  |
| 27 | `PP.TCD.CO.CODE` | `PpChatsDirectory_CoCode` | String |  |  |
| 28 | `PP.TCD.DEPT.CODE` | `PpChatsDirectory_DeptCode` | String |  |  |
| 29 | `PP.TCD.AUDITOR.CODE` | `PpChatsDirectory_AuditorCode` | String |  |  |
| 30 | `PP.TCD.AUDIT.DATE.TIME` | `PpChatsDirectory_AuditDateTime` | String |  |  |
