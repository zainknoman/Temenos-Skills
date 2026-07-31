# AM.SCENARIO.SAVED — Table Schema

> Source: `INSERTS/I_F.AM.SCENARIO.SAVED` in `AM_ModellingScenario.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.SCSVD.CREATION.DATE` | `AmScenarioSaved_CreationDate` | TField |  | Scenario creation date. Updated by automatic proposed orders routines. Validation Rules: No input. |
| 2 | `AM.SCSVD.CREATION.MODE` | `AmScenarioSaved_CreationMode` | TField |  | This field can be set to AUTO or MANUAL. |
| 3 | `AM.SCSVD.SESSION` | `AmScenarioSaved_Session` | TField |  | The session number of the user or process that created this record. |
| 4 | `AM.SCSVD.SAM.CODE` | `AmScenarioSaved_SamCode` | TField |  | The portfolio for which this scenario was created. Must be a valid entry in the SEC.ACC.MASTER table. |
| 5 | `AM.SCSVD.RESERVED12` | `AmScenarioSaved_Reserved12` | TField |  |  |
| 6 | `AM.SCSVD.RESERVED11` | `AmScenarioSaved_Reserved11` | TField |  |  |
| 7 | `AM.SCSVD.RESERVED10` | `AmScenarioSaved_Reserved10` | TField |  |  |
| 8 | `AM.SCSVD.SC.SELECTED` | `AmScenarioSaved_ScSelected` |  |  |  |
| 9 | `AM.SCSVD.SC.OPERATOR` | `AmScenarioSaved_ScOperator` |  |  |  |
| 10 | `AM.SCSVD.SC.LOCKED` | `AmScenarioSaved_ScLocked` |  |  |  |
| 11 | `AM.SCSVD.SC.DIRECTION` | `AmScenarioSaved_ScDirection` |  |  |  |
| 12 | `AM.SCSVD.SCA.SECURITY` | `AmScenarioSaved_ScaSecurity` |  |  |  |
| 13 | `AM.SCSVD.SCA.CURRENCY` | `AmScenarioSaved_ScaCurrency` |  |  |  |
| 14 | `AM.SCSVD.SCA.PRICE.TYPE` | `AmScenarioSaved_ScaPriceType` |  |  |  |
| 15 | `AM.SCSVD.SCA.NOM.HELD` | `AmScenarioSaved_ScaNomHeld` |  |  |  |
| 16 | `AM.SCSVD.SCA.AMT.HELD` | `AmScenarioSaved_ScaAmtHeld` |  |  |  |
| 17 | `AM.SCSVD.SCA.NOMINAL` | `AmScenarioSaved_ScaNominal` |  |  |  |
| 18 | `AM.SCSVD.SCA.PRICE` | `AmScenarioSaved_ScaPrice` |  |  |  |
| 19 | `AM.SCSVD.SC.PROPOSED.VAL` | `AmScenarioSaved_ScProposedVal` |  |  |  |
| 20 | `AM.SCSVD.SCA.VALUATION` | `AmScenarioSaved_ScaValuation` |  |  |  |
| 21 | `AM.SCSVD.SCP.ACCOUNT` | `AmScenarioSaved_ScpAccount` |  |  |  |
| 22 | `AM.SCSVD.SCP.CURRENCY` | `AmScenarioSaved_ScpCurrency` |  |  |  |
| 23 | `AM.SCSVD.SCP.VALUATION` | `AmScenarioSaved_ScpValuation` |  |  |  |
| 24 | `AM.SCSVD.SC.EXCH.RATE` | `AmScenarioSaved_ScExchRate` |  |  |  |
| 25 | `AM.SCSVD.SC.VIOLATION` | `AmScenarioSaved_ScViolation` |  |  |  |
| 26 | `AM.SCSVD.VIOL.LIST` | `AmScenarioSaved_ViolList` |  |  |  |
| 27 | `AM.SCSVD.NOTES` | `AmScenarioSaved_Notes` |  |  |  |
| 28 | `AM.SCSVD.REASON.TYPE` | `AmScenarioSaved_ReasonType` |  |  |  |
| 29 | `AM.SCSVD.SC.ORDER` | `AmScenarioSaved_ScOrder` |  |  |  |
| 30 | `AM.SCSVD.SC.PROP.NOMINAL` | `AmScenarioSaved_ScPropNominal` |  |  |  |
| 31 | `AM.SCSVD.RSN.TYPE.DESC` | `AmScenarioSaved_RsnTypeDesc` |  |  |  |
| 32 | `AM.SCSVD.RESERVED07` | `AmScenarioSaved_Reserved07` | TField |  |  |
| 33 | `AM.SCSVD.FX.SELECTED` | `AmScenarioSaved_FxSelected` |  |  |  |
| 34 | `AM.SCSVD.FX.OPERATOR` | `AmScenarioSaved_FxOperator` |  |  |  |
| 35 | `AM.SCSVD.FX.LOCKED` | `AmScenarioSaved_FxLocked` |  |  |  |
| 36 | `AM.SCSVD.FX.DEAL.TYPE` | `AmScenarioSaved_FxDealType` |  |  |  |
| 37 | `AM.SCSVD.FX.LEAD.CCY` | `AmScenarioSaved_FxLeadCcy` |  |  |  |
| 38 | `AM.SCSVD.FX.MATURITY` | `AmScenarioSaved_FxMaturity` |  |  |  |
| 39 | `AM.SCSVD.CURRENCY.SOLD` | `AmScenarioSaved_CurrencySold` |  |  |  |
| 40 | `AM.SCSVD.ACCOUNT.PAY` | `AmScenarioSaved_AccountPay` |  |  |  |
| 41 | `AM.SCSVD.AMOUNT.SOLD` | `AmScenarioSaved_AmountSold` |  |  |  |
| 42 | `AM.SCSVD.CURRENCY.BOUGHT` | `AmScenarioSaved_CurrencyBought` |  |  |  |
| 43 | `AM.SCSVD.ACCOUNT.REC` | `AmScenarioSaved_AccountRec` |  |  |  |
| 44 | `AM.SCSVD.AMOUNT.BOUGHT` | `AmScenarioSaved_AmountBought` |  |  |  |
| 45 | `AM.SCSVD.FX.EXCH.RATE` | `AmScenarioSaved_FxExchRate` |  |  |  |
| 46 | `AM.SCSVD.RESERVEDX06` | `AmScenarioSaved_Reservedx06` |  |  |  |
| 47 | `AM.SCSVD.RESERVEDX05` | `AmScenarioSaved_Reservedx05` |  |  |  |
| 48 | `AM.SCSVD.RESERVEDX04` | `AmScenarioSaved_Reservedx04` |  |  |  |
| 49 | `AM.SCSVD.FX.ORDER` | `AmScenarioSaved_FxOrder` |  |  |  |
| 50 | `AM.SCSVD.RESERVED06` | `AmScenarioSaved_Reserved06` | TField |  |  |
| 51 | `AM.SCSVD.RESERVED05` | `AmScenarioSaved_Reserved05` | TField |  |  |
| 52 | `AM.SCSVD.RESERVED04` | `AmScenarioSaved_Reserved04` | TField |  |  |
| 53 | `AM.SCSVD.AC.SELECTED` | `AmScenarioSaved_AcSelected` |  |  |  |
| 54 | `AM.SCSVD.AC.OPERATOR` | `AmScenarioSaved_AcOperator` |  |  |  |
| 55 | `AM.SCSVD.AC.LOCKED` | `AmScenarioSaved_AcLocked` |  |  |  |
| 56 | `AM.SCSVD.AC.DIRECTION` | `AmScenarioSaved_AcDirection` |  |  |  |
| 57 | `AM.SCSVD.ACA.CURRENCY` | `AmScenarioSaved_AcaCurrency` |  |  |  |
| 58 | `AM.SCSVD.ACA.ACCOUNT` | `AmScenarioSaved_AcaAccount` |  |  |  |
| 59 | `AM.SCSVD.ACA.VALUATION` | `AmScenarioSaved_AcaValuation` |  |  |  |
| 60 | `AM.SCSVD.RESERVEDX03` | `AmScenarioSaved_Reservedx03` |  |  |  |
| 61 | `AM.SCSVD.RESERVEDX02` | `AmScenarioSaved_Reservedx02` |  |  |  |
| 62 | `AM.SCSVD.RESERVEDX01` | `AmScenarioSaved_Reservedx01` |  |  |  |
| 63 | `AM.SCSVD.AC.ORDER` | `AmScenarioSaved_AcOrder` |  |  |  |
| 64 | `AM.SCSVD.SAM.VALUATION` | `AmScenarioSaved_SamValuation` | TField |  | This field contains the total valuation of a portfolio. Validation Rules: No input field. Automatically updated by the AM.REBALANCE routine whenever the rebalance is launched. |
| 65 | `AM.SCSVD.RESERVED03` | `AmScenarioSaved_Reserved03` | TField |  |  |
| 66 | `AM.SCSVD.RESERVED02` | `AmScenarioSaved_Reserved02` | TField |  |  |
| 67 | `AM.SCSVD.RESERVED01` | `AmScenarioSaved_Reserved01` | TField |  |  |
| 68 | `AM.SCSVD.LOCAL.REF` | `AmScenarioSaved_LocalRef` |  |  |  |
| 69 | `AM.SCSVD.OVERRIDE` | `AmScenarioSaved_Override` |  |  |  |
