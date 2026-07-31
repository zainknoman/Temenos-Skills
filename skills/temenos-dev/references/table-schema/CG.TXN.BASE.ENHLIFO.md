# CG.TXN.BASE.ENHLIFO — Table Schema

> Source: `INSERTS/I_F.CG.TXN.BASE.ENHLIFO` in `SC_SctCapitalGains.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CG.ENHLIFO.SECURITY.NO` | `CgTxnBaseEnhlifo_SecurityNo` | TField |  | The field will store the Security code for which Franking Credits are computed Validation Rules Noinput field.Updated by the system |
| 2 | `CG.ENHLIFO.PORTFOLIO` | `CgTxnBaseEnhlifo_Portfolio` | TField |  | The field will store the portfolio for which Franking Credits are computed Validation Rules Noinput field.Updated by the system |
| 3 | `CG.ENHLIFO.CG.BASE.ID` | `CgTxnBaseEnhlifo_CgBaseId` | TField |  | The Field is in three parts separated by a dot character ".". The first part contains the underlying CUSTOMER id,the second part contains the group to which the portfolio belongs, as defined in PORTFOLIO.GROUPING,thereforeindicating the id of the portfolio to which the security belongs.The third part identifies the security itself. For example: 12435.12435-1.000123-000 Where 12435 is the CUSTOMER id, 12435-1 indicates the portfolio group and 000123-000 indicates the security heldby the customer. Validation Rules Noinput field.Updated by the system |
| 4 | `CG.ENHLIFO.DIARY.ID` | `CgTxnBaseEnhlifo_DiaryId` | TField |  | The field will store the Diary Id for which Franking credits are computed based on Franked rate mentioned inDIARY record Validation Rules Noinput field.Updated by the system |
| 5 | `CG.ENHLIFO.ENTITLEMENT.ID` | `CgTxnBaseEnhlifo_EntitlementId` | TField |  | The field will store the Entitlement id for which Franking credits are computed based on Franked rate mentionedin DIARY record Validation Rules Noinput field.Updated by the system |
| 6 | `CG.ENHLIFO.EVENT.CURRENCY` | `CgTxnBaseEnhlifo_EventCurrency` | TField | Yes | Currency in which Franked Dividend is calculated. If event currency is a non-restricted Currency, then SettlementCurrency and Exchange rate is mandatory Validation Rules Noinput field.Updated by the system |
| 7 | `CG.ENHLIFO.SEC.CURRENCY` | `CgTxnBaseEnhlifo_SecCurrency` | TField |  | This field will contain the currency code indicating the security currency as recorded on the underlyingSECURITY.MASTER file Validation Rules Noinput field.Updated by the system |
| 8 | `CG.ENHLIFO.SEC.CCY.EXCH.RATE` | `CgTxnBaseEnhlifo_SecCcyExchRate` | TField |  | Field holds the Exchange Rate between the Event Currency and Security Currency. Updated by the system whilegeneratingEnhanced LIFO records Validation Rules Noinput field.Updated by the system |
| 9 | `CG.ENHLIFO.LCY.EXCH.RATE` | `CgTxnBaseEnhlifo_LcyExchRate` | TField |  | Field holds the Exchange Rate between the Event Currency and local Currency. Updated by the system whilegeneratingEnhanced LIFO records Validation Rules Noinput field.Updated by the system |
| 10 | `CG.ENHLIFO.DIVIDEND.EXDATE` | `CgTxnBaseEnhlifo_DividendExdate` | TField |  | The field will hold EX.DATE of the Diary event Validation Rules Noinput field.Updated by the system |
| 11 | `CG.ENHLIFO.FRANKED.DIVIDEND` | `CgTxnBaseEnhlifo_FrankedDividend` | TField |  | The field will hold the Franked dividend amount for this entitlement.It will be calculated as FRANKED.DIVIDEND =FRANKED.RATE*QUALIFIED.HOLDING Validation Rules Noinput field.Updated by the system |
| 12 | `CG.ENHLIFO.CORPORATE.TAX.RATE` | `CgTxnBaseEnhlifo_CorporateTaxRate` | TField |  | The field will hold Corporate Tax rate which will be used for computing the Franking credits. Defaulted from theCorporate Tax rate mentioned in CG.PARAMETER Validation Rules Noinput field.Updated by the system |
| 13 | `CG.ENHLIFO.FRANKING.CREDITS` | `CgTxnBaseEnhlifo_FrankingCredits` | TField |  | The field will hold Franking credits computed for this entitlement in Event CurrencyFRANKING.CREDITS = FRANKED.DIVIDEND * CORPORATE.TAX.RATE % / (1-CORPORATE.TAX.RATE %) Validation Rules Noinput field.Updated by the system |
| 14 | `CG.ENHLIFO.FRANKING.CREDITS.SEC.CCY` | `CgTxnBaseEnhlifo_FrankingCreditsSecCcy` | TField |  | The field will hold equivalent Franking credits computed for this entitlement in Security Currency Validation Rules Noinput field.Updated by the system |
| 15 | `CG.ENHLIFO.FRANKING.CREDITS.LCY` | `CgTxnBaseEnhlifo_FrankingCreditsLcy` | TField |  | The field will hold equivalent Franking credits computed for this entitlement in Local Currency Validation Rules Noinput field.Updated by the system |
| 16 | `CG.ENHLIFO.UNFRANKED.CFI` | `CgTxnBaseEnhlifo_UnfrankedCfi` | TField |  | The field will hold the UnFranked NCFI from the entitlement.UNFRANKED.NCFI = UNFRANKED.CFI.RATE * QUALIFYING.HOLDING Validation Rules Noinput field.Updated by the system |
| 17 | `CG.ENHLIFO.UNFRANKED.NCFI` | `CgTxnBaseEnhlifo_UnfrankedNcfi` | TField |  | The field will hold the UnFranked NCFI from the entitlement.UNFRANKED.NCFI = UNFRANKED.NCFI.RATE * QUALIFYING.HOLDING where UNFRANKED.NCFI.RATE is computed as UNFRANKED.RATE -UNFRANKED.CFI.RATE Validation Rules Noinput field.Updated by the system |
| 18 | `CG.ENHLIFO.NET.DIVIDEND` | `CgTxnBaseEnhlifo_NetDividend` | TField |  | The field will hold the Net Dividend from the entitlement. Validation Rules Noinput field.Updated by the system |
| 19 | `CG.ENHLIFO.GROSS.DIVIDEND` | `CgTxnBaseEnhlifo_GrossDividend` | TField |  | The field will hold the sum of Net Dividend and Franking credits resulted from the event Validation Rules Noinput field.Updated by the system |
| 20 | `CG.ENHLIFO.TRADE.DATE.TIME` | `CgTxnBaseEnhlifo_TradeDateTime` |  |  |  |
| 21 | `CG.ENHLIFO.SEC.TRANS.ID` | `CgTxnBaseEnhlifo_SecTransId` |  |  |  |
| 22 | `CG.ENHLIFO.TAX.LOT.ID` | `CgTxnBaseEnhlifo_TaxLotId` |  |  |  |
| 23 | `CG.ENHLIFO.TXN.TYPE` | `CgTxnBaseEnhlifo_TxnType` |  |  |  |
| 24 | `CG.ENHLIFO.ORIG.NOMINAL` | `CgTxnBaseEnhlifo_OrigNominal` |  |  |  |
| 25 | `CG.ENHLIFO.ORIG.FRANKING.CREDITS` | `CgTxnBaseEnhlifo_OrigFrankingCredits` |  |  |  |
| 26 | `CG.ENHLIFO.ORIG.FC.SEC.CCY` | `CgTxnBaseEnhlifo_OrigFcSecCcy` |  |  |  |
| 27 | `CG.ENHLIFO.ORIG.FC.LCY` | `CgTxnBaseEnhlifo_OrigFcLcy` |  |  |  |
| 28 | `CG.ENHLIFO.TRD.NOMINAL` | `CgTxnBaseEnhlifo_TrdNominal` |  |  |  |
| 29 | `CG.ENHLIFO.CG.NOMINAL` | `CgTxnBaseEnhlifo_CgNominal` |  |  |  |
| 30 | `CG.ENHLIFO.FRANKING.CRD.STATUS` | `CgTxnBaseEnhlifo_FrankingCrdStatus` |  |  |  |
| 31 | `CG.ENHLIFO.FC.RETAINED.LOTS` | `CgTxnBaseEnhlifo_FcRetainedLots` |  |  |  |
| 32 | `CG.ENHLIFO.FRANKING.CRD.RETAINED` | `CgTxnBaseEnhlifo_FrankingCrdRetained` |  |  |  |
| 33 | `CG.ENHLIFO.FC.RETAINED.SEC.CCY` | `CgTxnBaseEnhlifo_FcRetainedSecCcy` |  |  |  |
| 34 | `CG.ENHLIFO.FC.RETAINED.LCY` | `CgTxnBaseEnhlifo_FcRetainedLcy` |  |  |  |
| 35 | `CG.ENHLIFO.FC.RETAINED.MANUAL.UPD` | `CgTxnBaseEnhlifo_FcRetainedManualUpd` |  |  |  |
| 36 | `CG.ENHLIFO.FC.LOST.LOTS` | `CgTxnBaseEnhlifo_FcLostLots` |  |  |  |
| 37 | `CG.ENHLIFO.FRANKING.CRD.LOST` | `CgTxnBaseEnhlifo_FrankingCrdLost` |  |  |  |
| 38 | `CG.ENHLIFO.FC.LOST.SEC.CCY` | `CgTxnBaseEnhlifo_FcLostSecCcy` |  |  |  |
| 39 | `CG.ENHLIFO.FC.LOST.LCY` | `CgTxnBaseEnhlifo_FcLostLcy` |  |  |  |
| 40 | `CG.ENHLIFO.FC.LOST.MANUAL.UPD` | `CgTxnBaseEnhlifo_FcLostManualUpd` |  |  |  |
| 41 | `CG.ENHLIFO.UPDATE.METHOD` | `CgTxnBaseEnhlifo_UpdateMethod` |  |  |  |
| 42 | `CG.ENHLIFO.DAYS.HELD` | `CgTxnBaseEnhlifo_DaysHeld` |  |  |  |
| 43 | `CG.ENHLIFO.SALE.TXN.ID` | `CgTxnBaseEnhlifo_SaleTxnId` |  |  |  |
| 44 | `CG.ENHLIFO.SALE.TXN.NOM` | `CgTxnBaseEnhlifo_SaleTxnNom` |  |  |  |
| 45 | `CG.ENHLIFO.SALE.ADJ.FC` | `CgTxnBaseEnhlifo_SaleAdjFc` |  |  |  |
| 46 | `CG.ENHLIFO.SALE.ADJ.FC.SEC.CCY` | `CgTxnBaseEnhlifo_SaleAdjFcSecCcy` |  |  |  |
| 47 | `CG.ENHLIFO.SALE.ADJ.FC.LCY` | `CgTxnBaseEnhlifo_SaleAdjFcLcy` |  |  |  |
| 48 | `CG.ENHLIFO.TOT.FC.RETAINED` | `CgTxnBaseEnhlifo_TotFcRetained` | TField |  | This field will hold the total Retained Franking Credits in Event Currency Validation Rules Noinput field.Updated by the system |
| 49 | `CG.ENHLIFO.TOT.FC.RETAINED.SEC.CCY` | `CgTxnBaseEnhlifo_TotFcRetainedSecCcy` | TField |  | This field will hold the total Retained Franking Credits in security Currency Validation Rules Noinput field.Updated by the system |
| 50 | `CG.ENHLIFO.TOT.FC.RETAINED.LCY` | `CgTxnBaseEnhlifo_TotFcRetainedLcy` | TField |  | This field will hold the total Retained Franking Credits in local Currency Validation Rules Noinput field.Updated by the system |
| 51 | `CG.ENHLIFO.TOT.FC.LOST` | `CgTxnBaseEnhlifo_TotFcLost` | TField |  | This field will hold the total lost Franking Credits in Event Currency Validation Rules Noinput field.Updated by the system |
| 52 | `CG.ENHLIFO.TOT.FC.LOST.SEC.CCY` | `CgTxnBaseEnhlifo_TotFcLostSecCcy` | TField |  | This field will hold the total lost Franking Credits in security Currency Validation Rules Noinput field.Updated by the system |
| 53 | `CG.ENHLIFO.TOT.FC.LOST.LCY` | `CgTxnBaseEnhlifo_TotFcLostLcy` | TField |  | This field will hold the total lost Franking Credits in local Currency Validation Rules Noinput field.Updated by the system |
| 54 | `CG.ENHLIFO.RESERVED15` | `CgTxnBaseEnhlifo_Reserved15` | TField |  |  |
| 55 | `CG.ENHLIFO.RESERVED14` | `CgTxnBaseEnhlifo_Reserved14` | TField |  |  |
| 56 | `CG.ENHLIFO.RESERVED13` | `CgTxnBaseEnhlifo_Reserved13` | TField |  |  |
| 57 | `CG.ENHLIFO.RESERVED12` | `CgTxnBaseEnhlifo_Reserved12` | TField |  |  |
| 58 | `CG.ENHLIFO.RESERVED11` | `CgTxnBaseEnhlifo_Reserved11` | TField |  |  |
| 59 | `CG.ENHLIFO.RESERVED10` | `CgTxnBaseEnhlifo_Reserved10` | TField |  |  |
| 60 | `CG.ENHLIFO.RESERVED9` | `CgTxnBaseEnhlifo_Reserved9` | TField |  |  |
| 61 | `CG.ENHLIFO.RESERVED8` | `CgTxnBaseEnhlifo_Reserved8` | TField |  |  |
| 62 | `CG.ENHLIFO.RESERVED7` | `CgTxnBaseEnhlifo_Reserved7` | TField |  |  |
| 63 | `CG.ENHLIFO.RESERVED6` | `CgTxnBaseEnhlifo_Reserved6` | TField |  |  |
| 64 | `CG.ENHLIFO.RESERVED5` | `CgTxnBaseEnhlifo_Reserved5` | TField |  |  |
| 65 | `CG.ENHLIFO.RESERVED4` | `CgTxnBaseEnhlifo_Reserved4` | TField |  |  |
| 66 | `CG.ENHLIFO.RESERVED3` | `CgTxnBaseEnhlifo_Reserved3` | TField |  |  |
| 67 | `CG.ENHLIFO.RESERVED2` | `CgTxnBaseEnhlifo_Reserved2` | TField |  |  |
| 68 | `CG.ENHLIFO.RESERVED1` | `CgTxnBaseEnhlifo_Reserved1` | TField |  |  |
| 69 | `CG.ENHLIFO.LOCAL.REF` | `CgTxnBaseEnhlifo_LocalRef` |  |  |  |
| 70 | `CG.ENHLIFO.OVERRIDE` | `CgTxnBaseEnhlifo_Override` |  |  |  |
| 71 | `CG.ENHLIFO.RECORD.STATUS` | `CgTxnBaseEnhlifo_RecordStatus` | String |  |  |
| 72 | `CG.ENHLIFO.CURR.NO` | `CgTxnBaseEnhlifo_CurrNo` | String |  |  |
| 73 | `CG.ENHLIFO.INPUTTER` | `CgTxnBaseEnhlifo_Inputter` |  |  |  |
| 74 | `CG.ENHLIFO.DATE.TIME` | `CgTxnBaseEnhlifo_DateTime` |  |  |  |
| 75 | `CG.ENHLIFO.AUTHORISER` | `CgTxnBaseEnhlifo_Authoriser` | String |  |  |
| 76 | `CG.ENHLIFO.CO.CODE` | `CgTxnBaseEnhlifo_CoCode` | String |  |  |
| 77 | `CG.ENHLIFO.DEPT.CODE` | `CgTxnBaseEnhlifo_DeptCode` | String |  |  |
| 78 | `CG.ENHLIFO.AUDITOR.CODE` | `CgTxnBaseEnhlifo_AuditorCode` | String |  |  |
| 79 | `CG.ENHLIFO.AUDIT.DATE.TIME` | `CgTxnBaseEnhlifo_AuditDateTime` | String |  |  |
| 80 | `CG.ENHLIFO.SETT.CURRENCY` | `CgTxnBaseEnhlifo_SettCurrency` | TField |  | If CURRENCY is a restricted Currency, then this field contains the Settlement Currency. |
| 81 | `CG.ENHLIFO.SETT.EXCH.RATE` | `CgTxnBaseEnhlifo_SettExchRate` | TField |  | If CURRENCY is a restricted Currency,then this field contains the Exchange Rate between CURRENCY andSETT.CURRENCY. |
| 82 | `CG.ENHLIFO.FRANKED.CREDIT.RATE` | `CgTxnBaseEnhlifo_FrankedCreditRate` | TField |  | This field will hold Franking credit rate for computing the franking credit amount for the lot |
| 83 | `CG.ENHLIFO.UNFRANKED.RATE` | `CgTxnBaseEnhlifo_UnfrankedRate` | TField |  | This field will hold the Unfranked credit rate for computing the un-frankedCFI for the tax lot |
| 84 | `CG.ENHLIFO.UNFRANKED.CFI.RATE` | `CgTxnBaseEnhlifo_UnfrankedCfiRate` | TField |  | This field will hold the Unfranked Conduit Foreign Income rate used for computing theUNFRANKED.CFI amount |
| 85 | `CG.ENHLIFO.QUALIFY.HOLDING` | `CgTxnBaseEnhlifo_QualifyHolding` | TField |  | This field will hold the Qualify holding on which the franking details are computed |
