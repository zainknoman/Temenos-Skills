# SC.ADR.GDR.DETS — Table Schema

> Source: `INSERTS/I_F.SC.ADR.GDR.DETS` in `SC_ScoSecurityMasterMaintenance.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.ADRGDR.CONVERT.TO.SECURITY` | `ScAdrGdrDets_ConvertToSecurity` |  |  |  |
| 2 | `SC.ADRGDR.REL.TYPE` | `ScAdrGdrDets_RelType` |  |  |  |
| 3 | `SC.ADRGDR.OLD.SEC.RATIO` | `ScAdrGdrDets_OldSecRatio` |  |  |  |
| 4 | `SC.ADRGDR.NEW.SEC.RATIO` | `ScAdrGdrDets_NewSecRatio` |  |  |  |
| 5 | `SC.ADRGDR.CONV.FEE.CODE` | `ScAdrGdrDets_ConvFeeCode` |  |  |  |
| 6 | `SC.ADRGDR.FEE.DAP` | `ScAdrGdrDets_FeeDap` |  |  |  |
| 7 | `SC.ADRGDR.ADR.GDR.CONV.AGENT` | `ScAdrGdrDets_AdrGdrConvAgent` |  |  |  |
| 8 | `SC.ADRGDR.RESERVED.8` | `ScAdrGdrDets_Reserved8` | TField |  |  |
| 9 | `SC.ADRGDR.RESERVED.7` | `ScAdrGdrDets_Reserved7` | TField |  |  |
| 10 | `SC.ADRGDR.RESERVED.6` | `ScAdrGdrDets_Reserved6` | TField |  |  |
| 11 | `SC.ADRGDR.RESERVED.5` | `ScAdrGdrDets_Reserved5` | TField |  |  |
| 12 | `SC.ADRGDR.RESERVED.4` | `ScAdrGdrDets_Reserved4` | TField |  |  |
| 13 | `SC.ADRGDR.RESERVED.3` | `ScAdrGdrDets_Reserved3` | TField |  |  |
| 14 | `SC.ADRGDR.RESERVED.2` | `ScAdrGdrDets_Reserved2` | TField |  |  |
| 15 | `SC.ADRGDR.RESERVED.1` | `ScAdrGdrDets_Reserved1` | TField |  |  |
| 16 | `SC.ADRGDR.LOCAL.REF` | `ScAdrGdrDets_LocalRef` |  |  |  |
| 17 | `SC.ADRGDR.OVERRIDE` | `ScAdrGdrDets_Override` |  |  |  |
| 18 | `SC.ADRGDR.RECORD.STATUS` | `ScAdrGdrDets_RecordStatus` | String |  |  |
| 19 | `SC.ADRGDR.CURR.NO` | `ScAdrGdrDets_CurrNo` | String |  |  |
| 20 | `SC.ADRGDR.INPUTTER` | `ScAdrGdrDets_Inputter` |  |  |  |
| 21 | `SC.ADRGDR.DATE.TIME` | `ScAdrGdrDets_DateTime` |  |  |  |
| 22 | `SC.ADRGDR.AUTHORISER` | `ScAdrGdrDets_Authoriser` | String |  |  |
| 23 | `SC.ADRGDR.CO.CODE` | `ScAdrGdrDets_CoCode` | String |  |  |
| 24 | `SC.ADRGDR.DEPT.CODE` | `ScAdrGdrDets_DeptCode` | String |  |  |
| 25 | `SC.ADRGDR.AUDITOR.CODE` | `ScAdrGdrDets_AuditorCode` | String |  |  |
| 26 | `SC.ADRGDR.AUDIT.DATE.TIME` | `ScAdrGdrDets_AuditDateTime` | String |  |  |
