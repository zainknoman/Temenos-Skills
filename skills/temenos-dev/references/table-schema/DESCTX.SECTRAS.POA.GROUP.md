# DESCTX.SECTRAS.POA.GROUP — Table Schema

> Source: `INSERTS/I_F.DESCTX.SECTRAS.POA.GROUP` in `DESCTX_Taxation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `POA.GROUP.OPEN.DATE` | `DesctxSectrasPoaGroup_OpenDate` | TField |  | This field is used to capture the date when the POA group was created |
| 2 | `POA.GROUP.APPLY.DATE` | `DesctxSectrasPoaGroup_ApplyDate` | TField |  | This field is used to capture the date when the POA group was modified |
| 3 | `POA.GROUP.SCOPE` | `DesctxSectrasPoaGroup_Scope` | TField |  | This field is used to define the scope of POA Group. Here it contains constant value "I" |
| 4 | `POA.GROUP.TYPE` | `DesctxSectrasPoaGroup_Type` | TField |  | This field is used to define the type of POA Group. Here it contains Constant Value "10" |
| 5 | `POA.GROUP.EXERCISE.TYPE` | `DesctxSectrasPoaGroup_ExerciseType` | TField |  | This field is defines, Indication, whether the POA can be exercised by one authorized person or only in combination with further authorized persons.Here it contains Constant Value � O (Alphabet �O�) |
| 6 | `POA.GROUP.PERIOD.OF.VALID` | `DesctxSectrasPoaGroup_PeriodOfValid` | TField |  | This field defines, the value period of POA Group. Here it contains Constant 50 |
| 7 | `POA.GROUP.POA.EXT.CODE.TYPE` | `DesctxSectrasPoaGroup_PoaExtCodeType` |  |  |  |
| 8 | `POA.GROUP.POA.EXT.CODE` | `DesctxSectrasPoaGroup_PoaExtCode` |  |  |  |
| 9 | `POA.GROUP.ACC.EXT.CODE.TYPE` | `DesctxSectrasPoaGroup_AccExtCodeType` |  |  |  |
| 10 | `POA.GROUP.ACC.EXT.CODE` | `DesctxSectrasPoaGroup_AccExtCode` |  |  |  |
| 11 | `POA.GROUP.PARTNER.EXT.CODE.TYPE` | `DesctxSectrasPoaGroup_PartnerExtCodeType` |  |  |  |
| 12 | `POA.GROUP.PARTNER.EXT.CODE` | `DesctxSectrasPoaGroup_PartnerExtCode` |  |  |  |
| 13 | `POA.GROUP.CLOSE.DATE` | `DesctxSectrasPoaGroup_CloseDate` | TField |  | This field is used to capture the close date of the poa group |
| 14 | `POA.GROUP.ALTERNATE.ID` | `DesctxSectrasPoaGroup_AlternateId` | TField |  |  |
| 15 | `POA.GROUP.RESERVED.6` | `DesctxSectrasPoaGroup_Reserved6` | TField |  |  |
| 16 | `POA.GROUP.RESERVED.5` | `DesctxSectrasPoaGroup_Reserved5` | TField |  |  |
| 17 | `POA.GROUP.RESERVED.4` | `DesctxSectrasPoaGroup_Reserved4` | TField |  |  |
| 18 | `POA.GROUP.RESERVED.3` | `DesctxSectrasPoaGroup_Reserved3` | TField |  |  |
| 19 | `POA.GROUP.RESERVED.2` | `DesctxSectrasPoaGroup_Reserved2` | TField |  |  |
| 20 | `POA.GROUP.RESERVED.1` | `DesctxSectrasPoaGroup_Reserved1` | TField |  |  |
