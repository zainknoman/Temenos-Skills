# CAPL.CONTR.DEAL.RECEIPTS — Table Schema

> Source: `INSERTS/I_F.CAPL.CONTR.DEAL.RECEIPTS` in `CADEPO_CRAReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.DEAL.ISSUER.NAME` | `CaplContrDealReceipts_IssuerName` |  |  |  |
| 2 | `CAPL.DEAL.SPECIMEN.NO` | `CaplContrDealReceipts_SpecimenNo` |  |  |  |
| 3 | `CAPL.DEAL.ANNT.SIN.NO` | `CaplContrDealReceipts_AnntSinNo` |  |  |  |
| 4 | `CAPL.DEAL.AMT.SECOND.PERIOD` | `CaplContrDealReceipts_AmtSecondPeriod` |  |  |  |
| 5 | `CAPL.DEAL.AMT.FIRST.PER` | `CaplContrDealReceipts_AmtFirstPer` |  |  |  |
| 6 | `CAPL.DEAL.CONTR.YEAR` | `CaplContrDealReceipts_ContrYear` |  |  |  |
| 7 | `CAPL.DEAL.ANNT.NAME` | `CaplContrDealReceipts_AnntName` |  |  |  |
| 8 | `CAPL.DEAL.ADDRESS` | `CaplContrDealReceipts_Address` |  |  |  |
| 9 | `CAPL.DEAL.STREET` | `CaplContrDealReceipts_Street` |  |  |  |
| 10 | `CAPL.DEAL.TOWN` | `CaplContrDealReceipts_Town` |  |  |  |
| 11 | `CAPL.DEAL.POST.CODE` | `CaplContrDealReceipts_PostCode` |  |  |  |
| 12 | `CAPL.DEAL.COUNTRY` | `CaplContrDealReceipts_Country` |  |  |  |
| 13 | `CAPL.DEAL.CON.NAME` | `CaplContrDealReceipts_ConName` |  |  |  |
| 14 | `CAPL.DEAL.CON.SIN.NO` | `CaplContrDealReceipts_ConSinNo` |  |  |  |
| 15 | `CAPL.DEAL.RECEIPT.NO` | `CaplContrDealReceipts_ReceiptNo` |  |  |  |
| 16 | `CAPL.DEAL.RECEIPT.STATUS` | `CaplContrDealReceipts_ReceiptStatus` |  |  |  |
| 17 | `CAPL.DEAL.CONTRACT.NO` | `CaplContrDealReceipts_ContractNo` |  |  |  |
| 18 | `CAPL.DEAL.RECORD.STATUS` | `CaplContrDealReceipts_RecordStatus` |  |  |  |
| 19 | `CAPL.DEAL.CURR.NO` | `CaplContrDealReceipts_CurrNo` |  |  |  |
| 20 | `CAPL.DEAL.INPUTTER` | `CaplContrDealReceipts_Inputter` |  |  |  |
| 21 | `CAPL.DEAL.DATE.TIME` | `CaplContrDealReceipts_DateTime` |  |  |  |
| 22 | `CAPL.DEAL.AUTHORISER` | `CaplContrDealReceipts_Authoriser` |  |  |  |
| 23 | `CAPL.DEAL.CO.CODE` | `CaplContrDealReceipts_CoCode` |  |  |  |
| 24 | `CAPL.DEAL.DEPT.CODE` | `CaplContrDealReceipts_DeptCode` |  |  |  |
| 25 | `CAPL.DEAL.AUDITOR.CODE` | `CaplContrDealReceipts_AuditorCode` |  |  |  |
| 26 | `CAPL.DEAL.AUDIT.DATE.TIME` | `CaplContrDealReceipts_AuditDateTime` |  |  |  |
