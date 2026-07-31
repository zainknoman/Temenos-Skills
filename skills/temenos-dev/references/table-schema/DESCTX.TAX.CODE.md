# DESCTX.TAX.CODE — Table Schema

> Source: `INSERTS/I_F.DESCTX.TAX.CODE` in `DESCTX_Taxation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DESCTX.CODE.DESCRIPTION` | `DesctxTaxCode_Description` |  |  |  |
| 2 | `DESCTX.CODE.ACCOUNTING.ENTRY` | `DesctxTaxCode_AccountingEntry` | TField |  | it is yes or no field |
| 3 | `DESCTX.CODE.LOCAL.REF` | `DesctxTaxCode_LocalRef` |  |  |  |
| 4 | `DESCTX.CODE.OVERRIDE` | `DesctxTaxCode_Override` |  |  |  |
| 5 | `DESCTX.CODE.RECORD.STATUS` | `DesctxTaxCode_RecordStatus` | String |  |  |
| 6 | `DESCTX.CODE.CURR.NO` | `DesctxTaxCode_CurrNo` | String |  |  |
| 7 | `DESCTX.CODE.INPUTTER` | `DesctxTaxCode_Inputter` |  |  |  |
| 8 | `DESCTX.CODE.DATE.TIME` | `DesctxTaxCode_DateTime` |  |  |  |
| 9 | `DESCTX.CODE.AUTHORISER` | `DesctxTaxCode_Authoriser` | String |  |  |
| 10 | `DESCTX.CODE.CO.CODE` | `DesctxTaxCode_CoCode` | String |  |  |
| 11 | `DESCTX.CODE.DEPT.CODE` | `DesctxTaxCode_DeptCode` | String |  |  |
| 12 | `DESCTX.CODE.AUDITOR.CODE` | `DesctxTaxCode_AuditorCode` | String |  |  |
| 13 | `DESCTX.CODE.AUDIT.DATE.TIME` | `DesctxTaxCode_AuditDateTime` | String |  |  |
