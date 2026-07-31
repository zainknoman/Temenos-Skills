# TNCUIN.CUSTOMER.PARAM — Table Schema

> Source: `INSERTS/I_F.TNCUIN.CUSTOMER.PARAM` in `TNCUIN_CustomerCRM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TNCUIN.PARAM.MAJOR.AGE` | `TncuinCustomerParam_MajorAge` | TField |  | This field is to update the age at which the customer is considered as major |
| 2 | `TNCUIN.PARAM.POSTING.RESTRICT` | `TncuinCustomerParam_PostingRestrict` | TField |  | This field is to store which type of posting restriction to be applied for the customer when the document is not submitted Validation: This field should be a valid record from POSTING.RESTRICT |
| 3 | `TNCUIN.PARAM.RELATION.CODE` | `TncuinCustomerParam_RelationCode` | TField |  | This field stores the Relation code which has to be updated for the Minor Validation: This field should be a valid record from RELATION |
| 4 | `TNCUIN.PARAM.REVERSE.RELATION.CODE` | `TncuinCustomerParam_ReverseRelationCode` | TField |  | This field store the Reverse relation code for the Guarantor Validation: This field should be a valid record from RELATION |
| 5 | `TNCUIN.PARAM.STAFF.SECTOR` | `TncuinCustomerParam_StaffSector` |  |  |  |
| 6 | `TNCUIN.PARAM.INDUS.CLASSIFY` | `TncuinCustomerParam_IndusClassify` |  |  |  |
| 7 | `TNCUIN.PARAM.LOCAL.REF` | `TncuinCustomerParam_LocalRef` |  |  |  |
| 8 | `TNCUIN.PARAM.MINOR.POST.RESTRICT` | `TncuinCustomerParam_MinorPostRestrict` | TField |  | This posting restriction code has to set when customer minor at the time of creation |
| 9 | `TNCUIN.PARAM.RESERVED.4` | `TncuinCustomerParam_Reserved4` | TField |  |  |
| 10 | `TNCUIN.PARAM.RESERVED.3` | `TncuinCustomerParam_Reserved3` | TField |  |  |
| 11 | `TNCUIN.PARAM.RESERVED.2` | `TncuinCustomerParam_Reserved2` | TField |  |  |
| 12 | `TNCUIN.PARAM.RESERVED.1` | `TncuinCustomerParam_Reserved1` | TField |  |  |
| 13 | `TNCUIN.PARAM.OVERRIDE` | `TncuinCustomerParam_Override` |  |  |  |
| 14 | `TNCUIN.PARAM.RECORD.STATUS` | `TncuinCustomerParam_RecordStatus` | String |  |  |
| 15 | `TNCUIN.PARAM.CURR.NO` | `TncuinCustomerParam_CurrNo` | String |  |  |
| 16 | `TNCUIN.PARAM.INPUTTER` | `TncuinCustomerParam_Inputter` |  |  |  |
| 17 | `TNCUIN.PARAM.DATE.TIME` | `TncuinCustomerParam_DateTime` |  |  |  |
| 18 | `TNCUIN.PARAM.AUTHORISER` | `TncuinCustomerParam_Authoriser` | String |  |  |
| 19 | `TNCUIN.PARAM.CO.CODE` | `TncuinCustomerParam_CoCode` | String |  |  |
| 20 | `TNCUIN.PARAM.DEPT.CODE` | `TncuinCustomerParam_DeptCode` | String |  |  |
| 21 | `TNCUIN.PARAM.AUDITOR.CODE` | `TncuinCustomerParam_AuditorCode` | String |  |  |
| 22 | `TNCUIN.PARAM.AUDIT.DATE.TIME` | `TncuinCustomerParam_AuditDateTime` | String |  |  |
