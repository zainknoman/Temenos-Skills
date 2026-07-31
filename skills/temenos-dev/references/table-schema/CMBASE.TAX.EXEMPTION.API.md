# CMBASE.TAX.EXEMPTION.API — Table Schema

> Source: `INSERTS/I_F.CMBASE.TAX.EXEMPTION.API` in `CMBASE_TaxCalculation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TAX.EXEMPT.API.ID.ROUTINE` | `CmbaseTaxExemptionApi_IdRoutine` | TField |  | Routine to validate the record id. |
| 2 | `TAX.EXEMPT.API.RECORD.ROUTINE` | `CmbaseTaxExemptionApi_RecordRoutine` | TField |  | Template record routine. |
| 3 | `TAX.EXEMPT.API.VALIDATE.ROUTINE` | `CmbaseTaxExemptionApi_ValidateRoutine` | TField |  | Routine that contains the field validation logic. |
| 4 | `TAX.EXEMPT.API.AUTHORISE.ROUTINE` | `CmbaseTaxExemptionApi_AuthoriseRoutine` | TField |  | Routine that contains the logic for authorization. |
| 5 | `TAX.EXEMPT.API.RESERVED.15` | `CmbaseTaxExemptionApi_Reserved15` | TField |  | Reserved for future use. |
| 6 | `TAX.EXEMPT.API.RESERVED.14` | `CmbaseTaxExemptionApi_Reserved14` | TField |  | Reserved for future use. |
| 7 | `TAX.EXEMPT.API.RESERVED.13` | `CmbaseTaxExemptionApi_Reserved13` | TField |  | Reserved for future use. |
| 8 | `TAX.EXEMPT.API.RESERVED.12` | `CmbaseTaxExemptionApi_Reserved12` | TField |  | Reserved for future use. |
| 9 | `TAX.EXEMPT.API.RESERVED.11` | `CmbaseTaxExemptionApi_Reserved11` | TField |  | Reserved for future use. |
| 10 | `TAX.EXEMPT.API.RESERVED.10` | `CmbaseTaxExemptionApi_Reserved10` | TField |  | Reserved for future use. |
| 11 | `TAX.EXEMPT.API.RESERVED.9` | `CmbaseTaxExemptionApi_Reserved9` | TField |  | Reserved for future use. |
| 12 | `TAX.EXEMPT.API.RESERVED.8` | `CmbaseTaxExemptionApi_Reserved8` | TField |  | Reserved for future use. |
| 13 | `TAX.EXEMPT.API.RESERVED.7` | `CmbaseTaxExemptionApi_Reserved7` | TField |  | Reserved for future use. |
| 14 | `TAX.EXEMPT.API.RESERVED.6` | `CmbaseTaxExemptionApi_Reserved6` | TField |  | Reserved for future use. |
| 15 | `TAX.EXEMPT.API.RESERVED.5` | `CmbaseTaxExemptionApi_Reserved5` | TField |  | Reserved for future use. |
| 16 | `TAX.EXEMPT.API.RESERVED.4` | `CmbaseTaxExemptionApi_Reserved4` | TField |  | Reserved for future use. |
| 17 | `TAX.EXEMPT.API.RESERVED.3` | `CmbaseTaxExemptionApi_Reserved3` | TField |  | Reserved for future use. |
| 18 | `TAX.EXEMPT.API.RESERVED.2` | `CmbaseTaxExemptionApi_Reserved2` | TField |  | Reserved for future use. |
| 19 | `TAX.EXEMPT.API.RESERVED.1` | `CmbaseTaxExemptionApi_Reserved1` | TField |  | Reserved for future use. |
| 20 | `TAX.EXEMPT.API.LOCAL.REF` | `CmbaseTaxExemptionApi_LocalRef` |  |  |  |
| 21 | `TAX.EXEMPT.API.OVERRIDE` | `CmbaseTaxExemptionApi_Override` |  |  |  |
| 22 | `TAX.EXEMPT.API.RECORD.STATUS` | `CmbaseTaxExemptionApi_RecordStatus` | String |  |  |
| 23 | `TAX.EXEMPT.API.CURR.NO` | `CmbaseTaxExemptionApi_CurrNo` | String |  |  |
| 24 | `TAX.EXEMPT.API.INPUTTER` | `CmbaseTaxExemptionApi_Inputter` |  |  |  |
| 25 | `TAX.EXEMPT.API.DATE.TIME` | `CmbaseTaxExemptionApi_DateTime` |  |  |  |
| 26 | `TAX.EXEMPT.API.AUTHORISER` | `CmbaseTaxExemptionApi_Authoriser` | String |  |  |
| 27 | `TAX.EXEMPT.API.CO.CODE` | `CmbaseTaxExemptionApi_CoCode` | String |  |  |
| 28 | `TAX.EXEMPT.API.DEPT.CODE` | `CmbaseTaxExemptionApi_DeptCode` | String |  |  |
| 29 | `TAX.EXEMPT.API.AUDITOR.CODE` | `CmbaseTaxExemptionApi_AuditorCode` | String |  |  |
| 30 | `TAX.EXEMPT.API.AUDIT.DATE.TIME` | `CmbaseTaxExemptionApi_AuditDateTime` | String |  |  |
