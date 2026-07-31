# LBNCDR.COLLATERAL.PARAM — Table Schema

> Source: `INSERTS/I_F.LBNCDR.COLLATERAL.PARAM` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.COL.FAC.LIAB.TYPE` | `LbncdrCollateralParam_FacLiabType` | TField |  | It denotes the facility liability type like ACB AVM etc. Holds the value from the table SGL.LIAB.TYPES and should show the short description and description fields alone. This dropdown should only show the records which has short description UL T WITHOUT UNLIKE T Validation Rules 5 A |
| 2 | `LBNCDR.COL.TOT.COLL.LIAB.TYPE` | `LbncdrCollateralParam_TotCollLiabType` | TField |  | It denotes the total collateral liability type which needs to be added in Risk file. Holds the value from the table SGL.LIAB.TYPES should have a drop down from the table SGL.LIAB.TYPES and should show the short description and description fields alone. This dropdown should only show the records which has short description LK T LIKE T Validation Rules 5 A |
| 3 | `LBNCDR.COL.RANKING` | `LbncdrCollateralParam_Ranking` | TField |  | Holds the ranking based on which the D-line to be written at risk file. This to be defined based on no of collaterals. If the customer has no collateral then RANKING will be null. Validation Rules 2 N |
| 4 | `LBNCDR.COL.RESERVED.1` | `LbncdrCollateralParam_Reserved1` | TField |  |  |
| 5 | `LBNCDR.COL.RESERVED.2` | `LbncdrCollateralParam_Reserved2` | TField |  |  |
| 6 | `LBNCDR.COL.RESERVED.3` | `LbncdrCollateralParam_Reserved3` | TField |  |  |
| 7 | `LBNCDR.COL.RESERVED.4` | `LbncdrCollateralParam_Reserved4` | TField |  |  |
| 8 | `LBNCDR.COL.RESERVED.5` | `LbncdrCollateralParam_Reserved5` | TField |  |  |
| 9 | `LBNCDR.COL.RESERVED.6` | `LbncdrCollateralParam_Reserved6` | TField |  |  |
| 10 | `LBNCDR.COL.RESERVED.7` | `LbncdrCollateralParam_Reserved7` | TField |  |  |
| 11 | `LBNCDR.COL.RESERVED.8` | `LbncdrCollateralParam_Reserved8` | TField |  |  |
| 12 | `LBNCDR.COL.RESERVED.9` | `LbncdrCollateralParam_Reserved9` | TField |  |  |
| 13 | `LBNCDR.COL.RESERVED.10` | `LbncdrCollateralParam_Reserved10` | TField |  |  |
| 14 | `LBNCDR.COL.LOCAL.REF` | `LbncdrCollateralParam_LocalRef` |  |  |  |
| 15 | `LBNCDR.COL.OVERRIDE` | `LbncdrCollateralParam_Override` |  |  |  |
| 16 | `LBNCDR.COL.RECORD.STATUS` | `LbncdrCollateralParam_RecordStatus` | String |  |  |
| 17 | `LBNCDR.COL.CURR.NO` | `LbncdrCollateralParam_CurrNo` | String |  |  |
| 18 | `LBNCDR.COL.INPUTTER` | `LbncdrCollateralParam_Inputter` |  |  |  |
| 19 | `LBNCDR.COL.DATE.TIME` | `LbncdrCollateralParam_DateTime` |  |  |  |
| 20 | `LBNCDR.COL.AUTHORISER` | `LbncdrCollateralParam_Authoriser` | String |  |  |
| 21 | `LBNCDR.COL.CO.CODE` | `LbncdrCollateralParam_CoCode` | String |  |  |
| 22 | `LBNCDR.COL.DEPT.CODE` | `LbncdrCollateralParam_DeptCode` | String |  |  |
| 23 | `LBNCDR.COL.AUDITOR.CODE` | `LbncdrCollateralParam_AuditorCode` | String |  |  |
| 24 | `LBNCDR.COL.AUDIT.DATE.TIME` | `LbncdrCollateralParam_AuditDateTime` | String |  |  |
