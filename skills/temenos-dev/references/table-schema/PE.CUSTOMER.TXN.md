# PE.CUSTOMER.TXN — Table Schema

> Source: `INSERTS/I_F.PE.CUSTOMER.TXN` in `SC_ScPeFunds.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PE.CUS.CUSTOMER` | `PeCustomerTxn_Customer` | TField | Yes | This field holds the customer id for whom the subscription is recorded in PE.CUSTOMER.TXN record Validation Rules: Value to this field will be defaulted from the SAM id given in the id of the record Value of this field will be mapped to the CUSTOMER.NO field of SECURITY.TRANSFER or SEC.TRADE which will be created automatically This is a Mandatory and Nochange field This accepts valid CUSTOMER id |
| 2 | `SC.PE.CUS.PORTFOLIO` | `PeCustomerTxn_Portfolio` | TField | Yes | This field holds the SAM id inputted in the id Value to this field will be defaulted from SAM value from id of this record Validation Rules: Mandatory input and Nochange field This accepts valid SEC.ACC.MASTER id |
| 3 | `SC.PE.CUS.ACCOUNT` | `PeCustomerTxn_Account` | TField | Yes | This field holds the account of the Customer and this will be used for all payments made for PE fund Validation Rules: Standard T24 Account field Mandatory input and Nochange field Currency of this account should match with SECURITY.CURRENCY of the PE fund |
| 4 | `SC.PE.CUS.PE.FUND` | `PeCustomerTxn_PeFund` | TField | Yes | This field holds PE Fund(SECURITY.MASTER) value Value to this field will be defaulted from the SM given in id if the fund is PE fund. Validation Rules: accepts valid SECURITY.MASTER id Mandatory input and Nochange field |
| 5 | `SC.PE.CUS.DEPOSITORY` | `PeCustomerTxn_Depository` | TField | Yes | Identifies the Depository which will be mapped to Depository field of Security Transfer or SEC.TRADE Value of this field will be defauled from SAM for the fund Validation Rules: Mandatory field, Validation Error 'Depository Missing' will thrown against this field if the field is blank Input to this field should be a valid DEPOSITORY in CUSTOMER.SECURITY table |
| 6 | `SC.PE.CUS.COUNTERPARTY` | `PeCustomerTxn_Counterparty` | TField | Yes | Identifies the Issuer of the PE fund Validation Rules: Mandatory field Accepts valid id from CUSTOMER table |
| 7 | `SC.PE.CUS.COUNTERPARTY.ACCOUNT` | `PeCustomerTxn_CounterpartyAccount` | TField |  | This field holds the account of COUNTERPARTY which will be used for all accounting entries pertains to issuer of the fund Value of this field will be mapped to BR.ACC.NO of SECURITY.TRANSFER or SEC.TRADE records Validation Rules: Standard T24 Account field |
| 8 | `SC.PE.CUS.COMMITMENT.DATE` | `PeCustomerTxn_CommitmentDate` | TField | Yes | This field holds a date on which commitment from the customer is made Validation Rules: Standard T24 Date field Mandatory field |
| 9 | `SC.PE.CUS.COMMITMENT.AMOUNT` | `PeCustomerTxn_CommitmentAmount` | TField | Yes | This field holds the commitment amount specified in SECURITY.CURRENCY of the fund , for the customer for the specific fund Validation Rules: Standard T24 Amount field Mandatory field |
| 10 | `SC.PE.CUS.CHARGE.TYPE` | `PeCustomerTxn_ChargeType` | TField | No | This field holds the Commission code (FT.COMMISSION.TYPE) used to calculate the commission.The calculated commission is updated to the COMMISSION.AMOUTN field Value of this field will be passed as COMM.CODE to SEC.TRADE Validation Rules: Input should be a valid record in FT.COMMISSION.TYPE Optional field |
| 11 | `SC.PE.CUS.COMMISSION.PERCENTAGE` | `PeCustomerTxn_CommissionPercentage` | TField | No | This field holds the percentage of commission System calculates the COMMISSION.AMOUNT using this percentage when the commission amount is not inputted by user and this amount will be passed as CU Commission to SEC.TRADE System checks if the COMMISSION.AMOUNT is inputted, if so, the amount inputted is passed as Cu Commission If the COMMISSION.AMOUNT is blank, then system calculates Commission using this percentage if percentage is inputted If percentage is not inputted, then system calculates commission amount using charge type defined Validation Rules: Optional Field |
| 12 | `SC.PE.CUS.COMMISSION.AMOUNT` | `PeCustomerTxn_CommissionAmount` | TField | No | Identifies the Commission amount calcualted by COMMISSION.PERCENTAGE or CHARGE.TYPE This field can be directly inputted by user as a flat commission Value of this field will be passed as CU.COMMISSION during creation of SEC.TRADE Validation Rules: Optional Input. Standard T24 Amount field |
| 13 | `SC.PE.CUS.TAX.KEY` | `PeCustomerTxn_TaxKey` | TField |  | This field holds the valid id either from TAX table or TAX.TYPE.CONDITION table The value to this field will be defaulted from PE.PARAMETER when it is blank Tax amount will be calcualated using this field value and passed as COM.TAX.CODE to SEC.TRADE |
| 14 | `SC.PE.CUS.TAX.ON.COMMISSION` | `PeCustomerTxn_TaxOnCommission` | TField | No | Identifies the Tax calcualated on commission amount using TAX.KEY This value will be passed as CU.COMM.TAX to SEC.TRADE Validation Rules: Standard T24 Amount field Optional field. |
| 15 | `SC.PE.CUS.COMMIT.ADVICE` | `PeCustomerTxn_CommitAdvice` | TField |  | This field is an option field which can hold either YES or NO Value YES indicates the delivery advice for initial commitment will be generated Validation Rules: Option field Allowed values are YES , NO |
| 16 | `SC.PE.CUS.COMMIT.DELIVERY.REF` | `PeCustomerTxn_CommitDeliveryRef` | TField |  | This field holds the delivery reference which was generated during subscription when COMMIT.ADVICE is set to YES Validation Rules: Automatically updated by system when COMMIT.ADVICE is YES |
| 17 | `SC.PE.CUS.EVENT` | `PeCustomerTxn_Event` |  |  |  |
| 18 | `SC.PE.CUS.EVENT.STATUS` | `PeCustomerTxn_EventStatus` |  |  |  |
| 19 | `SC.PE.CUS.REFERENCE` | `PeCustomerTxn_Reference` |  |  |  |
| 20 | `SC.PE.CUS.EVENT.DATE` | `PeCustomerTxn_EventDate` |  |  |  |
| 21 | `SC.PE.CUS.VALUE.DATE` | `PeCustomerTxn_ValueDate` |  |  |  |
| 22 | `SC.PE.CUS.EVENT.AMOUNT` | `PeCustomerTxn_EventAmount` |  |  |  |
| 23 | `SC.PE.CUS.INTEREST.AMOUNT` | `PeCustomerTxn_InterestAmount` |  |  |  |
| 24 | `SC.PE.CUS.EVENT.ADVICE` | `PeCustomerTxn_EventAdvice` |  |  |  |
| 25 | `SC.PE.CUS.DELIVERY.REF` | `PeCustomerTxn_DeliveryRef` |  |  |  |
| 26 | `SC.PE.CUS.MATURITY.NOMINAL` | `PeCustomerTxn_MaturityNominal` | TField |  | This field holds the closing balance of Actual PE Security i.e: SM4 This field will be automatically updated by the system when Maturity event is triggered in PE.PRODUCT.EVENTS by inputting MATURITY.PRICE and MATURITY.DATE fields Validation Rules: Automatically updated by system for maturity event |
| 27 | `SC.PE.CUS.MATURITY.NAV` | `PeCustomerTxn_MaturityNav` | TField |  | This field holds the Maturity Price which was inputted in MATURITY.PRICE field of PE.PRODUCT.EVENTS application Validation Rules: Price Field Automatically updated by system |
| 28 | `SC.PE.CUS.MATURITY.AMOUNT` | `PeCustomerTxn_MaturityAmount` | TField |  | This field holds the amount for maturity event calculated as MATURITY.NOMINAL * MATURITY.PRICE during maturity Validation Rules: Standard T24 Amount field Automatically updated by system |
| 29 | `SC.PE.CUS.MATURITY.ADVICE` | `PeCustomerTxn_MaturityAdvice` | TField |  | This field is an option field which can hold either YES or NO Value YES indicates the delivery advice for Maturity will be generated Validation Rules: Option field Allowed values are YES , NO |
| 30 | `SC.PE.CUS.MATURITY.DELIVERY.REF` | `PeCustomerTxn_MaturityDeliveryRef` | TField |  | This field holds the delivery reference which was generated during maturity of a PE Fund when MATURITY.ADVICE is set to YES Validation Rules: Automatically updated by system when MATURITY.ADVICE is YES |
| 31 | `SC.PE.CUS.COMMITMENT.STATUS` | `PeCustomerTxn_CommitmentStatus` | TField |  | Identifies subscription status of a customer for a PE Fund. When the initial subscription is first recorded, typically the status is set to PROVISIONAL, at this point security movements do not take place. The status would be set to FINAL, after all the legal formalities (Such as the formal Signing of the contract) are completed. At this point, security movements take place in the background to reflect the initial commitment and the outstanding commitment Validation Rules: Values allowed are PROVISIONAL , FINAL User inputtable field Defaulted to PROVISIONAL during initial creation of PE.CUSTOMER.TXN record |
| 32 | `SC.PE.CUS.CURRENCY` | `PeCustomerTxn_Currency` | TField |  | Identifies the Currency of the PE fund Value will be defaulted from SECURITY.CURRENCY field of PE fund for which the customer is trying to subscirbe Field will be made as NOINPUT after default Validation Rules: Standard T24 Currency field System updated field |
| 33 | `SC.PE.CUS.TAP.REF.ID` | `PeCustomerTxn_TapRefId` | TField |  | Identifies the TAP reference id Validation Rules: Alpha Numeric field of length 50 characters |
| 34 | `SC.PE.CUS.TAP.EVENT.ID` | `PeCustomerTxn_TapEventId` | TField |  | Identifies the TAP Event id Validation Rules: Alpha Numeric field of length 50 characters |
| 35 | `SC.PE.CUS.SAVE.EVENT` | `PeCustomerTxn_SaveEvent` |  |  |  |
| 36 | `SC.PE.CUS.SAVE.EVENT.STATUS` | `PeCustomerTxn_SaveEventStatus` |  |  |  |
| 37 | `SC.PE.CUS.SAVE.REFERENCE` | `PeCustomerTxn_SaveReference` |  |  |  |
| 38 | `SC.PE.CUS.SAVE.EVENT.DATE` | `PeCustomerTxn_SaveEventDate` |  |  |  |
| 39 | `SC.PE.CUS.SAVE.VALUE.DATE` | `PeCustomerTxn_SaveValueDate` |  |  |  |
| 40 | `SC.PE.CUS.SAVE.EVENT.AMOUNT` | `PeCustomerTxn_SaveEventAmount` |  |  |  |
| 41 | `SC.PE.CUS.SAVE.INTEREST.AMOUNT` | `PeCustomerTxn_SaveInterestAmount` |  |  |  |
| 42 | `SC.PE.CUS.SAVE.EVENT.ADVICE` | `PeCustomerTxn_SaveEventAdvice` |  |  |  |
| 43 | `SC.PE.CUS.SAVE.DELIVERY.REF` | `PeCustomerTxn_SaveDeliveryRef` |  |  |  |
| 44 | `SC.PE.CUS.RESERVED1` | `PeCustomerTxn_Reserved1` |  |  |  |
| 45 | `SC.PE.CUS.RESERVED2` | `PeCustomerTxn_Reserved2` |  |  |  |
| 46 | `SC.PE.CUS.RESERVED3` | `PeCustomerTxn_Reserved3` |  |  |  |
| 47 | `SC.PE.CUS.RESERVED4` | `PeCustomerTxn_Reserved4` | TField |  |  |
| 48 | `SC.PE.CUS.RESERVED5` | `PeCustomerTxn_Reserved5` | TField |  |  |
| 49 | `SC.PE.CUS.RESERVED6` | `PeCustomerTxn_Reserved6` | TField |  |  |
| 50 | `SC.PE.CUS.RESERVED7` | `PeCustomerTxn_Reserved7` | TField |  |  |
| 51 | `SC.PE.CUS.RESERVED8` | `PeCustomerTxn_Reserved8` | TField |  |  |
| 52 | `SC.PE.CUS.RESERVED9` | `PeCustomerTxn_Reserved9` | TField |  |  |
| 53 | `SC.PE.CUS.RESERVED10` | `PeCustomerTxn_Reserved10` | TField |  |  |
| 54 | `SC.PE.CUS.RESERVED11` | `PeCustomerTxn_Reserved11` | TField |  |  |
| 55 | `SC.PE.CUS.RESERVED12` | `PeCustomerTxn_Reserved12` | TField |  |  |
| 56 | `SC.PE.CUS.RESERVED13` | `PeCustomerTxn_Reserved13` | TField |  |  |
| 57 | `SC.PE.CUS.RESERVED14` | `PeCustomerTxn_Reserved14` | TField |  |  |
| 58 | `SC.PE.CUS.RESERVED15` | `PeCustomerTxn_Reserved15` | TField |  |  |
| 59 | `SC.PE.CUS.RESERVED16` | `PeCustomerTxn_Reserved16` | TField |  |  |
| 60 | `SC.PE.CUS.RESERVED17` | `PeCustomerTxn_Reserved17` | TField |  |  |
| 61 | `SC.PE.CUS.RESERVED18` | `PeCustomerTxn_Reserved18` | TField |  |  |
| 62 | `SC.PE.CUS.RESERVED19` | `PeCustomerTxn_Reserved19` | TField |  |  |
| 63 | `SC.PE.CUS.RESERVED20` | `PeCustomerTxn_Reserved20` | TField |  |  |
| 64 | `SC.PE.CUS.LOCAL.REF` | `PeCustomerTxn_LocalRef` |  |  |  |
| 65 | `SC.PE.CUS.STMT.NOS` | `PeCustomerTxn_StmtNos` |  |  |  |
| 66 | `SC.PE.CUS.OVERRIDE` | `PeCustomerTxn_Override` |  |  |  |
| 67 | `SC.PE.CUS.RECORD.STATUS` | `PeCustomerTxn_RecordStatus` | String |  |  |
| 68 | `SC.PE.CUS.CURR.NO` | `PeCustomerTxn_CurrNo` | String |  |  |
| 69 | `SC.PE.CUS.INPUTTER` | `PeCustomerTxn_Inputter` |  |  |  |
| 70 | `SC.PE.CUS.DATE.TIME` | `PeCustomerTxn_DateTime` |  |  |  |
| 71 | `SC.PE.CUS.AUTHORISER` | `PeCustomerTxn_Authoriser` | String |  |  |
| 72 | `SC.PE.CUS.CO.CODE` | `PeCustomerTxn_CoCode` | String |  |  |
| 73 | `SC.PE.CUS.DEPT.CODE` | `PeCustomerTxn_DeptCode` | String |  |  |
| 74 | `SC.PE.CUS.AUDITOR.CODE` | `PeCustomerTxn_AuditorCode` | String |  |  |
| 75 | `SC.PE.CUS.AUDIT.DATE.TIME` | `PeCustomerTxn_AuditDateTime` | String |  |  |
