# BL.BALANCES — Table Schema

> Source: `INSERTS/I_F.BL.BALANCES` in `BL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BL.BAL.CONTRACT.ID` | `BlBalances_ContractId` | TField |  | The BL id to which the BR is attached is shown here. |
| 2 | `BL.BAL.OPERATION` | `BlBalances_Operation` | TField |  | The type of the Bill as defined in BTTC will appear in this field. eg. Collateral, Discount, Collection |
| 3 | `BL.BAL.CUSTOMER` | `BlBalances_Customer` | TField |  | The Drawer of the Bill (in case of a customer) or the Liability Customer (in case of a customer) will default in this field for that BR. |
| 4 | `BL.BAL.CURRENCY` | `BlBalances_Currency` | TField |  | The currency of the Bill Register will appear in this field |
| 5 | `BL.BAL.CURRENCY.MARKET` | `BlBalances_CurrencyMarket` | TField |  | The currency market defined while BL application will appear in this field |
| 6 | `BL.BAL.POSITION.TYPE` | `BlBalances_PositionType` | TField |  | Position type as defined for the BL contract will appear here. |
| 7 | `BL.BAL.CATEGORY` | `BlBalances_Category` | TField |  | The BL.Bill category will appear in this field. |
| 8 | `BL.BAL.LAST.ACCR.DATE` | `BlBalances_LastAccrDate` | TField |  | The last date up to which the Accrual done for Interest Received in Advance for BL contract of Discount operation. |
| 9 | `BL.BAL.PRINCIPAL` | `BlBalances_Principal` | TField |  | The Principal amount of the BL.Register will appear in this field. |
| 10 | `BL.BAL.START.DATE` | `BlBalances_StartDate` | TField |  | The start date of the Bill as defined in BR will appear in this field |
| 11 | `BL.BAL.END.DATE` | `BlBalances_EndDate` | TField |  | The Maturity date of the Bill as defined in the BR will appear in this field |
| 12 | `BL.BAL.PROJ.ACCR.AMT` | `BlBalances_ProjAccrAmt` | TField |  | This is the total Discount amount collected upfront from the customer for the actual no of days of the contract (Not including the Grace days) |
| 13 | `BL.BAL.DAILY.ACCR.AMT` | `BlBalances_DailyAccrAmt` | TField |  | This is the amount that has to be accrued daily. |
| 14 | `BL.BAL.ACCRUED.AMT` | `BlBalances_AccruedAmt` | TField |  | This field shows the amount accrued up to date as specified in the last accrual date. |
| 15 | `BL.BAL.GRACE.DAYS` | `BlBalances_GraceDays` | TField |  | Currently not used |
| 16 | `BL.BAL.TOT.GRACE.AMT` | `BlBalances_TotGraceAmt` | TField |  | This field shows the total Interest collected upfront for the Grace days. However the Grace days interest received in advance will be accrued on the last working day before the maturity of the contract. |
| 17 | `BL.BAL.DAILY.GRACE.AMT` | `BlBalances_DailyGraceAmt` | TField |  | This field shows the daily accrual to be done for the Grace days. |
| 18 | `BL.BAL.TAX.INT.AMT` | `BlBalances_TaxIntAmt` | TField |  | Currently not used |
| 19 | `BL.BAL.DAYS.ACCRUED` | `BlBalances_DaysAccrued` | TField |  | Currently not used. |
| 20 | `BL.BAL.INT.RATE` | `BlBalances_IntRate` | TField |  | This field shows the effective interest rate as specified in the respective BL.BILL. |
| 21 | `BL.BAL.INT.KEY` | `BlBalances_IntKey` | TField |  | This field shows the Interest key applicable for the BL.BILL Contract. |
| 22 | `BL.BAL.INT.BASIS` | `BlBalances_IntBasis` | TField |  | Interest Basis as defined in the BL.BILL will be defaulted here. |
| 23 | `BL.BAL.INT.SPREAD` | `BlBalances_IntSpread` | TField |  | Interest spread as defined in the BL.BILL contract defaulted here. |
| 24 | `BL.BAL.LIQ.MODE` | `BlBalances_LiqMode` | TField |  | The Liquidation Mode (Automatic, Semi-Automatic or Manual) as defined in the BR/BL will appear in this field. |
| 25 | `BL.BAL.MARGIN.PERCENT` | `BlBalances_MarginPercent` | TField |  | Currently not used |
| 26 | `BL.BAL.ACCOUNT.OFFICER` | `BlBalances_AccountOfficer` | TField |  | Account officer as defined in the BL gets defaulted here. |
| 27 | `BL.BAL.MARGIN.AMT` | `BlBalances_MarginAmt` | TField |  | HCurrently not used |
| 28 | `BL.BAL.LOCAL.REF` | `BlBalances_LocalRef` |  |  |  |
| 29 | `BL.BAL.EFF.PRINCIPAL` | `BlBalances_EffPrincipal` |  |  |  |
| 30 | `BL.BAL.EFF.DATE` | `BlBalances_EffDate` |  |  |  |
| 31 | `BL.BAL.SAVE.EXCH.RATE` | `BlBalances_SaveExchRate` |  |  |  |
| 32 | `BL.BAL.RESERVED17` | `BlBalances_Reserved17` |  |  |  |
| 33 | `BL.BAL.SUSP.INT.AMT` | `BlBalances_SuspIntAmt` | TField |  | When the unamortised discount interest portion is suspended, then this field holds the total suspended interest amount until it is recognized. This shall be reversed during any of below events happened in an invoice. 1) Maturity or settlement with liquidation mode as AUTOMATIC. 2) When the SUSPEND.INT is marked from YES to NO. 3) Underlying PD is settled or written off. |
| 34 | `BL.BAL.RESERVED15` | `BlBalances_Reserved15` | TField |  |  |
| 35 | `BL.BAL.RESERVED14` | `BlBalances_Reserved14` | TField |  |  |
| 36 | `BL.BAL.RESERVED13` | `BlBalances_Reserved13` | TField |  |  |
| 37 | `BL.BAL.RESERVED12` | `BlBalances_Reserved12` | TField |  |  |
| 38 | `BL.BAL.RESERVED11` | `BlBalances_Reserved11` | TField |  |  |
| 39 | `BL.BAL.RESERVED10` | `BlBalances_Reserved10` | TField |  |  |
| 40 | `BL.BAL.RESERVED9` | `BlBalances_Reserved9` | TField |  |  |
| 41 | `BL.BAL.RESERVED8` | `BlBalances_Reserved8` | TField |  |  |
| 42 | `BL.BAL.RESERVED7` | `BlBalances_Reserved7` | TField |  |  |
| 43 | `BL.BAL.RESERVED6` | `BlBalances_Reserved6` | TField |  |  |
| 44 | `BL.BAL.RESERVED5` | `BlBalances_Reserved5` | TField |  |  |
| 45 | `BL.BAL.RESERVED4` | `BlBalances_Reserved4` | TField |  |  |
| 46 | `BL.BAL.RESERVED3` | `BlBalances_Reserved3` | TField |  |  |
| 47 | `BL.BAL.RESERVED2` | `BlBalances_Reserved2` | TField |  |  |
| 48 | `BL.BAL.RESERVED1` | `BlBalances_Reserved1` | TField |  |  |
| 49 | `BL.BAL.CONSOL.KEY` | `BlBalances_ConsolKey` | TField |  | The Consol key ( key of the consolidation record in the CONSOLIDATE.ASST.LIAB file) will appear in this column Validation Rules: Internal field |
| 50 | `BL.BAL.REC.STATUS` | `BlBalances_RecStatus` | TField |  | The present status of the Bill will appear in this field. The following are the details of status, maintained by the system : CURR: The bill is in live status REVE: The bill is reversed status LIQ: The bill is in liquidated status Validation Rule This is an internal file. |
