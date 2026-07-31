# PA.CONSENT.TYPE.DEFINITION — Table Schema

> Source: `INSERTS/I_F.PA.CONSENT.TYPE.DEFINITION` in `PA_Consent.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PA.CTD.DESCRIPTION` | `PaConsentTypeDefinition_Description` | TField |  |  |
| 2 | `PA.CTD.PURPOSE` | `PaConsentTypeDefinition_Purpose` | TField |  |  |
| 3 | `PA.CTD.GRANULAR.CONSENT` | `PaConsentTypeDefinition_GranularConsent` |  |  |  |
| 4 | `PA.CTD.RESERVED.20` | `PaConsentTypeDefinition_Reserved20` | TField |  |  |
| 5 | `PA.CTD.RESERVED.19` | `PaConsentTypeDefinition_Reserved19` | TField |  |  |
| 6 | `PA.CTD.RESERVED.18` | `PaConsentTypeDefinition_Reserved18` | TField |  |  |
| 7 | `PA.CTD.RESERVED.17` | `PaConsentTypeDefinition_Reserved17` | TField |  |  |
| 8 | `PA.CTD.RESERVED.16` | `PaConsentTypeDefinition_Reserved16` | TField |  |  |
| 9 | `PA.CTD.RESERVED.15` | `PaConsentTypeDefinition_Reserved15` | TField |  |  |
| 10 | `PA.CTD.RESERVED.14` | `PaConsentTypeDefinition_Reserved14` | TField |  |  |
| 11 | `PA.CTD.RESERVED.13` | `PaConsentTypeDefinition_Reserved13` | TField |  |  |
| 12 | `PA.CTD.RESERVED.12` | `PaConsentTypeDefinition_Reserved12` | TField |  |  |
| 13 | `PA.CTD.RESERVED.11` | `PaConsentTypeDefinition_Reserved11` | TField |  |  |
| 14 | `PA.CTD.RESERVED.10` | `PaConsentTypeDefinition_Reserved10` | TField |  |  |
| 15 | `PA.CTD.RESERVED.09` | `PaConsentTypeDefinition_Reserved09` | TField |  |  |
| 16 | `PA.CTD.RESERVED.08` | `PaConsentTypeDefinition_Reserved08` | TField |  |  |
| 17 | `PA.CTD.RESERVED.07` | `PaConsentTypeDefinition_Reserved07` | TField |  |  |
| 18 | `PA.CTD.RESERVED.06` | `PaConsentTypeDefinition_Reserved06` | TField |  |  |
| 19 | `PA.CTD.RESERVED.05` | `PaConsentTypeDefinition_Reserved05` | TField |  |  |
| 20 | `PA.CTD.RESERVED.04` | `PaConsentTypeDefinition_Reserved04` | TField |  |  |
| 21 | `PA.CTD.RESERVED.03` | `PaConsentTypeDefinition_Reserved03` | TField |  |  |
| 22 | `PA.CTD.RESERVED.02` | `PaConsentTypeDefinition_Reserved02` | TField |  |  |
| 23 | `PA.CTD.RESERVED.01` | `PaConsentTypeDefinition_Reserved01` | TField |  |  |
| 24 | `PA.CTD.LOCAL.REF` | `PaConsentTypeDefinition_LocalRef` |  |  |  |
| 25 | `PA.CTD.OVERRIDE` | `PaConsentTypeDefinition_Override` |  |  |  |
| 26 | `PA.CTD.RECORD.STATUS` | `PaConsentTypeDefinition_RecordStatus` | String |  |  |
| 27 | `PA.CTD.CURR.NO` | `PaConsentTypeDefinition_CurrNo` | String |  |  |
| 28 | `PA.CTD.INPUTTER` | `PaConsentTypeDefinition_Inputter` |  |  |  |
| 29 | `PA.CTD.DATE.TIME` | `PaConsentTypeDefinition_DateTime` |  |  |  |
| 30 | `PA.CTD.AUTHORISER` | `PaConsentTypeDefinition_Authoriser` | String |  |  |
| 31 | `PA.CTD.CO.CODE` | `PaConsentTypeDefinition_CoCode` | String |  |  |
| 32 | `PA.CTD.DEPT.CODE` | `PaConsentTypeDefinition_DeptCode` | String |  |  |
| 33 | `PA.CTD.AUDITOR.CODE` | `PaConsentTypeDefinition_AuditorCode` | String |  |  |
| 34 | `PA.CTD.AUDIT.DATE.TIME` | `PaConsentTypeDefinition_AuditDateTime` | String |  |  |
