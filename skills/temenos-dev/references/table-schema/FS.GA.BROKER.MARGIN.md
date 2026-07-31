# FS.GA.BROKER.MARGIN — Table Schema

> Source: `INSERTS/I_F.FS.GA.BROKER.MARGIN` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.BROKER.MARGIN.PARENT.REF.ID` | `FsGaBrokerMargin_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.BROKER.MARGIN.ORA.ROWID` | `FsGaBrokerMargin_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.BROKER.MARGIN.CORRESPONDENT` | `FsGaBrokerMargin_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 4 | `FS.GA.BROKER.MARGIN.LOCAL.CURRENCY` | `FsGaBrokerMargin_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 5 | `FS.GA.BROKER.MARGIN.GTI.CODE` | `FsGaBrokerMargin_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 6 | `FS.GA.BROKER.MARGIN.INITIAL.MARGIN` | `FsGaBrokerMargin_InitialMargin` | TField |  | MultiFonds is able to compute the initial margin to be deposited with each opening or closing transaction. Enter the initial margin to be deposited per contract. Multifonds DB Column is MARG_INIT. |
| 7 | `FS.GA.BROKER.MARGIN.RESERVED10` | `FsGaBrokerMargin_Reserved10` | TField |  |  |
| 8 | `FS.GA.BROKER.MARGIN.RESERVED9` | `FsGaBrokerMargin_Reserved9` | TField |  |  |
| 9 | `FS.GA.BROKER.MARGIN.RESERVED8` | `FsGaBrokerMargin_Reserved8` | TField |  |  |
| 10 | `FS.GA.BROKER.MARGIN.RESERVED7` | `FsGaBrokerMargin_Reserved7` | TField |  |  |
| 11 | `FS.GA.BROKER.MARGIN.RESERVED6` | `FsGaBrokerMargin_Reserved6` | TField |  |  |
| 12 | `FS.GA.BROKER.MARGIN.RESERVED5` | `FsGaBrokerMargin_Reserved5` | TField |  |  |
| 13 | `FS.GA.BROKER.MARGIN.RESERVED4` | `FsGaBrokerMargin_Reserved4` | TField |  |  |
| 14 | `FS.GA.BROKER.MARGIN.RESERVED3` | `FsGaBrokerMargin_Reserved3` | TField |  |  |
| 15 | `FS.GA.BROKER.MARGIN.RESERVED2` | `FsGaBrokerMargin_Reserved2` | TField |  |  |
| 16 | `FS.GA.BROKER.MARGIN.RESERVED1` | `FsGaBrokerMargin_Reserved1` | TField |  |  |
| 17 | `FS.GA.BROKER.MARGIN.LOCAL.REF` | `FsGaBrokerMargin_LocalRef` |  |  |  |
| 18 | `FS.GA.BROKER.MARGIN.OVERRIDE` | `FsGaBrokerMargin_Override` |  |  |  |
| 19 | `FS.GA.BROKER.MARGIN.RECORD.STATUS` | `FsGaBrokerMargin_RecordStatus` | String |  |  |
| 20 | `FS.GA.BROKER.MARGIN.CURR.NO` | `FsGaBrokerMargin_CurrNo` | String |  |  |
| 21 | `FS.GA.BROKER.MARGIN.INPUTTER` | `FsGaBrokerMargin_Inputter` |  |  |  |
| 22 | `FS.GA.BROKER.MARGIN.DATE.TIME` | `FsGaBrokerMargin_DateTime` |  |  |  |
| 23 | `FS.GA.BROKER.MARGIN.AUTHORISER` | `FsGaBrokerMargin_Authoriser` | String |  |  |
| 24 | `FS.GA.BROKER.MARGIN.CO.CODE` | `FsGaBrokerMargin_CoCode` | String |  |  |
| 25 | `FS.GA.BROKER.MARGIN.DEPT.CODE` | `FsGaBrokerMargin_DeptCode` | String |  |  |
| 26 | `FS.GA.BROKER.MARGIN.AUDITOR.CODE` | `FsGaBrokerMargin_AuditorCode` | String |  |  |
| 27 | `FS.GA.BROKER.MARGIN.AUDIT.DATE.TIME` | `FsGaBrokerMargin_AuditDateTime` | String |  |  |
