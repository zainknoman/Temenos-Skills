# SEPA.REFUSAL.LIST — Table Schema

> Source: `INSERTS/I_F.SEPA.REFUSAL.LIST` in `EP_Refusal.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SEPA.REFLIS.REFUSAL.TXN` | `SepaRefusalList_RefusalTxn` |  |  |  |
| 2 | `SEPA.REFLIS.RECORD.STATUS` | `SepaRefusalList_RecordStatus` | String |  |  |
| 3 | `SEPA.REFLIS.CURR.NO` | `SepaRefusalList_CurrNo` | String |  |  |
| 4 | `SEPA.REFLIS.INPUTTER` | `SepaRefusalList_Inputter` |  |  |  |
| 5 | `SEPA.REFLIS.DATE.TIME` | `SepaRefusalList_DateTime` |  |  |  |
| 6 | `SEPA.REFLIS.AUTHORISER` | `SepaRefusalList_Authoriser` | String |  |  |
| 7 | `SEPA.REFLIS.CO.CODE` | `SepaRefusalList_CoCode` | String |  |  |
| 8 | `SEPA.REFLIS.DEPT.CODE` | `SepaRefusalList_DeptCode` | String |  |  |
| 9 | `SEPA.REFLIS.AUDITOR.CODE` | `SepaRefusalList_AuditorCode` | String |  |  |
| 10 | `SEPA.REFLIS.AUDIT.DATE.TIME` | `SepaRefusalList_AuditDateTime` | String |  |  |
