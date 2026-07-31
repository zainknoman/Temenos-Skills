# NOSTRO.ACCOUNT — Table Schema

> Source: `INSERTS/I_F.NOSTRO.ACCOUNT` in `AC_AccountOpening.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.NOS.APPLICATION` | `NostroAccount_Application` |  |  |  |
| 2 | `EB.NOS.TXN.TYPE` | `NostroAccount_TxnType` |  |  |  |
| 3 | `EB.NOS.ACCOUNT` | `NostroAccount_Account` |  |  |  |
| 4 | `EB.NOS.REGION.CODE` | `NostroAccount_RegionCode` |  |  |  |
| 5 | `EB.NOS.EFFECTIVE.DATE` | `NostroAccount_EffectiveDate` |  |  |  |
| 6 | `EB.NOS.NOTES` | `NostroAccount_Notes` |  |  |  |
| 7 | `EB.NOS.LAST.EFF.CHANGE` | `NostroAccount_LastEffChange` | TField |  |  |
| 8 | `EB.NOS.RESERVED.10` | `NostroAccount_Reserved10` | TField |  |  |
| 9 | `EB.NOS.RESERVED.9` | `NostroAccount_Reserved9` | TField |  |  |
| 10 | `EB.NOS.RESERVED.8` | `NostroAccount_Reserved8` | TField |  |  |
| 11 | `EB.NOS.RESERVED.7` | `NostroAccount_Reserved7` | TField |  |  |
| 12 | `EB.NOS.RESERVED.6` | `NostroAccount_Reserved6` | TField |  |  |
| 13 | `EB.NOS.RESERVED.5` | `NostroAccount_Reserved5` | TField |  |  |
| 14 | `EB.NOS.RESERVED.4` | `NostroAccount_Reserved4` | TField |  |  |
| 15 | `EB.NOS.RESERVED.3` | `NostroAccount_Reserved3` | TField |  |  |
| 16 | `EB.NOS.RESERVED.2` | `NostroAccount_Reserved2` | TField |  |  |
| 17 | `EB.NOS.RESERVED.1` | `NostroAccount_Reserved1` | TField |  |  |
| 18 | `EB.NOS.OVERRIDE` | `NostroAccount_Override` |  |  |  |
| 19 | `EB.NOS.RECORD.STATUS` | `NostroAccount_RecordStatus` | String |  |  |
| 20 | `EB.NOS.CURR.NO` | `NostroAccount_CurrNo` | String |  |  |
| 21 | `EB.NOS.INPUTTER` | `NostroAccount_Inputter` |  |  |  |
| 22 | `EB.NOS.DATE.TIME` | `NostroAccount_DateTime` |  |  |  |
| 23 | `EB.NOS.AUTHORISER` | `NostroAccount_Authoriser` | String |  |  |
| 24 | `EB.NOS.CO.CODE` | `NostroAccount_CoCode` | String |  |  |
| 25 | `EB.NOS.DEPT.CODE` | `NostroAccount_DeptCode` | String |  |  |
| 26 | `EB.NOS.AUDITOR.CODE` | `NostroAccount_AuditorCode` | String |  |  |
| 27 | `EB.NOS.AUDIT.DATE.TIME` | `NostroAccount_AuditDateTime` | String |  |  |
