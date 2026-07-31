# NACUST.EVENT.HISTORY — Table Schema

> Source: `INSERTS/I_F.NACUST.EVENT.HISTORY` in `NACUST_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NACUST.EVENT.HIS.EVENT.NAME` | `NacustEventHistory_EventName` |  |  |  |
| 2 | `NACUST.EVENT.HIS.EVENT.DATE` | `NacustEventHistory_EventDate` |  |  |  |
| 3 | `NACUST.EVENT.HIS.SYSTEM.DATE` | `NacustEventHistory_SystemDate` |  |  |  |
| 4 | `NACUST.EVENT.HIS.TIME.STAMP` | `NacustEventHistory_TimeStamp` |  |  |  |
| 5 | `NACUST.EVENT.HIS.CONTEXT.NAME` | `NacustEventHistory_ContextName` |  |  |  |
| 6 | `NACUST.EVENT.HIS.CONTEXT.VALUE` | `NacustEventHistory_ContextValue` |  |  |  |
| 7 | `NACUST.EVENT.HIS.DELIVERY.REF` | `NacustEventHistory_DeliveryRef` |  |  |  |
| 8 | `NACUST.EVENT.HIS.RESERVED.11` | `NacustEventHistory_Reserved11` |  |  |  |
| 9 | `NACUST.EVENT.HIS.RESERVED.10` | `NacustEventHistory_Reserved10` |  |  |  |
| 10 | `NACUST.EVENT.HIS.RESERVED.9` | `NacustEventHistory_Reserved9` |  |  |  |
| 11 | `NACUST.EVENT.HIS.RESERVED.8` | `NacustEventHistory_Reserved8` |  |  |  |
| 12 | `NACUST.EVENT.HIS.RESERVED.7` | `NacustEventHistory_Reserved7` |  |  |  |
| 13 | `NACUST.EVENT.HIS.RESERVED.6` | `NacustEventHistory_Reserved6` |  |  |  |
| 14 | `NACUST.EVENT.HIS.RESERVED.5` | `NacustEventHistory_Reserved5` | TField |  |  |
| 15 | `NACUST.EVENT.HIS.RESERVED.4` | `NacustEventHistory_Reserved4` | TField |  |  |
| 16 | `NACUST.EVENT.HIS.RESERVED.3` | `NacustEventHistory_Reserved3` | TField |  |  |
| 17 | `NACUST.EVENT.HIS.RESERVED.2` | `NacustEventHistory_Reserved2` | TField |  |  |
| 18 | `NACUST.EVENT.HIS.RESERVED.1` | `NacustEventHistory_Reserved1` | TField |  |  |
