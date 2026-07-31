# ALLFND.AFB.LOG — Table Schema

> Source: `INSERTS/I_F.ALLFND.AFB.LOG` in `ALLFND_CustomerOnboarding.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AFB.LOG.AFB.TRANSACTION.ID` | `AllfndAfbLog_AfbTransactionId` | TField |  | Transaction ID provided by the AFB for every transaction that is registered with AFB. |
| 2 | `AFB.LOG.ORDER.DATE` | `AllfndAfbLog_OrderDate` | TField |  |  |
| 3 | `AFB.LOG.VALUE.DATE` | `AllfndAfbLog_ValueDate` | TField |  |  |
| 4 | `AFB.LOG.SOURCE.AFB.CONTRACT.ID` | `AllfndAfbLog_SourceAfbContractId` | TField |  | Unique ID of source portfolio which is provided by AFB at the time of registration. |
| 5 | `AFB.LOG.SOURCE.CCV` | `AllfndAfbLog_SourceCcv` | TField |  | Unique 20 digit number of source portfolio which is geenrated at the time portfolio creation. |
| 6 | `AFB.LOG.CONTRACTID.UPDATE.REQUIRED` | `AllfndAfbLog_ContractidUpdateRequired` | TField |  | Updated by ESB with yes/no. Yes is updated if the AFBContract ID has to be saved in SEC.ACC.MASTER and No in case the AFB contract ID is already available in SEC.ACC.MASTER |
| 7 | `AFB.LOG.CUSTOMER.ID` | `AllfndAfbLog_CustomerId` | TField |  | Record ID of the Customer. |
| 8 | `AFB.LOG.AFB.CLIENT.ID` | `AllfndAfbLog_AfbClientId` |  |  |  |
| 9 | `AFB.LOG.CLIENTID.UPDATE.REQUIRED` | `AllfndAfbLog_ClientidUpdateRequired` | TField |  | Updated by ESB with yes/no. Yes is updated if the AFBClient ID has to be saved in CUSTOMER and No in case the AFBClient ID is already available in CUSTOMER. |
| 10 | `AFB.LOG.HOLDER.CUSTOMERID` | `AllfndAfbLog_HolderCustomerid` |  |  |  |
| 11 | `AFB.LOG.HOLDER.AFBCLIENTID` | `AllfndAfbLog_HolderAfbclientid` |  |  |  |
| 12 | `AFB.LOG.HOLDER.CLIENTID.UPDT.REQ` | `AllfndAfbLog_HolderClientidUpdtReq` |  |  |  |
| 13 | `AFB.LOG.TARGET.AFB.CONTRACTID` | `AllfndAfbLog_TargetAfbContractid` |  |  |  |
| 14 | `AFB.LOG.TARGET.CCV` | `AllfndAfbLog_TargetCcv` |  |  |  |
| 15 | `AFB.LOG.TARGET.CNTRCTID.UPDT.REQ` | `AllfndAfbLog_TargetCntrctidUpdtReq` |  |  |  |
| 16 | `AFB.LOG.STATUS` | `AllfndAfbLog_Status` | TField |  | Status of the request sent to AFB |
| 17 | `AFB.LOG.ERROR.CODE` | `AllfndAfbLog_ErrorCode` | TField |  | Error code returned by AFB during Client, Contract and Order registration |
| 18 | `AFB.LOG.ERROR.REASON` | `AllfndAfbLog_ErrorReason` |  |  |  |
| 19 | `AFB.LOG.APPLICATION` | `AllfndAfbLog_Application` | TField |  | Name of the Application which has triggered the API message to AFB |
| 20 | `AFB.LOG.TRANSACTION.TYPE` | `AllfndAfbLog_TransactionType` | TField |  | Indicates what kind of transaction is being processed |
| 21 | `AFB.LOG.SECURITY.NO` | `AllfndAfbLog_SecurityNo` | TField |  | Identifies the Security that is to be transferred |
| 22 | `AFB.LOG.SECURITY.CCY` | `AllfndAfbLog_SecurityCcy` | TField |  | Specifies the currency of the Security |
| 23 | `AFB.LOG.DEPOSITORY` | `AllfndAfbLog_Depository` | TField |  | Indicates the Depository that the Security is to be delivered from or to. |
| 24 | `AFB.LOG.PRICE.TYPE` | `AllfndAfbLog_PriceType` | TField |  | Specifies the type of price calculation relevant to the Security |
| 25 | `AFB.LOG.COST` | `AllfndAfbLog_Cost` | TField |  | This field may be used instead of the PRICE field to record the gross cost in the portfolios specified REFERENCE.CURRENCY of the security to be transferred into or out of the portfolio. If the PRICE field has been input then the COST field will already have been calculated and populated with the result. However, you may change the COST field contents but be aware that the PRICE field contents will be recalculated according to whatever value you may enter. Similarly, if the COST field is input and the PRICE field has been left blank then the system will calculate the PRICE given the COST. Should the REFERENCE.CURRENCY differ from the currency of the security then the appropriate foreign exchange rate is used to provide either the PRICE or the COST as required is created when this record is authorised in accepted status. |
| 26 | `AFB.LOG.GROSS.AMT.SEC.CCY` | `AllfndAfbLog_GrossAmtSecCcy` | TField |  | Calculates the Gross value of the Securities being transferred, ie. the Nominal.Amount (Field 11) valued at the Price (Field 12), displayed in the Security.Currency |
| 27 | `AFB.LOG.CHARGES` | `AllfndAfbLog_Charges` | TField |  | Records the charges levied against the Customer for the transaction. This is defaulted based on customer charge conditions set for SC.TRADING but could be manually amended |
| 28 | `AFB.LOG.LOCAL.TAX` | `AllfndAfbLog_LocalTax` | TField |  | Input field allowing the user to record the amount of any local tax to be charged on the Security Transfer Transaction. If nothing is input will default to the local tax calculated from the local tax rate on the SC.STD.POS.TRANSF. |
| 29 | `AFB.LOG.CU.CHARGE.TAX.TYPE` | `AllfndAfbLog_CuChargeTaxType` | TField |  | Charge or Tax type as defined in SCDX.CHARGE.PARAMETER (value will be from CHARGE.TAX.TYPE field). These will be the charges/taxes defined for the customer side. |
| 30 | `AFB.LOG.NET.AMT.SEC.CCY` | `AllfndAfbLog_NetAmtSecCcy` | TField |  | Calculates the current valuation of the Securities being transferred, ie.Gross.Amount +/- Charges + Accrued.Interest. |
| 31 | `AFB.LOG.SEC.EXCH.RATE` | `AllfndAfbLog_SecExchRate` | TField |  | Indicates the exchange rate for the conversion to Local Currency (for valuation purposes) of the Net.Amt.Sec.Ccy. |
| 32 | `AFB.LOG.CU.ACCOUNT.NO` | `AllfndAfbLog_CuAccountNo` | TField |  | Specifies the (internal cash) Account for the Customer, over which cash entries relating to the transaction are to be passed |
| 33 | `AFB.LOG.CU.ACCOUNT.CCY` | `AllfndAfbLog_CuAccountCcy` | TField |  | Indicates the Currency of the Customer Account. |
| 34 | `AFB.LOG.REFERENCE.CCY` | `AllfndAfbLog_ReferenceCcy` | TField |  | Records the Customers Reference.Ccy as specified in Field 2 of the Sec.Acc.Master record |
| 35 | `AFB.LOG.REF.EXCH.RATE` | `AllfndAfbLog_RefExchRate` | TField |  | Indicates the exchange rate between the Customers Reference.Ccy and the Local Currency |
| 36 | `AFB.LOG.BROKER.NO` | `AllfndAfbLog_BrokerNo` | TField |  | Identifies the party to/from whom the transfer is to be made. You may input any of the following CUSTOMER.SECURITY types : 1) Broker 2) Counterparty 3) Client Whereas the Broker and Counterparty are self explanatory the Client may be a Customer of the Bank who is not traditionally known as either a Broker or Counterparty but as a Client (Without a Portfolio) who transacts business with the Bank. It is therefore permissible within the Sec.Trade appliaction to enter a transaction on the Broker side of the transaction who will Purchase securities from a Client who is selling those securities. The system is intelligent enough to know that the Client is effectively a Customer without a Portfolio and will ensure that the accounting procedures for this transaction are dealt with properly. |
| 37 | `AFB.LOG.BR.NET.AMT` | `AllfndAfbLog_BrNetAmt` | TField |  | Specifies the Net.Amount due to/from the Broker (Field 23) for the transaction. Input is only required where the Security. Transfer is made against payment. |
| 38 | `AFB.LOG.CU.ACC.EX.RATE` | `AllfndAfbLog_CuAccExRate` | TField |  | Exchange rate to customer account currency |
| 39 | `AFB.LOG.CUST.NET.AMT` | `AllfndAfbLog_CustNetAmt` | TField |  | Specifies the Net.Amount due to/from the Customer for the transaction. Input is only required where the Security. Transfeust is made against payment. |
| 40 | `AFB.LOG.DELIVERY.INSTR` | `AllfndAfbLog_DeliveryInstr` | TField |  | Specifies the type of Delivery to be made for this transaction. This forms an important part of the transaction as it is linked to the delivery and clearing interfaces. For a fuller description of how the transaction processing within T24 works see the Securities Manual on Transaction Processing and Delivery Interfaces. |
| 41 | `AFB.LOG.MARKET.TYPE` | `AllfndAfbLog_MarketType` | TField |  | Defaults to N (Normal Market). Not currently used. However it was envisaged that this field would determine the difference between Spot and Forward Transactions in the Securities Market. |
| 42 | `AFB.LOG.COMMISSION.CODE` | `AllfndAfbLog_CommissionCode` | TField |  | This field accepts a valid FT.COMMISSION.TYPE ID ,Based on which the CHARGES will be calculated. |
| 43 | `AFB.LOG.COMM.PERCENT` | `AllfndAfbLog_CommPercent` | TField |  | Commission percentage applied |
| 44 | `AFB.LOG.VAULT.UPDATE` | `AllfndAfbLog_VaultUpdate` | TField |  | VAULT CONTROL PARAMETER FLAG NB. VAULT.PARAMETER details supercedes this flag Validation Rules: NO - Vault control facilities not in use for the security transfer application YES - Vault control facilities switched on |
| 45 | `AFB.LOG.CG.TRADE.TIME` | `AllfndAfbLog_CgTradeTime` | TField |  | This field enables you to specify an alternative time for any SECURITY.TRANSFER undergoing Capital Gains tax processing should this particular process have been requested within the SC.PARAMETER file field, CG.BASE.UPDATE. Input without a time specified is acceptable to the System but you should be aware that this will cause the time of actual input to determine the location of the transaction in the Captal Gains tax transaction file, CG.TXN.BASE |
| 46 | `AFB.LOG.CGT.BAMT.CCY` | `AllfndAfbLog_CgtBamtCcy` | TField |  | This field will signify the currency code in which the CGT base amount is denominatedThis field will signify the currency code in which the CGT base amount is denominated |
| 47 | `AFB.LOG.CGT.PARAM.COND` | `AllfndAfbLog_CgtParamCond` | TField |  | A multi-value NOINPUT field. The condition id allocated to this transaction relating to application CG.PARAM.CONDITION. This will determine the Capital Gains method and tax to be applied. |
| 48 | `AFB.LOG.CGT.SRC.LCL.TAX` | `AllfndAfbLog_CgtSrcLclTax` | TField |  | A NOINPUT multi-value associated field. This indicates whether the tax is to be deducted by the bank (LOCAL) or the depositor (SOURCE |
| 49 | `AFB.LOG.PAYMENT.REQD` | `AllfndAfbLog_PaymentReqd` | TField |  | This field specifies whether a customer payment is to be made. The default is set in the ADVICE.DEFAULT field in the SC.PARAMETER file |
| 50 | `AFB.LOG.BROKER.ADVICE.REQD` | `AllfndAfbLog_BrokerAdviceReqd` | TField |  | This field specifies whether a broker advice is to be sent. The default is set in the ADVICE.DEFAULT field in the SC.PARAMETER file. |
| 51 | `AFB.LOG.DEPOT.ADVICE.REQD` | `AllfndAfbLog_DepotAdviceReqd` | TField |  | This field specifies whether a depository advice is to be produced. The default is set in the ADVICE.DEFAULT field in the SC.PARAMETER file |
| 52 | `AFB.LOG.ACT.CHARGES` | `AllfndAfbLog_ActCharges` | TField |  | This field will hold the actual charges calculated by the system |
| 53 | `AFB.LOG.STATEMENT.NOS` | `AllfndAfbLog_StatementNos` | TField |  | A number Generated automatically by the system after authorisation which identifies either a statement entry or a category entry in respect of a transaction. After validation but before authorisation, the value VAL will be inserted in this field to indicate that the transaction has been validated successfully but is still waiting authorisation. After authorisation of a Funds Transfer transaction, the system will automatically insert a number into this field and this number may refer to a statement entry or a category entry depending on the value contained in the corresponding multivalue fields. The following examples will illustrate the use of this field. Example 1: On the execution date of a transaction there will normally be an entry on a Customer account and the following type of number will be generated at this field: 92.1 STMT.NO 673732684.48 92.2 STMT.NO 1 The number automatically generated in field 92.1 is unique to the transaction in question and is built in the following way: 1. The first four digits 6737 indicate the number of days since the 1st of January 1968. In our example, it corresponds to the 11th of June 1986. 2. The next five digits 32684 indicate the number of seconds since midnight. In our example, it corresponds to an entry generated on line at 09:04:44 AM. 3. The last two digits 48 indicate the number of hundreds of seconds. The value assigned (again automatically) to field 92.2 identifies the number in 92.1 as a statement entry number. If the User wishes to call this statement entry record on to the screen the User will invoke the STMT.ENTRY Application and the type the following at Awaiting ID :-673732684.480001 where the suffix 0001 identifies it as the first statement entry (there will normally be more than one as the next example will illustrate). |
| 54 | `AFB.LOG.SEC.ACCT.FROM` | `AllfndAfbLog_SecAcctFrom` | TField |  | Specifies the Security.Account from which the Transfer is to be made. Within the position transfer the system will allow the user to input a number of transfers |
| 55 | `AFB.LOG.SEC.ACCT.TO` | `AllfndAfbLog_SecAcctTo` | TField |  | Specifies the Security.Account to which the Transfer is to be made. Within the position transfer the system will allow the user to input a number of transfers |
| 56 | `AFB.LOG.SECURITY.ACCT` | `AllfndAfbLog_SecurityAcct` | TField |  | The multivalue fields 13 - 19 contain details of the individual transactions which have been created by the System when processing the transaction. For audit and control purposes the details relating to any particular Position Transfer are recorded at the transaction level itselfent. |
| 57 | `AFB.LOG.PT.SECURITY.NO` | `AllfndAfbLog_PtSecurityNo` | TField |  | The multivalue fields 13 - 19 contain details of the individual transactions which have been created by the System when processing the transaction. For audit and control purposes the details relating to any particular Position Transfer are recorded at the transaction level itself. |
| 58 | `AFB.LOG.DEPOSITORY.1` | `AllfndAfbLog_Depository1` | TField |  | Display the details of the individual transactions created by System in order to effect the Transfer as specified in Fields 1 to 6. |
| 59 | `AFB.LOG.NO.NOMINAL` | `AllfndAfbLog_NoNominal` | TField |  | The multivalue fields 13 - 19 contain details of the individual transactions which have been created by the System when processing the transaction. For audit and control purposes the details relating to any particular Position Transfer are recorded at the transaction level itself. |
| 60 | `AFB.LOG.PRICE` | `AllfndAfbLog_Price` | TField |  | The price at which the transferred position will be held by the new portfolio upon transfer. By default this will be the price at which the security is being held by the transferring party |
| 61 | `AFB.LOG.PT.SECURITY.CCY` | `AllfndAfbLog_PtSecurityCcy` | TField |  | Specifies the currency of the security. Defaults from SECURITY.CURRENCY field on the SECURITY.MASTER record |
| 62 | `AFB.LOG.PF.OUT.REF.CCY` | `AllfndAfbLog_PfOutRefCcy` | TField |  | This is the Reference Currency of the Portfolio from where positions are being transferred.BASE |
| 63 | `AFB.LOG.PF.REF.IN.CCY` | `AllfndAfbLog_PfRefInCcy` | TField |  | This is the Reference Currency of the Portfolio to which the positions are being transferred to |
| 64 | `AFB.LOG.XRATE.SEC.BASE` | `AllfndAfbLog_XrateSecBase` | TField |  | Specifies the exchange rate applicable between the Security currency and the Local Currency a number of transfers |
| 65 | `AFB.LOG.XRATE.BASE.POUT` | `AllfndAfbLog_XrateBasePout` | TField |  | Specifies the exchange rate applicable between the Local Currency and the Portfolio Reference Currency of the portfolio from where the position has been transferred out. |
| 66 | `AFB.LOG.XRATE.BASE.PFIN` | `AllfndAfbLog_XrateBasePfin` | TField |  | Specifies the exchange rate applicable between the Local Currency and the Portfolio Reference Currency of the portfolio that the position has been transferred in to. |
| 67 | `AFB.LOG.EXCHANGE.DATE` | `AllfndAfbLog_ExchangeDate` | TField |  | This field indicates the Exchange Rate to be Used during a Position Transfer. Valid Values are : EFFECTIVE - Exchange Rate on the trade date of the transaction will be used. TRADE - Exchange Rate as on the Trade Date of original transactions making up the position is used |
| 68 | `AFB.LOG.TRANS.TYPE.DR` | `AllfndAfbLog_TransTypeDr` | TField |  | The field is used to specify the security transaction code (debit) for the transactions. If not specified, the default is taken from SC.STD.POS.TRANSF |
| 69 | `AFB.LOG.TRANS.TYPE.CR` | `AllfndAfbLog_TransTypeCr` | TField |  | The field is used to specify the security transaction code (CREDIT) for the transactions. If not specified, the default is taken from SC.STD.POS.TRANSF |
| 70 | `AFB.LOG.NO.OF.POSITION` | `AllfndAfbLog_NoOfPosition` | TField |  | The field is used to specify the security transaction code (CREDIT) for the transactions. If not specified, the default is taken from SC.STD.POS.TRANSF |
| 71 | `AFB.LOG.PT.OVERRIDE.1` | `AllfndAfbLog_PtOverride1` | TField |  | Contains details of any overrides applicable to this Account |
| 72 | `AFB.LOG.PT.OVERRIDE.2` | `AllfndAfbLog_PtOverride2` | TField |  | Contains details of any overrides applicable to this Account |
| 73 | `AFB.LOG.PT.OVERRIDE.3` | `AllfndAfbLog_PtOverride3` | TField |  | Contains details of any overrides applicable to this Account |
| 74 | `AFB.LOG.PT.CO.CODE` | `AllfndAfbLog_PtCoCode` |  |  |  |
| 75 | `AFB.LOG.PT.DEPT.CODE` | `AllfndAfbLog_PtDeptCode` |  |  |  |
| 76 | `AFB.LOG.LOCAL.REF` | `AllfndAfbLog_LocalRef` |  |  |  |
| 77 | `AFB.LOG.RESERVED.1` | `AllfndAfbLog_Reserved1` | TField |  |  |
| 78 | `AFB.LOG.RESERVED.2` | `AllfndAfbLog_Reserved2` | TField |  |  |
| 79 | `AFB.LOG.RESERVED.3` | `AllfndAfbLog_Reserved3` | TField |  |  |
| 80 | `AFB.LOG.RESERVED.4` | `AllfndAfbLog_Reserved4` | TField |  |  |
| 81 | `AFB.LOG.RESERVED.5` | `AllfndAfbLog_Reserved5` | TField |  |  |
| 82 | `AFB.LOG.RESERVED.6` | `AllfndAfbLog_Reserved6` | TField |  |  |
| 83 | `AFB.LOG.RESERVED.7` | `AllfndAfbLog_Reserved7` | TField |  |  |
| 84 | `AFB.LOG.RESERVED.8` | `AllfndAfbLog_Reserved8` | TField |  |  |
| 85 | `AFB.LOG.RESERVED.9` | `AllfndAfbLog_Reserved9` | TField |  |  |
| 86 | `AFB.LOG.RESERVED.10` | `AllfndAfbLog_Reserved10` | TField |  |  |
| 87 | `AFB.LOG.OVERRIDE` | `AllfndAfbLog_Override` |  |  |  |
| 88 | `AFB.LOG.RECORD.STATUS` | `AllfndAfbLog_RecordStatus` | String |  |  |
| 89 | `AFB.LOG.CURR.NO` | `AllfndAfbLog_CurrNo` | String |  |  |
| 90 | `AFB.LOG.INPUTTER` | `AllfndAfbLog_Inputter` |  |  |  |
| 91 | `AFB.LOG.DATE.TIME` | `AllfndAfbLog_DateTime` |  |  |  |
| 92 | `AFB.LOG.AUTHORISER` | `AllfndAfbLog_Authoriser` | String |  |  |
| 93 | `AFB.LOG.CO.CODE` | `AllfndAfbLog_CoCode` | String |  |  |
| 94 | `AFB.LOG.DEPT.CODE` | `AllfndAfbLog_DeptCode` | String |  |  |
| 95 | `AFB.LOG.AUDITOR.CODE` | `AllfndAfbLog_AuditorCode` | String |  |  |
| 96 | `AFB.LOG.AUDIT.DATE.TIME` | `AllfndAfbLog_AuditDateTime` | String |  |  |
