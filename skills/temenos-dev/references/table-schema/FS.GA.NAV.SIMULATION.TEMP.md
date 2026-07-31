# FS.GA.NAV.SIMULATION.TEMP — Table Schema

> Source: `INSERTS/I_F.FS.GA.NAV.SIMULATION.TEMP` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.NAV.SIMULATION.TEMP.PARENT.REF.ID` | `FsGaNavSimulationTemp_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.NAV.SIMULATION.TEMP.ORA.ROWID` | `FsGaNavSimulationTemp_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.NAV.SIMULATION.TEMP.FUND.ID` | `FsGaNavSimulationTemp_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.NAV.SIMULATION.TEMP.VALUATION.TYPE` | `FsGaNavSimulationTemp_ValuationType` | TField |  | Type of NAV like O for Official, U for Unofficial, I for Intraday etc Multifonds DB Column is TYP_TRT. |
| 5 | `FS.GA.NAV.SIMULATION.TEMP.CALCULATION.TYPE` | `FsGaNavSimulationTemp_CalculationType` | TField |  | Calulation Type Multifonds DB Column is TYP_CALC. |
| 6 | `FS.GA.NAV.SIMULATION.TEMP.DATE.OF.NAV` | `FsGaNavSimulationTemp_DateOfNav` | TField |  | Date of the NAV Multifonds DB Column is DATE_NAV. |
| 7 | `FS.GA.NAV.SIMULATION.TEMP.PROCESSING.DATE` | `FsGaNavSimulationTemp_ProcessingDate` | TField |  | Knowledge Date of the NAV Multifonds DB Column is DATE_TRT. |
| 8 | `FS.GA.NAV.SIMULATION.TEMP.TOTAL.QUANTITY.PART` | `FsGaNavSimulationTemp_TotalQuantityPart` | TField |  | Total Quantity Part Multifonds DB Column is QT_TOT_PART. |
| 9 | `FS.GA.NAV.SIMULATION.TEMP.TOT.BRUT.AMOUNT` | `FsGaNavSimulationTemp_TotBrutAmount` | TField |  | TOT Brut Amount Multifonds DB Column is MNT_BRUT_TOT. |
| 10 | `FS.GA.NAV.SIMULATION.TEMP.STT.BRUT.AMOUNT` | `FsGaNavSimulationTemp_SttBrutAmount` | TField |  | STT Brut Amount Multifonds DB Column is MNT_BRUT_STT. |
| 11 | `FS.GA.NAV.SIMULATION.TEMP.NET.MNT` | `FsGaNavSimulationTemp_NetMnt` | TField |  | Net Mnt Multifonds DB Column is MNT_NET. |
| 12 | `FS.GA.NAV.SIMULATION.TEMP.PORTFOLIO.AMOUNT` | `FsGaNavSimulationTemp_PortfolioAmount` | TField |  | Portfolio Amount Multifonds DB Column is MNT_PORFOLIO. |
| 13 | `FS.GA.NAV.SIMULATION.TEMP.MANA.NET.AMOUNT` | `FsGaNavSimulationTemp_ManaNetAmount` | TField |  | MANA Net Amount Multifonds DB Column is MNT_NET_MANA. |
| 14 | `FS.GA.NAV.SIMULATION.TEMP.NET.TAX1.AMOUNT` | `FsGaNavSimulationTemp_NetTax1Amount` | TField |  | Net Tax1 Amount Multifonds DB Column is MNT_NET_TAXE1. |
| 15 | `FS.GA.NAV.SIMULATION.TEMP.NET.TAX2.AMOUNT` | `FsGaNavSimulationTemp_NetTax2Amount` | TField |  | Net Tax2 Amount Multifonds DB Column is MNT_NET_TAXE2. |
| 16 | `FS.GA.NAV.SIMULATION.TEMP.NET.TAX3.AMOUNT` | `FsGaNavSimulationTemp_NetTax3Amount` | TField |  | Net Tax3 Amount Multifonds DB Column is MNT_NET_TAXE3. |
| 17 | `FS.GA.NAV.SIMULATION.TEMP.NET.TAX4.AMOUNT` | `FsGaNavSimulationTemp_NetTax4Amount` | TField |  | Net Tax4 Amount Multifonds DB Column is MNT_NET_TAXE4. |
| 18 | `FS.GA.NAV.SIMULATION.TEMP.NET.TAX5.AMOUNT` | `FsGaNavSimulationTemp_NetTax5Amount` | TField |  | Net Tax5 Amount Multifonds DB Column is MNT_NET_TAXE5. |
| 19 | `FS.GA.NAV.SIMULATION.TEMP.NET.TAX6.AMOUNT` | `FsGaNavSimulationTemp_NetTax6Amount` | TField |  | Net Tax6 Amount Multifonds DB Column is MNT_NET_TAXE6. |
| 20 | `FS.GA.NAV.SIMULATION.TEMP.NET.TAX7.AMOUNT` | `FsGaNavSimulationTemp_NetTax7Amount` | TField |  | Net Tax7 Amount Multifonds DB Column is MNT_NET_TAXE7. |
| 21 | `FS.GA.NAV.SIMULATION.TEMP.NET.TAX8.AMOUNT` | `FsGaNavSimulationTemp_NetTax8Amount` | TField |  | Net Tax8 Amount Multifonds DB Column is MNT_NET_TAXE8. |
| 22 | `FS.GA.NAV.SIMULATION.TEMP.BF.NAV.NUMBER` | `FsGaNavSimulationTemp_BfNavNumber` | TField |  | BF NAV Number Multifonds DB Column is NB_NAV_BF. |
| 23 | `FS.GA.NAV.SIMULATION.TEMP.AF.NAV.NUMBER` | `FsGaNavSimulationTemp_AfNavNumber` | TField |  | AF NAV Number Multifonds DB Column is NB_NAV_AF. |
| 24 | `FS.GA.NAV.SIMULATION.TEMP.COUNT.AMOUNT` | `FsGaNavSimulationTemp_CountAmount` | TField |  | Count Amount Multifonds DB Column is MNT_COUT. |
| 25 | `FS.GA.NAV.SIMULATION.TEMP.FUND.ENTRY.NUMBER` | `FsGaNavSimulationTemp_FundEntryNumber` | TField |  | Entry number of the fund Multifonds DB Column is NECRITUR_PTF. |
| 26 | `FS.GA.NAV.SIMULATION.TEMP.TRT.FIN.DATE` | `FsGaNavSimulationTemp_TrtFinDate` | TField |  | TRT FIN Date Multifonds DB Column is DATE_TRT_FIN. |
| 27 | `FS.GA.NAV.SIMULATION.TEMP.PRICE.DATE` | `FsGaNavSimulationTemp_PriceDate` | TField |  | Date of the Price or Ex rate used in NAV Multifonds DB Column is DATE_COURS. |
| 28 | `FS.GA.NAV.SIMULATION.TEMP.NAV.DATE.COURS` | `FsGaNavSimulationTemp_NavDateCours` | TField |  | NAV Date Cours Multifonds DB Column is DATE_COURS_NAV. |
| 29 | `FS.GA.NAV.SIMULATION.TEMP.VALUATION.METHOD` | `FsGaNavSimulationTemp_ValuationMethod` | TField |  | This field enable user to define a default valuation method by Fund / GTI / Process Multifonds DB Column is FCYELD. |
| 30 | `FS.GA.NAV.SIMULATION.TEMP.SIMULATION.YIELD` | `FsGaNavSimulationTemp_SimulationYield` | TField |  | Simulation Yield Multifonds DB Column is FCYELD_SIM. |
| 31 | `FS.GA.NAV.SIMULATION.TEMP.NET.SIMULATION.AMOUNT` | `FsGaNavSimulationTemp_NetSimulationAmount` | TField |  | Net Simulation Amount Multifonds DB Column is MNT_NET_SIM. |
| 32 | `FS.GA.NAV.SIMULATION.TEMP.CASH.AMOUNT` | `FsGaNavSimulationTemp_CashAmount` | TField |  | Cash Amount Multifonds DB Column is MNT_CASH. |
| 33 | `FS.GA.NAV.SIMULATION.TEMP.ACTIF.AMOUNT` | `FsGaNavSimulationTemp_ActifAmount` | TField |  | ACTIF Amount Multifonds DB Column is MNT_ACTIF. |
| 34 | `FS.GA.NAV.SIMULATION.TEMP.INTEREST.AMOUNT` | `FsGaNavSimulationTemp_InterestAmount` | TField |  | Interest Amount Multifonds DB Column is MNT_INT. |
| 35 | `FS.GA.NAV.SIMULATION.TEMP.TRT.EXP.TYPE` | `FsGaNavSimulationTemp_TrtExpType` | TField |  | TRT Exp Type Multifonds DB Column is TYP_TRT_EXP. |
| 36 | `FS.GA.NAV.SIMULATION.TEMP.AVERAGE.CASH.AMOUNT` | `FsGaNavSimulationTemp_AverageCashAmount` | TField |  | Average Cash Amount Multifonds DB Column is MNT_AVG_CASH. |
| 37 | `FS.GA.NAV.SIMULATION.TEMP.AVERAGE.ACTIF.AMOUNT` | `FsGaNavSimulationTemp_AverageActifAmount` | TField |  | Average ACTIF Ammount Multifonds DB Column is MNT_AVG_ACTIF. |
| 38 | `FS.GA.NAV.SIMULATION.TEMP.AVERAGE.ACTIF.PERCENTAGE` | `FsGaNavSimulationTemp_AverageActifPercentage` | TField |  | Average ACTIF Percentage Multifonds DB Column is MNT_AVG_ACTIF_PCT. |
| 39 | `FS.GA.NAV.SIMULATION.TEMP.TRANSAC.NUMBER` | `FsGaNavSimulationTemp_TransacNumber` | TField |  | Transaction Number Multifonds DB Column is TRAN_NO. |
| 40 | `FS.GA.NAV.SIMULATION.TEMP.PROCESS.ID` | `FsGaNavSimulationTemp_ProcessId` | TField |  | The Id of the Nav process. NA1, NA2 etc Multifonds DB Column is NAV_PROCESS. |
| 41 | `FS.GA.NAV.SIMULATION.TEMP.APPLICATION.ACCOUNTING.DATE` | `FsGaNavSimulationTemp_ApplicationAccountingDate` | TField |  | Application Accounting Date Multifonds DB Column is DCTA_APP. |
| 42 | `FS.GA.NAV.SIMULATION.TEMP.BID.MID.PERCENTAGE` | `FsGaNavSimulationTemp_BidMidPercentage` | TField |  | Bid Mid Percentage Multifonds DB Column is PCT_BID_MID. |
| 43 | `FS.GA.NAV.SIMULATION.TEMP.OFFER.MID.PERCENTAGE` | `FsGaNavSimulationTemp_OfferMidPercentage` | TField |  | Offer Mid Percentage Multifonds DB Column is PCT_OFFER_MID. |
| 44 | `FS.GA.NAV.SIMULATION.TEMP.DEFAULT.AUTHORIZED.BASIS` | `FsGaNavSimulationTemp_DefaultAuthorizedBasis` | TField |  | Basis for the price per unit for Subscription and redemption for the External fund share unit price. (B - Bid, M - Mid, O - Offer &amp; L - Middle). Multifonds DB Column is AUTH_BASIS. |
| 45 | `FS.GA.NAV.SIMULATION.TEMP.CONFIRMED` | `FsGaNavSimulationTemp_Confirmed` | TField |  | This field denotes the status of the trade. Confirmed or Not Confirmed Multifonds DB Column is FLG_CONFIRM. |
| 46 | `FS.GA.NAV.SIMULATION.TEMP.SPREAD.BID` | `FsGaNavSimulationTemp_SpreadBid` | TField |  | Spread Bid Multifonds DB Column is SPREAD_BID. |
| 47 | `FS.GA.NAV.SIMULATION.TEMP.SPREAD.OFFER` | `FsGaNavSimulationTemp_SpreadOffer` | TField |  | Spread Offer Multifonds DB Column is SPREAD_OFFER. |
| 48 | `FS.GA.NAV.SIMULATION.TEMP.BF.SWING.NET.AMOUNT` | `FsGaNavSimulationTemp_BfSwingNetAmount` | TField |  | Bf Swing Net Amount Multifonds DB Column is MNT_NET_BF_SWING. |
| 49 | `FS.GA.NAV.SIMULATION.TEMP.SWING.VALUATION.METHOD` | `FsGaNavSimulationTemp_SwingValuationMethod` | TField |  | Swing Valuation Method Multifonds DB Column is SWING_FCYELD. |
| 50 | `FS.GA.NAV.SIMULATION.TEMP.ROUNDING.METHOD` | `FsGaNavSimulationTemp_RoundingMethod` | TField |  | Rounding Method Multifonds DB Column is ROUNDING_METHOD. |
| 51 | `FS.GA.NAV.SIMULATION.TEMP.EQUITY.AT.POSITION` | `FsGaNavSimulationTemp_EquityAtPosition` | TField |  | Equity at Position Multifonds DB Column is FLG_POSITION. |
| 52 | `FS.GA.NAV.SIMULATION.TEMP.NET.WORTH` | `FsGaNavSimulationTemp_NetWorth` | TField |  | Net Worth Flag Multifonds DB Column is FLG_NET_WORTH. |
| 53 | `FS.GA.NAV.SIMULATION.TEMP.GROSS.ROR.IN.BPS` | `FsGaNavSimulationTemp_GrossRorInBps` | TField |  | Gross ROR In Bps Multifonds DB Column is GROSS_ROR_BPS. |
| 54 | `FS.GA.NAV.SIMULATION.TEMP.GROSS.ROR.IN.PERCENTAGE` | `FsGaNavSimulationTemp_GrossRorInPercentage` | TField |  | Gross ROR In Percentage Multifonds DB Column is GROSS_ROR_PCT. |
| 55 | `FS.GA.NAV.SIMULATION.TEMP.GROSS.UNIT.VALUE` | `FsGaNavSimulationTemp_GrossUnitValue` | TField |  | Gross Unit Value Multifonds DB Column is GROSS_UNIT_VALUE. |
| 56 | `FS.GA.NAV.SIMULATION.TEMP.GROSS.ROR.BPS.BID` | `FsGaNavSimulationTemp_GrossRorBpsBid` | TField |  | Gross ROR Bps Bid Multifonds DB Column is GROSS_ROR_BPS_BID. |
| 57 | `FS.GA.NAV.SIMULATION.TEMP.GROSS.ROR.PCT.BID` | `FsGaNavSimulationTemp_GrossRorPctBid` | TField |  | Gross ROR Pct Bid Multifonds DB Column is GROSS_ROR_PCT_BID. |
| 58 | `FS.GA.NAV.SIMULATION.TEMP.GROSS.ROR.BPS.OFFER` | `FsGaNavSimulationTemp_GrossRorBpsOffer` | TField |  | Gross ROR Bps Offer Multifonds DB Column is GROSS_ROR_BPS_OFFER. |
| 59 | `FS.GA.NAV.SIMULATION.TEMP.GROSS.ROR.PCT.OFFER` | `FsGaNavSimulationTemp_GrossRorPctOffer` | TField |  | Gross ROR Pct Offer Multifonds DB Column is GROSS_ROR_PCT_OFFER. |
| 60 | `FS.GA.NAV.SIMULATION.TEMP.GROSS.ROR.PCT.AARR` | `FsGaNavSimulationTemp_GrossRorPctAarr` | TField |  | Gross ROR Pct Aarr Multifonds DB Column is GROSS_ROR_PCT_AARR. |
| 61 | `FS.GA.NAV.SIMULATION.TEMP.GROSS.ROR.PCT.BID.AARR` | `FsGaNavSimulationTemp_GrossRorPctBidAarr` | TField |  | Gross ROR Pct Bid Aarr Multifonds DB Column is GROSS_ROR_PCT_BID_AARR. |
| 62 | `FS.GA.NAV.SIMULATION.TEMP.KNOWLEDGE.DATE` | `FsGaNavSimulationTemp_KnowledgeDate` | TField |  | Knowledge Date Multifonds DB Column is KNOWLEDGEDATE. |
| 63 | `FS.GA.NAV.SIMULATION.TEMP.RESERVED10` | `FsGaNavSimulationTemp_Reserved10` | TField |  |  |
| 64 | `FS.GA.NAV.SIMULATION.TEMP.RESERVED9` | `FsGaNavSimulationTemp_Reserved9` | TField |  |  |
| 65 | `FS.GA.NAV.SIMULATION.TEMP.RESERVED8` | `FsGaNavSimulationTemp_Reserved8` | TField |  |  |
| 66 | `FS.GA.NAV.SIMULATION.TEMP.RESERVED7` | `FsGaNavSimulationTemp_Reserved7` | TField |  |  |
| 67 | `FS.GA.NAV.SIMULATION.TEMP.RESERVED6` | `FsGaNavSimulationTemp_Reserved6` | TField |  |  |
| 68 | `FS.GA.NAV.SIMULATION.TEMP.RESERVED5` | `FsGaNavSimulationTemp_Reserved5` | TField |  |  |
| 69 | `FS.GA.NAV.SIMULATION.TEMP.RESERVED4` | `FsGaNavSimulationTemp_Reserved4` | TField |  |  |
| 70 | `FS.GA.NAV.SIMULATION.TEMP.RESERVED3` | `FsGaNavSimulationTemp_Reserved3` | TField |  |  |
| 71 | `FS.GA.NAV.SIMULATION.TEMP.RESERVED2` | `FsGaNavSimulationTemp_Reserved2` | TField |  |  |
| 72 | `FS.GA.NAV.SIMULATION.TEMP.RESERVED1` | `FsGaNavSimulationTemp_Reserved1` | TField |  |  |
| 73 | `FS.GA.NAV.SIMULATION.TEMP.LOCAL.REF` | `FsGaNavSimulationTemp_LocalRef` |  |  |  |
| 74 | `FS.GA.NAV.SIMULATION.TEMP.OVERRIDE` | `FsGaNavSimulationTemp_Override` |  |  |  |
| 75 | `FS.GA.NAV.SIMULATION.TEMP.RECORD.STATUS` | `FsGaNavSimulationTemp_RecordStatus` | String |  |  |
| 76 | `FS.GA.NAV.SIMULATION.TEMP.CURR.NO` | `FsGaNavSimulationTemp_CurrNo` | String |  |  |
| 77 | `FS.GA.NAV.SIMULATION.TEMP.INPUTTER` | `FsGaNavSimulationTemp_Inputter` |  |  |  |
| 78 | `FS.GA.NAV.SIMULATION.TEMP.DATE.TIME` | `FsGaNavSimulationTemp_DateTime` |  |  |  |
| 79 | `FS.GA.NAV.SIMULATION.TEMP.AUTHORISER` | `FsGaNavSimulationTemp_Authoriser` | String |  |  |
| 80 | `FS.GA.NAV.SIMULATION.TEMP.CO.CODE` | `FsGaNavSimulationTemp_CoCode` | String |  |  |
| 81 | `FS.GA.NAV.SIMULATION.TEMP.DEPT.CODE` | `FsGaNavSimulationTemp_DeptCode` | String |  |  |
| 82 | `FS.GA.NAV.SIMULATION.TEMP.AUDITOR.CODE` | `FsGaNavSimulationTemp_AuditorCode` | String |  |  |
| 83 | `FS.GA.NAV.SIMULATION.TEMP.AUDIT.DATE.TIME` | `FsGaNavSimulationTemp_AuditDateTime` | String |  |  |
