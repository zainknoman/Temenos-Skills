# LD.TXN.CODES — Table Schema

> Source: `INSERTS/I_F.LD.TXN.CODES` in `LD_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LD.TXN.OPEN.DEPOSIT` | `LdTxnCodes_OpenDeposit` | TField |  | Transaction code used for statement entry when a deposit is placed. Validation Rules: Should be a valid entry in the TRANSACTION table |
| 2 | `LD.TXN.OPEN.LOAN` | `LdTxnCodes_OpenLoan` | TField |  | Transaction code used for statement entry when a loan is given. Validation Rules: Should be a valid entry in the TRANSACTION table |
| 3 | `LD.TXN.OPEN.PLACEMENT` | `LdTxnCodes_OpenPlacement` | TField |  | Transaction code used for statement entry when a placement is made. Validation Rules: Should be a valid entry in the TRANSACTION table. . |
| 4 | `LD.TXN.OPEN.ACC.REC` | `LdTxnCodes_OpenAccRec` | TField |  | Transaction code used for statement entry when an account receivable type loan is given Validation Rules: Should be a valid entry in the TRANSACTION file |
| 5 | `LD.TXN.OPEN.SUNDRY` | `LdTxnCodes_OpenSundry` | TField |  | Transaction code used for statement entry when a sundry deposit is placed Validation Rules: Should be a valid entry in the TRANSACTION table. |
| 6 | `LD.TXN.OPEN.COMMT` | `LdTxnCodes_OpenCommt` | TField |  | Reserved for future use. |
| 7 | `LD.TXN.PRIN.INCREASE` | `LdTxnCodes_PrinIncrease` | TField |  | Transaction code for statement entry when a principal increase is done on a contract. Validation Rules: Should be a valid entry in the TRANSACTION table. |
| 8 | `LD.TXN.OPEN.LIAB.COMMT` | `LdTxnCodes_OpenLiabCommt` | TField |  | Reserved for future use. |
| 9 | `LD.TXN.PRIN.REPAYMENT` | `LdTxnCodes_PrinRepayment` | TField |  | Transaction code for statement entry when principal is repaid on a loan or deposit contract. Validation Rules: Should be a valid entry in TRANSACTION table. |
| 10 | `LD.TXN.INT.PAY` | `LdTxnCodes_IntPay` | TField |  | Transaction code for statement entry when interest is paid on a deposit contract. Validation Rules: Should be a valid entry in TRANSACTION table. |
| 11 | `LD.TXN.COM.PAY` | `LdTxnCodes_ComPay` | TField |  | Transaction code for statement entry when commission is paid on a contract. Validation Rules: Should be a valid entry in the TRANSACTION table. |
| 12 | `LD.TXN.COM.REC` | `LdTxnCodes_ComRec` | TField |  | Transaction code used for statement entry when commission is received on a contract. Validation Rules: Should be a valid entry in TRANSACTION table. |
| 13 | `LD.TXN.CAP.CHG` | `LdTxnCodes_CapChg` | TField |  | Transaction code used for the category entry when a charge is capitalised (added to the principal amount) Validation Rules: Should be a valid entry in the TRANSACTION table. |
| 14 | `LD.TXN.INT.REC` | `LdTxnCodes_IntRec` | TField |  | Transaction code used for statement entry when interest is received on a loan contract. Validation Rules: Should be a valid entry in the TRANSACTION table. |
| 15 | `LD.TXN.COM.ADJ` | `LdTxnCodes_ComAdj` | TField |  | Reserved for future use. |
| 16 | `LD.TXN.INT.ADJ` | `LdTxnCodes_IntAdj` | TField |  | Reserved for future use. |
| 17 | `LD.TXN.INT.ACCRUAL` | `LdTxnCodes_IntAccrual` | TField |  | Transaction code for category entry when interest is accrued on a contract. Validation Rules: Should be a valid entry in TRANSACTION file. |
| 18 | `LD.TXN.COM.ACCRUAL` | `LdTxnCodes_ComAccrual` | TField |  | Transaction code for category entry when commission is accrued on a contract. Validation Rules: Should be a valid entry in the TRANSACTION table. |
| 19 | `LD.TXN.PRIN.DECREASE` | `LdTxnCodes_PrinDecrease` | TField |  | Transaction code for statement entry when a principal decrease is effected in a contract. Validation Rules: Should be a valid entry in TRANSACTION code. |
| 20 | `LD.TXN.CHRG.REC` | `LdTxnCodes_ChrgRec` | TField |  | Transaction code for statement entry when charge is received on a contract. Validation Rules: Should be a valid entry in TRANSACTION table. |
| 21 | `LD.TXN.CHRG.PAY` | `LdTxnCodes_ChrgPay` | TField |  | Transaction code used for statement entry when a charge is paid in a contract. Validation Rules: Should be a valid entry in TRANSACTION table. |
| 22 | `LD.TXN.REVERSAL.DEPOSIT` | `LdTxnCodes_ReversalDeposit` | TField |  | Transaction code for statement entry when a deposit contract is reversed. Validation Rules: Should be a valid entry in TRANSACTION file. |
| 23 | `LD.TXN.REVERSAL.LOAN` | `LdTxnCodes_ReversalLoan` | TField |  | Transaction code for statement entry when a loan contract is reversed. Validation Rules: Should be a valid entry in TRANSACTION table. |
| 24 | `LD.TXN.REVERSAL.PLACEMENT` | `LdTxnCodes_ReversalPlacement` | TField |  | Transaction code for statement entry when a placement contract is reversed. Validation Rules: Should be a valid entry in TRANSACTION file. |
| 25 | `LD.TXN.REV.ACC.REC` | `LdTxnCodes_RevAccRec` | TField |  | Transaction code for reversal of Account Receivable type loan. Validation Rules: Should be a valid entry in TRANSACTION file. |
| 26 | `LD.TXN.REVERSAL.SUNDRY` | `LdTxnCodes_ReversalSundry` | TField |  | Transaction entry for reversal of Sundry Deposit type loan contract. Validation Rules: Should be valid entry in TRANSACTION table. |
| 27 | `LD.TXN.REVERSAL.COMMT` | `LdTxnCodes_ReversalCommt` | TField |  | Reserved for future use. |
| 28 | `LD.TXN.REV.LIAB.COMMT` | `LdTxnCodes_RevLiabCommt` | TField |  | Reserved for future use. |
| 29 | `LD.TXN.TAX.DEB` | `LdTxnCodes_TaxDeb` | TField |  | Transaction code for statement entry when customer's account is debited for tax. Validation Rules: Should be a valid entry in TRANSACTION table. |
| 30 | `LD.TXN.LOCAL.REF` | `LdTxnCodes_LocalRef` |  |  |  |
| 31 | `LD.TXN.RESERVED.10` | `LdTxnCodes_Reserved10` | TField |  |  |
| 32 | `LD.TXN.RESERVED.9` | `LdTxnCodes_Reserved9` | TField |  |  |
| 33 | `LD.TXN.RESERVED.8` | `LdTxnCodes_Reserved8` | TField |  |  |
| 34 | `LD.TXN.RESERVED.7` | `LdTxnCodes_Reserved7` | TField |  |  |
| 35 | `LD.TXN.RESERVED.6` | `LdTxnCodes_Reserved6` | TField |  |  |
| 36 | `LD.TXN.RESERVED.5` | `LdTxnCodes_Reserved5` | TField |  |  |
| 37 | `LD.TXN.RESERVED.4` | `LdTxnCodes_Reserved4` | TField |  |  |
| 38 | `LD.TXN.RESERVED.3` | `LdTxnCodes_Reserved3` | TField |  |  |
| 39 | `LD.TXN.RESERVED.2` | `LdTxnCodes_Reserved2` | TField |  |  |
| 40 | `LD.TXN.RESERVED.1` | `LdTxnCodes_Reserved1` | TField |  |  |
| 41 | `LD.TXN.OVERRIDE` | `LdTxnCodes_Override` |  |  |  |
| 42 | `LD.TXN.RECORD.STATUS` | `LdTxnCodes_RecordStatus` | String |  |  |
| 43 | `LD.TXN.CURR.NO` | `LdTxnCodes_CurrNo` | String |  |  |
| 44 | `LD.TXN.INPUTTER` | `LdTxnCodes_Inputter` |  |  |  |
| 45 | `LD.TXN.DATE.TIME` | `LdTxnCodes_DateTime` |  |  |  |
| 46 | `LD.TXN.AUTHORISER` | `LdTxnCodes_Authoriser` | String |  |  |
| 47 | `LD.TXN.CO.CODE` | `LdTxnCodes_CoCode` | String |  |  |
| 48 | `LD.TXN.DEPT.CODE` | `LdTxnCodes_DeptCode` | String |  |  |
| 49 | `LD.TXN.AUDITOR.CODE` | `LdTxnCodes_AuditorCode` | String |  |  |
| 50 | `LD.TXN.AUDIT.DATE.TIME` | `LdTxnCodes_AuditDateTime` | String |  |  |
