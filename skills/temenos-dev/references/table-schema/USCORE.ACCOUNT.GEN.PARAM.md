# USCORE.ACCOUNT.GEN.PARAM — Table Schema

> Source: `INSERTS/I_F.USCORE.ACCOUNT.GEN.PARAM` in `USCORE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USCORE.AC.GEN.PAR.PRODUCT.LINE` | `UscoreAccountGenParam_ProductLine` |  |  |  |
| 2 | `USCORE.AC.GEN.PAR.GAP` | `UscoreAccountGenParam_Gap` |  |  |  |
| 3 | `USCORE.AC.GEN.PAR.PREFIX` | `UscoreAccountGenParam_Prefix` |  |  |  |
| 4 | `USCORE.AC.GEN.PAR.RESERVED.15` | `UscoreAccountGenParam_Reserved15` |  |  |  |
| 5 | `USCORE.AC.GEN.PAR.RESERVED.14` | `UscoreAccountGenParam_Reserved14` |  |  |  |
| 6 | `USCORE.AC.GEN.PAR.RESERVED.13` | `UscoreAccountGenParam_Reserved13` |  |  |  |
| 7 | `USCORE.AC.GEN.PAR.DEFAULT.PREFIX` | `UscoreAccountGenParam_DefaultPrefix` | TField | Yes | This field is used to set default account number prefix. If PRODCUT.LINE not setup, it will use DEFAULT.PREFIX and account generator gap will be 1. Numeric 1 digits and mandatory field. |
| 8 | `USCORE.AC.GEN.PAR.RESERVED.12` | `UscoreAccountGenParam_Reserved12` | TField |  |  |
| 9 | `USCORE.AC.GEN.PAR.RESERVED.11` | `UscoreAccountGenParam_Reserved11` | TField |  |  |
| 10 | `USCORE.AC.GEN.PAR.RESERVED.10` | `UscoreAccountGenParam_Reserved10` | TField |  |  |
| 11 | `USCORE.AC.GEN.PAR.RESERVED.9` | `UscoreAccountGenParam_Reserved9` | TField |  |  |
| 12 | `USCORE.AC.GEN.PAR.RESERVED.8` | `UscoreAccountGenParam_Reserved8` | TField |  |  |
| 13 | `USCORE.AC.GEN.PAR.RESERVED.7` | `UscoreAccountGenParam_Reserved7` | TField |  |  |
| 14 | `USCORE.AC.GEN.PAR.RESERVED.6` | `UscoreAccountGenParam_Reserved6` | TField |  |  |
| 15 | `USCORE.AC.GEN.PAR.RESERVED.5` | `UscoreAccountGenParam_Reserved5` | TField |  |  |
| 16 | `USCORE.AC.GEN.PAR.RESERVED.4` | `UscoreAccountGenParam_Reserved4` | TField |  |  |
| 17 | `USCORE.AC.GEN.PAR.RESERVED.3` | `UscoreAccountGenParam_Reserved3` | TField |  |  |
| 18 | `USCORE.AC.GEN.PAR.RESERVED.2` | `UscoreAccountGenParam_Reserved2` | TField |  |  |
| 19 | `USCORE.AC.GEN.PAR.RESERVED.1` | `UscoreAccountGenParam_Reserved1` | TField |  |  |
| 20 | `USCORE.AC.GEN.PAR.RECORD.STATUS` | `UscoreAccountGenParam_RecordStatus` | String |  |  |
| 21 | `USCORE.AC.GEN.PAR.CURR.NO` | `UscoreAccountGenParam_CurrNo` | String |  |  |
| 22 | `USCORE.AC.GEN.PAR.INPUTTER` | `UscoreAccountGenParam_Inputter` |  |  |  |
| 23 | `USCORE.AC.GEN.PAR.DATE.TIME` | `UscoreAccountGenParam_DateTime` |  |  |  |
| 24 | `USCORE.AC.GEN.PAR.AUTHORISER` | `UscoreAccountGenParam_Authoriser` | String |  |  |
| 25 | `USCORE.AC.GEN.PAR.CO.CODE` | `UscoreAccountGenParam_CoCode` | String |  |  |
| 26 | `USCORE.AC.GEN.PAR.DEPT.CODE` | `UscoreAccountGenParam_DeptCode` | String |  |  |
| 27 | `USCORE.AC.GEN.PAR.AUDITOR.CODE` | `UscoreAccountGenParam_AuditorCode` | String |  |  |
| 28 | `USCORE.AC.GEN.PAR.AUDIT.DATE.TIME` | `UscoreAccountGenParam_AuditDateTime` | String |  |  |
