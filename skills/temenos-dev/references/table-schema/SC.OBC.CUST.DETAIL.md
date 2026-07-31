# SC.OBC.CUST.DETAIL — Table Schema

> Source: `INSERTS/I_F.SC.OBC.CUST.DETAIL` in `SC_SctServiceBasedOrders.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.OCD.CUSTOMER.NO` | `ScObcCustDetail_CustomerNo` | TField |  | Customer Number. |
| 2 | `SC.OCD.SECURITY.NO` | `ScObcCustDetail_SecurityNo` | TField |  | The Security Number of the Order to be Generated Validation Rules: Must be a valid SECURITY.MASTER code Must match the details on the associated ORDER.BY.CUST record |
| 3 | `SC.OCD.SECURITY.ACCOUNT` | `ScObcCustDetail_SecurityAccount` | TField |  | Portfolio Number Cannot be a memo account or a dealer book portfolio. |
| 4 | `SC.OCD.RESERVED48` | `ScObcCustDetail_Reserved48` | TField |  |  |
| 5 | `SC.OCD.VALUE` | `ScObcCustDetail_Value` | TField |  | Value of the transaction as calculated by ORDER.BY.CUST service. For debit orders this will be the nominal holding, for credit orders this will be the valuation amount. |
| 6 | `SC.OCD.TRANSACTION.CODE` | `ScObcCustDetail_TransactionCode` | TField |  | Transaction Code. This will be as input in the ORDER.BY.CUST record. i.e. BUY/SELL/TRI/TRO, Depending on whether it is a credit or debit transaction. Must match the details on the associated ORDER.BY.CUST record |
| 7 | `SC.OCD.THEOR.NOM` | `ScObcCustDetail_TheorNom` | TField |  | The Nominal as calculated in ORDER.BY.CUST before applying any rounding factors. |
| 8 | `SC.OCD.NOMINAL` | `ScObcCustDetail_Nominal` | TField |  | Modified Nominal taking into account of the Rounding Factors. Validation Rules: This field may be modified by the user. Must be multiples of the security trading units. |
| 9 | `SC.OCD.EXT.CUSTODIAN` | `ScObcCustDetail_ExtCustodian` | TField |  | To identify the external custodian where position is held. |
| 10 | `SC.OCD.RESERVED44` | `ScObcCustDetail_Reserved44` | TField |  |  |
| 11 | `SC.OCD.RESERVED43` | `ScObcCustDetail_Reserved43` | TField |  |  |
| 12 | `SC.OCD.RESERVED42` | `ScObcCustDetail_Reserved42` | TField |  |  |
| 13 | `SC.OCD.RESERVED41` | `ScObcCustDetail_Reserved41` | TField |  |  |
| 14 | `SC.OCD.RESERVED40` | `ScObcCustDetail_Reserved40` | TField |  |  |
| 15 | `SC.OCD.RESERVED39` | `ScObcCustDetail_Reserved39` | TField |  |  |
| 16 | `SC.OCD.RESERVED38` | `ScObcCustDetail_Reserved38` | TField |  |  |
| 17 | `SC.OCD.RESERVED37` | `ScObcCustDetail_Reserved37` | TField |  |  |
| 18 | `SC.OCD.RESERVED36` | `ScObcCustDetail_Reserved36` | TField |  |  |
| 19 | `SC.OCD.RESERVED35` | `ScObcCustDetail_Reserved35` | TField |  |  |
| 20 | `SC.OCD.RESERVED34` | `ScObcCustDetail_Reserved34` | TField |  |  |
| 21 | `SC.OCD.RESERVED33` | `ScObcCustDetail_Reserved33` | TField |  |  |
| 22 | `SC.OCD.RESERVED32` | `ScObcCustDetail_Reserved32` | TField |  |  |
| 23 | `SC.OCD.RESERVED31` | `ScObcCustDetail_Reserved31` | TField |  |  |
| 24 | `SC.OCD.RESERVED30` | `ScObcCustDetail_Reserved30` | TField |  |  |
| 25 | `SC.OCD.RESERVED29` | `ScObcCustDetail_Reserved29` | TField |  |  |
| 26 | `SC.OCD.RESERVED28` | `ScObcCustDetail_Reserved28` | TField |  |  |
| 27 | `SC.OCD.MARKET.VALUE` | `ScObcCustDetail_MarketValue` | TField |  | Market Value of the Order Nominal NOINPUT field. |
| 28 | `SC.OCD.PORT.PERCENT` | `ScObcCustDetail_PortPercent` | TField |  | The percentage of the portfolio valuation of the order nominal. NOINPUT field. |
| 29 | `SC.OCD.DEPOSITORY` | `ScObcCustDetail_Depository` | TField |  | For Sale Orders - This is the Depository of the existing Security.Position Validation Rules: Must be a depository as specified in CUSTOMER.SECURITY |
| 30 | `SC.OCD.RESERVED25` | `ScObcCustDetail_Reserved25` | TField |  |  |
| 31 | `SC.OCD.RESERVED24` | `ScObcCustDetail_Reserved24` | TField |  |  |
| 32 | `SC.OCD.RESERVED23` | `ScObcCustDetail_Reserved23` | TField |  |  |
| 33 | `SC.OCD.RESERVED22` | `ScObcCustDetail_Reserved22` | TField |  |  |
| 34 | `SC.OCD.RESERVED21` | `ScObcCustDetail_Reserved21` | TField |  |  |
| 35 | `SC.OCD.SERVICE.REF` | `ScObcCustDetail_ServiceRef` | TField |  | Service Reference. the ORDER.BY.CUST ID to which the record relates. Must exist as an unauthorised record. |
| 36 | `SC.OCD.THREAD.KEY` | `ScObcCustDetail_ThreadKey` | TField |  | Thread Key, this identifies the service agent that built the record. |
| 37 | `SC.OCD.SOO.CUST.DETAIL.ID` | `ScObcCustDetail_SooCustDetailId` | TField |  | SC.SOO.CUST.DETAIL.KEY |
| 38 | `SC.OCD.TRADE.CCY` | `ScObcCustDetail_TradeCcy` | TField |  | The trade currency for the ORDER.BY.CUST. Will be defaulted from the ORDER.TYPE and the security field SECURITY.CURRENCY. NOINPUT field |
| 39 | `SC.OCD.RESERVED19` | `ScObcCustDetail_Reserved19` | TField |  |  |
| 40 | `SC.OCD.RESERVED18` | `ScObcCustDetail_Reserved18` | TField |  |  |
| 41 | `SC.OCD.RESERVED17` | `ScObcCustDetail_Reserved17` | TField |  |  |
| 42 | `SC.OCD.RESERVED16` | `ScObcCustDetail_Reserved16` | TField |  |  |
| 43 | `SC.OCD.RESERVED15` | `ScObcCustDetail_Reserved15` | TField |  |  |
| 44 | `SC.OCD.RESERVED14` | `ScObcCustDetail_Reserved14` | TField |  |  |
| 45 | `SC.OCD.RESERVED13` | `ScObcCustDetail_Reserved13` | TField |  |  |
| 46 | `SC.OCD.RESERVED12` | `ScObcCustDetail_Reserved12` | TField |  |  |
| 47 | `SC.OCD.RESERVED11` | `ScObcCustDetail_Reserved11` | TField |  |  |
| 48 | `SC.OCD.RESERVED10` | `ScObcCustDetail_Reserved10` | TField |  |  |
| 49 | `SC.OCD.RESERVED09` | `ScObcCustDetail_Reserved09` | TField |  |  |
| 50 | `SC.OCD.RESERVED08` | `ScObcCustDetail_Reserved08` | TField |  |  |
| 51 | `SC.OCD.RESERVED07` | `ScObcCustDetail_Reserved07` | TField |  |  |
| 52 | `SC.OCD.RESERVED06` | `ScObcCustDetail_Reserved06` | TField |  |  |
| 53 | `SC.OCD.RESERVED05` | `ScObcCustDetail_Reserved05` | TField |  |  |
| 54 | `SC.OCD.RESERVED04` | `ScObcCustDetail_Reserved04` | TField |  |  |
| 55 | `SC.OCD.RESERVED03` | `ScObcCustDetail_Reserved03` | TField |  |  |
| 56 | `SC.OCD.RESERVED02` | `ScObcCustDetail_Reserved02` | TField |  |  |
| 57 | `SC.OCD.RESERVED01` | `ScObcCustDetail_Reserved01` | TField |  |  |
| 58 | `SC.OCD.LOCAL.REF` | `ScObcCustDetail_LocalRef` |  |  |  |
| 59 | `SC.OCD.OVERRIDE` | `ScObcCustDetail_Override` |  |  |  |
| 60 | `SC.OCD.RECORD.STATUS` | `ScObcCustDetail_RecordStatus` | String |  |  |
| 61 | `SC.OCD.CURR.NO` | `ScObcCustDetail_CurrNo` | String |  |  |
| 62 | `SC.OCD.INPUTTER` | `ScObcCustDetail_Inputter` |  |  |  |
| 63 | `SC.OCD.DATE.TIME` | `ScObcCustDetail_DateTime` |  |  |  |
| 64 | `SC.OCD.AUTHORISER` | `ScObcCustDetail_Authoriser` | String |  |  |
| 65 | `SC.OCD.CO.CODE` | `ScObcCustDetail_CoCode` | String |  |  |
| 66 | `SC.OCD.DEPT.CODE` | `ScObcCustDetail_DeptCode` | String |  |  |
| 67 | `SC.OCD.AUDITOR.CODE` | `ScObcCustDetail_AuditorCode` | String |  |  |
| 68 | `SC.OCD.AUDIT.DATE.TIME` | `ScObcCustDetail_AuditDateTime` | String |  |  |
