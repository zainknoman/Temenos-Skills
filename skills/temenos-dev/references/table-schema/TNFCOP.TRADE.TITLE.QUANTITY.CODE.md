# TNFCOP.TRADE.TITLE.QUANTITY.CODE — Table Schema

> Source: `INSERTS/I_F.TNFCOP.TRADE.TITLE.QUANTITY.CODE` in `TNFCOP_TradeTitle.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TRADE.QCODE.DESCRIPTION` | `TnfcopTradeTitleQuantityCode_Description` |  |  |  |
| 2 | `TRADE.QCODE.RESERVED.5` | `TnfcopTradeTitleQuantityCode_Reserved5` | TField |  | Field for future use |
| 3 | `TRADE.QCODE.RESERVED.4` | `TnfcopTradeTitleQuantityCode_Reserved4` | TField |  | Field for future use |
| 4 | `TRADE.QCODE.RESERVED.3` | `TnfcopTradeTitleQuantityCode_Reserved3` | TField |  | Field for future use |
| 5 | `TRADE.QCODE.RESERVED.2` | `TnfcopTradeTitleQuantityCode_Reserved2` | TField |  | Field for future use |
| 6 | `TRADE.QCODE.RESERVED.1` | `TnfcopTradeTitleQuantityCode_Reserved1` | TField |  | Field for future use |
| 7 | `TRADE.QCODE.LOCAL.REF` | `TnfcopTradeTitleQuantityCode_LocalRef` |  |  |  |
| 8 | `TRADE.QCODE.OVERRIDE` | `TnfcopTradeTitleQuantityCode_Override` |  |  |  |
| 9 | `TRADE.QCODE.RECORD.STATUS` | `TnfcopTradeTitleQuantityCode_RecordStatus` | String |  |  |
| 10 | `TRADE.QCODE.CURR.NO` | `TnfcopTradeTitleQuantityCode_CurrNo` | String |  |  |
| 11 | `TRADE.QCODE.INPUTTER` | `TnfcopTradeTitleQuantityCode_Inputter` |  |  |  |
| 12 | `TRADE.QCODE.DATE.TIME` | `TnfcopTradeTitleQuantityCode_DateTime` |  |  |  |
| 13 | `TRADE.QCODE.AUTHORISER` | `TnfcopTradeTitleQuantityCode_Authoriser` | String |  |  |
| 14 | `TRADE.QCODE.CO.CODE` | `TnfcopTradeTitleQuantityCode_CoCode` | String |  |  |
| 15 | `TRADE.QCODE.DEPT.CODE` | `TnfcopTradeTitleQuantityCode_DeptCode` | String |  |  |
| 16 | `TRADE.QCODE.AUDITOR.CODE` | `TnfcopTradeTitleQuantityCode_AuditorCode` | String |  |  |
| 17 | `TRADE.QCODE.AUDIT.DATE.TIME` | `TnfcopTradeTitleQuantityCode_AuditDateTime` | String |  |  |
