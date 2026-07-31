# GLROUP.ROLLUP.LOG — Table Schema

> Source: `INSERTS/I_F.GLROUP.ROLLUP.LOG` in `GLROUP_GLRollup.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GLROUP.LOG.DEBIT.ACCOUNT` | `GlRollupLog_DebitAccount` |  |  |  |
| 2 | `GLROUP.LOG.CREDIT.ACCOUNT` | `GlRollupLog_CreditAccount` |  |  |  |
| 3 | `GLROUP.LOG.AMOUNT` | `GlRollupLog_Amount` |  |  |  |
| 4 | `GLROUP.LOG.PROCESSING.DATE` | `GlRollupLog_ProcessingDate` |  |  |  |
| 5 | `GLROUP.LOG.TXN.REF` | `GlRollupLog_TxnRef` |  |  |  |
| 6 | `GLROUP.LOG.STATUS` | `GlRollupLog_Status` |  |  |  |
| 7 | `GLROUP.LOG.MESSAGE` | `GlRollupLog_Message` |  |  |  |
| 8 | `GLROUP.LOG.RESERVED.10` | `GlRollupLog_Reserved10` |  |  |  |
| 9 | `GLROUP.LOG.RESERVED.9` | `GlRollupLog_Reserved9` |  |  |  |
| 10 | `GLROUP.LOG.RESERVED.8` | `GlRollupLog_Reserved8` |  |  |  |
| 11 | `GLROUP.LOG.RESERVED.7` | `GlRollupLog_Reserved7` |  |  |  |
| 12 | `GLROUP.LOG.RESERVED.6` | `GlRollupLog_Reserved6` |  |  |  |
| 13 | `GLROUP.LOG.RESERVED.5` | `GlRollupLog_Reserved5` |  |  |  |
| 14 | `GLROUP.LOG.RESERVED.4` | `GlRollupLog_Reserved4` |  |  |  |
| 15 | `GLROUP.LOG.RESERVED.3` | `GlRollupLog_Reserved3` |  |  |  |
| 16 | `GLROUP.LOG.RESERVED.2` | `GlRollupLog_Reserved2` |  |  |  |
| 17 | `GLROUP.LOG.RESERVED.1` | `GlRollupLog_Reserved1` |  |  |  |
| 18 | `GLROUP.LOG.RECORD.STATUS` | `GlRollupLog_RecordStatus` |  |  |  |
| 19 | `GLROUP.LOG.CURR.NO` | `GlRollupLog_CurrNo` |  |  |  |
| 20 | `GLROUP.LOG.INPUTTER` | `GlRollupLog_Inputter` |  |  |  |
| 21 | `GLROUP.LOG.DATE.TIME` | `GlRollupLog_DateTime` |  |  |  |
| 22 | `GLROUP.LOG.AUTHORISER` | `GlRollupLog_Authoriser` |  |  |  |
| 23 | `GLROUP.LOG.CO.CODE` | `GlRollupLog_CoCode` |  |  |  |
| 24 | `GLROUP.LOG.DEPT.CODE` | `GlRollupLog_DeptCode` |  |  |  |
| 25 | `GLROUP.LOG.AUDITOR.CODE` | `GlRollupLog_AuditorCode` |  |  |  |
| 26 | `GLROUP.LOG.AUDIT.DATE.TIME` | `GlRollupLog_AuditDateTime` |  |  |  |
