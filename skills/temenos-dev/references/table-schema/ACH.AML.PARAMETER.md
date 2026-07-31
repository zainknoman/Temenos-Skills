# ACH.AML.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ACH.AML.PARAMETER` in `ACHFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACHAML.DESCRIPTION` | `AchAmlParameter_Description` |  |  |  |
| 2 | `ACHAML.VALIDATE.LEVELS` | `AchAmlParameter_ValidateLevels` | TField |  | Maximum level of the ACH entries record can be validated up to 99 Its a numeric field. |
| 3 | `ACHAML.RETRY` | `AchAmlParameter_Retry` | TField |  | If this field is set then failed ACH transaction can be retried. Values allowed are Y and N |
| 4 | `ACHAML.RESPONSE.PATH` | `AchAmlParameter_ResponsePath` | TField |  | AML response will be captured in this path |
| 5 | `ACHAML.RESPONSE.TIME` | `AchAmlParameter_ResponseTime` | TField |  | AML response time will be recorded in this field |
| 6 | `ACHAML.LOCAL.REF` | `AchAmlParameter_LocalRef` |  |  |  |
| 7 | `ACHAML.RESERVED.20` | `AchAmlParameter_Reserved20` | TField |  |  |
| 8 | `ACHAML.RESERVED.19` | `AchAmlParameter_Reserved19` | TField |  |  |
| 9 | `ACHAML.RESERVED.18` | `AchAmlParameter_Reserved18` | TField |  |  |
| 10 | `ACHAML.RESERVED.17` | `AchAmlParameter_Reserved17` | TField |  |  |
| 11 | `ACHAML.RESERVED.16` | `AchAmlParameter_Reserved16` | TField |  |  |
| 12 | `ACHAML.RESERVED.15` | `AchAmlParameter_Reserved15` | TField |  |  |
| 13 | `ACHAML.RESERVED.14` | `AchAmlParameter_Reserved14` | TField |  |  |
| 14 | `ACHAML.RESERVED.13` | `AchAmlParameter_Reserved13` | TField |  |  |
| 15 | `ACHAML.RESERVED.12` | `AchAmlParameter_Reserved12` | TField |  |  |
| 16 | `ACHAML.RESERVED.11` | `AchAmlParameter_Reserved11` | TField |  |  |
| 17 | `ACHAML.RESERVED.10` | `AchAmlParameter_Reserved10` | TField |  |  |
| 18 | `ACHAML.RESERVED.9` | `AchAmlParameter_Reserved9` | TField |  |  |
| 19 | `ACHAML.RESERVED.8` | `AchAmlParameter_Reserved8` | TField |  |  |
| 20 | `ACHAML.RESERVED.7` | `AchAmlParameter_Reserved7` | TField |  |  |
| 21 | `ACHAML.RESERVED.6` | `AchAmlParameter_Reserved6` | TField |  |  |
| 22 | `ACHAML.RESERVED.5` | `AchAmlParameter_Reserved5` | TField |  |  |
| 23 | `ACHAML.RESERVED.4` | `AchAmlParameter_Reserved4` | TField |  |  |
| 24 | `ACHAML.RESERVED.3` | `AchAmlParameter_Reserved3` | TField |  |  |
| 25 | `ACHAML.RESERVED.2` | `AchAmlParameter_Reserved2` | TField |  |  |
| 26 | `ACHAML.RESERVED.1` | `AchAmlParameter_Reserved1` | TField |  |  |
| 27 | `ACHAML.OVERRIDE` | `AchAmlParameter_Override` |  |  |  |
| 28 | `ACHAML.RECORD.STATUS` | `AchAmlParameter_RecordStatus` | String |  |  |
| 29 | `ACHAML.CURR.NO` | `AchAmlParameter_CurrNo` | String |  |  |
| 30 | `ACHAML.INPUTTER` | `AchAmlParameter_Inputter` |  |  |  |
| 31 | `ACHAML.DATE.TIME` | `AchAmlParameter_DateTime` |  |  |  |
| 32 | `ACHAML.AUTHORISER` | `AchAmlParameter_Authoriser` | String |  |  |
| 33 | `ACHAML.CO.CODE` | `AchAmlParameter_CoCode` | String |  |  |
| 34 | `ACHAML.DEPT.CODE` | `AchAmlParameter_DeptCode` | String |  |  |
| 35 | `ACHAML.AUDITOR.CODE` | `AchAmlParameter_AuditorCode` | String |  |  |
| 36 | `ACHAML.AUDIT.DATE.TIME` | `AchAmlParameter_AuditDateTime` | String |  |  |
