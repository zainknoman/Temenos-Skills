# AA.PROPERTY.CLASS — Table Schema

> Source: `INSERTS/I_F.AA.PROPERTY.CLASS` in `AA_ProductFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PC.DESCRIPTION` | `AaPropertyClass_Description` |  |  |  |
| 2 | `AA.PC.FULL.DESC` | `AaPropertyClass_FullDesc` |  |  |  |
| 3 | `AA.PC.TYPE` | `AaPropertyClass_Type` |  |  |  |
| 4 | `AA.PC.LINKED.PROP.CLASS` | `AaPropertyClass_LinkedPropClass` |  |  |  |
| 5 | `AA.PC.PRODUCT.LINE` | `AaPropertyClass_ProductLine` |  |  |  |
| 6 | `AA.PC.BALANCE.PREFIX` | `AaPropertyClass_BalancePrefix` |  |  |  |
| 7 | `AA.PC.CLASS.GROUP` | `AaPropertyClass_ClassGroup` | TField |  | This field can be used for grouping of products. The list of groups available can be defined in the EB.LOOKUP file for AA.PC.GROUP. Used for enquiry and display purposes for filtering out the required classes. |
| 8 | `AA.PC.DEL.INFO.REQD` | `AaPropertyClass_DelInfoReqd` | TField |  | This field denotes whether delivery information is required for the property class. If this field is set to Y then delivery processing is done for the property class |
| 9 | `AA.PC.RESERVED08` | `AaPropertyClass_Reserved08` | TField |  |  |
| 10 | `AA.PC.RESERVED07` | `AaPropertyClass_Reserved07` | TField |  |  |
| 11 | `AA.PC.RESERVED06` | `AaPropertyClass_Reserved06` | TField |  |  |
| 12 | `AA.PC.RESERVED05` | `AaPropertyClass_Reserved05` | TField |  |  |
| 13 | `AA.PC.RESERVED04` | `AaPropertyClass_Reserved04` | TField |  |  |
| 14 | `AA.PC.RESERVED03` | `AaPropertyClass_Reserved03` | TField |  |  |
| 15 | `AA.PC.RESERVED02` | `AaPropertyClass_Reserved02` | TField |  |  |
| 16 | `AA.PC.LOCAL.REF` | `AaPropertyClass_LocalRef` |  |  |  |
| 17 | `AA.PC.RECORD.STATUS` | `AaPropertyClass_RecordStatus` | String |  |  |
| 18 | `AA.PC.CURR.NO` | `AaPropertyClass_CurrNo` | String |  |  |
| 19 | `AA.PC.INPUTTER` | `AaPropertyClass_Inputter` |  |  |  |
| 20 | `AA.PC.DATE.TIME` | `AaPropertyClass_DateTime` |  |  |  |
| 21 | `AA.PC.AUTHORISER` | `AaPropertyClass_Authoriser` | String |  |  |
| 22 | `AA.PC.CO.CODE` | `AaPropertyClass_CoCode` | String |  |  |
| 23 | `AA.PC.DEPT.CODE` | `AaPropertyClass_DeptCode` | String |  |  |
| 24 | `AA.PC.AUDITOR.CODE` | `AaPropertyClass_AuditorCode` | String |  |  |
| 25 | `AA.PC.AUDIT.DATE.TIME` | `AaPropertyClass_AuditDateTime` | String |  |  |
| 26 | `AA.PC.BALANCE.SUFFIX` | `AaPropertyClass_BalanceSuffix` |  |  |  |
| 27 | `AA.PC.API.ATTRIBUTE.TYPE` | `AaPropertyClass_ApiAttributeType` | TField |  |  |
