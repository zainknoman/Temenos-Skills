# CZ.CDP.PDD.SEARCH.REQUEST — Table Schema

> Source: `INSERTS/I_F.CZ.CDP.PDD.SEARCH.REQUEST` in `CZ_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CZ.CPSR.CLEAR.PREVIOUS.RESULTS` | `CzCdpPddSearchRequest_ClearPreviousResults` | TField |  | The field denotes whether or not to clear the existing search results of the application already present in CZ.CDP.PDD.SEARCH.RESULTS. Validation Rules: Possible values are YES or NO YES clears the existing CZ.CDP.PDD.SEARCH.RESULTS data and NO adds the current search results to the existing data. If no value is specified, the system defaults the field with YES. |
| 2 | `CZ.CPSR.FIELD.TYPE` | `CzCdpPddSearchRequest_FieldType` |  |  |  |
| 3 | `CZ.CPSR.PRODUCT.ID` | `CzCdpPddSearchRequest_ProductId` |  |  |  |
| 4 | `CZ.CPSR.TABLE.NAME` | `CzCdpPddSearchRequest_TableName` |  |  |  |
| 5 | `CZ.CPSR.ID.LOOKUP` | `CzCdpPddSearchRequest_IdLookup` |  |  |  |
| 6 | `CZ.CPSR.ALL.ID.FIELDS` | `CzCdpPddSearchRequest_AllIdFields` |  |  |  |
| 7 | `CZ.CPSR.DATA.LOOKUP` | `CzCdpPddSearchRequest_DataLookup` |  |  |  |
| 8 | `CZ.CPSR.ALL.DATA.FIELDS` | `CzCdpPddSearchRequest_AllDataFields` |  |  |  |
| 9 | `CZ.CPSR.FIELD.NAME` | `CzCdpPddSearchRequest_FieldName` |  |  |  |
| 10 | `CZ.CPSR.DATA.TYPE` | `CzCdpPddSearchRequest_DataType` |  |  |  |
| 11 | `CZ.CPSR.FIELD.LENGTH` | `CzCdpPddSearchRequest_FieldLength` |  |  |  |
| 12 | `CZ.CPSR.PDD.ITEM` | `CzCdpPddSearchRequest_PddItem` | TField |  | This field allows items that are already marked as PDD to be included as part of the search process. A field can be considered marked as PDD if they are already included in CZ.CDP.DATA.DEFINITION or the PDD definition is available in STANDARD.SELECTION. Validation Rule: Possible values are Yes or No. Default is Yes, that is the items already marked as PDD are always included in the search. When set as No the fields will be validated for other criteria, like datatype, fieldname and field length given in the search request. |
| 13 | `CZ.CPSR.RESERVED.20` | `CzCdpPddSearchRequest_Reserved20` | TField |  |  |
| 14 | `CZ.CPSR.RESERVED.19` | `CzCdpPddSearchRequest_Reserved19` | TField |  |  |
| 15 | `CZ.CPSR.RESERVED.18` | `CzCdpPddSearchRequest_Reserved18` | TField |  |  |
| 16 | `CZ.CPSR.RESERVED.17` | `CzCdpPddSearchRequest_Reserved17` | TField |  |  |
| 17 | `CZ.CPSR.RESERVED.16` | `CzCdpPddSearchRequest_Reserved16` | TField |  |  |
| 18 | `CZ.CPSR.RESERVED.15` | `CzCdpPddSearchRequest_Reserved15` | TField |  |  |
| 19 | `CZ.CPSR.RESERVED.14` | `CzCdpPddSearchRequest_Reserved14` | TField |  |  |
| 20 | `CZ.CPSR.RESERVED.13` | `CzCdpPddSearchRequest_Reserved13` | TField |  |  |
| 21 | `CZ.CPSR.RESERVED.12` | `CzCdpPddSearchRequest_Reserved12` | TField |  |  |
| 22 | `CZ.CPSR.RESERVED.11` | `CzCdpPddSearchRequest_Reserved11` | TField |  |  |
| 23 | `CZ.CPSR.RESERVED.10` | `CzCdpPddSearchRequest_Reserved10` | TField |  |  |
| 24 | `CZ.CPSR.RESERVED.09` | `CzCdpPddSearchRequest_Reserved09` | TField |  |  |
| 25 | `CZ.CPSR.RESERVED.08` | `CzCdpPddSearchRequest_Reserved08` | TField |  |  |
| 26 | `CZ.CPSR.RESERVED.07` | `CzCdpPddSearchRequest_Reserved07` | TField |  |  |
| 27 | `CZ.CPSR.RESERVED.06` | `CzCdpPddSearchRequest_Reserved06` | TField |  |  |
| 28 | `CZ.CPSR.RESERVED.05` | `CzCdpPddSearchRequest_Reserved05` | TField |  |  |
| 29 | `CZ.CPSR.RESERVED.04` | `CzCdpPddSearchRequest_Reserved04` | TField |  |  |
| 30 | `CZ.CPSR.RESERVED.03` | `CzCdpPddSearchRequest_Reserved03` | TField |  |  |
| 31 | `CZ.CPSR.RESERVED.02` | `CzCdpPddSearchRequest_Reserved02` | TField |  |  |
| 32 | `CZ.CPSR.RESERVED.01` | `CzCdpPddSearchRequest_Reserved01` | TField |  |  |
| 33 | `CZ.CPSR.LOCAL.REF` | `CzCdpPddSearchRequest_LocalRef` |  |  |  |
| 34 | `CZ.CPSR.RECORD.STATUS` | `CzCdpPddSearchRequest_RecordStatus` | String |  |  |
| 35 | `CZ.CPSR.CURR.NO` | `CzCdpPddSearchRequest_CurrNo` | String |  |  |
| 36 | `CZ.CPSR.INPUTTER` | `CzCdpPddSearchRequest_Inputter` |  |  |  |
| 37 | `CZ.CPSR.DATE.TIME` | `CzCdpPddSearchRequest_DateTime` |  |  |  |
| 38 | `CZ.CPSR.AUTHORISER` | `CzCdpPddSearchRequest_Authoriser` | String |  |  |
| 39 | `CZ.CPSR.CO.CODE` | `CzCdpPddSearchRequest_CoCode` | String |  |  |
| 40 | `CZ.CPSR.DEPT.CODE` | `CzCdpPddSearchRequest_DeptCode` | String |  |  |
| 41 | `CZ.CPSR.AUDITOR.CODE` | `CzCdpPddSearchRequest_AuditorCode` | String |  |  |
| 42 | `CZ.CPSR.AUDIT.DATE.TIME` | `CzCdpPddSearchRequest_AuditDateTime` | String |  |  |
