# SC.PART.SETT.PARAM — Table Schema

> Source: `INSERTS/I_F.SC.PART.SETT.PARAM` in `SC_SctSettlement.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.PSP.DEPOSITORY` | `ScPartSettParam_Depository` |  |  |  |
| 2 | `SC.PSP.SUB.ACCOUNT` | `ScPartSettParam_SubAccount` |  |  |  |
| 3 | `SC.PSP.ALLOW.PART.SETT` | `ScPartSettParam_AllowPartSett` |  |  |  |
| 4 | `SC.PSP.PART.SETT.QTY` | `ScPartSettParam_PartSettQty` |  |  |  |
| 5 | `SC.PSP.PART.SETT.CCY` | `ScPartSettParam_PartSettCcy` |  |  |  |
| 6 | `SC.PSP.PART.SETT.AMT` | `ScPartSettParam_PartSettAmt` |  |  |  |
| 7 | `SC.PSP.RESERVED.10` | `ScPartSettParam_Reserved10` | TField |  |  |
| 8 | `SC.PSP.RESERVED.9` | `ScPartSettParam_Reserved9` | TField |  |  |
| 9 | `SC.PSP.RESERVED.8` | `ScPartSettParam_Reserved8` | TField |  |  |
| 10 | `SC.PSP.RESERVED.7` | `ScPartSettParam_Reserved7` | TField |  |  |
| 11 | `SC.PSP.RESERVED.6` | `ScPartSettParam_Reserved6` | TField |  |  |
| 12 | `SC.PSP.RESERVED.5` | `ScPartSettParam_Reserved5` | TField |  |  |
| 13 | `SC.PSP.RESERVED.4` | `ScPartSettParam_Reserved4` | TField |  |  |
| 14 | `SC.PSP.RESERVED.3` | `ScPartSettParam_Reserved3` | TField |  |  |
| 15 | `SC.PSP.RESERVED.2` | `ScPartSettParam_Reserved2` | TField |  |  |
| 16 | `SC.PSP.RESERVED.1` | `ScPartSettParam_Reserved1` | TField |  |  |
| 17 | `SC.PSP.LOCAL.REF` | `ScPartSettParam_LocalRef` |  |  |  |
| 18 | `SC.PSP.OVERRIDE` | `ScPartSettParam_Override` |  |  |  |
| 19 | `SC.PSP.RECORD.STATUS` | `ScPartSettParam_RecordStatus` | String |  |  |
| 20 | `SC.PSP.CURR.NO` | `ScPartSettParam_CurrNo` | String |  |  |
| 21 | `SC.PSP.INPUTTER` | `ScPartSettParam_Inputter` |  |  |  |
| 22 | `SC.PSP.DATE.TIME` | `ScPartSettParam_DateTime` |  |  |  |
| 23 | `SC.PSP.AUTHORISER` | `ScPartSettParam_Authoriser` | String |  |  |
| 24 | `SC.PSP.CO.CODE` | `ScPartSettParam_CoCode` | String |  |  |
| 25 | `SC.PSP.DEPT.CODE` | `ScPartSettParam_DeptCode` | String |  |  |
| 26 | `SC.PSP.AUDITOR.CODE` | `ScPartSettParam_AuditorCode` | String |  |  |
| 27 | `SC.PSP.AUDIT.DATE.TIME` | `ScPartSettParam_AuditDateTime` | String |  |  |
