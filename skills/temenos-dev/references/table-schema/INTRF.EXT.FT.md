# INTRF.EXT.FT — Table Schema

> Source: `INSERTS/I_F.INTRF.EXT.FT` in `CAONBK_OnlineBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INTR.EXT.FT.BANK.NO` | `IntrfExtFt_BankNo` |  |  |  |
| 2 | `INTR.EXT.FT.TRANSIT.NO` | `IntrfExtFt_TransitNo` |  |  |  |
| 3 | `INTR.EXT.FT.ACCOUNT.NO` | `IntrfExtFt_AccountNo` |  |  |  |
| 4 | `INTR.EXT.FT.INTRF.ALLOWED` | `IntrfExtFt_IntrfAllowed` |  |  |  |
| 5 | `INTR.EXT.FT.LOCAL.REF` | `IntrfExtFt_LocalRef` |  |  |  |
| 6 | `INTR.EXT.FT.RESERVED.10` | `IntrfExtFt_Reserved10` |  |  |  |
| 7 | `INTR.EXT.FT.RESERVED.9` | `IntrfExtFt_Reserved9` |  |  |  |
| 8 | `INTR.EXT.FT.RESERVED.8` | `IntrfExtFt_Reserved8` |  |  |  |
| 9 | `INTR.EXT.FT.RESERVED.7` | `IntrfExtFt_Reserved7` |  |  |  |
| 10 | `INTR.EXT.FT.RESERVED.6` | `IntrfExtFt_Reserved6` |  |  |  |
| 11 | `INTR.EXT.FT.RESERVED.5` | `IntrfExtFt_Reserved5` |  |  |  |
| 12 | `INTR.EXT.FT.RESERVED.4` | `IntrfExtFt_Reserved4` |  |  |  |
| 13 | `INTR.EXT.FT.RESERVED.3` | `IntrfExtFt_Reserved3` |  |  |  |
| 14 | `INTR.EXT.FT.RESERVED.2` | `IntrfExtFt_Reserved2` |  |  |  |
| 15 | `INTR.EXT.FT.RESERVED.1` | `IntrfExtFt_Reserved1` |  |  |  |
| 16 | `INTR.EXT.FT.OVERRIDE` | `IntrfExtFt_Override` |  |  |  |
| 17 | `INTR.EXT.FT.RECORD.STATUS` | `IntrfExtFt_RecordStatus` |  |  |  |
| 18 | `INTR.EXT.FT.CURR.NO` | `IntrfExtFt_CurrNo` |  |  |  |
| 19 | `INTR.EXT.FT.INPUTTER` | `IntrfExtFt_Inputter` |  |  |  |
| 20 | `INTR.EXT.FT.DATE.TIME` | `IntrfExtFt_DateTime` |  |  |  |
| 21 | `INTR.EXT.FT.AUTHORISER` | `IntrfExtFt_Authoriser` |  |  |  |
| 22 | `INTR.EXT.FT.CO.CODE` | `IntrfExtFt_CoCode` |  |  |  |
| 23 | `INTR.EXT.FT.DEPT.CODE` | `IntrfExtFt_DeptCode` |  |  |  |
| 24 | `INTR.EXT.FT.AUDITOR.CODE` | `IntrfExtFt_AuditorCode` |  |  |  |
| 25 | `INTR.EXT.FT.AUDIT.DATE.TIME` | `IntrfExtFt_AuditDateTime` |  |  |  |
