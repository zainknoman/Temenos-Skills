# SC.MT548.MATCH.CODE — Table Schema

> Source: `INSERTS/I_F.SC.MT548.MATCH.CODE` in `SC_STP.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.MCE.DESCRIPTION` | `ScMt548MatchCode_Description` |  |  |  |
| 2 | `SC.MCE.APPLICATION.TYPE` | `ScMt548MatchCode_ApplicationType` | TField |  | Specifies the application type of the Matching code. Validation Rules: Allowed Input is S, L or M. S � Swift standard L � Local M - Indicates that match code is MX specific |
| 3 | `SC.MCE.ACTION.REQUIRED` | `ScMt548MatchCode_ActionRequired` | TField |  | This field would be updated by bank to state if this status needs further action. If action required is set to YES, this will be shown in ACTION.REQUIRED Field in SC.CTDY.MT548.INSTRUCT table |
| 4 | `SC.MCE.REASON.MANDATORY` | `ScMt548MatchCode_ReasonMandatory` | TField | Yes | This field Specifies whether REASON.CODE Field in SC.CTDY.MT548.INSTRUCT Table is Mandatory or Not. REASON.CODE in SC.CTDY.MT548.INSTRUCT Table is Mandatory if REASON.MANDATORY is checked Otherwise Not Mandatory |
| 5 | `SC.MCE.RESERVED.2` | `ScMt548MatchCode_Reserved2` |  |  |  |
| 6 | `SC.MCE.RESERVED.1` | `ScMt548MatchCode_Reserved1` |  |  |  |
| 7 | `SC.MCE.LOCAL.REF` | `ScMt548MatchCode_LocalRef` |  |  |  |
| 8 | `SC.MCE.OVERRIDE` | `ScMt548MatchCode_Override` |  |  |  |
| 9 | `SC.MCE.RECORD.STATUS` | `ScMt548MatchCode_RecordStatus` | String |  |  |
| 10 | `SC.MCE.CURR.NO` | `ScMt548MatchCode_CurrNo` | String |  |  |
| 11 | `SC.MCE.INPUTTER` | `ScMt548MatchCode_Inputter` |  |  |  |
| 12 | `SC.MCE.DATE.TIME` | `ScMt548MatchCode_DateTime` |  |  |  |
| 13 | `SC.MCE.AUTHORISER` | `ScMt548MatchCode_Authoriser` | String |  |  |
| 14 | `SC.MCE.CO.CODE` | `ScMt548MatchCode_CoCode` | String |  |  |
| 15 | `SC.MCE.DEPT.CODE` | `ScMt548MatchCode_DeptCode` | String |  |  |
| 16 | `SC.MCE.AUDITOR.CODE` | `ScMt548MatchCode_AuditorCode` | String |  |  |
| 17 | `SC.MCE.AUDIT.DATE.TIME` | `ScMt548MatchCode_AuditDateTime` | String |  |  |
