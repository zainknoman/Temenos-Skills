# AA.DECISION.PARAMETER — Table Schema

> Source: `INSERTS/I_F.AA.DECISION.PARAMETER` in `AA_Services.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.DEP.DESCRIPTION` | `AaDecisionParameter_Description` |  |  |  |
| 2 | `AA.DEP.DEFAULT.DECISION` | `AaDecisionParameter_DefaultDecision` | TField |  |  |
| 3 | `AA.DEP.PRODUCT.LINE` | `AaDecisionParameter_ProductLine` |  |  |  |
| 4 | `AA.DEP.PRODUCT.GROUP` | `AaDecisionParameter_ProductGroup` |  |  |  |
| 5 | `AA.DEP.PRODUCT` | `AaDecisionParameter_Product` |  |  |  |
| 6 | `AA.DEP.ACTIVITY.CLASS` | `AaDecisionParameter_ActivityClass` |  |  |  |
| 7 | `AA.DEP.ACTIVITY` | `AaDecisionParameter_Activity` |  |  |  |
| 8 | `AA.DEP.ARRANGEMENT.COMPANY` | `AaDecisionParameter_ArrangementCompany` |  |  |  |
| 9 | `AA.DEP.RESERVED.10` | `AaDecisionParameter_Reserved10` |  |  |  |
| 10 | `AA.DEP.RESERVED.09` | `AaDecisionParameter_Reserved09` |  |  |  |
| 11 | `AA.DEP.RESERVED.08` | `AaDecisionParameter_Reserved08` |  |  |  |
| 12 | `AA.DEP.RESERVED.07` | `AaDecisionParameter_Reserved07` |  |  |  |
| 13 | `AA.DEP.RESERVED.06` | `AaDecisionParameter_Reserved06` |  |  |  |
| 14 | `AA.DEP.DECISION` | `AaDecisionParameter_Decision` |  |  |  |
| 15 | `AA.DEP.RESERVED.05` | `AaDecisionParameter_Reserved05` | TField |  |  |
| 16 | `AA.DEP.RESERVED.04` | `AaDecisionParameter_Reserved04` | TField |  |  |
| 17 | `AA.DEP.RESERVED.03` | `AaDecisionParameter_Reserved03` | TField |  |  |
| 18 | `AA.DEP.RESERVED.02` | `AaDecisionParameter_Reserved02` | TField |  |  |
| 19 | `AA.DEP.RESERVED.01` | `AaDecisionParameter_Reserved01` | TField |  |  |
| 20 | `AA.DEP.LOCAL.REF` | `AaDecisionParameter_LocalRef` |  |  |  |
| 21 | `AA.DEP.OVERRIDE` | `AaDecisionParameter_Override` |  |  |  |
| 22 | `AA.DEP.RECORD.STATUS` | `AaDecisionParameter_RecordStatus` | String |  |  |
| 23 | `AA.DEP.CURR.NO` | `AaDecisionParameter_CurrNo` | String |  |  |
| 24 | `AA.DEP.INPUTTER` | `AaDecisionParameter_Inputter` |  |  |  |
| 25 | `AA.DEP.DATE.TIME` | `AaDecisionParameter_DateTime` |  |  |  |
| 26 | `AA.DEP.AUTHORISER` | `AaDecisionParameter_Authoriser` | String |  |  |
| 27 | `AA.DEP.CO.CODE` | `AaDecisionParameter_CoCode` | String |  |  |
| 28 | `AA.DEP.DEPT.CODE` | `AaDecisionParameter_DeptCode` | String |  |  |
| 29 | `AA.DEP.AUDITOR.CODE` | `AaDecisionParameter_AuditorCode` | String |  |  |
| 30 | `AA.DEP.AUDIT.DATE.TIME` | `AaDecisionParameter_AuditDateTime` | String |  |  |
