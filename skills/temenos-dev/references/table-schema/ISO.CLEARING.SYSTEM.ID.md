# ISO.CLEARING.SYSTEM.ID — Table Schema

> Source: `INSERTS/I_F.ISO.CLEARING.SYSTEM.ID` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.ISO.DESCRIPTION` | `IsoClearingSystemId_Description` | TField |  | Description of the national clearing system |
| 2 | `DE.ISO.SWIFT.PREFIX` | `IsoClearingSystemId_SwiftPrefix` | TField |  | This will hold the value of national system clearing code to be used as per swift standards |
| 3 | `DE.ISO.COUNTRY` | `IsoClearingSystemId_Country` | TField |  | Contains the Country of the clearing code Validation Rules: Must be a valid entry from COUNTRY table |
| 4 | `DE.ISO.NATIONAL.ID.FORMAT` | `IsoClearingSystemId_IsoNationalIdFormat` |  |  |  |
| 5 | `DE.ISO.RESERVED.09` | `IsoClearingSystemId_Reserved09` | TField |  |  |
| 6 | `DE.ISO.RESERVED.08` | `IsoClearingSystemId_Reserved08` | TField |  |  |
| 7 | `DE.ISO.RESERVED.07` | `IsoClearingSystemId_Reserved07` | TField |  |  |
| 8 | `DE.ISO.RESERVED.06` | `IsoClearingSystemId_Reserved06` | TField |  |  |
| 9 | `DE.ISO.RESERVED.05` | `IsoClearingSystemId_Reserved05` | TField |  |  |
| 10 | `DE.ISO.RESERVED.04` | `IsoClearingSystemId_Reserved04` | TField |  |  |
| 11 | `DE.ISO.RESERVED.03` | `IsoClearingSystemId_Reserved03` | TField |  |  |
| 12 | `DE.ISO.RESERVED.02` | `IsoClearingSystemId_Reserved02` | TField |  |  |
| 13 | `DE.ISO.RESERVED.01` | `IsoClearingSystemId_Reserved01` | TField |  |  |
| 14 | `DE.ISO.LOCAL.REF` | `IsoClearingSystemId_LocalRef` |  |  |  |
| 15 | `DE.ISO.OVERRIDE` | `IsoClearingSystemId_Override` |  |  |  |
| 16 | `DE.ISO.RECORD.STATUS` | `IsoClearingSystemId_RecordStatus` | String |  |  |
| 17 | `DE.ISO.CURR.NO` | `IsoClearingSystemId_CurrNo` | String |  |  |
| 18 | `DE.ISO.INPUTTER` | `IsoClearingSystemId_Inputter` |  |  |  |
| 19 | `DE.ISO.DATE.TIME` | `IsoClearingSystemId_DateTime` |  |  |  |
| 20 | `DE.ISO.AUTHORISER` | `IsoClearingSystemId_Authoriser` | String |  |  |
| 21 | `DE.ISO.CO.CODE` | `IsoClearingSystemId_CoCode` | String |  |  |
| 22 | `DE.ISO.DEPT.CODE` | `IsoClearingSystemId_DeptCode` | String |  |  |
| 23 | `DE.ISO.AUDITOR.CODE` | `IsoClearingSystemId_AuditorCode` | String |  |  |
| 24 | `DE.ISO.AUDIT.DATE.TIME` | `IsoClearingSystemId_AuditDateTime` | String |  |  |
