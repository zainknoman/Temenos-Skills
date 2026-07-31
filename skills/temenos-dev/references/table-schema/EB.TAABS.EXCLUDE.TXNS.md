# EB.TAABS.EXCLUDE.TXNS — Table Schema

> Source: `INSERTS/I_F.EB.TAABS.EXCLUDE.TXNS` in `EB_ProductConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.TETX.EXCLUDE.TXN` | `EbTaabsExcludeTxns_ExcludeTxn` | TField |  | This field indicates if the associated EB.TAABS.CAPTURE.TXNS record need to be excluded or included for release in the target system. |
| 2 | `EB.TETX.REASON.FOR.EXCL` | `EbTaabsExcludeTxns_ReasonForExcl` | TField |  | This field indicates the reason associated for tagging the record for exclusion or inclusion. |
| 3 | `EB.TETX.LOCAL.REF` | `EbTaabsExcludeTxns_LocalRef` |  |  |  |
| 4 | `EB.TETX.OVERRIDE` | `EbTaabsExcludeTxns_Override` |  |  |  |
| 5 | `EB.TETX.RECORD.STATUS` | `EbTaabsExcludeTxns_RecordStatus` | String |  |  |
| 6 | `EB.TETX.CURR.NO` | `EbTaabsExcludeTxns_CurrNo` | String |  |  |
| 7 | `EB.TETX.INPUTTER` | `EbTaabsExcludeTxns_Inputter` |  |  |  |
| 8 | `EB.TETX.DATE.TIME` | `EbTaabsExcludeTxns_DateTime` |  |  |  |
| 9 | `EB.TETX.AUTHORISER` | `EbTaabsExcludeTxns_Authoriser` | String |  |  |
| 10 | `EB.TETX.CO.CODE` | `EbTaabsExcludeTxns_CoCode` | String |  |  |
| 11 | `EB.TETX.DEPT.CODE` | `EbTaabsExcludeTxns_DeptCode` | String |  |  |
| 12 | `EB.TETX.AUDITOR.CODE` | `EbTaabsExcludeTxns_AuditorCode` | String |  |  |
| 13 | `EB.TETX.AUDIT.DATE.TIME` | `EbTaabsExcludeTxns_AuditDateTime` | String |  |  |
