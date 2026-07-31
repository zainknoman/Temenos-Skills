# MO.ACCOUNT.MAPPING — Table Schema

> Source: `INSERTS/I_F.MO.ACCOUNT.MAPPING` in `MO_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MO.AC.ACCT.DR.TRANS` | `MoAccountMapping_AcctDrTrans` |  |  |  |
| 2 | `MO.AC.ACCT.CR.TRANS` | `MoAccountMapping_AcctCrTrans` |  |  |  |
| 3 | `MO.AC.ACCT.CAT.DR.TRANS` | `MoAccountMapping_AcctCatDrTrans` |  |  |  |
| 4 | `MO.AC.ACCT.CAT.CR.TRANS` | `MoAccountMapping_AcctCatCrTrans` |  |  |  |
| 5 | `MO.AC.ACCT.EXCLUDE` | `MoAccountMapping_AcctExclude` |  |  |  |
| 6 | `MO.AC.RESERVED.10` | `MoAccountMapping_Reserved10` | TField |  |  |
| 7 | `MO.AC.RESERVED.9` | `MoAccountMapping_Reserved9` | TField |  |  |
| 8 | `MO.AC.RESERVED.8` | `MoAccountMapping_Reserved8` | TField |  |  |
| 9 | `MO.AC.RESERVED.7` | `MoAccountMapping_Reserved7` | TField |  |  |
| 10 | `MO.AC.RESERVED.6` | `MoAccountMapping_Reserved6` | TField |  |  |
| 11 | `MO.AC.RESERVED.5` | `MoAccountMapping_Reserved5` | TField |  |  |
| 12 | `MO.AC.RESERVED.4` | `MoAccountMapping_Reserved4` | TField |  |  |
| 13 | `MO.AC.RESERVED.3` | `MoAccountMapping_Reserved3` | TField |  |  |
| 14 | `MO.AC.RESERVED.2` | `MoAccountMapping_Reserved2` | TField |  |  |
| 15 | `MO.AC.RESERVED.1` | `MoAccountMapping_Reserved1` | TField |  |  |
| 16 | `MO.AC.LOCAL.REF` | `MoAccountMapping_LocalRef` |  |  |  |
| 17 | `MO.AC.OVERRIDE` | `MoAccountMapping_Override` |  |  |  |
| 18 | `MO.AC.RECORD.STATUS` | `MoAccountMapping_RecordStatus` | String |  |  |
| 19 | `MO.AC.CURR.NO` | `MoAccountMapping_CurrNo` | String |  |  |
| 20 | `MO.AC.INPUTTER` | `MoAccountMapping_Inputter` |  |  |  |
| 21 | `MO.AC.DATE.TIME` | `MoAccountMapping_DateTime` |  |  |  |
| 22 | `MO.AC.AUTHORISER` | `MoAccountMapping_Authoriser` | String |  |  |
| 23 | `MO.AC.CO.CODE` | `MoAccountMapping_CoCode` | String |  |  |
| 24 | `MO.AC.DEPT.CODE` | `MoAccountMapping_DeptCode` | String |  |  |
| 25 | `MO.AC.AUDITOR.CODE` | `MoAccountMapping_AuditorCode` | String |  |  |
| 26 | `MO.AC.AUDIT.DATE.TIME` | `MoAccountMapping_AuditDateTime` | String |  |  |
