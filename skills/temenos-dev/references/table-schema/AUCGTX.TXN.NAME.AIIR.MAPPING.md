# AUCGTX.TXN.NAME.AIIR.MAPPING — Table Schema

> Source: `INSERTS/I_F.AUCGTX.TXN.NAME.AIIR.MAPPING` in `AUCGTX_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TXN.MAPPING.AIIR.TXN.SUB.TYPE.CODE` | `AucgtxTxnNameAiirMapping_AiirTxnSubTypeCode` | TField |  | The AIIR transaction sub type code which maps to the transaction name in T24. |
| 2 | `TXN.MAPPING.AIIR.TXN.SUB.TYPE.DESC` | `AucgtxTxnNameAiirMapping_AiirTxnSubTypeDesc` | TField |  | The description associated with the AIIR Transaction sub type code. |
| 3 | `TXN.MAPPING.LOCAL.REF` | `AucgtxTxnNameAiirMapping_LocalRef` |  |  |  |
| 4 | `TXN.MAPPING.RESERVED.1` | `AucgtxTxnNameAiirMapping_Reserved1` | TField |  |  |
| 5 | `TXN.MAPPING.RESERVED.2` | `AucgtxTxnNameAiirMapping_Reserved2` | TField |  |  |
| 6 | `TXN.MAPPING.RESERVED.3` | `AucgtxTxnNameAiirMapping_Reserved3` | TField |  |  |
| 7 | `TXN.MAPPING.RESERVED.4` | `AucgtxTxnNameAiirMapping_Reserved4` | TField |  |  |
| 8 | `TXN.MAPPING.RESERVED.5` | `AucgtxTxnNameAiirMapping_Reserved5` | TField |  |  |
| 9 | `TXN.MAPPING.RESERVED.6` | `AucgtxTxnNameAiirMapping_Reserved6` | TField |  |  |
| 10 | `TXN.MAPPING.RESERVED.7` | `AucgtxTxnNameAiirMapping_Reserved7` | TField |  |  |
| 11 | `TXN.MAPPING.RESERVED.8` | `AucgtxTxnNameAiirMapping_Reserved8` | TField |  |  |
| 12 | `TXN.MAPPING.RESERVED.9` | `AucgtxTxnNameAiirMapping_Reserved9` | TField |  |  |
| 13 | `TXN.MAPPING.RESERVED.10` | `AucgtxTxnNameAiirMapping_Reserved10` | TField |  |  |
| 14 | `TXN.MAPPING.OVERRIDE` | `AucgtxTxnNameAiirMapping_Override` |  |  |  |
| 15 | `TXN.MAPPING.RECORD.STATUS` | `AucgtxTxnNameAiirMapping_RecordStatus` | String |  |  |
| 16 | `TXN.MAPPING.CURR.NO` | `AucgtxTxnNameAiirMapping_CurrNo` | String |  |  |
| 17 | `TXN.MAPPING.INPUTTER` | `AucgtxTxnNameAiirMapping_Inputter` |  |  |  |
| 18 | `TXN.MAPPING.DATE.TIME` | `AucgtxTxnNameAiirMapping_DateTime` |  |  |  |
| 19 | `TXN.MAPPING.AUTHORISER` | `AucgtxTxnNameAiirMapping_Authoriser` | String |  |  |
| 20 | `TXN.MAPPING.CO.CODE` | `AucgtxTxnNameAiirMapping_CoCode` | String |  |  |
| 21 | `TXN.MAPPING.DEPT.CODE` | `AucgtxTxnNameAiirMapping_DeptCode` | String |  |  |
| 22 | `TXN.MAPPING.AUDITOR.CODE` | `AucgtxTxnNameAiirMapping_AuditorCode` | String |  |  |
| 23 | `TXN.MAPPING.AUDIT.DATE.TIME` | `AucgtxTxnNameAiirMapping_AuditDateTime` | String |  |  |
