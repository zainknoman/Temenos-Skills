# IL.SOURCESYS — Table Schema

> Source: `INSERTS/I_F.IL.SOURCESYS` in `IL_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IL.SRCSYS.SRCSYS.NAME` | `IlSourcesys_SrcsysName` | TField | Yes | This field holds the name of the source system. Validation Rules: Standard T24 Alphanumeric field and accepts upto 35 characters. Mandatory field. |
| 2 | `IL.SRCSYS.SRCSYS.DESCRIPTION` | `IlSourcesys_SrcsysDescription` |  |  |  |
| 3 | `IL.SRCSYS.RESERVED.10` | `IlSourcesys_Reserved10` |  |  |  |
| 4 | `IL.SRCSYS.RESERVED.9` | `IlSourcesys_Reserved9` |  |  |  |
| 5 | `IL.SRCSYS.RESERVED.8` | `IlSourcesys_Reserved8` |  |  |  |
| 6 | `IL.SRCSYS.RESERVED.7` | `IlSourcesys_Reserved7` | TField |  |  |
| 7 | `IL.SRCSYS.RESERVED.6` | `IlSourcesys_Reserved6` | TField |  |  |
| 8 | `IL.SRCSYS.RESERVED.5` | `IlSourcesys_Reserved5` | TField |  |  |
| 9 | `IL.SRCSYS.RESERVED.4` | `IlSourcesys_Reserved4` | TField |  |  |
| 10 | `IL.SRCSYS.RESERVED.3` | `IlSourcesys_Reserved3` | TField |  |  |
| 11 | `IL.SRCSYS.RESERVED.2` | `IlSourcesys_Reserved2` | TField |  |  |
| 12 | `IL.SRCSYS.RESERVED.1` | `IlSourcesys_Reserved1` | TField |  |  |
| 13 | `IL.SRCSYS.LOCAL.REF` | `IlSourcesys_LocalRef` |  |  |  |
| 14 | `IL.SRCSYS.OVERRIDE` | `IlSourcesys_Override` |  |  |  |
| 15 | `IL.SRCSYS.RECORD.STATUS` | `IlSourcesys_RecordStatus` | String |  |  |
| 16 | `IL.SRCSYS.CURR.NO` | `IlSourcesys_CurrNo` | String |  |  |
| 17 | `IL.SRCSYS.INPUTTER` | `IlSourcesys_Inputter` |  |  |  |
| 18 | `IL.SRCSYS.DATE.TIME` | `IlSourcesys_DateTime` |  |  |  |
| 19 | `IL.SRCSYS.AUTHORISER` | `IlSourcesys_Authoriser` | String |  |  |
| 20 | `IL.SRCSYS.CO.CODE` | `IlSourcesys_CoCode` | String |  |  |
| 21 | `IL.SRCSYS.DEPT.CODE` | `IlSourcesys_DeptCode` | String |  |  |
| 22 | `IL.SRCSYS.AUDITOR.CODE` | `IlSourcesys_AuditorCode` | String |  |  |
| 23 | `IL.SRCSYS.AUDIT.DATE.TIME` | `IlSourcesys_AuditDateTime` | String |  |  |
