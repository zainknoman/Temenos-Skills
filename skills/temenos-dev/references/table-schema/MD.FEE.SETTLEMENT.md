# MD.FEE.SETTLEMENT — Table Schema

> Source: `INSERTS/I_F.MD.FEE.SETTLEMENT` in `MD_Fees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MD.FSM.SETTLEMENT.TYPE` | `MdFeeSettlement_SettlementType` | TField | Yes | Determines the action required to be performed. Options: REFUND � To refund the charges and commission. System will default all the charges and commission eligible for refund. CLAIM SETTLEMENT or CLAIM WRITEOFF � To settle/write off the claimed commission. System will default the details commission amount claimed. Mandatory field. |
| 2 | `MD.FSM.CHARGE.CODE` | `MdFeeSettlement_ChargeCode` |  |  |  |
| 3 | `MD.FSM.CHARGE.DATE` | `MdFeeSettlement_ChargeDate` |  |  |  |
| 4 | `MD.FSM.CHARGE.SEQUENCE` | `MdFeeSettlement_ChargeSequence` |  |  |  |
| 5 | `MD.FSM.CHARGE.ACCOUNT` | `MdFeeSettlement_ChargeAccount` |  |  |  |
| 6 | `MD.FSM.CHARGE.CURRENCY` | `MdFeeSettlement_ChargeCurrency` |  |  |  |
| 7 | `MD.FSM.TOT.CHARGE.AMT` | `MdFeeSettlement_TotChargeAmt` |  |  |  |
| 8 | `MD.FSM.CHARGE.AMT` | `MdFeeSettlement_ChargeAmt` |  |  |  |
| 9 | `MD.FSM.REFUND.OPTION` | `MdFeeSettlement_RefundOption` |  |  |  |
| 10 | `MD.FSM.REFUND.AMT` | `MdFeeSettlement_RefundAmt` |  |  |  |
| 11 | `MD.FSM.REFUND.DATE` | `MdFeeSettlement_RefundDate` |  |  |  |
| 12 | `MD.FSM.REFUND.DESC` | `MdFeeSettlement_RefundDesc` |  |  |  |
| 13 | `MD.FSM.REALISED.AMT` | `MdFeeSettlement_RealisedAmt` |  |  |  |
| 14 | `MD.FSM.UNREALISED.AMT` | `MdFeeSettlement_UnrealisedAmt` |  |  |  |
| 15 | `MD.FSM.CSN.ACCOUNT` | `MdFeeSettlement_CsnAccount` | TField |  | Defaulted from MD.BALANCES when SETTLEMENT.TYPE is �Refund�. User can amend the defaulted value with a valid account but in the currency of commission. User input field for claim settlement. |
| 16 | `MD.FSM.CSN.CURRENCY` | `MdFeeSettlement_CsnCurrency` | TField |  | Defaulted from the MD.BALANCES record. Holds the currency of commission. System maintained field. |
| 17 | `MD.FSM.TOT.CSN.AMOUNT` | `MdFeeSettlement_TotCsnAmount` | TField |  | Defaulted from MD.BALANCES record. Holds the total commission amount collected. System maintained field. |
| 18 | `MD.FSM.CSN.AMOUNT` | `MdFeeSettlement_CsnAmount` | TField |  | Defaulted from MD.BALANCES record. Holds the commission amount available for refund. System maintained field. |
| 19 | `MD.FSM.CSN.REFUND.OPTION` | `MdFeeSettlement_CsnRefundOption` | TField |  | Allows the user to initiate the component of commission amount for refund. Options: REALISED UNREALISED BOTH Validations: Unrealised amount must be refunded first. 'BOTH' option allowed only when realised and unrealised components are present. |
| 20 | `MD.FSM.CSN.REFUND.AMT` | `MdFeeSettlement_CsnRefundAmt` | TField |  | Commission amount available for refund defaulted based on CSN.REFUND.OPTION. User can amend the defaulted value. |
| 21 | `MD.FSM.CSN.REFUND.DATE` | `MdFeeSettlement_CsnRefundDate` | TField |  | Holds the date of refund. Defaulted to system date. System maintained field. |
| 22 | `MD.FSM.CSN.REFUND.DESC` | `MdFeeSettlement_CsnRefundDesc` | TField | Yes | Holds the reason for refund. User input mandatory field. |
| 23 | `MD.FSM.CSN.REALISED.AMT` | `MdFeeSettlement_CsnRealisedAmt` | TField |  | Holds the commission realised amount available for refund. System defaulted field. |
| 24 | `MD.FSM.CSN.UNREALISED.AMT` | `MdFeeSettlement_CsnUnrealisedAmt` | TField |  | Holds the commission unrealised amount available for refund. System defaulted field. |
| 25 | `MD.FSM.CLAIM.STLE.AMT` | `MdFeeSettlement_ClaimStleAmt` | TField |  | Holds the claim commission amount to be settled. Can be less than, equal to or greater than the claimed amount. User input field. |
| 26 | `MD.FSM.CLAIM.DIFF.AMT` | `MdFeeSettlement_ClaimDiffAmt` | TField |  | Holds the balance amount in case the settled amount is less than the claimed amount. This amount can either be debited from the customer�s account or written off. User input field. |
| 27 | `MD.FSM.CLAIM.DIFF.ACC` | `MdFeeSettlement_ClaimDiffAcc` | TField |  | Holds the account from which the balance amount is to be debited in case the settled amount is less than the claimed amount. Must be a PL write off category (defined in MD.PARAMETER) in case of write off of the unsettled amount or a valid customer�s account in case the unsettled amount is to be collected from the customer. User input field. |
| 28 | `MD.FSM.CSN.EXCH.RATE` | `MdFeeSettlement_CsnExchRate` | TField |  | Holds the exchange rate to be applied when commission refund account is different from the deal currency. Defaulted from 'CURRENCY' table when not input by the user. |
| 29 | `MD.FSM.DELIVERY.REF` | `MdFeeSettlement_DeliveryRef` |  |  |  |
| 30 | `MD.FSM.EB.ADV.NO` | `MdFeeSettlement_EbAdvNo` |  |  |  |
| 31 | `MD.FSM.MESSAGE.TYPE` | `MdFeeSettlement_MessageType` |  |  |  |
| 32 | `MD.FSM.MSG.CLASS.NO` | `MdFeeSettlement_MsgClassNo` |  |  |  |
| 33 | `MD.FSM.OVR.CARRIER` | `MdFeeSettlement_OvrCarrier` |  |  |  |
| 34 | `MD.FSM.OVR.ADDRESS` | `MdFeeSettlement_OvrAddress` |  |  |  |
| 35 | `MD.FSM.SEND.MESSAGE` | `MdFeeSettlement_SendMessage` |  |  |  |
| 36 | `MD.FSM.LOCAL.REF` | `MdFeeSettlement_LocalRef` |  |  |  |
| 37 | `MD.FSM.RESERVED.1` | `MdFeeSettlement_Reserved1` | TField |  |  |
| 38 | `MD.FSM.RESERVED.2` | `MdFeeSettlement_Reserved2` | TField |  |  |
| 39 | `MD.FSM.RESERVED.3` | `MdFeeSettlement_Reserved3` | TField |  |  |
| 40 | `MD.FSM.RESERVED.4` | `MdFeeSettlement_Reserved4` | TField |  |  |
| 41 | `MD.FSM.RESERVED.5` | `MdFeeSettlement_Reserved5` | TField |  |  |
| 42 | `MD.FSM.RESERVED.6` | `MdFeeSettlement_Reserved6` | TField |  |  |
| 43 | `MD.FSM.RESERVED.7` | `MdFeeSettlement_Reserved7` | TField |  |  |
| 44 | `MD.FSM.RESERVED.8` | `MdFeeSettlement_Reserved8` | TField |  |  |
| 45 | `MD.FSM.RESERVED.9` | `MdFeeSettlement_Reserved9` | TField |  |  |
| 46 | `MD.FSM.RESERVED.10` | `MdFeeSettlement_Reserved10` | TField |  |  |
| 47 | `MD.FSM.STMT.NOS` | `MdFeeSettlement_StmtNos` |  |  |  |
| 48 | `MD.FSM.OVERRIDE` | `MdFeeSettlement_Override` |  |  |  |
| 49 | `MD.FSM.RECORD.STATUS` | `MdFeeSettlement_RecordStatus` | String |  |  |
| 50 | `MD.FSM.CURR.NO` | `MdFeeSettlement_CurrNo` | String |  |  |
| 51 | `MD.FSM.INPUTTER` | `MdFeeSettlement_Inputter` |  |  |  |
| 52 | `MD.FSM.DATE.TIME` | `MdFeeSettlement_DateTime` |  |  |  |
| 53 | `MD.FSM.AUTHORISER` | `MdFeeSettlement_Authoriser` | String |  |  |
| 54 | `MD.FSM.CO.CODE` | `MdFeeSettlement_CoCode` | String |  |  |
| 55 | `MD.FSM.DEPT.CODE` | `MdFeeSettlement_DeptCode` | String |  |  |
| 56 | `MD.FSM.AUDITOR.CODE` | `MdFeeSettlement_AuditorCode` | String |  |  |
| 57 | `MD.FSM.AUDIT.DATE.TIME` | `MdFeeSettlement_AuditDateTime` | String |  |  |
