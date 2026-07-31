# FIPAVL.FEE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.FIPAVL.FEE.PARAMETER` in `FIPAVL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FIPAVL.FEE.PARAMETER.WITH.AGREE.CR.REF.NUM` | `FipavlFeeParameter_WithAgreeCrRefNum` | TField |  | Fee details for Customer agreement exists and Creditor reference code exists |
| 2 | `FIPAVL.FEE.PARAMETER.NO.AGREE.WITH.CR.REF.NUM` | `FipavlFeeParameter_NoAgreeWithCrRefNum` | TField |  | Fee details for Customer agreement does NOT exists and Creditor reference code exists |
| 3 | `FIPAVL.FEE.PARAMETER.NO.AGREE.NO.CR.REF.NUM` | `FipavlFeeParameter_NoAgreeNoCrRefNum` | TField |  | Fee details for Customer agreement does NOT exists and Creditor reference code does NOT exists |
| 4 | `FIPAVL.FEE.PARAMETER.ERI.PER.OCCURENCE.FEE` | `FipavlFeeParameter_EriPerOccurenceFee` | TField |  | Fee details for Customer agreement exists and Creditor reference code does NOT exists |
| 5 | `FIPAVL.FEE.PARAMETER.RESERVED.10` | `FipavlFeeParameter_Reserved10` | TField |  |  |
| 6 | `FIPAVL.FEE.PARAMETER.RESERVED.9` | `FipavlFeeParameter_Reserved9` | TField |  |  |
| 7 | `FIPAVL.FEE.PARAMETER.RESERVED.8` | `FipavlFeeParameter_Reserved8` | TField |  |  |
| 8 | `FIPAVL.FEE.PARAMETER.RESERVED.7` | `FipavlFeeParameter_Reserved7` | TField |  |  |
| 9 | `FIPAVL.FEE.PARAMETER.RESERVED.6` | `FipavlFeeParameter_Reserved6` | TField |  |  |
| 10 | `FIPAVL.FEE.PARAMETER.RESERVED.5` | `FipavlFeeParameter_Reserved5` | TField |  |  |
| 11 | `FIPAVL.FEE.PARAMETER.RESERVED.4` | `FipavlFeeParameter_Reserved4` | TField |  |  |
| 12 | `FIPAVL.FEE.PARAMETER.RESERVED.3` | `FipavlFeeParameter_Reserved3` | TField |  |  |
| 13 | `FIPAVL.FEE.PARAMETER.RESERVED.2` | `FipavlFeeParameter_Reserved2` | TField |  |  |
| 14 | `FIPAVL.FEE.PARAMETER.RESERVED.1` | `FipavlFeeParameter_Reserved1` | TField |  |  |
| 15 | `FIPAVL.FEE.PARAMETER.LOCAL.REF` | `FipavlFeeParameter_LocalRef` |  |  |  |
| 16 | `FIPAVL.FEE.PARAMETER.OVERRIDE` | `FipavlFeeParameter_Override` |  |  |  |
| 17 | `FIPAVL.FEE.PARAMETER.RECORD.STATUS` | `FipavlFeeParameter_RecordStatus` | String |  |  |
| 18 | `FIPAVL.FEE.PARAMETER.CURR.NO` | `FipavlFeeParameter_CurrNo` | String |  |  |
| 19 | `FIPAVL.FEE.PARAMETER.INPUTTER` | `FipavlFeeParameter_Inputter` |  |  |  |
| 20 | `FIPAVL.FEE.PARAMETER.DATE.TIME` | `FipavlFeeParameter_DateTime` |  |  |  |
| 21 | `FIPAVL.FEE.PARAMETER.AUTHORISER` | `FipavlFeeParameter_Authoriser` | String |  |  |
| 22 | `FIPAVL.FEE.PARAMETER.CO.CODE` | `FipavlFeeParameter_CoCode` | String |  |  |
| 23 | `FIPAVL.FEE.PARAMETER.DEPT.CODE` | `FipavlFeeParameter_DeptCode` | String |  |  |
| 24 | `FIPAVL.FEE.PARAMETER.AUDITOR.CODE` | `FipavlFeeParameter_AuditorCode` | String |  |  |
| 25 | `FIPAVL.FEE.PARAMETER.AUDIT.DATE.TIME` | `FipavlFeeParameter_AuditDateTime` | String |  |  |
