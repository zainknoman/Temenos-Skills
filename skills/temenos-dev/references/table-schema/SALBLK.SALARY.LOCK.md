# SALBLK.SALARY.LOCK — Table Schema

> Source: `INSERTS/I_F.SALBLK.SALARY.LOCK` in `SALBLK_SalaryBlocking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SAL.LOCK.SAL.CREDIT.ACC` | `SalblkSalaryLock_SalCreditAcc` | TField |  | This field identifies the account number in which the salary amount received. |
| 2 | `SAL.LOCK.ARRANGEMENT.CCY` | `SalblkSalaryLock_ArrangementCcy` | TField |  | This field identifies the currency of the Loan account. |
| 3 | `SAL.LOCK.SAL.CREDIT.DATE` | `SalblkSalaryLock_SalCreditDate` |  |  |  |
| 4 | `SAL.LOCK.LOCKED.AMOUNT` | `SalblkSalaryLock_LockedAmount` |  |  |  |
| 5 | `SAL.LOCK.LOAN.DUE.DATE` | `SalblkSalaryLock_LoanDueDate` |  |  |  |
| 6 | `SAL.LOCK.AC.LOCK.REF` | `SalblkSalaryLock_AcLockRef` |  |  |  |
| 7 | `SAL.LOCK.LOAN.DUE.AMOUNT` | `SalblkSalaryLock_LoanDueAmount` |  |  |  |
| 8 | `SAL.LOCK.PAYIN.ACCOUNT` | `SalblkSalaryLock_PayinAccount` |  |  |  |
| 9 | `SAL.LOCK.SAL.AC.CO.CODE` | `SalblkSalaryLock_SalAcCoCode` |  |  |  |
| 10 | `SAL.LOCK.RESERVED.10` | `SalblkSalaryLock_Reserved10` | TField |  |  |
| 11 | `SAL.LOCK.RESERVED.9` | `SalblkSalaryLock_Reserved9` | TField |  |  |
| 12 | `SAL.LOCK.RESERVED.8` | `SalblkSalaryLock_Reserved8` | TField |  |  |
| 13 | `SAL.LOCK.RESERVED.7` | `SalblkSalaryLock_Reserved7` | TField |  |  |
| 14 | `SAL.LOCK.RESERVED.6` | `SalblkSalaryLock_Reserved6` | TField |  |  |
| 15 | `SAL.LOCK.RESERVED.5` | `SalblkSalaryLock_Reserved5` | TField |  |  |
| 16 | `SAL.LOCK.RESERVED.4` | `SalblkSalaryLock_Reserved4` | TField |  |  |
| 17 | `SAL.LOCK.RESERVED.3` | `SalblkSalaryLock_Reserved3` | TField |  |  |
| 18 | `SAL.LOCK.RESERVED.2` | `SalblkSalaryLock_Reserved2` | TField |  |  |
| 19 | `SAL.LOCK.RESERVED.1` | `SalblkSalaryLock_Reserved1` | TField |  |  |
| 20 | `SAL.LOCK.LOCAL.REF` | `SalblkSalaryLock_LocalRef` |  |  |  |
| 21 | `SAL.LOCK.OVERRIDE` | `SalblkSalaryLock_Override` |  |  |  |
