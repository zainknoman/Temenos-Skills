# ST.TRANSFER.RULE — Table Schema

> Source: `INSERTS/I_F.ST.TRANSFER.RULE` in `ST_Payments.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.TRR.DESCRIPTION` | `StTransferRule_Description` |  |  |  |
| 2 | `ST.TRR.RULE.API` | `StTransferRule_RuleApi` |  |  |  |
| 3 | `ST.TRR.RESERVED.10` | `StTransferRule_Reserved10` | TField |  |  |
| 4 | `ST.TRR.RESERVED.9` | `StTransferRule_Reserved9` | TField |  |  |
| 5 | `ST.TRR.RESERVED.8` | `StTransferRule_Reserved8` | TField |  |  |
| 6 | `ST.TRR.RESERVED.7` | `StTransferRule_Reserved7` | TField |  |  |
| 7 | `ST.TRR.RESERVED.6` | `StTransferRule_Reserved6` | TField |  |  |
| 8 | `ST.TRR.RESERVED.5` | `StTransferRule_Reserved5` | TField |  |  |
| 9 | `ST.TRR.RESERVED.4` | `StTransferRule_Reserved4` | TField |  |  |
| 10 | `ST.TRR.RESERVED.3` | `StTransferRule_Reserved3` | TField |  |  |
| 11 | `ST.TRR.RESERVED.2` | `StTransferRule_Reserved2` | TField |  |  |
| 12 | `ST.TRR.RESERVED.1` | `StTransferRule_Reserved1` | TField |  |  |
| 13 | `ST.TRR.LOCAL.REF` | `StTransferRule_LocalRef` |  |  |  |
| 14 | `ST.TRR.OVERRIDE` | `StTransferRule_Override` |  |  |  |
| 15 | `ST.TRR.RECORD.STATUS` | `StTransferRule_RecordStatus` | String |  |  |
| 16 | `ST.TRR.CURR.NO` | `StTransferRule_CurrNo` | String |  |  |
| 17 | `ST.TRR.INPUTTER` | `StTransferRule_Inputter` |  |  |  |
| 18 | `ST.TRR.DATE.TIME` | `StTransferRule_DateTime` |  |  |  |
| 19 | `ST.TRR.AUTHORISER` | `StTransferRule_Authoriser` | String |  |  |
| 20 | `ST.TRR.CO.CODE` | `StTransferRule_CoCode` | String |  |  |
| 21 | `ST.TRR.DEPT.CODE` | `StTransferRule_DeptCode` | String |  |  |
| 22 | `ST.TRR.AUDITOR.CODE` | `StTransferRule_AuditorCode` | String |  |  |
| 23 | `ST.TRR.AUDIT.DATE.TIME` | `StTransferRule_AuditDateTime` | String |  |  |
