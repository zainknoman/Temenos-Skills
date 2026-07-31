# FS.BMAP.TXN.REF — Table Schema

> Source: `INSERTS/I_F.FS.BMAP.TXN.REF` in `FS_ApplicationFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.BMAP.TXN.CHILD.APP.NAME` | `FsBmapTxnRef_ChildAppName` |  |  |  |
| 2 | `FS.BMAP.TXN.TXN.REF` | `FsBmapTxnRef_TxnRef` |  |  |  |
| 3 | `FS.BMAP.TXN.DELETED.CHILD.APP.NAME` | `FsBmapTxnRef_DeletedChildAppName` |  |  |  |
| 4 | `FS.BMAP.TXN.DELETED.TXN.REF` | `FsBmapTxnRef_DeletedTxnRef` |  |  |  |
| 5 | `FS.BMAP.TXN.UNIQUE.IDENTIFIER` | `FsBmapTxnRef_UniqueIdentifier` | TField |  |  |
| 6 | `FS.BMAP.TXN.RESERVED5` | `FsBmapTxnRef_Reserved5` | TField |  |  |
| 7 | `FS.BMAP.TXN.RESERVED4` | `FsBmapTxnRef_Reserved4` | TField |  |  |
| 8 | `FS.BMAP.TXN.RESERVED3` | `FsBmapTxnRef_Reserved3` | TField |  |  |
| 9 | `FS.BMAP.TXN.RESERVED2` | `FsBmapTxnRef_Reserved2` | TField |  |  |
| 10 | `FS.BMAP.TXN.RESERVED1` | `FsBmapTxnRef_Reserved1` | TField |  |  |
| 11 | `FS.BMAP.TXN.LOCAL.REF` | `FsBmapTxnRef_LocalRef` |  |  |  |
| 12 | `FS.BMAP.TXN.OVERRIDE` | `FsBmapTxnRef_Override` |  |  |  |
| 13 | `FS.BMAP.TXN.RECORD.STATUS` | `FsBmapTxnRef_RecordStatus` | String |  |  |
| 14 | `FS.BMAP.TXN.CURR.NO` | `FsBmapTxnRef_CurrNo` | String |  |  |
| 15 | `FS.BMAP.TXN.INPUTTER` | `FsBmapTxnRef_Inputter` |  |  |  |
| 16 | `FS.BMAP.TXN.DATE.TIME` | `FsBmapTxnRef_DateTime` |  |  |  |
| 17 | `FS.BMAP.TXN.AUTHORISER` | `FsBmapTxnRef_Authoriser` | String |  |  |
| 18 | `FS.BMAP.TXN.CO.CODE` | `FsBmapTxnRef_CoCode` | String |  |  |
| 19 | `FS.BMAP.TXN.DEPT.CODE` | `FsBmapTxnRef_DeptCode` | String |  |  |
| 20 | `FS.BMAP.TXN.AUDITOR.CODE` | `FsBmapTxnRef_AuditorCode` | String |  |  |
| 21 | `FS.BMAP.TXN.AUDIT.DATE.TIME` | `FsBmapTxnRef_AuditDateTime` | String |  |  |
