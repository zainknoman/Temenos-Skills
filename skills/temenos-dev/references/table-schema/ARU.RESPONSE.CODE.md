# ARU.RESPONSE.CODE — Table Schema

> Source: `INSERTS/I_F.ARU.RESPONSE.CODE` in `CAEBPS_EbillsInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARU.RES.DESCRIPTION` | `AruResponseCode_Description` | TField |  |  |
| 2 | `ARU.RES.LOCAL.REF` | `AruResponseCode_LocalRef` |  |  |  |
| 3 | `ARU.RES.RESERVED.10` | `AruResponseCode_Reserved10` | TField |  |  |
| 4 | `ARU.RES.RESERVED.9` | `AruResponseCode_Reserved9` | TField |  |  |
| 5 | `ARU.RES.RESERVED.8` | `AruResponseCode_Reserved8` | TField |  |  |
| 6 | `ARU.RES.RESERVED.7` | `AruResponseCode_Reserved7` | TField |  |  |
| 7 | `ARU.RES.RESERVED.6` | `AruResponseCode_Reserved6` | TField |  |  |
| 8 | `ARU.RES.RESERVED.5` | `AruResponseCode_Reserved5` | TField |  |  |
| 9 | `ARU.RES.RESERVED.4` | `AruResponseCode_Reserved4` | TField |  |  |
| 10 | `ARU.RES.RESERVED.3` | `AruResponseCode_Reserved3` | TField |  |  |
| 11 | `ARU.RES.RESERVED.2` | `AruResponseCode_Reserved2` | TField |  |  |
| 12 | `ARU.RES.RESERVED.1` | `AruResponseCode_Reserved1` | TField |  |  |
| 13 | `ARU.RES.OVERRIDE` | `AruResponseCode_Override` |  |  |  |
| 14 | `ARU.RES.RECORD.STATUS` | `AruResponseCode_RecordStatus` | String |  |  |
| 15 | `ARU.RES.CURR.NO` | `AruResponseCode_CurrNo` | String |  |  |
| 16 | `ARU.RES.INPUTTER` | `AruResponseCode_Inputter` |  |  |  |
| 17 | `ARU.RES.DATE.TIME` | `AruResponseCode_DateTime` |  |  |  |
| 18 | `ARU.RES.AUTHORISER` | `AruResponseCode_Authoriser` | String |  |  |
| 19 | `ARU.RES.CO.CODE` | `AruResponseCode_CoCode` | String |  |  |
| 20 | `ARU.RES.DEPT.CODE` | `AruResponseCode_DeptCode` | String |  |  |
| 21 | `ARU.RES.AUDITOR.CODE` | `AruResponseCode_AuditorCode` | String |  |  |
| 22 | `ARU.RES.AUDIT.DATE.TIME` | `AruResponseCode_AuditDateTime` | String |  |  |
