# LIMIT.COL.ALLOC.WORK — Table Schema

> Source: `INSERTS/I_F.LIMIT.COL.ALLOC.WORK` in `LI_Collateral.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.ALOC.LIMIT.ID` | `LimitColAllocWork_LimitId` |  |  |  |
| 2 | `LI.ALOC.LIMIT.CCY` | `LimitColAllocWork_LimitCcy` |  |  |  |
| 3 | `LI.ALOC.COLL.CODE` | `LimitColAllocWork_CollCode` |  |  |  |
| 4 | `LI.ALOC.COLL.RIGHT` | `LimitColAllocWork_CollRight` |  |  |  |
| 5 | `LI.ALOC.COL.ALOC.PTY` | `LimitColAllocWork_ColAlocPty` |  |  |  |
| 6 | `LI.ALOC.MAI.ALOC.PTY` | `LimitColAllocWork_MaiAlocPty` |  |  |  |
| 7 | `LI.ALOC.ALOCATED.AMT` | `LimitColAllocWork_AlocatedAmt` |  |  |  |
| 8 | `LI.ALOC.COVER.EXTEND` | `LimitColAllocWork_CoverExtend` |  |  |  |
| 9 | `LI.ALOC.AMT.SHORT` | `LimitColAllocWork_AmtShort` |  |  |  |
| 10 | `LI.ALOC.AMT.SHORT.LCY` | `LimitColAllocWork_AmtShortLcy` |  |  |  |
| 11 | `LI.ALOC.COLL.RIGHT.ID` | `LimitColAllocWork_CollRightId` |  |  |  |
| 12 | `LI.ALOC.UNUTIL.COL.AMT` | `LimitColAllocWork_UnutilColAmt` |  |  |  |
| 13 | `LI.ALOC.UNUT.COL.LCY` | `LimitColAllocWork_UnutColLcy` |  |  |  |
| 14 | `LI.ALOC.MODIFIED.MANUALLY` | `LimitColAllocWork_ModifiedManually` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 15 | `LI.ALOC.LAST.REALLOC.TIME` | `LimitColAllocWork_LastReallocTime` | TField |  |  |
| 16 | `LI.ALOC.COLLATERAL.POOL.ID` | `LimitColAllocWork_CollateralPoolId` | TField |  |  |
| 17 | `LI.ALOC.RESERVED.1` | `LimitColAllocWork_Reserved1` | TField |  |  |
| 18 | `LI.ALOC.RECORD.STATUS` | `LimitColAllocWork_RecordStatus` | String |  |  |
| 19 | `LI.ALOC.CURR.NO` | `LimitColAllocWork_CurrNo` | String |  |  |
| 20 | `LI.ALOC.INPUTTER` | `LimitColAllocWork_Inputter` |  |  |  |
| 21 | `LI.ALOC.DATE.TIME` | `LimitColAllocWork_DateTime` |  |  |  |
| 22 | `LI.ALOC.AUTHORISER` | `LimitColAllocWork_Authoriser` | String |  |  |
| 23 | `LI.ALOC.CO.CODE` | `LimitColAllocWork_CoCode` | String |  |  |
| 24 | `LI.ALOC.DEPT.CODE` | `LimitColAllocWork_DeptCode` | String |  |  |
| 25 | `LI.ALOC.AUDITOR.CODE` | `LimitColAllocWork_AuditorCode` | String |  |  |
| 26 | `LI.ALOC.AUDIT.DATE.TIME` | `LimitColAllocWork_AuditDateTime` | String |  |  |
| 27 | `LI.ALOC.ALT.COLR.RIGHT` | `LimitColAllocWork_AltColrRight` |  |  |  |
| 28 | `LI.ALOC.ALT.COLR.ID` | `LimitColAllocWork_AltColrId` |  |  |  |
| 29 | `LI.ALOC.LIMIT.CAP.PERC` | `LimitColAllocWork_LimitCapPerc` |  |  |  |
