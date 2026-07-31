# FS.GA.FAIR.VALUE.INDEX.MOVEMENT — Table Schema

> Source: `INSERTS/I_F.FS.GA.FAIR.VALUE.INDEX.MOVEMENT` in `FS_StaticData.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.NAV.GROUP.CODE` | `FsGaFairValueIndexMovement_NavGroupCode` | TField |  | The NAV group code is the list of funds grouped together for NAV processing, reporting etc Multifonds DB Column is NAV_GROUP. |
| 2 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.INTERNAL.SECURITY.ID` | `FsGaFairValueIndexMovement_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 3 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.CURRENT.DATE.AND.TIME` | `FsGaFairValueIndexMovement_CurrentDateAndTime` | TField |  | Allows user to update the current date. Multifonds DB Column is CURR_TIME_COURS. |
| 4 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.CURRENT.VALUE` | `FsGaFairValueIndexMovement_CurrentValue` | TField |  | Allows user to update the current value of the index. User can manually override 'Current value' or insert it using 'Index movement' loader. Multifonds DB Column is CURR_COURS. |
| 5 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.PRICE.DATE` | `FsGaFairValueIndexMovement_PriceDate` | TField |  | Date of the Price or Ex rate used in NAV Multifonds DB Column is DATE_COURS. |
| 6 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.VARIATION.PERCENT` | `FsGaFairValueIndexMovement_VariationPercent` | TField |  | Based on the current value and previous value of the index, system calculates the variation in percentage. Multifonds DB Column is TOL_COURS. |
| 7 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.RESERVED10` | `FsGaFairValueIndexMovement_Reserved10` | TField |  |  |
| 8 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.RESERVED9` | `FsGaFairValueIndexMovement_Reserved9` | TField |  |  |
| 9 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.RESERVED8` | `FsGaFairValueIndexMovement_Reserved8` | TField |  |  |
| 10 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.RESERVED7` | `FsGaFairValueIndexMovement_Reserved7` | TField |  |  |
| 11 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.RESERVED6` | `FsGaFairValueIndexMovement_Reserved6` | TField |  |  |
| 12 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.RESERVED5` | `FsGaFairValueIndexMovement_Reserved5` | TField |  |  |
| 13 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.RESERVED4` | `FsGaFairValueIndexMovement_Reserved4` | TField |  |  |
| 14 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.RESERVED3` | `FsGaFairValueIndexMovement_Reserved3` | TField |  |  |
| 15 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.RESERVED2` | `FsGaFairValueIndexMovement_Reserved2` | TField |  |  |
| 16 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.RESERVED1` | `FsGaFairValueIndexMovement_Reserved1` | TField |  |  |
| 17 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.RECORD.STATUS` | `FsGaFairValueIndexMovement_RecordStatus` | String |  |  |
| 18 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.CURR.NO` | `FsGaFairValueIndexMovement_CurrNo` | String |  |  |
| 19 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.INPUTTER` | `FsGaFairValueIndexMovement_Inputter` |  |  |  |
| 20 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.DATE.TIME` | `FsGaFairValueIndexMovement_DateTime` |  |  |  |
| 21 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.AUTHORISER` | `FsGaFairValueIndexMovement_Authoriser` | String |  |  |
| 22 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.CO.CODE` | `FsGaFairValueIndexMovement_CoCode` | String |  |  |
| 23 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.DEPT.CODE` | `FsGaFairValueIndexMovement_DeptCode` | String |  |  |
| 24 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.AUDITOR.CODE` | `FsGaFairValueIndexMovement_AuditorCode` | String |  |  |
| 25 | `FS.GA.FAIR.VALUE.INDEX.MOVEMENT.AUDIT.DATE.TIME` | `FsGaFairValueIndexMovement_AuditDateTime` | String |  |  |
