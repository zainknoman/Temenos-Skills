# NETTING.ENTRY — Table Schema

> Source: `INSERTS/I_F.NETTING.ENTRY` in `AC_PaymentNetting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.NTE.VALUE.DATE` | `NettingEntry_ValueDate` |  |  |  |
| 2 | `AC.NTE.CURRENCY` | `NettingEntry_Currency` |  |  |  |
| 3 | `AC.NTE.NETTING.ACCOUNT` | `NettingEntry_NettingAccount` |  |  |  |
| 4 | `AC.NTE.AMOUNT` | `NettingEntry_Amount` |  |  |  |
| 5 | `AC.NTE.ENTRY.TYPE` | `NettingEntry_EntryType` |  |  |  |
| 6 | `AC.NTE.COUNTERPARTY` | `NettingEntry_Counterparty` |  |  |  |
| 7 | `AC.NTE.NP.REF` | `NettingEntry_NpRef` |  |  |  |
| 8 | `AC.NTE.NOSTRO.ACCOUNT` | `NettingEntry_NostroAccount` |  |  |  |
| 9 | `AC.NTE.RELATED.REF` | `NettingEntry_RelatedRef` |  |  |  |
| 10 | `AC.NTE.SEND.CORR.BK` | `NettingEntry_SendCorrBk` |  |  |  |
| 11 | `AC.NTE.REC.CORR.BK` | `NettingEntry_RecCorrBk` |  |  |  |
| 12 | `AC.NTE.INTERMED.BK` | `NettingEntry_IntermedBk` |  |  |  |
| 13 | `AC.NTE.INTERM.ACCT` | `NettingEntry_IntermAcct` |  |  |  |
| 14 | `AC.NTE.ACCT.WITH.BK` | `NettingEntry_AcctWithBk` |  |  |  |
| 15 | `AC.NTE.AWB.ACCT` | `NettingEntry_AwbAcct` |  |  |  |
| 16 | `AC.NTE.BEN.CUST` | `NettingEntry_BenCust` |  |  |  |
| 17 | `AC.NTE.BEN.ACCT.NO` | `NettingEntry_BenAcctNo` |  |  |  |
| 18 | `AC.NTE.BK.TO.BK` | `NettingEntry_BkToBk` |  |  |  |
| 19 | `AC.NTE.ORDER.CUST` | `NettingEntry_OrderCust` |  |  |  |
| 20 | `AC.NTE.ORDER.BANK` | `NettingEntry_OrderBank` |  |  |  |
| 21 | `AC.NTE.SWIFT.CHG.DETS` | `NettingEntry_SwiftChgDets` |  |  |  |
| 22 | `AC.NTE.SENDER.CHG` | `NettingEntry_SenderChg` |  |  |  |
| 23 | `AC.NTE.RECEIVER.CHG` | `NettingEntry_ReceiverChg` |  |  |  |
| 24 | `AC.NTE.EXCHANGE.RATE` | `NettingEntry_ExchangeRate` |  |  |  |
| 25 | `AC.NTE.INSTRUCTED.CCY` | `NettingEntry_InstructedCcy` |  |  |  |
| 26 | `AC.NTE.INSTRUCTED.AMT` | `NettingEntry_InstructedAmt` |  |  |  |
| 27 | `AC.NTE.OPERATION.CODE` | `NettingEntry_OperationCode` |  |  |  |
| 28 | `AC.NTE.REMITT.INFO` | `NettingEntry_RemittInfo` |  |  |  |
| 29 | `AC.NTE.ORD.CUST.CODE` | `NettingEntry_OrdCustCode` |  |  |  |
| 30 | `AC.NTE.DRAWDOWN.ACC` | `NettingEntry_DrawdownAcc` |  |  |  |
| 31 | `AC.NTE.BEN.NAME` | `NettingEntry_BenName` |  |  |  |
| 32 | `AC.NTE.BEN.ADDRESS` | `NettingEntry_BenAddress` |  |  |  |
| 33 | `AC.NTE.BEN.COUNTRY` | `NettingEntry_BenCountry` |  |  |  |
| 34 | `AC.NTE.BEN.TOWN` | `NettingEntry_BenTown` |  |  |  |
| 35 | `AC.NTE.NP.REF.STATUS` | `NettingEntry_NpRefStatus` |  |  |  |
| 36 | `AC.NTE.CLS.DEAL` | `NettingEntry_ClsDeal` | TField |  | This field specifies if the Payment is a CLS deal i.e. the Payment will be settled through Multilateral Netting or Bilateral Netting. Value YES in this field indicates that the Payment will be settled as Multilateral Netting. Value NO or blank in this field indicates that the Payment will be settled as Bilateral Netting. Validation Rules: System generated. No input. |
