# SAFECUSTODY.EXTRACT.POSTED — Table Schema

> Source: `INSERTS/I_F.SAFECUSTODY.EXTRACT.POSTED` in `AM_Fees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.EP.CUSTOMER` | `SafecustodyExtractPosted_Customer` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 2 | `SC.EP.DEPOSITORY` | `SafecustodyExtractPosted_Depository` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 3 | `SC.EP.SECURITY.CODE` | `SafecustodyExtractPosted_SecurityCode` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 4 | `SC.EP.PRICE.CURRENCY` | `SafecustodyExtractPosted_PriceCurrency` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 5 | `SC.EP.ACT.CLOSING.NOM` | `SafecustodyExtractPosted_ActClosingNom` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 6 | `SC.EP.ACT.CL.NOM.LCY` | `SafecustodyExtractPosted_ActClNomLcy` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 7 | `SC.EP.MARKET.PRICE` | `SafecustodyExtractPosted_MarketPrice` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 8 | `SC.EP.PRICE.CCY.XRATE` | `SafecustodyExtractPosted_PriceCcyXrate` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 9 | `SC.EP.ACT.MRKT.VAL.LCY` | `SafecustodyExtractPosted_ActMrktValLcy` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 10 | `SC.EP.EXT.DATE` | `SafecustodyExtractPosted_ExtDate` |  |  |  |
| 11 | `SC.EP.MARKET.VAL.LCY` | `SafecustodyExtractPosted_MarketValLcy` |  |  |  |
| 12 | `SC.EP.CLOSING.NOM.LCY` | `SafecustodyExtractPosted_ClosingNomLcy` |  |  |  |
| 13 | `SC.EP.CL.NOM.IN.LCY` | `SafecustodyExtractPosted_ClNomInLcy` |  |  |  |
| 14 | `SC.EP.AVG.CLOSING.NOM` | `SafecustodyExtractPosted_AvgClosingNom` |  |  |  |
| 15 | `SC.EP.AVG.CL.NOM.LCY` | `SafecustodyExtractPosted_AvgClNomLcy` |  |  |  |
| 16 | `SC.EP.AVG.AST.BAL.LCY` | `SafecustodyExtractPosted_AvgAstBalLcy` |  |  |  |
| 17 | `SC.EP.MARKET.VAL.SCY` | `SafecustodyExtractPosted_MarketValScy` |  |  |  |
| 18 | `SC.EP.AVG.AST.BAL.SCY` | `SafecustodyExtractPosted_AvgAstBalScy` |  |  |  |
| 19 | `SC.EP.TOT.EST.FEE.LCY` | `SafecustodyExtractPosted_TotEstFeeLcy` |  |  |  |
| 20 | `SC.EP.TOT.CHRGD.AMT.LCY` | `SafecustodyExtractPosted_TotChrgdAmtLcy` |  |  |  |
| 21 | `SC.EP.PL.RECOG.SAFE.LCY` | `SafecustodyExtractPosted_PlRecogSafeLcy` |  |  |  |
| 22 | `SC.EP.MV.RES.5` | `SafecustodyExtractPosted_MvRes5` |  |  |  |
| 23 | `SC.EP.MV.RES.4` | `SafecustodyExtractPosted_MvRes4` |  |  |  |
| 24 | `SC.EP.MV.RES.3` | `SafecustodyExtractPosted_MvRes3` |  |  |  |
| 25 | `SC.EP.MV.RES.2` | `SafecustodyExtractPosted_MvRes2` |  |  |  |
| 26 | `SC.EP.MV.RES.1` | `SafecustodyExtractPosted_MvRes1` |  |  |  |
| 27 | `SC.EP.PORTFOLIO` | `SafecustodyExtractPosted_Portfolio` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 28 | `SC.EP.ACT.MRKT.VAL.SCY` | `SafecustodyExtractPosted_ActMrktValScy` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 29 | `SC.EP.SECURITY.CCY` | `SafecustodyExtractPosted_SecurityCcy` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 30 | `SC.EP.PRODUCT` | `SafecustodyExtractPosted_Product` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 31 | `SC.EP.RESERVED.6` | `SafecustodyExtractPosted_Reserved6` | TField |  |  |
| 32 | `SC.EP.RESERVED.5` | `SafecustodyExtractPosted_Reserved5` | TField |  |  |
| 33 | `SC.EP.RESERVED.4` | `SafecustodyExtractPosted_Reserved4` | TField |  |  |
| 34 | `SC.EP.RESERVED.3` | `SafecustodyExtractPosted_Reserved3` | TField |  |  |
| 35 | `SC.EP.RESERVED.2` | `SafecustodyExtractPosted_Reserved2` | TField |  |  |
| 36 | `SC.EP.RESERVED.1` | `SafecustodyExtractPosted_Reserved1` | TField |  |  |
| 37 | `SC.EP.LOCAL.REF` | `SafecustodyExtractPosted_LocalRef` |  |  |  |
