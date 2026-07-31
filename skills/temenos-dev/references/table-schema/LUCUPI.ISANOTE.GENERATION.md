# LUCUPI.ISANOTE.GENERATION — Table Schema

> Source: `INSERTS/I_F.LUCUPI.ISANOTE.GENERATION` in `LUCUPI_MultilineExtract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LUCUPI.ISANOTE.GEN.ISANOTE1.GENERATED` | `LucupiIsanoteGeneration_Isanote1Generated` | TField |  | This fieLd has values Yes or No. If the first ISANOTE is generated for the file or transaction, the value should be updated as Yes otherwise No. This is system-generated field. |
| 2 | `LUCUPI.ISANOTE.GEN.TOTAL.TRANSACTIONS` | `LucupiIsanoteGeneration_TotalTransactions` | TField |  | Total number of transactions in the pain file |
| 3 | `LUCUPI.ISANOTE.GEN.TRANSACTION.PROCESSED` | `LucupiIsanoteGeneration_TransactionProcessed` | TField |  | Reflects the number of transactions processed for the ISANOTE1 |
| 4 | `LUCUPI.ISANOTE.GEN.PENDING.TRANSACTIONS` | `LucupiIsanoteGeneration_PendingTransactions` | TField |  | Reflects the pending transactions to be processed for this file reference Usually takes value as TOTAL.TRANSACTIONS - TRANSACTION.PROCESSED |
| 5 | `LUCUPI.ISANOTE.GEN.PP.REFERENCE` | `LucupiIsanoteGeneration_PpReference` |  |  |  |
| 6 | `LUCUPI.ISANOTE.GEN.ISANOTE2.GENERATED` | `LucupiIsanoteGeneration_Isanote2Generated` | TField |  | This fieLd has values Yes, No or Part. The second ISANOTE will be generated if the value in this field is 'Part' and once the second ISANOTE is generated for the file or transaction, the value should be updated as Yes. This is system-generated field. |
| 7 | `LUCUPI.ISANOTE.GEN.RESERVED.1` | `LucupiIsanoteGeneration_Reserved1` | TField |  |  |
| 8 | `LUCUPI.ISANOTE.GEN.RESERVED.2` | `LucupiIsanoteGeneration_Reserved2` | TField |  |  |
| 9 | `LUCUPI.ISANOTE.GEN.RESERVED.3` | `LucupiIsanoteGeneration_Reserved3` | TField |  |  |
| 10 | `LUCUPI.ISANOTE.GEN.RESERVED.4` | `LucupiIsanoteGeneration_Reserved4` | TField |  |  |
| 11 | `LUCUPI.ISANOTE.GEN.RESERVED.5` | `LucupiIsanoteGeneration_Reserved5` | TField |  |  |
| 12 | `LUCUPI.ISANOTE.GEN.RESERVED.6` | `LucupiIsanoteGeneration_Reserved6` | TField |  |  |
| 13 | `LUCUPI.ISANOTE.GEN.RESERVED.7` | `LucupiIsanoteGeneration_Reserved7` | TField |  |  |
| 14 | `LUCUPI.ISANOTE.GEN.RESERVED.8` | `LucupiIsanoteGeneration_Reserved8` | TField |  |  |
| 15 | `LUCUPI.ISANOTE.GEN.RESERVED.9` | `LucupiIsanoteGeneration_Reserved9` | TField |  |  |
| 16 | `LUCUPI.ISANOTE.GEN.RESERVED.10` | `LucupiIsanoteGeneration_Reserved10` | TField |  |  |
| 17 | `LUCUPI.ISANOTE.GEN.OVERRIDE` | `LucupiIsanoteGeneration_Override` |  |  |  |
| 18 | `LUCUPI.ISANOTE.GEN.RECORD.STATUS` | `LucupiIsanoteGeneration_RecordStatus` | String |  |  |
| 19 | `LUCUPI.ISANOTE.GEN.CURR.NO` | `LucupiIsanoteGeneration_CurrNo` | String |  |  |
| 20 | `LUCUPI.ISANOTE.GEN.INPUTTER` | `LucupiIsanoteGeneration_Inputter` |  |  |  |
| 21 | `LUCUPI.ISANOTE.GEN.DATE.TIME` | `LucupiIsanoteGeneration_DateTime` |  |  |  |
| 22 | `LUCUPI.ISANOTE.GEN.AUTHORISER` | `LucupiIsanoteGeneration_Authoriser` | String |  |  |
| 23 | `LUCUPI.ISANOTE.GEN.CO.CODE` | `LucupiIsanoteGeneration_CoCode` | String |  |  |
| 24 | `LUCUPI.ISANOTE.GEN.DEPT.CODE` | `LucupiIsanoteGeneration_DeptCode` | String |  |  |
| 25 | `LUCUPI.ISANOTE.GEN.AUDITOR.CODE` | `LucupiIsanoteGeneration_AuditorCode` | String |  |  |
| 26 | `LUCUPI.ISANOTE.GEN.AUDIT.DATE.TIME` | `LucupiIsanoteGeneration_AuditDateTime` | String |  |  |
