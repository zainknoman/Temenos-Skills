# MEETING.ENTITLEMENT — Table Schema

> Source: `INSERTS/I_F.MEETING.ENTITLEMENT` in `SC_SccEntitlements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.MEN.PORTFOLIO.NO` | `MeetingEntitlement_PortfolioNo` | TField |  | This field holds the portfolio Number to which the MEETING.ENTITLEMENT record is created for. Validation Rules: Must be a valid SEC.ACC.MASTER record. This is a NOINPUT field |
| 2 | `SC.MEN.SECURITY.NO` | `MeetingEntitlement_SecurityNo` | TField |  | This field holds the Security number for which the event is taking place. Updated from the originating MEETING.DIARY record. Validation Rules: This is a NOINPUT field |
| 3 | `SC.MEN.DEPOSITORY` | `MeetingEntitlement_Depository` | TField |  | This field holds the depository number the MEETING.ENTITLEMENT record related to. Validation Rules: This is a NOINPUT field |
| 4 | `SC.MEN.SUB.ACCOUNT` | `MeetingEntitlement_SubAccount` | TField |  | This field holds the sub account of the depository. Validation Rules: This is a NOINPUT field. |
| 5 | `SC.MEN.QUALIFY.HOLDING` | `MeetingEntitlement_QualifyHolding` | TField |  | This field denotes the portfolio Holding as on fixing Date. If fixing date is blank in the MEETING.DIARY record then this field will hold the portfolio Holding as on date ofcreation of MEETING.ENTITLEMENT record. |
| 6 | `SC.MEN.MEETING.DATE` | `MeetingEntitlement_MeetingDate` | TField |  | This field denotes the shareholders meeting date. Updated from the originating MEETING.DIARY record. Validation Rules: It is a NOINPUT field. |
| 7 | `SC.MEN.MEETING.TIME` | `MeetingEntitlement_MeetingTime` | TField |  | This field denotes the time of the meeting. Updated from the originating MEETING.DIARY record. Validation Rules: It is a NOINPUT field. |
| 8 | `SC.MEN.RESOLUTION.NO` | `MeetingEntitlement_ResolutionNo` |  |  |  |
| 9 | `SC.MEN.RESOLUTION.DESC` | `MeetingEntitlement_ResolutionDesc` |  |  |  |
| 10 | `SC.MEN.VOTE.TYPE` | `MeetingEntitlement_VoteType` |  |  |  |
| 11 | `SC.MEN.QTY.VOTED.FOR` | `MeetingEntitlement_QtyVotedFor` |  |  |  |
| 12 | `SC.MEN.ELECT.DATE` | `MeetingEntitlement_ElectDate` |  |  |  |
| 13 | `SC.MEN.ELECT.TIME` | `MeetingEntitlement_ElectTime` |  |  |  |
| 14 | `SC.MEN.ELECT.USER` | `MeetingEntitlement_ElectUser` |  |  |  |
| 15 | `SC.MEN.TOTAL.VOTES` | `MeetingEntitlement_TotalVotes` |  |  |  |
| 16 | `SC.MEN.PENDING.NOM` | `MeetingEntitlement_PendingNom` |  |  |  |
| 17 | `SC.MEN.DEF.INSTR.DATE` | `MeetingEntitlement_DefInstrDate` | TField |  | Noinput field that will contains the date on which the system will apply default instructions to theMEETING.ENTITLEMENTrecord. This field is populated from the DEF.INSTR.DATE field of the related MEETING.DIARY record. Validation Rules: Noinput field automatically populated by the system |
| 18 | `SC.MEN.AUT.AUTH.DATE` | `MeetingEntitlement_AutAuthDate` | TField |  | Noinput field that will contain the date on which the MEETING.ENTITLEMENT record will be automatically authorisedduringthe START.OF.DAY process. This field is populated from the ENT.AUTO.AUTH.DATE field of the related MEETING.DIARY record. Validation Rules: Noinput field automatically populated by the system |
| 19 | `SC.MEN.MANUAL.CREATION` | `MeetingEntitlement_ManualCreation` | TField |  | This field indicates whether the Meeting Entitlement is generated manually or through service. This field getsupdated to'YES' when the Meeting Entitlement is inputted manually. Validation Rules: No input field. |
| 20 | `SC.MEN.RESERVED02` | `MeetingEntitlement_Reserved02` | TField |  |  |
| 21 | `SC.MEN.RESERVED01` | `MeetingEntitlement_Reserved01` | TField |  |  |
| 22 | `SC.MEN.LOCAL.REF` | `MeetingEntitlement_LocalRef` |  |  |  |
| 23 | `SC.MEN.STMT.NOS` | `MeetingEntitlement_StmtNos` |  |  |  |
| 24 | `SC.MEN.OVERRIDE` | `MeetingEntitlement_Override` |  |  |  |
| 25 | `SC.MEN.RECORD.STATUS` | `MeetingEntitlement_RecordStatus` | String |  |  |
| 26 | `SC.MEN.CURR.NO` | `MeetingEntitlement_CurrNo` | String |  |  |
| 27 | `SC.MEN.INPUTTER` | `MeetingEntitlement_Inputter` |  |  |  |
| 28 | `SC.MEN.DATE.TIME` | `MeetingEntitlement_DateTime` |  |  |  |
| 29 | `SC.MEN.AUTHORISER` | `MeetingEntitlement_Authoriser` | String |  |  |
| 30 | `SC.MEN.CO.CODE` | `MeetingEntitlement_CoCode` | String |  |  |
| 31 | `SC.MEN.DEPT.CODE` | `MeetingEntitlement_DeptCode` | String |  |  |
| 32 | `SC.MEN.AUDITOR.CODE` | `MeetingEntitlement_AuditorCode` | String |  |  |
| 33 | `SC.MEN.AUDIT.DATE.TIME` | `MeetingEntitlement_AuditDateTime` | String |  |  |
