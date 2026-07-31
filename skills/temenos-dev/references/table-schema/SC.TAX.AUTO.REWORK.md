# SC.TAX.AUTO.REWORK — Table Schema

> Source: `INSERTS/I_F.SC.TAX.AUTO.REWORK` in `SC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.TAR.DESCRIPTION` | `ScTaxAutoRework_Description` |  |  |  |
| 2 | `SC.TAR.REWORK.TXN.ID` | `ScTaxAutoRework_ReworkTxnId` |  |  |  |
| 3 | `SC.TAR.RESERVED.10` | `ScTaxAutoRework_Reserved10` | TField |  |  |
| 4 | `SC.TAR.RESERVED.9` | `ScTaxAutoRework_Reserved9` | TField |  |  |
| 5 | `SC.TAR.RESERVED.8` | `ScTaxAutoRework_Reserved8` | TField |  |  |
| 6 | `SC.TAR.RESERVED.7` | `ScTaxAutoRework_Reserved7` | TField |  |  |
| 7 | `SC.TAR.RESERVED.6` | `ScTaxAutoRework_Reserved6` | TField |  |  |
| 8 | `SC.TAR.RESERVED.5` | `ScTaxAutoRework_Reserved5` | TField |  |  |
| 9 | `SC.TAR.RESERVED.4` | `ScTaxAutoRework_Reserved4` | TField |  |  |
| 10 | `SC.TAR.RESERVED.3` | `ScTaxAutoRework_Reserved3` | TField |  |  |
| 11 | `SC.TAR.RESERVED.2` | `ScTaxAutoRework_Reserved2` | TField |  |  |
| 12 | `SC.TAR.RESERVED.1` | `ScTaxAutoRework_Reserved1` | TField |  |  |
| 13 | `SC.TAR.LOCAL.REF` | `ScTaxAutoRework_LocalRef` |  |  |  |
| 14 | `SC.TAR.OVERRIDE` | `ScTaxAutoRework_Override` |  |  |  |
| 15 | `SC.TAR.RECORD.STATUS` | `ScTaxAutoRework_RecordStatus` | String |  |  |
| 16 | `SC.TAR.CURR.NO` | `ScTaxAutoRework_CurrNo` | String |  |  |
| 17 | `SC.TAR.INPUTTER` | `ScTaxAutoRework_Inputter` |  |  |  |
| 18 | `SC.TAR.DATE.TIME` | `ScTaxAutoRework_DateTime` |  |  |  |
| 19 | `SC.TAR.AUTHORISER` | `ScTaxAutoRework_Authoriser` | String |  |  |
| 20 | `SC.TAR.CO.CODE` | `ScTaxAutoRework_CoCode` | String |  |  |
| 21 | `SC.TAR.DEPT.CODE` | `ScTaxAutoRework_DeptCode` | String |  |  |
| 22 | `SC.TAR.AUDITOR.CODE` | `ScTaxAutoRework_AuditorCode` | String |  |  |
| 23 | `SC.TAR.AUDIT.DATE.TIME` | `ScTaxAutoRework_AuditDateTime` | String |  |  |
