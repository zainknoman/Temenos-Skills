# FS.GA.REBATE.FEE.PAYMENT — Table Schema

> Source: `INSERTS/I_F.FS.GA.REBATE.FEE.PAYMENT` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.REBATE.FEE.PAYMENT.PARENT.REF.ID` | `FsGaRebateFeePayment_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.REBATE.FEE.PAYMENT.ORA.ROWID` | `FsGaRebateFeePayment_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.REBATE.FEE.PAYMENT.FUND.ID` | `FsGaRebateFeePayment_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.REBATE.FEE.PAYMENT.INTERNAL.SECURITY.ID` | `FsGaRebateFeePayment_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 5 | `FS.GA.REBATE.FEE.PAYMENT.AMOUNT.IN.FUND.CURRENCY` | `FsGaRebateFeePayment_AmountInFundCurrency` | TField |  | Amount In Fund Currency Multifonds DB Column is MONTANT_PTF. |
| 6 | `FS.GA.REBATE.FEE.PAYMENT.TRANSACTION.NUMBER` | `FsGaRebateFeePayment_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 7 | `FS.GA.REBATE.FEE.PAYMENT.SERVICE.CODE` | `FsGaRebateFeePayment_ServiceCode` | TField |  | This is an internal code in Global accounting to identify transactions of a particular instruments, This helps user to define certain rule for a specific type of instruments in various places. Multifonds DB Column is CSERVICE. |
| 8 | `FS.GA.REBATE.FEE.PAYMENT.STATUS.CODE` | `FsGaRebateFeePayment_StatusCode` | TField |  | Status Code Multifonds DB Column is STATUS. |
| 9 | `FS.GA.REBATE.FEE.PAYMENT.TRADE.DATE` | `FsGaRebateFeePayment_TradeDate` | TField |  | Trade date of the trnsaction Multifonds DB Column is DOPER. |
| 10 | `FS.GA.REBATE.FEE.PAYMENT.RESERVED10` | `FsGaRebateFeePayment_Reserved10` | TField |  |  |
| 11 | `FS.GA.REBATE.FEE.PAYMENT.RESERVED9` | `FsGaRebateFeePayment_Reserved9` | TField |  |  |
| 12 | `FS.GA.REBATE.FEE.PAYMENT.RESERVED8` | `FsGaRebateFeePayment_Reserved8` | TField |  |  |
| 13 | `FS.GA.REBATE.FEE.PAYMENT.RESERVED7` | `FsGaRebateFeePayment_Reserved7` | TField |  |  |
| 14 | `FS.GA.REBATE.FEE.PAYMENT.RESERVED6` | `FsGaRebateFeePayment_Reserved6` | TField |  |  |
| 15 | `FS.GA.REBATE.FEE.PAYMENT.RESERVED5` | `FsGaRebateFeePayment_Reserved5` | TField |  |  |
| 16 | `FS.GA.REBATE.FEE.PAYMENT.RESERVED4` | `FsGaRebateFeePayment_Reserved4` | TField |  |  |
| 17 | `FS.GA.REBATE.FEE.PAYMENT.RESERVED3` | `FsGaRebateFeePayment_Reserved3` | TField |  |  |
| 18 | `FS.GA.REBATE.FEE.PAYMENT.RESERVED2` | `FsGaRebateFeePayment_Reserved2` | TField |  |  |
| 19 | `FS.GA.REBATE.FEE.PAYMENT.RESERVED1` | `FsGaRebateFeePayment_Reserved1` | TField |  |  |
| 20 | `FS.GA.REBATE.FEE.PAYMENT.LOCAL.REF` | `FsGaRebateFeePayment_LocalRef` |  |  |  |
| 21 | `FS.GA.REBATE.FEE.PAYMENT.OVERRIDE` | `FsGaRebateFeePayment_Override` |  |  |  |
| 22 | `FS.GA.REBATE.FEE.PAYMENT.RECORD.STATUS` | `FsGaRebateFeePayment_RecordStatus` | String |  |  |
| 23 | `FS.GA.REBATE.FEE.PAYMENT.CURR.NO` | `FsGaRebateFeePayment_CurrNo` | String |  |  |
| 24 | `FS.GA.REBATE.FEE.PAYMENT.INPUTTER` | `FsGaRebateFeePayment_Inputter` |  |  |  |
| 25 | `FS.GA.REBATE.FEE.PAYMENT.DATE.TIME` | `FsGaRebateFeePayment_DateTime` |  |  |  |
| 26 | `FS.GA.REBATE.FEE.PAYMENT.AUTHORISER` | `FsGaRebateFeePayment_Authoriser` | String |  |  |
| 27 | `FS.GA.REBATE.FEE.PAYMENT.CO.CODE` | `FsGaRebateFeePayment_CoCode` | String |  |  |
| 28 | `FS.GA.REBATE.FEE.PAYMENT.DEPT.CODE` | `FsGaRebateFeePayment_DeptCode` | String |  |  |
| 29 | `FS.GA.REBATE.FEE.PAYMENT.AUDITOR.CODE` | `FsGaRebateFeePayment_AuditorCode` | String |  |  |
| 30 | `FS.GA.REBATE.FEE.PAYMENT.AUDIT.DATE.TIME` | `FsGaRebateFeePayment_AuditDateTime` | String |  |  |
