# ITREGE.PUMA.EXTRACTS — Table Schema

> Source: `INSERTS/I_F.ITREGE.PUMA.EXTRACTS` in `ITREGE_AgencyRevenue.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ITREGE.PUMA.EXT.PUMA.EXTRACT.TYPE` | `ItregePumaExtracts_PumaExtractType` | TField |  | Field to define the define extract type It is a lookup field with all the type puma extracts |
| 2 | `ITREGE.PUMA.EXT.FROM.DATE` | `ItregePumaExtracts_FromDate` | TField |  | Field to define the Date from which the records are to the extracted |
| 3 | `ITREGE.PUMA.EXT.TO.DATE` | `ItregePumaExtracts_ToDate` | TField |  | Field to define the Date To which the records are to be extracted |
| 4 | `ITREGE.PUMA.EXT.EXCLUDE.ACC.MOVMTS.PRODUCT` | `ItregePumaExtracts_ExcludeAccMovmtsProduct` |  |  |  |
| 5 | `ITREGE.PUMA.EXT.COMMISSION.TYPE.INCLUDED` | `ItregePumaExtracts_CommissionTypeIncluded` |  |  |  |
| 6 | `ITREGE.PUMA.EXT.INCOME.LOSS.MOVMT.TYPE` | `ItregePumaExtracts_IncomeLossMovmtType` |  |  |  |
| 7 | `ITREGE.PUMA.EXT.DEBIT.CREDIT.TXN.SIGN` | `ItregePumaExtracts_DebitCreditTxnSign` |  |  |  |
| 8 | `ITREGE.PUMA.EXT.DEBIT.CREDIT.MOVMT.TYPE` | `ItregePumaExtracts_DebitCreditMovmtType` |  |  |  |
| 9 | `ITREGE.PUMA.EXT.FEE.CODE` | `ItregePumaExtracts_FeeCode` |  |  |  |
| 10 | `ITREGE.PUMA.EXT.RESERVED.5` | `ItregePumaExtracts_Reserved5` | TField |  |  |
| 11 | `ITREGE.PUMA.EXT.RESERVED.4` | `ItregePumaExtracts_Reserved4` | TField |  |  |
| 12 | `ITREGE.PUMA.EXT.RESERVED.3` | `ItregePumaExtracts_Reserved3` | TField |  |  |
| 13 | `ITREGE.PUMA.EXT.RESERVED.2` | `ItregePumaExtracts_Reserved2` | TField |  |  |
| 14 | `ITREGE.PUMA.EXT.RESERVED.1` | `ItregePumaExtracts_Reserved1` | TField |  |  |
| 15 | `ITREGE.PUMA.EXT.OVERRIDE` | `ItregePumaExtracts_Override` |  |  |  |
| 16 | `ITREGE.PUMA.EXT.RECORD.STATUS` | `ItregePumaExtracts_RecordStatus` | String |  |  |
| 17 | `ITREGE.PUMA.EXT.CURR.NO` | `ItregePumaExtracts_CurrNo` | String |  |  |
| 18 | `ITREGE.PUMA.EXT.INPUTTER` | `ItregePumaExtracts_Inputter` |  |  |  |
| 19 | `ITREGE.PUMA.EXT.DATE.TIME` | `ItregePumaExtracts_DateTime` |  |  |  |
| 20 | `ITREGE.PUMA.EXT.AUTHORISER` | `ItregePumaExtracts_Authoriser` | String |  |  |
| 21 | `ITREGE.PUMA.EXT.CO.CODE` | `ItregePumaExtracts_CoCode` | String |  |  |
| 22 | `ITREGE.PUMA.EXT.DEPT.CODE` | `ItregePumaExtracts_DeptCode` | String |  |  |
| 23 | `ITREGE.PUMA.EXT.AUDITOR.CODE` | `ItregePumaExtracts_AuditorCode` | String |  |  |
| 24 | `ITREGE.PUMA.EXT.AUDIT.DATE.TIME` | `ItregePumaExtracts_AuditDateTime` | String |  |  |
