# LBNCDR.LOAN.TYPE — Table Schema

> Source: `INSERTS/I_F.LBNCDR.LOAN.TYPE` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.LOT.SHORT.DESC` | `LbncdrLoanType_ShortDesc` | TField |  | Holds the Loan Type Short Description Validation Rules 4 A |
| 2 | `LBNCDR.LOT.DESCRIPTION` | `LbncdrLoanType_Description` | TField |  | Holds the Loan Type Description Validation Rules 50 ANY |
| 3 | `LBNCDR.LOT.LOCAL.CCY` | `LbncdrLoanType_LocalCcy` | TField |  | Holds Loan Type Local Currency Validation Rules 3 ANY |
| 4 | `LBNCDR.LOT.RESERVED.10` | `LbncdrLoanType_Reserved10` | TField |  |  |
| 5 | `LBNCDR.LOT.RESERVED.9` | `LbncdrLoanType_Reserved9` | TField |  |  |
| 6 | `LBNCDR.LOT.RESERVED.8` | `LbncdrLoanType_Reserved8` | TField |  |  |
| 7 | `LBNCDR.LOT.RESERVED.7` | `LbncdrLoanType_Reserved7` | TField |  |  |
| 8 | `LBNCDR.LOT.RESERVED.6` | `LbncdrLoanType_Reserved6` | TField |  |  |
| 9 | `LBNCDR.LOT.RESERVED.5` | `LbncdrLoanType_Reserved5` | TField |  |  |
| 10 | `LBNCDR.LOT.RESERVED.4` | `LbncdrLoanType_Reserved4` | TField |  |  |
| 11 | `LBNCDR.LOT.RESERVED.3` | `LbncdrLoanType_Reserved3` | TField |  |  |
| 12 | `LBNCDR.LOT.RESERVED.2` | `LbncdrLoanType_Reserved2` | TField |  |  |
| 13 | `LBNCDR.LOT.RESERVED.1` | `LbncdrLoanType_Reserved1` | TField |  |  |
| 14 | `LBNCDR.LOT.LOCAL.REF` | `LbncdrLoanType_LocalRef` |  |  |  |
| 15 | `LBNCDR.LOT.OVERRIDE` | `LbncdrLoanType_Override` |  |  |  |
| 16 | `LBNCDR.LOT.RECORD.STATUS` | `LbncdrLoanType_RecordStatus` | String |  |  |
| 17 | `LBNCDR.LOT.CURR.NO` | `LbncdrLoanType_CurrNo` | String |  |  |
| 18 | `LBNCDR.LOT.INPUTTER` | `LbncdrLoanType_Inputter` |  |  |  |
| 19 | `LBNCDR.LOT.DATE.TIME` | `LbncdrLoanType_DateTime` |  |  |  |
| 20 | `LBNCDR.LOT.AUTHORISER` | `LbncdrLoanType_Authoriser` | String |  |  |
| 21 | `LBNCDR.LOT.CO.CODE` | `LbncdrLoanType_CoCode` | String |  |  |
| 22 | `LBNCDR.LOT.DEPT.CODE` | `LbncdrLoanType_DeptCode` | String |  |  |
| 23 | `LBNCDR.LOT.AUDITOR.CODE` | `LbncdrLoanType_AuditorCode` | String |  |  |
| 24 | `LBNCDR.LOT.AUDIT.DATE.TIME` | `LbncdrLoanType_AuditDateTime` | String |  |  |
