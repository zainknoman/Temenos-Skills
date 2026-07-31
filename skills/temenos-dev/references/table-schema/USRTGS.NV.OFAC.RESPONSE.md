# USRTGS.NV.OFAC.RESPONSE — Table Schema

> Source: `INSERTS/I_F.USRTGS.NV.OFAC.RESPONSE` in `USRTGS_Fedwire.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FWOFAC.RESPONSE` | `UsrtgsNvOfacResponse_OfacResponse` |  |  |  |
| 2 | `FWOFAC.RESPONSE.STATUS` | `UsrtgsNvOfacResponse_ResponseStatus` |  |  |  |
| 3 | `FWOFAC.OVERRIDE` | `UsrtgsNvOfacResponse_Override` |  |  |  |
| 4 | `FWOFAC.RECORD.STATUS` | `UsrtgsNvOfacResponse_RecordStatus` | String |  |  |
| 5 | `FWOFAC.CURR.NO` | `UsrtgsNvOfacResponse_CurrNo` | String |  |  |
| 6 | `FWOFAC.INPUTTER` | `UsrtgsNvOfacResponse_Inputter` |  |  |  |
| 7 | `FWOFAC.DATE.TIME` | `UsrtgsNvOfacResponse_DateTime` |  |  |  |
| 8 | `FWOFAC.AUTHORISER` | `UsrtgsNvOfacResponse_Authoriser` | String |  |  |
| 9 | `FWOFAC.CO.CODE` | `UsrtgsNvOfacResponse_CoCode` | String |  |  |
| 10 | `FWOFAC.DEPT.CODE` | `UsrtgsNvOfacResponse_DeptCode` | String |  |  |
| 11 | `FWOFAC.AUDITOR.CODE` | `UsrtgsNvOfacResponse_AuditorCode` | String |  |  |
| 12 | `FWOFAC.AUDIT.DATE.TIME` | `UsrtgsNvOfacResponse_AuditDateTime` | String |  |  |
