# CAMB.H.INTRC.TXN.PARAM — Table Schema

> Source: `INSERTS/I_F.CAMB.H.INTRC.TXN.PARAM` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.ITP.DEBIT.TXN.TYPE` | `CambHIntrcTxnParam_DebitTxnType` | TField |  | This field is used to indicate the Debit transaction type to be used for Interac Debit transfers.This field accepts only valid FT.TXN.TYPE.CONDITION value.Eg: ACMT |
| 2 | `CAMB.ITP.DEBIT.COMM.TYPE` | `CambHIntrcTxnParam_DebitCommType` | TField |  | This field is used to define the charge setup to be used for Interac Debit Transfers.This field accepts only valid FT.COMMISSION.TYPE values.Eg: INTERAC |
| 3 | `CAMB.ITP.CREDIT.TXN.TYPE` | `CambHIntrcTxnParam_CreditTxnType` | TField |  | This field is used to indicate the Credit transaction type to be used for Interac credit transfers.This field accepts only valid FT.TXN.TYPE.CONDITION value.Eg: ACRT |
| 4 | `CAMB.ITP.CREDIT.COMM.TYPE` | `CambHIntrcTxnParam_CreditCommType` | TField |  | This field is used to define the charge setup to be used for Interac credit Transfers.This field accepts only valid FT.COMMISSION.TYPE values.Eg: INTERAC |
| 5 | `CAMB.ITP.REVERSE.TXN.TYPE` | `CambHIntrcTxnParam_ReverseTxnType` | TField |  | This field is used to indicate the transaction type to be used for Reversing the Interac transfers.This field accepts only valid FT.TXN.TYPE.CONDITION value.Eg: ACMT |
| 6 | `CAMB.ITP.REVERSE.COMM.TYPE` | `CambHIntrcTxnParam_ReverseCommType` | TField |  | This field is used to define the charge setup to be used for reversing Interac Transfers.This field accepts only valid FT.COMMISSION.TYPE values.Eg: INTERAC |
| 7 | `CAMB.ITP.SUSP.ACCT` | `CambHIntrcTxnParam_SuspAcct` | TField |  | This field is used to indicate the Internal/Suspense account to be used for posting Interac transfers.It should be a valid internal account from ACCOUNT table.Eg: CAD1015000010011 |
| 8 | `CAMB.ITP.ETF.CR.CATEG` | `CambHIntrcTxnParam_EtfCrCateg` | TField |  | Valid Category ID from CATEGORY table used to define Internal Accounts for e-Transfer Credit GLThe Value in this field would indicate that the e-Transfer Internal GL Accounts will be maintained by Branch.Mutually Exclusive with ETF CR GL AccountsEg: 10150 |
| 9 | `CAMB.ITP.ETF.DR.CATEG` | `CambHIntrcTxnParam_EtfDrCateg` | TField |  | Valid Category ID from CATEGORY table used to define Internal Accounts for e-Transfer debit GLThe Value in this field would indicate that the e-Transfer Internal GL Accounts will be maintained by Branch.Mutually Exclusive with ETF DR GL AccountsEg: 10150 |
| 10 | `CAMB.ITP.ETF.CR.GL.ACCT` | `CambHIntrcTxnParam_EtfCrGlAcct` | TField |  | Valid Internal Account from ACCOUNT table for e-Transfer Credit GL.Value in this field would indicate that the e-Transfer Internal Credit GL Account will be centralized.Mutually Exclusive with EFT CR CategoryEg: CAD1404400010011 |
| 11 | `CAMB.ITP.ETF.DR.GL.ACCT` | `CambHIntrcTxnParam_EtfDrGlAcct` | TField |  | Valid Internal Account from ACCOUNT table for e-Transfer debit GL.Value in this field would indicate that the e-Transfer Internal debit GL Account will be centralized.Mutually Exclusive with EFT DR CategoryEg: CAD1404400010011 |
| 12 | `CAMB.ITP.WIRE.NUMERIC.CCY` | `CambHIntrcTxnParam_WireNumericCcy` |  |  |  |
| 13 | `CAMB.ITP.WIRE.TRF.ACCOUN` | `CambHIntrcTxnParam_WireTrfAccoun` |  |  |  |
| 14 | `CAMB.ITP.WIRE.TRF.FTTC` | `CambHIntrcTxnParam_WireTrfFttc` |  |  |  |
| 15 | `CAMB.ITP.RDC.CRDT.TXN.TYPE` | `CambHIntrcTxnParam_RdcCrdtTxnType` | TField |  | This field used to define Valid FT.TXN.TYPE.CONDITION(Transaction Type) to be used for processing Mobile Remote Deposit Capture transactionsEg: ACMT |
| 16 | `CAMB.ITP.RDC.COMM.TYPE` | `CambHIntrcTxnParam_RdcCommType` | TField |  | This field used to define Valid FT.COMMISSION.TYPE(Transaction Charge ) to be used for processing Mobile Remote Deposit Capture transactionsEg: RDCG |
| 17 | `CAMB.ITP.RDC.REVE.TXN.TYPE` | `CambHIntrcTxnParam_RdcReveTxnType` | TField |  | This field used to define Valid FT.TXN.TYPE.CONDITION(Transaction Type) to be used for processing reversal of Mobile Remote Deposit Capture transactionsEg: ACMT |
| 18 | `CAMB.ITP.RDC.REVR.COMM` | `CambHIntrcTxnParam_RdcRevrComm` | TField |  | This field used to define Valid FT.COMMISSION.TYPE(Transaction Charge ) to be used for processing reversal of Mobile Remote Deposit Capture transactionsEg: RDCG |
| 19 | `CAMB.ITP.RDC.SUSP.CATEG` | `CambHIntrcTxnParam_RdcSuspCateg` | TField |  | This field used to define Valid Suspense Category to be defined for processing Mobile Remote Deposit Capture transactionsEg: 10001 |
| 20 | `CAMB.ITP.RDC.SUSP.ACCT` | `CambHIntrcTxnParam_RdcSuspAcct` | TField |  | This field used to define Valid Internal/Suspense Account to be defined for processing Mobile Remote Deposit Capture transactions.Eg: CAD1404400010011Either RDC.SUSP.ACCT or RDC.SUSP.CATEG should be entered. |
| 21 | `CAMB.ITP.INTRC.REV.VER` | `CambHIntrcTxnParam_IntrcRevVer` |  |  |  |
| 22 | `CAMB.ITP.RESERVED.4` | `CambHIntrcTxnParam_Reserved4` | TField |  |  |
| 23 | `CAMB.ITP.RESERVED.3` | `CambHIntrcTxnParam_Reserved3` | TField |  |  |
| 24 | `CAMB.ITP.RESERVED.2` | `CambHIntrcTxnParam_Reserved2` | TField |  |  |
| 25 | `CAMB.ITP.RESERVED.1` | `CambHIntrcTxnParam_Reserved1` | TField |  |  |
| 26 | `CAMB.ITP.RECORD.STATUS` | `CambHIntrcTxnParam_RecordStatus` | String |  |  |
| 27 | `CAMB.ITP.CURR.NO` | `CambHIntrcTxnParam_CurrNo` | String |  |  |
| 28 | `CAMB.ITP.INPUTTER` | `CambHIntrcTxnParam_Inputter` |  |  |  |
| 29 | `CAMB.ITP.DATE.TIME` | `CambHIntrcTxnParam_DateTime` |  |  |  |
| 30 | `CAMB.ITP.AUTHORISER` | `CambHIntrcTxnParam_Authoriser` | String |  |  |
| 31 | `CAMB.ITP.CO.CODE` | `CambHIntrcTxnParam_CoCode` | String |  |  |
| 32 | `CAMB.ITP.DEPT.CODE` | `CambHIntrcTxnParam_DeptCode` | String |  |  |
| 33 | `CAMB.ITP.AUDITOR.CODE` | `CambHIntrcTxnParam_AuditorCode` | String |  |  |
| 34 | `CAMB.ITP.AUDIT.DATE.TIME` | `CambHIntrcTxnParam_AuditDateTime` | String |  |  |
