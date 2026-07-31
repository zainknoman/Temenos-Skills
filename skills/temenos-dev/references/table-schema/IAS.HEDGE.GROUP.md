# IAS.HEDGE.GROUP — Table Schema

> Source: `INSERTS/I_F.IAS.HEDGE.GROUP` in `IA_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IAS.HG.DESCRIPTION` | `IasHedgeGroup_Description` |  |  |  |
| 2 | `IAS.HG.HEDGE.TYPE` | `IasHedgeGroup_HedgeType` | TField |  | Specifies the type of Hedge to be applied for this Group. Validation Rules: Valid IAS.HEDGE.TYPE. |
| 3 | `IAS.HG.START.DATE` | `IasHedgeGroup_StartDate` | TField |  | Start Date of the Hedge Agreement. Validation Rules: Valid T24 Date - format YYYY/ MM / DD |
| 4 | `IAS.HG.END.DATE` | `IasHedgeGroup_EndDate` | TField |  | End Date of the Hedge Agreement. Validation Rules: Valid T24 Date - format YYYY/ MM / DD |
| 5 | `IAS.HG.LAST.CALC.DATE` | `IasHedgeGroup_LastCalcDate` | TField |  | The last date for the calculation of the information on the Group. Validation Rules: Valid T24 Date - format YYYY/ MM / DD |
| 6 | `IAS.HG.HEDGED.CONT.ID` | `IasHedgeGroup_HedgedContId` |  |  |  |
| 7 | `IAS.HG.HEDGED.CON.CCY` | `IasHedgeGroup_HedgedConCcy` |  |  |  |
| 8 | `IAS.HG.HEDGED.CON.AMT` | `IasHedgeGroup_HedgedConAmt` |  |  |  |
| 9 | `IAS.HG.HEDGED.CON.LAMT` | `IasHedgeGroup_HedgedConLamt` |  |  |  |
| 10 | `IAS.HG.HEDGING.CONT.ID` | `IasHedgeGroup_HedgingContId` |  |  |  |
| 11 | `IAS.HG.HEDGING.CON.CCY` | `IasHedgeGroup_HedgingConCcy` |  |  |  |
| 12 | `IAS.HG.HEDGING.CON.AMT` | `IasHedgeGroup_HedgingConAmt` |  |  |  |
| 13 | `IAS.HG.HEDGING.CO.LAMT` | `IasHedgeGroup_HedgingCoLamt` |  |  |  |
| 14 | `IAS.HG.EFFECTIVE.PERC` | `IasHedgeGroup_EffectivePerc` | TField |  | This field holds the percentage effectiveness of the hedge group. |
| 15 | `IAS.HG.CONTRACT.TYPE` | `IasHedgeGroup_ContractType` |  |  |  |
| 16 | `IAS.HG.CONTRACT.ID` | `IasHedgeGroup_ContractId` |  |  |  |
| 17 | `IAS.HG.CONTRACT.CCY` | `IasHedgeGroup_ContractCcy` |  |  |  |
| 18 | `IAS.HG.BOOK.COST` | `IasHedgeGroup_BookCost` |  |  |  |
| 19 | `IAS.HG.FAIR.VALUE` | `IasHedgeGroup_FairValue` |  |  |  |
| 20 | `IAS.HG.ADJUSTMENT.AMT` | `IasHedgeGroup_AdjustmentAmt` |  |  |  |
| 21 | `IAS.HG.RESERVED12` | `IasHedgeGroup_Reserved12` |  |  |  |
| 22 | `IAS.HG.RESERVED11` | `IasHedgeGroup_Reserved11` |  |  |  |
| 23 | `IAS.HG.RESERVED10` | `IasHedgeGroup_Reserved10` |  |  |  |
| 24 | `IAS.HG.RESERVED9` | `IasHedgeGroup_Reserved9` |  |  |  |
| 25 | `IAS.HG.IFRS.SUB.TYPE` | `IasHedgeGroup_IfrsSubType` | TField |  | This field provides the link to IFRS.SUB.TYPE in order to pick the posting details for the adjustments performed under Hedge. Validation Rules: Inputtbale only when 'IH' product is installed in the company. |
| 26 | `IAS.HG.HEDGE.STATUS` | `IasHedgeGroup_HedgeStatus` | TField |  | Field to hold the Hedge status for the contracts defined in Hedge relation. Validation Rules: Allowed values are EFFECTIVE, INEFFECTIVE, CLOSED.RELATION |
| 27 | `IAS.HG.RESERVED8` | `IasHedgeGroup_Reserved8` | TField |  |  |
| 28 | `IAS.HG.RESERVED7` | `IasHedgeGroup_Reserved7` | TField |  |  |
| 29 | `IAS.HG.RESERVED6` | `IasHedgeGroup_Reserved6` | TField |  |  |
| 30 | `IAS.HG.RESERVED5` | `IasHedgeGroup_Reserved5` | TField |  |  |
| 31 | `IAS.HG.RESERVED4` | `IasHedgeGroup_Reserved4` | TField |  |  |
| 32 | `IAS.HG.RESERVED3` | `IasHedgeGroup_Reserved3` | TField |  |  |
| 33 | `IAS.HG.RESERVED2` | `IasHedgeGroup_Reserved2` | TField |  |  |
| 34 | `IAS.HG.RESERVED1` | `IasHedgeGroup_Reserved1` | TField |  |  |
| 35 | `IAS.HG.LOCAL.REF` | `IasHedgeGroup_LocalRef` |  |  |  |
| 36 | `IAS.HG.OVERRIDE` | `IasHedgeGroup_Override` |  |  |  |
| 37 | `IAS.HG.RECORD.STATUS` | `IasHedgeGroup_RecordStatus` | String |  |  |
| 38 | `IAS.HG.CURR.NO` | `IasHedgeGroup_CurrNo` | String |  |  |
| 39 | `IAS.HG.INPUTTER` | `IasHedgeGroup_Inputter` |  |  |  |
| 40 | `IAS.HG.DATE.TIME` | `IasHedgeGroup_DateTime` |  |  |  |
| 41 | `IAS.HG.AUTHORISER` | `IasHedgeGroup_Authoriser` | String |  |  |
| 42 | `IAS.HG.CO.CODE` | `IasHedgeGroup_CoCode` | String |  |  |
| 43 | `IAS.HG.DEPT.CODE` | `IasHedgeGroup_DeptCode` | String |  |  |
| 44 | `IAS.HG.AUDITOR.CODE` | `IasHedgeGroup_AuditorCode` | String |  |  |
| 45 | `IAS.HG.AUDIT.DATE.TIME` | `IasHedgeGroup_AuditDateTime` | String |  |  |
