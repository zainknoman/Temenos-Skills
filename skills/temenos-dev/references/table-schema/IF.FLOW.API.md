# IF.FLOW.API — Table Schema

> Source: `INSERTS/I_F.IF.FLOW.API` in `IF_FlowCatalog.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IF.INT.API.API.NAME` | `IfFlowApi_ApiName` |  |  |  |
| 2 | `IF.INT.API.IF.INT.PARAM.NAME` | `IfFlowApi_IfIntParamName` |  |  |  |
| 3 | `IF.INT.API.IF.INT.PARAM.TYPE` | `IfFlowApi_IfIntParamType` |  |  |  |
| 4 | `IF.INT.API.IF.INT.DIRECTION` | `IfFlowApi_IfIntDirection` |  |  |  |
| 5 | `IF.INT.API.IF.INT.API.RESERVED.4` | `IfFlowApi_IfIntApiReserved4` |  |  |  |
| 6 | `IF.INT.API.IF.INT.API.RESERVED.5` | `IfFlowApi_IfIntApiReserved5` |  |  |  |
| 7 | `IF.INT.API.IF.INT.API.RESERVED.6` | `IfFlowApi_IfIntApiReserved6` |  |  |  |
| 8 | `IF.INT.API.RESERVED.7` | `IfFlowApi_Reserved7` |  |  |  |
| 9 | `IF.INT.API.RESERVED.8` | `IfFlowApi_Reserved8` |  |  |  |
| 10 | `IF.INT.API.RESERVED.9` | `IfFlowApi_Reserved9` |  |  |  |
| 11 | `IF.INT.API.RESERVED.10` | `IfFlowApi_Reserved10` |  |  |  |
| 12 | `IF.INT.API.API.NOTES` | `IfFlowApi_ApiNotes` |  |  |  |
| 13 | `IF.INT.API.EB.API.HOOK` | `IfFlowApi_EbApiHook` |  |  |  |
| 14 | `IF.INT.API.OPERATION.NAME` | `IfFlowApi_OperationName` |  |  |  |
| 15 | `IF.INT.API.RESERVED.13` | `IfFlowApi_Reserved13` | TField |  |  |
| 16 | `IF.INT.API.RESERVED.14` | `IfFlowApi_Reserved14` | TField |  |  |
| 17 | `IF.INT.API.RESERVED.15` | `IfFlowApi_Reserved15` | TField |  |  |
| 18 | `IF.INT.API.RESERVED.16` | `IfFlowApi_Reserved16` | TField |  |  |
| 19 | `IF.INT.API.RESERVED.17` | `IfFlowApi_Reserved17` | TField |  |  |
| 20 | `IF.INT.API.RESERVED.18` | `IfFlowApi_Reserved18` | TField |  |  |
| 21 | `IF.INT.API.RESERVED.19` | `IfFlowApi_Reserved19` | TField |  |  |
| 22 | `IF.INT.API.RESERVED.20` | `IfFlowApi_Reserved20` | TField |  |  |
| 23 | `IF.INT.API.OVERRIDE` | `IfFlowApi_Override` |  |  |  |
| 24 | `IF.INT.API.RECORD.STATUS` | `IfFlowApi_RecordStatus` | String |  |  |
| 25 | `IF.INT.API.CURR.NO` | `IfFlowApi_CurrNo` | String |  |  |
| 26 | `IF.INT.API.INPUTTER` | `IfFlowApi_Inputter` |  |  |  |
| 27 | `IF.INT.API.DATE.TIME` | `IfFlowApi_DateTime` |  |  |  |
| 28 | `IF.INT.API.AUTHORISER` | `IfFlowApi_Authoriser` | String |  |  |
| 29 | `IF.INT.API.CO.CODE` | `IfFlowApi_CoCode` | String |  |  |
| 30 | `IF.INT.API.DEPT.CODE` | `IfFlowApi_DeptCode` | String |  |  |
| 31 | `IF.INT.API.AUDITOR.CODE` | `IfFlowApi_AuditorCode` | String |  |  |
| 32 | `IF.INT.API.AUDIT.DATE.TIME` | `IfFlowApi_AuditDateTime` | String |  |  |
