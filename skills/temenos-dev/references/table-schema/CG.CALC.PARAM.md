# CG.CALC.PARAM — Table Schema

> Source: `INSERTS/I_F.CG.CALC.PARAM` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CG.CALC.CG.FROM.DATE` | `CgCalcParam_CgFromDate` | TField | Yes | This field will hold the date only after which Capital gains will be calculated and updated in base record. Capital gains will be calculated only for lots purchased after this date. Validation Rules: This field is a mandatory field. This will be a standard date field |
| 2 | `CG.CALC.DATE` | `CgCalcParam_Date` |  |  |  |
| 3 | `CG.CALC.CG.ST.CALC.METHOD` | `CgCalcParam_CgStCalcMethod` |  |  |  |
| 4 | `CG.CALC.CG.LT.CALC.METHOD` | `CgCalcParam_CgLtCalcMethod` |  |  |  |
| 5 | `CG.CALC.INDEX.MTD.UPTO.DATE` | `CgCalcParam_IndexMtdUptoDate` |  |  |  |
| 6 | `CG.CALC.INDEX.QTR.NUMERATOR` | `CgCalcParam_IndexQtrNumerator` |  |  |  |
| 7 | `CG.CALC.INDEX.QTR.DENOM` | `CgCalcParam_IndexQtrDenom` |  |  |  |
| 8 | `CG.CALC.CALC.API` | `CgCalcParam_CalcApi` |  |  |  |
| 9 | `CG.CALC.EXC.EXEMPT.LOT` | `CgCalcParam_ExcExemptLot` | TField |  |  |
| 10 | `CG.CALC.RESERVED.19` | `CgCalcParam_Reserved19` | TField |  |  |
| 11 | `CG.CALC.RESERVED.18` | `CgCalcParam_Reserved18` | TField |  |  |
| 12 | `CG.CALC.RESERVED.17` | `CgCalcParam_Reserved17` | TField |  |  |
| 13 | `CG.CALC.RESERVED.16` | `CgCalcParam_Reserved16` | TField |  |  |
| 14 | `CG.CALC.RESERVED.15` | `CgCalcParam_Reserved15` | TField |  |  |
| 15 | `CG.CALC.RESERVED.14` | `CgCalcParam_Reserved14` | TField |  |  |
| 16 | `CG.CALC.RESERVED.13` | `CgCalcParam_Reserved13` | TField |  |  |
| 17 | `CG.CALC.RESERVED.12` | `CgCalcParam_Reserved12` | TField |  |  |
| 18 | `CG.CALC.RESERVED.11` | `CgCalcParam_Reserved11` | TField |  |  |
| 19 | `CG.CALC.RESERVED.10` | `CgCalcParam_Reserved10` | TField |  |  |
| 20 | `CG.CALC.RESERVED.9` | `CgCalcParam_Reserved9` | TField |  |  |
| 21 | `CG.CALC.RESERVED.8` | `CgCalcParam_Reserved8` | TField |  |  |
| 22 | `CG.CALC.RESERVED.7` | `CgCalcParam_Reserved7` | TField |  |  |
| 23 | `CG.CALC.RESERVED.6` | `CgCalcParam_Reserved6` | TField |  |  |
| 24 | `CG.CALC.RESERVED.5` | `CgCalcParam_Reserved5` | TField |  |  |
| 25 | `CG.CALC.RESERVED.4` | `CgCalcParam_Reserved4` | TField |  |  |
| 26 | `CG.CALC.RESERVED.3` | `CgCalcParam_Reserved3` | TField |  |  |
| 27 | `CG.CALC.RESERVED.2` | `CgCalcParam_Reserved2` | TField |  |  |
| 28 | `CG.CALC.RESERVED.1` | `CgCalcParam_Reserved1` | TField |  |  |
| 29 | `CG.CALC.LOCAL.REF` | `CgCalcParam_LocalRef` |  |  |  |
| 30 | `CG.CALC.OVERRIDE` | `CgCalcParam_Override` |  |  |  |
| 31 | `CG.CALC.RECORD.STATUS` | `CgCalcParam_RecordStatus` | String |  |  |
| 32 | `CG.CALC.CURR.NO` | `CgCalcParam_CurrNo` | String |  |  |
| 33 | `CG.CALC.INPUTTER` | `CgCalcParam_Inputter` |  |  |  |
| 34 | `CG.CALC.DATE.TIME` | `CgCalcParam_DateTime` |  |  |  |
| 35 | `CG.CALC.AUTHORISER` | `CgCalcParam_Authoriser` | String |  |  |
| 36 | `CG.CALC.CO.CODE` | `CgCalcParam_CoCode` | String |  |  |
| 37 | `CG.CALC.DEPT.CODE` | `CgCalcParam_DeptCode` | String |  |  |
| 38 | `CG.CALC.AUDITOR.CODE` | `CgCalcParam_AuditorCode` | String |  |  |
| 39 | `CG.CALC.AUDIT.DATE.TIME` | `CgCalcParam_AuditDateTime` | String |  |  |
