# CONSOL.UPDATE.WORK — Table Schema

> Source: `INSERTS/I_F.CONSOL.UPDATE.WORK` in `AC_EntryCreation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RE.CUW.CURRENCY` | `ConsolUpdateWork_Currency` | TField |  | Currency of the record. |
| 2 | `RE.CUW.MAT.DATE` | `ConsolUpdateWork_MatDate` |  |  |  |
| 3 | `RE.CUW.CREDIT.MVMT` | `ConsolUpdateWork_CreditMvmt` |  |  |  |
| 4 | `RE.CUW.CREDIT.LCY.MVMT` | `ConsolUpdateWork_CreditLcyMvmt` |  |  |  |
| 5 | `RE.CUW.DEBIT.MVMT` | `ConsolUpdateWork_DebitMvmt` |  |  |  |
| 6 | `RE.CUW.DEBIT.LCY.MVMT` | `ConsolUpdateWork_DebitLcyMvmt` |  |  |  |
| 7 | `RE.CUW.SCHD.AMOUNT` | `ConsolUpdateWork_SchdAmount` |  |  |  |
| 8 | `RE.CUW.ASSET.TYPE` | `ConsolUpdateWork_AssetType` |  |  |  |
| 9 | `RE.CUW.ASST.MAT.DATE` | `ConsolUpdateWork_AsstMatDate` |  |  |  |
| 10 | `RE.CUW.ASST.SCHD.AMOUNT` | `ConsolUpdateWork_AsstSchdAmount` |  |  |  |
| 11 | `RE.CUW.ASST.CREDIT.MVMT` | `ConsolUpdateWork_AsstCreditMvmt` |  |  |  |
| 12 | `RE.CUW.ASST.CREDIT.LCY.MVMT` | `ConsolUpdateWork_AsstCreditLcyMvmt` |  |  |  |
| 13 | `RE.CUW.ASST.DEBIT.MVMT` | `ConsolUpdateWork_AsstDebitMvmt` |  |  |  |
| 14 | `RE.CUW.ASST.DEBIT.LCY.MVMT` | `ConsolUpdateWork_AsstDebitLcyMvmt` |  |  |  |
