# DE.MESSAGE.GROUP — Table Schema

> Source: `INSERTS/I_F.DE.MESSAGE.GROUP` in `PF_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.MSGRP.DESCRIPTION` | `DeMessageGroup_Description` |  |  |  |
| 2 | `DE.MSGRP.MESSAGE.APP` | `DeMessageGroup_MessageApp` |  |  |  |
| 3 | `DE.MSGRP.RESERVED.5` | `DeMessageGroup_Reserved5` | TField |  |  |
| 4 | `DE.MSGRP.RESERVED.4` | `DeMessageGroup_Reserved4` | TField |  |  |
| 5 | `DE.MSGRP.RESERVED.3` | `DeMessageGroup_Reserved3` | TField |  |  |
| 6 | `DE.MSGRP.RESERVED.2` | `DeMessageGroup_Reserved2` | TField |  |  |
| 7 | `DE.MSGRP.RESERVED.1` | `DeMessageGroup_Reserved1` | TField |  |  |
| 8 | `DE.MSGRP.LOCAL.REF` | `DeMessageGroup_LocalRef` |  |  |  |
| 9 | `DE.MSGRP.OVERRIDE` | `DeMessageGroup_Override` |  |  |  |
| 10 | `DE.MSGRP.RECORD.STATUS` | `DeMessageGroup_RecordStatus` | String |  |  |
| 11 | `DE.MSGRP.CURR.NO` | `DeMessageGroup_CurrNo` | String |  |  |
| 12 | `DE.MSGRP.INPUTTER` | `DeMessageGroup_Inputter` |  |  |  |
| 13 | `DE.MSGRP.DATE.TIME` | `DeMessageGroup_DateTime` |  |  |  |
| 14 | `DE.MSGRP.AUTHORISER` | `DeMessageGroup_Authoriser` | String |  |  |
| 15 | `DE.MSGRP.CO.CODE` | `DeMessageGroup_CoCode` | String |  |  |
| 16 | `DE.MSGRP.DEPT.CODE` | `DeMessageGroup_DeptCode` | String |  |  |
| 17 | `DE.MSGRP.AUDITOR.CODE` | `DeMessageGroup_AuditorCode` | String |  |  |
| 18 | `DE.MSGRP.AUDIT.DATE.TIME` | `DeMessageGroup_AuditDateTime` | String |  |  |
