# FS.GA.CHARGE.ALLOCATION — Table Schema

> Source: `INSERTS/I_F.FS.GA.CHARGE.ALLOCATION` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CHARGE.ALLOCATION.FUND.ID` | `FsGaChargeAllocation_FundId` |  |  |  |
| 2 | `FS.GA.CHARGE.ALLOCATION.TRANSACTION.FEES.CODE` | `FsGaChargeAllocation_TransactionFeesCode` |  |  |  |
| 3 | `FS.GA.CHARGE.ALLOCATION.GTI.CODE` | `FsGaChargeAllocation_GtiCode` |  |  |  |
| 4 | `FS.GA.CHARGE.ALLOCATION.DEBIT.ACCOUNT.NUMBER` | `FsGaChargeAllocation_DebitAccountNumber` |  |  |  |
| 5 | `FS.GA.CHARGE.ALLOCATION.DEBIT.ACCOUNT.SUFFIX.NUMBER` | `FsGaChargeAllocation_DebitAccountSuffixNumber` |  |  |  |
| 6 | `FS.GA.CHARGE.ALLOCATION.CREDIT.ACCOUNT.NUMBER` | `FsGaChargeAllocation_CreditAccountNumber` |  |  |  |
| 7 | `FS.GA.CHARGE.ALLOCATION.CREDIT.ACCOUNT.SUFFIX.NUMBER` | `FsGaChargeAllocation_CreditAccountSuffixNumber` |  |  |  |
| 8 | `FS.GA.CHARGE.ALLOCATION.CURRENCY.FLAG` | `FsGaChargeAllocation_CurrencyFlag` |  |  |  |
| 9 | `FS.GA.CHARGE.ALLOCATION.DATE.VAL` | `FsGaChargeAllocation_DateVal` |  |  |  |
| 10 | `FS.GA.CHARGE.ALLOCATION.DEBIT.CREDIT.INDICATOR` | `FsGaChargeAllocation_DebitCreditIndicator` |  |  |  |
| 11 | `FS.GA.CHARGE.ALLOCATION.INTEREST.DAYS` | `FsGaChargeAllocation_InterestDays` |  |  |  |
| 12 | `FS.GA.CHARGE.ALLOCATION.NEGATIVE.DEBIT.ACCOUNT.NO` | `FsGaChargeAllocation_NegativeDebitAccountNo` |  |  |  |
| 13 | `FS.GA.CHARGE.ALLOCATION.NEG.DEBIT.ACCOUNT.SUFFIX.NO` | `FsGaChargeAllocation_NegDebitAccountSuffixNo` |  |  |  |
| 14 | `FS.GA.CHARGE.ALLOCATION.NEGATIVE.CREDIT.ACCOUNT.NO` | `FsGaChargeAllocation_NegativeCreditAccountNo` |  |  |  |
| 15 | `FS.GA.CHARGE.ALLOCATION.NEG.CREDIT.ACCOUNT.SUFFIX.NO` | `FsGaChargeAllocation_NegCreditAccountSuffixNo` |  |  |  |
| 16 | `FS.GA.CHARGE.ALLOCATION.IFRS.CATEGORY` | `FsGaChargeAllocation_IfrsCategory` |  |  |  |
| 17 | `FS.GA.CHARGE.ALLOCATION.RESERVED10` | `FsGaChargeAllocation_Reserved10` |  |  |  |
| 18 | `FS.GA.CHARGE.ALLOCATION.RESERVED9` | `FsGaChargeAllocation_Reserved9` |  |  |  |
| 19 | `FS.GA.CHARGE.ALLOCATION.RESERVED8` | `FsGaChargeAllocation_Reserved8` |  |  |  |
| 20 | `FS.GA.CHARGE.ALLOCATION.RESERVED7` | `FsGaChargeAllocation_Reserved7` |  |  |  |
| 21 | `FS.GA.CHARGE.ALLOCATION.RESERVED6` | `FsGaChargeAllocation_Reserved6` |  |  |  |
| 22 | `FS.GA.CHARGE.ALLOCATION.RESERVED5` | `FsGaChargeAllocation_Reserved5` |  |  |  |
| 23 | `FS.GA.CHARGE.ALLOCATION.RESERVED4` | `FsGaChargeAllocation_Reserved4` |  |  |  |
| 24 | `FS.GA.CHARGE.ALLOCATION.RESERVED3` | `FsGaChargeAllocation_Reserved3` |  |  |  |
| 25 | `FS.GA.CHARGE.ALLOCATION.RESERVED2` | `FsGaChargeAllocation_Reserved2` |  |  |  |
| 26 | `FS.GA.CHARGE.ALLOCATION.RESERVED1` | `FsGaChargeAllocation_Reserved1` |  |  |  |
| 27 | `FS.GA.CHARGE.ALLOCATION.RECORD.STATUS` | `FsGaChargeAllocation_RecordStatus` |  |  |  |
| 28 | `FS.GA.CHARGE.ALLOCATION.CURR.NO` | `FsGaChargeAllocation_CurrNo` |  |  |  |
| 29 | `FS.GA.CHARGE.ALLOCATION.INPUTTER` | `FsGaChargeAllocation_Inputter` |  |  |  |
| 30 | `FS.GA.CHARGE.ALLOCATION.DATE.TIME` | `FsGaChargeAllocation_DateTime` |  |  |  |
| 31 | `FS.GA.CHARGE.ALLOCATION.AUTHORISER` | `FsGaChargeAllocation_Authoriser` |  |  |  |
| 32 | `FS.GA.CHARGE.ALLOCATION.CO.CODE` | `FsGaChargeAllocation_CoCode` |  |  |  |
| 33 | `FS.GA.CHARGE.ALLOCATION.DEPT.CODE` | `FsGaChargeAllocation_DeptCode` |  |  |  |
| 34 | `FS.GA.CHARGE.ALLOCATION.AUDITOR.CODE` | `FsGaChargeAllocation_AuditorCode` |  |  |  |
| 35 | `FS.GA.CHARGE.ALLOCATION.AUDIT.DATE.TIME` | `FsGaChargeAllocation_AuditDateTime` |  |  |  |
