# SAFECUSTODY.EXTRACT — Table Schema

> Source: `INSERTS/I_F.SAFECUSTODY.EXTRACT` in `SC_ScfSafekeepingFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.CBL.CUSTOMER` | `SafecustodyExtract_Customer` | TField |  | Customer code |
| 2 | `SC.CBL.DEPOSITORY` | `SafecustodyExtract_Depository` | TField |  | Depository |
| 3 | `SC.CBL.SECURITY.CODE` | `SafecustodyExtract_SecurityCode` | TField |  | Security code or asset id |
| 4 | `SC.CBL.PRICE.CURRENCY` | `SafecustodyExtract_PriceCurrency` | TField |  | Standard T24 currency field. Validation Rules: A maximum of 15 characters may be entered. This is a NOINPUT field. Must be the key to a valid entry on the CURRENCY file. |
| 5 | `SC.CBL.ACT.CLOSING.NOM` | `SafecustodyExtract_ActClosingNom` | TField |  | Standard T24 amount field. Validation Rules: This is a NOINPUT field. Calculated automatically During the calculation of Safecustody Fees this field is referenced for the following AVERAGE.CLOSING-BASE.CODEmethod: CLOSING-NOMINAL. |
| 6 | `SC.CBL.ACT.CL.NOM.LCY` | `SafecustodyExtract_ActClNomLcy` | TField |  | Closing nominal, local currency. During the calculation of Safecustody Fees this field is referenced for the following AVERAGE.CLOSING-BASE.CODEmethod: CLOSING-NOMINAL.LCY. |
| 7 | `SC.CBL.MARKET.PRICE` | `SafecustodyExtract_MarketPrice` | TField |  | Validation Rules: This is a NOINPUT field. Calculated automatically |
| 8 | `SC.CBL.PRICE.CCY.XRATE` | `SafecustodyExtract_PriceCcyXrate` | TField |  | Standard T24 rate field. Validation Rules: This is a NOINPUT field. Calculated automatically |
| 9 | `SC.CBL.ACT.MRKT.VAL.LCY` | `SafecustodyExtract_ActMrktValLcy` | TField |  | Validation Rules: This is a NOINPUT field. Calculated automatically. During the calculation of Safecustody Fees this field is referenced for the following AVERAGE.CLOSING-BASE.CODEmethod: CLOSING-VALUE. |
| 10 | `SC.CBL.EXT.DATE` | `SafecustodyExtract_ExtDate` |  |  |  |
| 11 | `SC.CBL.MARKET.VAL.LCY` | `SafecustodyExtract_MarketValLcy` |  |  |  |
| 12 | `SC.CBL.CLOSING.NOM.LCY` | `SafecustodyExtract_ClosingNomLcy` |  |  |  |
| 13 | `SC.CBL.CL.NOM.IN.LCY` | `SafecustodyExtract_ClNomInLcy` |  |  |  |
| 14 | `SC.CBL.AVG.CLOSING.NOM` | `SafecustodyExtract_AvgClosingNom` |  |  |  |
| 15 | `SC.CBL.AVG.CL.NOM.LCY` | `SafecustodyExtract_AvgClNomLcy` |  |  |  |
| 16 | `SC.CBL.AVG.AST.BAL.LCY` | `SafecustodyExtract_AvgAstBalLcy` |  |  |  |
| 17 | `SC.CBL.MARKET.VAL.SCY` | `SafecustodyExtract_MarketValScy` |  |  |  |
| 18 | `SC.CBL.AVG.AST.BAL.SCY` | `SafecustodyExtract_AvgAstBalScy` |  |  |  |
| 19 | `SC.CBL.TOT.EST.FEE.LCY` | `SafecustodyExtract_TotEstFeeLcy` |  |  |  |
| 20 | `SC.CBL.TOT.CHRGD.AMT.LCY` | `SafecustodyExtract_TotChrgdAmtLcy` |  |  |  |
| 21 | `SC.CBL.PL.RECOG.SAFE.LCY` | `SafecustodyExtract_PlRecogSafeLcy` |  |  |  |
| 22 | `SC.CBL.MV.RES.5` | `SafecustodyExtract_MvRes5` |  |  |  |
| 23 | `SC.CBL.MV.RES.4` | `SafecustodyExtract_MvRes4` |  |  |  |
| 24 | `SC.CBL.MV.RES.3` | `SafecustodyExtract_MvRes3` |  |  |  |
| 25 | `SC.CBL.MV.RES.2` | `SafecustodyExtract_MvRes2` |  |  |  |
| 26 | `SC.CBL.MV.RES.1` | `SafecustodyExtract_MvRes1` |  |  |  |
| 27 | `SC.CBL.PORTFOLIO` | `SafecustodyExtract_Portfolio` | TField |  | Portfolio |
| 28 | `SC.CBL.ACT.MRKT.VAL.SCY` | `SafecustodyExtract_ActMrktValScy` | TField |  | Actual market value, security currency |
| 29 | `SC.CBL.SECURITY.CCY` | `SafecustodyExtract_SecurityCcy` | TField |  | security currency, for securities data this will be security currency, for other assets this will be taken fromthe associated SC.POS.ASSET record. |
| 30 | `SC.CBL.PRODUCT` | `SafecustodyExtract_Product` | TField |  | Product to which the asset belongs, for securities data this will be SC, for other assets this will be taken fromthe associated SC.POS.ASSET record. |
| 31 | `SC.CBL.RESERVED.6` | `SafecustodyExtract_Reserved6` | TField |  |  |
| 32 | `SC.CBL.RESERVED.5` | `SafecustodyExtract_Reserved5` | TField |  |  |
| 33 | `SC.CBL.RESERVED.4` | `SafecustodyExtract_Reserved4` | TField |  |  |
| 34 | `SC.CBL.RESERVED.3` | `SafecustodyExtract_Reserved3` | TField |  |  |
| 35 | `SC.CBL.RESERVED.2` | `SafecustodyExtract_Reserved2` | TField |  |  |
| 36 | `SC.CBL.RESERVED.1` | `SafecustodyExtract_Reserved1` | TField |  |  |
| 37 | `SC.CBL.LOCAL.REF` | `SafecustodyExtract_LocalRef` |  |  |  |
| 38 | `SC.CBL.RECORD.STATUS` | `SafecustodyExtract_RecordStatus` | String |  |  |
| 39 | `SC.CBL.CURR.NO` | `SafecustodyExtract_CurrNo` | String |  |  |
| 40 | `SC.CBL.INPUTTER` | `SafecustodyExtract_Inputter` |  |  |  |
| 41 | `SC.CBL.DATE.TIME` | `SafecustodyExtract_DateTime` |  |  |  |
| 42 | `SC.CBL.AUTHORISER` | `SafecustodyExtract_Authoriser` | String |  |  |
| 43 | `SC.CBL.CO.CODE` | `SafecustodyExtract_CoCode` | String |  |  |
| 44 | `SC.CBL.DEPT.CODE` | `SafecustodyExtract_DeptCode` | String |  |  |
| 45 | `SC.CBL.AUDITOR.CODE` | `SafecustodyExtract_AuditorCode` | String |  |  |
| 46 | `SC.CBL.AUDIT.DATE.TIME` | `SafecustodyExtract_AuditDateTime` | String |  |  |
