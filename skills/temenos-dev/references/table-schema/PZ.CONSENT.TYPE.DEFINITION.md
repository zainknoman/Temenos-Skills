# PZ.CONSENT.TYPE.DEFINITION — Table Schema

> Source: `INSERTS/I_F.PZ.CONSENT.TYPE.DEFINITION` in `PZ_Consent.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PZ.CTD.DESCRIPTION` | `PzConsentTypeDefinition_Description` |  |  |  |
| 2 | `PZ.CTD.PURPOSE` | `PzConsentTypeDefinition_Purpose` | TField |  | Field to indicate type of consent that is stored. Validation Rules: The Account Consent module is designed to record different purposes of consent (AISP, CBPII and for someguidelines, PISP). |
| 3 | `PZ.CTD.GRANULAR.CONSENT` | `PzConsentTypeDefinition_GranularConsent` |  |  |  |
| 4 | `PZ.CTD.FULL.DESCRIPTION` | `PzConsentTypeDefinition_FullDescription` | TField |  | Field to provide additional information related to the Consent Type description. The value in this field can be displayed as supplementary information within online channels screens. Validation Rules: Allowed values - Alphanumeric values in addition to a special character '\|' to assist, where multiple valuesneed to be defined. |
| 5 | `PZ.CTD.RESERVED.19` | `PzConsentTypeDefinition_Reserved19` | TField |  |  |
| 6 | `PZ.CTD.RESERVED.18` | `PzConsentTypeDefinition_Reserved18` | TField |  |  |
| 7 | `PZ.CTD.RESERVED.17` | `PzConsentTypeDefinition_Reserved17` | TField |  |  |
| 8 | `PZ.CTD.RESERVED.16` | `PzConsentTypeDefinition_Reserved16` | TField |  |  |
| 9 | `PZ.CTD.RESERVED.15` | `PzConsentTypeDefinition_Reserved15` | TField |  |  |
| 10 | `PZ.CTD.RESERVED.14` | `PzConsentTypeDefinition_Reserved14` | TField |  |  |
| 11 | `PZ.CTD.RESERVED.13` | `PzConsentTypeDefinition_Reserved13` | TField |  |  |
| 12 | `PZ.CTD.RESERVED.12` | `PzConsentTypeDefinition_Reserved12` | TField |  |  |
| 13 | `PZ.CTD.RESERVED.11` | `PzConsentTypeDefinition_Reserved11` | TField |  |  |
| 14 | `PZ.CTD.RESERVED.10` | `PzConsentTypeDefinition_Reserved10` | TField |  |  |
| 15 | `PZ.CTD.RESERVED.09` | `PzConsentTypeDefinition_Reserved09` | TField |  |  |
| 16 | `PZ.CTD.RESERVED.08` | `PzConsentTypeDefinition_Reserved08` | TField |  |  |
| 17 | `PZ.CTD.RESERVED.07` | `PzConsentTypeDefinition_Reserved07` | TField |  |  |
| 18 | `PZ.CTD.RESERVED.06` | `PzConsentTypeDefinition_Reserved06` | TField |  |  |
| 19 | `PZ.CTD.RESERVED.05` | `PzConsentTypeDefinition_Reserved05` | TField |  |  |
| 20 | `PZ.CTD.RESERVED.04` | `PzConsentTypeDefinition_Reserved04` | TField |  |  |
| 21 | `PZ.CTD.RESERVED.03` | `PzConsentTypeDefinition_Reserved03` | TField |  |  |
| 22 | `PZ.CTD.RESERVED.02` | `PzConsentTypeDefinition_Reserved02` | TField |  |  |
| 23 | `PZ.CTD.RESERVED.01` | `PzConsentTypeDefinition_Reserved01` | TField |  |  |
| 24 | `PZ.CTD.LOCAL.REF` | `PzConsentTypeDefinition_LocalRef` |  |  |  |
| 25 | `PZ.CTD.OVERRIDE` | `PzConsentTypeDefinition_Override` |  |  |  |
| 26 | `PZ.CTD.RECORD.STATUS` | `PzConsentTypeDefinition_RecordStatus` | String |  |  |
| 27 | `PZ.CTD.CURR.NO` | `PzConsentTypeDefinition_CurrNo` | String |  |  |
| 28 | `PZ.CTD.INPUTTER` | `PzConsentTypeDefinition_Inputter` |  |  |  |
| 29 | `PZ.CTD.DATE.TIME` | `PzConsentTypeDefinition_DateTime` |  |  |  |
| 30 | `PZ.CTD.AUTHORISER` | `PzConsentTypeDefinition_Authoriser` | String |  |  |
| 31 | `PZ.CTD.CO.CODE` | `PzConsentTypeDefinition_CoCode` | String |  |  |
| 32 | `PZ.CTD.DEPT.CODE` | `PzConsentTypeDefinition_DeptCode` | String |  |  |
| 33 | `PZ.CTD.AUDITOR.CODE` | `PzConsentTypeDefinition_AuditorCode` | String |  |  |
| 34 | `PZ.CTD.AUDIT.DATE.TIME` | `PzConsentTypeDefinition_AuditDateTime` | String |  |  |
