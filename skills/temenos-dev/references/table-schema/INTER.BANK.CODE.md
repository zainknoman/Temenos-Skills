# INTER.BANK.CODE — Table Schema

> Source: `INSERTS/I_F.INTER.BANK.CODE` in `HKDDPR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IN.BNK.CODE.DESCRIPTION` | `InterBankCode_Description` |  |  |  |
| 2 | `IN.BNK.CODE.CLR.NOSTRO.ACCOUNT` | `InterBankCode_ClrNostroAccount` |  |  |  |
| 3 | `IN.BNK.CODE.CLR.NOSTRO.CURRENCY` | `InterBankCode_ClrNostroCurrency` |  |  |  |
| 4 | `IN.BNK.CODE.RESERVED.9` | `InterBankCode_Reserved9` | TField |  |  |
| 5 | `IN.BNK.CODE.RESERVED.8` | `InterBankCode_Reserved8` | TField |  |  |
| 6 | `IN.BNK.CODE.RESERVED.7` | `InterBankCode_Reserved7` | TField |  |  |
| 7 | `IN.BNK.CODE.RESERVED.6` | `InterBankCode_Reserved6` | TField |  |  |
| 8 | `IN.BNK.CODE.RESERVED.5` | `InterBankCode_Reserved5` | TField |  |  |
| 9 | `IN.BNK.CODE.RESERVED.4` | `InterBankCode_Reserved4` | TField |  |  |
| 10 | `IN.BNK.CODE.RESERVED.3` | `InterBankCode_Reserved3` | TField |  |  |
| 11 | `IN.BNK.CODE.RESERVED.2` | `InterBankCode_Reserved2` | TField |  |  |
| 12 | `IN.BNK.CODE.RESERVED.1` | `InterBankCode_Reserved1` | TField |  |  |
| 13 | `IN.BNK.CODE.LOCAL.REF` | `InterBankCode_LocalRef` |  |  |  |
| 14 | `IN.BNK.CODE.OVERRIDE` | `InterBankCode_Override` |  |  |  |
| 15 | `IN.BNK.CODE.RECORD.STATUS` | `InterBankCode_RecordStatus` | String |  |  |
| 16 | `IN.BNK.CODE.CURR.NO` | `InterBankCode_CurrNo` | String |  |  |
| 17 | `IN.BNK.CODE.INPUTTER` | `InterBankCode_Inputter` |  |  |  |
| 18 | `IN.BNK.CODE.DATE.TIME` | `InterBankCode_DateTime` |  |  |  |
| 19 | `IN.BNK.CODE.AUTHORISER` | `InterBankCode_Authoriser` | String |  |  |
| 20 | `IN.BNK.CODE.CO.CODE` | `InterBankCode_CoCode` | String |  |  |
| 21 | `IN.BNK.CODE.DEPT.CODE` | `InterBankCode_DeptCode` | String |  |  |
| 22 | `IN.BNK.CODE.AUDITOR.CODE` | `InterBankCode_AuditorCode` | String |  |  |
| 23 | `IN.BNK.CODE.AUDIT.DATE.TIME` | `InterBankCode_AuditDateTime` | String |  |  |
