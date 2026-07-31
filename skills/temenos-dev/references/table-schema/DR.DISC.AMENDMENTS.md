# DR.DISC.AMENDMENTS — Table Schema

> Source: `INSERTS/I_F.DR.DISC.AMENDMENTS` in `LC_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DISC.DR.DRAW.CURRENCY` | `DrDiscAmendments_DrawCurrency` | TField |  | Specifies the currency of the drawing. Validation Rules: (1) NO INPUT FIELD - The field will be populated from drawings |
| 2 | `DISC.DR.DOCUMENT.AMOUNT` | `DrDiscAmendments_DocumentAmount` | TField |  | Contains the amount to be drawn under this drawing expressed in the currency above (DRAW.CURRENCY). Validation Rules: (1) NOINPUT FIELD - This field will be populated from drawings. |
| 3 | `DISC.DR.VALUE.DATE` | `DrDiscAmendments_ValueDate` | TField |  | Contains the VALUE.DATE of the drawings. Validation Rules: (1) NOINPUT FIELD - This field will be populated from drawings. |
| 4 | `DISC.DR.MATURITY.DATE` | `DrDiscAmendments_MaturityDate` | TField |  | Contains the original maturity date before amendment of drawings. Validation Rules: (1) NOINPUT FIELD - This field will be populated from drawings |
| 5 | `DISC.DR.DISCOUNT.RATE` | `DrDiscAmendments_DiscountRate` | TField |  | Contains the discount rate of last discounted drawings. Validation Rules: (1) NOINPUT FIELD - This field will be populated from drawings. |
| 6 | `DISC.DR.DISCOUNT.AMT` | `DrDiscAmendments_DiscountAmt` | TField |  | Contains the discount amount of last discounted drawings. Validation Rules: (1)NO INPUT FIELD - This field will be populated from drawings. |
| 7 | `DISC.DR.LOAD.RATE` | `DrDiscAmendments_LoadRate` | TField |  | Contains the load rate of last discounted drawings. Validation Rules: (1)NO INPUT FIELD - This field will be populated from drawings. |
| 8 | `DISC.DR.LOAD.AMOUNT` | `DrDiscAmendments_LoadAmount` | TField |  | Contains the load rate of last discounted drawings. Validation Rules: (1)NO INPUT FIELD - This field will be populated from drawings. |
| 9 | `DISC.DR.DRAWDOWN.ACCOUNT` | `DrDiscAmendments_DrawdownAccount` | TField |  | Identifies the account where funds are to be received from under this drawings. Validation Rules: (1)NO INPUT FIELD - This field will be populated from drawings. |
| 10 | `DISC.DR.PAYMENT.ACCOUNT` | `DrDiscAmendments_PaymentAccount` | TField |  | Identifies the account where funds are to be paid to under this drawing. Validation Rules: (1) No Input Field - This field will be populated from drawings. |
| 11 | `DISC.DR.PAY.AMT.BEF.AMD` | `DrDiscAmendments_PayAmtBefAmd` | TField |  | Contains the Payment amount of last discounted drawings. Validation Rules: |
| 12 | `DISC.DR.REIM.AMT.BEF.AMD` | `DrDiscAmendments_ReimAmtBefAmd` | TField |  | Contains the Reimbursement amount of last discounted drawings. Validation Rules: (1) No Input Field - This field will be populated from drawings. |
| 13 | `DISC.DR.DISC.AMRT.TO.DTE` | `DrDiscAmendments_DiscAmrtToDte` | TField |  | Contains the Discount amount accrued to date, if the drawing has been discounted. |
| 14 | `DISC.DR.LOAD.AMRT.TO.DTE` | `DrDiscAmendments_LoadAmrtToDte` | TField |  | Contains the Load amount accrued to date, if the drawing has been discounted, and a load amount/rate specified |
| 15 | `DISC.DR.NEW.MATURITY.DATE` | `DrDiscAmendments_NewMaturityDate` | TField |  | This field will accept new maturity date for amending discounted drawings. Validation Rules: |
| 16 | `DISC.DR.NEW.DISC.RATE` | `DrDiscAmendments_NewDiscRate` | TField |  | This field will accept new discount rate for amendments This field will be enabled only when New Maturity Date is greater than existing Maturity date. If this field is entered, payment will be made for the DOCUMENT.AMOUNT minus the DISCOUNT.AMT+ NEW.DISC.AMOUNT calculated from this rate and also minus any load + NEW.LOAD.AMOUNT. The discount amount will be accrued over the life of the drawing at the rate specified in the LC.PARAMETERS file. Either a new discount rate or a new discount amount may be entered. The system will calculate the one not input. Validation Rules: (1) Standard rate format. |
| 17 | `DISC.DR.NEW.DISC.AMOUNT` | `DrDiscAmendments_NewDiscAmount` | TField |  | This field will accept new discount amount for discount amendment. If entered then NEW.DISC.RATE cannot be entered. Total discount amount cannot exceed document amount. The new discount amount is calculated as the value added by NEW.DISC.AMOUNT on the date of extension upto the new maturity date and the amount accrued till today i.e.value from DISC.AMRT.TO.DTE Validation Rules: (1) 1-4 type Amt characters plus a decimal point. Standard Amount Format . |
| 18 | `DISC.DR.NEW.LOAD.RATE` | `DrDiscAmendments_NewLoadRate` | TField | Conditional | Allowed if NEW.DISC.RATE or NEW.DISC.AMOUNT is present. When there is a load in drawings this field is mandatory. The load amount will be accrued over the life of the drawing, at the frequency specified in the LC.PARAMETERS file, separately from the discount amount. If the user wishes to enter a load amount rather than a load rate, then this can be performed by entering a value in the LOAD.AMT field below. If this is the case, then this field will be calculated and updated by the system. Validation Rules: (1) Standard rate format (Only up to 6 integer and decimal characters). (Optional input) (2) Can only be entered if NEW.DISC.RATE, or NEW.DISC.AMOUNT has been entered. (3) If entered, then NEW.LOAD.AMOUNT cannot be entered. |
| 19 | `DISC.DR.NEW.LOAD.AMOUNT` | `DrDiscAmendments_NewLoadAmount` | TField | No | Optional and only allowed if NEW.DISC.RATE or NEW.DISC.AMOUNT is present. The load amount will be accrued over the life of the drawing, at the frequency specified in the LC.PARAMETERS file, separately from the discount amount. If the user wishes to enter a load rate rather than a load amount, then this can be performed by entering a value in the NEW.LOAD.RATE field above. If this is the case, then this field will be calculated and updated by the system. Validation Rules: (1) 1-14 type AMT (Standard Amount Format) characters plus a decimal point. (2) Can only be entered if NEW.DISC.RATE, or NEW.DISC.AMOUNT has been entered. (3) If entered, then NEW.LOAD.RATE cannot be entered. |
| 20 | `DISC.DR.EFFECTIVE.DATE` | `DrDiscAmendments_EffectiveDate` | TField |  | Date from which new discount rate or new load rate will be effective. This field will be enabled only when NEW.MATURITY.DATE is greater than existing MATURITY.DATE. (1) Cannot be less than VALUE.DATE of drawings. (2) Defaulted to TODAY (3) Cannot be less than today. (4) Cannot be greater than old maturity of drawings. Validation Rules: (1) Standard date format |
| 21 | `DISC.DR.RETURN.INTEREST` | `DrDiscAmendments_ReturnInterest` | TField |  | This field will accept either 'YES' or 'NO'. If set to 'YES' and excess amount is less than zero then excess amount will be returned to customer if DISC.PARTY.CHRD is B else it will be adjusted in LIVEDB if DISC.PARTY.CHRD is O. If set to 'NO' excess amount will be retained and credited to P/L in a category specified in LC.PARAMETERS. When DR.DEBIT.TO.CUST is set as TRFLOAN, the system resets the value of this field to YES, thereby crediting the discount party charged with not only the pending amortization amount but also the already amortized amount that has been credited to P&amp;L. Validation Rules: Valid input is 'YES' / 'NO' Enabled except for extension of NEW.MATURITY.DATE Defaults to |
| 22 | `DISC.DR.WAIVE.CHARGES` | `DrDiscAmendments_WaiveCharges` | TField |  | Indicates whether charges are to be waived on this Drawing. If set to 'Y' then no charges will be taken. If this field is set to 'Y' then all charges relating to this Drawing will be waived, i.e.. no default charges will be added. Validation Rules: Valid inputs are 'Yes' or 'No'. Defaults to NO. |
| 23 | `DISC.DR.CHARGE.CODE` | `DrDiscAmendments_ChargeCode` |  |  |  |
| 24 | `DISC.DR.CHARGE.ACCOUNT` | `DrDiscAmendments_ChargeAccount` |  |  |  |
| 25 | `DISC.DR.CHARGE.PERIOD` | `DrDiscAmendments_ChargePeriod` |  |  |  |
| 26 | `DISC.DR.CHARGE.CURRENCY` | `DrDiscAmendments_ChargeCurrency` |  |  |  |
| 27 | `DISC.DR.CHARGE.XCHG` | `DrDiscAmendments_ChargeXchg` |  |  |  |
| 28 | `DISC.DR.CHARGE.AMOUNT` | `DrDiscAmendments_ChargeAmount` |  |  |  |
| 29 | `DISC.DR.PARTY.CHARGED` | `DrDiscAmendments_PartyCharged` |  |  |  |
| 30 | `DISC.DR.CHARGE.STATUS` | `DrDiscAmendments_ChargeStatus` |  |  |  |
| 31 | `DISC.DR.RELATED.DRAWING` | `DrDiscAmendments_RelatedDrawing` |  |  |  |
| 32 | `DISC.DR.CHARGE.LCCY.AMT` | `DrDiscAmendments_ChargeLccyAmt` |  |  |  |
| 33 | `DISC.DR.CHARGE.ACC.AMT` | `DrDiscAmendments_ChargeAccAmt` |  |  |  |
| 34 | `DISC.DR.TAX.CODE` | `DrDiscAmendments_TaxCode` |  |  |  |
| 35 | `DISC.DR.TAX.AMT` | `DrDiscAmendments_TaxAmt` |  |  |  |
| 36 | `DISC.DR.TAX.LCCY.AMT` | `DrDiscAmendments_TaxLccyAmt` |  |  |  |
| 37 | `DISC.DR.CHG.CODE` | `DrDiscAmendments_ChgCode` |  |  |  |
| 38 | `DISC.DR.TAX.ACC.AMT` | `DrDiscAmendments_TaxAccAmt` |  |  |  |
| 39 | `DISC.DR.EFF.DISC.AMOUNT` | `DrDiscAmendments_EffDiscAmount` | TField |  | This field will contain total recalculated discount amount for the drawings Validation Rules: (1)Standard amount format. (2) No Input Field. (3) System Generated. |
| 40 | `DISC.DR.EFF.LOAD.AMOUNT` | `DrDiscAmendments_EffLoadAmount` | TField |  | This field will contain the total recalculated load amount for the drawings after amendment. Validation Rules: System Generated. |
| 41 | `DISC.DR.EXCESS.INTEREST` | `DrDiscAmendments_ExcessInterest` | TField |  | This is system field and will contain excess amount to be collected/returned to customer with sign. If excess amount is less than zero and based on value in RETURN.INTEREST field excess amount will be credied to customer or P/L. If excess amount is greater then zero then excess amount will be debited from customer Validation Rules: System Generated. |
| 42 | `DISC.DR.DELIVERY.REF` | `DrDiscAmendments_DeliveryRef` |  |  |  |
| 43 | `DISC.DR.USANCE.ACT.SENT` | `DrDiscAmendments_UsanceActSent` |  |  |  |
| 44 | `DISC.DR.EB.ADV.NO` | `DrDiscAmendments_EbAdvNo` |  |  |  |
| 45 | `DISC.DR.MESSAGE.TYPE` | `DrDiscAmendments_MessageType` |  |  |  |
| 46 | `DISC.DR.MSG.CLASS.NO` | `DrDiscAmendments_MsgClassNo` |  |  |  |
| 47 | `DISC.DR.MSG.SEND.DATE` | `DrDiscAmendments_MsgSendDate` |  |  |  |
| 48 | `DISC.DR.OVR.CARRIER` | `DrDiscAmendments_OvrCarrier` |  |  |  |
| 49 | `DISC.DR.ADDRESSEE` | `DrDiscAmendments_Addressee` |  |  |  |
| 50 | `DISC.DR.SEND.MESSAGE` | `DrDiscAmendments_SendMessage` |  |  |  |
| 51 | `DISC.DR.LOCAL.REF` | `DrDiscAmendments_LocalRef` |  |  |  |
| 52 | `DISC.DR.DR.DEBIT.TO.CUST` | `DrDiscAmendments_DrDebitToCust` | TField | Yes | Input in this field signifies either that the customer is being debited for a sight bill, which was previously debited to an Internal account or is adjusted to a Loan account. Valid inputs are DEBITED and TRFLOAN. While the former is used to signify that Customer account is debited the latter implies that the payable component has been converted to a Loan. When DEBITED is chosen, the discount amount that is yet to be amortized is either credited to the account of the Discount party charged or booked to the P&amp;L account as determined by RETURN.INTEREST. If TRFLOAN is chosen, the amount of discount yet to be amortized along with the discount already amortized is credited to the Discount party charged by reversing out the P&amp;L entries as well. Input in this field is allowed only when the contract is matured Online or Backdated. Validation Rules: Valid inputs are DEBITED/TRFLOAN Valid only for Sight Bills. Cannot be input for Extension and Pre-closure (where the NEW.MATURITY.DATE is greater than Today). Mandatory input when a Discounted Bill is matured online or Back-dated, that was earlier set as NOTDEBITED. |
| 53 | `DISC.DR.RECEIV.SETT.ACCT` | `DrDiscAmendments_ReceivSettAcct` | TField |  | Input in this field denotes the account to be debited when maturing the sight bill. Valid only if DR.DEBIT.TO.CUST is input. Accepts any valid customer account of the same currency as the DRAWDOWN.ACCOUNT. On committing the amendment with an account in this field, the Internal account is credited and customer account is debited, with discount and charges, if any. Validation Rules: Valid only for Sight Discounted Bills. Input permitted only when DR.DEBIT.TO.CUST is input. Accepts any valid Customer account in the same currency as that of the DRAWDOWN.ACCOUNT. |
| 54 | `DISC.DR.REIM.AMT.AFT.AMD` | `DrDiscAmendments_ReimAmtAftAmd` | TField |  | This is a System maintained field and displays the value of Reimbursement amount after taking into effect any change that has been made during the current amendment like extension of maturity date or pre-closure or online maturity or backdated, which might affect the discount amount and the Reimbursement amount. Validation Rules: System Maintained. |
| 55 | `DISC.DR.PAY.AMT.AFT.AMD` | `DrDiscAmendments_PayAmtAftAmd` | TField |  | This is a System maintained field and displays the value of Payment amount after taking into effect any change that has been made during the current amendment like extension of maturity date or pre-closure or online maturity or backdated, which might affect the discount amount and the Payment amount. Validation Rules: System Maintained. |
| 56 | `DISC.DR.PARTICIPANT` | `DrDiscAmendments_Participant` |  |  |  |
| 57 | `DISC.DR.PART.SHARE` | `DrDiscAmendments_PartShare` |  |  |  |
| 58 | `DISC.DR.PART.AMT` | `DrDiscAmendments_PartAmt` |  |  |  |
| 59 | `DISC.DR.PART.DISC.AGREE` | `DrDiscAmendments_PartDiscAgree` |  |  |  |
| 60 | `DISC.DR.PART.DISC.AMT` | `DrDiscAmendments_PartDiscAmt` |  |  |  |
| 61 | `DISC.DR.PART.LOAD.AMT` | `DrDiscAmendments_PartLoadAmt` |  |  |  |
| 62 | `DISC.DR.PART.EXCESS.AMT` | `DrDiscAmendments_PartExcessAmt` |  |  |  |
| 63 | `DISC.DR.RESERVED.11` | `DrDiscAmendments_Reserved11` |  |  |  |
| 64 | `DISC.DR.RESERVED.12` | `DrDiscAmendments_Reserved12` |  |  |  |
| 65 | `DISC.DR.FREE.TEXT.MSG` | `DrDiscAmendments_FreeTextMsg` |  |  |  |
| 66 | `DISC.DR.MT202.SND.RCV.INF` | `DrDiscAmendments_Mt202SndRcvInf` |  |  |  |
| 67 | `DISC.DR.INST.PORT.NO` | `DrDiscAmendments_InstPortNo` | TField |  |  |
| 68 | `DISC.DR.RATE.BOOKED` | `DrDiscAmendments_RateBooked` | TField | No | This field displays the exchange rate quoted by the treasury department to the trade finance department (ie excluding department spread). When the document currency &lt;DRAW.CURRENCY&gt; and debit account currency &lt;DRAWDOWN.ACCOUNT.CURRENCY&gt; differ, the user will be able to insert an exchange rate to be applied &lt;DEBIT.CUST.RATE&gt;. This &lt;DEBIT.CUST.RATE&gt; can be derived from the departmental spread indicated in &lt;RATE.SPREAD&gt; and the treasury rate displayed in this &lt;RATE.BOOKED&gt; field. Default calculated from currency table, using current mid market spot rate. Validation Rules: Standard rate format (Only up to 6 integer and decimal characters). (Optional input) Input to this field is only allowed if the drawdown account is in a different currency to the draw currency. |
| 69 | `DISC.DR.RESERVED3` | `DrDiscAmendments_Reserved3` | TField |  |  |
| 70 | `DISC.DR.RESERVED2` | `DrDiscAmendments_Reserved2` | TField |  |  |
| 71 | `DISC.DR.RESERVED1` | `DrDiscAmendments_Reserved1` | TField |  |  |
| 72 | `DISC.DR.STMT.ENTRY.NO` | `DrDiscAmendments_StmtEntryNo` |  |  |  |
| 73 | `DISC.DR.OVERRIDE` | `DrDiscAmendments_Override` |  |  |  |
| 74 | `DISC.DR.RECORD.STATUS` | `DrDiscAmendments_RecordStatus` | String |  |  |
| 75 | `DISC.DR.CURR.NO` | `DrDiscAmendments_CurrNo` | String |  |  |
| 76 | `DISC.DR.INPUTTER` | `DrDiscAmendments_Inputter` |  |  |  |
| 77 | `DISC.DR.DATE.TIME` | `DrDiscAmendments_DateTime` |  |  |  |
| 78 | `DISC.DR.AUTHORISER` | `DrDiscAmendments_Authoriser` | String |  |  |
| 79 | `DISC.DR.CO.CODE` | `DrDiscAmendments_CoCode` | String |  |  |
| 80 | `DISC.DR.DEPT.CODE` | `DrDiscAmendments_DeptCode` | String |  |  |
| 81 | `DISC.DR.AUDITOR.CODE` | `DrDiscAmendments_AuditorCode` | String |  |  |
| 82 | `DISC.DR.AUDIT.DATE.TIME` | `DrDiscAmendments_AuditDateTime` | String |  |  |
