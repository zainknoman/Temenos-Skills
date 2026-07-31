# FS.GA.ACCOUNT.POSITIONS — Table Schema

> Source: `INSERTS/I_F.FS.GA.ACCOUNT.POSITIONS` in `FS_GlobalAccountingTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACCOUNT.POSITIONS.FUND.ID` | `FsGaAccountPositions_Fund` |  |  |  |
| 2 | `ACCOUNT.POSITIONS.ACCOUNT` | `FsGaAccountPositions_Account` | TField |  | Account Multifonds DB Column is NRUBR. |
| 3 | `ACCOUNT.POSITIONS.GL.ACCOUNT.SUFFIX` | `FsGaAccountPositions_SuffixNumber` |  |  |  |
| 4 | `ACCOUNT.POSITIONS.LOCAL.CURRENCY` | `FsGaAccountPositions_Currency` |  |  |  |
| 5 | `ACCOUNT.POSITIONS.VALUE.DATE` | `FsGaAccountPositions_ValueDate` | TField |  | Value Date Multifonds DB Column is DVAL. |
| 6 | `ACCOUNT.POSITIONS.SERVICE.CODE` | `FsGaAccountPositions_ServiceCode` | TField |  | Service Code Multifonds DB Column is CSERV. |
| 7 | `ACCOUNT.POSITIONS.CONTRACT` | `FsGaAccountPositions_Contract` | TField |  | Contract Multifonds DB Column is NCONTRAT. |
| 8 | `ACCOUNT.POSITIONS.DESCRIPTION` | `FsGaAccountPositions_Description` | TField |  | Description Multifonds DB Column is XLIBELLE. |
| 9 | `ACCOUNT.POSITIONS.MSOLDE` | `FsGaAccountPositions_Msolde` | TField |  | Msolde Multifonds DB Column is MSOLDE. |
| 10 | `ACCOUNT.POSITIONS.AMOUNT.IN.CLOSING.DAY` | `FsGaAccountPositions_AmountInClosingDay` | TField |  | Amount in closing day Multifonds DB Column is MDCLO. |
| 11 | `ACCOUNT.POSITIONS.NEXT` | `FsGaAccountPositions_Next` | TField |  | Next Multifonds DB Column is NEXT. |
| 12 | `ACCOUNT.POSITIONS.CLOSING.DATE` | `FsGaAccountPositions_ClosingDate` | TField |  | Closing date Multifonds DB Column is DDCLO. |
| 13 | `ACCOUNT.POSITIONS.LAST.INTER.BOOKING.DATE` | `FsGaAccountPositions_LastInterBookingDate` | TField |  | Last inter booking date Multifonds DB Column is DVCLO. |
| 14 | `ACCOUNT.POSITIONS.CUSA` | `FsGaAccountPositions_Cusa` | TField |  | CUSA Multifonds DB Column is CUSA. |
| 15 | `ACCOUNT.POSITIONS.AMOUNT` | `FsGaAccountPositions_Amount` | TField |  | Amount Multifonds DB Column is MSDB. |
| 16 | `ACCOUNT.POSITIONS.AT.CLOSING.DATE` | `FsGaAccountPositions_AtClosingDate` | TField |  | At closing date Multifonds DB Column is MSDBPTF. |
| 17 | `ACCOUNT.POSITIONS.MSPTF` | `FsGaAccountPositions_Msptf` | TField |  | MSPTF Multifonds DB Column is MSPTF. |
| 18 | `ACCOUNT.POSITIONS.MNT.INT.CR` | `FsGaAccountPositions_MntIntCr` | TField |  | Mnt Int CR Multifonds DB Column is MNT_INT_CR. |
| 19 | `ACCOUNT.POSITIONS.ARCHIVE` | `FsGaAccountPositions_Archive` | TField |  | Archive Multifonds DB Column is ARCHIVE. |
| 20 | `ACCOUNT.POSITIONS.MINIMUM.DEBIT` | `FsGaAccountPositions_MinimumDebit` | TField |  | Minimum debit Multifonds DB Column is MNT_MIN_DB. |
| 21 | `ACCOUNT.POSITIONS.MINIMUM.CREDIT` | `FsGaAccountPositions_MinimumCredit` | TField |  | Minimum credit Multifonds DB Column is MNT_MIN_CR. |
| 22 | `ACCOUNT.POSITIONS.IMPORT.FLAG` | `FsGaAccountPositions_ImportFlag` | TField |  | Import Flag Multifonds DB Column is FLG_IMPOT. |
| 23 | `ACCOUNT.POSITIONS.NS.PORTFOLIO` | `FsGaAccountPositions_NsPortfolio` | TField |  | Ns Portfolio Multifonds DB Column is NS_PORTFOLIO. |
| 24 | `ACCOUNT.POSITIONS.NEXT.DWH` | `FsGaAccountPositions_NextDwh` | TField |  | Next Dwh Multifonds DB Column is NEXT_DWH. |
| 25 | `ACCOUNT.POSITIONS.INCOME.TYPE` | `FsGaAccountPositions_IncomeType` | TField |  | Income type Multifonds DB Column is TREVENU. |
| 26 | `ACCOUNT.POSITIONS.NEXT.FUND.ID` | `FsGaAccountPositions_NextFund` | TField |  | Next fund Multifonds DB Column is NEXT_FND. |
| 27 | `ACCOUNT.POSITIONS.MSOLDE.TRADE` | `FsGaAccountPositions_MsoldeTrade` | TField |  | Msolde Trade Multifonds DB Column is MSOLDE_TRADE. |
| 28 | `ACCOUNT.POSITIONS.MSPTF.TRADE` | `FsGaAccountPositions_MsptfTrade` | TField |  | MSPTF Trade Multifonds DB Column is MSPTF_TRADE. |
| 29 | `ACCOUNT.POSITIONS.INTEREST.AMOUNT.POSITIVE` | `FsGaAccountPositions_InterestAmountPositive` | TField |  | Interest amount positive Multifonds DB Column is MNT_INT_POS. |
| 30 | `ACCOUNT.POSITIONS.INTEREST.AMOUNT.NEGATIVE` | `FsGaAccountPositions_InterestAmountNegative` | TField |  | Interest amount negative Multifonds DB Column is MNT_INT_NEG. |
| 31 | `ACCOUNT.POSITIONS.FUND.CALC.AMOUNT` | `FsGaAccountPositions_FundCalcAmount` | TField |  | Fund calc amount Multifonds DB Column is MINT_PTF_CALC. |
| 32 | `ACCOUNT.POSITIONS.DEAL.CALC.AMOUNT` | `FsGaAccountPositions_DealCalcAmount` | TField |  | Deal calc amount Multifonds DB Column is MINT_DEAL_CALC. |
| 33 | `ACCOUNT.POSITIONS.REVISION.CODE` | `FsGaAccountPositions_RevisionCode` | TField |  | Revision code Multifonds DB Column is REVISION_CODE. |
| 34 | `ACCOUNT.POSITIONS.CR.INTEREST.AMOUNT.ADJUSTMENT` | `FsGaAccountPositions_CrInterestAmountAdjustment` | TField |  | CR interest amount adjustment Multifonds DB Column is MNT_INT_CR_ADJ. |
| 35 | `ACCOUNT.POSITIONS.TAXES.PERCENTAGE` | `FsGaAccountPositions_TaxesPercentage` | TField |  | Taxes percentage Multifonds DB Column is PCT_IMPOT. |
| 36 | `ACCOUNT.POSITIONS.MNT.IMPOT` | `FsGaAccountPositions_MntImpot` | TField |  | Mnt Impot Multifonds DB Column is MNT_IMPOT. |
| 37 | `ACCOUNT.POSITIONS.SC.CODE.ASSET` | `FsGaAccountPositions_ScCodeAsset` | TField |  | Sc code asset Multifonds DB Column is SCALE_CODE_DB. |
| 38 | `ACCOUNT.POSITIONS.SC.CODE.LIABILITY` | `FsGaAccountPositions_ScCodeLiability` | TField |  | Sc code liability Multifonds DB Column is SCALE_CODE_CR. |
| 39 | `ACCOUNT.POSITIONS.LEND.FEE.FLAG` | `FsGaAccountPositions_LendFeeFlag` | TField |  | Lend Fee Flag Multifonds DB Column is FLG_LEND_FEE. |
| 40 | `ACCOUNT.POSITIONS.CFD.INTEREST.START.FLAG` | `FsGaAccountPositions_CfdInterestStartFlag` | TField |  | CFD Interest Start Flag Multifonds DB Column is FLG_CFD_INT_START. |
| 41 | `ACCOUNT.POSITIONS.IFRS.CLASS` | `FsGaAccountPositions_IfrsClass` | TField |  | IFRS class Multifonds DB Column is CGTI_IFRS. |
| 42 | `ACCOUNT.POSITIONS.DEAL.TYPE` | `FsGaAccountPositions_DealType` | TField |  | Deal Type Multifonds DB Column is TYP_DEAL. |
| 43 | `ACCOUNT.POSITIONS.BROKER` | `FsGaAccountPositions_Broker` | TField |  | Broker Multifonds DB Column is NCORRESP_CTR. |
| 44 | `ACCOUNT.POSITIONS.NEGATIVE.INTEREST.DEBIT.FLAG` | `FsGaAccountPositions_NegativeInterestDebitFlag` | TField |  | Negative Interest Debit Flag Multifonds DB Column is FLG_INT_NEG_DB. |
| 45 | `ACCOUNT.POSITIONS.NEGATIVE.INTEREST.CREDIT.FLAG` | `FsGaAccountPositions_NegativeInterestCreditFlag` | TField |  | Negative Interest Credit Flag Multifonds DB Column is FLG_INT_NEG_CR. |
| 46 | `ACCOUNT.POSITIONS.NEGATIVE.INTEREST.AMOUNT.DEBIT` | `FsGaAccountPositions_NegativeInterestAmountDebit` | TField |  | Negative interest amount debit Multifonds DB Column is INT_NEG_MINT_DB. |
| 47 | `ACCOUNT.POSITIONS.NEGATIVE.INTEREST.AMNT.CREDIT` | `FsGaAccountPositions_NegativeInterestAmntCredit` | TField |  | Negative interest amnt credit Multifonds DB Column is INT_NEG_MINT_CR. |
| 48 | `ACCOUNT.POSITIONS.WHT.ROUND.DOWN` | `FsGaAccountPositions_WhtRoundDownFlag` |  |  |  |
| 49 | `ACCOUNT.POSITIONS.POS.AMOUNT.DEBIT` | `FsGaAccountPositions_PosAmountDebit` | TField |  | Pos amount debit Multifonds DB Column is POS_MINT_DB. |
| 50 | `ACCOUNT.POSITIONS.POS.AMOUNT.CREDIT` | `FsGaAccountPositions_PosAmountCredit` | TField |  | Pos amount credit Multifonds DB Column is POS_MINT_CR. |
| 51 | `ACCOUNT.POSITIONS.RECORD.STATUS` | `FsGaAccountPositions_RecordStatus` | String |  |  |
| 52 | `ACCOUNT.POSITIONS.CURR.NO` | `FsGaAccountPositions_CurrNo` | String |  |  |
| 53 | `ACCOUNT.POSITIONS.INPUTTER` | `FsGaAccountPositions_Inputter` |  |  |  |
| 54 | `ACCOUNT.POSITIONS.DATE.TIME` | `FsGaAccountPositions_DateTime` |  |  |  |
| 55 | `ACCOUNT.POSITIONS.AUTHORISER` | `FsGaAccountPositions_Authoriser` | String |  |  |
| 56 | `ACCOUNT.POSITIONS.CO.CODE` | `FsGaAccountPositions_CoCode` | String |  |  |
| 57 | `ACCOUNT.POSITIONS.DEPT.CODE` | `FsGaAccountPositions_DeptCode` | String |  |  |
| 58 | `ACCOUNT.POSITIONS.AUDITOR.CODE` | `FsGaAccountPositions_AuditorCode` | String |  |  |
| 59 | `ACCOUNT.POSITIONS.AUDIT.DATE.TIME` | `FsGaAccountPositions_AuditDateTime` | String |  |  |
