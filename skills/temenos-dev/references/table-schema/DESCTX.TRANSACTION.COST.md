# DESCTX.TRANSACTION.COST — Table Schema

> Source: `INSERTS/I_F.DESCTX.TRANSACTION.COST` in `DESCTX_Taxation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SECTRAS.TRN.COST.VALID.FROM.DATE` | `DesctxTransactionCost_ValidFromDate` |  |  |  |
| 2 | `SECTRAS.TRN.COST.TXN.COST.PERC` | `DesctxTransactionCost_TxnCostPerc` |  |  |  |
| 3 | `SECTRAS.TRN.COST.LOCAL.REF` | `DesctxTransactionCost_LocalRef` |  |  |  |
| 4 | `SECTRAS.TRN.COST.RESERVED.8` | `DesctxTransactionCost_Reserved8` | TField |  | This field is reserved for future use. |
| 5 | `SECTRAS.TRN.COST.RESERVED.7` | `DesctxTransactionCost_Reserved7` | TField |  | This field is reserved for future use. |
| 6 | `SECTRAS.TRN.COST.RESERVED.6` | `DesctxTransactionCost_Reserved6` | TField |  | This field is reserved for future use. |
| 7 | `SECTRAS.TRN.COST.RESERVED.5` | `DesctxTransactionCost_Reserved5` | TField |  | This field is reserved for future use. |
| 8 | `SECTRAS.TRN.COST.RESERVED.4` | `DesctxTransactionCost_Reserved4` | TField |  | This field is reserved for future use. |
| 9 | `SECTRAS.TRN.COST.RESERVED.3` | `DesctxTransactionCost_Reserved3` | TField |  | This field is reserved for future use. |
| 10 | `SECTRAS.TRN.COST.RESERVED.2` | `DesctxTransactionCost_Reserved2` | TField |  | This field is reserved for future use. |
| 11 | `SECTRAS.TRN.COST.RESERVED.1` | `DesctxTransactionCost_Reserved1` | TField |  | This field is reserved for future use. |
| 12 | `SECTRAS.TRN.COST.OVERRIDE` | `DesctxTransactionCost_Override` |  |  |  |
| 13 | `SECTRAS.TRN.COST.RECORD.STATUS` | `DesctxTransactionCost_RecordStatus` | String |  |  |
| 14 | `SECTRAS.TRN.COST.CURR.NO` | `DesctxTransactionCost_CurrNo` | String |  |  |
| 15 | `SECTRAS.TRN.COST.INPUTTER` | `DesctxTransactionCost_Inputter` |  |  |  |
| 16 | `SECTRAS.TRN.COST.DATE.TIME` | `DesctxTransactionCost_DateTime` |  |  |  |
| 17 | `SECTRAS.TRN.COST.AUTHORISER` | `DesctxTransactionCost_Authoriser` | String |  |  |
| 18 | `SECTRAS.TRN.COST.CO.CODE` | `DesctxTransactionCost_CoCode` | String |  |  |
| 19 | `SECTRAS.TRN.COST.DEPT.CODE` | `DesctxTransactionCost_DeptCode` | String |  |  |
| 20 | `SECTRAS.TRN.COST.AUDITOR.CODE` | `DesctxTransactionCost_AuditorCode` | String |  |  |
| 21 | `SECTRAS.TRN.COST.AUDIT.DATE.TIME` | `DesctxTransactionCost_AuditDateTime` | String |  |  |
