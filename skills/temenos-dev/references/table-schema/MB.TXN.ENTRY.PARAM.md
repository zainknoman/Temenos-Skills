# MB.TXN.ENTRY.PARAM — Table Schema

> Source: `INSERTS/I_F.MB.TXN.ENTRY.PARAM` in `EB_ModelBank.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.MB.EXC.ASSET` | `MbTxnEntryParam_ExcAsset` |  |  |  |
| 2 | `EB.MB.EXC.RE.TYPE` | `MbTxnEntryParam_ExcReType` |  |  |  |
| 3 | `EB.MB.EXC.CATEGORY` | `MbTxnEntryParam_ExcCategory` |  |  |  |
| 4 | `EB.MB.LOCAL.REF` | `MbTxnEntryParam_LocalRef` |  |  |  |
| 5 | `EB.MB.RECORD.STATUS` | `MbTxnEntryParam_RecordStatus` | String |  |  |
| 6 | `EB.MB.CURR.NO` | `MbTxnEntryParam_CurrNo` | String |  |  |
| 7 | `EB.MB.INPUTTER` | `MbTxnEntryParam_Inputter` |  |  |  |
| 8 | `EB.MB.DATE.TIME` | `MbTxnEntryParam_DateTime` |  |  |  |
| 9 | `EB.MB.AUTHORISER` | `MbTxnEntryParam_Authoriser` | String |  |  |
| 10 | `EB.MB.CO.CODE` | `MbTxnEntryParam_CoCode` | String |  |  |
| 11 | `EB.MB.DEPT.CODE` | `MbTxnEntryParam_DeptCode` | String |  |  |
| 12 | `EB.MB.AUDITOR.CODE` | `MbTxnEntryParam_AuditorCode` | String |  |  |
| 13 | `EB.MB.AUDIT.DATE.TIME` | `MbTxnEntryParam_AuditDateTime` | String |  |  |
