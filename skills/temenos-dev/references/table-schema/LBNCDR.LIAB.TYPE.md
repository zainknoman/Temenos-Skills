# LBNCDR.LIAB.TYPE — Table Schema

> Source: `INSERTS/I_F.LBNCDR.LIAB.TYPE` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.LIT.SHORT.DESCRIPTION` | `LbncdrLiabType_ShortDescription` | TField |  |  |
| 2 | `LBNCDR.LIT.DESCRIPTION` | `LbncdrLiabType_Description` | TField |  | Holds the Liability Group Description Validation Rules 50 ANY |
| 3 | `LBNCDR.LIT.AUTHORIZED` | `LbncdrLiabType_Authorized` | TField |  | YES or NO Validation Rules 3 ANY |
| 4 | `LBNCDR.LIT.TYPE` | `LbncdrLiabType_Type` | TField |  | YES or NO Validation Rules 3 ANY |
| 5 | `LBNCDR.LIT.MARGIN` | `LbncdrLiabType_Margin` | TField |  | YES or NO Validation Rules 3 ANY |
| 6 | `LBNCDR.LIT.RESERVED.10` | `LbncdrLiabType_Reserved10` | TField |  |  |
| 7 | `LBNCDR.LIT.RESERVED.9` | `LbncdrLiabType_Reserved9` | TField |  |  |
| 8 | `LBNCDR.LIT.RESERVED.8` | `LbncdrLiabType_Reserved8` | TField |  |  |
| 9 | `LBNCDR.LIT.RESERVED.7` | `LbncdrLiabType_Reserved7` | TField |  |  |
| 10 | `LBNCDR.LIT.RESERVED.6` | `LbncdrLiabType_Reserved6` | TField |  |  |
| 11 | `LBNCDR.LIT.RESERVED.5` | `LbncdrLiabType_Reserved5` | TField |  |  |
| 12 | `LBNCDR.LIT.RESERVED.4` | `LbncdrLiabType_Reserved4` | TField |  |  |
| 13 | `LBNCDR.LIT.RESERVED.3` | `LbncdrLiabType_Reserved3` | TField |  |  |
| 14 | `LBNCDR.LIT.RESERVED.2` | `LbncdrLiabType_Reserved2` | TField |  |  |
| 15 | `LBNCDR.LIT.RESERVED.1` | `LbncdrLiabType_Reserved1` | TField |  |  |
| 16 | `LBNCDR.LIT.LOCAL.REF` | `LbncdrLiabType_LocalRef` |  |  |  |
| 17 | `LBNCDR.LIT.OVERRIDE` | `LbncdrLiabType_Override` |  |  |  |
| 18 | `LBNCDR.LIT.RECORD.STATUS` | `LbncdrLiabType_RecordStatus` | String |  |  |
| 19 | `LBNCDR.LIT.CURR.NO` | `LbncdrLiabType_CurrNo` | String |  |  |
| 20 | `LBNCDR.LIT.INPUTTER` | `LbncdrLiabType_Inputter` |  |  |  |
| 21 | `LBNCDR.LIT.DATE.TIME` | `LbncdrLiabType_DateTime` |  |  |  |
| 22 | `LBNCDR.LIT.AUTHORISER` | `LbncdrLiabType_Authoriser` | String |  |  |
| 23 | `LBNCDR.LIT.CO.CODE` | `LbncdrLiabType_CoCode` | String |  |  |
| 24 | `LBNCDR.LIT.DEPT.CODE` | `LbncdrLiabType_DeptCode` | String |  |  |
| 25 | `LBNCDR.LIT.AUDITOR.CODE` | `LbncdrLiabType_AuditorCode` | String |  |  |
| 26 | `LBNCDR.LIT.AUDIT.DATE.TIME` | `LbncdrLiabType_AuditDateTime` | String |  |  |
