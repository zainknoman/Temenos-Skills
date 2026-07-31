# SC.SOO.CUST.DETAIL — Table Schema

> Source: `INSERTS/I_F.SC.SOO.CUST.DETAIL` in `SC_SctServiceBasedOrders.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.SCD.SECURITY.NO` | `ScSooCustDetail_SecurityNo` | TField |  | Security Number as entered in ORDER.BY.CUST |
| 2 | `SC.SCD.CUST.NUMBER` | `ScSooCustDetail_CustNumber` | TField |  | Identifies the Customer with whom the trade is made. |
| 3 | `SC.SCD.TRANSACTION.CODE` | `ScSooCustDetail_TransactionCode` | TField |  | This is the transaction code as passed through by SC.OBC.CUST.DETAIL i.e. BUY / SELL |
| 4 | `SC.SCD.SECURITY.ACCNT` | `ScSooCustDetail_SecurityAccnt` | TField |  | Portfolio Number |
| 5 | `SC.SCD.NO.NOMINAL` | `ScSooCustDetail_NoNominal` | TField |  | Specifies the Nominal Amount of the Security to be bought or sold. |
| 6 | `SC.SCD.RESERVED50` | `ScSooCustDetail_Reserved50` | TField |  |  |
| 7 | `SC.SCD.CURR.PRICE` | `ScSooCustDetail_CurrPrice` | TField |  | If ORDER.TYPE field is set to 'CASH' then this field is used to calculate how much nominal to trade, calculated from the CU.CASH.AMOUNT field. If the record was created by the ORDER.BY.CUST application then this field will be defaulted from either the MARKET.PRICE or MARKET.PRICE.CR depending on the type of trade. If this field is left blank then it will defaulted from the LAST.PRICE field in the SECURITY.MASTER record. |
| 8 | `SC.SCD.RESERVED49` | `ScSooCustDetail_Reserved49` | TField |  |  |
| 9 | `SC.SCD.RESERVED48` | `ScSooCustDetail_Reserved48` | TField |  |  |
| 10 | `SC.SCD.RESERVED47` | `ScSooCustDetail_Reserved47` | TField |  |  |
| 11 | `SC.SCD.RESERVED46` | `ScSooCustDetail_Reserved46` | TField |  |  |
| 12 | `SC.SCD.RESERVED45` | `ScSooCustDetail_Reserved45` | TField |  |  |
| 13 | `SC.SCD.RESERVED44` | `ScSooCustDetail_Reserved44` | TField |  |  |
| 14 | `SC.SCD.CUST.ACC.NO` | `ScSooCustDetail_CustAccNo` | TField |  | Identifies the customer's account over which the financial entries relative to the underlying transaction are to be passed. Will default according to the definitions recorded in the customer's portfolio as defined in the SECURITY.ACCNT field. |
| 15 | `SC.SCD.CU.EX.RATE.ACC` | `ScSooCustDetail_CuExRateAcc` | TField |  | This field contains the exchange rate applicable between the currency of the customer's account and the settlement currency of the transaction. Defaults to the current rate calculated using the currency files |
| 16 | `SC.SCD.SETTLEMENT.CCY` | `ScSooCustDetail_SettlementCcy` | TField |  | Settlement Currency |
| 17 | `SC.SCD.RESERVED43` | `ScSooCustDetail_Reserved43` | TField |  |  |
| 18 | `SC.SCD.RESERVED42` | `ScSooCustDetail_Reserved42` | TField |  |  |
| 19 | `SC.SCD.RESERVED41` | `ScSooCustDetail_Reserved41` | TField |  |  |
| 20 | `SC.SCD.RESERVED40` | `ScSooCustDetail_Reserved40` | TField |  |  |
| 21 | `SC.SCD.RESERVED39` | `ScSooCustDetail_Reserved39` | TField |  |  |
| 22 | `SC.SCD.RESERVED38` | `ScSooCustDetail_Reserved38` | TField |  |  |
| 23 | `SC.SCD.RESERVED37` | `ScSooCustDetail_Reserved37` | TField |  |  |
| 24 | `SC.SCD.RESERVED36` | `ScSooCustDetail_Reserved36` | TField |  |  |
| 25 | `SC.SCD.RESERVED35` | `ScSooCustDetail_Reserved35` | TField |  |  |
| 26 | `SC.SCD.RESERVED34` | `ScSooCustDetail_Reserved34` | TField |  |  |
| 27 | `SC.SCD.RESERVED33` | `ScSooCustDetail_Reserved33` | TField |  |  |
| 28 | `SC.SCD.RESERVED32` | `ScSooCustDetail_Reserved32` | TField |  |  |
| 29 | `SC.SCD.RESERVED31` | `ScSooCustDetail_Reserved31` | TField |  |  |
| 30 | `SC.SCD.RESERVED30` | `ScSooCustDetail_Reserved30` | TField |  |  |
| 31 | `SC.SCD.RESERVED29` | `ScSooCustDetail_Reserved29` | TField |  |  |
| 32 | `SC.SCD.RESERVED28` | `ScSooCustDetail_Reserved28` | TField |  |  |
| 33 | `SC.SCD.CU.DEPOSITORY` | `ScSooCustDetail_CuDepository` | TField |  | Identifies where the security is held or is to be held |
| 34 | `SC.SCD.SUB.ACCOUNT` | `ScSooCustDetail_SubAccount` | TField |  | The sub account at the depository where the securities are held or are to be held. |
| 35 | `SC.SCD.EXT.CUSTODIAN` | `ScSooCustDetail_ExtCustodian` | TField |  | To identify the external custodian where position is held. |
| 36 | `SC.SCD.RESERVED24` | `ScSooCustDetail_Reserved24` | TField |  |  |
| 37 | `SC.SCD.RESERVED23` | `ScSooCustDetail_Reserved23` | TField |  |  |
| 38 | `SC.SCD.RESERVED22` | `ScSooCustDetail_Reserved22` | TField |  |  |
| 39 | `SC.SCD.RESERVED21` | `ScSooCustDetail_Reserved21` | TField |  |  |
| 40 | `SC.SCD.SERVICE.REF` | `ScSooCustDetail_ServiceRef` | TField |  | Service reference. This will be the ORDER.BY.CUST key. |
| 41 | `SC.SCD.THREAD.KEY` | `ScSooCustDetail_ThreadKey` | TField |  | Identifies the service agent that created the record. |
| 42 | `SC.SCD.OBC.CUST.DETAIL.ID` | `ScSooCustDetail_ObcCustDetailId` | TField |  | SC.OBC.CUST.DETAIL Key |
| 43 | `SC.SCD.SEC.TRADE.DET.ID` | `ScSooCustDetail_SecTradeDetId` | TField |  | SC.SEC.TRADE.DETAIL ID |
| 44 | `SC.SCD.TRADED.NOM` | `ScSooCustDetail_TradedNom` | TField |  | This is the nominal that has already been traded if a partial has been executed. |
| 45 | `SC.SCD.OUTSTAND.NOM` | `ScSooCustDetail_OutstandNom` | TField |  | The outstanding nominal. This is the amount left over in the order once partial executions have taken place. |
| 46 | `SC.SCD.ORIGINAL.NOM` | `ScSooCustDetail_OriginalNom` | TField |  | Original Nominal as passed through by the SC.OBC.CUST.DETAIL. |
| 47 | `SC.SCD.DEPOSITORY` | `ScSooCustDetail_Depository` | TField |  | The DEPOSITORY as passed through by the SC.OBC.CUST.DETAIL record |
| 48 | `SC.SCD.RESERVED16` | `ScSooCustDetail_Reserved16` | TField |  |  |
| 49 | `SC.SCD.ORDER.TYPE` | `ScSooCustDetail_OrderType` | TField | Yes | Details the type of Order being passed to the Dealers. Whether buy or sell at BEST or at MARKET. A buy or sell instruction to a dealer with the "at Market" flag signifies that there is no limit or restriction on the price at which he can execute the transaction. The client or investment manager is happy with the market price. Best price indicates that the dealer ought really to "shop" around for his price as there may be a lot of activity and consequently differing prices to be achieved. Price indicates that the price input within field 9 is a minimum or maximum price to be paid or received for the securities stipulated. LIMIT.PRICE is mandatory input for both Price and Stop kind of order types. Cash indicates that the customer wants to trade a particular amount of cash in the transaction. The nominal will be calculated from this cash amount &amp; can either be net or gross of charges/commissions. This is controlled by the CASH.CHRGS field. The type of order is determined based on the specifications for various order types in SC.ORDER.TYPE file. System-generated field only. |
| 50 | `SC.SCD.TRADE.CCY` | `ScSooCustDetail_TradeCcy` | TField |  | Specifies the currency in which the transaction will be settled. The trade currency is the settlement currency for the Broker involved. As with the SEC.TRADE application it determines the currency of the account to which the Broker Net amount is posted. The customer however can be debited in a different currency. System-generated field only. |
| 51 | `SC.SCD.LIMIT.PRICE` | `ScSooCustDetail_LimitPrice` | TField |  | The Price at which the shares are to be bought or sold. This can be used in conjunction with field ORDER.TYPE to inform the Dealers of a Limit price to be reached before the transaction should be executed. When this value is left blank, with field ORDER.TYPE set to "M", it indicates that the securities are to be bought or sold at Market. If field ORDER.TYPE is set to "P", and this field is entered, then the instructions to the Dealer are to trade, but only, at the price stipulated. Dealers will rarely accept open ended Limit instructions as it places a heavy burden on them. System-generated field only. |
| 52 | `SC.SCD.LIMIT.TYPE` | `ScSooCustDetail_LimitType` | TField |  | Field used to default the LIMIT.DATE field. Input of GTD, GTM, GTY or GTW allowed. GTD - Order valid until the order date. GTW - Order valid for seven calendar days from order date. GTM - Order valid until the end of the month of the order date. GTY - Order valid until the end of the year of the order date. System-generated field only. |
| 53 | `SC.SCD.LIMIT.EXP.DATE` | `ScSooCustDetail_LimitExpDate` | TField |  | This field specifies the validity of the Limit, i.e. how long is it to remain in force. The validity of that date will depend very much on work and local practices. System-generated field only. |
| 54 | `SC.SCD.CU.INCOME.ACC` | `ScSooCustDetail_CuIncomeAcc` | TField |  | Income account to which charge are to be posted. |
| 55 | `SC.SCD.CU.INCOME.CCY` | `ScSooCustDetail_CuIncomeCcy` | TField |  | Currency of income account. |
| 56 | `SC.SCD.RESERVED08` | `ScSooCustDetail_Reserved08` | TField |  |  |
| 57 | `SC.SCD.RESERVED07` | `ScSooCustDetail_Reserved07` | TField |  |  |
| 58 | `SC.SCD.RESERVED06` | `ScSooCustDetail_Reserved06` | TField |  |  |
| 59 | `SC.SCD.RESERVED05` | `ScSooCustDetail_Reserved05` | TField |  |  |
| 60 | `SC.SCD.RESERVED04` | `ScSooCustDetail_Reserved04` | TField |  |  |
| 61 | `SC.SCD.RESERVED03` | `ScSooCustDetail_Reserved03` | TField |  |  |
| 62 | `SC.SCD.RESERVED02` | `ScSooCustDetail_Reserved02` | TField |  |  |
| 63 | `SC.SCD.RESERVED01` | `ScSooCustDetail_Reserved01` | TField |  |  |
| 64 | `SC.SCD.LOCAL.REF` | `ScSooCustDetail_LocalRef` |  |  |  |
| 65 | `SC.SCD.OVERRIDE` | `ScSooCustDetail_Override` |  |  |  |
| 66 | `SC.SCD.RECORD.STATUS` | `ScSooCustDetail_RecordStatus` | String |  |  |
| 67 | `SC.SCD.CURR.NO` | `ScSooCustDetail_CurrNo` | String |  |  |
| 68 | `SC.SCD.INPUTTER` | `ScSooCustDetail_Inputter` |  |  |  |
| 69 | `SC.SCD.DATE.TIME` | `ScSooCustDetail_DateTime` |  |  |  |
| 70 | `SC.SCD.AUTHORISER` | `ScSooCustDetail_Authoriser` | String |  |  |
| 71 | `SC.SCD.CO.CODE` | `ScSooCustDetail_CoCode` | String |  |  |
| 72 | `SC.SCD.DEPT.CODE` | `ScSooCustDetail_DeptCode` | String |  |  |
| 73 | `SC.SCD.AUDITOR.CODE` | `ScSooCustDetail_AuditorCode` | String |  |  |
| 74 | `SC.SCD.AUDIT.DATE.TIME` | `ScSooCustDetail_AuditDateTime` | String |  |  |
