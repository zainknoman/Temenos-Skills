# CAREGS.CDIC.HOLD.INSTRUCTION — Table Schema

> Source: `INSERTS/I_F.CAREGS.CDIC.HOLD.INSTRUCTION` in `CADEPO_CDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CDIC.HLD.INST.INSUR.DETERMINATION.CATEG` | `CaregsCdicHoldInstruction_InsurDeterminationCateg` |  |  |  |
| 2 | `CDIC.HLD.INST.PRODUCT.CODE` | `CaregsCdicHoldInstruction_ProductCode` |  |  |  |
| 3 | `CDIC.HLD.INST.CLEARING.CODE` | `CaregsCdicHoldInstruction_ClearingCode` |  |  |  |
| 4 | `CDIC.HLD.INST.PRODUCT.DESCRIPTION` | `CaregsCdicHoldInstruction_ProductDescription` |  |  |  |
| 5 | `CDIC.HLD.INST.CDIC.HOLD` | `CaregsCdicHoldInstruction_CdicHold` |  |  |  |
| 6 | `CDIC.HLD.INST.CDIC.ACCESSIBLE.BALANCE` | `CaregsCdicHoldInstruction_CdicAccessibleBalance` |  |  |  |
| 7 | `CDIC.HLD.INST.RESERVED1` | `CaregsCdicHoldInstruction_Reserved1` |  |  |  |
| 8 | `CDIC.HLD.INST.RESERVED2` | `CaregsCdicHoldInstruction_Reserved2` |  |  |  |
| 9 | `CDIC.HLD.INST.RESERVED3` | `CaregsCdicHoldInstruction_Reserved3` |  |  |  |
| 10 | `CDIC.HLD.INST.RESERVED4` | `CaregsCdicHoldInstruction_Reserved4` |  |  |  |
| 11 | `CDIC.HLD.INST.RESERVED5` | `CaregsCdicHoldInstruction_Reserved5` |  |  |  |
| 12 | `CDIC.HLD.INST.RESERVED.1` | `CaregsCdicHoldInstruction_Reserved1` |  |  |  |
| 13 | `CDIC.HLD.INST.RESERVED.2` | `CaregsCdicHoldInstruction_Reserved2` |  |  |  |
| 14 | `CDIC.HLD.INST.RESERVED.3` | `CaregsCdicHoldInstruction_Reserved3` |  |  |  |
| 15 | `CDIC.HLD.INST.RESERVED.4` | `CaregsCdicHoldInstruction_Reserved4` |  |  |  |
| 16 | `CDIC.HLD.INST.RESERVED.5` | `CaregsCdicHoldInstruction_Reserved5` |  |  |  |
| 17 | `CDIC.HLD.INST.RECORD.STATUS` | `CaregsCdicHoldInstruction_RecordStatus` | String |  |  |
| 18 | `CDIC.HLD.INST.CURR.NO` | `CaregsCdicHoldInstruction_CurrNo` | String |  |  |
| 19 | `CDIC.HLD.INST.INPUTTER` | `CaregsCdicHoldInstruction_Inputter` |  |  |  |
| 20 | `CDIC.HLD.INST.DATE.TIME` | `CaregsCdicHoldInstruction_DateTime` |  |  |  |
| 21 | `CDIC.HLD.INST.AUTHORISER` | `CaregsCdicHoldInstruction_Authoriser` | String |  |  |
| 22 | `CDIC.HLD.INST.CO.CODE` | `CaregsCdicHoldInstruction_CoCode` | String |  |  |
| 23 | `CDIC.HLD.INST.DEPT.CODE` | `CaregsCdicHoldInstruction_DeptCode` | String |  |  |
| 24 | `CDIC.HLD.INST.AUDITOR.CODE` | `CaregsCdicHoldInstruction_AuditorCode` | String |  |  |
| 25 | `CDIC.HLD.INST.AUDIT.DATE.TIME` | `CaregsCdicHoldInstruction_AuditDateTime` | String |  |  |
