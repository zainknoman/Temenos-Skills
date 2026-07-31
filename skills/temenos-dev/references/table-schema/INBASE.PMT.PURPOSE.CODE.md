# INBASE.PMT.PURPOSE.CODE — Table Schema

> Source: `INSERTS/I_F.INBASE.PMT.PURPOSE.CODE` in `INBASE_CustomerValidations.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INBASE.PMT.PURCHASE.SALE.INDICATOR` | `InbasePmtPurposeCode_PurchaseSaleIndicator` | TField |  | Purpose Sale Indicator |
| 2 | `INBASE.PMT.DESCRIPTION` | `InbasePmtPurposeCode_Description` |  |  |  |
| 3 | `INBASE.PMT.GROUP.NO` | `InbasePmtPurposeCode_GroupNo` | TField |  | Group Number of the Purpose Code |
| 4 | `INBASE.PMT.PURPOSE.GROUP.NAME` | `InbasePmtPurposeCode_PurposeGroupName` |  |  |  |
| 5 | `INBASE.PMT.SECURITY.ADVICE.PRINTING` | `InbasePmtPurposeCode_SecurityAdvicePrinting` | TField |  | Determines if a security advise printing is needed for the particular purpose code |
| 6 | `INBASE.PMT.RESERVED.2` | `InbasePmtPurposeCode_Reserved2` | TField |  | Reserved for future purpose |
| 7 | `INBASE.PMT.RESERVED.1` | `InbasePmtPurposeCode_Reserved1` | TField |  | Reserved for future purpose |
| 8 | `INBASE.PMT.LOCAL.REF` | `InbasePmtPurposeCode_LocalRef` |  |  |  |
| 9 | `INBASE.PMT.OVERRIDE` | `InbasePmtPurposeCode_Override` |  |  |  |
| 10 | `INBASE.PMT.RECORD.STATUS` | `InbasePmtPurposeCode_RecordStatus` | String |  |  |
| 11 | `INBASE.PMT.CURR.NO` | `InbasePmtPurposeCode_CurrNo` | String |  |  |
| 12 | `INBASE.PMT.INPUTTER` | `InbasePmtPurposeCode_Inputter` |  |  |  |
| 13 | `INBASE.PMT.DATE.TIME` | `InbasePmtPurposeCode_DateTime` |  |  |  |
| 14 | `INBASE.PMT.AUTHORISER` | `InbasePmtPurposeCode_Authoriser` | String |  |  |
| 15 | `INBASE.PMT.CO.CODE` | `InbasePmtPurposeCode_CoCode` | String |  |  |
| 16 | `INBASE.PMT.DEPT.CODE` | `InbasePmtPurposeCode_DeptCode` | String |  |  |
| 17 | `INBASE.PMT.AUDITOR.CODE` | `InbasePmtPurposeCode_AuditorCode` | String |  |  |
| 18 | `INBASE.PMT.AUDIT.DATE.TIME` | `InbasePmtPurposeCode_AuditDateTime` | String |  |  |
