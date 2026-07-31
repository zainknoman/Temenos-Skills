# ST.PROXY.LINK — Table Schema

> Source: `INSERTS/I_F.ST.PROXY.LINK` in `ST_AliasManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ST.PRL.PROXY.TYPE` | `StProxyLink_ProxyType` |  |  |  |
| 2 | `ST.PRL.PROXY.IDENTIFIER` | `StProxyLink_ProxyIdentifier` |  |  |  |
| 3 | `ST.PRL.PROXY.LINK.ID` | `StProxyLink_ProxyLinkId` |  |  |  |
| 4 | `ST.PRL.STATUS` | `StProxyLink_Status` |  |  |  |
