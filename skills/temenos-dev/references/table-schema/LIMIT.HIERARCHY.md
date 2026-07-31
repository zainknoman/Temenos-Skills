# LIMIT.HIERARCHY — Table Schema

> Source: `INSERTS/I_F.LIMIT.HIERARCHY` in `LI_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.LH.GRP.REP.LIMIT` | `LimitHierarchy_GrpRepLimit` |  |  |  |
| 2 | `LI.LH.GRP.REP.LIMIT.FV` | `LimitHierarchy_GrpRepLimitFv` |  |  |  |
| 3 | `LI.LH.CUSTOMER.ID` | `LimitHierarchy_CustomerId` |  |  |  |
| 4 | `LI.LH.CUST.REP.LIMIT` | `LimitHierarchy_CustRepLimit` |  |  |  |
| 5 | `LI.LH.CUST.REP.LIMIT.FV` | `LimitHierarchy_CustRepLimitFv` |  |  |  |
| 6 | `LI.LH.RESERVED.10` | `LimitHierarchy_Reserved10` |  |  |  |
| 7 | `LI.LH.RESERVED.9` | `LimitHierarchy_Reserved9` |  |  |  |
| 8 | `LI.LH.RESERVED.8` | `LimitHierarchy_Reserved8` |  |  |  |
| 9 | `LI.LH.RESERVED.7` | `LimitHierarchy_Reserved7` |  |  |  |
| 10 | `LI.LH.RESERVED.6` | `LimitHierarchy_Reserved6` |  |  |  |
| 11 | `LI.LH.VAL.LIMIT.PROD` | `LimitHierarchy_ValLimitProd` | TField |  | Contains the Limit Product defined in the Validation limit. |
| 12 | `LI.LH.VAL.LIMIT.FV` | `LimitHierarchy_ValLimitFv` | TField |  | Conatins the FIXED.VARIABLE marker defined in the Validation limit. |
| 13 | `LI.LH.VAL.LIMIT.JOINT` | `LimitHierarchy_ValLimitJoint` | TField |  | Contains the JOINT.LIABILITY flag defined in the Validation limit. |
| 14 | `LI.LH.PROD.REP.LIMIT` | `LimitHierarchy_ProdRepLimit` |  |  |  |
| 15 | `LI.LH.PROD.REP.LIMIT.FV` | `LimitHierarchy_ProdRepLimitFv` |  |  |  |
| 16 | `LI.LH.UTIL.LIMIT.ID` | `LimitHierarchy_UtilLimitId` |  |  |  |
| 17 | `LI.LH.UTIL.LIMIT.LEVEL` | `LimitHierarchy_UtilLimitLevel` |  |  |  |
| 18 | `LI.LH.UTIL.LIMIT.PROD` | `LimitHierarchy_UtilLimitProd` |  |  |  |
| 19 | `LI.LH.UTIL.LIMIT.CUSTOMER` | `LimitHierarchy_UtilLimitCustomer` |  |  |  |
| 20 | `LI.LH.UTIL.LIMIT.FV` | `LimitHierarchy_UtilLimitFv` |  |  |  |
| 21 | `LI.LH.UTIL.LIMIT.CHILD` | `LimitHierarchy_UtilLimitChild` |  |  |  |
| 22 | `LI.LH.UTIL.LIMIT.PARENT` | `LimitHierarchy_UtilLimitParent` |  |  |  |
| 23 | `LI.LH.RESERVED.5` | `LimitHierarchy_Reserved5` |  |  |  |
| 24 | `LI.LH.RESERVED.4` | `LimitHierarchy_Reserved4` |  |  |  |
| 25 | `LI.LH.RESERVED.3` | `LimitHierarchy_Reserved3` |  |  |  |
| 26 | `LI.LH.RESERVED.2` | `LimitHierarchy_Reserved2` |  |  |  |
| 27 | `LI.LH.RESERVED.1` | `LimitHierarchy_Reserved1` |  |  |  |
| 28 | `LI.LH.GRP.REP.RISK.GRP` | `LimitHierarchy_GrpRepRiskGrp` |  |  |  |
| 29 | `LI.LH.PROD.REP.RISK.GRP` | `LimitHierarchy_ProdRepRiskGrp` |  |  |  |
