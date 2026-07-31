# AA.ACCRUAL.FREQUENCY — Table Schema

> Source: `INSERTS/I_F.AA.ACCRUAL.FREQUENCY` in `AA_Interest.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.ACC.FQU.DEFAULT.LCY` | `AaAccrualFrequency_DefaultLcy` | TField | Yes | This field represents the default accrual frequency for all interest properties in local currency for all the products Validation Rules: Standard date/frequency format. Mandatory input |
| 2 | `AA.ACC.FQU.DEFAULT.FCY` | `AaAccrualFrequency_DefaultFcy` | TField | Yes | This field represents the default accrual frequency for all interest properties in foreign currency for all the products. Validation Rules: Standard date/frequency format. Mandatory input |
| 3 | `AA.ACC.FQU.DEFAULT.OL.ACCRUAL` | `AaAccrualFrequency_DefaultOlAccrual` | TField |  | This field is used to specify if by default system has to project the accruals for all of the properties belonging to all of the products. When the field is set to YES, system will perform accruals(including posting) for all of the properties belonging to all of the products online. The service AA.ONLINE.ACCRUAL.SERVICE needs to be run to perform this process. |
| 4 | `AA.ACC.FQU.PROPERTY` | `AaAccrualFrequency_Property` |  |  |  |
| 5 | `AA.ACC.FQU.PROPERTY.OL.ACCRUAL` | `AaAccrualFrequency_PropertyOlAccrual` |  |  |  |
| 6 | `AA.ACC.FQU.PROPERTY.LCY` | `AaAccrualFrequency_PropertyLcy` |  |  |  |
| 7 | `AA.ACC.FQU.PROPERTY.FCY` | `AaAccrualFrequency_PropertyFcy` |  |  |  |
| 8 | `AA.ACC.FQU.PRODUCT` | `AaAccrualFrequency_Product` |  |  |  |
| 9 | `AA.ACC.FQU.PROD.PROP` | `AaAccrualFrequency_ProdProp` |  |  |  |
| 10 | `AA.ACC.FQU.PROD.PROP.OL.ACCRUAL` | `AaAccrualFrequency_ProdPropOlAccrual` |  |  |  |
| 11 | `AA.ACC.FQU.PRD.PROP.LCY` | `AaAccrualFrequency_PrdPropLcy` |  |  |  |
| 12 | `AA.ACC.FQU.PRD.PROP.FCY` | `AaAccrualFrequency_PrdPropFcy` |  |  |  |
| 13 | `AA.ACC.FQU.LOCAL.REF` | `AaAccrualFrequency_LocalRef` |  |  |  |
| 14 | `AA.ACC.FQU.FORCED.TO.SOD` | `AaAccrualFrequency_Reserved10` |  |  |  |
| 15 | `AA.ACC.FQU.RESERVED09` | `AaAccrualFrequency_Reserved09` | TField |  |  |
| 16 | `AA.ACC.FQU.RESERVED08` | `AaAccrualFrequency_Reserved08` | TField |  |  |
| 17 | `AA.ACC.FQU.RESERVED07` | `AaAccrualFrequency_Reserved07` | TField |  |  |
| 18 | `AA.ACC.FQU.RESERVED06` | `AaAccrualFrequency_Reserved06` | TField |  |  |
| 19 | `AA.ACC.FQU.RESERVED05` | `AaAccrualFrequency_Reserved05` | TField |  |  |
| 20 | `AA.ACC.FQU.RESERVED04` | `AaAccrualFrequency_Reserved04` | TField |  |  |
| 21 | `AA.ACC.FQU.RESERVED03` | `AaAccrualFrequency_Reserved03` | TField |  |  |
| 22 | `AA.ACC.FQU.RESERVED02` | `AaAccrualFrequency_Reserved02` | TField |  |  |
| 23 | `AA.ACC.FQU.RESERVED01` | `AaAccrualFrequency_Reserved01` | TField |  |  |
| 24 | `AA.ACC.FQU.RECORD.STATUS` | `AaAccrualFrequency_RecordStatus` | String |  |  |
| 25 | `AA.ACC.FQU.CURR.NO` | `AaAccrualFrequency_CurrNo` | String |  |  |
| 26 | `AA.ACC.FQU.INPUTTER` | `AaAccrualFrequency_Inputter` |  |  |  |
| 27 | `AA.ACC.FQU.DATE.TIME` | `AaAccrualFrequency_DateTime` |  |  |  |
| 28 | `AA.ACC.FQU.AUTHORISER` | `AaAccrualFrequency_Authoriser` | String |  |  |
| 29 | `AA.ACC.FQU.CO.CODE` | `AaAccrualFrequency_CoCode` | String |  |  |
| 30 | `AA.ACC.FQU.DEPT.CODE` | `AaAccrualFrequency_DeptCode` | String |  |  |
| 31 | `AA.ACC.FQU.AUDITOR.CODE` | `AaAccrualFrequency_AuditorCode` | String |  |  |
| 32 | `AA.ACC.FQU.AUDIT.DATE.TIME` | `AaAccrualFrequency_AuditDateTime` | String |  |  |
