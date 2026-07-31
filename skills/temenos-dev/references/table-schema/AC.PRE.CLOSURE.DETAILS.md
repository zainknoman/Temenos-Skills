# AC.PRE.CLOSURE.DETAILS — Table Schema

> Source: `INSERTS/I_F.AC.PRE.CLOSURE.DETAILS` in `AC_AccountClosure.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `APCL.CAPITAL.DATE` | `AcPreClosureDetails_CapitalDate` | TField |  | The date specified for the interest and charges capitalisation during the closure process Validation rules No input - this will default to the current system date. |
| 2 | `APCL.OPEN.ACTUAL.BAL` | `AcPreClosureDetails_OpenActualBal` | TField |  | Contains the Open Actual Balance on the account at the time the simulation is run. Validation rules No input |
| 3 | `APCL.OPEN.CLEARED.BAL` | `AcPreClosureDetails_OpenClearedBal` | TField |  | Contains the Open Cleared Balance on the account at the time the simulation is run. Validation rules No input field |
| 4 | `APCL.ONLINE.ACTUAL.BAL` | `AcPreClosureDetails_OnlineActualBal` | TField |  | Contains the current Online&#160;Actual Balance on the Account at the time the simulation is run. Validation rules No Input field |
| 5 | `APCL.ONLINE.CLEARED.BAL` | `AcPreClosureDetails_OnlineClearedBal` | TField |  | Contains the current Online Cleared Balance on the account at the time the simulation is run. Validation rules No input field |
| 6 | `APCL.STANDING.ORDERS` | `AcPreClosureDetails_StandingOrders` | TField |  | Indicates whether or not there are any existing standing orders for this account. It will hold a value of either Yes or No. Validation rules No Input field |
| 7 | `APCL.UNCLEARED.ENTRIES` | `AcPreClosureDetails_UnclearedEntries` | TField |  | Indicates whether or not there were any existing un-cleared entries for the account. It will hold the value Yes or No Validation rules No input field |
| 8 | `APCL.TOTAL.CR.INTEREST` | `AcPreClosureDetails_TotalCrInterest` | TField |  | The total amount of outstanding credit and credit interest 2 calculated up to the specified capitalisation date Validation rules No input field |
| 9 | `APCL.TOTAL.DR.INTEREST` | `AcPreClosureDetails_TotalDrInterest` | TField |  | The total amount of debit and debit interest 2 calculated up to the specified capitalisation date. Validation rules No input field |
| 10 | `APCL.TOTAL.PENDING.DR` | `AcPreClosureDetails_TotalPendingDr` | TField |  | This reflects the total DR interest that is pending or this account Validation rules No input field |
| 11 | `APCL.TOTAL.CHARGES` | `AcPreClosureDetails_TotalCharges` | TField |  | The total amount of outstanding account ledger charges and interest related charges calculates up to the specified capitalisation date. Validation rules No input field |
| 12 | `APCL.TOTAL.PENDING.CHG` | `AcPreClosureDetails_TotalPendingChg` | TField |  | This field reflects the total charges pending on the account at the time the simulation is run. Validation rules No input field |
| 13 | `APCL.TOTAL.TAX` | `AcPreClosureDetails_TotalTax` | TField |  | This field contains the total amount of Tax outstanding on interest and charges calculated up to the specified capitalisation date. Validation rules No input field |
| 14 | `APCL.TOTAL.PENDING.TAX` | `AcPreClosureDetails_TotalPendingTax` | TField |  | This field reflects the total tax pending on the account. Validation rules No input field |
| 15 | `APCL.ACCT.LIQUIDATED.TO` | `AcPreClosureDetails_AcctLiquidatedTo` | TField |  | If interest and charges are to be booked to another ACCOUNT, this field contains the number of the ACCOUNT to which they will be booked. This is the Liquidity Account specified in the INTEREST LIQU ACCT field of the originating ACCOUNT record. Validation rules No input field |
| 16 | `APCL.CURRENCY` | `AcPreClosureDetails_Currency` | TField |  | This field holds the currency of the account. Validation rules No input field &#160; |
| 17 | `APCL.SETTLEMENT.ACCT` | `AcPreClosureDetails_SettlementAcct` | TField |  | This field is current not used for the simulation Validation rules No input field |
| 18 | `APCL.CHEQUES.OS` | `AcPreClosureDetails_ChequesOs` | TField |  | This field indicates whether there are any outstanding cheques for this account or not. Validation rules No input field |
| 19 | `APCL.BANK.CARDS` | `AcPreClosureDetails_BankCards` |  |  |  |
| 20 | `APCL.CC.CHGS.OS` | `AcPreClosureDetails_CcChgsOs` | TField |  | The total of any uncollected cheque and/or card changes. Validation rules 1-19 standard amount format |
| 21 | `APCL.BC.BANK.SORT.CODE` | `AcPreClosureDetails_BcBankSortCode` | TField |  | This field is current not used for the simulation Validation rules No input field |
| 22 | `APCL.ACCT.LIQU.CURRENCY` | `AcPreClosureDetails_AcctLiquCurrency` | TField |  | Identifies the currency of the account liquidated to in field ACCT.LIQUIDATED.TO. This is the Interest currency, if any, specified in the originating ACCOUNT record. Validation rules No input field |
| 23 | `APCL.POSTING.RESTRICT` | `AcPreClosureDetails_PostingRestrict` | TField |  |  |
| 24 | `APCL.TOTAL.PREMIUM.AMT` | `AcPreClosureDetails_TotalPremiumAmt` | TField |  | This field contains the total amount of premium interest calculated up to the capitalisation date. Validation rules No input field |
| 25 | `APCL.TOTAL.ACC.AMT` | `AcPreClosureDetails_TotalAccAmt` | TField |  | This field defines the total balance amount to the account inclusive of all charges and interest applicable at present. Validation rules No input field |
| 26 | `APCL.CHARGEABLE.AMT` | `AcPreClosureDetails_ChargeableAmt` | TField |  | Defines the balance on the account on which closing penalty needs to be applied. Validation rules No input field |
| 27 | `APCL.CLO.CHARGE.TYPE` | `AcPreClosureDetails_CloChargeType` | TField |  | This field is current not used for the simulation Validation rules No input field |
| 28 | `APCL.CLO.CHARGE.AMT` | `AcPreClosureDetails_CloChargeAmt` | TField |  | This field is current not used for the simulation Validation rules No input field |
| 29 | `APCL.CLO.CH.TAX.TYPE` | `AcPreClosureDetails_CloChTaxType` | TField |  | This field is current not used for the simulation Validation rules No input field |
| 30 | `APCL.CLO.CH.TAX.AMT` | `AcPreClosureDetails_CloChTaxAmt` | TField |  | This field is current not used for the simulation Validation rules No input field |
| 31 | `APCL.CLO.CHARGE.POSTED` | `AcPreClosureDetails_CloChargePosted` | TField |  | This field is current not used for the simulation Validation rules No input field |
| 32 | `APCL.CAP.INTEREST` | `AcPreClosureDetails_CapInterest` | TField |  | This field defines whether the account will capitalise interest Validation rules Yes |
| 33 | `APCL.LOCAL.REF` | `AcPreClosureDetails_LocalRef` |  |  |  |
| 34 | `APCL.CLOSE.ONLINE` | `AcPreClosureDetails_CloseOnline` | TField |  | This field is current not used for the simulation Validation rules No input field |
| 35 | `APCL.FT.ID` | `AcPreClosureDetails_FtId` | TField |  | This field is current not used for the simulation Validation rules No input field |
| 36 | `APCL.CLOSE.MODE` | `AcPreClosureDetails_CloseMode` | TField |  | This field is current not used for the simulation Validation rules No input field |
| 37 | `APCL.LCCY.CHARGE.AMT` | `AcPreClosureDetails_LccyChargeAmt` | TField |  | This field is current not used for the simulation Validation rules No input field |
| 38 | `APCL.CLOSURE.REASON` | `AcPreClosureDetails_ClosureReason` | TField |  |  |
| 39 | `APCL.CLOSURE.NOTES` | `AcPreClosureDetails_ClosureNotes` |  |  |  |
| 40 | `APCL.RESERVED.3` | `AcPreClosureDetails_Reserved3` | TField |  |  |
| 41 | `APCL.RESERVED.2` | `AcPreClosureDetails_Reserved2` | TField |  |  |
| 42 | `APCL.RESERVED.1` | `AcPreClosureDetails_Reserved1` |  |  |  |
| 43 | `APCL.OVERRIDE` | `AcPreClosureDetails_Override` |  |  |  |
| 44 | `APCL.RECORD.STATUS` | `AcPreClosureDetails_RecordStatus` | String |  |  |
| 45 | `APCL.CURR.NO` | `AcPreClosureDetails_CurrNo` | String |  |  |
| 46 | `APCL.INPUTTER` | `AcPreClosureDetails_Inputter` |  |  |  |
| 47 | `APCL.DATE.TIME` | `AcPreClosureDetails_DateTime` |  |  |  |
| 48 | `APCL.AUTHORISER` | `AcPreClosureDetails_Authoriser` | String |  |  |
| 49 | `APCL.CO.CODE` | `AcPreClosureDetails_CoCode` | String |  |  |
| 50 | `APCL.DEPT.CODE` | `AcPreClosureDetails_DeptCode` | String |  |  |
| 51 | `APCL.AUDITOR.CODE` | `AcPreClosureDetails_AuditorCode` | String |  |  |
| 52 | `APCL.AUDIT.DATE.TIME` | `AcPreClosureDetails_AuditDateTime` | String |  |  |
