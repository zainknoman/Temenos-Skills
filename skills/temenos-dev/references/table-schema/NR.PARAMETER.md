# NR.PARAMETER — Table Schema

> Source: `INSERTS/I_F.NR.PARAMETER` in `NR_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NR.PARAM.TRANS.TYPE` | `NrParameter_TransType` |  |  |  |
| 2 | `NR.PARAM.MATCH.FLD.STMT` | `NrParameter_MatchFldStmt` |  |  |  |
| 3 | `NR.PARAM.MATCH.FLD.LEDGER` | `NrParameter_MatchFldLedger` |  |  |  |
| 4 | `NR.PARAM.SPLIT.ITEMS` | `NrParameter_SplitItems` | TField |  | This field allows the user to determine whether item 'splits' are allowed in the manual matching process. Item splits are never allowed in the automatching process. Validation Rules: Allowed input 'Y' or blank |
| 5 | `NR.PARAM.RETENTION.DAYS` | `NrParameter_RetentionDays` | TField |  | This field determines how long (in days) matched items remain on the live items file before being transferred to the history file. Validation Rules: 3 character numeric field Indicates number of days |
| 6 | `NR.PARAM.T24.LOCATION` | `NrParameter_T24Location` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 7 | `NR.PARAM.RESERVED11` | `NrParameter_Reserved11` | TField |  |  |
| 8 | `NR.PARAM.T24.TYPE` | `NrParameter_T24Type` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 9 | `NR.PARAM.EXTERNAL.LOCATION` | `NrParameter_ExternalLocation` | TField |  | This field contains the location (ie. file name) that incoming statements will be routed to when generated. Validation Rules: 20 character alphanumeric field name |
| 10 | `NR.PARAM.RESERVED12` | `NrParameter_Reserved12` | TField |  |  |
| 11 | `NR.PARAM.EXTERNAL.TYPE` | `NrParameter_ExternalType` | TField |  | This field contains the type of record that will be generated for the External.Location file. This may be either DIVERT or MESSAGE Validation Rules: 7 character alphanumeric field Acceptable Input - DIVERT and MESSAGE |
| 12 | `NR.PARAM.RESERVED10` | `NrParameter_Reserved10` | TField |  | Reserved for future use Validation Rules: No Input allowed |
| 13 | `NR.PARAM.RESERVED9` | `NrParameter_Reserved9` | TField |  | Reserved for future use Validation Rules: No Input allowed |
| 14 | `NR.PARAM.RESERVED8` | `NrParameter_Reserved8` | TField |  | Reserved for future use Validation Rules: No Input allowed |
| 15 | `NR.PARAM.RESERVED7` | `NrParameter_Reserved7` | TField |  | Reserved for future use Validation Rules: No Input allowed |
| 16 | `NR.PARAM.RESERVED6` | `NrParameter_Reserved6` | TField |  | Reserved for future use Validation Rules: No Input allowed |
| 17 | `NR.PARAM.RESERVED5` | `NrParameter_Reserved5` | TField |  | Reserved for future use Validation Rules: No Input allowed |
| 18 | `NR.PARAM.RESERVED4` | `NrParameter_Reserved4` | TField |  | Reserved for future use Validation Rules: No Input allowed |
| 19 | `NR.PARAM.RESERVED3` | `NrParameter_Reserved3` | TField |  | Reserved for future use Validation Rules: No Input allowed |
| 20 | `NR.PARAM.RESERVED2` | `NrParameter_Reserved2` | TField |  | Reserved for future use Validation Rules: No Input allowed |
| 21 | `NR.PARAM.RESERVED1` | `NrParameter_Reserved1` | TField |  | Reserved for future use Validation Rules: No Input allowed |
| 22 | `NR.PARAM.LOCAL.REF` | `NrParameter_LocalRef` |  |  |  |
| 23 | `NR.PARAM.OVERRIDE` | `NrParameter_Override` |  |  |  |
| 24 | `NR.PARAM.RECORD.STATUS` | `NrParameter_RecordStatus` | String |  |  |
| 25 | `NR.PARAM.CURR.NO` | `NrParameter_CurrNo` | String |  |  |
| 26 | `NR.PARAM.INPUTTER` | `NrParameter_Inputter` |  |  |  |
| 27 | `NR.PARAM.DATE.TIME` | `NrParameter_DateTime` |  |  |  |
| 28 | `NR.PARAM.AUTHORISER` | `NrParameter_Authoriser` | String |  |  |
| 29 | `NR.PARAM.CO.CODE` | `NrParameter_CoCode` | String |  |  |
| 30 | `NR.PARAM.DEPT.CODE` | `NrParameter_DeptCode` | String |  |  |
| 31 | `NR.PARAM.AUDITOR.CODE` | `NrParameter_AuditorCode` | String |  |  |
| 32 | `NR.PARAM.AUDIT.DATE.TIME` | `NrParameter_AuditDateTime` | String |  |  |
