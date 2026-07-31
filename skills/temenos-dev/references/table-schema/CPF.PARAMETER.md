# CPF.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CPF.PARAMETER` in `FNDINV_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CPF.PARAM.SUSP.CATEGORY` | `CpfParameter_SuspCategory` | TField |  | Suspense category to which the accounting entries should be raised. |
| 2 | `CPF.PARAM.CASH.DEPOSITORY` | `CpfParameter_CashDepository` | TField |  |  |
| 3 | `CPF.PARAM.REINVEST.DEPOSITORY` | `CpfParameter_ReinvestDepository` | TField |  |  |
| 4 | `CPF.PARAM.BUY.TXN.NAME` | `CpfParameter_BuyTxnName` | TField |  | The buy or subscription transaction name in case of CPF/EPF orders. |
| 5 | `CPF.PARAM.SELL.TXN.NAME` | `CpfParameter_SellTxnName` | TField |  | The sell or redemption transaction name in case of CPF/EPF orders. |
| 6 | `CPF.PARAM.LOCAL.REF` | `CpfParameter_LocalRef` |  |  |  |
| 7 | `CPF.PARAM.RESERVED.1` | `CpfParameter_Reserved1` | TField |  |  |
| 8 | `CPF.PARAM.RESERVED.2` | `CpfParameter_Reserved2` | TField |  |  |
| 9 | `CPF.PARAM.RESERVED.3` | `CpfParameter_Reserved3` | TField |  |  |
| 10 | `CPF.PARAM.RESERVED.4` | `CpfParameter_Reserved4` | TField |  |  |
| 11 | `CPF.PARAM.RESERVED.5` | `CpfParameter_Reserved5` | TField |  |  |
| 12 | `CPF.PARAM.RESERVED.6` | `CpfParameter_Reserved6` | TField |  |  |
| 13 | `CPF.PARAM.RESERVED.7` | `CpfParameter_Reserved7` | TField |  |  |
| 14 | `CPF.PARAM.RESERVED.8` | `CpfParameter_Reserved8` | TField |  |  |
| 15 | `CPF.PARAM.RESERVED.9` | `CpfParameter_Reserved9` | TField |  |  |
| 16 | `CPF.PARAM.RESERVED.10` | `CpfParameter_Reserved10` | TField |  |  |
| 17 | `CPF.PARAM.OVERRIDE` | `CpfParameter_Override` |  |  |  |
| 18 | `CPF.PARAM.RECORD.STATUS` | `CpfParameter_RecordStatus` | String |  |  |
| 19 | `CPF.PARAM.CURR.NO` | `CpfParameter_CurrNo` | String |  |  |
| 20 | `CPF.PARAM.INPUTTER` | `CpfParameter_Inputter` |  |  |  |
| 21 | `CPF.PARAM.DATE.TIME` | `CpfParameter_DateTime` |  |  |  |
| 22 | `CPF.PARAM.AUTHORISER` | `CpfParameter_Authoriser` | String |  |  |
| 23 | `CPF.PARAM.CO.CODE` | `CpfParameter_CoCode` | String |  |  |
| 24 | `CPF.PARAM.DEPT.CODE` | `CpfParameter_DeptCode` | String |  |  |
| 25 | `CPF.PARAM.AUDITOR.CODE` | `CpfParameter_AuditorCode` | String |  |  |
| 26 | `CPF.PARAM.AUDIT.DATE.TIME` | `CpfParameter_AuditDateTime` | String |  |  |
