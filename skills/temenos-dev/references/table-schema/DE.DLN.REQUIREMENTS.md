# DE.DLN.REQUIREMENTS — Table Schema

> Source: `INSERTS/I_F.DE.DLN.REQUIREMENTS` in `DE_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.DLR.CURRENCY` | `DeDlnRequirements_Currency` |  |  |  |
| 2 | `DE.DLR.MIN.AMOUNT` | `DeDlnRequirements_MinAmount` |  |  |  |
| 3 | `DE.DLR.OVERDUE.TIME.INTERVAL` | `DeDlnRequirements_OverdueTimeInterval` |  |  |  |
| 4 | `DE.DLR.DEFAULT.MIN.AMT` | `DeDlnRequirements_DefaultMinAmt` | TField |  |  |
| 5 | `DE.DLR.DEF.OVRDUE.TIME.INTERVAL` | `DeDlnRequirements_DefOvrdueTimeInterval` | TField |  |  |
| 6 | `DE.DLR.RESERVED.10` | `DeDlnRequirements_Reserved10` | TField |  |  |
| 7 | `DE.DLR.RESERVED.9` | `DeDlnRequirements_Reserved9` | TField |  |  |
| 8 | `DE.DLR.RESERVED.8` | `DeDlnRequirements_Reserved8` | TField |  |  |
| 9 | `DE.DLR.RESERVED.7` | `DeDlnRequirements_Reserved7` | TField |  |  |
| 10 | `DE.DLR.RESERVED.6` | `DeDlnRequirements_Reserved6` | TField |  |  |
| 11 | `DE.DLR.RESERVED.5` | `DeDlnRequirements_Reserved5` | TField |  |  |
| 12 | `DE.DLR.RESERVED.4` | `DeDlnRequirements_Reserved4` | TField |  |  |
| 13 | `DE.DLR.RESERVED.3` | `DeDlnRequirements_Reserved3` | TField |  |  |
| 14 | `DE.DLR.RESERVED.2` | `DeDlnRequirements_Reserved2` | TField |  |  |
| 15 | `DE.DLR.RESERVED.1` | `DeDlnRequirements_Reserved1` | TField |  |  |
| 16 | `DE.DLR.LOCAL.REF` | `DeDlnRequirements_LocalRef` |  |  |  |
| 17 | `DE.DLR.OVERRIDE` | `DeDlnRequirements_Override` |  |  |  |
| 18 | `DE.DLR.RECORD.STATUS` | `DeDlnRequirements_RecordStatus` | String |  |  |
| 19 | `DE.DLR.CURR.NO` | `DeDlnRequirements_CurrNo` | String |  |  |
| 20 | `DE.DLR.INPUTTER` | `DeDlnRequirements_Inputter` |  |  |  |
| 21 | `DE.DLR.DATE.TIME` | `DeDlnRequirements_DateTime` |  |  |  |
| 22 | `DE.DLR.AUTHORISER` | `DeDlnRequirements_Authoriser` | String |  |  |
| 23 | `DE.DLR.CO.CODE` | `DeDlnRequirements_CoCode` | String |  |  |
| 24 | `DE.DLR.DEPT.CODE` | `DeDlnRequirements_DeptCode` | String |  |  |
| 25 | `DE.DLR.AUDITOR.CODE` | `DeDlnRequirements_AuditorCode` | String |  |  |
| 26 | `DE.DLR.AUDIT.DATE.TIME` | `DeDlnRequirements_AuditDateTime` | String |  |  |
