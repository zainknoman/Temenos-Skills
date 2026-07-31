# PP.SLA.PER.CODEWORD — Table Schema

> Source: `INSERTS/I_F.PP.SLA.PER.CODEWORD` in `PP_SLADeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.SLA.MessagePriority` | `PpSlaPerCodeword_Messagepriority` |  |  |  |
| 2 | `PP.SLA.CodeWord` | `PpSlaPerCodeword_Codeword` |  |  |  |
| 3 | `PP.SLA.CodeWordTag` | `PpSlaPerCodeword_Codewordtag` |  |  |  |
| 4 | `PP.SLA.CodeWordText` | `PpSlaPerCodeword_Codewordtext` |  |  |  |
| 5 | `PP.SLA.Ranking` | `PpSlaPerCodeword_Ranking` |  |  |  |
| 6 | `PP.SLA.SLAID` | `PpSlaPerCodeword_Slaid` |  |  |  |
| 7 | `PP.SLA.StartDate` | `PpSlaPerCodeword_Startdate` | TField |  | Specifies the date from which the record is to be considered as active for payments processing. Validation Rules: No Input Field If the start date is given in ID then the start date gets populated from the id Or else start date gets populated from the field TODAY in the table DATES |
| 8 | `PP.SLA.EndDate` | `PpSlaPerCodeword_Enddate` | TField |  | Specifies the date until which the record is to be considered as active for payments processing.Post this date, the record will be set as Inactive by the payments hub. |
| 9 | `PP.SLA.RESERVED.5` | `PpSlaPerCodeword_Reserved5` | TField |  |  |
| 10 | `PP.SLA.RESERVED.4` | `PpSlaPerCodeword_Reserved4` | TField |  |  |
| 11 | `PP.SLA.RESERVED.3` | `PpSlaPerCodeword_Reserved3` | TField |  |  |
| 12 | `PP.SLA.RESERVED.2` | `PpSlaPerCodeword_Reserved2` | TField |  |  |
| 13 | `PP.SLA.RESERVED.1` | `PpSlaPerCodeword_Reserved1` | TField |  |  |
| 14 | `PP.SLA.LOCAL.REF` | `PpSlaPerCodeword_LocalRef` |  |  |  |
| 15 | `PP.SLA.OVERRIDE` | `PpSlaPerCodeword_Override` |  |  |  |
| 16 | `PP.SLA.RECORD.STATUS` | `PpSlaPerCodeword_RecordStatus` | String |  |  |
| 17 | `PP.SLA.CURR.NO` | `PpSlaPerCodeword_CurrNo` | String |  |  |
| 18 | `PP.SLA.INPUTTER` | `PpSlaPerCodeword_Inputter` |  |  |  |
| 19 | `PP.SLA.DATE.TIME` | `PpSlaPerCodeword_DateTime` |  |  |  |
| 20 | `PP.SLA.AUTHORISER` | `PpSlaPerCodeword_Authoriser` | String |  |  |
| 21 | `PP.SLA.CO.CODE` | `PpSlaPerCodeword_CoCode` | String |  |  |
| 22 | `PP.SLA.DEPT.CODE` | `PpSlaPerCodeword_DeptCode` | String |  |  |
| 23 | `PP.SLA.AUDITOR.CODE` | `PpSlaPerCodeword_AuditorCode` | String |  |  |
| 24 | `PP.SLA.AUDIT.DATE.TIME` | `PpSlaPerCodeword_AuditDateTime` | String |  |  |
