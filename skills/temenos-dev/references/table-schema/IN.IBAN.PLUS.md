# IN.IBAN.PLUS — Table Schema

> Source: `INSERTS/I_F.IN.IBAN.PLUS` in `IN_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IN.PL.MODIFICATION.FLAG` | `InIbanPlus_ModificationFlag` | TField |  | A flag which indicates whether there is a change in the record, since the last release of the IBAN structure file. Validation Rules: A - Addition since last IBAN structure file. D - Deletion since last IBAN structure file. U - Unchanged since last IBAN structure file. M - Modification since last IBAN structure file. E - Expired : Reserved for future use. |
| 2 | `IN.PL.RECORD.KEY` | `InIbanPlus_RecordKey` | TField |  |  |
| 3 | `IN.PL.INSTITUTION.NAME` | `InIbanPlus_InstitutionName` |  |  |  |
| 4 | `IN.PL.COUNTRY.NAME` | `InIbanPlus_CountryName` | TField |  | Residence Country Name of the financial institution that issued the IBAN. Validation Rules: A maximum of 35 characters can be entered. |
| 5 | `IN.PL.ISO.COUNTRY.CODE` | `InIbanPlus_IsoCountryCode` | TField |  | Residence Country code of the financial institution that issued the IBAN. Validation Rules: A maximum of 2 characters can be entered. |
| 6 | `IN.PL.IBAN.COUNTRY.CODE` | `InIbanPlus_IbanCountryCode` | TField |  | The country code of the IBANs that the institution issued. Under certain circumstances this can be different from the country indicated in field "ISO COUNTRY CODE". Example Banks in Guernsey (GG) issue IBANs using GB when the clearing system in Great Britain is used. Validation Rules: A maximum of 2 characters can be entered. |
| 7 | `IN.PL.IBAN.BIC` | `InIbanPlus_IbanBic` | TField |  | This is the BIC Code issued together with the IBANs to the institution's clients. Validation Rules: A maximum of 11 characters can be entered. |
| 8 | `IN.PL.ROUTING.BIC` | `InIbanPlus_RoutingBic` | TField |  | Contains the ROUTING BIC which is the best approximation to send SEPA payment over SWIFT, when IBAN BIC is not connected to SWIFT. Validation Rules: A maximum of 11 characters can be entered. |
| 9 | `IN.PL.IBAN.NATIONAL.ID` | `InIbanPlus_IbanNationalId` | TField |  | Specifies the National ID that is included in the IBAN. Validation Rules: A maximum of 15 characters can be entered. |
| 10 | `IN.PL.SERVICE.CONTEXT` | `InIbanPlus_ServiceContext` | TField |  | Code indicating the context of the payment services provided by the financial institution. SEPA - Single Euro Payments Area NULL - The institution uses the IBAN standard but is not a participant of SEPA. Validation Rules: A maximum of 4 characters can be entered. |
| 11 | `IN.PL.FIELD.A` | `InIbanPlus_FieldA` | TField |  |  |
| 12 | `IN.PL.FIELD.B` | `InIbanPlus_FieldB` | TField |  |  |
| 13 | `IN.PL.SOURCE.NAME` | `InIbanPlus_SourceName` | TField |  | This field will be populated as a result of the upload process with the File Name of the IBAN Plus, through which the record was created in the system or amended This field will not be populated when a manual record is created in DE.BIC Validation Rules: NOINPUT field |
| 14 | `IN.PL.EXCLUDED.COMPANY` | `InIbanPlus_ExcludedCompany` |  |  |  |
| 15 | `IN.PL.ALLOWED.COMPANY` | `InIbanPlus_AllowedCompany` |  |  |  |
| 16 | `IN.PL.STATUS` | `InIbanPlus_Status` | TField |  | Captures the status of the IBAN Plus record Validation Rules: Can be either Blank or DELETE. Default value is blank. |
| 17 | `IN.PL.ENTRY.TYPE` | `InIbanPlus_EntryType` | TField |  | Set as UPLOAD when record is uploaded through IN.IBAN.PLUS.UPLOAD.SERVICE. In other scenarios, it is set as CUSTOM. Validation Rules: NOINPUT field |
| 18 | `IN.PL.RESERVED.15` | `InIbanPlus_Reserved15` | TField |  |  |
| 19 | `IN.PL.RESERVED.14` | `InIbanPlus_Reserved14` | TField |  |  |
| 20 | `IN.PL.RESERVED.13` | `InIbanPlus_Reserved13` | TField |  |  |
| 21 | `IN.PL.RESERVED.12` | `InIbanPlus_Reserved12` | TField |  |  |
| 22 | `IN.PL.RESERVED.11` | `InIbanPlus_Reserved11` | TField |  |  |
| 23 | `IN.PL.RESERVED.10` | `InIbanPlus_Reserved10` | TField |  |  |
| 24 | `IN.PL.RESERVED.9` | `InIbanPlus_Reserved9` | TField |  |  |
| 25 | `IN.PL.RESERVED.8` | `InIbanPlus_Reserved8` | TField |  |  |
| 26 | `IN.PL.RESERVED.7` | `InIbanPlus_Reserved7` | TField |  |  |
| 27 | `IN.PL.RESERVED.6` | `InIbanPlus_Reserved6` | TField |  |  |
| 28 | `IN.PL.RESERVED.5` | `InIbanPlus_Reserved5` | TField |  |  |
| 29 | `IN.PL.RESERVED.4` | `InIbanPlus_Reserved4` | TField |  |  |
| 30 | `IN.PL.RESERVED.3` | `InIbanPlus_Reserved3` | TField |  |  |
| 31 | `IN.PL.LOCAL.REF` | `InIbanPlus_LocalRef` |  |  |  |
| 32 | `IN.PL.OVERRIDE` | `InIbanPlus_Override` |  |  |  |
| 33 | `IN.PL.RECORD.STATUS` | `InIbanPlus_RecordStatus` | String |  |  |
| 34 | `IN.PL.CURR.NO` | `InIbanPlus_CurrNo` | String |  |  |
| 35 | `IN.PL.INPUTTER` | `InIbanPlus_Inputter` |  |  |  |
| 36 | `IN.PL.DATE.TIME` | `InIbanPlus_DateTime` |  |  |  |
| 37 | `IN.PL.AUTHORISER` | `InIbanPlus_Authoriser` | String |  |  |
| 38 | `IN.PL.CO.CODE` | `InIbanPlus_CoCode` | String |  |  |
| 39 | `IN.PL.DEPT.CODE` | `InIbanPlus_DeptCode` | String |  |  |
| 40 | `IN.PL.AUDITOR.CODE` | `InIbanPlus_AuditorCode` | String |  |  |
| 41 | `IN.PL.AUDIT.DATE.TIME` | `InIbanPlus_AuditDateTime` | String |  |  |
