# LBNCDR.CLASS.CLIENT — Table Schema

> Source: `INSERTS/I_F.LBNCDR.CLASS.CLIENT` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.CC.CLT.CLASS.CODE` | `LbncdrClassClient_CltClassCode` | TField |  |  |
| 2 | `LBNCDR.CC.CLT.CLASS.DES.LATIN` | `LbncdrClassClient_CltClassDesLatin` | TField |  | Holds the Loan Type Description Validation Rules 35 ANY |
| 3 | `LBNCDR.CC.CLT.CLASS.DES.ARABI` | `LbncdrClassClient_CltClassDesArabi` | TField |  | Holds Loan Type Local Currency Validation Rules 2 ANY |
| 4 | `LBNCDR.CC.RESERVED.10` | `LbncdrClassClient_Reserved10` | TField |  |  |
| 5 | `LBNCDR.CC.RESERVED.9` | `LbncdrClassClient_Reserved9` | TField |  |  |
| 6 | `LBNCDR.CC.RESERVED.8` | `LbncdrClassClient_Reserved8` | TField |  |  |
| 7 | `LBNCDR.CC.RESERVED.7` | `LbncdrClassClient_Reserved7` | TField |  |  |
| 8 | `LBNCDR.CC.RESERVED.6` | `LbncdrClassClient_Reserved6` | TField |  |  |
| 9 | `LBNCDR.CC.RESERVED.5` | `LbncdrClassClient_Reserved5` | TField |  |  |
| 10 | `LBNCDR.CC.RESERVED.4` | `LbncdrClassClient_Reserved4` | TField |  |  |
| 11 | `LBNCDR.CC.RESERVED.3` | `LbncdrClassClient_Reserved3` | TField |  |  |
| 12 | `LBNCDR.CC.RESERVED.2` | `LbncdrClassClient_Reserved2` | TField |  |  |
| 13 | `LBNCDR.CC.RESERVED.1` | `LbncdrClassClient_Reserved1` | TField |  |  |
| 14 | `LBNCDR.CC.OVERRIDE` | `LbncdrClassClient_Override` |  |  |  |
| 15 | `LBNCDR.CC.RECORD.STATUS` | `LbncdrClassClient_RecordStatus` | String |  |  |
| 16 | `LBNCDR.CC.CURR.NO` | `LbncdrClassClient_CurrNo` | String |  |  |
| 17 | `LBNCDR.CC.INPUTTER` | `LbncdrClassClient_Inputter` |  |  |  |
| 18 | `LBNCDR.CC.DATE.TIME` | `LbncdrClassClient_DateTime` |  |  |  |
| 19 | `LBNCDR.CC.AUTHORISER` | `LbncdrClassClient_Authoriser` | String |  |  |
| 20 | `LBNCDR.CC.CO.CODE` | `LbncdrClassClient_CoCode` | String |  |  |
| 21 | `LBNCDR.CC.DEPT.CODE` | `LbncdrClassClient_DeptCode` | String |  |  |
| 22 | `LBNCDR.CC.AUDITOR.CODE` | `LbncdrClassClient_AuditorCode` | String |  |  |
| 23 | `LBNCDR.CC.AUDIT.DATE.TIME` | `LbncdrClassClient_AuditDateTime` | String |  |  |
