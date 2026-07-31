# CZ.CDP.DATA.DEFINITION — Table Schema

> Source: `INSERTS/I_F.CZ.CDP.DATA.DEFINITION` in `CZ_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CZ.CDS.PRODUCT` | `CzCdpDataDefinition_Product` | TField |  | Valid PRODUCT Id NOINPUT field Product to which the given Application"i.e.ID" belongs to |
| 2 | `CZ.CDS.FILE.TYPE` | `CzCdpDataDefinition_FileType` | TField |  | Possible values are INT, CUS, CST, FIN, FTD, FTF, CCY, NOS NOINPUT field Classification to which the given Application "i.e ID" belongs to. Retrived from FILE.CONTROL of that application |
| 3 | `CZ.CDS.SYS.FIELD.NAME` | `CzCdpDataDefinition_SysFieldName` |  |  |  |
| 4 | `CZ.CDS.SYS.FIELD.ATTRIBUTES` | `CzCdpDataDefinition_SysFieldAttributes` |  |  |  |
| 5 | `CZ.CDS.SYS.PURPOSE` | `CzCdpDataDefinition_SysPurpose` |  |  |  |
| 6 | `CZ.CDS.SYS.ERASE.OPTION` | `CzCdpDataDefinition_SysEraseOption` |  |  |  |
| 7 | `CZ.CDS.SYS.ACCESSIBILITY` | `CzCdpDataDefinition_SysAccessibility` |  |  |  |
| 8 | `CZ.CDS.SYS.EXCLUDE` | `CzCdpDataDefinition_SysExclude` |  |  |  |
| 9 | `CZ.CDS.SYS.PARTY.IDENTIFIER` | `CzCdpDataDefinition_SysPartyIdentifier` |  |  |  |
| 10 | `CZ.CDS.SYS.PARTY.POS.API` | `CzCdpDataDefinition_SysPartyPosApi` |  |  |  |
| 11 | `CZ.CDS.SYS.RESERVED.08` | `CzCdpDataDefinition_SysReserved08` |  |  |  |
| 12 | `CZ.CDS.SYS.RESERVED.07` | `CzCdpDataDefinition_SysReserved07` |  |  |  |
| 13 | `CZ.CDS.SYS.RESERVED.06` | `CzCdpDataDefinition_SysReserved06` |  |  |  |
| 14 | `CZ.CDS.SYS.RESERVED.05` | `CzCdpDataDefinition_SysReserved05` |  |  |  |
| 15 | `CZ.CDS.SYS.RESERVED.04` | `CzCdpDataDefinition_SysReserved04` |  |  |  |
| 16 | `CZ.CDS.SYS.RESERVED.03` | `CzCdpDataDefinition_SysReserved03` |  |  |  |
| 17 | `CZ.CDS.SYS.RESERVED.02` | `CzCdpDataDefinition_SysReserved02` |  |  |  |
| 18 | `CZ.CDS.SYS.RESERVED.01` | `CzCdpDataDefinition_SysReserved01` |  |  |  |
| 19 | `CZ.CDS.USR.FIELD.NAME` | `CzCdpDataDefinition_UsrFieldName` |  |  |  |
| 20 | `CZ.CDS.USR.FIELD.ATTRIBUTES` | `CzCdpDataDefinition_UsrFieldAttributes` |  |  |  |
| 21 | `CZ.CDS.USR.PURPOSE` | `CzCdpDataDefinition_UsrPurpose` |  |  |  |
| 22 | `CZ.CDS.USR.ERASE.OPTION` | `CzCdpDataDefinition_UsrEraseOption` |  |  |  |
| 23 | `CZ.CDS.USR.ACCESSIBILITY` | `CzCdpDataDefinition_UsrAccessibility` |  |  |  |
| 24 | `CZ.CDS.USR.EXCLUDE` | `CzCdpDataDefinition_UsrExclude` |  |  |  |
| 25 | `CZ.CDS.USR.PARTY.IDENTIFIER` | `CzCdpDataDefinition_UsrPartyIdentifier` |  |  |  |
| 26 | `CZ.CDS.USR.PARTY.POS.API` | `CzCdpDataDefinition_UsrPartyPosApi` |  |  |  |
| 27 | `CZ.CDS.USR.RESERVED.08` | `CzCdpDataDefinition_UsrReserved08` |  |  |  |
| 28 | `CZ.CDS.USR.RESERVED.07` | `CzCdpDataDefinition_UsrReserved07` |  |  |  |
| 29 | `CZ.CDS.USR.RESERVED.06` | `CzCdpDataDefinition_UsrReserved06` |  |  |  |
| 30 | `CZ.CDS.USR.RESERVED.05` | `CzCdpDataDefinition_UsrReserved05` |  |  |  |
| 31 | `CZ.CDS.USR.RESERVED.04` | `CzCdpDataDefinition_UsrReserved04` |  |  |  |
| 32 | `CZ.CDS.USR.RESERVED.03` | `CzCdpDataDefinition_UsrReserved03` |  |  |  |
| 33 | `CZ.CDS.USR.RESERVED.02` | `CzCdpDataDefinition_UsrReserved02` |  |  |  |
| 34 | `CZ.CDS.USR.RESERVED.01` | `CzCdpDataDefinition_UsrReserved01` |  |  |  |
| 35 | `CZ.CDS.USE.IN.ACTIVITY` | `CzCdpDataDefinition_UseInActivity` | TField |  | The functionality is moved to ST.CUSTOMER.ACTIVITY.PARAMETER in higher releases and hence not in use anymore |
| 36 | `CZ.CDS.CUST.ACCESS.TYPE` | `CzCdpDataDefinition_CustAccessType` | TField |  | The functionality is moved to ST.CUSTOMER.ACTIVITY.PARAMETER in higher releases and hence not in use anymore |
| 37 | `CZ.CDS.CUST.ACCESS.LINK` | `CzCdpDataDefinition_CustAccessLink` | TField |  | The functionality is moved to ST.CUSTOMER.ACTIVITY.PARAMETER in higher releases and hence not in use anymore |
| 38 | `CZ.CDS.PARTY.APPLICATION` | `CzCdpDataDefinition_PartyApplication` | TField | Yes | Defines the party application to which the application being configured for customer activity processing belongs. The field is defaulted with a value of CUSTOMER. In higher releases where Customer activity and CDP processing functionality enhanced for PERSON.ENTITY as well, the field is allowed input with options CUSTOMER or PERSON.ENTITY or TRANSACTION. It is mandatory that for a proper processing, user must ensure that this field is set with the appropriate party application relevant to the application being configured If this field is not mentioned then this application's PARTY.APPLICATION is considered as CUSTOMER during the CDP processing TRANSACTION option is used to allow the user to configure the application eligible for transaction erasure. This field will be disabled, Once the party application is changed as TRANSACTION. |
| 39 | `CZ.CDS.PARTY.ACCESS.TYPE` | `CzCdpDataDefinition_PartyAccessType` | TField |  | The functionality is moved to ST.CUSTOMER.ACTIVITY.PARAMETER in higher releases and hence not in use anymore |
| 40 | `CZ.CDS.PARTY.ACCESS.LINK` | `CzCdpDataDefinition_PartyAccessLink` | TField |  | The functionality is moved to ST.CUSTOMER.ACTIVITY.PARAMETER in higher releases and hence not in use anymore |
| 41 | `CZ.CDS.FEA.FIELD.NAME` | `CzCdpDataDefinition_FeaFieldName` |  |  |  |
| 42 | `CZ.CDS.FEA.PRODUCT` | `CzCdpDataDefinition_FeaProduct` |  |  |  |
| 43 | `CZ.CDS.FEA.FIELD.ATTRIBUTES` | `CzCdpDataDefinition_FeaFieldAttributes` |  |  |  |
| 44 | `CZ.CDS.FEA.PURPOSE` | `CzCdpDataDefinition_FeaPurpose` |  |  |  |
| 45 | `CZ.CDS.FEA.ERASE.OPTION` | `CzCdpDataDefinition_FeaEraseOption` |  |  |  |
| 46 | `CZ.CDS.FEA.ACCESSIBILITY` | `CzCdpDataDefinition_FeaAccessibility` |  |  |  |
| 47 | `CZ.CDS.FEA.PARTY.IDENTIFIER` | `CzCdpDataDefinition_FeaPartyIdentifier` |  |  |  |
| 48 | `CZ.CDS.FEA.PARTY.POS.API` | `CzCdpDataDefinition_FeaPartyPosApi` |  |  |  |
| 49 | `CZ.CDS.FEA.RESERVED.03` | `CzCdpDataDefinition_FeaReserved03` |  |  |  |
| 50 | `CZ.CDS.FEA.RESERVED.02` | `CzCdpDataDefinition_FeaReserved02` |  |  |  |
| 51 | `CZ.CDS.FEA.RESERVED.01` | `CzCdpDataDefinition_FeaReserved01` |  |  |  |
| 52 | `CZ.CDS.MASTER.APPLICATION` | `CzCdpDataDefinition_MasterApplication` | TField |  | The field denotes whether the application is a master application or a sub-table.For contract wise erasure, the system erases contracts along with sub-tables if configured.If a master application is mentioned in this field, then when a contract erasure requestis made for the master application,the sub-table also gets erased. Validation rules: The field is not allowed input for ECB applications as all the ECB applications are considered as master applications by themselves. The field is allowed input only if ALLOW.CONTRACT.ERASURE is set as YES in CZ.CDP.PARAMETER. Allowed value is a valid T24 application. |
| 53 | `CZ.CDS.MASTER.LINK.TYPE` | `CzCdpDataDefinition_MasterLinkType` | TField | Yes | The field denotes the link between the sub-table and the master application. With this link when the master application contract is erased,the sub-table contracts are also selected for erasure. Validation rules: The field is mandatory if a master application is mentioned. Allowed values are ID_CONCAT_FIELD_API. ID - If the master application ID and the sub-table ID are the same. CONCAT - If the sub-table records are availble in a CONCAT file keyed in by the master application record ID.Concat table name to be mentioned in MASTER.LINK.METHOD FIELD - If there is a field in the sub table that has the master application record ID. Field to be mentioned in MASTER.LINK.METHOD API - For any other cases. The API name to be mentioned in MASTER.LINK.METHOD and needs to be a valid EB.API record. |
| 54 | `CZ.CDS.MASTER.LINK.METHOD` | `CzCdpDataDefinition_MasterLinkMethod` | TField | Yes | The field contains the method through which the sub-table is linked to the master application. Validation rules: Input is mandatory if MASTER.LINK.TYPE is mentioned as CONCAT or FIELD or API. CONCAT - A valid T24 table name FIELD - A valid field from the sub-table application API - A valid EB.API record |
| 55 | `CZ.CDS.RESERVED.06` | `CzCdpDataDefinition_Reserved06` | TField |  |  |
| 56 | `CZ.CDS.RESERVED.05` | `CzCdpDataDefinition_Reserved05` | TField |  |  |
| 57 | `CZ.CDS.RESERVED.04` | `CzCdpDataDefinition_Reserved04` | TField |  |  |
| 58 | `CZ.CDS.RESERVED.03` | `CzCdpDataDefinition_Reserved03` | TField |  |  |
| 59 | `CZ.CDS.RESERVED.02` | `CzCdpDataDefinition_Reserved02` | TField |  |  |
| 60 | `CZ.CDS.LOCAL.REF` | `CzCdpDataDefinition_LocalRef` |  |  |  |
| 61 | `CZ.CDS.OVERRIDE` | `CzCdpDataDefinition_Override` |  |  |  |
| 62 | `CZ.CDS.RECORD.STATUS` | `CzCdpDataDefinition_RecordStatus` | String |  |  |
| 63 | `CZ.CDS.CURR.NO` | `CzCdpDataDefinition_CurrNo` | String |  |  |
| 64 | `CZ.CDS.INPUTTER` | `CzCdpDataDefinition_Inputter` |  |  |  |
| 65 | `CZ.CDS.DATE.TIME` | `CzCdpDataDefinition_DateTime` |  |  |  |
| 66 | `CZ.CDS.AUTHORISER` | `CzCdpDataDefinition_Authoriser` | String |  |  |
| 67 | `CZ.CDS.CO.CODE` | `CzCdpDataDefinition_CoCode` | String |  |  |
| 68 | `CZ.CDS.DEPT.CODE` | `CzCdpDataDefinition_DeptCode` | String |  |  |
| 69 | `CZ.CDS.AUDITOR.CODE` | `CzCdpDataDefinition_AuditorCode` | String |  |  |
| 70 | `CZ.CDS.AUDIT.DATE.TIME` | `CzCdpDataDefinition_AuditDateTime` | String |  |  |
| 71 | `CZ.CDS.INCL.FOR.PROSPECT` | `CzCdpDataDefinition_InclForProspect` | TField |  | Within each CZ.CDP.DATA.DEFINITION record, this field will define whether the application is to be considered for prospect data erasure processing or not. Validation Rule: Allowed input - YES or NULL(BLANK) YES � meaning the application is applicable for Prospect related erasure processing NULL � meaning the application is not applicable for Prospect related erasure processing |
