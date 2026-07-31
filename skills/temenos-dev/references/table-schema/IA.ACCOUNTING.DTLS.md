# IA.ACCOUNTING.DTLS — Table Schema

> Source: `INSERTS/I_F.IA.ACCOUNTING.DTLS` in `IA_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IA.ACDT.EB.CASHFLOW.VERN` | `IaAccountingDtls_EbCashflowVern` |  |  |  |
| 2 | `IA.ACDT.ACCOUNTING.MTD` | `IaAccountingDtls_AccountingMtd` |  |  |  |
| 3 | `IA.ACDT.TOTAL.ACCRUAL` | `IaAccountingDtls_TotalAccrual` |  |  |  |
| 4 | `IA.ACDT.CONTRACT.POST.AMT` | `IaAccountingDtls_ContractPostAmt` |  |  |  |
| 5 | `IA.ACDT.IAS.POSTING.AMT` | `IaAccountingDtls_IasPostingAmt` |  |  |  |
| 6 | `IA.ACDT.POSTING.AMT` | `IaAccountingDtls_PostingAmt` |  |  |  |
| 7 | `IA.ACDT.IA.POSTING.CAT` | `IaAccountingDtls_IaPostingCat` |  |  |  |
| 8 | `IA.ACDT.TRANS.CODE` | `IaAccountingDtls_TransCode` |  |  |  |
| 9 | `IA.ACDT.CONTRA.CAT` | `IaAccountingDtls_ContraCat` |  |  |  |
| 10 | `IA.ACDT.CONTRA.CODE` | `IaAccountingDtls_ContraCode` |  |  |  |
