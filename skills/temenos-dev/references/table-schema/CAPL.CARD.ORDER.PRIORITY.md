# CAPL.CARD.ORDER.PRIORITY — Table Schema

> Source: `INSERTS/I_F.CAPL.CARD.ORDER.PRIORITY` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.CRD.PTY.DECSRIPTION` | `CaplCardOrderPriority_Decsription` | TField |  |  |
| 2 | `CAPL.CRD.PTY.RESERVED.9` | `CaplCardOrderPriority_Reserved9` | TField |  |  |
| 3 | `CAPL.CRD.PTY.RESERVED.8` | `CaplCardOrderPriority_Reserved8` | TField |  |  |
| 4 | `CAPL.CRD.PTY.RESERVED.7` | `CaplCardOrderPriority_Reserved7` | TField |  |  |
| 5 | `CAPL.CRD.PTY.RESERVED.6` | `CaplCardOrderPriority_Reserved6` | TField |  |  |
| 6 | `CAPL.CRD.PTY.RESERVED.5` | `CaplCardOrderPriority_Reserved5` | TField |  |  |
| 7 | `CAPL.CRD.PTY.RESERVED.4` | `CaplCardOrderPriority_Reserved4` | TField |  |  |
| 8 | `CAPL.CRD.PTY.RESERVED.3` | `CaplCardOrderPriority_Reserved3` | TField |  |  |
| 9 | `CAPL.CRD.PTY.RESERVED.2` | `CaplCardOrderPriority_Reserved2` | TField |  |  |
| 10 | `CAPL.CRD.PTY.RESERVED.1` | `CaplCardOrderPriority_Reserved1` | TField |  |  |
| 11 | `CAPL.CRD.PTY.LOCAL.REF` | `CaplCardOrderPriority_LocalRef` |  |  |  |
| 12 | `CAPL.CRD.PTY.OVERRIDE` | `CaplCardOrderPriority_Override` |  |  |  |
| 13 | `CAPL.CRD.PTY.RECORD.STATUS` | `CaplCardOrderPriority_RecordStatus` | String |  |  |
| 14 | `CAPL.CRD.PTY.CURR.NO` | `CaplCardOrderPriority_CurrNo` | String |  |  |
| 15 | `CAPL.CRD.PTY.INPUTTER` | `CaplCardOrderPriority_Inputter` |  |  |  |
| 16 | `CAPL.CRD.PTY.DATE.TIME` | `CaplCardOrderPriority_DateTime` |  |  |  |
| 17 | `CAPL.CRD.PTY.AUTHORISER` | `CaplCardOrderPriority_Authoriser` | String |  |  |
| 18 | `CAPL.CRD.PTY.CO.CODE` | `CaplCardOrderPriority_CoCode` | String |  |  |
| 19 | `CAPL.CRD.PTY.DEPT.CODE` | `CaplCardOrderPriority_DeptCode` | String |  |  |
| 20 | `CAPL.CRD.PTY.AUDITOR.CODE` | `CaplCardOrderPriority_AuditorCode` | String |  |  |
| 21 | `CAPL.CRD.PTY.AUDIT.DATE.TIME` | `CaplCardOrderPriority_AuditDateTime` | String |  |  |
