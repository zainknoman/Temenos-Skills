# CAREGS.CDIC.ACCT.GROUP.CODES — Table Schema

> Source: `INSERTS/I_F.CAREGS.CDIC.ACCT.GROUP.CODES` in `CADEPO_CDIC.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CDIC.DEF.CODES.DEFAULT.ACCT.GRP` | `CaregsCdicAcctGroupCodes_DefaultAcctGrp` | TField |  |  |
| 2 | `CDIC.DEF.CODES.DEFAULT.GRP.DESC` | `CaregsCdicAcctGroupCodes_DefaultGrpDesc` | TField |  |  |
| 3 | `CDIC.DEF.CODES.RESERVED.1` | `CaregsCdicAcctGroupCodes_Reserved1` | TField |  |  |
| 4 | `CDIC.DEF.CODES.RESERVED.2` | `CaregsCdicAcctGroupCodes_Reserved2` | TField |  |  |
| 5 | `CDIC.DEF.CODES.RESERVED.3` | `CaregsCdicAcctGroupCodes_Reserved3` | TField |  |  |
| 6 | `CDIC.DEF.CODES.RESERVED.4` | `CaregsCdicAcctGroupCodes_Reserved4` | TField |  |  |
| 7 | `CDIC.DEF.CODES.RESERVED.5` | `CaregsCdicAcctGroupCodes_Reserved5` | TField |  |  |
| 8 | `CDIC.DEF.CODES.LOCAL.REF` | `CaregsCdicAcctGroupCodes_LocalRef` |  |  |  |
| 9 | `CDIC.DEF.CODES.RECORD.STATUS` | `CaregsCdicAcctGroupCodes_RecordStatus` | String |  |  |
| 10 | `CDIC.DEF.CODES.CURR.NO` | `CaregsCdicAcctGroupCodes_CurrNo` | String |  |  |
| 11 | `CDIC.DEF.CODES.INPUTTER` | `CaregsCdicAcctGroupCodes_Inputter` |  |  |  |
| 12 | `CDIC.DEF.CODES.DATE.TIME` | `CaregsCdicAcctGroupCodes_DateTime` |  |  |  |
| 13 | `CDIC.DEF.CODES.AUTHORISER` | `CaregsCdicAcctGroupCodes_Authoriser` | String |  |  |
| 14 | `CDIC.DEF.CODES.CO.CODE` | `CaregsCdicAcctGroupCodes_CoCode` | String |  |  |
| 15 | `CDIC.DEF.CODES.DEPT.CODE` | `CaregsCdicAcctGroupCodes_DeptCode` | String |  |  |
| 16 | `CDIC.DEF.CODES.AUDITOR.CODE` | `CaregsCdicAcctGroupCodes_AuditorCode` | String |  |  |
| 17 | `CDIC.DEF.CODES.AUDIT.DATE.TIME` | `CaregsCdicAcctGroupCodes_AuditDateTime` | String |  |  |
