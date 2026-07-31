# FS.GI.DIST.INV.PROXY.RIGHT — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.INV.PROXY.RIGHT` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.INV.PROXY.RIGHT.PARENT.REF.ID` | `FsGiDistInvProxyRight_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.INV.PROXY.RIGHT.ORA.ROWID` | `FsGiDistInvProxyRight_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.INV.PROXY.RIGHT.INVESTOR.ID` | `FsGiDistInvProxyRight_InvestorId` | TField |  | Client Internal ID Multifonds DB Column is NCLIENT. |
| 4 | `FS.GI.DIST.INV.PROXY.RIGHT.PROXY.ID` | `FsGiDistInvProxyRight_ProxyId` | TField |  | Proxy ID (Investor or Register) linked in the entity relationship. Multifonds DB Column is PROXY. |
| 5 | `FS.GI.DIST.INV.PROXY.RIGHT.PROXY.CODE.RIGHTS` | `FsGiDistInvProxyRight_ProxyCodeRights` | TField |  | Rights allocated to proxy ID. Multifonds DB Column is NDROIT. |
| 6 | `FS.GI.DIST.INV.PROXY.RIGHT.RESERVED10` | `FsGiDistInvProxyRight_Reserved10` | TField |  |  |
| 7 | `FS.GI.DIST.INV.PROXY.RIGHT.RESERVED9` | `FsGiDistInvProxyRight_Reserved9` | TField |  |  |
| 8 | `FS.GI.DIST.INV.PROXY.RIGHT.RESERVED8` | `FsGiDistInvProxyRight_Reserved8` | TField |  |  |
| 9 | `FS.GI.DIST.INV.PROXY.RIGHT.RESERVED7` | `FsGiDistInvProxyRight_Reserved7` | TField |  |  |
| 10 | `FS.GI.DIST.INV.PROXY.RIGHT.RESERVED6` | `FsGiDistInvProxyRight_Reserved6` | TField |  |  |
| 11 | `FS.GI.DIST.INV.PROXY.RIGHT.RESERVED5` | `FsGiDistInvProxyRight_Reserved5` | TField |  |  |
| 12 | `FS.GI.DIST.INV.PROXY.RIGHT.RESERVED4` | `FsGiDistInvProxyRight_Reserved4` | TField |  |  |
| 13 | `FS.GI.DIST.INV.PROXY.RIGHT.RESERVED3` | `FsGiDistInvProxyRight_Reserved3` | TField |  |  |
| 14 | `FS.GI.DIST.INV.PROXY.RIGHT.RESERVED2` | `FsGiDistInvProxyRight_Reserved2` | TField |  |  |
| 15 | `FS.GI.DIST.INV.PROXY.RIGHT.RESERVED1` | `FsGiDistInvProxyRight_Reserved1` | TField |  |  |
| 16 | `FS.GI.DIST.INV.PROXY.RIGHT.LOCAL.REF` | `FsGiDistInvProxyRight_LocalRef` |  |  |  |
| 17 | `FS.GI.DIST.INV.PROXY.RIGHT.OVERRIDE` | `FsGiDistInvProxyRight_Override` |  |  |  |
| 18 | `FS.GI.DIST.INV.PROXY.RIGHT.RECORD.STATUS` | `FsGiDistInvProxyRight_RecordStatus` | String |  |  |
| 19 | `FS.GI.DIST.INV.PROXY.RIGHT.CURR.NO` | `FsGiDistInvProxyRight_CurrNo` | String |  |  |
| 20 | `FS.GI.DIST.INV.PROXY.RIGHT.INPUTTER` | `FsGiDistInvProxyRight_Inputter` |  |  |  |
| 21 | `FS.GI.DIST.INV.PROXY.RIGHT.DATE.TIME` | `FsGiDistInvProxyRight_DateTime` |  |  |  |
| 22 | `FS.GI.DIST.INV.PROXY.RIGHT.AUTHORISER` | `FsGiDistInvProxyRight_Authoriser` | String |  |  |
| 23 | `FS.GI.DIST.INV.PROXY.RIGHT.CO.CODE` | `FsGiDistInvProxyRight_CoCode` | String |  |  |
| 24 | `FS.GI.DIST.INV.PROXY.RIGHT.DEPT.CODE` | `FsGiDistInvProxyRight_DeptCode` | String |  |  |
| 25 | `FS.GI.DIST.INV.PROXY.RIGHT.AUDITOR.CODE` | `FsGiDistInvProxyRight_AuditorCode` | String |  |  |
| 26 | `FS.GI.DIST.INV.PROXY.RIGHT.AUDIT.DATE.TIME` | `FsGiDistInvProxyRight_AuditDateTime` | String |  |  |
