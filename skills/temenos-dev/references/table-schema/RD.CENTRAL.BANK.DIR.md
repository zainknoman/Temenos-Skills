# RD.CENTRAL.BANK.DIR — Table Schema

> Source: `INSERTS/I_F.RD.CENTRAL.BANK.DIR` in `RD_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RD.CBD.FLAG` | `RdCentralBankDir_Flag` | TField | No | Holds the modification flag provided by SWIFTRef BDP file and will be used by the upload process to handle therecord. Validation Rules: A - Addition. D - Deletion. M - Modification. This is an optional field. |
| 2 | `RD.CBD.SOURCE.KEY` | `RdCentralBankDir_SourceKey` | TField |  |  |
| 3 | `RD.CBD.INSTITUTION.NAME` | `RdCentralBankDir_InstitutionName` |  |  |  |
| 4 | `RD.CBD.CITY` | `RdCentralBankDir_City` | TField |  | Holds the City name of the institution/branch. Wherever possible, the field is standardized. means that maincities are spelled the same way across the file. Validation Rules: The value for this field can be of alphanumeric with the maximum length of 35. |
| 5 | `RD.CBD.BRANCH` | `RdCentralBankDir_Branch` |  |  |  |
| 6 | `RD.CBD.BIC8` | `RdCentralBankDir_Bic8` | TField |  | BIC (party prefix, country, and party suffix) where: party prefix (4 char), country code(2 char), party suffix(2char). Validation Rules: The value for this field can be of alphanumeric with the maximum length of 8. |
| 7 | `RD.CBD.BRANCH.CODE` | `RdCentralBankDir_BranchCode` | TField |  |  |
| 8 | `RD.CBD.BIC` | `RdCentralBankDir_Bic` | TField |  | This is the unique BIC related to the institution. The BIC consists of: party prefix (4 char), country code(2char), party suffix(2 char) , branch identifier (3 char - XXX for main office). Validation Rules: The value for this field can be of alphanumeric with the maximum length of 11. |
| 9 | `RD.CBD.ROUTING.BIC.CODE` | `RdCentralBankDir_RoutingBicCode` | TField |  | If the BIC indicated in the field BIC is not connected to the SWIFT network this will indicate the connected BICof the same institution, if available, or of its correspondent through which it connects. Validation Rules: The value for this field can be of alphanumeric with the maximum length of 11. |
| 10 | `RD.CBD.PARENT.BK.CODE` | `RdCentralBankDir_ParentBkCode` | TField |  | The record key of the parent entity. This value identifies the set of entities (records) belonging to the group.It groups BICs and National ID records that belong to the same parent (parent BIC). Validation Rules: The value for this field can be of alphanumeric with the maximum length of 12. |
| 11 | `RD.CBD.COUNTRY.CODE` | `RdCentralBankDir_CountryCode` | TField |  | ISO country code of the financial institution/branch. Validation Rules: The value for this field should be a valid record in COUNTRY application. The value for this field can be of alphanumeric with the maximum length of 2. |
| 12 | `RD.CBD.NATIONAL.ID` | `RdCentralBankDir_NationalId` | TField |  | This is the National identifier of the institution/branch. This field contains the National bank code for thefinancial institution (for example, BSC codes for UK banks). Validation Rules: The value for this field can be of alphanumeric with the maximum length of 15. |
| 13 | `RD.CBD.NAT.ID.TYPE` | `RdCentralBankDir_NatIdType` | TField |  | This is the name of the national code or the name/acronym of the national code provider. Validation Rules: The value for this field can be of alphanumeric with the maximum length of 70. |
| 14 | `RD.CBD.CHIPSUID` | `RdCentralBankDir_Chipsuid` | TField |  | This field contains the CHIPS Universal ID for the financial institution. Validation Rules: The value for this field can be of alphanumeric with the maximum length of 6. |
| 15 | `RD.CBD.SUBTYPE.IND` | `RdCentralBankDir_SubtypeInd` | TField |  | The business type of the entity. Subtype Indicator is provided only for records with a BIC. For example: a bankor a broker. Validation Rules: This value will be selected from a list (EB.LOOKUP>SUBTYPE.IND). |
| 16 | `RD.CBD.SERVICE.CODES` | `RdCentralBankDir_ServiceCodes` |  |  |  |
| 17 | `RD.CBD.BR.QUALIFIER` | `RdCentralBankDir_BrQualifier` | TField |  | BIC branch qualifiers. Validation Rules: The value for this field can be of alphanumeric with the maximum length of 35. |
| 18 | `RD.CBD.ADDRESS` | `RdCentralBankDir_Address` |  |  |  |
| 19 | `RD.CBD.ZIP` | `RdCentralBankDir_Zip` | TField |  | Zip code of the institution/branch. Validation Rules: The value for this field can be of alphanumeric with the maximum length of 15. |
| 20 | `RD.CBD.LOCATION` | `RdCentralBankDir_Location` |  |  |  |
| 21 | `RD.CBD.COUNTRY` | `RdCentralBankDir_Country` |  |  |  |
| 22 | `RD.CBD.POBNUMBER` | `RdCentralBankDir_Pobnumber` | TField |  | This is the Post Office Box (POB) number that relates to financial institution. Validation Rules: The value for this field can be of alphanumeric with the maximum length of 35. |
| 23 | `RD.CBD.VALID.FROM` | `RdCentralBankDir_ValidFrom` | TField |  | The date since the whole record becomes effective due to a change of its attribute. Validation Rules: Standard date format (YYYYMMDD). Allowed only for uploaded records |
| 24 | `RD.CBD.OFFICE.TYPE` | `RdCentralBankDir_OfficeType` | TField |  | This field indicates the status of the entity in the entities hierarchy. Validation Rules: This value will be selected from a list (EB.LOOKUP>OFFICE.TYPE). |
| 25 | `RD.CBD.PARENT.OFFICE.KEY` | `RdCentralBankDir_ParentOfficeKey` | TField |  | This field indicates the RECORD KEY of the closest entity upwards in the entities hierarchy. Validation Rules: The value for this field can be of alphanumeric with the maximum length of 12. |
| 26 | `RD.CBD.HEAD.OFFICE.KEY` | `RdCentralBankDir_HeadOfficeKey` | TField |  | This field indicates the RECORD KEY of the "HO - Head Office" in the entities hierarchy. Validation Rules: The value for this field can be of alphanumeric with the maximum length of 12. |
| 27 | `RD.CBD.LEGAL.TYPE` | `RdCentralBankDir_LegalType` | TField |  | This field indicates the status of the entity in the legal hierarchy. Validation Rules: This value will be selected from a list (EB.LOOKUP>LEGAL.TYPE). |
| 28 | `RD.CBD.LEGAL.PARENT.KEY` | `RdCentralBankDir_LegalParentKey` | TField |  | This field indicates the RECORD KEY of the "L - Legal Entity" in the legal hierarchy. Validation Rules: The value for this field can be of alphanumeric with the maximum length of 12. |
| 29 | `RD.CBD.GROUP.TYPE` | `RdCentralBankDir_GroupType` | TField |  | The type of entity that identifies the group (Parent or Member). Validation Rules: The value for this field can be of alphanumeric with the maximum length of 6. |
| 30 | `RD.CBD.INSTITUTION.STATUS` | `RdCentralBankDir_InstitutionStatus` | TField |  |  |
| 31 | `RD.CBD.CO.OPER.GROUP.KEY` | `RdCentralBankDir_CoOperGroupKey` | TField |  | If the record indicates a cooperative bank which belongs to a cooperative bank grouping, then this fieldindicates the Record Key of the cooperative central bank for that group. Hierarchy in this case flows downward. Inthe case of any such cooperative central bank, the value here is its own Record Key. If the cooperative bankconcerned does not belong to a cooperative bank grouping, then the field is empty. Validation Rules: The value for this field can be of alphanumeric with the maximum length of 12. |
| 32 | `RD.CBD.ISO.LEI.CODE` | `RdCentralBankDir_IsoLeiCode` | TField |  | The code of the Legal Entity Identifier. Validation Rules: The value for this field can be of alphanumeric with the maximum length of 35. |
| 33 | `RD.CBD.TIMEZONE` | `RdCentralBankDir_Timezone` | TField |  | Time-zone for the entity. Validation Rules: The value for this field can be of alphanumeric with the maximum length of 10. |
| 34 | `RD.CBD.NETWORK.CONNECTION` | `RdCentralBankDir_NetworkConnection` | TField |  | Status of an entity's connection to SWIFT.Network connectivity is provided only for records containing a BIC. Validation Rules: The value for this field can be of alphanumeric with the maximum length of 4. |
| 35 | `RD.CBD.SSI.GROUP.KEY` | `RdCentralBankDir_SsiGroupKey` | TField |  | The SSI Group the entity belongs to. Validation Rules: The value for this field can be of alphanumeric with the maximum length of 12. |
| 36 | `RD.CBD.IBAN.KEY` | `RdCentralBankDir_IbanKey` | TField |  | The key of the record in IBAN Plus which defines the IBAN details for this entity. Validation Rules: The value for this field can be of alphanumeric with the maximum length of 12. |
| 37 | `RD.CBD.ENTRY.TYPE` | `RdCentralBankDir_EntryType` | TField |  | Will indicate if the entry is manually created or created by an upload. Validation Rules: Not allowed for manual input. Possible values are UPLOAD and CUSTOM. |
| 38 | `RD.CBD.SOURCE.NAME` | `RdCentralBankDir_SourceName` | TField |  | This will be the name of the upload file through which the record in the directory has been created/amended .Applicable only for uploaded records. Validation Rules: This field will not be populated when a manual record and it will be populated as a result of the upload process |
| 39 | `RD.CBD.EXCLUDED.COMPANY` | `RdCentralBankDir_ExcludedCompany` |  |  |  |
| 40 | `RD.CBD.ALLOWED.COMPANY` | `RdCentralBankDir_AllowedCompany` |  |  |  |
| 41 | `RD.CBD.STATUS` | `RdCentralBankDir_Status` | TField |  | Indicates status of record. When status is set as DELETE, record will be reversed. Validation Rules: Allowed values are Blank and DELETE. |
| 42 | `RD.CBD.RESERVED.5` | `RdCentralBankDir_Reserved5` | TField |  |  |
| 43 | `RD.CBD.RESERVED.4` | `RdCentralBankDir_Reserved4` | TField |  |  |
| 44 | `RD.CBD.RESERVED.3` | `RdCentralBankDir_Reserved3` | TField |  |  |
| 45 | `RD.CBD.RESERVED.2` | `RdCentralBankDir_Reserved2` | TField |  |  |
| 46 | `RD.CBD.RESERVED.1` | `RdCentralBankDir_Reserved1` | TField |  |  |
| 47 | `RD.CBD.LOCAL.REF` | `RdCentralBankDir_LocalRef` |  |  |  |
| 48 | `RD.CBD.OVERRIDE` | `RdCentralBankDir_Override` |  |  |  |
| 49 | `RD.CBD.RECORD.STATUS` | `RdCentralBankDir_RecordStatus` | String |  |  |
| 50 | `RD.CBD.CURR.NO` | `RdCentralBankDir_CurrNo` | String |  |  |
| 51 | `RD.CBD.INPUTTER` | `RdCentralBankDir_Inputter` |  |  |  |
| 52 | `RD.CBD.DATE.TIME` | `RdCentralBankDir_DateTime` |  |  |  |
| 53 | `RD.CBD.AUTHORISER` | `RdCentralBankDir_Authoriser` | String |  |  |
| 54 | `RD.CBD.CO.CODE` | `RdCentralBankDir_CoCode` | String |  |  |
| 55 | `RD.CBD.DEPT.CODE` | `RdCentralBankDir_DeptCode` | String |  |  |
| 56 | `RD.CBD.AUDITOR.CODE` | `RdCentralBankDir_AuditorCode` | String |  |  |
| 57 | `RD.CBD.AUDIT.DATE.TIME` | `RdCentralBankDir_AuditDateTime` | String |  |  |
