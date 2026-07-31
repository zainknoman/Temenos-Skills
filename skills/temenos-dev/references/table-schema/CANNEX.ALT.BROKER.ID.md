# CANNEX.ALT.BROKER.ID — Table Schema

> Source: `INSERTS/I_F.CANNEX.ALT.BROKER.ID` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CANNEX.ALT.BR.AGENT.ID` | `CannexAltBrokerId_AgentId` | TField |  |  |
| 2 | `CANNEX.ALT.BR.RESERVED.1` | `CannexAltBrokerId_Reserved1` | TField |  |  |
| 3 | `CANNEX.ALT.BR.RESERVED.2` | `CannexAltBrokerId_Reserved2` | TField |  |  |
| 4 | `CANNEX.ALT.BR.RESERVED.3` | `CannexAltBrokerId_Reserved3` | TField |  |  |
| 5 | `CANNEX.ALT.BR.RESERVED.4` | `CannexAltBrokerId_Reserved4` | TField |  |  |
| 6 | `CANNEX.ALT.BR.RESERVED.5` | `CannexAltBrokerId_Reserved5` | TField |  |  |
| 7 | `CANNEX.ALT.BR.RESERVED.6` | `CannexAltBrokerId_Reserved6` | TField |  |  |
| 8 | `CANNEX.ALT.BR.RESERVED.7` | `CannexAltBrokerId_Reserved7` | TField |  |  |
| 9 | `CANNEX.ALT.BR.RESERVED.8` | `CannexAltBrokerId_Reserved8` | TField |  |  |
| 10 | `CANNEX.ALT.BR.RESERVED.9` | `CannexAltBrokerId_Reserved9` | TField |  |  |
| 11 | `CANNEX.ALT.BR.RESERVED.10` | `CannexAltBrokerId_Reserved10` | TField |  |  |
| 12 | `CANNEX.ALT.BR.LOCAL.REF` | `CannexAltBrokerId_LocalRef` |  |  |  |
| 13 | `CANNEX.ALT.BR.OVERRIDE` | `CannexAltBrokerId_Override` |  |  |  |
| 14 | `CANNEX.ALT.BR.RECORD.STATUS` | `CannexAltBrokerId_RecordStatus` | String |  |  |
| 15 | `CANNEX.ALT.BR.CURR.NO` | `CannexAltBrokerId_CurrNo` | String |  |  |
| 16 | `CANNEX.ALT.BR.INPUTTER` | `CannexAltBrokerId_Inputter` |  |  |  |
| 17 | `CANNEX.ALT.BR.DATE.TIME` | `CannexAltBrokerId_DateTime` |  |  |  |
| 18 | `CANNEX.ALT.BR.AUTHORISER` | `CannexAltBrokerId_Authoriser` | String |  |  |
| 19 | `CANNEX.ALT.BR.CO.CODE` | `CannexAltBrokerId_CoCode` | String |  |  |
| 20 | `CANNEX.ALT.BR.DEPT.CODE` | `CannexAltBrokerId_DeptCode` | String |  |  |
| 21 | `CANNEX.ALT.BR.AUDITOR.CODE` | `CannexAltBrokerId_AuditorCode` | String |  |  |
| 22 | `CANNEX.ALT.BR.AUDIT.DATE.TIME` | `CannexAltBrokerId_AuditDateTime` | String |  |  |
