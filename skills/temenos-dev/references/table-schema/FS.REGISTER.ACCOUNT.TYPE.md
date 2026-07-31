# FS.REGISTER.ACCOUNT.TYPE — Table Schema

> Source: `INSERTS/I_F.FS.REGISTER.ACCOUNT.TYPE` in `FS_CommonCustom.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.REGISTER.ACCOUNT.TYPE.DESCRIPTION` | `FsRegisterAccountType_Description` |  |  |  |
| 2 | `FS.REGISTER.ACCOUNT.TYPE.FILTER.KEY` | `FsRegisterAccountType_FilterKey` | TField |  | Filter key for the lookup code Multifonds DB Column is ABREGE. |
| 3 | `FS.REGISTER.ACCOUNT.TYPE.RECORD.ID` | `FsRegisterAccountType_RecordId` | TField |  | Record ID Multifonds DB Column is RECORDID. |
| 4 | `FS.REGISTER.ACCOUNT.TYPE.RESERVED10` | `FsRegisterAccountType_Reserved10` | TField |  |  |
| 5 | `FS.REGISTER.ACCOUNT.TYPE.RESERVED9` | `FsRegisterAccountType_Reserved9` | TField |  |  |
| 6 | `FS.REGISTER.ACCOUNT.TYPE.RESERVED8` | `FsRegisterAccountType_Reserved8` | TField |  |  |
| 7 | `FS.REGISTER.ACCOUNT.TYPE.RESERVED7` | `FsRegisterAccountType_Reserved7` | TField |  |  |
| 8 | `FS.REGISTER.ACCOUNT.TYPE.RESERVED6` | `FsRegisterAccountType_Reserved6` | TField |  |  |
| 9 | `FS.REGISTER.ACCOUNT.TYPE.RESERVED5` | `FsRegisterAccountType_Reserved5` | TField |  |  |
| 10 | `FS.REGISTER.ACCOUNT.TYPE.RESERVED4` | `FsRegisterAccountType_Reserved4` | TField |  |  |
| 11 | `FS.REGISTER.ACCOUNT.TYPE.RESERVED3` | `FsRegisterAccountType_Reserved3` | TField |  |  |
| 12 | `FS.REGISTER.ACCOUNT.TYPE.RESERVED2` | `FsRegisterAccountType_Reserved2` | TField |  |  |
| 13 | `FS.REGISTER.ACCOUNT.TYPE.RESERVED1` | `FsRegisterAccountType_Reserved1` | TField |  |  |
| 14 | `FS.REGISTER.ACCOUNT.TYPE.LOCAL.REF` | `FsRegisterAccountType_LocalRef` |  |  |  |
| 15 | `FS.REGISTER.ACCOUNT.TYPE.OVERRIDE` | `FsRegisterAccountType_Override` |  |  |  |
| 16 | `FS.REGISTER.ACCOUNT.TYPE.RECORD.STATUS` | `FsRegisterAccountType_RecordStatus` | String |  |  |
| 17 | `FS.REGISTER.ACCOUNT.TYPE.CURR.NO` | `FsRegisterAccountType_CurrNo` | String |  |  |
| 18 | `FS.REGISTER.ACCOUNT.TYPE.INPUTTER` | `FsRegisterAccountType_Inputter` |  |  |  |
| 19 | `FS.REGISTER.ACCOUNT.TYPE.DATE.TIME` | `FsRegisterAccountType_DateTime` |  |  |  |
| 20 | `FS.REGISTER.ACCOUNT.TYPE.AUTHORISER` | `FsRegisterAccountType_Authoriser` | String |  |  |
| 21 | `FS.REGISTER.ACCOUNT.TYPE.CO.CODE` | `FsRegisterAccountType_CoCode` | String |  |  |
| 22 | `FS.REGISTER.ACCOUNT.TYPE.DEPT.CODE` | `FsRegisterAccountType_DeptCode` | String |  |  |
| 23 | `FS.REGISTER.ACCOUNT.TYPE.AUDITOR.CODE` | `FsRegisterAccountType_AuditorCode` | String |  |  |
| 24 | `FS.REGISTER.ACCOUNT.TYPE.AUDIT.DATE.TIME` | `FsRegisterAccountType_AuditDateTime` | String |  |  |
