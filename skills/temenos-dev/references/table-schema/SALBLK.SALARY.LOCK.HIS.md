# SALBLK.SALARY.LOCK.HIS — Table Schema

> Source: `INSERTS/I_F.SALBLK.SALARY.LOCK.HIS` in `SALBLK_SalaryBlocking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SAL.LOCK.HIS.SAL.CREDIT.ACC` | `SalblkSalaryLockHis_SalCreditAcc` | TField |  | This field identifies the account number in which the salary amount received. |
| 2 | `SAL.LOCK.HIS.ARRANGEMENT.CCY` | `SalblkSalaryLockHis_ArrangementCcy` | TField |  | This field identifies the currency of the Loan account. |
| 3 | `SAL.LOCK.HIS.SAL.CREDIT.DATE` | `SalblkSalaryLockHis_SalCreditDate` |  |  |  |
| 4 | `SAL.LOCK.HIS.LOCKED.AMOUNT` | `SalblkSalaryLockHis_LockedAmount` |  |  |  |
| 5 | `SAL.LOCK.HIS.LOAN.DUE.DATE` | `SalblkSalaryLockHis_LoanDueDate` |  |  |  |
| 6 | `SAL.LOCK.HIS.AC.LOCK.REF` | `SalblkSalaryLockHis_AcLockRef` |  |  |  |
| 7 | `SAL.LOCK.HIS.LOAN.DUE.AMOUNT` | `SalblkSalaryLockHis_LoanDueAmount` |  |  |  |
| 8 | `SAL.LOCK.HIS.PAYIN.ACCOUNT` | `SalblkSalaryLockHis_PayinAccount` |  |  |  |
| 9 | `SAL.LOCK.HIS.SAL.AC.CO.CODE` | `SalblkSalaryLockHis_SalAcCoCode` |  |  |  |
| 10 | `SAL.LOCK.HIS.RESERVED.10` | `SalblkSalaryLockHis_Reserved10` | TField |  |  |
| 11 | `SAL.LOCK.HIS.RESERVED.9` | `SalblkSalaryLockHis_Reserved9` | TField |  |  |
| 12 | `SAL.LOCK.HIS.RESERVED.8` | `SalblkSalaryLockHis_Reserved8` | TField |  |  |
| 13 | `SAL.LOCK.HIS.RESERVED.7` | `SalblkSalaryLockHis_Reserved7` | TField |  |  |
| 14 | `SAL.LOCK.HIS.RESERVED.6` | `SalblkSalaryLockHis_Reserved6` | TField |  |  |
| 15 | `SAL.LOCK.HIS.RESERVED.5` | `SalblkSalaryLockHis_Reserved5` | TField |  |  |
| 16 | `SAL.LOCK.HIS.RESERVED.4` | `SalblkSalaryLockHis_Reserved4` | TField |  |  |
| 17 | `SAL.LOCK.HIS.RESERVED.3` | `SalblkSalaryLockHis_Reserved3` | TField |  |  |
| 18 | `SAL.LOCK.HIS.RESERVED.2` | `SalblkSalaryLockHis_Reserved2` | TField |  |  |
| 19 | `SAL.LOCK.HIS.RESERVED.1` | `SalblkSalaryLockHis_Reserved1` | TField |  |  |
| 20 | `SAL.LOCK.HIS.LOCAL.REF` | `SalblkSalaryLockHis_LocalRef` |  |  |  |
| 21 | `SAL.LOCK.HIS.OVERRIDE` | `SalblkSalaryLockHis_Override` |  |  |  |
