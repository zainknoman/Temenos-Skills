# TNFCOP.TRADE.PARAM — Table Schema

> Source: `INSERTS/I_F.TNFCOP.TRADE.PARAM` in `TNFCOP_ExportDocumentaryCredit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TNFCOP.TRADE.PARAM.PYMT.GTEE.TYPE` | `TnfcopTradeParam_PymtGteeType` |  |  |  |
| 2 | `TNFCOP.TRADE.PARAM.LOCAL.REF` | `TnfcopTradeParam_LocalRef` |  |  |  |
| 3 | `TNFCOP.TRADE.PARAM.AVALIZED.LC` | `TnfcopTradeParam_AvalizedLc` |  |  |  |
| 4 | `TNFCOP.TRADE.PARAM.RESERVED.9` | `TnfcopTradeParam_Reserved9` |  |  |  |
| 5 | `TNFCOP.TRADE.PARAM.RESERVED.8` | `TnfcopTradeParam_Reserved8` |  |  |  |
| 6 | `TNFCOP.TRADE.PARAM.RESERVED.7` | `TnfcopTradeParam_Reserved7` | TField |  | Reserved field for future use |
| 7 | `TNFCOP.TRADE.PARAM.RESERVED.6` | `TnfcopTradeParam_Reserved6` | TField |  | Reserved field for future use |
| 8 | `TNFCOP.TRADE.PARAM.RESERVED.5` | `TnfcopTradeParam_Reserved5` | TField |  | Reserved field for future use |
| 9 | `TNFCOP.TRADE.PARAM.RESERVED.4` | `TnfcopTradeParam_Reserved4` | TField |  | Reserved field for future use |
| 10 | `TNFCOP.TRADE.PARAM.RESERVED.3` | `TnfcopTradeParam_Reserved3` | TField |  | Reserved field for future use |
| 11 | `TNFCOP.TRADE.PARAM.RESERVED.2` | `TnfcopTradeParam_Reserved2` | TField |  | Reserved field for future use |
| 12 | `TNFCOP.TRADE.PARAM.RESERVED.1` | `TnfcopTradeParam_Reserved1` | TField |  | Reserved field for future use |
| 13 | `TNFCOP.TRADE.PARAM.OVERRIDE` | `TnfcopTradeParam_Override` |  |  |  |
| 14 | `TNFCOP.TRADE.PARAM.RECORD.STATUS` | `TnfcopTradeParam_RecordStatus` | String |  |  |
| 15 | `TNFCOP.TRADE.PARAM.CURR.NO` | `TnfcopTradeParam_CurrNo` | String |  |  |
| 16 | `TNFCOP.TRADE.PARAM.INPUTTER` | `TnfcopTradeParam_Inputter` |  |  |  |
| 17 | `TNFCOP.TRADE.PARAM.DATE.TIME` | `TnfcopTradeParam_DateTime` |  |  |  |
| 18 | `TNFCOP.TRADE.PARAM.AUTHORISER` | `TnfcopTradeParam_Authoriser` | String |  |  |
| 19 | `TNFCOP.TRADE.PARAM.CO.CODE` | `TnfcopTradeParam_CoCode` | String |  |  |
| 20 | `TNFCOP.TRADE.PARAM.DEPT.CODE` | `TnfcopTradeParam_DeptCode` | String |  |  |
| 21 | `TNFCOP.TRADE.PARAM.AUDITOR.CODE` | `TnfcopTradeParam_AuditorCode` | String |  |  |
| 22 | `TNFCOP.TRADE.PARAM.AUDIT.DATE.TIME` | `TnfcopTradeParam_AuditDateTime` | String |  |  |
