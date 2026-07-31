# FS.GA.SCALE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.FS.GA.SCALE.PARAMETER` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `GA.SCALE.PARAM.SCALE` | `FsGaScaleParameter_Scale` | TField |  | If the fee type is equal to "5 - Scale", a scale code needs to be entered. Note that scales must have been created before via the button scale Multifonds DB Column is CBAREME. |
| 2 | `GA.SCALE.PARAM.HIGHEST` | `FsGaScaleParameter_Highest` | TField |  | Enter the highest scale amount Multifonds DB Column is MNT_MAX. |
| 3 | `GA.SCALE.PARAM.FEES.RATE` | `FsGaScaleParameter_FeesRate` | TField |  | The percentage of fees that needs to be applied on a transaction. Multifonds DB Column is PC_MNT. |
| 4 | `GA.SCALE.PARAM.AMOUNT.FOR.DEFINING.SCALE` | `FsGaScaleParameter_AmountForDefiningScale` | TField |  | Specify amount to define scale for charges. Multifonds DB Column is PC_AMMOUNT. |
| 5 | `GA.SCALE.PARAM.EFFECTIVE.DATE` | `FsGaScaleParameter_EffectiveDate` | TField |  | Effective date to be applied. Multifonds DB Column is DATE_EFFECTIVE. |
| 6 | `GA.SCALE.PARAM.RESERVED10` | `FsGaScaleParameter_Reserved10` | TField |  |  |
| 7 | `GA.SCALE.PARAM.RESERVED9` | `FsGaScaleParameter_Reserved9` | TField |  |  |
| 8 | `GA.SCALE.PARAM.RESERVED8` | `FsGaScaleParameter_Reserved8` | TField |  |  |
| 9 | `GA.SCALE.PARAM.RESERVED7` | `FsGaScaleParameter_Reserved7` | TField |  |  |
| 10 | `GA.SCALE.PARAM.RESERVED6` | `FsGaScaleParameter_Reserved6` | TField |  |  |
| 11 | `GA.SCALE.PARAM.RESERVED5` | `FsGaScaleParameter_Reserved5` | TField |  |  |
| 12 | `GA.SCALE.PARAM.RESERVED4` | `FsGaScaleParameter_Reserved4` | TField |  |  |
| 13 | `GA.SCALE.PARAM.RESERVED3` | `FsGaScaleParameter_Reserved3` | TField |  |  |
| 14 | `GA.SCALE.PARAM.RESERVED2` | `FsGaScaleParameter_Reserved2` | TField |  |  |
| 15 | `GA.SCALE.PARAM.RESERVED1` | `FsGaScaleParameter_Reserved1` | TField |  |  |
| 16 | `GA.SCALE.PARAM.LOCAL.REF` | `FsGaScaleParameter_LocalRef` |  |  |  |
| 17 | `GA.SCALE.PARAM.OVERRIDE` | `FsGaScaleParameter_Override` |  |  |  |
| 18 | `GA.SCALE.PARAM.RECORD.STATUS` | `FsGaScaleParameter_RecordStatus` | String |  |  |
| 19 | `GA.SCALE.PARAM.CURR.NO` | `FsGaScaleParameter_CurrNo` | String |  |  |
| 20 | `GA.SCALE.PARAM.INPUTTER` | `FsGaScaleParameter_Inputter` |  |  |  |
| 21 | `GA.SCALE.PARAM.DATE.TIME` | `FsGaScaleParameter_DateTime` |  |  |  |
| 22 | `GA.SCALE.PARAM.AUTHORISER` | `FsGaScaleParameter_Authoriser` | String |  |  |
| 23 | `GA.SCALE.PARAM.CO.CODE` | `FsGaScaleParameter_CoCode` | String |  |  |
| 24 | `GA.SCALE.PARAM.DEPT.CODE` | `FsGaScaleParameter_DeptCode` | String |  |  |
| 25 | `GA.SCALE.PARAM.AUDITOR.CODE` | `FsGaScaleParameter_AuditorCode` | String |  |  |
| 26 | `GA.SCALE.PARAM.AUDIT.DATE.TIME` | `FsGaScaleParameter_AuditDateTime` | String |  |  |
