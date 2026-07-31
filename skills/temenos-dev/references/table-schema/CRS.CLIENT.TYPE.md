# CRS.CLIENT.TYPE — Table Schema

> Source: `INSERTS/I_F.CRS.CLIENT.TYPE` in `CD_CustomerIdentification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CD.CT.DESCRIPTION` | `CrsClientType_Description` | TField | Yes | Holds the descriptive information of the record. Validation rules: Any free text Mandatory field. |
| 2 | `CD.CT.CRS.CODE` | `CrsClientType_CrsCode` | TField |  | Each client type classified under CRS is represented with a corresponding code to be used in CRS reporting. This field holds a valid CRS code for every client type record defined using this table. The code is then used in CRS.CUST.SUPP.INFO record to identify the customer as belonging to INDIVIDUAL classification or under ENTITY. Validation rules: The allowed values are: CRS101 CRS102 CRS103 REST - Additional for the client types who doesnt fall under above three categories yet to be reported. CRS101, CRS102, CRS103 are codes for entities. Any other CRS code or no CRS code is considered as Individual by default. CRS Code REST means neither Individual nor entity. |
| 3 | `CD.CT.CUS.FIELD.NAME` | `CrsClientType_CusFieldName` |  |  |  |
| 4 | `CD.CT.CUS.OPERATOR` | `CrsClientType_CusOperator` |  |  |  |
| 5 | `CD.CT.CUS.FIELD.VALUE` | `CrsClientType_CusFieldValue` |  |  |  |
| 6 | `CD.CT.RULE.TYPE` | `CrsClientType_RuleType` |  |  |  |
| 7 | `CD.CT.RULE.ID` | `CrsClientType_RuleId` |  |  |  |
| 8 | `CD.CT.IS.PASSIVE.NFE` | `CrsClientType_IsPassiveNfe` | TField |  | Field to specify if the entity is of type Passive Non Financial Entity. Yes or No field Input allowed only for ENTITY client types. Client types with CRS code as CRS101, CRS102 or CRS103 are considered as Entities |
| 9 | `CD.CT.RESERVED.04` | `CrsClientType_Reserved04` | TField |  |  |
| 10 | `CD.CT.RESERVED.03` | `CrsClientType_Reserved03` | TField |  |  |
| 11 | `CD.CT.RESERVED.02` | `CrsClientType_Reserved02` | TField |  |  |
| 12 | `CD.CT.RESERVED.01` | `CrsClientType_Reserved01` | TField |  |  |
| 13 | `CD.CT.LOCAL.REF` | `CrsClientType_LocalRef` |  |  |  |
| 14 | `CD.CT.OVERRIDE` | `CrsClientType_Override` |  |  |  |
| 15 | `CD.CT.RECORD.STATUS` | `CrsClientType_RecordStatus` | String |  |  |
| 16 | `CD.CT.CURR.NO` | `CrsClientType_CurrNo` | String |  |  |
| 17 | `CD.CT.INPUTTER` | `CrsClientType_Inputter` |  |  |  |
| 18 | `CD.CT.DATE.TIME` | `CrsClientType_DateTime` |  |  |  |
| 19 | `CD.CT.AUTHORISER` | `CrsClientType_Authoriser` | String |  |  |
| 20 | `CD.CT.CO.CODE` | `CrsClientType_CoCode` | String |  |  |
| 21 | `CD.CT.DEPT.CODE` | `CrsClientType_DeptCode` | String |  |  |
| 22 | `CD.CT.AUDITOR.CODE` | `CrsClientType_AuditorCode` | String |  |  |
| 23 | `CD.CT.AUDIT.DATE.TIME` | `CrsClientType_AuditDateTime` | String |  |  |
