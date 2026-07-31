# LBNCDR.LIAB.CROSS.LOAN — Table Schema

> Source: `INSERTS/I_F.LBNCDR.LIAB.CROSS.LOAN` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.LCL.POSS.LIAB.CROSS.ID` | `LbncdrLiabCrossLoan_PossLiabCrossId` |  |  |  |
| 2 | `LBNCDR.LCL.RESERVED.10` | `LbncdrLiabCrossLoan_Reserved10` | TField |  |  |
| 3 | `LBNCDR.LCL.RESERVED.9` | `LbncdrLiabCrossLoan_Reserved9` | TField |  |  |
| 4 | `LBNCDR.LCL.RESERVED.8` | `LbncdrLiabCrossLoan_Reserved8` | TField |  |  |
| 5 | `LBNCDR.LCL.RESERVED.7` | `LbncdrLiabCrossLoan_Reserved7` | TField |  |  |
| 6 | `LBNCDR.LCL.RESERVED.6` | `LbncdrLiabCrossLoan_Reserved6` | TField |  |  |
| 7 | `LBNCDR.LCL.RESERVED.5` | `LbncdrLiabCrossLoan_Reserved5` | TField |  |  |
| 8 | `LBNCDR.LCL.RESERVED.4` | `LbncdrLiabCrossLoan_Reserved4` | TField |  |  |
| 9 | `LBNCDR.LCL.RESERVED.3` | `LbncdrLiabCrossLoan_Reserved3` | TField |  |  |
| 10 | `LBNCDR.LCL.RESERVED.2` | `LbncdrLiabCrossLoan_Reserved2` | TField |  |  |
| 11 | `LBNCDR.LCL.RESERVED.1` | `LbncdrLiabCrossLoan_Reserved1` | TField |  |  |
| 12 | `LBNCDR.LCL.LOCAL.REF` | `LbncdrLiabCrossLoan_LocalRef` |  |  |  |
| 13 | `LBNCDR.LCL.OVERRIDE` | `LbncdrLiabCrossLoan_Override` |  |  |  |
| 14 | `LBNCDR.LCL.RECORD.STATUS` | `LbncdrLiabCrossLoan_RecordStatus` | String |  |  |
| 15 | `LBNCDR.LCL.CURR.NO` | `LbncdrLiabCrossLoan_CurrNo` | String |  |  |
| 16 | `LBNCDR.LCL.INPUTTER` | `LbncdrLiabCrossLoan_Inputter` |  |  |  |
| 17 | `LBNCDR.LCL.DATE.TIME` | `LbncdrLiabCrossLoan_DateTime` |  |  |  |
| 18 | `LBNCDR.LCL.AUTHORISER` | `LbncdrLiabCrossLoan_Authoriser` | String |  |  |
| 19 | `LBNCDR.LCL.CO.CODE` | `LbncdrLiabCrossLoan_CoCode` | String |  |  |
| 20 | `LBNCDR.LCL.DEPT.CODE` | `LbncdrLiabCrossLoan_DeptCode` | String |  |  |
| 21 | `LBNCDR.LCL.AUDITOR.CODE` | `LbncdrLiabCrossLoan_AuditorCode` | String |  |  |
| 22 | `LBNCDR.LCL.AUDIT.DATE.TIME` | `LbncdrLiabCrossLoan_AuditDateTime` | String |  |  |
