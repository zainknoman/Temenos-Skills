# FS.GA.ACCOUNT.LINK — Table Schema

> Source: `INSERTS/I_F.FS.GA.ACCOUNT.LINK` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACCOUNT.LINK.VALUATION.MODEL` | `FsGaAccountLink_ValuationModel` | TField |  | Valuation model Multifonds DB Column is NESTI. |
| 2 | `ACCOUNT.LINK.ACCOUNT` | `FsGaAccountLink_Account` | TField |  | Account Multifonds DB Column is NCOMPTE. |
| 3 | `ACCOUNT.LINK.GROUP.CODE.DESCRIPTION` | `FsGaAccountLink_GroupCodeDescription` | TField |  | Group Code Description Multifonds DB Column is NGROUP. |
| 4 | `ACCOUNT.LINK.REPORTING.CODE` | `FsGaAccountLink_ReportingCode` | TField |  | Reporting code Multifonds DB Column is CODE_RAPPORT. |
| 5 | `ACCOUNT.LINK.CASH.CODE` | `FsGaAccountLink_CashCode` | TField |  | Cash code Multifonds DB Column is CODE_CASH. |
| 6 | `ACCOUNT.LINK.NUM.OF.DAYS` | `FsGaAccountLink_NumOfDays` | TField |  | Num of days Multifonds DB Column is NB_JOURS. |
| 7 | `ACCOUNT.LINK.PROCESSING.TREATMENT.TYPE` | `FsGaAccountLink_ProcessingTreatmentType` | TField |  | Processing Treatment type Multifonds DB Column is CTYP. |
| 8 | `ACCOUNT.LINK.SWISS.BANK.STATISTIC` | `FsGaAccountLink_SwissBankStatistic` | TField |  | Swiss bank statistic Multifonds DB Column is CTYP_TRT. |
| 9 | `ACCOUNT.LINK.AMOUNT.TYPE` | `FsGaAccountLink_AmountType` | TField |  | Amount type Multifonds DB Column is CTYP_AMOUNT. |
| 10 | `ACCOUNT.LINK.NEG.GROUP.CODE.DESCRIPTION` | `FsGaAccountLink_NegGroupCodeDescription` | TField |  | Neg Group Code Description Multifonds DB Column is NEG_NGROUP. |
| 11 | `ACCOUNT.LINK.RECORD.STATUS` | `FsGaAccountLink_RecordStatus` | String |  |  |
| 12 | `ACCOUNT.LINK.CURR.NO` | `FsGaAccountLink_CurrNo` | String |  |  |
| 13 | `ACCOUNT.LINK.INPUTTER` | `FsGaAccountLink_Inputter` |  |  |  |
| 14 | `ACCOUNT.LINK.DATE.TIME` | `FsGaAccountLink_DateTime` |  |  |  |
| 15 | `ACCOUNT.LINK.AUTHORISER` | `FsGaAccountLink_Authoriser` | String |  |  |
| 16 | `ACCOUNT.LINK.CO.CODE` | `FsGaAccountLink_CoCode` | String |  |  |
| 17 | `ACCOUNT.LINK.DEPT.CODE` | `FsGaAccountLink_DeptCode` | String |  |  |
| 18 | `ACCOUNT.LINK.AUDITOR.CODE` | `FsGaAccountLink_AuditorCode` | String |  |  |
| 19 | `ACCOUNT.LINK.AUDIT.DATE.TIME` | `FsGaAccountLink_AuditDateTime` | String |  |  |
