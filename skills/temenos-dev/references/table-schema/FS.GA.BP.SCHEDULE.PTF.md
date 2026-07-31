# FS.GA.BP.SCHEDULE.PTF — Table Schema

> Source: `INSERTS/I_F.FS.GA.BP.SCHEDULE.PTF` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BP.SCHEDULE.PTF.FUND.ID` | `FsGaBpSchedulePtf_Fund` |  |  |  |
| 2 | `BP.SCHEDULE.PTF.INTERNAL.SECURITY.ID` | `FsGaBpSchedulePtf_SecurityId` |  |  |  |
| 3 | `BP.SCHEDULE.PTF.CORRESPONDENT` | `FsGaBpSchedulePtf_Correspondent` | TField |  | Correspondent Multifonds DB Column is NCORRESP. |
| 4 | `BP.SCHEDULE.PTF.AP.SERVICE.CODE` | `FsGaBpSchedulePtf_ApServiceCode` | TField |  | Ap Service code Multifonds DB Column is CSERV. |
| 5 | `BP.SCHEDULE.PTF.CONTRACT` | `FsGaBpSchedulePtf_Contract` | TField |  | Contract Multifonds DB Column is NCONTRAT. |
| 6 | `BP.SCHEDULE.PTF.MANAGER.CODE` | `FsGaBpSchedulePtf_Manager` |  |  |  |
| 7 | `BP.SCHEDULE.PTF.START.DATE` | `FsGaBpSchedulePtf_StartDate` | TField |  | Start date Multifonds DB Column is DDEBUT. |
| 8 | `BP.SCHEDULE.PTF.END.DATE` | `FsGaBpSchedulePtf_EndDate` | TField |  | End date Multifonds DB Column is DFIN. |
| 9 | `BP.SCHEDULE.PTF.BP.AMOUNT` | `FsGaBpSchedulePtf_BpAmount` | TField |  | BP Amount Multifonds DB Column is MNT_BP. |
| 10 | `BP.SCHEDULE.PTF.DWH.EXPORT` | `FsGaBpSchedulePtf_DwhExport` | TField |  | Dwh Export Multifonds DB Column is DWH_EXPORT. |
| 11 | `BP.SCHEDULE.PTF.FLAG.IOP` | `FsGaBpSchedulePtf_FlagIop` | TField |  | Flag IOP Multifonds DB Column is FLG_IOP. |
| 12 | `BP.SCHEDULE.PTF.CURRENCY.BPS` | `FsGaBpSchedulePtf_CurrencyBps` | TField |  | Currency BPS Multifonds DB Column is CMON_BP. |
| 13 | `BP.SCHEDULE.PTF.RECORD.STATUS` | `FsGaBpSchedulePtf_RecordStatus` | String |  |  |
| 14 | `BP.SCHEDULE.PTF.CURR.NO` | `FsGaBpSchedulePtf_CurrNo` | String |  |  |
| 15 | `BP.SCHEDULE.PTF.INPUTTER` | `FsGaBpSchedulePtf_Inputter` |  |  |  |
| 16 | `BP.SCHEDULE.PTF.DATE.TIME` | `FsGaBpSchedulePtf_DateTime` |  |  |  |
| 17 | `BP.SCHEDULE.PTF.AUTHORISER` | `FsGaBpSchedulePtf_Authoriser` | String |  |  |
| 18 | `BP.SCHEDULE.PTF.CO.CODE` | `FsGaBpSchedulePtf_CoCode` | String |  |  |
| 19 | `BP.SCHEDULE.PTF.DEPT.CODE` | `FsGaBpSchedulePtf_DeptCode` | String |  |  |
| 20 | `BP.SCHEDULE.PTF.AUDITOR.CODE` | `FsGaBpSchedulePtf_AuditorCode` | String |  |  |
| 21 | `BP.SCHEDULE.PTF.AUDIT.DATE.TIME` | `FsGaBpSchedulePtf_AuditDateTime` | String |  |  |
