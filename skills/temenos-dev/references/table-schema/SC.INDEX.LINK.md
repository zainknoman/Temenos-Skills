# SC.INDEX.LINK — Table Schema

> Source: `INSERTS/I_F.SC.INDEX.LINK` in `SC_ScoSecurityMasterMaintenance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.IND.INDEX.EFF.DATE` | `ScIndexLink_IndexEffDate` | TField |  | Date on which Inflation index is Effective. Defaulted from Effective Date given in the ID. |
| 2 | `SC.IND.INDEX.FACTOR` | `ScIndexLink_IndexFactor` | TField |  | The index factor which will be used for all the transactions thatoccur on or after the effective date. |
| 3 | `SC.IND.ABS.INDEX.ISSUE` | `ScIndexLink_AbsIndexIssue` | TField |  | An information only field. This field will hold the absolute inflation value at the time of issue of the instrument. |
| 4 | `SC.IND.RESERVED1` | `ScIndexLink_Reserved1` | TField |  |  |
| 5 | `SC.IND.RESERVED2` | `ScIndexLink_Reserved2` | TField |  |  |
| 6 | `SC.IND.RESERVED3` | `ScIndexLink_Reserved3` | TField |  |  |
| 7 | `SC.IND.RESERVED4` | `ScIndexLink_Reserved4` | TField |  |  |
| 8 | `SC.IND.RESERVED5` | `ScIndexLink_Reserved5` | TField |  |  |
| 9 | `SC.IND.RESERVED6` | `ScIndexLink_Reserved6` | TField |  |  |
| 10 | `SC.IND.RESERVED7` | `ScIndexLink_Reserved7` | TField |  |  |
| 11 | `SC.IND.RESERVED8` | `ScIndexLink_Reserved8` | TField |  |  |
| 12 | `SC.IND.RESERVED9` | `ScIndexLink_Reserved9` | TField |  |  |
| 13 | `SC.IND.RESERVED10` | `ScIndexLink_Reserved10` | TField |  |  |
| 14 | `SC.IND.RESERVED11` | `ScIndexLink_Reserved11` | TField |  |  |
| 15 | `SC.IND.RESERVED12` | `ScIndexLink_Reserved12` | TField |  |  |
| 16 | `SC.IND.RESERVED13` | `ScIndexLink_Reserved13` | TField |  |  |
| 17 | `SC.IND.RESERVED14` | `ScIndexLink_Reserved14` | TField |  |  |
| 18 | `SC.IND.RESERVED15` | `ScIndexLink_Reserved15` | TField |  |  |
| 19 | `SC.IND.RESERVED16` | `ScIndexLink_Reserved16` | TField |  |  |
| 20 | `SC.IND.RESERVED17` | `ScIndexLink_Reserved17` | TField |  |  |
| 21 | `SC.IND.RESERVED18` | `ScIndexLink_Reserved18` | TField |  |  |
| 22 | `SC.IND.LOCAL.REF` | `ScIndexLink_LocalRef` |  |  |  |
| 23 | `SC.IND.OVERRIDE` | `ScIndexLink_Override` |  |  |  |
| 24 | `SC.IND.RECORD.STATUS` | `ScIndexLink_RecordStatus` | String |  |  |
| 25 | `SC.IND.CURR.NO` | `ScIndexLink_CurrNo` | String |  |  |
| 26 | `SC.IND.INPUTTER` | `ScIndexLink_Inputter` |  |  |  |
| 27 | `SC.IND.DATE.TIME` | `ScIndexLink_DateTime` |  |  |  |
| 28 | `SC.IND.AUTHORISER` | `ScIndexLink_Authoriser` | String |  |  |
| 29 | `SC.IND.CO.CODE` | `ScIndexLink_CoCode` | String |  |  |
| 30 | `SC.IND.DEPT.CODE` | `ScIndexLink_DeptCode` | String |  |  |
| 31 | `SC.IND.AUDITOR.CODE` | `ScIndexLink_AuditorCode` | String |  |  |
| 32 | `SC.IND.AUDIT.DATE.TIME` | `ScIndexLink_AuditDateTime` | String |  |  |
