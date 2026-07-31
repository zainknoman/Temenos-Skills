# SL.BUY.SELL — Table Schema

> Source: `INSERTS/I_F.SL.BUY.SELL` in `SL_BuySell.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SL.BS.VALUE.DATE` | `SlBuySell_ValueDate` | TField |  | Indicates the value date of the Buy/Sell transaction. Validation Rules: Standard Date field. Can be backdated if TXN.TYPE is PM. Cannot be greater than System date . Value date should not lesser than the Tranche start date and greater than the tranche end date for BS types. |
| 2 | `SL.BS.TXN.TYPE` | `SlBuySell_TxnType` | TField | Yes | Allowed values or BS or PM. BS may be chosen for recording Buy/Sell transaction. PM may be chosen for recording Principal Movement. Based on the value in this field certain fields would be blocked for input. For PM type transaction, field Total.SL.Amt and associated multi-value set of fields from Tr.Code to Part.Amount would alone be available for input. The amount of principal movement may be input in Total.SL.Amt field. The tranche particulars may be input in the fields Tr.Code to Part.Amount. For BS type transaction, Field Sell.Type to Amortise.Prem.Disc would only be available for input. Validation Rules: Allowed values or BS or PM Input Mandatory |
| 3 | `SL.BS.SELL.TYPE` | `SlBuySell_SellType` | TField |  | Indicates whether the Buy/Sell operation is for Contingent portion (Commitment available amount) or for Non-Contingent portion (loan). Option 'C' indicates Contingent portion and Option NC indicates non-contingent portion. If option 'C' is chosen, fields Sell.Participant, Buy.Participant, Tranche.Code, Total.Sl.Amt, Tot.Consideration and Amortise.Prem.Disc alone would be available for input. For option NC, fields Sell.Participant, Buy.Participant, associated fields Sl.Ref.No to Cons.Perc and Amortise.Prem.Disc would be available for input. Validation Rules: Allowed values are C or NC Once a value is chosen, the same cannot be modified in the same record. |
| 4 | `SL.BS.SELL.PARTICIPANT` | `SlBuySell_SellParticipant` | TField |  | Indicates the ID of the participant selling either the Contingent or Non-Contingent portion. Validation Rules: For Sell.Type 'C', must be a participant in the facility. For Sell.Type 'NC', must be a participant in the underlying loan. |
| 5 | `SL.BS.BUY.PARTICIPANT` | `SlBuySell_BuyParticipant` | TField |  | Indicates the ID of the participant buying either the Contingent or Non-contingent portion. A new participant can enter into a syndicate by buying a portion of the facility. Validation Rules: Must be a valid reference in the Customer table. |
| 6 | `SL.BS.TRANCHE.CODE` | `SlBuySell_TrancheCode` | TField | Yes | When a facility is defined with tranches the available amount under each tranche is held separately for drawdown management. Further individual participants' share is held at tranche level also. For a Contingent buy/sell transaction (buy/sell of available amount) , the tranche under which trading is done needs to be captured to update the revised share of participation at the tranche level. The tranche under a facility is uniquely identified by a code and the same may be input here. Validation Rules: Must be a valid tranche code in the facility. Allow.Cont.Sale field in the tranche must be flagged 'Y' Input allowed only for Sell.type 'C'. Mandatory input for Sell.Type 'C'. |
| 7 | `SL.BS.SL.REF.NO` | `SlBuySell_SlRefNo` |  |  |  |
| 8 | `SL.BS.SL.AMOUNT` | `SlBuySell_SlAmount` |  |  |  |
| 9 | `SL.BS.INT.SETTLE.AMT` | `SlBuySell_IntSettleAmt` |  |  |  |
| 10 | `SL.BS.CONSIDERATION` | `SlBuySell_Consideration` |  |  |  |
| 11 | `SL.BS.CONS.PERC` | `SlBuySell_ConsPerc` |  |  |  |
| 12 | `SL.BS.TOTAL.SL.AMT` | `SlBuySell_TotalSlAmt` | TField |  | Indicates the amount by which principal movement is to be effected. Also, indicates the amount being bought or sold for a contingent buy/sell transaction. Validation Rules: Input allowed for Txn.Type 'PM'. Input allowed for Txn.Type 'BS' and Sell.Type 'C' |
| 13 | `SL.BS.TOT.CONSIDERATION` | `SlBuySell_TotConsideration` | TField |  | Indicates the amount of consideration for a contingent buy/sell transaction. It is possible to record a transaction involving bulk sale of loans (NC type) denominated the same currency. This is done by multivaluing SL.Ref.No field which is associated with fields SL.Amount, Consideration and Cons.Perc. The sum of values in Consideration field in the multivale sets is populated in this field. Example : GLOBUS Bank has participation in two drawings to the extent of USD 10,000 and USD 20,000. These two drawings are sold for a consideration of USD 11,000 and USD 19,500 respectively, which may be input in the field Consideration or Cons.Perc in each multivalue set. The total consideration for the transaction is USD 30,500. This value is calculated by the system and populated in Tot.Consideration field. For a Non Contingent buy/sell transaction fund flow would happen for the value in this field, if GLOBUS Bank is involved in the transaction. Validation Rules: Input allowed only Txn.Type 'BS' and Sell.Type 'C' |
| 14 | `SL.BS.PREM.DISC` | `SlBuySell_PremDisc` | TField |  | System calculated. Indicates premium or discount on a transaction. Validation Rules: No input field |
| 15 | `SL.BS.AMORTISE.PREM.DISC` | `SlBuySell_AmortisePremDisc` | TField |  | A transaction involving buying/selling at a premium or discount could result in a profit or loss to the bank. Such profit or loss may be either immediately recognised in the Profit &amp; Loss Account or amortised over the life of the contract. If this field is flagged 'YES', the profit or loss on the transaction would be amortised over the life of the contract. If this field is flagged 'NO', the profit or loss would be recognised immediately. For example GLOBUS Bank Buys a loan of USD 10,000 for USD 11,000. As the loan is bought at a premium, there is a loss of USD 1,000due to this transaction. GLOBUS Bank may decide to amortise this loss over the life of the loan. Validation Rules: Allowed values are 'YES' or 'NO' Default value is NULL Input allowed only if GLOBUS Bank is either the Seller or Buyer |
| 16 | `SL.BS.LIMIT.REF` | `SlBuySell_LimitRef` | TField |  | System maintained field. Indicates the limit line to be impacted upon when GLOBUS bank is involved in the transaction. Validation Rules: No input allowed. |
| 17 | `SL.BS.TR.CODE` | `SlBuySell_TrCode` |  |  |  |
| 18 | `SL.BS.TR.AMOUNT` | `SlBuySell_TrAmount` |  |  |  |
| 19 | `SL.BS.PM.PRORATA` | `SlBuySell_PmProrata` |  |  |  |
| 20 | `SL.BS.PARTICIPANT` | `SlBuySell_Participant` |  |  |  |
| 21 | `SL.BS.PART.AMOUNT` | `SlBuySell_PartAmount` |  |  |  |
| 22 | `SL.BS.DELIVERY.CUST` | `SlBuySell_DeliveryCust` |  |  |  |
| 23 | `SL.BS.ACTIVITY.CODE` | `SlBuySell_ActivityCode` |  |  |  |
| 24 | `SL.BS.ACTIVITY.DATE` | `SlBuySell_ActivityDate` |  |  |  |
| 25 | `SL.BS.PRIOR.DAYS` | `SlBuySell_PriorDays` |  |  |  |
| 26 | `SL.BS.MSG.TYPE` | `SlBuySell_MsgType` |  |  |  |
| 27 | `SL.BS.MSG.CLASS` | `SlBuySell_MsgClass` |  |  |  |
| 28 | `SL.BS.OVR.CARRIER` | `SlBuySell_OvrCarrier` |  |  |  |
| 29 | `SL.BS.SEND.MSG` | `SlBuySell_SendMsg` |  |  |  |
| 30 | `SL.BS.MSG.DATE` | `SlBuySell_MsgDate` |  |  |  |
| 31 | `SL.BS.DELIVERY.REF` | `SlBuySell_DeliveryRef` |  |  |  |
| 32 | `SL.BS.NEW.DD.END.DATE` | `SlBuySell_NewDdEndDate` | TField |  | This field holds the new drawdown end date which is used to update DRAW.MAT.DATE, CMT.FEE.DUE.DT, TRANCHE.END.DT in Facility. Input to this field is allowed only after expiry of DRAW.MAT.DATE and for NON-REVOLVING type Facility with TXN.TYPE is PM (Prin movement) Validation rules: Standard date type field Allowed date would be greater than TODAY and less than Facility Maturity date |
| 33 | `SL.BS.AMORTISE.FREQ` | `SlBuySell_AmortiseFreq` | TField |  | Frequency at which the amortisation of the premium/discount amount should be carried out in a loan trading operation Validation rules: Standard frequency field Allowed only in number of months or days |
| 34 | `SL.BS.PART.INT.AMOUNT` | `SlBuySell_PartIntAmount` | TField |  | Holds the interest settlement amount during NC type of contract. Validation Rules: Standard T24 amount type field Input is allowed only for NC type of contracts |
| 35 | `SL.BS.PRODUCT.TYPE` | `SlBuySell_ProductType` |  |  |  |
| 36 | `SL.BS.PRODUCT.AMT` | `SlBuySell_ProductAmt` |  |  |  |
| 37 | `SL.BS.PROD.TR.CODE` | `SlBuySell_ProdTrCode` |  |  |  |
| 38 | `SL.BS.PROD.TR.AMT` | `SlBuySell_ProdTrAmt` |  |  |  |
| 39 | `SL.BS.NEW.PART.ACCOUNT` | `SlBuySell_NewPartAccount` | TField |  | Holds the BUY participant bank account which newly enters the syndication. The default value is in �SPVCN� order for the BUY participant.Value of the existing Buy participant will default its account from FACILITY. Validation Rules: Field accepts input only if the new participant bank is entering into syndication along with the type of transaction set to �BS�. Input not allowed if the participant is a T24 bank |
| 40 | `SL.BS.RESERVED.FIELDS.5` | `SlBuySell_ReservedFields5` | TField |  |  |
| 41 | `SL.BS.RESERVED.FIELDS.4` | `SlBuySell_ReservedFields4` | TField |  |  |
| 42 | `SL.BS.RESERVED.FIELDS.3` | `SlBuySell_ReservedFields3` | TField |  |  |
| 43 | `SL.BS.RESERVED.FIELDS.2` | `SlBuySell_ReservedFields2` | TField |  |  |
| 44 | `SL.BS.RESERVED.FIELDS.1` | `SlBuySell_ReservedFields1` | TField |  |  |
| 45 | `SL.BS.LOCAL.REF` | `SlBuySell_LocalRef` |  |  |  |
| 46 | `SL.BS.STMT.NO` | `SlBuySell_StmtNo` |  |  |  |
| 47 | `SL.BS.OVERRIDE` | `SlBuySell_Override` |  |  |  |
| 48 | `SL.BS.RECORD.STATUS` | `SlBuySell_RecordStatus` | String |  |  |
| 49 | `SL.BS.CURR.NO` | `SlBuySell_CurrNo` | String |  |  |
| 50 | `SL.BS.INPUTTER` | `SlBuySell_Inputter` |  |  |  |
| 51 | `SL.BS.DATE.TIME` | `SlBuySell_DateTime` |  |  |  |
| 52 | `SL.BS.AUTHORISER` | `SlBuySell_Authoriser` | String |  |  |
| 53 | `SL.BS.CO.CODE` | `SlBuySell_CoCode` | String |  |  |
| 54 | `SL.BS.DEPT.CODE` | `SlBuySell_DeptCode` | String |  |  |
| 55 | `SL.BS.AUDITOR.CODE` | `SlBuySell_AuditorCode` | String |  |  |
| 56 | `SL.BS.AUDIT.DATE.TIME` | `SlBuySell_AuditDateTime` | String |  |  |
