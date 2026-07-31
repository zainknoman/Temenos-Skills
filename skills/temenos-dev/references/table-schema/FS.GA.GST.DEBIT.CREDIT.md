# FS.GA.GST.DEBIT.CREDIT — Table Schema

> Source: `INSERTS/I_F.FS.GA.GST.DEBIT.CREDIT` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.GST.DEBIT.CREDIT.PARENT.REF.ID` | `FsGaGstDebitCredit_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.GST.DEBIT.CREDIT.ORA.ROWID` | `FsGaGstDebitCredit_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.GST.DEBIT.CREDIT.FUND.ID` | `FsGaGstDebitCredit_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.GST.DEBIT.CREDIT.TRANSACTION.NUMBER` | `FsGaGstDebitCredit_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 5 | `FS.GA.GST.DEBIT.CREDIT.GL.ACCOUNT` | `FsGaGstDebitCredit_GlAccount` | TField |  | Cash Account Number Multifonds DB Column is NRUBR. |
| 6 | `FS.GA.GST.DEBIT.CREDIT.LOCAL.CURRENCY` | `FsGaGstDebitCredit_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 7 | `FS.GA.GST.DEBIT.CREDIT.AMOUNT.IN.LOCAL.CURRENCY` | `FsGaGstDebitCredit_AmountInLocalCurrency` | TField |  | Amount of fees in deal currency. Multifonds DB Column is MONTANT. |
| 8 | `FS.GA.GST.DEBIT.CREDIT.GST.IN.PERCENTAGE` | `FsGaGstDebitCredit_GstInPercentage` | TField |  | GST in percentage Multifonds DB Column is PCT_GST. |
| 9 | `FS.GA.GST.DEBIT.CREDIT.RITC.IN.PERCENTAGE` | `FsGaGstDebitCredit_RitcInPercentage` | TField |  | RITC in percentage Multifonds DB Column is PCT_RITC. |
| 10 | `FS.GA.GST.DEBIT.CREDIT.INTERNAL.SECURITY.ID` | `FsGaGstDebitCredit_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 11 | `FS.GA.GST.DEBIT.CREDIT.MANAGER.CODE` | `FsGaGstDebitCredit_ManagerCode` | TField |  | Manager identifier in case of funds having multiple manager who manage the assets Multifonds DB Column is NS_PORTFOLIO. |
| 12 | `FS.GA.GST.DEBIT.CREDIT.FLAG.TO.REGROSS` | `FsGaGstDebitCredit_FlagToRegross` | TField |  | Regross operation Multifonds DB Column is REGROSS. |
| 13 | `FS.GA.GST.DEBIT.CREDIT.GST.SEPERATION` | `FsGaGstDebitCredit_GstSeperation` | TField |  | GST and RITC separation Multifonds DB Column is GST_SEP. |
| 14 | `FS.GA.GST.DEBIT.CREDIT.SETTLE.DATE` | `FsGaGstDebitCredit_SettleDate` | TField |  | Settlement date of transaction Multifonds DB Column is DVALEUR. |
| 15 | `FS.GA.GST.DEBIT.CREDIT.DEBIT.CREDIT.INDICATOR` | `FsGaGstDebitCredit_DebitCreditIndicator` | TField |  | Debit credit indicator tagged to an account number Multifonds DB Column is CSENS. |
| 16 | `FS.GA.GST.DEBIT.CREDIT.GST.AMOUNT` | `FsGaGstDebitCredit_GstAmount` | TField |  | GST Amount Multifonds DB Column is GST_MONTANT. |
| 17 | `FS.GA.GST.DEBIT.CREDIT.RITC.AMOUNT` | `FsGaGstDebitCredit_RitcAmount` | TField |  | RITC Amount Multifonds DB Column is RITC_MONTANT. |
| 18 | `FS.GA.GST.DEBIT.CREDIT.GST.AMOUNT.IN.FUND.CCY` | `FsGaGstDebitCredit_GstAmountInFundCcy` | TField |  | GST Amount In Fund Ccy Multifonds DB Column is GST_MONTANT_PTF. |
| 19 | `FS.GA.GST.DEBIT.CREDIT.RITC.AMOUNT.IN.FUND.CCY` | `FsGaGstDebitCredit_RitcAmountInFundCcy` | TField |  | RITC Amount In Fund Ccy Multifonds DB Column is RITC_MONTANT_PTF. |
| 20 | `FS.GA.GST.DEBIT.CREDIT.LINE` | `FsGaGstDebitCredit_Line` | TField |  | Line Multifonds DB Column is NLIGNE. |
| 21 | `FS.GA.GST.DEBIT.CREDIT.AMOUNT.IN.FUND.CURRENCY` | `FsGaGstDebitCredit_AmountInFundCurrency` | TField |  | Amount In Fund Currency Multifonds DB Column is MONTANT_PTF. |
| 22 | `FS.GA.GST.DEBIT.CREDIT.CORRESPONDENT` | `FsGaGstDebitCredit_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 23 | `FS.GA.GST.DEBIT.CREDIT.RESERVED10` | `FsGaGstDebitCredit_Reserved10` | TField |  |  |
| 24 | `FS.GA.GST.DEBIT.CREDIT.RESERVED9` | `FsGaGstDebitCredit_Reserved9` | TField |  |  |
| 25 | `FS.GA.GST.DEBIT.CREDIT.RESERVED8` | `FsGaGstDebitCredit_Reserved8` | TField |  |  |
| 26 | `FS.GA.GST.DEBIT.CREDIT.RESERVED7` | `FsGaGstDebitCredit_Reserved7` | TField |  |  |
| 27 | `FS.GA.GST.DEBIT.CREDIT.RESERVED6` | `FsGaGstDebitCredit_Reserved6` | TField |  |  |
| 28 | `FS.GA.GST.DEBIT.CREDIT.RESERVED5` | `FsGaGstDebitCredit_Reserved5` | TField |  |  |
| 29 | `FS.GA.GST.DEBIT.CREDIT.RESERVED4` | `FsGaGstDebitCredit_Reserved4` | TField |  |  |
| 30 | `FS.GA.GST.DEBIT.CREDIT.RESERVED3` | `FsGaGstDebitCredit_Reserved3` | TField |  |  |
| 31 | `FS.GA.GST.DEBIT.CREDIT.RESERVED2` | `FsGaGstDebitCredit_Reserved2` | TField |  |  |
| 32 | `FS.GA.GST.DEBIT.CREDIT.RESERVED1` | `FsGaGstDebitCredit_Reserved1` | TField |  |  |
| 33 | `FS.GA.GST.DEBIT.CREDIT.LOCAL.REF` | `FsGaGstDebitCredit_LocalRef` |  |  |  |
| 34 | `FS.GA.GST.DEBIT.CREDIT.OVERRIDE` | `FsGaGstDebitCredit_Override` |  |  |  |
| 35 | `FS.GA.GST.DEBIT.CREDIT.RECORD.STATUS` | `FsGaGstDebitCredit_RecordStatus` | String |  |  |
| 36 | `FS.GA.GST.DEBIT.CREDIT.CURR.NO` | `FsGaGstDebitCredit_CurrNo` | String |  |  |
| 37 | `FS.GA.GST.DEBIT.CREDIT.INPUTTER` | `FsGaGstDebitCredit_Inputter` |  |  |  |
| 38 | `FS.GA.GST.DEBIT.CREDIT.DATE.TIME` | `FsGaGstDebitCredit_DateTime` |  |  |  |
| 39 | `FS.GA.GST.DEBIT.CREDIT.AUTHORISER` | `FsGaGstDebitCredit_Authoriser` | String |  |  |
| 40 | `FS.GA.GST.DEBIT.CREDIT.CO.CODE` | `FsGaGstDebitCredit_CoCode` | String |  |  |
| 41 | `FS.GA.GST.DEBIT.CREDIT.DEPT.CODE` | `FsGaGstDebitCredit_DeptCode` | String |  |  |
| 42 | `FS.GA.GST.DEBIT.CREDIT.AUDITOR.CODE` | `FsGaGstDebitCredit_AuditorCode` | String |  |  |
| 43 | `FS.GA.GST.DEBIT.CREDIT.AUDIT.DATE.TIME` | `FsGaGstDebitCredit_AuditDateTime` | String |  |  |
