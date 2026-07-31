# REGION.CHARGES — Table Schema

> Source: `INSERTS/I_F.REGION.CHARGES` in `CALEND_DischargeFee.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `REG.CHAR.CHARGE.AMOUNT` | `RegionCharges_ChargeAmount` | TField |  |  |
| 2 | `REG.CHAR.RESERVED.12` | `RegionCharges_Reserved12` | TField |  |  |
| 3 | `REG.CHAR.RESERVED.11` | `RegionCharges_Reserved11` | TField |  |  |
| 4 | `REG.CHAR.RESERVED.10` | `RegionCharges_Reserved10` | TField |  |  |
| 5 | `REG.CHAR.RESERVED.9` | `RegionCharges_Reserved9` | TField |  |  |
| 6 | `REG.CHAR.RESERVED.8` | `RegionCharges_Reserved8` | TField |  |  |
| 7 | `REG.CHAR.RESERVED.7` | `RegionCharges_Reserved7` | TField |  |  |
| 8 | `REG.CHAR.RESERVED.6` | `RegionCharges_Reserved6` | TField |  |  |
| 9 | `REG.CHAR.RESERVED.5` | `RegionCharges_Reserved5` | TField |  |  |
| 10 | `REG.CHAR.RESERVED.4` | `RegionCharges_Reserved4` | TField |  |  |
| 11 | `REG.CHAR.RESERVED.3` | `RegionCharges_Reserved3` | TField |  |  |
| 12 | `REG.CHAR.RESERVED.2` | `RegionCharges_Reserved2` | TField |  |  |
| 13 | `REG.CHAR.RESERVED.1` | `RegionCharges_Reserved1` | TField |  |  |
| 14 | `REG.CHAR.RECORD.STATUS` | `RegionCharges_RecordStatus` | String |  |  |
| 15 | `REG.CHAR.CURR.NO` | `RegionCharges_CurrNo` | String |  |  |
| 16 | `REG.CHAR.INPUTTER` | `RegionCharges_Inputter` |  |  |  |
| 17 | `REG.CHAR.DATE.TIME` | `RegionCharges_DateTime` |  |  |  |
| 18 | `REG.CHAR.AUTHORISER` | `RegionCharges_Authoriser` | String |  |  |
| 19 | `REG.CHAR.CO.CODE` | `RegionCharges_CoCode` | String |  |  |
| 20 | `REG.CHAR.DEPT.CODE` | `RegionCharges_DeptCode` | String |  |  |
| 21 | `REG.CHAR.AUDITOR.CODE` | `RegionCharges_AuditorCode` | String |  |  |
| 22 | `REG.CHAR.AUDIT.DATE.TIME` | `RegionCharges_AuditDateTime` | String |  |  |
