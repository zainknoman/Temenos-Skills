# FS.GA.SCALE.CODE.DESCRIPTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.SCALE.CODE.DESCRIPTION` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SCALE.CODE.DESCRIPTION.SCALE` | `FsGaScaleCodeDescription_Scale` | TField |  | Scale Code allows the user to create different types of scale of fee calculations. E.g, Defining the NAV changes, performance fee. Multifonds DB Column is SCALE_CODE. |
| 2 | `FS.GA.SCALE.CODE.DESCRIPTION.LIB.SCALE.CODE` | `FsGaScaleCodeDescription_LibScaleCode` | TField |  | Scale Code. Multifonds DB Column is LIB_SCALE_CODE. |
| 3 | `FS.GA.SCALE.CODE.DESCRIPTION.RESERVED10` | `FsGaScaleCodeDescription_Reserved10` | TField |  |  |
| 4 | `FS.GA.SCALE.CODE.DESCRIPTION.RESERVED9` | `FsGaScaleCodeDescription_Reserved9` | TField |  |  |
| 5 | `FS.GA.SCALE.CODE.DESCRIPTION.RESERVED8` | `FsGaScaleCodeDescription_Reserved8` | TField |  |  |
| 6 | `FS.GA.SCALE.CODE.DESCRIPTION.RESERVED7` | `FsGaScaleCodeDescription_Reserved7` | TField |  |  |
| 7 | `FS.GA.SCALE.CODE.DESCRIPTION.RESERVED6` | `FsGaScaleCodeDescription_Reserved6` | TField |  |  |
| 8 | `FS.GA.SCALE.CODE.DESCRIPTION.RESERVED5` | `FsGaScaleCodeDescription_Reserved5` | TField |  |  |
| 9 | `FS.GA.SCALE.CODE.DESCRIPTION.RESERVED4` | `FsGaScaleCodeDescription_Reserved4` | TField |  |  |
| 10 | `FS.GA.SCALE.CODE.DESCRIPTION.RESERVED3` | `FsGaScaleCodeDescription_Reserved3` | TField |  |  |
| 11 | `FS.GA.SCALE.CODE.DESCRIPTION.RESERVED2` | `FsGaScaleCodeDescription_Reserved2` | TField |  |  |
| 12 | `FS.GA.SCALE.CODE.DESCRIPTION.RESERVED1` | `FsGaScaleCodeDescription_Reserved1` | TField |  |  |
| 13 | `FS.GA.SCALE.CODE.DESCRIPTION.RECORD.STATUS` | `FsGaScaleCodeDescription_RecordStatus` | String |  |  |
| 14 | `FS.GA.SCALE.CODE.DESCRIPTION.CURR.NO` | `FsGaScaleCodeDescription_CurrNo` | String |  |  |
| 15 | `FS.GA.SCALE.CODE.DESCRIPTION.INPUTTER` | `FsGaScaleCodeDescription_Inputter` |  |  |  |
| 16 | `FS.GA.SCALE.CODE.DESCRIPTION.DATE.TIME` | `FsGaScaleCodeDescription_DateTime` |  |  |  |
| 17 | `FS.GA.SCALE.CODE.DESCRIPTION.AUTHORISER` | `FsGaScaleCodeDescription_Authoriser` | String |  |  |
| 18 | `FS.GA.SCALE.CODE.DESCRIPTION.CO.CODE` | `FsGaScaleCodeDescription_CoCode` | String |  |  |
| 19 | `FS.GA.SCALE.CODE.DESCRIPTION.DEPT.CODE` | `FsGaScaleCodeDescription_DeptCode` | String |  |  |
| 20 | `FS.GA.SCALE.CODE.DESCRIPTION.AUDITOR.CODE` | `FsGaScaleCodeDescription_AuditorCode` | String |  |  |
| 21 | `FS.GA.SCALE.CODE.DESCRIPTION.AUDIT.DATE.TIME` | `FsGaScaleCodeDescription_AuditDateTime` | String |  |  |
