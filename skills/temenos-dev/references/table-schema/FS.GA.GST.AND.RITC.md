# FS.GA.GST.AND.RITC — Table Schema

> Source: `INSERTS/I_F.FS.GA.GST.AND.RITC` in `FS_ChargesFees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.GST.AND.RITC.FUND.ID` | `FsGaGstAndRitc_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.GST.AND.RITC.GL.ACCOUNT` | `FsGaGstAndRitc_GlAccount` | TField |  | Cash Account Number Multifonds DB Column is NRUBR. |
| 3 | `FS.GA.GST.AND.RITC.GST.IN.PERCENTAGE` | `FsGaGstAndRitc_GstInPercentage` | TField |  | GST in percentage Multifonds DB Column is PCT_GST. |
| 4 | `FS.GA.GST.AND.RITC.RITC.IN.PERCENTAGE` | `FsGaGstAndRitc_RitcInPercentage` | TField |  | RITC in percentage Multifonds DB Column is PCT_RITC. |
| 5 | `FS.GA.GST.AND.RITC.FLAG.TO.REGROSS` | `FsGaGstAndRitc_FlagToRegross` | TField |  | Regross operation Multifonds DB Column is REGROSS. |
| 6 | `FS.GA.GST.AND.RITC.GST.SEPERATION` | `FsGaGstAndRitc_GstSeperation` | TField |  | GST and RITC separation Multifonds DB Column is GST_SEP. |
| 7 | `FS.GA.GST.AND.RITC.INTERNAL.SECURITY.ID` | `FsGaGstAndRitc_InternalSecurityId` | TField |  | Security identifier used in the transaction Multifonds DB Column is NOVAL. |
| 8 | `FS.GA.GST.AND.RITC.CORRESPONDENT` | `FsGaGstAndRitc_Correspondent` | TField |  | Correspondent bank where the cash proceeds from the transaction would be settled Multifonds DB Column is NCORRESP. |
| 9 | `FS.GA.GST.AND.RITC.RESERVED10` | `FsGaGstAndRitc_Reserved10` | TField |  |  |
| 10 | `FS.GA.GST.AND.RITC.RESERVED9` | `FsGaGstAndRitc_Reserved9` | TField |  |  |
| 11 | `FS.GA.GST.AND.RITC.RESERVED8` | `FsGaGstAndRitc_Reserved8` | TField |  |  |
| 12 | `FS.GA.GST.AND.RITC.RESERVED7` | `FsGaGstAndRitc_Reserved7` | TField |  |  |
| 13 | `FS.GA.GST.AND.RITC.RESERVED6` | `FsGaGstAndRitc_Reserved6` | TField |  |  |
| 14 | `FS.GA.GST.AND.RITC.RESERVED5` | `FsGaGstAndRitc_Reserved5` | TField |  |  |
| 15 | `FS.GA.GST.AND.RITC.RESERVED4` | `FsGaGstAndRitc_Reserved4` | TField |  |  |
| 16 | `FS.GA.GST.AND.RITC.RESERVED3` | `FsGaGstAndRitc_Reserved3` | TField |  |  |
| 17 | `FS.GA.GST.AND.RITC.RESERVED2` | `FsGaGstAndRitc_Reserved2` | TField |  |  |
| 18 | `FS.GA.GST.AND.RITC.RESERVED1` | `FsGaGstAndRitc_Reserved1` | TField |  |  |
| 19 | `FS.GA.GST.AND.RITC.RECORD.STATUS` | `FsGaGstAndRitc_RecordStatus` | String |  |  |
| 20 | `FS.GA.GST.AND.RITC.CURR.NO` | `FsGaGstAndRitc_CurrNo` | String |  |  |
| 21 | `FS.GA.GST.AND.RITC.INPUTTER` | `FsGaGstAndRitc_Inputter` |  |  |  |
| 22 | `FS.GA.GST.AND.RITC.DATE.TIME` | `FsGaGstAndRitc_DateTime` |  |  |  |
| 23 | `FS.GA.GST.AND.RITC.AUTHORISER` | `FsGaGstAndRitc_Authoriser` | String |  |  |
| 24 | `FS.GA.GST.AND.RITC.CO.CODE` | `FsGaGstAndRitc_CoCode` | String |  |  |
| 25 | `FS.GA.GST.AND.RITC.DEPT.CODE` | `FsGaGstAndRitc_DeptCode` | String |  |  |
| 26 | `FS.GA.GST.AND.RITC.AUDITOR.CODE` | `FsGaGstAndRitc_AuditorCode` | String |  |  |
| 27 | `FS.GA.GST.AND.RITC.AUDIT.DATE.TIME` | `FsGaGstAndRitc_AuditDateTime` | String |  |  |
