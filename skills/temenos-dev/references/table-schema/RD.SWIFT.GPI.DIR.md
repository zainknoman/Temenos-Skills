# RD.SWIFT.GPI.DIR — Table Schema

> Source: `INSERTS/I_F.RD.SWIFT.GPI.DIR` in `RD_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RD.SGD.FLAG` | `RdSwiftGpiDir_Flag` | TField |  | A flag which indicates whether there is a change in the record, since the last release of the Swift GPI directory. Validation Rules: A - Addition M - Modification D - Deletion |
| 2 | `RD.SGD.SOURCE.KEY` | `RdSwiftGpiDir_SourceKey` | TField | Yes | The identifier of the record in the SWIFT gpi Directory Validation Rules: Mandatory field. |
| 3 | `RD.SGD.CBD.RECORDKEY` | `RdSwiftGpiDir_CbdRecordkey` | TField |  | The corresponding record key of the participant in the T24 Centralised Bank Directory, containing the participant's details Validation Rules: A maximum of 12 characters can be entered. |
| 4 | `RD.SGD.PLATFORM` | `RdSwiftGpiDir_Platform` | TField |  | Indicates the service platform. Validation Rules: A maximum of 8 characters can be entered. |
| 5 | `RD.SGD.SERVICE.ID` | `RdSwiftGpiDir_ServiceId` | TField |  | Service type identifier. For example, the value of field 111 in block 3 of the gpi MT 103. Validation Rules: A maximum of 3 characters can be entered. |
| 6 | `RD.SGD.SERVICE.NAME` | `RdSwiftGpiDir_ServiceName` | TField |  | Name of the service. Validation Rules: A maximum of 7 characters can be entered. |
| 7 | `RD.SGD.PARTICIPANT.ID` | `RdSwiftGpiDir_ParticipantId` | TField | Yes | Participant's routing ID, at which it is reachable for receiving gpi payments. It can be a BIC8 followed by XXX, a BIC8 followed by a 3-character branch code, or a clearing code (NATIONAL ID) of the non-FIN PMI. Validation Rules: Mandatory field. A maximum of 50 characters can be entered. |
| 8 | `RD.SGD.ID.TYPE` | `RdSwiftGpiDir_IdType` | TField |  | Type of the identifier used for the PARTICIPANT ID, such as the BIC or a NATIONAL ID of a non-FIN PMI. Validation Rules: Allowed values are BIC or NATIONAL ID |
| 9 | `RD.SGD.PARTICIPANT.NAME` | `RdSwiftGpiDir_ParticipantName` | TField |  | The institution name of the participant. Validation Rules: A maximum of 105 characters can be entered. |
| 10 | `RD.SGD.COUNTRY.CODE` | `RdSwiftGpiDir_CountryCode` | TField |  | The 2-character ISO country code of the participant. Validation Rules: Should be a valid Country from COUNTRY table |
| 11 | `RD.SGD.CURRENCY.CODE` | `RdSwiftGpiDir_CurrencyCode` | TField |  | The 3-character ISO currency code, accepted in field 32A of incoming gpi MT 103 payment by the Participant ID, or by the gpi intermediary (if any) through which the participant can be reached for this currency. Validation Rules: Should be a valid Country from CURRENCY table |
| 12 | `RD.SGD.CUT.OFF.TIME` | `RdSwiftGpiDir_CutOffTime` | TField |  | Participant's public gpi cut-off time for gpi payments in this currency Validation Rules: A maximum of 11 characters can be entered. |
| 13 | `RD.SGD.CUT.OFF.DAY` | `RdSwiftGpiDir_CutOffDay` | TField |  | CUT-OFF DAY can be empty (same day cut-off time) or can contain the value "D-n" (where n can be a value between 1 and 9). |
| 14 | `RD.SGD.LOCAL.TIME.ZONE` | `RdSwiftGpiDir_LocalTimeZone` | TField |  | Time zone of the participant. |
| 15 | `RD.SGD.ACT.AS.INTERMEDIARY` | `RdSwiftGpiDir_ActAsIntermediary` | TField |  | "Y" (Yes) or "N" (No) flag specifying whether the participant acts as the gpi Intermediary Agent for gpi payments in a given currency and over a given REACHABLE THROUGH channel (in field REACHABLE THROUGH) |
| 16 | `RD.SGD.REACHABLE.THROUGH` | `RdSwiftGpiDir_ReachableThrough` | TField |  | The channel through which the participant is reachable for gpi payment instructions for one of its gpi currencies. |
| 17 | `RD.SGD.CHANNEL.TYPE` | `RdSwiftGpiDir_ChannelType` | TField |  | The type of the REACHABLE THROUGH channel. Validation Rules: Allowed values are INTERMEDIARY, FIN-PMI, D-C, NON-FIN-PMI |
| 18 | `RD.SGD.START.DATE` | `RdSwiftGpiDir_StartDate` | TField |  | The future date when the record will become valid (including this day itself, if it is a business day). |
| 19 | `RD.SGD.STOP.DATE` | `RdSwiftGpiDir_StopDate` | TField |  | The future date until the record is valid (including this day itself, if it is a business day). |
| 20 | `RD.SGD.SSI.RECORD.KEY` | `RdSwiftGpiDir_SsiRecordKey` | TField |  | The record key of the Standing Settlement Instruction (SSI) in SWIFTRef's SSI Plus directory for this participant and currency. |
| 21 | `RD.SGD.DELEGATED.TO` | `RdSwiftGpiDir_DelegatedTo` | TField |  | The BIC which must take the action of forwarding the payment or updating the tracker on behalf of the participant ID. Validation Rules: It is a valid BIC of 8 characters. |
| 22 | `RD.SGD.ATTRIBUTE.15` | `RdSwiftGpiDir_Attribute15` |  |  |  |
| 23 | `RD.SGD.ATTRIBUTE.16` | `RdSwiftGpiDir_Attribute16` | TField |  | Not used. Reserved for future use. |
| 24 | `RD.SGD.ATTRIBUTE.17` | `RdSwiftGpiDir_Attribute17` | TField |  | Not used. Reserved for future use. |
| 25 | `RD.SGD.ATTRIBUTE.18` | `RdSwiftGpiDir_Attribute18` | TField |  | Not used. Reserved for future use. |
| 26 | `RD.SGD.ATTRIBUTE.19` | `RdSwiftGpiDir_Attribute19` | TField |  | Not used. Reserved for future use. |
| 27 | `RD.SGD.ATTRIBUTE.20` | `RdSwiftGpiDir_Attribute20` | TField |  | Not used. Reserved for future use. |
| 28 | `RD.SGD.ACTIVATION.DATE` | `RdSwiftGpiDir_ActivationDate` | TField |  | Not used. |
| 29 | `RD.SGD.FIELD.A` | `RdSwiftGpiDir_FieldA` | TField |  | Not used. Reserved for future use. |
| 30 | `RD.SGD.FIELD.B` | `RdSwiftGpiDir_FieldB` | TField |  | Not used. Reserved for future use. |
| 31 | `RD.SGD.FIELD.C` | `RdSwiftGpiDir_FieldC` | TField |  | Not used. Reserved for future use. |
| 32 | `RD.SGD.SOURCE.NAME` | `RdSwiftGpiDir_SourceName` | TField |  | This will be the name of the upload file through which the record in the directory has been created/amended Will be blank when a custom record is created/amended. Validation Rules: NOINPUT field |
| 33 | `RD.SGD.ENTRY.TYPE` | `RdSwiftGpiDir_EntryType` | TField |  | Will indicate if the entry is manually created (Custom record) or created by an upload process. Validation Rules: NOINPUT field. Can have values UPLOAD (if uploaded) or CUSTOM (if manually created). |
| 34 | `RD.SGD.STATUS` | `RdSwiftGpiDir_Status` | TField |  | Captures the status of the record Validation Rules: Can be either Blank or DELETE. Default value is blank. |
| 35 | `RD.SGD.ALLOWED.COMPANY` | `RdSwiftGpiDir_AllowedCompany` |  |  |  |
| 36 | `RD.SGD.EXCLUDED.COMPANY` | `RdSwiftGpiDir_ExcludedCompany` |  |  |  |
| 37 | `RD.SGD.RESERVED.10` | `RdSwiftGpiDir_Reserved10` | TField |  |  |
| 38 | `RD.SGD.RESERVED.9` | `RdSwiftGpiDir_Reserved9` | TField |  |  |
| 39 | `RD.SGD.RESERVED.8` | `RdSwiftGpiDir_Reserved8` | TField |  |  |
| 40 | `RD.SGD.RESERVED.7` | `RdSwiftGpiDir_Reserved7` | TField |  |  |
| 41 | `RD.SGD.RESERVED.6` | `RdSwiftGpiDir_Reserved6` | TField |  |  |
| 42 | `RD.SGD.RESERVED.5` | `RdSwiftGpiDir_Reserved5` | TField |  |  |
| 43 | `RD.SGD.RESERVED.4` | `RdSwiftGpiDir_Reserved4` | TField |  |  |
| 44 | `RD.SGD.RESERVED.3` | `RdSwiftGpiDir_Reserved3` | TField |  |  |
| 45 | `RD.SGD.RESERVED.2` | `RdSwiftGpiDir_Reserved2` | TField |  |  |
| 46 | `RD.SGD.RESERVED.1` | `RdSwiftGpiDir_Reserved1` | TField |  |  |
| 47 | `RD.SGD.LOCAL.REF` | `RdSwiftGpiDir_LocalRef` |  |  |  |
| 48 | `RD.SGD.OVERRIDE` | `RdSwiftGpiDir_Override` |  |  |  |
| 49 | `RD.SGD.RECORD.STATUS` | `RdSwiftGpiDir_RecordStatus` | String |  |  |
| 50 | `RD.SGD.CURR.NO` | `RdSwiftGpiDir_CurrNo` | String |  |  |
| 51 | `RD.SGD.INPUTTER` | `RdSwiftGpiDir_Inputter` |  |  |  |
| 52 | `RD.SGD.DATE.TIME` | `RdSwiftGpiDir_DateTime` |  |  |  |
| 53 | `RD.SGD.AUTHORISER` | `RdSwiftGpiDir_Authoriser` | String |  |  |
| 54 | `RD.SGD.CO.CODE` | `RdSwiftGpiDir_CoCode` | String |  |  |
| 55 | `RD.SGD.DEPT.CODE` | `RdSwiftGpiDir_DeptCode` | String |  |  |
| 56 | `RD.SGD.AUDITOR.CODE` | `RdSwiftGpiDir_AuditorCode` | String |  |  |
| 57 | `RD.SGD.AUDIT.DATE.TIME` | `RdSwiftGpiDir_AuditDateTime` | String |  |  |
