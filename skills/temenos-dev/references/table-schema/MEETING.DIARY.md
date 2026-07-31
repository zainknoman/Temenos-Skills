# MEETING.DIARY — Table Schema

> Source: `INSERTS/I_F.MEETING.DIARY` in `SC_SccEventCapture.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.DMT.SECURITY.NO` | `MeetingDiary_SecurityNo` | TField |  | This field denotes the security number that this Meeting Diary record relates to. Validation Rules: Input can be a valid SECURITY.MASTER ID, a Security Mnemonic or a Security Alternative Index. |
| 2 | `SC.DMT.EVENT.TYPE` | `MeetingDiary_EventType` | TField |  | This field denotes the event type of incoming MX message. This must be a valid DIARY.TYPE record where MEETING.EVENT.MX is set to Yes. |
| 3 | `SC.DMT.DEPOSITORY` | `MeetingDiary_Depository` | TField |  | This field denotes the depository from whom the notice is originated from. ALL will not be supported. If there are multiple depositories MEETING.DIARY record needs to be created for each depository. |
| 4 | `SC.DMT.CURR.FUNC` | `MeetingDiary_CurrFunc` | TField |  | This field is to capture the latest notification type. The function must contain any of the codes like NEWM, REPL, etc. The valid functions will be defined by EB.LOOKUP table - MSG.FUNC*(NEWM,REPL,RMDR) |
| 5 | `SC.DMT.CURR.STATUS.CODE` | `MeetingDiary_CurrStatusCode` | TField |  | This field is to capture the event completion status. The valid statuses will be defined by EB.LOOKUP table - MSG.STATUS*(COMP,INCO) |
| 6 | `SC.DMT.CONF.STATUS` | `MeetingDiary_ConfStatus` | TField |  | This field specifies the status of the occurrence of an event. Possible values are CONF or UCON. |
| 7 | `SC.DMT.MEETING.ID` | `MeetingDiary_MeetingId` | TField |  | This field denotes the unique id assigned to the meeting by the sender of the message. Validation Rules: A maximum of 35 characters may be entered. |
| 8 | `SC.DMT.ISSR.MEETING.ID` | `MeetingDiary_IssrMeetingId` | TField |  | This field denotes the unique id assigned to the meeting by the issuer. Validation Rules: A maximum of 35 characters may be entered. |
| 9 | `SC.DMT.CAEV.TYPE` | `MeetingDiary_CaevType` | TField |  | This field denotes the type of security holders meeting i.e. the event indicator. |
| 10 | `SC.DMT.CLASSIFICATION.TYPE` | `MeetingDiary_ClassificationType` | TField |  | This field denotes the classification of the meeting. eg. AMET. This will be mapped from the incoming message. |
| 11 | `SC.DMT.CTCT.PRSN.NAME` | `MeetingDiary_CtctPrsnName` | TField |  | This field denotes the contact person at the party organising the meeting either at the issuer or at anintermediary. Validation Rules: A maximum of 35 characters may be entered. |
| 12 | `SC.DMT.CTCT.TYPE` | `MeetingDiary_CtctType` |  |  |  |
| 13 | `SC.DMT.CTCT.VALUE` | `MeetingDiary_CtctValue` |  |  |  |
| 14 | `SC.DMT.RESULT.DATE` | `MeetingDiary_ResultDate` | TField |  | This field denotes the date on which the company publishes the result of the meeting. Validation Rules: Standard T24 Date format. |
| 15 | `SC.DMT.FIXING.DATE` | `MeetingDiary_FixingDate` | TField |  | All the shareholders of the security specified as on this date are entitled for the event. eg. Record Date Validation Rules: Standard T24 Date format. |
| 16 | `SC.DMT.MEETING.DATE` | `MeetingDiary_MeetingDate` | TField |  | This field denotes the shareholders meeting date. Validation Rules: Standard T24 Date format. |
| 17 | `SC.DMT.MEETING.TIME` | `MeetingDiary_MeetingTime` | TField |  | This field denotes the time of the meeting. |
| 18 | `SC.DMT.MEET.ADDR.TYPE` | `MeetingDiary_MeetAddrType` |  |  |  |
| 19 | `SC.DMT.MEET.ADDR.LINE` | `MeetingDiary_MeetAddrLine` |  |  |  |
| 20 | `SC.DMT.MEET.STREET.NAME` | `MeetingDiary_MeetStreetName` |  |  |  |
| 21 | `SC.DMT.MEET.BLDG.NUM` | `MeetingDiary_MeetBldgNum` |  |  |  |
| 22 | `SC.DMT.MEET.POST.CODE` | `MeetingDiary_MeetPostCode` |  |  |  |
| 23 | `SC.DMT.MEET.TOWN.NAME` | `MeetingDiary_MeetTownName` |  |  |  |
| 24 | `SC.DMT.MEET.CTRY.SUB.DIV` | `MeetingDiary_MeetCtrySubDiv` |  |  |  |
| 25 | `SC.DMT.MEET.COUNTRY` | `MeetingDiary_MeetCountry` |  |  |  |
| 26 | `SC.DMT.ISSUER.BIC` | `MeetingDiary_IssuerBic` | TField |  | This field denotes the BIC of the issuer of the security to which this meeting event applies. When this is present then the issuer name and address cannot be set. |
| 27 | `SC.DMT.ISSUER.NAME` | `MeetingDiary_IssuerName` | TField |  | This field denotes the name of the issuer of the security to which this meeting event applies. When the issuer name is given then the ISSUER.BIC cannot be given. Validation Rules: A maximum of 350 characters may be entered. |
| 28 | `SC.DMT.ISSUER.ADDR.TYPE` | `MeetingDiary_IssuerAddrType` | TField |  | This field identifies the nature of postal address. |
| 29 | `SC.DMT.ISSUER.ADDR.LINE` | `MeetingDiary_IssuerAddrLine` | TField |  | This field provides the address of the issuer. Validation Rules: A maximum of 70 characters may be entered. |
| 30 | `SC.DMT.ISSUER.STREET.NAME` | `MeetingDiary_IssuerStreetName` | TField |  | This field provides the street name where the issuer's building is located. Validation Rules: A maximum of 70 characters may be entered. |
| 31 | `SC.DMT.ISSUER.BLDG.NUM` | `MeetingDiary_IssuerBldgNum` | TField |  | This field provides the issuer's building number. Validation Rules: A maximum of 16 characters may be entered. |
| 32 | `SC.DMT.ISSUER.POST.CODE` | `MeetingDiary_IssuerPostCode` | TField |  | This field provides the postal code of the issuer building location. Validation Rules: A maximum of 16 characters may be entered. |
| 33 | `SC.DMT.ISSUER.TOWN.NAME` | `MeetingDiary_IssuerTownName` | TField |  | This field denotes the town name of the issuer's building. Validation Rules: A maximum of 35 characters may be entered. |
| 34 | `SC.DMT.ISSUER.CTRY.SUB.DIV` | `MeetingDiary_IssuerCtrySubDiv` | TField |  | This field denotes the region / state of the issuer's building location. Validation Rules: A maximum of 35 characters may be entered. |
| 35 | `SC.DMT.ISSUER.COUNTRY` | `MeetingDiary_IssuerCountry` | TField |  | This field denotes the country code of the issuer's location. Validation Rules: Must be the key to a valid entry on the COUNTRY file. |
| 36 | `SC.DMT.RESOLUTION.NO` | `MeetingDiary_ResolutionNo` |  |  |  |
| 37 | `SC.DMT.LANGUAGE` | `MeetingDiary_Language` |  |  |  |
| 38 | `SC.DMT.DESCRIPTION` | `MeetingDiary_Description` |  |  |  |
| 39 | `SC.DMT.FOR.INFO.ONLY` | `MeetingDiary_ForInfoOnly` |  |  |  |
| 40 | `SC.DMT.STATUS` | `MeetingDiary_Status` |  |  |  |
| 41 | `SC.DMT.VOTE.INSTR.TYPE` | `MeetingDiary_VoteInstrType` |  |  |  |
| 42 | `SC.DMT.ENTITLEMENT.RATIO` | `MeetingDiary_EntitlementRatio` |  |  |  |
| 43 | `SC.DMT.ENTITLEMENT.DESC` | `MeetingDiary_EntitlementDesc` |  |  |  |
| 44 | `SC.DMT.PARTIAL.VOTE` | `MeetingDiary_PartialVote` | TField |  | This field denotes whether part of the position can be un-voted. Possible values True or False. Yes = True; Blank = False. |
| 45 | `SC.DMT.SPLIT.VOTE` | `MeetingDiary_SplitVote` | TField |  | This field denotes whether the vote can be split i.e. a shareholder can cast different votes for different partsof the holding. Possible values True or False. Yes = True; Blank = False. |
| 46 | `SC.DMT.VOTE.DEADLINE.DATE` | `MeetingDiary_VoteDeadlineDate` | TField |  | This field denotes the date by which the vote instructions should be submitted. |
| 47 | `SC.DMT.VOTE.DEADLINE.TIME` | `MeetingDiary_VoteDeadlineTime` | TField |  | This field denotes the time by which the vote instructions should be submitted. |
| 48 | `SC.DMT.VOTE.MTHD.TYPE` | `MeetingDiary_VoteMthdType` |  |  |  |
| 49 | `SC.DMT.VOTE.MTHD` | `MeetingDiary_VoteMthd` |  |  |  |
| 50 | `SC.DMT.VOTE.ADDR.TYPE` | `MeetingDiary_VoteAddrType` |  |  |  |
| 51 | `SC.DMT.VOTE.ADDR.LINE` | `MeetingDiary_VoteAddrLine` |  |  |  |
| 52 | `SC.DMT.VOTE.STREET.NAME` | `MeetingDiary_VoteStreetName` |  |  |  |
| 53 | `SC.DMT.VOTE.BLDG.NUM` | `MeetingDiary_VoteBldgNum` |  |  |  |
| 54 | `SC.DMT.VOTE.POST.CODE` | `MeetingDiary_VotePostCode` |  |  |  |
| 55 | `SC.DMT.VOTE.TOWN.NAME` | `MeetingDiary_VoteTownName` |  |  |  |
| 56 | `SC.DMT.VOTE.CTRY.SUB.DIV` | `MeetingDiary_VoteCtrySubDiv` |  |  |  |
| 57 | `SC.DMT.VOTE.COUNTRY` | `MeetingDiary_VoteCountry` |  |  |  |
| 58 | `SC.DMT.REVOKE.DATE` | `MeetingDiary_RevokeDate` | TField |  | This field holds the date until which the instructing party can revoke, change or withdraw its votinginstruction. Validation Rules: Standard T24 Date format. |
| 59 | `SC.DMT.REVOKE.TIME` | `MeetingDiary_RevokeTime` | TField |  | This field holds the time until which the instructing party can revoke, change or withdraw its votinginstruction. |
| 60 | `SC.DMT.DELIVERY.INREF` | `MeetingDiary_DeliveryInref` | TField |  | This field will hold the inward delivery reference. |
| 61 | `SC.DMT.PRE.ADVICE.REQ` | `MeetingDiary_PreAdviceReq` | TField |  | This field determines whether pre confirmation advices are generated when MEETING.DIARY is created The value will be defaulted from the relevant DIARY.TYPE record. |
| 62 | `SC.DMT.CONFIRM.REQ` | `MeetingDiary_ConfirmReq` | TField |  | This field determines whether confirmation advices are generated when meeting entitlements are created via thisMEETING.DIARY record. The value will be defaulted from the relevant DIARY.TYPE record. |
| 63 | `SC.DMT.RERUN` | `MeetingDiary_Rerun` | TField |  | This field will allow the user to regenerate the MEETING.ENTITLEMENT record for a MEETING.DIARY. Options Allowed Yes, NULL If the field is set to Yes, then the MEETING.ENTITLEMENT records for the MEETING.DIARY will be regenerated toreflect the changes made to the MEETING.DIARY. |
| 64 | `SC.DMT.RETAIN.OPTION` | `MeetingDiary_RetainOption` | TField |  | When this field is set to YES, then on rerunning the service those Meeting Entitlements records where the optionis chosen will be retained. |
| 65 | `SC.DMT.STP` | `MeetingDiary_Stp` | TField |  | This field is only for informatory purpose and will determine whether the Meeting Diary caters to Full STP. |
| 66 | `SC.DMT.DEF.INSTR.DATE` | `MeetingDiary_DefInstrDate` | TField |  | This field holds the date on which the Start of Day process will apply default vote option to theMEETING.ENTITLEMENT records This field is automatically populated from the parameters entered in the related DIARY.TYPE record. This field can also be amended by the user. |
| 67 | `SC.DMT.ENT.AUTO.AUTH.DATE` | `MeetingDiary_EntAutoAuthDate` | TField |  | This field holds the date on which the Start of Day process will automatically authorize the MEETING.ENTITLEMENTrecord. This field is automatically populated from the parameters entered in the related DIARY.TYPE record. This field can also be amended by the user. |
| 68 | `SC.DMT.RESOLUTION.NUM` | `MeetingDiary_ResolutionNum` |  |  |  |
| 69 | `SC.DMT.SUB.ACC.OPT.QTY` | `MeetingDiary_SubAccOptQty` |  |  |  |
| 70 | `SC.DMT.INIT.ADVICE.SENT` | `MeetingDiary_InitAdviceSent` | TField |  | This field indicates whether initial advice is sent from meeting diary Validation Rules Noinput Field |
| 71 | `SC.DMT.RESERVED05` | `MeetingDiary_Reserved05` |  |  |  |
| 72 | `SC.DMT.RESERVED04` | `MeetingDiary_Reserved04` |  |  |  |
| 73 | `SC.DMT.RESERVED03` | `MeetingDiary_Reserved03` |  |  |  |
| 74 | `SC.DMT.RESERVED02` | `MeetingDiary_Reserved02` |  |  |  |
| 75 | `SC.DMT.RESERVED01` | `MeetingDiary_Reserved01` |  |  |  |
| 76 | `SC.DMT.LOCAL.REF` | `MeetingDiary_LocalRef` |  |  |  |
| 77 | `SC.DMT.STMT.NOS` | `MeetingDiary_StmtNos` |  |  |  |
| 78 | `SC.DMT.OVERRIDE` | `MeetingDiary_Override` |  |  |  |
| 79 | `SC.DMT.RECORD.STATUS` | `MeetingDiary_RecordStatus` | String |  |  |
| 80 | `SC.DMT.CURR.NO` | `MeetingDiary_CurrNo` | String |  |  |
| 81 | `SC.DMT.INPUTTER` | `MeetingDiary_Inputter` |  |  |  |
| 82 | `SC.DMT.DATE.TIME` | `MeetingDiary_DateTime` |  |  |  |
| 83 | `SC.DMT.AUTHORISER` | `MeetingDiary_Authoriser` | String |  |  |
| 84 | `SC.DMT.CO.CODE` | `MeetingDiary_CoCode` | String |  |  |
| 85 | `SC.DMT.DEPT.CODE` | `MeetingDiary_DeptCode` | String |  |  |
| 86 | `SC.DMT.AUDITOR.CODE` | `MeetingDiary_AuditorCode` | String |  |  |
| 87 | `SC.DMT.AUDIT.DATE.TIME` | `MeetingDiary_AuditDateTime` | String |  |  |
