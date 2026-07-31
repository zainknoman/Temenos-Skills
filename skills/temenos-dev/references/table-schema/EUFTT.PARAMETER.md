# EUFTT.PARAMETER — Table Schema

> Source: `INSERTS/I_F.EUFTT.PARAMETER` in `EF_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EF.FTT.STATUS` | `EufttParameter_Status` | TField |  | Field describes the current status of the of Financial Institution with respect to EU-FTT compliance Validation Rules: Valid values are Opt In - Opting In for EU FTT compliance Opt Out - Opting out of the EU FTT Compliance Exempt - Exempted entities under EU FTT Compliance |
| 2 | `EF.FTT.AGREEMENT.DATE` | `EufttParameter_AgreementDate` | TField |  | To state the agreement date when the respective financial institution agrees to follow the EU-FTT regulation Validation Rules: Valid values are: Valid T24 Date |
| 3 | `EF.FTT.EFFECTIVE.DATE` | `EufttParameter_EffectiveDate` | TField |  | To state the effective date since when the financial institution will start complying to the provisions of EU-FTT regulation Validation Rules: Valid values are: Valid T24 Date |
| 4 | `EF.FTT.FTT.COUNTRIES` | `EufttParameter_FttCountries` |  |  |  |
| 5 | `EF.FTT.RESERVED.20` | `EufttParameter_Reserved20` |  |  |  |
| 6 | `EF.FTT.RESERVED.19` | `EufttParameter_Reserved19` | TField |  |  |
| 7 | `EF.FTT.RESERVED.18` | `EufttParameter_Reserved18` | TField |  |  |
| 8 | `EF.FTT.RESERVED.17` | `EufttParameter_Reserved17` | TField |  |  |
| 9 | `EF.FTT.RESERVED.16` | `EufttParameter_Reserved16` | TField |  |  |
| 10 | `EF.FTT.RESERVED.15` | `EufttParameter_Reserved15` | TField |  |  |
| 11 | `EF.FTT.RESERVED.14` | `EufttParameter_Reserved14` | TField |  |  |
| 12 | `EF.FTT.RESERVED.13` | `EufttParameter_Reserved13` | TField |  |  |
| 13 | `EF.FTT.RESERVED.12` | `EufttParameter_Reserved12` | TField |  |  |
| 14 | `EF.FTT.RESERVED.11` | `EufttParameter_Reserved11` | TField |  |  |
| 15 | `EF.FTT.RESERVED.10` | `EufttParameter_Reserved10` | TField |  |  |
| 16 | `EF.FTT.RESERVED.09` | `EufttParameter_Reserved09` | TField |  |  |
| 17 | `EF.FTT.RESERVED.08` | `EufttParameter_Reserved08` | TField |  |  |
| 18 | `EF.FTT.RESERVED.07` | `EufttParameter_Reserved07` | TField |  |  |
| 19 | `EF.FTT.RESERVED.06` | `EufttParameter_Reserved06` | TField |  |  |
| 20 | `EF.FTT.RESERVED.05` | `EufttParameter_Reserved05` | TField |  |  |
| 21 | `EF.FTT.RESERVED.04` | `EufttParameter_Reserved04` | TField |  |  |
| 22 | `EF.FTT.RESERVED.03` | `EufttParameter_Reserved03` | TField |  |  |
| 23 | `EF.FTT.RESERVED.02` | `EufttParameter_Reserved02` | TField |  |  |
| 24 | `EF.FTT.RESERVED.01` | `EufttParameter_Reserved01` | TField |  |  |
| 25 | `EF.FTT.LOCAL.REF` | `EufttParameter_LocalRef` |  |  |  |
| 26 | `EF.FTT.OVERRIDE` | `EufttParameter_Override` |  |  |  |
| 27 | `EF.FTT.RECORD.STATUS` | `EufttParameter_RecordStatus` | String |  |  |
| 28 | `EF.FTT.CURR.NO` | `EufttParameter_CurrNo` | String |  |  |
| 29 | `EF.FTT.INPUTTER` | `EufttParameter_Inputter` |  |  |  |
| 30 | `EF.FTT.DATE.TIME` | `EufttParameter_DateTime` |  |  |  |
| 31 | `EF.FTT.AUTHORISER` | `EufttParameter_Authoriser` | String |  |  |
| 32 | `EF.FTT.CO.CODE` | `EufttParameter_CoCode` | String |  |  |
| 33 | `EF.FTT.DEPT.CODE` | `EufttParameter_DeptCode` | String |  |  |
| 34 | `EF.FTT.AUDITOR.CODE` | `EufttParameter_AuditorCode` | String |  |  |
| 35 | `EF.FTT.AUDIT.DATE.TIME` | `EufttParameter_AuditDateTime` | String |  |  |
