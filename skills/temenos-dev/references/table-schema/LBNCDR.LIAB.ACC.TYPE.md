# LBNCDR.LIAB.ACC.TYPE — Table Schema

> Source: `INSERTS/I_F.LBNCDR.LIAB.ACC.TYPE` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.LAT.LIAB.TYPE` | `LbncdrLiabAccType_LiabType` | TField |  | Holds the Liability Type value. Must be first part of the id. e.g. ID is ABL.5 Liability Type ABL Validation Rules 3 A |
| 2 | `LBNCDR.LAT.LIAB.TYPE.DESC` | `LbncdrLiabAccType_LiabTypeDesc` | TField |  | Holds the Liability Type Description value. Validation Rules 65 ANY |
| 3 | `LBNCDR.LAT.AC.TYPE` | `LbncdrLiabAccType_AcType` | TField |  | Holds the Account Type value. Must be second part of the id e.g. ID is ABL.5 Account Type 5 Validation Rules 2 A |
| 4 | `LBNCDR.LAT.AC.TYPE.DESC` | `LbncdrLiabAccType_AcTypeDesc` | TField |  | Holds the Account Type Description value Validation Rules 65 A |
| 5 | `LBNCDR.LAT.GUARANTY.IND` | `LbncdrLiabAccType_GuarantyInd` | TField |  | Holds 0 or 1 0 means No and 1 means Yes Validation Rules 1 ANY |
| 6 | `LBNCDR.LAT.LIAB.DETS` | `LbncdrLiabAccType_LiabDets` | TField |  | Holds Liability Group or Liability Sub-Group or Liability Type Validation Rules 6 ANY |
| 7 | `LBNCDR.LAT.CREDIT.IND` | `LbncdrLiabAccType_CreditInd` | TField |  | Holds 0 or 1 0 means No and 1 means Yes Validation Rules 1 ANY |
| 8 | `LBNCDR.LAT.RESERVED.1` | `LbncdrLiabAccType_Reserved1` | TField |  |  |
| 9 | `LBNCDR.LAT.RESERVED.2` | `LbncdrLiabAccType_Reserved2` | TField |  |  |
| 10 | `LBNCDR.LAT.RESERVED.3` | `LbncdrLiabAccType_Reserved3` | TField |  |  |
| 11 | `LBNCDR.LAT.RESERVED.4` | `LbncdrLiabAccType_Reserved4` | TField |  |  |
| 12 | `LBNCDR.LAT.RESERVED.5` | `LbncdrLiabAccType_Reserved5` | TField |  |  |
| 13 | `LBNCDR.LAT.RESERVED.6` | `LbncdrLiabAccType_Reserved6` | TField |  |  |
| 14 | `LBNCDR.LAT.RESERVED.7` | `LbncdrLiabAccType_Reserved7` | TField |  |  |
| 15 | `LBNCDR.LAT.RESERVED.8` | `LbncdrLiabAccType_Reserved8` | TField |  |  |
| 16 | `LBNCDR.LAT.LOCAL.REF` | `LbncdrLiabAccType_LocalRef` |  |  |  |
| 17 | `LBNCDR.LAT.OVERRIDE` | `LbncdrLiabAccType_Override` |  |  |  |
| 18 | `LBNCDR.LAT.RECORD.STATUS` | `LbncdrLiabAccType_RecordStatus` | String |  |  |
| 19 | `LBNCDR.LAT.CURR.NO` | `LbncdrLiabAccType_CurrNo` | String |  |  |
| 20 | `LBNCDR.LAT.INPUTTER` | `LbncdrLiabAccType_Inputter` |  |  |  |
| 21 | `LBNCDR.LAT.DATE.TIME` | `LbncdrLiabAccType_DateTime` |  |  |  |
| 22 | `LBNCDR.LAT.AUTHORISER` | `LbncdrLiabAccType_Authoriser` | String |  |  |
| 23 | `LBNCDR.LAT.CO.CODE` | `LbncdrLiabAccType_CoCode` | String |  |  |
| 24 | `LBNCDR.LAT.DEPT.CODE` | `LbncdrLiabAccType_DeptCode` | String |  |  |
| 25 | `LBNCDR.LAT.AUDITOR.CODE` | `LbncdrLiabAccType_AuditorCode` | String |  |  |
| 26 | `LBNCDR.LAT.AUDIT.DATE.TIME` | `LbncdrLiabAccType_AuditDateTime` | String |  |  |
