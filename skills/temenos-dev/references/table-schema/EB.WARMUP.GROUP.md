# EB.WARMUP.GROUP — Table Schema

> Source: `INSERTS/I_F.EB.WARMUP.GROUP` in `EB_Utility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.WPGRP.APPLICATION` | `EbWarmupGroup_Application` |  |  |  |
| 2 | `EB.WPGRP.RECORD.ID` | `EbWarmupGroup_RecordId` |  |  |  |
| 3 | `EB.WPGRP.READ.API` | `EbWarmupGroup_ReadApi` |  |  |  |
| 4 | `EB.WPGRP.READ.API.INFO` | `EbWarmupGroup_ReadApiInfo` |  |  |  |
| 5 | `EB.WPGRP.RESERVED.12` | `EbWarmupGroup_Reserved12` |  |  |  |
| 6 | `EB.WPGRP.RESERVED.11` | `EbWarmupGroup_Reserved11` |  |  |  |
| 7 | `EB.WPGRP.LOCAL.ROUTINE` | `EbWarmupGroup_LocalRoutine` |  |  |  |
| 8 | `EB.WPGRP.RESERVED.10` | `EbWarmupGroup_Reserved10` |  |  |  |
| 9 | `EB.WPGRP.RESERVED.9` | `EbWarmupGroup_Reserved9` |  |  |  |
| 10 | `EB.WPGRP.RESERVED.8` | `EbWarmupGroup_Reserved8` |  |  |  |
| 11 | `EB.WPGRP.RESERVED.7` | `EbWarmupGroup_Reserved7` |  |  |  |
| 12 | `EB.WPGRP.RESERVED.6` | `EbWarmupGroup_Reserved6` |  |  |  |
| 13 | `EB.WPGRP.RESERVED.5` | `EbWarmupGroup_Reserved5` |  |  |  |
| 14 | `EB.WPGRP.RESERVED.4` | `EbWarmupGroup_Reserved4` |  |  |  |
| 15 | `EB.WPGRP.RESERVED.3` | `EbWarmupGroup_Reserved3` |  |  |  |
| 16 | `EB.WPGRP.RESERVED.2` | `EbWarmupGroup_Reserved2` |  |  |  |
| 17 | `EB.WPGRP.RESERVED.1` | `EbWarmupGroup_Reserved1` |  |  |  |
| 18 | `EB.WPGRP.RECORD.STATUS` | `EbWarmupGroup_RecordStatus` | String |  |  |
| 19 | `EB.WPGRP.CURR.NO` | `EbWarmupGroup_CurrNo` | String |  |  |
| 20 | `EB.WPGRP.INPUTTER` | `EbWarmupGroup_Inputter` |  |  |  |
| 21 | `EB.WPGRP.DATE.TIME` | `EbWarmupGroup_DateTime` |  |  |  |
| 22 | `EB.WPGRP.AUTHORISER` | `EbWarmupGroup_Authoriser` | String |  |  |
| 23 | `EB.WPGRP.CO.CODE` | `EbWarmupGroup_CoCode` | String |  |  |
| 24 | `EB.WPGRP.DEPT.CODE` | `EbWarmupGroup_DeptCode` | String |  |  |
| 25 | `EB.WPGRP.AUDITOR.CODE` | `EbWarmupGroup_AuditorCode` | String |  |  |
| 26 | `EB.WPGRP.AUDIT.DATE.TIME` | `EbWarmupGroup_AuditDateTime` | String |  |  |
| 27 | `EB.WPGRP.DESCRIPTION` | `EbWarmupGroup_Description` |  |  |  |
