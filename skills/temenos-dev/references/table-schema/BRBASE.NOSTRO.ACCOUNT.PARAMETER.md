# BRBASE.NOSTRO.ACCOUNT.PARAMETER — Table Schema

> Source: `INSERTS/I_F.BRBASE.NOSTRO.ACCOUNT.PARAMETER` in `BRBASE_InterfaceConnector.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NOS.ACCT.PARAM.DEFAULT.NOSTRO.CCY` | `BrbaseNostroAccountParameter_DefaultNostroCcy` |  |  |  |
| 2 | `NOS.ACCT.PARAM.DEFAULT.NOSTRO.ACCT` | `BrbaseNostroAccountParameter_DefaultNostroAcct` |  |  |  |
| 3 | `NOS.ACCT.PARAM.COMPENSATION.CODE` | `BrbaseNostroAccountParameter_CompensationCode` |  |  |  |
| 4 | `NOS.ACCT.PARAM.COMPENSATION.NOSTRO.CCY` | `BrbaseNostroAccountParameter_CompensationNostroCcy` |  |  |  |
| 5 | `NOS.ACCT.PARAM.COMPENSATION.NOSTRO.ACCT` | `BrbaseNostroAccountParameter_CompensationNostroAcct` |  |  |  |
| 6 | `NOS.ACCT.PARAM.LOCAL.REF` | `BrbaseNostroAccountParameter_LocalRef` |  |  |  |
| 7 | `NOS.ACCT.PARAM.OVERRIDE` | `BrbaseNostroAccountParameter_Override` |  |  |  |
| 8 | `NOS.ACCT.PARAM.RECORD.STATUS` | `BrbaseNostroAccountParameter_RecordStatus` | String |  |  |
| 9 | `NOS.ACCT.PARAM.CURR.NO` | `BrbaseNostroAccountParameter_CurrNo` | String |  |  |
| 10 | `NOS.ACCT.PARAM.INPUTTER` | `BrbaseNostroAccountParameter_Inputter` |  |  |  |
| 11 | `NOS.ACCT.PARAM.DATE.TIME` | `BrbaseNostroAccountParameter_DateTime` |  |  |  |
| 12 | `NOS.ACCT.PARAM.AUTHORISER` | `BrbaseNostroAccountParameter_Authoriser` | String |  |  |
| 13 | `NOS.ACCT.PARAM.CO.CODE` | `BrbaseNostroAccountParameter_CoCode` | String |  |  |
| 14 | `NOS.ACCT.PARAM.DEPT.CODE` | `BrbaseNostroAccountParameter_DeptCode` | String |  |  |
| 15 | `NOS.ACCT.PARAM.AUDITOR.CODE` | `BrbaseNostroAccountParameter_AuditorCode` | String |  |  |
| 16 | `NOS.ACCT.PARAM.AUDIT.DATE.TIME` | `BrbaseNostroAccountParameter_AuditDateTime` | String |  |  |
