# PM.PARAMETER — Table Schema

> Source: `INSERTS/I_F.PM.PARAMETER` in `PM_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PM.PP.APPLN` | `PmParameter_Appln` |  |  |  |
| 2 | `PM.PP.PROC.CODE` | `PmParameter_ProcCode` |  |  |  |
| 3 | `PM.PP.APPLN.INC` | `PmParameter_ApplnInc` |  |  |  |
| 4 | `PM.PP.COL` | `PmParameter_Col` | TField |  | For internal use only. Validation Rules: 2 Numeric Characters. Value = 22 |
| 5 | `PM.PP.FX.ROW` | `PmParameter_FxRow` | TField |  | For internal use only. Validation Rules: 1 - 3 numeric Characters Value = "50" |
| 6 | `PM.PP.FX.FOREX` | `PmParameter_FxForex` | TField |  | This field contains the position class that is associated with FX spot and Swap/Forward deals done under the rebate method. Validation Rules: 5 characters, type 'AA'. Must be a valid record on PM.POSN.CLASS. |
| 7 | `PM.PP.FX.SW` | `PmParameter_FxSw` | TField | No | This field contains the position CLASS that is associated wit Forex SW/FW deals that have REVALUATION type equal to "IN" or "SL" Validation Rules: 5, type 'AA'. (Optional) Must be a valid record on PM.POSN.CLASS. |
| 8 | `PM.PP.FX.INT.SW.ST` | `PmParameter_FxIntSwSt` | TField | No | This field contains the position CLASS that is associated with FX Swap deals that have REVALUATION type of 'SL' or 'IN'. It represents the position class for the start activity. This is the start activity POSN Class for FX interest swaps. Validation Rules: 5 characters, Type 'A'. (Optional) Must be a valid record on PM POSN CLASS. Must be present if FX.INT.SW.MAT.is present. |
| 9 | `PM.PP.FX.INT.SW.MAT` | `PmParameter_FxIntSwMat` | TField | No | This field contains the position CLASS that is associated with Forex SW/FW deals that have REVALUATION type of 'SL' or 'IN'. It represents the position class for the maturity activity. This is the start activity POSN CLASS for FX interest swaps. Validation Rules: 5 characters, Type 'AA'. (Optional) Must be a valid record on PM POSN CLASS. Must be present if FX.INT.SW.ST. is present. Must not be present if FX.INT.Sw.ST is not present. |
| 10 | `PM.PP.FX.PRIN.ST` | `PmParameter_FxPrinSt` | TField | No | This field contains the position class that is associated with Forex FW deals that have REVALUATION type of 'IH'. It represents the position class for the start activity. This activity is for the Notional Amounts involved in an FX deal at the associated Spot date. Validation Rules: 5 Characters, Type 'AA'. (Optional) |
| 11 | `PM.PP.FX.SW.PL.FWD.POS` | `PmParameter_FxSwPlFwdPos` | TField |  | This field contains the position class that is associated with FX Swap deals using 'SF' revaluation type. Validation Rules: 5 characters, type 'AA'. Must be a valid record on PM.POSN.CLASS. |
| 12 | `PM.PP.FX.CASH.HDG.INT` | `PmParameter_FxCashHdgInt` | TField |  | This field is obsolete at 14.2.0 This field contained the position class that is associated with Forex FW deals that have REVALUATION type of 'IH'. It represents the position class for the HEDGED Interest activity. Validation Rules: Obsolete |
| 13 | `PM.PP.FX.GAP.PRIN.ST` | `PmParameter_FxGapPrinSt` | TField |  | This field is obsolete at 14.2.0 This field contained the position class that is associated with Forex FW deals that have REVALUATION type of 'IH'. It represents the position class for the START activity to be used in the GAP analysis. Validation Rules: Obsolete |
| 14 | `PM.PP.FX.GAP.PRIN.MAT` | `PmParameter_FxGapPrinMat` | TField |  | This field is obsolete at 14.2.0 This field contained the position class that is associated with Forex FW deals that have REVALUATION type of 'IH'. It represents the position class for the MATURITY activity to be used in the GAP analysis. Validation Rules: Obsolete |
| 15 | `PM.PP.FX.ASST.LIAB` | `PmParameter_FxAsstLiab` | TField | Yes | This field contains the Position Class record that is associated with the Currrency Asset and Liability position. This field is required if Position Management is active and there are any currency positions in the T24 system. Validation Rules: 5 characters, type "AA". (Mandatory) |
| 16 | `PM.PP.FX.FWD.INT.COVER` | `PmParameter_FxFwdIntCover` | TField |  | This field contains the position class that is associated with FX Forward Interest Cover deals. Validation Rules: 5 characters, type 'AA'. Must be a valid record on PM.POSN.CLASS. |
| 17 | `PM.PP.FX.OPT.AVAIL.CLS` | `PmParameter_FxOptAvailCls` | TField |  | PM Class for the unused element of FOREX multi-option deal. Validation Rules: 5 Characters of the type 'AA' Must exist on the PM.POSN.CLASS file |
| 18 | `PM.PP.MM.ROW` | `PmParameter_MmRow` | TField |  | For internal use only. Validation Rules: 1 - 3 numeric characters. Value "50" |
| 19 | `PM.PP.LMM.DEP.CAT` | `PmParameter_LmmDepCat` |  |  |  |
| 20 | `PM.PP.LMM.LOAN.CAT` | `PmParameter_LmmLoanCat` |  |  |  |
| 21 | `PM.PP.LMM.ONITE.GAP.ST` | `PmParameter_LmmOniteGapSt` | TField |  | This field contains the start POSN CLASS for Overnight (one day) money. 1. This is the POSN CLASS for the start activity. 2. If this is specified, for any one day money, it takes precedence over the position class defined in LMM GAP ST. Validation Rules: |
| 22 | `PM.PP.LMM.ONITE.GAP.MAT` | `PmParameter_LmmOniteGapMat` | TField |  | This field contains the maturity POSN CLASS for Overnight (one day) money. 1. This is the POSN CLASS for the maturity activity. 2. If this is specified, for any one day money, it takes precedence over the position class defined in LMM GAP MAT. Validation Rules: |
| 23 | `PM.PP.LMM.ONITE.GM.SFX` | `PmParameter_LmmOniteGmSfx` | TField |  | This field contains the date suffix. 1. This field allows the system to generate one day money maturity activity. 2. If a period is set to 'ODM' in PM CALENDAR, this field should be set to the same corresponding DATE SFX. Validation Rules: 1 character, type ''. Must be either 0 or 2. |
| 24 | `PM.PP.LMM.CAT` | `PmParameter_LmmCat` |  |  |  |
| 25 | `PM.PP.LMM.GAP.ST` | `PmParameter_LmmGapSt` |  |  |  |
| 26 | `PM.PP.LMM.GAP.MAT` | `PmParameter_LmmGapMat` |  |  |  |
| 27 | `PM.PP.LMM.GM.DATE.SFX` | `PmParameter_LmmGmDateSfx` |  |  |  |
| 28 | `PM.PP.LMM.INTEREST` | `PmParameter_LmmInterest` | TField | No | This field contains the Position Class assigned to Interest Maturity Activity on Money Market transactions. Validation Rules: 5 characters, type "A" (optional). |
| 29 | `PM.PP.LMM.R2` | `PmParameter_LmmR2` | TField |  | This field is reserved for future use. Validation Rules: No input. |
| 30 | `PM.PP.LMM.R3` | `PmParameter_LmmR3` | TField |  | This field is reserved for future use. Validation Rules: No input. |
| 31 | `PM.PP.ENQ.NEG.SIGN` | `PmParameter_EnqNegSign` | TField | Yes | Validation Rules: Mandatory input. A maximum of 12 characters may be entered. The following values are permitted: PLACINGS TAKINGS |
| 32 | `PM.PP.HVL.APP` | `PmParameter_HvlApp` |  |  |  |
| 33 | `PM.PP.PM.FX.SYNTH.RTN` | `PmParameter_R9` |  |  |  |
| 34 | `PM.PP.FRA.LONG.RATE` | `PmParameter_R8` |  |  |  |
| 35 | `PM.UPD.PDPCWF.FOR` | `PmParameter_UpdPdpcwfFor` |  |  |  |
| 36 | `PM.PP.R6` | `PmParameter_R6` | TField |  | This field is reserved for future use. Validation Rules: No input. |
| 37 | `PM.PP.R5` | `PmParameter_R5` | TField |  | This field is reserved for future use. Validation Rules: No input. |
| 38 | `PM.PP.R4` | `PmParameter_R4` | TField |  | This field is reserved for future use. Validation Rules: No input. |
| 39 | `PM.PP.R3` | `PmParameter_R3` | TField |  | This field is reserved for future use. Validation Rules: No input. |
| 40 | `PM.PP.R2` | `PmParameter_R2` | TField |  | This field is reserved for future use. Validation Rules: No input. |
| 41 | `PM.PP.R1` | `PmParameter_R1` | TField |  | This field is reserved for future use. Validation Rules: No input. |
| 42 | `PM.PP.R0` | `PmParameter_R0` | TField |  | This field is reserved for future use. Validation Rules: No input. |
| 43 | `PM.PP.FRA.TRADE.GAP` | `PmParameter_FraTradeGap` | TField |  | This field indicates whether GAP activies are generated for TRADE type FRA deals. GAP activites are always generated for HEDGE type trades. Validation Rules: YES indicates that GAP activities are generated for TRADE type deals, NO or blank indicates that GAP activities are not generated. |
| 44 | `PM.PP.FX.NDF` | `PmParameter_FxNdf` | TField |  | The PM.POSN.CLASS used to identify Negotiated Deal activities. Validation Rules: 5 Characters of the type 'AA' Must exist on the PM.POSN.CLASS file |
| 45 | `PM.PP.BUILD.LCY.POSN` | `PmParameter_BuildLcyPosn` | TField |  | Introduced in Release G14.1 Specifies whether a FXP Position needs to be generated in PM.TRAN.ACTIVITY for the Local Currency, when a transaction involving a Foreign Currency and a Local Currency is input in the Applications FT, TT and DC. If this parameter is set to YES, data related to FXP Position class FTFFT or TTFXP (depending on the Parameterization in PM.PC.PARAM) would be respectively updated in PM.TRAN.ACTIVITY, for Local Currency movement also, when a Transaction involving a Foreign and Local Currency is input in the Applications FT and TT. If this parameter is set to YES, data related to FXP Position class DCFDC (depending on the Parameterization in PM.PC.PARAM) would be updated in PM.TRAN.ACTIVITY for Local Currency movement also, when a Foreign Currency Transaction is input in the Application DC. In this parameter is set to NO or Null, then in the above specified cases the FXP type Position class data would be generated only for Foreign Currency movement. Validation Rules: Valid values are YES, NO or Null. NO and Null are equivalent. |
| 46 | `PM.PP.ZERO.INT.RATE` | `PmParameter_ZeroIntRate` | TField |  | Introduced in G14.1. Specifies whether contracts with Zero interest rates need to be updated in PM.DLY.POSN.CLASS GAP position records in the Sub-value 10 fields. If this field is Null or NO, then contracts with Zero interest rates would not be updated in PM.DLY.POSN.CLASS GAP position records in the Sub-value 10 fields, and consequently they would not be reported in PM.GAP enquiry, which is the functionality before the T24 release G14.1. On the other hand, if this field is set to YES, then then contracts with Zero interest rates would be updated in PM.DLY.POSN.CLASS GAP position records in the Sub-value 10 fields, and consequently they would be reported in PM.GAP enquiry. Example 1: PM.PARAMETER: ZERO.INT.RATE:YES MM0235700101: PRINCIPAL: USD 1,000,000, INTEREST.RATE: 0, MATURITY DATE: 20031223 MM0235700102: PRINCIPAL: USD 2,000,000, INTEREST.RATE: 10, MATURITY DATE: 20031223 BNK Example 2: PM.PARAMETER: ZERO.INT.RATE:NO or NULL. MM0235700301: PRINCIPAL: EUR 1,000,000, INTEREST.RATE: 0, MATURITY DATE: 20031223 MM0235700302: PRINCIPAL: EUR 2,000,000, INTEREST.RATE: 10, MATURITY DATE: 20031223 BNK Validation Rules: Valid values are YES, NO or Null. |
| 47 | `PM.PP.RESERVED.1` | `PmParameter_Reserved1` | TField |  |  |
| 48 | `PM.PP.RECORD.STATUS` | `PmParameter_RecordStatus` | String |  |  |
| 49 | `PM.PP.CURR.NO` | `PmParameter_CurrNo` | String |  |  |
| 50 | `PM.PP.INPUTTER` | `PmParameter_Inputter` |  |  |  |
| 51 | `PM.PP.DATE.TIME` | `PmParameter_DateTime` |  |  |  |
| 52 | `PM.PP.AUTHORISER` | `PmParameter_Authoriser` | String |  |  |
| 53 | `PM.PP.CO.CODE` | `PmParameter_CoCode` | String |  |  |
| 54 | `PM.PP.DEPT.CODE` | `PmParameter_DeptCode` | String |  |  |
| 55 | `PM.PP.AUDITOR.CODE` | `PmParameter_AuditorCode` | String |  |  |
| 56 | `PM.PP.AUDIT.DATE.TIME` | `PmParameter_AuditDateTime` | String |  |  |
