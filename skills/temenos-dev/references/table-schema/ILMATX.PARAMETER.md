# ILMATX.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ILMATX.PARAMETER` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MATX.MUTUAL.FUNDS.SAT` | `IlmatxParameter_MutualFundsSat` |  |  |  |
| 2 | `MATX.EXCLUDED.SECURITY.INSTRUMENT` | `IlmatxParameter_ExcludedSecurityInstrument` |  |  |  |
| 3 | `MATX.EXCLUDED.DERIVATIVE.INSTRUMENT` | `IlmatxParameter_ExcludedDerivativeInstrument` |  |  |  |
| 4 | `MATX.BANK.CODE` | `IlmatxParameter_BankCode` | TField |  | This field is configured with the bank code. |
| 5 | `MATX.BRANCH.CODE` | `IlmatxParameter_BranchCode` | TField |  | This field is configured with the branch code. |
| 6 | `MATX.ACCOUNT.CATEGORY` | `IlmatxParameter_AccountCategory` | TField |  | This field is configured with the account category of the bank |
| 7 | `MATX.RESERVED.8` | `IlmatxParameter_Reserved8` |  |  |  |
| 8 | `MATX.RESERVED.7` | `IlmatxParameter_Reserved7` | TField |  | Reserved for future use. |
| 9 | `MATX.RESERVED.6` | `IlmatxParameter_Reserved6` | TField |  | Reserved for future use. |
| 10 | `MATX.RESERVED.5` | `IlmatxParameter_Reserved5` | TField |  | Reserved for future use. |
| 11 | `MATX.RESERVED.4` | `IlmatxParameter_Reserved4` | TField |  | Reserved for future use. |
| 12 | `MATX.RESERVED.3` | `IlmatxParameter_Reserved3` | TField |  | Reserved for future use. |
| 13 | `MATX.RESERVED.2` | `IlmatxParameter_Reserved2` | TField |  | Reserved for future use. |
| 14 | `MATX.RESERVED.1` | `IlmatxParameter_Reserved1` | TField |  | Reserved for future use. |
| 15 | `MATX.LOCAL.REF` | `IlmatxParameter_LocalRef` |  |  |  |
| 16 | `MATX.OVERRIDE` | `IlmatxParameter_Override` |  |  |  |
| 17 | `MATX.RECORD.STATUS` | `IlmatxParameter_RecordStatus` | String |  |  |
| 18 | `MATX.CURR.NO` | `IlmatxParameter_CurrNo` | String |  |  |
| 19 | `MATX.INPUTTER` | `IlmatxParameter_Inputter` |  |  |  |
| 20 | `MATX.DATE.TIME` | `IlmatxParameter_DateTime` |  |  |  |
| 21 | `MATX.AUTHORISER` | `IlmatxParameter_Authoriser` | String |  |  |
| 22 | `MATX.CO.CODE` | `IlmatxParameter_CoCode` | String |  |  |
| 23 | `MATX.DEPT.CODE` | `IlmatxParameter_DeptCode` | String |  |  |
| 24 | `MATX.AUDITOR.CODE` | `IlmatxParameter_AuditorCode` | String |  |  |
| 25 | `MATX.AUDIT.DATE.TIME` | `IlmatxParameter_AuditDateTime` | String |  |  |
