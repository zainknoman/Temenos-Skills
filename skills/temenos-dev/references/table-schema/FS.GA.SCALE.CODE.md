# FS.GA.SCALE.CODE — Table Schema

> Source: `INSERTS/I_F.FS.GA.SCALE.CODE` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.SCALE.CODE.SCALE` | `FsGaScaleCode_Scale` | TField |  | Scale Code allows the user to create different types of scale of fee calculations. E.g, Defining the NAV changes, performance fee. Multifonds DB Column is SCALE_CODE. |
| 2 | `FS.GA.SCALE.CODE.HIGHEST` | `FsGaScaleCode_Highest` | TField |  | Enter the highest scale amount Multifonds DB Column is MNT_MAX. |
| 3 | `FS.GA.SCALE.CODE.SCALE.PERCENTAGE` | `FsGaScaleCode_ScalePercentage` | TField |  | Percentage of interest applicable for every tranche or scale wise cash balances Multifonds DB Column is TINT. |
| 4 | `FS.GA.SCALE.CODE.RESERVED10` | `FsGaScaleCode_Reserved10` | TField |  |  |
| 5 | `FS.GA.SCALE.CODE.RESERVED9` | `FsGaScaleCode_Reserved9` | TField |  |  |
| 6 | `FS.GA.SCALE.CODE.RESERVED8` | `FsGaScaleCode_Reserved8` | TField |  |  |
| 7 | `FS.GA.SCALE.CODE.RESERVED7` | `FsGaScaleCode_Reserved7` | TField |  |  |
| 8 | `FS.GA.SCALE.CODE.RESERVED6` | `FsGaScaleCode_Reserved6` | TField |  |  |
| 9 | `FS.GA.SCALE.CODE.RESERVED5` | `FsGaScaleCode_Reserved5` | TField |  |  |
| 10 | `FS.GA.SCALE.CODE.RESERVED4` | `FsGaScaleCode_Reserved4` | TField |  |  |
| 11 | `FS.GA.SCALE.CODE.RESERVED3` | `FsGaScaleCode_Reserved3` | TField |  |  |
| 12 | `FS.GA.SCALE.CODE.RESERVED2` | `FsGaScaleCode_Reserved2` | TField |  |  |
| 13 | `FS.GA.SCALE.CODE.RESERVED1` | `FsGaScaleCode_Reserved1` | TField |  |  |
| 14 | `FS.GA.SCALE.CODE.RECORD.STATUS` | `FsGaScaleCode_RecordStatus` | String |  |  |
| 15 | `FS.GA.SCALE.CODE.CURR.NO` | `FsGaScaleCode_CurrNo` | String |  |  |
| 16 | `FS.GA.SCALE.CODE.INPUTTER` | `FsGaScaleCode_Inputter` |  |  |  |
| 17 | `FS.GA.SCALE.CODE.DATE.TIME` | `FsGaScaleCode_DateTime` |  |  |  |
| 18 | `FS.GA.SCALE.CODE.AUTHORISER` | `FsGaScaleCode_Authoriser` | String |  |  |
| 19 | `FS.GA.SCALE.CODE.CO.CODE` | `FsGaScaleCode_CoCode` | String |  |  |
| 20 | `FS.GA.SCALE.CODE.DEPT.CODE` | `FsGaScaleCode_DeptCode` | String |  |  |
| 21 | `FS.GA.SCALE.CODE.AUDITOR.CODE` | `FsGaScaleCode_AuditorCode` | String |  |  |
| 22 | `FS.GA.SCALE.CODE.AUDIT.DATE.TIME` | `FsGaScaleCode_AuditDateTime` | String |  |  |
