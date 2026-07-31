# LBNCDR.EXTRACT.MAPPING — Table Schema

> Source: `INSERTS/I_F.LBNCDR.EXTRACT.MAPPING` in `LBNCDR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LBNCDR.MAP.LOAN.TYPE` | `LbncdrExtractMapping_LoanType` | TField |  | Holds the valid record ID from the Liability Group SGL.H.CDR.LOAN.TYPE Validation Rules 2 N |
| 2 | `LBNCDR.MAP.LIAB.GRP` | `LbncdrExtractMapping_LiabGrp` | TField |  | Holds the valid record ID from the Liability Group SGL.H.CDR.LIAB.GROUP Validation Rules 2 N |
| 3 | `LBNCDR.MAP.LIAB.SUB.GRP` | `LbncdrExtractMapping_LiabSubGrp` | TField |  | Holds the valid record ID from the Liability Sub Group SGL.H.CDR.LIAB.SUB.GROUP Validation Rules 2 N |
| 4 | `LBNCDR.MAP.LIAB.TYPE.NO.COLL` | `LbncdrExtractMapping_LiabTypeNoColl` | TField |  | Holds the drop down from the table SGL.LIAB.TYPES and should show the short description and description fields alone. The version for amending this table should always default the LIAB.TYPE.NO.COLL value as ABL if there is no existing value in it. Validation Rules 3 A |
| 5 | `LBNCDR.MAP.LAWR.CHG.LOAN.TYPE` | `LbncdrExtractMapping_LawrChgLoanType` | TField |  |  |
| 6 | `LBNCDR.MAP.PRODUCT.ID` | `LbncdrExtractMapping_ProductId` | TField |  |  |
| 7 | `LBNCDR.MAP.PRD.LOAN.TYPE` | `LbncdrExtractMapping_PrdLoanType` | TField |  |  |
| 8 | `LBNCDR.MAP.CONT.LOAN.TYPE` | `LbncdrExtractMapping_ContLoanType` | TField |  |  |
| 9 | `LBNCDR.MAP.DEF.LOAN.TYPE` | `LbncdrExtractMapping_DefLoanType` | TField |  |  |
| 10 | `LBNCDR.MAP.RESERVED.10` | `LbncdrExtractMapping_Reserved10` | TField |  |  |
| 11 | `LBNCDR.MAP.RESERVED.9` | `LbncdrExtractMapping_Reserved9` | TField |  |  |
| 12 | `LBNCDR.MAP.RESERVED.8` | `LbncdrExtractMapping_Reserved8` | TField |  |  |
| 13 | `LBNCDR.MAP.RESERVED.7` | `LbncdrExtractMapping_Reserved7` | TField |  |  |
| 14 | `LBNCDR.MAP.RESERVED.6` | `LbncdrExtractMapping_Reserved6` | TField |  |  |
| 15 | `LBNCDR.MAP.RESERVED.5` | `LbncdrExtractMapping_Reserved5` | TField |  |  |
| 16 | `LBNCDR.MAP.RESERVED.4` | `LbncdrExtractMapping_Reserved4` | TField |  |  |
| 17 | `LBNCDR.MAP.RESERVED.3` | `LbncdrExtractMapping_Reserved3` | TField |  |  |
| 18 | `LBNCDR.MAP.RESERVED.2` | `LbncdrExtractMapping_Reserved2` | TField |  |  |
| 19 | `LBNCDR.MAP.RESERVED.1` | `LbncdrExtractMapping_Reserved1` | TField |  |  |
| 20 | `LBNCDR.MAP.LOCAL.REF` | `LbncdrExtractMapping_LocalRef` |  |  |  |
| 21 | `LBNCDR.MAP.OVERRIDE` | `LbncdrExtractMapping_Override` |  |  |  |
| 22 | `LBNCDR.MAP.RECORD.STATUS` | `LbncdrExtractMapping_RecordStatus` | String |  |  |
| 23 | `LBNCDR.MAP.CURR.NO` | `LbncdrExtractMapping_CurrNo` | String |  |  |
| 24 | `LBNCDR.MAP.INPUTTER` | `LbncdrExtractMapping_Inputter` |  |  |  |
| 25 | `LBNCDR.MAP.DATE.TIME` | `LbncdrExtractMapping_DateTime` |  |  |  |
| 26 | `LBNCDR.MAP.AUTHORISER` | `LbncdrExtractMapping_Authoriser` | String |  |  |
| 27 | `LBNCDR.MAP.CO.CODE` | `LbncdrExtractMapping_CoCode` | String |  |  |
| 28 | `LBNCDR.MAP.DEPT.CODE` | `LbncdrExtractMapping_DeptCode` | String |  |  |
| 29 | `LBNCDR.MAP.AUDITOR.CODE` | `LbncdrExtractMapping_AuditorCode` | String |  |  |
| 30 | `LBNCDR.MAP.AUDIT.DATE.TIME` | `LbncdrExtractMapping_AuditDateTime` | String |  |  |
