# FS.GI.DIST.PROXY.RIGHT — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.PROXY.RIGHT` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.PROXY.RIGHT.PARENT.REF.ID` | `FsGiDistProxyRight_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.PROXY.RIGHT.ORA.ROWID` | `FsGiDistProxyRight_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.PROXY.RIGHT.REGISTER.ID` | `FsGiDistProxyRight_RegisterId` | TField |  | Register Internal ID. Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.DIST.PROXY.RIGHT.PROXY.ID` | `FsGiDistProxyRight_ProxyId` | TField |  | Proxy ID (Investor/Register) linked in the entity relationship. Multifonds DB Column is PROXY. |
| 5 | `FS.GI.DIST.PROXY.RIGHT.PROXY.CODE.RIGHTS` | `FsGiDistProxyRight_ProxyCodeRights` | TField |  | Rights allocated to Proxy ID Multifonds DB Column is NDROIT. |
| 6 | `FS.GI.DIST.PROXY.RIGHT.RESERVED10` | `FsGiDistProxyRight_Reserved10` | TField |  |  |
| 7 | `FS.GI.DIST.PROXY.RIGHT.RESERVED9` | `FsGiDistProxyRight_Reserved9` | TField |  |  |
| 8 | `FS.GI.DIST.PROXY.RIGHT.RESERVED8` | `FsGiDistProxyRight_Reserved8` | TField |  |  |
| 9 | `FS.GI.DIST.PROXY.RIGHT.RESERVED7` | `FsGiDistProxyRight_Reserved7` | TField |  |  |
| 10 | `FS.GI.DIST.PROXY.RIGHT.RESERVED6` | `FsGiDistProxyRight_Reserved6` | TField |  |  |
| 11 | `FS.GI.DIST.PROXY.RIGHT.RESERVED5` | `FsGiDistProxyRight_Reserved5` | TField |  |  |
| 12 | `FS.GI.DIST.PROXY.RIGHT.RESERVED4` | `FsGiDistProxyRight_Reserved4` | TField |  |  |
| 13 | `FS.GI.DIST.PROXY.RIGHT.RESERVED3` | `FsGiDistProxyRight_Reserved3` | TField |  |  |
| 14 | `FS.GI.DIST.PROXY.RIGHT.RESERVED2` | `FsGiDistProxyRight_Reserved2` | TField |  |  |
| 15 | `FS.GI.DIST.PROXY.RIGHT.RESERVED1` | `FsGiDistProxyRight_Reserved1` | TField |  |  |
| 16 | `FS.GI.DIST.PROXY.RIGHT.LOCAL.REF` | `FsGiDistProxyRight_LocalRef` |  |  |  |
| 17 | `FS.GI.DIST.PROXY.RIGHT.OVERRIDE` | `FsGiDistProxyRight_Override` |  |  |  |
| 18 | `FS.GI.DIST.PROXY.RIGHT.RECORD.STATUS` | `FsGiDistProxyRight_RecordStatus` | String |  |  |
| 19 | `FS.GI.DIST.PROXY.RIGHT.CURR.NO` | `FsGiDistProxyRight_CurrNo` | String |  |  |
| 20 | `FS.GI.DIST.PROXY.RIGHT.INPUTTER` | `FsGiDistProxyRight_Inputter` |  |  |  |
| 21 | `FS.GI.DIST.PROXY.RIGHT.DATE.TIME` | `FsGiDistProxyRight_DateTime` |  |  |  |
| 22 | `FS.GI.DIST.PROXY.RIGHT.AUTHORISER` | `FsGiDistProxyRight_Authoriser` | String |  |  |
| 23 | `FS.GI.DIST.PROXY.RIGHT.CO.CODE` | `FsGiDistProxyRight_CoCode` | String |  |  |
| 24 | `FS.GI.DIST.PROXY.RIGHT.DEPT.CODE` | `FsGiDistProxyRight_DeptCode` | String |  |  |
| 25 | `FS.GI.DIST.PROXY.RIGHT.AUDITOR.CODE` | `FsGiDistProxyRight_AuditorCode` | String |  |  |
| 26 | `FS.GI.DIST.PROXY.RIGHT.AUDIT.DATE.TIME` | `FsGiDistProxyRight_AuditDateTime` | String |  |  |
