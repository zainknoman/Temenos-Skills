# SL.FAC.PROD.DETAILS — Table Schema

> Source: `INSERTS/I_F.SL.FAC.PROD.DETAILS` in `SL_Facility.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SFPD.CURRENCY` | `SlFacProdDetails_Currency` | TField |  | This holds the currency of the FACILITY contract |
| 2 | `SFPD.PROD.TYPE` | `SlFacProdDetails_ProdType` |  |  |  |
| 3 | `SFPD.PROD.OUTS.AMT` | `SlFacProdDetails_ProdOutsAmt` |  |  |  |
| 4 | `SFPD.PROD.TR.CODE` | `SlFacProdDetails_ProdTrCode` |  |  |  |
| 5 | `SFPD.PROD.TR.OUTS.AMT` | `SlFacProdDetails_ProdTrOutsAmt` |  |  |  |
| 6 | `SFPD.PROD.TR.AMT.MVD` | `SlFacProdDetails_ProdTrAmtMvd` |  |  |  |
