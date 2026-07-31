# SE.MS.APPLICATION — Table Schema

> Source: `INSERTS/I_F.SE.MS.APPLICATION` in `SE_TestFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MS.APP.SERVER.NAME` | `SeMsApplication_ServerName` | TField |  |  |
| 2 | `MS.APP.AGENT.NUMBER` | `SeMsApplication_AgentNumber` | TField |  |  |
| 3 | `MS.APP.SESSION.NUMBER` | `SeMsApplication_SessionNumber` | TField |  |  |
| 4 | `MS.APP.DATA.PAYLOAD` | `SeMsApplication_DataPayload` | TField |  |  |
| 5 | `MS.APP.LAST.UPD.TIMESTAMP` | `SeMsApplication_LastUpdTimestamp` | TField |  |  |
| 6 | `MS.APP.RESERVED.04` | `SeMsApplication_Reserved04` | TField |  |  |
| 7 | `MS.APP.RESERVED.03` | `SeMsApplication_Reserved03` | TField |  |  |
| 8 | `MS.APP.RESERVED.02` | `SeMsApplication_Reserved02` | TField |  |  |
| 9 | `MS.APP.RESERVED.01` | `SeMsApplication_Reserved01` | TField |  |  |
