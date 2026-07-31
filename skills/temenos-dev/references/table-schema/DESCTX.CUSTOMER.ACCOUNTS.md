# DESCTX.CUSTOMER.ACCOUNTS — Table Schema

> Source: `INSERTS/I_F.DESCTX.CUSTOMER.ACCOUNTS` in `DESCTX_Taxation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SECTRAS.CUS.ACCT.ACCOUNT.NO` | `DesctxCustomerAccounts_AccountNo` |  |  |  |
| 2 | `SECTRAS.CUS.ACCT.DEPOSIT.NO` | `DesctxCustomerAccounts_DepositNo` |  |  |  |
| 3 | `SECTRAS.CUS.ACCT.SEC.ACC.MASTER` | `DesctxCustomerAccounts_SecAccMaster` |  |  |  |
| 4 | `SECTRAS.CUS.ACCT.LOCAL.REF` | `DesctxCustomerAccounts_LocalRef` |  |  |  |
| 5 | `SECTRAS.CUS.ACCT.RESERVED.8` | `DesctxCustomerAccounts_Reserved8` | TField |  |  |
| 6 | `SECTRAS.CUS.ACCT.RESERVED.7` | `DesctxCustomerAccounts_Reserved7` | TField |  |  |
| 7 | `SECTRAS.CUS.ACCT.RESERVED.6` | `DesctxCustomerAccounts_Reserved6` | TField |  |  |
| 8 | `SECTRAS.CUS.ACCT.RESERVED.5` | `DesctxCustomerAccounts_Reserved5` | TField |  |  |
| 9 | `SECTRAS.CUS.ACCT.RESERVED.4` | `DesctxCustomerAccounts_Reserved4` | TField |  |  |
| 10 | `SECTRAS.CUS.ACCT.RESERVED.3` | `DesctxCustomerAccounts_Reserved3` | TField |  |  |
| 11 | `SECTRAS.CUS.ACCT.RESERVED.2` | `DesctxCustomerAccounts_Reserved2` | TField |  |  |
| 12 | `SECTRAS.CUS.ACCT.RESERVED.1` | `DesctxCustomerAccounts_Reserved1` | TField |  |  |
| 13 | `SECTRAS.CUS.ACCT.OVERRIDE` | `DesctxCustomerAccounts_Override` |  |  |  |
