# CARD.ELIGIBILITY — Table Schema

> Source: `INSERTS/I_F.CARD.ELIGIBILITY` in `CACARD_CardManagement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.CDEG.FIELD.TO.CHK` | `CardEligibility_FieldToChk` |  |  |  |
| 2 | `CAMB.CDEG.FIELD.OPERAND` | `CardEligibility_FieldOperand` |  |  |  |
| 3 | `CAMB.CDEG.FIELD.VALUE` | `CardEligibility_FieldValue` |  |  |  |
| 4 | `CAMB.CDEG.RESERVED.1` | `CardEligibility_Reserved1` | TField |  |  |
| 5 | `CAMB.CDEG.RESERVED.2` | `CardEligibility_Reserved2` | TField |  |  |
| 6 | `CAMB.CDEG.RESERVED.3` | `CardEligibility_Reserved3` | TField |  |  |
| 7 | `CAMB.CDEG.RESERVED.4` | `CardEligibility_Reserved4` | TField |  |  |
| 8 | `CAMB.CDEG.RESERVED.5` | `CardEligibility_Reserved5` | TField |  |  |
| 9 | `CAMB.CDEG.RESERVED.6` | `CardEligibility_Reserved6` | TField |  |  |
| 10 | `CAMB.CDEG.RESERVED.7` | `CardEligibility_Reserved7` | TField |  |  |
| 11 | `CAMB.CDEG.RESERVED.8` | `CardEligibility_Reserved8` | TField |  |  |
| 12 | `CAMB.CDEG.RESERVED.9` | `CardEligibility_Reserved9` | TField |  |  |
| 13 | `CAMB.CDEG.RESERVED.10` | `CardEligibility_Reserved10` | TField |  |  |
| 14 | `CAMB.CDEG.RESERVED.11` | `CardEligibility_Reserved11` | TField |  |  |
| 15 | `CAMB.CDEG.LOCAL.REF` | `CardEligibility_LocalRef` |  |  |  |
| 16 | `CAMB.CDEG.RECORD.STATUS` | `CardEligibility_RecordStatus` | String |  |  |
| 17 | `CAMB.CDEG.CURR.NO` | `CardEligibility_CurrNo` | String |  |  |
| 18 | `CAMB.CDEG.INPUTTER` | `CardEligibility_Inputter` |  |  |  |
| 19 | `CAMB.CDEG.DATE.TIME` | `CardEligibility_DateTime` |  |  |  |
| 20 | `CAMB.CDEG.AUTHORISER` | `CardEligibility_Authoriser` | String |  |  |
| 21 | `CAMB.CDEG.CO.CODE` | `CardEligibility_CoCode` | String |  |  |
| 22 | `CAMB.CDEG.DEPT.CODE` | `CardEligibility_DeptCode` | String |  |  |
| 23 | `CAMB.CDEG.AUDITOR.CODE` | `CardEligibility_AuditorCode` | String |  |  |
| 24 | `CAMB.CDEG.AUDIT.DATE.TIME` | `CardEligibility_AuditDateTime` | String |  |  |
