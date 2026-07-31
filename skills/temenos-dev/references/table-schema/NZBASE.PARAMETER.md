# NZBASE.PARAMETER — Table Schema

> Source: `INSERTS/I_F.NZBASE.PARAMETER` in `NZBASE_CustomerAccountInfrastructure.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `NZBASE.PARAMETER.PNZ.OFF.NO.START` | `NzbaseParameter_PnzOffNoStart` | TField |  | This field holds the Start Range of the Office Suspense Account Number. |
| 2 | `NZBASE.PARAMETER.PNZ.OFF.NO.END` | `NzbaseParameter_PnzOffNoEnd` | TField |  | This field holds the End Range of the Office Suspense Account Number. |
| 3 | `NZBASE.PARAMETER.MOD11C.EXEMPT` | `NzbaseParameter_Mod11cExempt` |  |  |  |
| 4 | `NZBASE.PARAMETER.SUFFIX.LEN.ENTRY` | `NzbaseParameter_SuffixLenEntry` | TField |  | The value in this field indicates the length of the suffix in the Account Number that is to be entered by the user in the SETTLE.ACCT.NUMBER field in the XNZ.ADDITIONAL.INFO external property class. |
| 5 | `NZBASE.PARAMETER.SUFFIX.PAD.ZERO` | `NzbaseParameter_SuffixPadZero` | TField |  | The number of zeros to be padded before the suffix when the Account Number is stored in the SETTLE.ACCT.NUMBER field in the XNZ.ADDITIONAL.INFO external property class. |
| 6 | `NZBASE.PARAMETER.BASE.ACCT.NO.LEN` | `NzbaseParameter_BaseAcctNoLen` | TField |  | The length of the Base Account Number. |
| 7 | `NZBASE.PARAMETER.BRANCH.NO.LEN` | `NzbaseParameter_BranchNoLen` | TField |  | The length of the Branch Number. |
| 8 | `NZBASE.PARAMETER.BANK.NO.LEN` | `NzbaseParameter_BankNoLen` | TField |  | The length of the Bank Number (or) Interchange Number. |
| 9 | `NZBASE.PARAMETER.BANK.NO.PAD.ZERO` | `NzbaseParameter_BankNoPadZero` | TField |  | The number of zeros to be padded before the bank number. |
| 10 | `NZBASE.PARAMETER.ACCT.NO.ENTRY.LEN` | `NzbaseParameter_AcctNoEntryLen` | TField |  | The length of the user entered Settlement account number. |
| 11 | `NZBASE.PARAMETER.LOCAL.REF` | `NzbaseParameter_LocalRef` |  |  |  |
| 12 | `NZBASE.PARAMETER.OVERRIDE` | `NzbaseParameter_Override` |  |  |  |
| 13 | `NZBASE.PARAMETER.RECORD.STATUS` | `NzbaseParameter_RecordStatus` | String |  |  |
| 14 | `NZBASE.PARAMETER.CURR.NO` | `NzbaseParameter_CurrNo` | String |  |  |
| 15 | `NZBASE.PARAMETER.INPUTTER` | `NzbaseParameter_Inputter` |  |  |  |
| 16 | `NZBASE.PARAMETER.DATE.TIME` | `NzbaseParameter_DateTime` |  |  |  |
| 17 | `NZBASE.PARAMETER.AUTHORISER` | `NzbaseParameter_Authoriser` | String |  |  |
| 18 | `NZBASE.PARAMETER.CO.CODE` | `NzbaseParameter_CoCode` | String |  |  |
| 19 | `NZBASE.PARAMETER.DEPT.CODE` | `NzbaseParameter_DeptCode` | String |  |  |
| 20 | `NZBASE.PARAMETER.AUDITOR.CODE` | `NzbaseParameter_AuditorCode` | String |  |  |
| 21 | `NZBASE.PARAMETER.AUDIT.DATE.TIME` | `NzbaseParameter_AuditDateTime` | String |  |  |
