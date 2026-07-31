# FS.GA.CORP.ACTION.COMMISSION.TAX — Table Schema

> Source: `INSERTS/I_F.FS.GA.CORP.ACTION.COMMISSION.TAX` in `FS_IncomeCorporateAction.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.CORP.ACTION.COMMISSION.TAX.PARENT.REF.ID` | `FsGaCorpActionCommissionTax_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.CORP.ACTION.COMMISSION.TAX.ORA.ROWID` | `FsGaCorpActionCommissionTax_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.CORP.ACTION.COMMISSION.TAX.OPERATION.CODE` | `FsGaCorpActionCommissionTax_OperationCode` | TField |  | Operation code identifier Multifonds DB Column is COPER. |
| 4 | `FS.GA.CORP.ACTION.COMMISSION.TAX.INTERNAL.SECURITY.ID` | `FsGaCorpActionCommissionTax_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 5 | `FS.GA.CORP.ACTION.COMMISSION.TAX.NSEQUENCE` | `FsGaCorpActionCommissionTax_Nsequence` | TField |  | Corresponds to the sequence number Multifonds DB Column is NSEQ. |
| 6 | `FS.GA.CORP.ACTION.COMMISSION.TAX.SUBSEQUENCE.NUMBER` | `FsGaCorpActionCommissionTax_SubsequenceNumber` | TField |  | Corresponds to the sub sequence number Multifonds DB Column is NSUB_SEQ. |
| 7 | `FS.GA.CORP.ACTION.COMMISSION.TAX.FUND.ID` | `FsGaCorpActionCommissionTax_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 8 | `FS.GA.CORP.ACTION.COMMISSION.TAX.CORRESPONDENT` | `FsGaCorpActionCommissionTax_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 9 | `FS.GA.CORP.ACTION.COMMISSION.TAX.TRANSACTION.SERVICE.CODE` | `FsGaCorpActionCommissionTax_TransactionServiceCode` | TField |  | This is the transaction type. Multifonds DB Column is CSERV. |
| 10 | `FS.GA.CORP.ACTION.COMMISSION.TAX.LOT.NUMBER` | `FsGaCorpActionCommissionTax_LotNumber` | TField |  | Tax lot number to identify tax lots based on acquisition date Multifonds DB Column is NCONTRAT. |
| 11 | `FS.GA.CORP.ACTION.COMMISSION.TAX.FEE.CODE` | `FsGaCorpActionCommissionTax_FeeCode` | TField |  | Fees code for booking transaction fees Multifonds DB Column is CODE_COM. |
| 12 | `FS.GA.CORP.ACTION.COMMISSION.TAX.AMOUNT.OR.PERCENTAGE` | `FsGaCorpActionCommissionTax_AmountOrPercentage` | TField |  | Percentage of transaction fees Multifonds DB Column is TAX_COM. |
| 13 | `FS.GA.CORP.ACTION.COMMISSION.TAX.AMOUNT.IN.SECURITY.CURRENCY` | `FsGaCorpActionCommissionTax_AmountInSecurityCurrency` | TField |  | Amount in deal currency Multifonds DB Column is AMOUNT. |
| 14 | `FS.GA.CORP.ACTION.COMMISSION.TAX.ARCHIVE` | `FsGaCorpActionCommissionTax_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 15 | `FS.GA.CORP.ACTION.COMMISSION.TAX.AMOUNT.IN.SETTLEMENT.CURRENCY` | `FsGaCorpActionCommissionTax_AmountInSettlementCurrency` | TField |  | Fees amount in settlement currency Multifonds DB Column is AMOUNT_FAC. |
| 16 | `FS.GA.CORP.ACTION.COMMISSION.TAX.CURRENCY.OF.FEES` | `FsGaCorpActionCommissionTax_CurrencyOfFees` | TField |  | The currency in which the fees are denoted in a transaction. Multifonds DB Column is CMON_FAC. |
| 17 | `FS.GA.CORP.ACTION.COMMISSION.TAX.TRANSACTION.NUMBER` | `FsGaCorpActionCommissionTax_TransactionNumber` | TField |  | A sequential number attached to every transaction by fund and service code Multifonds DB Column is NECRITUR. |
| 18 | `FS.GA.CORP.ACTION.COMMISSION.TAX.BROKER` | `FsGaCorpActionCommissionTax_Broker` | TField |  | Broker Multifonds DB Column is FLG_BROKER. |
| 19 | `FS.GA.CORP.ACTION.COMMISSION.TAX.FEES.TEMP` | `FsGaCorpActionCommissionTax_FeesTemp` | TField |  | Fees Temp Multifonds DB Column is MFRAIS_TEMP. |
| 20 | `FS.GA.CORP.ACTION.COMMISSION.TAX.ANNOUNCEMENT` | `FsGaCorpActionCommissionTax_Announcement` | TField |  | Announcement Identifier Multifonds DB Column is FLG_ANNOUNCEMENT. |
| 21 | `FS.GA.CORP.ACTION.COMMISSION.TAX.RESERVED10` | `FsGaCorpActionCommissionTax_Reserved10` | TField |  |  |
| 22 | `FS.GA.CORP.ACTION.COMMISSION.TAX.RESERVED9` | `FsGaCorpActionCommissionTax_Reserved9` | TField |  |  |
| 23 | `FS.GA.CORP.ACTION.COMMISSION.TAX.RESERVED8` | `FsGaCorpActionCommissionTax_Reserved8` | TField |  |  |
| 24 | `FS.GA.CORP.ACTION.COMMISSION.TAX.RESERVED7` | `FsGaCorpActionCommissionTax_Reserved7` | TField |  |  |
| 25 | `FS.GA.CORP.ACTION.COMMISSION.TAX.RESERVED6` | `FsGaCorpActionCommissionTax_Reserved6` | TField |  |  |
| 26 | `FS.GA.CORP.ACTION.COMMISSION.TAX.RESERVED5` | `FsGaCorpActionCommissionTax_Reserved5` | TField |  |  |
| 27 | `FS.GA.CORP.ACTION.COMMISSION.TAX.RESERVED4` | `FsGaCorpActionCommissionTax_Reserved4` | TField |  |  |
| 28 | `FS.GA.CORP.ACTION.COMMISSION.TAX.RESERVED3` | `FsGaCorpActionCommissionTax_Reserved3` | TField |  |  |
| 29 | `FS.GA.CORP.ACTION.COMMISSION.TAX.RESERVED2` | `FsGaCorpActionCommissionTax_Reserved2` | TField |  |  |
| 30 | `FS.GA.CORP.ACTION.COMMISSION.TAX.RESERVED1` | `FsGaCorpActionCommissionTax_Reserved1` | TField |  |  |
| 31 | `FS.GA.CORP.ACTION.COMMISSION.TAX.LOCAL.REF` | `FsGaCorpActionCommissionTax_LocalRef` |  |  |  |
| 32 | `FS.GA.CORP.ACTION.COMMISSION.TAX.OVERRIDE` | `FsGaCorpActionCommissionTax_Override` |  |  |  |
| 33 | `FS.GA.CORP.ACTION.COMMISSION.TAX.RECORD.STATUS` | `FsGaCorpActionCommissionTax_RecordStatus` | String |  |  |
| 34 | `FS.GA.CORP.ACTION.COMMISSION.TAX.CURR.NO` | `FsGaCorpActionCommissionTax_CurrNo` | String |  |  |
| 35 | `FS.GA.CORP.ACTION.COMMISSION.TAX.INPUTTER` | `FsGaCorpActionCommissionTax_Inputter` |  |  |  |
| 36 | `FS.GA.CORP.ACTION.COMMISSION.TAX.DATE.TIME` | `FsGaCorpActionCommissionTax_DateTime` |  |  |  |
| 37 | `FS.GA.CORP.ACTION.COMMISSION.TAX.AUTHORISER` | `FsGaCorpActionCommissionTax_Authoriser` | String |  |  |
| 38 | `FS.GA.CORP.ACTION.COMMISSION.TAX.CO.CODE` | `FsGaCorpActionCommissionTax_CoCode` | String |  |  |
| 39 | `FS.GA.CORP.ACTION.COMMISSION.TAX.DEPT.CODE` | `FsGaCorpActionCommissionTax_DeptCode` | String |  |  |
| 40 | `FS.GA.CORP.ACTION.COMMISSION.TAX.AUDITOR.CODE` | `FsGaCorpActionCommissionTax_AuditorCode` | String |  |  |
| 41 | `FS.GA.CORP.ACTION.COMMISSION.TAX.AUDIT.DATE.TIME` | `FsGaCorpActionCommissionTax_AuditDateTime` | String |  |  |
