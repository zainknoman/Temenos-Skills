# FS.GA.WEM.EXCEP.CATEGORY — Table Schema

> Source: `INSERTS/I_F.FS.GA.WEM.EXCEP.CATEGORY` in `FS_WEM.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EXCEPTION.CATEG.SERIAL` | `FsGaWemExcepCategory_Serial` | TField |  | Family ID Multifonds DB Column is P_SERIAL. |
| 2 | `EXCEPTION.CATEG.USER` | `FsGaWemExcepCategory_User` | TField |  | User Multifonds DB Column is P_USER. |
| 3 | `EXCEPTION.CATEG.ROLE` | `FsGaWemExcepCategory_Role` | TField |  | Right Flag Multifonds DB Column is P_ROLE. |
| 4 | `EXCEPTION.CATEG.JUSTIFICATION.TEXT` | `FsGaWemExcepCategory_JustificationText` | TField |  | JUSTIFICATION.TEXT Multifonds DB Column is P_STRING. |
| 5 | `EXCEPTION.CATEG.CATEGORY` | `FsGaWemExcepCategory_Category` | TField |  | CATEGORY Multifonds DB Column is P_CATEGORY. |
| 6 | `EXCEPTION.CATEG.STATUS` | `FsGaWemExcepCategory_Status` | TField |  | STATUS Multifonds DB Column is P_STATUS. |
| 7 | `EXCEPTION.CATEG.RESERVED5` | `FsGaWemExcepCategory_Reserved5` | TField |  |  |
| 8 | `EXCEPTION.CATEG.RESERVED4` | `FsGaWemExcepCategory_Reserved4` | TField |  |  |
| 9 | `EXCEPTION.CATEG.RESERVED3` | `FsGaWemExcepCategory_Reserved3` | TField |  |  |
| 10 | `EXCEPTION.CATEG.RESERVED2` | `FsGaWemExcepCategory_Reserved2` | TField |  |  |
| 11 | `EXCEPTION.CATEG.RESERVED1` | `FsGaWemExcepCategory_Reserved1` | TField |  |  |
| 12 | `EXCEPTION.CATEG.LOCAL.REF` | `FsGaWemExcepCategory_LocalRef` |  |  |  |
| 13 | `EXCEPTION.CATEG.OVERRIDE` | `FsGaWemExcepCategory_Override` |  |  |  |
| 14 | `EXCEPTION.CATEG.RECORD.STATUS` | `FsGaWemExcepCategory_RecordStatus` | String |  |  |
| 15 | `EXCEPTION.CATEG.CURR.NO` | `FsGaWemExcepCategory_CurrNo` | String |  |  |
| 16 | `EXCEPTION.CATEG.INPUTTER` | `FsGaWemExcepCategory_Inputter` |  |  |  |
| 17 | `EXCEPTION.CATEG.DATE.TIME` | `FsGaWemExcepCategory_DateTime` |  |  |  |
| 18 | `EXCEPTION.CATEG.AUTHORISER` | `FsGaWemExcepCategory_Authoriser` | String |  |  |
| 19 | `EXCEPTION.CATEG.CO.CODE` | `FsGaWemExcepCategory_CoCode` | String |  |  |
| 20 | `EXCEPTION.CATEG.DEPT.CODE` | `FsGaWemExcepCategory_DeptCode` | String |  |  |
| 21 | `EXCEPTION.CATEG.AUDITOR.CODE` | `FsGaWemExcepCategory_AuditorCode` | String |  |  |
| 22 | `EXCEPTION.CATEG.AUDIT.DATE.TIME` | `FsGaWemExcepCategory_AuditDateTime` | String |  |  |
