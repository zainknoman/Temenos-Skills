# CMBASE.TAX.NAMED.ACTIVITY.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CMBASE.TAX.NAMED.ACTIVITY.PARAMETER` in `CMBASE_TaxCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACTIVITY.PARAM.BANK.NAMED.ACTIVITY` | `CmbaseTaxNamedActivityParameter_BankNamedActivity` |  |  |  |
| 2 | `ACTIVITY.PARAM.STANDARD.ACTIVITY` | `CmbaseTaxNamedActivityParameter_StandardActivity` |  |  |  |
| 3 | `ACTIVITY.PARAM.RESERVED.15` | `CmbaseTaxNamedActivityParameter_Reserved15` | TField |  | Field reserved for future use. |
| 4 | `ACTIVITY.PARAM.RESERVED.14` | `CmbaseTaxNamedActivityParameter_Reserved14` | TField |  | Field reserved for future use. |
| 5 | `ACTIVITY.PARAM.RESERVED.13` | `CmbaseTaxNamedActivityParameter_Reserved13` | TField |  | Field reserved for future use. |
| 6 | `ACTIVITY.PARAM.RESERVED.12` | `CmbaseTaxNamedActivityParameter_Reserved12` | TField |  | Field reserved for future use. |
| 7 | `ACTIVITY.PARAM.RESERVED.11` | `CmbaseTaxNamedActivityParameter_Reserved11` | TField |  | Field reserved for future use. |
| 8 | `ACTIVITY.PARAM.RESERVED.10` | `CmbaseTaxNamedActivityParameter_Reserved10` | TField |  | Field reserved for future use. |
| 9 | `ACTIVITY.PARAM.RESERVED.9` | `CmbaseTaxNamedActivityParameter_Reserved9` | TField |  | Field reserved for future use. |
| 10 | `ACTIVITY.PARAM.RESERVED.8` | `CmbaseTaxNamedActivityParameter_Reserved8` | TField |  | Field reserved for future use. |
| 11 | `ACTIVITY.PARAM.RESERVED.7` | `CmbaseTaxNamedActivityParameter_Reserved7` | TField |  | Field reserved for future use. |
| 12 | `ACTIVITY.PARAM.RESERVED.6` | `CmbaseTaxNamedActivityParameter_Reserved6` | TField |  | Field reserved for future use. |
| 13 | `ACTIVITY.PARAM.RESERVED.5` | `CmbaseTaxNamedActivityParameter_Reserved5` | TField |  | Field reserved for future use. |
| 14 | `ACTIVITY.PARAM.RESERVED.4` | `CmbaseTaxNamedActivityParameter_Reserved4` | TField |  | Field reserved for future use. |
| 15 | `ACTIVITY.PARAM.RESERVED.3` | `CmbaseTaxNamedActivityParameter_Reserved3` | TField |  | Field reserved for future use. |
| 16 | `ACTIVITY.PARAM.RESERVED.2` | `CmbaseTaxNamedActivityParameter_Reserved2` | TField |  | Field reserved for future use. |
| 17 | `ACTIVITY.PARAM.RESERVED.1` | `CmbaseTaxNamedActivityParameter_Reserved1` | TField |  | Field reserved for future use. |
| 18 | `ACTIVITY.PARAM.LOCAL.REF` | `CmbaseTaxNamedActivityParameter_LocalRef` |  |  |  |
| 19 | `ACTIVITY.PARAM.OVERRIDE` | `CmbaseTaxNamedActivityParameter_Override` |  |  |  |
| 20 | `ACTIVITY.PARAM.RECORD.STATUS` | `CmbaseTaxNamedActivityParameter_RecordStatus` | String |  |  |
| 21 | `ACTIVITY.PARAM.CURR.NO` | `CmbaseTaxNamedActivityParameter_CurrNo` | String |  |  |
| 22 | `ACTIVITY.PARAM.INPUTTER` | `CmbaseTaxNamedActivityParameter_Inputter` |  |  |  |
| 23 | `ACTIVITY.PARAM.DATE.TIME` | `CmbaseTaxNamedActivityParameter_DateTime` |  |  |  |
| 24 | `ACTIVITY.PARAM.AUTHORISER` | `CmbaseTaxNamedActivityParameter_Authoriser` | String |  |  |
| 25 | `ACTIVITY.PARAM.CO.CODE` | `CmbaseTaxNamedActivityParameter_CoCode` | String |  |  |
| 26 | `ACTIVITY.PARAM.DEPT.CODE` | `CmbaseTaxNamedActivityParameter_DeptCode` | String |  |  |
| 27 | `ACTIVITY.PARAM.AUDITOR.CODE` | `CmbaseTaxNamedActivityParameter_AuditorCode` | String |  |  |
| 28 | `ACTIVITY.PARAM.AUDIT.DATE.TIME` | `CmbaseTaxNamedActivityParameter_AuditDateTime` | String |  |  |
