# XML.TAG.DEFINITION — Table Schema

> Source: `INSERTS/I_F.XML.TAG.DEFINITION` in `IX_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `XML.DESCRIPTION` | `XmlTagDefinition_Description` |  |  |  |
| 2 | `XML.DATA.SOURCE` | `XmlTagDefinition_DataSource` | TField |  | DATA SOURCE This field defines the source where the data for the User configurable tag will be retrieved The possible values are VALUE, API, TABLE VALUE is used if the data for the tag is a fixed value API if the data for the tag is to be retrieved through an API TABLE if the data for the tag is directly linked to a T24 table Validation Rules: Allowed to input only for User Configurable Child Data tags |
| 3 | `XML.SOURCE.VALUE` | `XmlTagDefinition_SourceValue` | TField | Yes | SOURCE VALUE This field will contain a fixed value if the DATA.SOURCE is set to VALUE. If the DATA.SOURCE is set to API, this field will contain the name of the API to call to get the data Validation Rules: Allowed to input only for User Configurable Child Data tags Input is mandatory if DATA.SOURCE is set to VALUE or API Input not allowed if the DATA.SOURCE is set to TABLE |
| 4 | `XML.SOURCE.TABLE` | `XmlTagDefinition_SourceTable` | TField | Yes | SOURCE.TABLE This field holds a T24 table name from which data for the tag is to be retrieved Validation Rules: Allowed to input only for User Configurable Child Data tags Input is allowed only if DATA.SOURCE is set to TABLE Mandatory input in case of DATA.SOURCE set to TABLE |
| 5 | `XML.SOURCE.FIELD` | `XmlTagDefinition_SourceField` | TField |  | SOURCE FIELD This field will hold a valid field name from the table defined as SOURCE.TABLE The field name specified can also be a local reference field |
| 6 | `XML.SOURCE.LINK` | `XmlTagDefinition_SourceLink` | TField |  | SOURCE LINK This field will hold link from the STMT.ENTRY record to the source table defined It will be a valid field in STMT.ENTRY record which is the Id of the defined source table Validation Rules: Allowed to input only for User Configurable Child Data tags |
| 7 | `XML.SUPPRESS.FLAG` | `XmlTagDefinition_SuppressFlag` | TField | No | SUPPRESS.FLAG If this field is set to YES then the tag will not be included in the CAMT message Validation Rules: Allowed to input only for Optional tags |
| 8 | `XML.LOCAL.REF` | `XmlTagDefinition_LocalRef` |  |  |  |
| 9 | `XML.MANDATORY.OPT` | `XmlTagDefinition_MandatoryOpt` | TField | Conditional | MANDATORY.OPT To indicate whether the tag is mandatory or optional If set to 'YES', tag is mandatory. Validation Rules: Options are YES/NO System maintained. No manual input. |
| 10 | `XML.USER.CONFIG` | `XmlTagDefinition_UserConfig` | TField |  | USER.CONFIG Indicates whether the value of the tag can be customized. Tag can be customisable only when set to 'YES'. Validation Rules: Options are YES/NO System maintained. No manual input. |
| 11 | `XML.GROUP.TAG` | `XmlTagDefinition_GroupTag` | TField |  | GROUP.TAG Field to identify whether the record is parent tag or child group tag or data tag Allowed values are PARENT, CHILD, DATA |
| 12 | `XML.SUPPRESS.RTN` | `XmlTagDefinition_SuppressRtn` | TField | No | SUPPRESS.RTN An API to determine whether the group tag to be suppressed Validation Rules: Allowed to input only when the tag is optional and user configurable Should be a valid EB.API |
| 13 | `XML.DETAIL.RTN` | `XmlTagDefinition_DetailRtn` | TField |  | DETAIL.RTN An API to return the details for all the tags under the group Validation Rules: Should be a valid EB.API Allowed to input only for the Group tags that are User configurable |
| 14 | `XML.RESERVED.10` | `XmlTagDefinition_Reserved10` | TField |  |  |
| 15 | `XML.RESERVED.09` | `XmlTagDefinition_Reserved09` | TField |  |  |
| 16 | `XML.MSG.TYPE` | `XmlTagDefinition_MsgType` |  |  |  |
| 17 | `XML.MSG.SUPPRESS` | `XmlTagDefinition_MsgSuppress` |  |  |  |
| 18 | `XML.MSG.SUPPRESS.RTN` | `XmlTagDefinition_MsgSuppressRtn` |  |  |  |
| 19 | `XML.MSG.DETAILS.RTN` | `XmlTagDefinition_MsgDetailsRtn` |  |  |  |
| 20 | `XML.RESERVED.08` | `XmlTagDefinition_Reserved08` |  |  |  |
| 21 | `XML.RESERVED.07` | `XmlTagDefinition_Reserved07` |  |  |  |
| 22 | `XML.APP.TXN.ID` | `XmlTagDefinition_AppTxnId` |  |  |  |
| 23 | `XML.APP.SUPPRESS` | `XmlTagDefinition_AppSuppress` |  |  |  |
| 24 | `XML.APP.SUPPRESS.RTN` | `XmlTagDefinition_AppSuppressRtn` |  |  |  |
| 25 | `XML.APP.DETAILS.RTN` | `XmlTagDefinition_AppDetailsRtn` |  |  |  |
| 26 | `XML.RESERVED.06` | `XmlTagDefinition_Reserved06` |  |  |  |
| 27 | `XML.RESERVED.05` | `XmlTagDefinition_Reserved05` |  |  |  |
| 28 | `XML.CHILD.TAG` | `XmlTagDefinition_ChildTag` |  |  |  |
| 29 | `XML.PARENT.GROUP` | `XmlTagDefinition_ParentGroup` | TField |  | PARENT.GROUP Indicates the group tag which is the parent to the underlying parent tag or data tag. Validation Rules: Valid XML.TAG.DEFINITION record with GROUP.TAG field as PARENT System maintained. No manual input. |
| 30 | `XML.CHILD.GROUP` | `XmlTagDefinition_ChildGroup` |  |  |  |
| 31 | `XML.RESERVED.04` | `XmlTagDefinition_Reserved04` | TField |  |  |
| 32 | `XML.RESERVED.03` | `XmlTagDefinition_Reserved03` | TField |  |  |
| 33 | `XML.RESERVED.02` | `XmlTagDefinition_Reserved02` | TField |  |  |
| 34 | `XML.RESERVED.01` | `XmlTagDefinition_Reserved01` | TField |  |  |
| 35 | `XML.RECORD.STATUS` | `XmlTagDefinition_RecordStatus` | String |  |  |
| 36 | `XML.CURR.NO` | `XmlTagDefinition_CurrNo` | String |  |  |
| 37 | `XML.INPUTTER` | `XmlTagDefinition_Inputter` |  |  |  |
| 38 | `XML.DATE.TIME` | `XmlTagDefinition_DateTime` |  |  |  |
| 39 | `XML.AUTHORISER` | `XmlTagDefinition_Authoriser` | String |  |  |
| 40 | `XML.CO.CODE` | `XmlTagDefinition_CoCode` | String |  |  |
| 41 | `XML.DEPT.CODE` | `XmlTagDefinition_DeptCode` | String |  |  |
| 42 | `XML.AUDITOR.CODE` | `XmlTagDefinition_AuditorCode` | String |  |  |
| 43 | `XML.AUDIT.DATE.TIME` | `XmlTagDefinition_AuditDateTime` | String |  |  |
