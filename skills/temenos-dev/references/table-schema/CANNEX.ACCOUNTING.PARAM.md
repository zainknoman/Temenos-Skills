# CANNEX.ACCOUNTING.PARAM — Table Schema

> Source: `INSERTS/I_F.CANNEX.ACCOUNTING.PARAM` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CANNEX.AC.CURRENCY` | `CannexAccountingParam_Currency` |  |  |  |
| 2 | `CANNEX.AC.DR.ACCOUNT` | `CannexAccountingParam_DrAccount` |  |  |  |
| 3 | `CANNEX.AC.FUND.ACCOUNT` | `CannexAccountingParam_FundAccount` | TField |  | This field is used to indicate if the Cannex GICs to be funded using GL Account or Customer/Agent Account.Note: Default option would be GL Account if not defined. |
| 4 | `CANNEX.AC.RESERVED.2` | `CannexAccountingParam_Reserved2` | TField |  |  |
| 5 | `CANNEX.AC.RESERVED.3` | `CannexAccountingParam_Reserved3` | TField |  |  |
| 6 | `CANNEX.AC.RESERVED.4` | `CannexAccountingParam_Reserved4` | TField |  |  |
| 7 | `CANNEX.AC.RESERVED.5` | `CannexAccountingParam_Reserved5` | TField |  |  |
| 8 | `CANNEX.AC.RESERVED.6` | `CannexAccountingParam_Reserved6` | TField |  |  |
| 9 | `CANNEX.AC.RESERVED.7` | `CannexAccountingParam_Reserved7` | TField |  |  |
| 10 | `CANNEX.AC.RESERVED.8` | `CannexAccountingParam_Reserved8` | TField |  |  |
| 11 | `CANNEX.AC.RESERVED.9` | `CannexAccountingParam_Reserved9` | TField |  |  |
| 12 | `CANNEX.AC.RESERVED.10` | `CannexAccountingParam_Reserved10` | TField |  |  |
| 13 | `CANNEX.AC.LOCAL.REF` | `CannexAccountingParam_LocalRef` |  |  |  |
| 14 | `CANNEX.AC.OVERRIDE` | `CannexAccountingParam_Override` |  |  |  |
| 15 | `CANNEX.AC.RECORD.STATUS` | `CannexAccountingParam_RecordStatus` | String |  |  |
| 16 | `CANNEX.AC.CURR.NO` | `CannexAccountingParam_CurrNo` | String |  |  |
| 17 | `CANNEX.AC.INPUTTER` | `CannexAccountingParam_Inputter` |  |  |  |
| 18 | `CANNEX.AC.DATE.TIME` | `CannexAccountingParam_DateTime` |  |  |  |
| 19 | `CANNEX.AC.AUTHORISER` | `CannexAccountingParam_Authoriser` | String |  |  |
| 20 | `CANNEX.AC.CO.CODE` | `CannexAccountingParam_CoCode` | String |  |  |
| 21 | `CANNEX.AC.DEPT.CODE` | `CannexAccountingParam_DeptCode` | String |  |  |
| 22 | `CANNEX.AC.AUDITOR.CODE` | `CannexAccountingParam_AuditorCode` | String |  |  |
| 23 | `CANNEX.AC.AUDIT.DATE.TIME` | `CannexAccountingParam_AuditDateTime` | String |  |  |
