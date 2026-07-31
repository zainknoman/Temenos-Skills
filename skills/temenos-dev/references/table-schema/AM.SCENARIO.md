# AM.SCENARIO — Table Schema

> Source: `INSERTS/I_F.AM.SCENARIO` in `AM_ModellingScenario.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AM.SCE.CREATION.DATE` | `AmScenario_CreationDate` | TField |  | Scenario creation date. Updated by automatic proposed orders routines. Validation Rules: No input. |
| 2 | `AM.SCE.CREATION.MODE` | `AmScenario_CreationMode` | TField |  | This field can be set to AUTO or MANUAL. |
| 3 | `AM.SCE.SESSION` | `AmScenario_Session` | TField |  | The session number of the user or process that created this record. Part of the key to this record. |
| 4 | `AM.SCE.SAM.CODE` | `AmScenario_SamCode` | TField |  | The portfolio for which this scenario was created. Must be a valid entry in the SEC.ACC.MASTER table. |
| 5 | `AM.SCE.RESERVED12` | `AmScenario_Reserved12` | TField |  |  |
| 6 | `AM.SCE.RESERVED11` | `AmScenario_Reserved11` | TField |  |  |
| 7 | `AM.SCE.RESERVED10` | `AmScenario_Reserved10` | TField |  |  |
| 8 | `AM.SCE.SC.SELECTED` | `AmScenario_ScSelected` |  |  |  |
| 9 | `AM.SCE.SC.OPERATOR` | `AmScenario_ScOperator` |  |  |  |
| 10 | `AM.SCE.SC.LOCKED` | `AmScenario_ScLocked` |  |  |  |
| 11 | `AM.SCE.SC.DIRECTION` | `AmScenario_ScDirection` |  |  |  |
| 12 | `AM.SCE.SCA.SECURITY` | `AmScenario_ScaSecurity` |  |  |  |
| 13 | `AM.SCE.SCA.CURRENCY` | `AmScenario_ScaCurrency` |  |  |  |
| 14 | `AM.SCE.SCA.PRICE.TYPE` | `AmScenario_ScaPriceType` |  |  |  |
| 15 | `AM.SCE.SCA.NOM.HELD` | `AmScenario_ScaNomHeld` |  |  |  |
| 16 | `AM.SCE.SCA.AMT.HELD` | `AmScenario_ScaAmtHeld` |  |  |  |
| 17 | `AM.SCE.SCA.NOMINAL` | `AmScenario_ScaNominal` |  |  |  |
| 18 | `AM.SCE.SCA.PRICE` | `AmScenario_ScaPrice` |  |  |  |
| 19 | `AM.SCE.SC.PROPOSED.VAL` | `AmScenario_ScProposedVal` |  |  |  |
| 20 | `AM.SCE.SCA.VALUATION` | `AmScenario_ScaValuation` |  |  |  |
| 21 | `AM.SCE.SCP.ACCOUNT` | `AmScenario_ScpAccount` |  |  |  |
| 22 | `AM.SCE.SCP.CURRENCY` | `AmScenario_ScpCurrency` |  |  |  |
| 23 | `AM.SCE.SCP.VALUATION` | `AmScenario_ScpValuation` |  |  |  |
| 24 | `AM.SCE.SC.EXCH.RATE` | `AmScenario_ScExchRate` |  |  |  |
| 25 | `AM.SCE.SC.VIOLATION` | `AmScenario_ScViolation` |  |  |  |
| 26 | `AM.SCE.VIOL.LIST` | `AmScenario_ViolList` |  |  |  |
| 27 | `AM.SCE.NOTES` | `AmScenario_Notes` |  |  |  |
| 28 | `AM.SCE.REASON.TYPE` | `AmScenario_ReasonType` |  |  |  |
| 29 | `AM.SCE.SC.ORDER` | `AmScenario_ScOrder` |  |  |  |
| 30 | `AM.SCE.SC.PROP.NOMINAL` | `AmScenario_ScPropNominal` |  |  |  |
| 31 | `AM.SCE.RSN.TYPE.DESC` | `AmScenario_RsnTypeDesc` |  |  |  |
| 32 | `AM.SCE.RESERVED07` | `AmScenario_Reserved07` | TField |  |  |
| 33 | `AM.SCE.FX.SELECTED` | `AmScenario_FxSelected` |  |  |  |
| 34 | `AM.SCE.FX.OPERATOR` | `AmScenario_FxOperator` |  |  |  |
| 35 | `AM.SCE.FX.LOCKED` | `AmScenario_FxLocked` |  |  |  |
| 36 | `AM.SCE.FX.DEAL.TYPE` | `AmScenario_FxDealType` |  |  |  |
| 37 | `AM.SCE.FX.LEAD.CCY` | `AmScenario_FxLeadCcy` |  |  |  |
| 38 | `AM.SCE.FX.MATURITY` | `AmScenario_FxMaturity` |  |  |  |
| 39 | `AM.SCE.CURRENCY.SOLD` | `AmScenario_CurrencySold` |  |  |  |
| 40 | `AM.SCE.ACCOUNT.PAY` | `AmScenario_AccountPay` |  |  |  |
| 41 | `AM.SCE.AMOUNT.SOLD` | `AmScenario_AmountSold` |  |  |  |
| 42 | `AM.SCE.CURRENCY.BOUGHT` | `AmScenario_CurrencyBought` |  |  |  |
| 43 | `AM.SCE.ACCOUNT.REC` | `AmScenario_AccountRec` |  |  |  |
| 44 | `AM.SCE.AMOUNT.BOUGHT` | `AmScenario_AmountBought` |  |  |  |
| 45 | `AM.SCE.FX.EXCH.RATE` | `AmScenario_FxExchRate` |  |  |  |
| 46 | `AM.SCE.RESERVEDX06` | `AmScenario_Reservedx06` |  |  |  |
| 47 | `AM.SCE.RESERVEDX05` | `AmScenario_Reservedx05` |  |  |  |
| 48 | `AM.SCE.RESERVEDX04` | `AmScenario_Reservedx04` |  |  |  |
| 49 | `AM.SCE.FX.ORDER` | `AmScenario_FxOrder` |  |  |  |
| 50 | `AM.SCE.RESERVED06` | `AmScenario_Reserved06` | TField |  |  |
| 51 | `AM.SCE.RESERVED05` | `AmScenario_Reserved05` | TField |  |  |
| 52 | `AM.SCE.RESERVED04` | `AmScenario_Reserved04` | TField |  |  |
| 53 | `AM.SCE.AC.SELECTED` | `AmScenario_AcSelected` |  |  |  |
| 54 | `AM.SCE.AC.OPERATOR` | `AmScenario_AcOperator` |  |  |  |
| 55 | `AM.SCE.AC.LOCKED` | `AmScenario_AcLocked` |  |  |  |
| 56 | `AM.SCE.AC.DIRECTION` | `AmScenario_AcDirection` |  |  |  |
| 57 | `AM.SCE.ACA.CURRENCY` | `AmScenario_AcaCurrency` |  |  |  |
| 58 | `AM.SCE.ACA.ACCOUNT` | `AmScenario_AcaAccount` |  |  |  |
| 59 | `AM.SCE.ACA.VALUATION` | `AmScenario_AcaValuation` |  |  |  |
| 60 | `AM.SCE.RESERVEDX03` | `AmScenario_Reservedx03` |  |  |  |
| 61 | `AM.SCE.RESERVEDX02` | `AmScenario_Reservedx02` |  |  |  |
| 62 | `AM.SCE.RESERVEDX01` | `AmScenario_Reservedx01` |  |  |  |
| 63 | `AM.SCE.AC.ORDER` | `AmScenario_AcOrder` |  |  |  |
| 64 | `AM.SCE.SAM.VALUATION` | `AmScenario_SamValuation` | TField |  | This field contains the total valuation of a portfolio. Validation Rules: No input field. Automatically updated by the AM.REBALANCE routine whenever the rebalance is launched. |
| 65 | `AM.SCE.RESERVED03` | `AmScenario_Reserved03` | TField |  |  |
| 66 | `AM.SCE.RESERVED02` | `AmScenario_Reserved02` | TField |  |  |
| 67 | `AM.SCE.RESERVED01` | `AmScenario_Reserved01` | TField |  |  |
| 68 | `AM.SCE.LOCAL.REF` | `AmScenario_LocalRef` |  |  |  |
| 69 | `AM.SCE.OVERRIDE` | `AmScenario_Override` |  |  |  |
| 70 | `AM.SCE.RECORD.STATUS` | `AmScenario_RecordStatus` | String |  |  |
| 71 | `AM.SCE.CURR.NO` | `AmScenario_CurrNo` | String |  |  |
| 72 | `AM.SCE.INPUTTER` | `AmScenario_Inputter` |  |  |  |
| 73 | `AM.SCE.DATE.TIME` | `AmScenario_DateTime` |  |  |  |
| 74 | `AM.SCE.AUTHORISER` | `AmScenario_Authoriser` | String |  |  |
| 75 | `AM.SCE.CO.CODE` | `AmScenario_CoCode` | String |  |  |
| 76 | `AM.SCE.DEPT.CODE` | `AmScenario_DeptCode` | String |  |  |
| 77 | `AM.SCE.AUDITOR.CODE` | `AmScenario_AuditorCode` | String |  |  |
| 78 | `AM.SCE.AUDIT.DATE.TIME` | `AmScenario_AuditDateTime` | String |  |  |
