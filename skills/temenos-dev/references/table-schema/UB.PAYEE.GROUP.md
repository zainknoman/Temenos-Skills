# UB.PAYEE.GROUP — Table Schema

> Source: `INSERTS/I_F.UB.PAYEE.GROUP` in `CAEBPS_EbillsInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UB.PG.SHORT.DESCRP` | `UbPayeeGroup_ShortDescrp` |  |  |  |
| 2 | `UB.PG.DESCRIPTION` | `UbPayeeGroup_Description` |  |  |  |
| 3 | `UB.PG.EXTERNAL.ID` | `UbPayeeGroup_ExternalId` |  |  |  |
| 4 | `UB.PG.RESERVED.10` | `UbPayeeGroup_Reserved10` |  |  |  |
| 5 | `UB.PG.RESERVED.9` | `UbPayeeGroup_Reserved9` |  |  |  |
| 6 | `UB.PG.RESERVED.8` | `UbPayeeGroup_Reserved8` |  |  |  |
| 7 | `UB.PG.ACTIVE` | `UbPayeeGroup_Active` |  |  |  |
| 8 | `UB.PG.RESERVED.7` | `UbPayeeGroup_Reserved7` |  |  |  |
| 9 | `UB.PG.RESERVED.6` | `UbPayeeGroup_Reserved6` |  |  |  |
| 10 | `UB.PG.RESERVED.5` | `UbPayeeGroup_Reserved5` |  |  |  |
| 11 | `UB.PG.RESERVED.4` | `UbPayeeGroup_Reserved4` |  |  |  |
| 12 | `UB.PG.PAYEE.ACCT` | `UbPayeeGroup_PayeeAcct` |  |  |  |
| 13 | `UB.PG.LOCAL.REF` | `UbPayeeGroup_LocalRef` |  |  |  |
| 14 | `UB.PG.RESERVED.3` | `UbPayeeGroup_Reserved3` |  |  |  |
| 15 | `UB.PG.RESERVED.2` | `UbPayeeGroup_Reserved2` |  |  |  |
| 16 | `UB.PG.RESERVED.1` | `UbPayeeGroup_Reserved1` |  |  |  |
| 17 | `UB.PG.OVERRIDE` | `UbPayeeGroup_Override` |  |  |  |
| 18 | `UB.PG.RECORD.STATUS` | `UbPayeeGroup_RecordStatus` |  |  |  |
| 19 | `UB.PG.CURR.NO` | `UbPayeeGroup_CurrNo` |  |  |  |
| 20 | `UB.PG.INPUTTER` | `UbPayeeGroup_Inputter` |  |  |  |
| 21 | `UB.PG.DATE.TIME` | `UbPayeeGroup_DateTime` |  |  |  |
| 22 | `UB.PG.AUTHORISER` | `UbPayeeGroup_Authoriser` |  |  |  |
| 23 | `UB.PG.CO.CODE` | `UbPayeeGroup_CoCode` |  |  |  |
| 24 | `UB.PG.DEPT.CODE` | `UbPayeeGroup_DeptCode` |  |  |  |
| 25 | `UB.PG.AUDITOR.CODE` | `UbPayeeGroup_AuditorCode` |  |  |  |
| 26 | `UB.PG.AUDIT.DATE.TIME` | `UbPayeeGroup_AuditDateTime` |  |  |  |
