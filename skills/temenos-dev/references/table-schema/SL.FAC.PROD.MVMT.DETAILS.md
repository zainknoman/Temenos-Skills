# SL.FAC.PROD.MVMT.DETAILS — Table Schema

> Source: `INSERTS/I_F.SL.FAC.PROD.MVMT.DETAILS` in `SL_Facility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SFPMD.CURRENCY` | `SlFacProdMvmtDetails_Currency` | TField |  | This holds the currency of the FACILITY contract |
| 2 | `SFPMD.PROD.TYPE` | `SlFacProdMvmtDetails_ProdType` |  |  |  |
| 3 | `SFPMD.PROD.TR.CODE` | `SlFacProdMvmtDetails_ProdTrCode` |  |  |  |
| 4 | `SFPMD.PROD.AMT.MOVED` | `SlFacProdMvmtDetails_ProdAmtMoved` |  |  |  |
| 5 | `SFPMD.PROD.MVMT.EFF.DATE` | `SlFacProdMvmtDetails_ProdMvmtEffDate` |  |  |  |
| 6 | `SFPMD.PROD.ID` | `SlFacProdMvmtDetails_ProdId` |  |  |  |
