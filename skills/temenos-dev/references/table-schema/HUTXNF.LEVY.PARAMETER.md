# HUTXNF.LEVY.PARAMETER — Table Schema

> Source: `INSERTS/I_F.HUTXNF.LEVY.PARAMETER` in `HUTXNF_TransactionLevy.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HU.LP.ELIGIBLE.PRODUCT` | `HutxnfLevyParameter_EligibleProduct` |  |  |  |
| 2 | `HU.LP.ELIGIBLE.TRANS.CODE` | `HutxnfLevyParameter_EligibleTransCode` |  |  |  |
| 3 | `HU.LP.PAYMENT.TRANS.CODE` | `HutxnfLevyParameter_PaymentTransCode` |  |  |  |
| 4 | `HU.LP.CUS.SEGMENT.SZEP.TRANSFER` | `HutxnfLevyParameter_CusSegmentSzepTransfer` |  |  |  |
| 5 | `HU.LP.BEN.ACC.SZEP.TRANSFER` | `HutxnfLevyParameter_BenAccSzepTransfer` |  |  |  |
| 6 | `HU.LP.BEN.ACC.CHARITY` | `HutxnfLevyParameter_BenAccCharity` |  |  |  |
| 7 | `HU.LP.CUS.SEGMENT.STATE.TREASURY` | `HutxnfLevyParameter_CusSegmentStateTreasury` |  |  |  |
| 8 | `HU.LP.BEN.ACC.STATE.TREASURY` | `HutxnfLevyParameter_BenAccStateTreasury` |  |  |  |
| 9 | `HU.LP.FCY.ACC.STATE.TREASURY` | `HutxnfLevyParameter_FcyAccStateTreasury` |  |  |  |
| 10 | `HU.LP.LEVY.EXEMPT.AMT` | `HutxnfLevyParameter_LevyExemptAmt` | TField |  | This field holds the transaction amount over and above which levy is eligible for private individual. |
| 11 | `HU.LP.LEVY.PERCENT.PVT.INDIVIDUAL` | `HutxnfLevyParameter_LevyPercentPvtIndividual` | TField |  | This field holds the levy rate for the private individual. |
| 12 | `HU.LP.MAX.LEVY.AMT.PVT.INDIVIDUAL` | `HutxnfLevyParameter_MaxLevyAmtPvtIndividual` | TField |  | This field holds the maximum Levy amount ceiling for private individual. |
| 13 | `HU.LP.GFO.CODE.SME` | `HutxnfLevyParameter_GfoCodeSme` |  |  |  |
| 14 | `HU.LP.LEVY.PERCENT.NONPVT.INDIVIDUAL` | `HutxnfLevyParameter_LevyPercentNonpvtIndividual` | TField |  | This field holds the levy rate for the non-private individual. |
| 15 | `HU.LP.MAX.LEVY.AMT.NONPVT.INDIVIDUAL` | `HutxnfLevyParameter_MaxLevyAmtNonpvtIndividual` | TField |  | This field holds the maximum Levy amount ceiling for non-private individual. |
| 16 | `HU.LP.OTHER.CATEGORY` | `HutxnfLevyParameter_OtherCategory` | TField |  | This field holds the PL category for other transactions |
| 17 | `HU.LP.CASH.WITHDRAWAL.TRANS.CODE` | `HutxnfLevyParameter_CashWithdrawalTransCode` |  |  |  |
| 18 | `HU.LP.LEVY.PERCENT.CASH.WITHDRAWAL` | `HutxnfLevyParameter_LevyPercentCashWithdrawal` | TField |  | This field holds the levy rate for the cash withdrawal transaction. |
| 19 | `HU.LP.CASH.RELATED.CATEGORY` | `HutxnfLevyParameter_CashRelatedCategory` | TField |  | This field holds the PL category for cash related transactions. |
| 20 | `HU.LP.CARD.PUR.CONT.TRANS.CODE` | `HutxnfLevyParameter_CardPurContTransCode` |  |  |  |
| 21 | `HU.LP.LEVY.AMT.CONTACTLESS` | `HutxnfLevyParameter_LevyAmtContactless` | TField |  | This field holds the annual levy amount for bank card purchase transactions per customer and per bankcard, if at least one transaction (in the given calendar year) is contactless. |
| 22 | `HU.LP.CARD.PUR.NCONT.TRANS.CODE` | `HutxnfLevyParameter_CardPurNcontTransCode` |  |  |  |
| 23 | `HU.LP.LEVY.AMT.NONCONTACTLESS` | `HutxnfLevyParameter_LevyAmtNoncontactless` | TField |  | This field holds the annual levy amount for bank card purchase transactions per customer and per bankcard, if all purchase transactions (in the given calendar year) are other than contactless. |
| 24 | `HU.LP.CARD.RELATED.CATEGORY` | `HutxnfLevyParameter_CardRelatedCategory` | TField |  | This field holds the PL category for card related transactions. |
| 25 | `HU.LP.CCY.EXCHANGE.TRANS.CODE` | `HutxnfLevyParameter_CcyExchangeTransCode` |  |  |  |
| 26 | `HU.LP.CURRENCY.MARKET` | `HutxnfLevyParameter_CurrencyMarket` | TField |  | This field holds the currency market from which the NBH rate are taken for currency exchange transactions |
| 27 | `HU.LP.FX.RELATED.CATEGORY` | `HutxnfLevyParameter_FxRelatedCategory` | TField |  | This field holds the PL category for FX related transactions. |
| 28 | `HU.LP.OWN.ACC.TRANSFER.TRANS.CODE` | `HutxnfLevyParameter_OwnAccTransferTransCode` |  |  |  |
| 29 | `HU.LP.CUR.ACC.RET.ACC.TRANS.CODE` | `HutxnfLevyParameter_CurAccRetAccTransCode` |  |  |  |
| 30 | `HU.LP.GROUP.FINANCING.TRANS.CODE` | `HutxnfLevyParameter_GroupFinancingTransCode` |  |  |  |
| 31 | `HU.LP.LOAN.RELATED.TRANS.CODE` | `HutxnfLevyParameter_LoanRelatedTransCode` |  |  |  |
| 32 | `HU.LP.LOAN.RELATED.CATEGORY` | `HutxnfLevyParameter_LoanRelatedCategory` | TField |  | This field holds the PL category for loan related transactions. |
| 33 | `HU.LP.TRANSFER.RELATED.CATEGORY` | `HutxnfLevyParameter_TransferRelatedCategory` | TField |  | This field holds the PL category for transfer related transactions. |
| 34 | `HU.LP.PAYMENT.ORDER.PRODUCT` | `HutxnfLevyParameter_PaymentOrderProduct` | TField |  | This field holds the payment order product used to raise booking entries through PO |
| 35 | `HU.LP.CREDIT.ACCOUNT.CATEGORY` | `HutxnfLevyParameter_CreditAccountCategory` | TField |  | This field holds category used to form the internal credit account for booking entries |
| 36 | `HU.LP.OLD.CARD.NO.HOOK` | `HutxnfLevyParameter_OldCardNoHook` | TField |  | This field provides a provision to attach a hook routine which return the old card number of the customer as an output. |
| 37 | `HU.LP.POST.UPDATE.HOOK` | `HutxnfLevyParameter_PostUpdateHook` | A (alphanumeric) |  | An EB.API record id with a source type of METHOD which implements an interface defined in the EB.API record HUTXNF.LEVY.PARAM.POST.UPDATE.HOOK. This field supports the TransactionFee.processEligibleTransaction() method. The TransactionFee class is in the com.temenos.t24.api.hook.countrymodelbank.hungary package which is in HUTXNF_TransactionFeeHook.jar shipped with T24. This routine is invoked during HUTXNF.UPDATE.LEVY.TRANSACTION service. Validation Rules: Up to 35 type A (alphanumeric) characters. The subroutine entered should exist in EB.API record. |
| 38 | `HU.LP.RESERVED.8` | `HutxnfLevyParameter_Reserved8` |  |  |  |
| 39 | `HU.LP.RESERVED.7` | `HutxnfLevyParameter_Reserved7` |  |  |  |
| 40 | `HU.LP.RESERVED.6` | `HutxnfLevyParameter_Reserved6` |  |  |  |
| 41 | `HU.LP.RESERVED.5` | `HutxnfLevyParameter_Reserved5` |  |  |  |
| 42 | `HU.LP.RESERVED.4` | `HutxnfLevyParameter_Reserved4` |  |  |  |
| 43 | `HU.LP.RESERVED.3` | `HutxnfLevyParameter_Reserved3` |  |  |  |
| 44 | `HU.LP.RESERVED.2` | `HutxnfLevyParameter_Reserved2` | TField |  |  |
| 45 | `HU.LP.RESERVED.1` | `HutxnfLevyParameter_Reserved1` | TField |  |  |
| 46 | `HU.LP.LOCAL.REF` | `HutxnfLevyParameter_LocalRef` |  |  |  |
| 47 | `HU.LP.OVERRIDE` | `HutxnfLevyParameter_Override` |  |  |  |
| 48 | `HU.LP.RECORD.STATUS` | `HutxnfLevyParameter_RecordStatus` | String |  |  |
| 49 | `HU.LP.CURR.NO` | `HutxnfLevyParameter_CurrNo` | String |  |  |
| 50 | `HU.LP.INPUTTER` | `HutxnfLevyParameter_Inputter` |  |  |  |
| 51 | `HU.LP.DATE.TIME` | `HutxnfLevyParameter_DateTime` |  |  |  |
| 52 | `HU.LP.AUTHORISER` | `HutxnfLevyParameter_Authoriser` | String |  |  |
| 53 | `HU.LP.CO.CODE` | `HutxnfLevyParameter_CoCode` | String |  |  |
| 54 | `HU.LP.DEPT.CODE` | `HutxnfLevyParameter_DeptCode` | String |  |  |
| 55 | `HU.LP.AUDITOR.CODE` | `HutxnfLevyParameter_AuditorCode` | String |  |  |
| 56 | `HU.LP.AUDIT.DATE.TIME` | `HutxnfLevyParameter_AuditDateTime` | String |  |  |
