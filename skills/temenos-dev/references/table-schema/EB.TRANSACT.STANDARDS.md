# EB.TRANSACT.STANDARDS — Table Schema

> Source: `INSERTS/I_F.EB.TRANSACT.STANDARDS` in `EB_Upgrade.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `TRNS.STD.DESCRIPTION` | `EbTransactStandards_Description` |  |  |  |
| 2 | `TRNS.STD.APPLICATION` | `EbTransactStandards_Application` |  |  |  |
| 3 | `TRNS.STD.STANDARDS` | `EbTransactStandards_Standards` |  |  |  |
| 4 | `TRNS.STD.RESERVED.5` | `EbTransactStandards_Reserved5` | TField |  |  |
| 5 | `TRNS.STD.RESERVED.4` | `EbTransactStandards_Reserved4` | TField |  |  |
| 6 | `TRNS.STD.RESERVED.3` | `EbTransactStandards_Reserved3` | TField |  |  |
| 7 | `TRNS.STD.RESERVED.2` | `EbTransactStandards_Reserved2` | TField |  |  |
| 8 | `TRNS.STD.RESERVED.1` | `EbTransactStandards_Reserved1` | TField |  |  |
| 9 | `TRNS.STD.LOCAL.REF` | `EbTransactStandards_LocalRef` |  |  |  |
| 10 | `TRNS.STD.OVERRIDE` | `EbTransactStandards_Override` |  |  |  |
| 11 | `TRNS.STD.RECORD.STATUS` | `EbTransactStandards_RecordStatus` | String |  |  |
| 12 | `TRNS.STD.CURR.NO` | `EbTransactStandards_CurrNo` | String |  |  |
| 13 | `TRNS.STD.INPUTTER` | `EbTransactStandards_Inputter` |  |  |  |
| 14 | `TRNS.STD.DATE.TIME` | `EbTransactStandards_DateTime` |  |  |  |
| 15 | `TRNS.STD.AUTHORISER` | `EbTransactStandards_Authoriser` | String |  |  |
| 16 | `TRNS.STD.CO.CODE` | `EbTransactStandards_CoCode` | String |  |  |
| 17 | `TRNS.STD.DEPT.CODE` | `EbTransactStandards_DeptCode` | String |  |  |
| 18 | `TRNS.STD.AUDITOR.CODE` | `EbTransactStandards_AuditorCode` | String |  |  |
| 19 | `TRNS.STD.AUDIT.DATE.TIME` | `EbTransactStandards_AuditDateTime` | String |  |  |
