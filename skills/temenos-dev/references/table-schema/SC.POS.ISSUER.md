# SC.POS.ISSUER — Table Schema

> Source: `INSERTS/I_F.SC.POS.ISSUER` in `SC_ScvValuationUpdates.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SPI.ISSUER` | `ScPosIssuer_Issuer` |  |  |  |
| 2 | `SC.SPI.MARGIN.VALUE` | `ScPosIssuer_MarginValue` |  |  |  |
| 3 | `SC.SPI.ESTIMATION` | `ScPosIssuer_Estimation` |  |  |  |
| 4 | `SC.SPI.APPROVED` | `ScPosIssuer_Approved` |  |  |  |
| 5 | `SC.SPI.SC.POS.ASSET` | `ScPosIssuer_ScPosAsset` |  |  |  |
| 6 | `SC.SPI.SECURITY.NO` | `ScPosIssuer_SecurityNo` |  |  |  |
| 7 | `SC.SPI.MV.MARGIN.AMT` | `ScPosIssuer_MvMarginAmt` |  |  |  |
| 8 | `SC.SPI.EQ.MARGIN.AMT` | `ScPosIssuer_EqMarginAmt` |  |  |  |
| 9 | `SC.SPI.EXCEPTION` | `ScPosIssuer_Exception` |  |  |  |
| 10 | `SC.SPI.INDEX` | `ScPosIssuer_Index` |  |  |  |
| 11 | `SC.SPI.ADJ.MARGIN.VALUE` | `ScPosIssuer_AdjMarginValue` | TField |  | This will be same as MARGIN.VALUE field in SEC.ACC.MASTER. |
| 12 | `SC.SPI.ADJ.ESTIMATION` | `ScPosIssuer_AdjEstimation` | TField |  | This will be same as VALUATION.AMT field in SEC.ACC.MASTER. |
| 13 | `SC.SPI.RESERVED.1` | `ScPosIssuer_Reserved1` | TField |  |  |
| 14 | `SC.SPI.RESERVED.2` | `ScPosIssuer_Reserved2` | TField |  |  |
| 15 | `SC.SPI.RESERVED.3` | `ScPosIssuer_Reserved3` | TField |  |  |
| 16 | `SC.SPI.RESERVED.4` | `ScPosIssuer_Reserved4` | TField |  |  |
| 17 | `SC.SPI.RESERVED.5` | `ScPosIssuer_Reserved5` | TField |  |  |
| 18 | `SC.SPI.RESERVED.6` | `ScPosIssuer_Reserved6` | TField |  |  |
| 19 | `SC.SPI.RESERVED.7` | `ScPosIssuer_Reserved7` | TField |  |  |
| 20 | `SC.SPI.RESERVED.8` | `ScPosIssuer_Reserved8` | TField |  |  |
| 21 | `SC.SPI.RESERVED.9` | `ScPosIssuer_Reserved9` | TField |  |  |
| 22 | `SC.SPI.RESERVED.10` | `ScPosIssuer_Reserved10` | TField |  |  |
| 23 | `SC.SPI.LOCAL.REF` | `ScPosIssuer_LocalRef` |  |  |  |
