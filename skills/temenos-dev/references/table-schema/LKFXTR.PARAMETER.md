# LKFXTR.PARAMETER — Table Schema

> Source: `INSERTS/I_F.LKFXTR.PARAMETER` in `LKFXTR_ForexTransactionReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LKFXTR.PARAM.BANK.CODE` | `LkfxtrParameter_BankCode` | TField |  |  |
| 2 | `LKFXTR.PARAM.BANK.CUSTOMER.ID` | `LkfxtrParameter_BankCustomerId` | TField |  |  |
| 3 | `LKFXTR.PARAM.CURRENCY` | `LkfxtrParameter_Currency` | TField |  |  |
| 4 | `LKFXTR.PARAM.FORM.ID.TYPE` | `LkfxtrParameter_FormIdType` |  |  |  |
| 5 | `LKFXTR.PARAM.GLOBAL.ID.TYPE` | `LkfxtrParameter_GlobalIdType` |  |  |  |
| 6 | `LKFXTR.PARAM.APPLICATION` | `LkfxtrParameter_Application` |  |  |  |
| 7 | `LKFXTR.PARAM.LOCAL.REF` | `LkfxtrParameter_LocalRef` |  |  |  |
| 8 | `LKFXTR.PARAM.OVERRIDE` | `LkfxtrParameter_Override` |  |  |  |
| 9 | `LKFXTR.PARAM.RECORD.STATUS` | `LkfxtrParameter_RecordStatus` | String |  |  |
| 10 | `LKFXTR.PARAM.CURR.NO` | `LkfxtrParameter_CurrNo` | String |  |  |
| 11 | `LKFXTR.PARAM.INPUTTER` | `LkfxtrParameter_Inputter` |  |  |  |
| 12 | `LKFXTR.PARAM.DATE.TIME` | `LkfxtrParameter_DateTime` |  |  |  |
| 13 | `LKFXTR.PARAM.AUTHORISER` | `LkfxtrParameter_Authoriser` | String |  |  |
| 14 | `LKFXTR.PARAM.CO.CODE` | `LkfxtrParameter_CoCode` | String |  |  |
| 15 | `LKFXTR.PARAM.DEPT.CODE` | `LkfxtrParameter_DeptCode` | String |  |  |
| 16 | `LKFXTR.PARAM.AUDITOR.CODE` | `LkfxtrParameter_AuditorCode` | String |  |  |
| 17 | `LKFXTR.PARAM.AUDIT.DATE.TIME` | `LkfxtrParameter_AuditDateTime` | String |  |  |
