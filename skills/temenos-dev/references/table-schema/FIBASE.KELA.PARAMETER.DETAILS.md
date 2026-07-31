# FIBASE.KELA.PARAMETER.DETAILS — Table Schema

> Source: `INSERTS/I_F.FIBASE.KELA.PARAMETER.DETAILS` in `FIBASE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `KELA.PARAMETER.TRANSFER.RECORD.CODE` | `FibaseKelaParameterDetails_TransferRecordCode` | TField |  | This field stores a transfer record code |
| 2 | `KELA.PARAMETER.BANK.SPECIFIC.CODE` | `FibaseKelaParameterDetails_BankSpecificCode` | TField |  | This field stores the code for the bank |
| 3 | `KELA.PARAMETER.BANKING.GROUP.ID` | `FibaseKelaParameterDetails_BankingGroupId` | TField |  | This field stores banking group ids Values: 41 = Savings Banks 42 = OmaSp 47 = POP banks |
| 4 | `KELA.PARAMETER.RESERVED.8` | `FibaseKelaParameterDetails_Reserved8` |  |  |  |
| 5 | `KELA.PARAMETER.RESERVED.7` | `FibaseKelaParameterDetails_Reserved7` |  |  |  |
| 6 | `KELA.PARAMETER.RESERVED.6` | `FibaseKelaParameterDetails_Reserved6` |  |  |  |
| 7 | `KELA.PARAMETER.RESERVED.5` | `FibaseKelaParameterDetails_Reserved5` |  |  |  |
| 8 | `KELA.PARAMETER.RESERVED.4` | `FibaseKelaParameterDetails_Reserved4` |  |  |  |
| 9 | `KELA.PARAMETER.RESERVED.3` | `FibaseKelaParameterDetails_Reserved3` |  |  |  |
| 10 | `KELA.PARAMETER.RESERVED.2` | `FibaseKelaParameterDetails_Reserved2` |  |  |  |
| 11 | `KELA.PARAMETER.RESERVED.1` | `FibaseKelaParameterDetails_Reserved1` |  |  |  |
| 12 | `KELA.PARAMETER.LOCAL.REF` | `FibaseKelaParameterDetails_LocalRef` |  |  |  |
| 13 | `KELA.PARAMETER.OVERRIDE` | `FibaseKelaParameterDetails_Override` |  |  |  |
| 14 | `KELA.PARAMETER.RECORD.STATUS` | `FibaseKelaParameterDetails_RecordStatus` | String |  |  |
| 15 | `KELA.PARAMETER.CURR.NO` | `FibaseKelaParameterDetails_CurrNo` | String |  |  |
| 16 | `KELA.PARAMETER.INPUTTER` | `FibaseKelaParameterDetails_Inputter` |  |  |  |
| 17 | `KELA.PARAMETER.DATE.TIME` | `FibaseKelaParameterDetails_DateTime` |  |  |  |
| 18 | `KELA.PARAMETER.AUTHORISER` | `FibaseKelaParameterDetails_Authoriser` | String |  |  |
| 19 | `KELA.PARAMETER.CO.CODE` | `FibaseKelaParameterDetails_CoCode` | String |  |  |
| 20 | `KELA.PARAMETER.DEPT.CODE` | `FibaseKelaParameterDetails_DeptCode` | String |  |  |
| 21 | `KELA.PARAMETER.AUDITOR.CODE` | `FibaseKelaParameterDetails_AuditorCode` | String |  |  |
| 22 | `KELA.PARAMETER.AUDIT.DATE.TIME` | `FibaseKelaParameterDetails_AuditDateTime` | String |  |  |
