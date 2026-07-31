# FATCA.W9.EXEMPTION.CODES — Table Schema

> Source: `INSERTS/I_F.FATCA.W9.EXEMPTION.CODES` in `FA_CustomerIdentification.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FA.EC.DESCRIPTION` | `FatcaW9ExemptionCodes_Description` |  |  |  |
| 2 | `FA.EC.OTHER.INFO` | `FatcaW9ExemptionCodes_OtherInfo` |  |  |  |
| 3 | `FA.EC.RESERVED.5` | `FatcaW9ExemptionCodes_Reserved5` |  |  |  |
| 4 | `FA.EC.RESERVED.4` | `FatcaW9ExemptionCodes_Reserved4` |  |  |  |
| 5 | `FA.EC.RESERVED.3` | `FatcaW9ExemptionCodes_Reserved3` |  |  |  |
| 6 | `FA.EC.RESERVED.2` | `FatcaW9ExemptionCodes_Reserved2` |  |  |  |
| 7 | `FA.EC.RESERVED.1` | `FatcaW9ExemptionCodes_Reserved1` |  |  |  |
| 8 | `FA.EC.LOCAL.REF` | `FatcaW9ExemptionCodes_LocalRef` |  |  |  |
| 9 | `FA.EC.RECORD.STATUS` | `FatcaW9ExemptionCodes_RecordStatus` |  |  |  |
| 10 | `FA.EC.CURR.NO` | `FatcaW9ExemptionCodes_CurrNo` |  |  |  |
| 11 | `FA.EC.INPUTTER` | `FatcaW9ExemptionCodes_Inputter` |  |  |  |
| 12 | `FA.EC.DATE.TIME` | `FatcaW9ExemptionCodes_DateTime` |  |  |  |
| 13 | `FA.EC.AUTHORISER` | `FatcaW9ExemptionCodes_Authoriser` |  |  |  |
| 14 | `FA.EC.CO.CODE` | `FatcaW9ExemptionCodes_CoCode` |  |  |  |
| 15 | `FA.EC.DEPT.CODE` | `FatcaW9ExemptionCodes_DeptCode` |  |  |  |
| 16 | `FA.EC.AUDITOR.CODE` | `FatcaW9ExemptionCodes_AuditorCode` |  |  |  |
| 17 | `FA.EC.AUDIT.DATE.TIME` | `FatcaW9ExemptionCodes_AuditDateTime` |  |  |  |
