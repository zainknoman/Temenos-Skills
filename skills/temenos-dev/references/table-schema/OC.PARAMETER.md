# OC.PARAMETER — Table Schema

> Source: `INSERTS/I_F.OC.PARAMETER` in `OC_Parameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OC.PARAM.BANK.LEI` | `OcParameter_BankLei` | TField | Yes | Legal Entity Identifier of the T24 bank. LEI will be used for precise, reliable, and unique identification of each party in a derivative trade. Validation Rules : Mandatory field. Upto 40 alphanumeric characters can be allowed. |
| 2 | `OC.PARAM.REGULATOR` | `OcParameter_Regulator` | TField | Yes | Regulator Name /ID, whose regulations, T24 bank has to comply with. For example, ESMA, CFTC, HKMA etc., This is a key field in OC.PARAMETER. Mandatory field. Validation Rules: Should be a valid OC.REGULATOR ID. |
| 3 | `OC.PARAM.USI.NAME.SPACE` | `OcParameter_UsiNameSpace` | TField | No | Denotes the name space given by CFTC or any other regulator as applicable to T24 bank. Part of Unique Transaction Identifier (UTI) where ever T24 bank is generating the UTI. Optional field. Validation Rules: 20 character alphanumeric. |
| 4 | `OC.PARAM.NAT.COMP.AUTHORITY` | `OcParameter_NatCompAuthority` | TField |  | National Competent Authority. Denotes local country regulator ID as applicable to EU countries. Validation Rules: Should be a valid OC.REGULATOR ID. |
| 5 | `OC.PARAM.NOVATION.TYPE` | `OcParameter_NovationType` | TField | No | This field indicates how the system should handle novation for cleared trades and will be used as and when Novation functionality is introduced. Optional. Validation Rules: Valid values are manual, auto and none. |
| 6 | `OC.PARAM.CLIENT.COLL.SEGRE` | `OcParameter_ClientCollSegre` | TField | No | Client Collateral segregation. This field indicates how the client collateral will be handled ,i.e. is it reported along with bank collateral or separately. Applicable only when Collateral management functionality is built/used. Optional. Reserved for future use. Validation Rules: Valid values are Yes and None. |
| 7 | `OC.PARAM.COLATERAL.REPORTED` | `OcParameter_ColateralReported` | TField | No | This field indicates how the MTM value of collateral to be reported to Trade Repository. No workflows are envisaged based on the value in this field. Mainly for reporting requirement. Optional Field. Validation Rules: Valid values are per transaction and per portfolio. |
| 8 | `OC.PARAM.THIRD.PARTY.REPORTING` | `OcParameter_ThirdPartyReporting` | TField | No | This field indicates whether the bank has delegated the reporting to a 3rd Party. Optional Field. Validation Rules: Valid values are yes and None. |
| 9 | `OC.PARAM.REGULATORY.CLASS` | `OcParameter_RegulatoryClass` | TField |  |  |
| 10 | `OC.PARAM.DEF.TRADE.REPOSITORY` | `OcParameter_DefTradeRepository` | TField |  |  |
| 11 | `OC.PARAM.UTI.USI.API` | `OcParameter_UtiUsiApi` | TField | No | This field holds the UTI/USI generation routine/logic. The logic to generate the UTI/USI can be tailored to suit the User�s requirements. Optional Field. Validation Rules: Input should have a valid entry in PGM.FILE. |
| 12 | `OC.PARAM.CORPORATE.SECTOR` | `OcParameter_CorporateSector` |  |  |  |
| 13 | `OC.PARAM.REPORTING.ENTITY` | `OcParameter_ReportingEntity` | TField |  |  |
| 14 | `OC.PARAM.RESERVED.8` | `OcParameter_Reserved8` | TField |  |  |
| 15 | `OC.PARAM.RESERVED.7` | `OcParameter_Reserved7` | TField |  |  |
| 16 | `OC.PARAM.RESERVED.6` | `OcParameter_Reserved6` | TField |  |  |
| 17 | `OC.PARAM.RESERVED.5` | `OcParameter_Reserved5` | TField |  |  |
| 18 | `OC.PARAM.RESERVED.4` | `OcParameter_Reserved4` | TField |  |  |
| 19 | `OC.PARAM.RESERVED.3` | `OcParameter_Reserved3` | TField |  |  |
| 20 | `OC.PARAM.RESERVED.2` | `OcParameter_Reserved2` | TField |  |  |
| 21 | `OC.PARAM.RESERVED.1` | `OcParameter_Reserved1` | TField |  |  |
| 22 | `OC.PARAM.LOCAL.REF` | `OcParameter_LocalRef` |  |  |  |
| 23 | `OC.PARAM.RECORD.STATUS` | `OcParameter_RecordStatus` | String |  |  |
| 24 | `OC.PARAM.CURR.NO` | `OcParameter_CurrNo` | String |  |  |
| 25 | `OC.PARAM.INPUTTER` | `OcParameter_Inputter` |  |  |  |
| 26 | `OC.PARAM.DATE.TIME` | `OcParameter_DateTime` |  |  |  |
| 27 | `OC.PARAM.AUTHORISER` | `OcParameter_Authoriser` | String |  |  |
| 28 | `OC.PARAM.CO.CODE` | `OcParameter_CoCode` | String |  |  |
| 29 | `OC.PARAM.DEPT.CODE` | `OcParameter_DeptCode` | String |  |  |
| 30 | `OC.PARAM.AUDITOR.CODE` | `OcParameter_AuditorCode` | String |  |  |
| 31 | `OC.PARAM.AUDIT.DATE.TIME` | `OcParameter_AuditDateTime` | String |  |  |
