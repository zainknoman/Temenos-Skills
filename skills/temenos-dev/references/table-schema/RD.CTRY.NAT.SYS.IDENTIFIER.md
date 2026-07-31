# RD.CTRY.NAT.SYS.IDENTIFIER — Table Schema

> Source: `INSERTS/I_F.RD.CTRY.NAT.SYS.IDENTIFIER` in `RD_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RD.CNSI.COUNTRY.CODE` | `RdCtryNatSysIdentifier_CountryCode` | TField |  | The country code to which the national identifier belongs Validation Rules: The value for this field should be a valid record in COUNTRY application. Defaulted from country code component of ID. |
| 2 | `RD.CNSI.ISO.CLEARING.SYS.ID` | `RdCtryNatSysIdentifier_IsoClearingSysId` | TField |  | The ISO identifier of the Clearing System Id Validation Rules: This value will be selected from a list (EB.LOOKUP>ISO.CLEARING.SYS.ID). |
| 3 | `RD.CNSI.SWIFT.CLR.SYS.ID` | `RdCtryNatSysIdentifier_SwiftClrSysId` | TField |  | The clearing prefix used in SWIFT message Validation Rules: This value will be selected from a list (EB.LOOKUP>SWIFT.CLR.SYS.ID). |
| 4 | `RD.CNSI.CLR.SYS.ACRYNM` | `RdCtryNatSysIdentifier_ClrSysAcrynm` | TField |  | The National Id Type indicated in Bank Directory Plus Validation Rules: This value will be selected from a list (EB.LOOKUP>SWIFT.CLR.SYS.ID). |
| 5 | `RD.CNSI.NATIONAL.ID.FORMAT` | `RdCtryNatSysIdentifier_NationalIdFormat` | TField |  | The format of national id Validation Rules: The value for this field can be of free text with the maximum length of 35. |
| 6 | `RD.CNSI.NATIONAL.ID.TYPE` | `RdCtryNatSysIdentifier_NationalIdType` | TField |  | The format of national id type as per bank directory. Validation Rules: The value for this field can be of free text with the maximum length of 35. |
| 7 | `RD.CNSI.RESERVED.4` | `RdCtryNatSysIdentifier_Reserved4` | TField |  |  |
| 8 | `RD.CNSI.RESERVED.3` | `RdCtryNatSysIdentifier_Reserved3` | TField |  |  |
| 9 | `RD.CNSI.RESERVED.2` | `RdCtryNatSysIdentifier_Reserved2` | TField |  |  |
| 10 | `RD.CNSI.RESERVED.1` | `RdCtryNatSysIdentifier_Reserved1` | TField |  |  |
| 11 | `RD.CNSI.LOCAL.REF` | `RdCtryNatSysIdentifier_LocalRef` |  |  |  |
| 12 | `RD.CNSI.OVERRIDE` | `RdCtryNatSysIdentifier_Override` |  |  |  |
| 13 | `RD.CNSI.RECORD.STATUS` | `RdCtryNatSysIdentifier_RecordStatus` | String |  |  |
| 14 | `RD.CNSI.CURR.NO` | `RdCtryNatSysIdentifier_CurrNo` | String |  |  |
| 15 | `RD.CNSI.INPUTTER` | `RdCtryNatSysIdentifier_Inputter` |  |  |  |
| 16 | `RD.CNSI.DATE.TIME` | `RdCtryNatSysIdentifier_DateTime` |  |  |  |
| 17 | `RD.CNSI.AUTHORISER` | `RdCtryNatSysIdentifier_Authoriser` | String |  |  |
| 18 | `RD.CNSI.CO.CODE` | `RdCtryNatSysIdentifier_CoCode` | String |  |  |
| 19 | `RD.CNSI.DEPT.CODE` | `RdCtryNatSysIdentifier_DeptCode` | String |  |  |
| 20 | `RD.CNSI.AUDITOR.CODE` | `RdCtryNatSysIdentifier_AuditorCode` | String |  |  |
| 21 | `RD.CNSI.AUDIT.DATE.TIME` | `RdCtryNatSysIdentifier_AuditDateTime` | String |  |  |
