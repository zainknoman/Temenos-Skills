# AM.MATRIX — Table Schema

> Source: `INSERTS/I_F.AM.MATRIX` in `AM_Modelling.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.MAT.DESCRIPTION` | `AmMatrix_Description` |  |  |  |
| 2 | `AM.MAT.AXIS.X` | `AmMatrix_AxisX` | TField | No | Contains the axis which will determine the abscissa of the matrix. Validation Rules: Must be a valid axis code (Optional input) |
| 3 | `AM.MAT.AXIS.Y` | `AmMatrix_AxisY` | TField | No | Contains the axis that will determine the ordinate of the matrix. Validation Rules: Must be a valid axis (Optional input) |
| 4 | `AM.MAT.MEMBER.X` | `AmMatrix_MemberX` |  |  |  |
| 5 | `AM.MAT.MEMBER.Y` | `AmMatrix_MemberY` |  |  |  |
| 6 | `AM.MAT.WEIGHT` | `AmMatrix_Weight` |  |  |  |
| 7 | `AM.MAT.DEVIATION.MAX` | `AmMatrix_DeviationMax` |  |  |  |
| 8 | `AM.MAT.DEVIATION.MIN` | `AmMatrix_DeviationMin` |  |  |  |
| 9 | `AM.MAT.REBALANCE` | `AmMatrix_Rebalance` |  |  |  |
| 10 | `AM.MAT.LINK` | `AmMatrix_Link` |  |  |  |
| 11 | `AM.MAT.BENCHMARK` | `AmMatrix_Benchmark` | TField |  | This field takes value from AM.BENCHMARK , provided this matrix has the benchmark record. |
| 12 | `AM.MAT.UPD.BENCHMARK.WGT` | `AmMatrix_UpdBenchmarkWgt` | TField |  | It can be set as YES or NO .If it is set to YES it calculates weightage for the corresponding benchmark and update it in BENCH.WGT field of AM.BENCHMARK . |
| 13 | `AM.MAT.PRIORITY.X` | `AmMatrix_PriorityX` |  |  |  |
| 14 | `AM.MAT.PRIORITY.Y` | `AmMatrix_PriorityY` |  |  |  |
| 15 | `AM.MAT.RESERVED.5` | `AmMatrix_Reserved5` | TField |  |  |
| 16 | `AM.MAT.RESERVED.4` | `AmMatrix_Reserved4` | TField |  |  |
| 17 | `AM.MAT.RESERVED.3` | `AmMatrix_Reserved3` | TField |  |  |
| 18 | `AM.MAT.RESERVED.2` | `AmMatrix_Reserved2` | TField |  |  |
| 19 | `AM.MAT.RESERVED.1` | `AmMatrix_Reserved1` | TField |  |  |
| 20 | `AM.MAT.LOCAL.REF` | `AmMatrix_LocalRef` |  |  |  |
| 21 | `AM.MAT.OVERRIDE` | `AmMatrix_Override` |  |  |  |
| 22 | `AM.MAT.RECORD.STATUS` | `AmMatrix_RecordStatus` | String |  |  |
| 23 | `AM.MAT.CURR.NO` | `AmMatrix_CurrNo` | String |  |  |
| 24 | `AM.MAT.INPUTTER` | `AmMatrix_Inputter` |  |  |  |
| 25 | `AM.MAT.DATE.TIME` | `AmMatrix_DateTime` |  |  |  |
| 26 | `AM.MAT.AUTHORISER` | `AmMatrix_Authoriser` | String |  |  |
| 27 | `AM.MAT.CO.CODE` | `AmMatrix_CoCode` | String |  |  |
| 28 | `AM.MAT.DEPT.CODE` | `AmMatrix_DeptCode` | String |  |  |
| 29 | `AM.MAT.AUDITOR.CODE` | `AmMatrix_AuditorCode` | String |  |  |
| 30 | `AM.MAT.AUDIT.DATE.TIME` | `AmMatrix_AuditDateTime` | String |  |  |
