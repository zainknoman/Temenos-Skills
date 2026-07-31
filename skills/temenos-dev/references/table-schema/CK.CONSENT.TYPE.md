# CK.CONSENT.TYPE — Table Schema

> Source: `INSERTS/I_F.CK.CONSENT.TYPE` in `CK_Consent.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CK.CT.DESCRIPTION` | `CkConsentType_Description` |  |  |  |
| 2 | `CK.CT.PURPOSE` | `CkConsentType_Purpose` | TField | Yes | This is a mandatory field to identify the purpose for the Consent Type. Validation Rules: Valid options are CDP, AISP and OTHER |
| 3 | `CK.CT.SUB.TYPE` | `CkConsentType_SubType` |  |  |  |
| 4 | `CK.CT.FULL.DESCRIPTION` | `CkConsentType_FullDescription` | TField | No | Detailed description of the Consent Type Validation Rules: 100 Free text. Optional field |
| 5 | `CK.CT.RESERVED.19` | `CkConsentType_Reserved19` | TField |  |  |
| 6 | `CK.CT.RESERVED.18` | `CkConsentType_Reserved18` | TField |  |  |
| 7 | `CK.CT.RESERVED.17` | `CkConsentType_Reserved17` | TField |  |  |
| 8 | `CK.CT.RESERVED.16` | `CkConsentType_Reserved16` | TField |  |  |
| 9 | `CK.CT.RESERVED.15` | `CkConsentType_Reserved15` | TField |  |  |
| 10 | `CK.CT.RESERVED.14` | `CkConsentType_Reserved14` | TField |  |  |
| 11 | `CK.CT.RESERVED.13` | `CkConsentType_Reserved13` | TField |  |  |
| 12 | `CK.CT.RESERVED.12` | `CkConsentType_Reserved12` | TField |  |  |
| 13 | `CK.CT.RESERVED.11` | `CkConsentType_Reserved11` | TField |  |  |
| 14 | `CK.CT.RESERVED.10` | `CkConsentType_Reserved10` | TField |  |  |
| 15 | `CK.CT.RESERVED.09` | `CkConsentType_Reserved09` | TField |  |  |
| 16 | `CK.CT.RESERVED.08` | `CkConsentType_Reserved08` | TField |  |  |
| 17 | `CK.CT.RESERVED.07` | `CkConsentType_Reserved07` | TField |  |  |
| 18 | `CK.CT.RESERVED.06` | `CkConsentType_Reserved06` | TField |  |  |
| 19 | `CK.CT.RESERVED.05` | `CkConsentType_Reserved05` | TField |  |  |
| 20 | `CK.CT.RESERVED.04` | `CkConsentType_Reserved04` | TField |  |  |
| 21 | `CK.CT.RESERVED.03` | `CkConsentType_Reserved03` | TField |  |  |
| 22 | `CK.CT.RESERVED.02` | `CkConsentType_Reserved02` | TField |  |  |
| 23 | `CK.CT.RESERVED.01` | `CkConsentType_Reserved01` | TField |  |  |
| 24 | `CK.CT.LOCAL.REF` | `CkConsentType_LocalRef` |  |  |  |
| 25 | `CK.CT.RECORD.STATUS` | `CkConsentType_RecordStatus` | String |  |  |
| 26 | `CK.CT.CURR.NO` | `CkConsentType_CurrNo` | String |  |  |
| 27 | `CK.CT.INPUTTER` | `CkConsentType_Inputter` |  |  |  |
| 28 | `CK.CT.DATE.TIME` | `CkConsentType_DateTime` |  |  |  |
| 29 | `CK.CT.AUTHORISER` | `CkConsentType_Authoriser` | String |  |  |
| 30 | `CK.CT.CO.CODE` | `CkConsentType_CoCode` | String |  |  |
| 31 | `CK.CT.DEPT.CODE` | `CkConsentType_DeptCode` | String |  |  |
| 32 | `CK.CT.AUDITOR.CODE` | `CkConsentType_AuditorCode` | String |  |  |
| 33 | `CK.CT.AUDIT.DATE.TIME` | `CkConsentType_AuditDateTime` | String |  |  |
