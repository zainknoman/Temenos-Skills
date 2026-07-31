# PP.PARTY.ROLE — Table Schema

> Source: `INSERTS/I_F.PP.PARTY.ROLE` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.PTR.PartyRole` | `PpPartyRole_Partyrole` |  |  |  |
| 2 | `PP.PTR.PartyRoleTag` | `PpPartyRole_Partyroletag` | TField | Yes | Specifies the tag number to be associated with the party role configured Validation Rules: Mandatory Field. 6 alphanumeric characters. |
| 3 | `PP.PTR.PartyRoleDescription` | `PpPartyRole_Partyroledescription` |  |  |  |
| 4 | `PP.PTR.LOCAL.REF` | `PpPartyRole_LocalRef` |  |  |  |
| 5 | `PP.PTR.RESERVED.5` | `PpPartyRole_Reserved5` | TField |  |  |
| 6 | `PP.PTR.RESERVED.4` | `PpPartyRole_Reserved4` | TField |  |  |
| 7 | `PP.PTR.RESERVED.3` | `PpPartyRole_Reserved3` | TField |  |  |
| 8 | `PP.PTR.RESERVED.2` | `PpPartyRole_Reserved2` | TField |  |  |
| 9 | `PP.PTR.RESERVED.1` | `PpPartyRole_Reserved1` | TField |  |  |
| 10 | `PP.PTR.OVERRIDE` | `PpPartyRole_Override` |  |  |  |
| 11 | `PP.PTR.RECORD.STATUS` | `PpPartyRole_RecordStatus` | String |  |  |
| 12 | `PP.PTR.CURR.NO` | `PpPartyRole_CurrNo` | String |  |  |
| 13 | `PP.PTR.INPUTTER` | `PpPartyRole_Inputter` |  |  |  |
| 14 | `PP.PTR.DATE.TIME` | `PpPartyRole_DateTime` |  |  |  |
| 15 | `PP.PTR.AUTHORISER` | `PpPartyRole_Authoriser` | String |  |  |
| 16 | `PP.PTR.CO.CODE` | `PpPartyRole_CoCode` | String |  |  |
| 17 | `PP.PTR.DEPT.CODE` | `PpPartyRole_DeptCode` | String |  |  |
| 18 | `PP.PTR.AUDITOR.CODE` | `PpPartyRole_AuditorCode` | String |  |  |
| 19 | `PP.PTR.AUDIT.DATE.TIME` | `PpPartyRole_AuditDateTime` | String |  |  |
