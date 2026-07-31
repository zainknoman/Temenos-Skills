# FS.GA.BT.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.BT.EXCEPTION` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BT.EXCEP.FUND.ID` | `FsGaBtException_Fund` |  |  |  |
| 2 | `BT.EXCEP.TRANSACTION.CODE` | `FsGaBtException_OperationCode` |  |  |  |
| 3 | `BT.EXCEP.DEFAULT.OPERAION.CODE.FLAG` | `FsGaBtException_DefaultOperaionCodeFlag` | TField |  | Default Operaion Code Flag Multifonds DB Column is FLG_BT. |
| 4 | `BT.EXCEP.DWH.EXPORT.FLAG` | `FsGaBtException_DwhExportFlag` | TField |  | DWH Export flag Multifonds DB Column is DWH_EXPORT. |
| 5 | `BT.EXCEP.RECORD.STATUS` | `FsGaBtException_RecordStatus` | String |  |  |
| 6 | `BT.EXCEP.CURR.NO` | `FsGaBtException_CurrNo` | String |  |  |
| 7 | `BT.EXCEP.INPUTTER` | `FsGaBtException_Inputter` |  |  |  |
| 8 | `BT.EXCEP.DATE.TIME` | `FsGaBtException_DateTime` |  |  |  |
| 9 | `BT.EXCEP.AUTHORISER` | `FsGaBtException_Authoriser` | String |  |  |
| 10 | `BT.EXCEP.CO.CODE` | `FsGaBtException_CoCode` | String |  |  |
| 11 | `BT.EXCEP.DEPT.CODE` | `FsGaBtException_DeptCode` | String |  |  |
| 12 | `BT.EXCEP.AUDITOR.CODE` | `FsGaBtException_AuditorCode` | String |  |  |
| 13 | `BT.EXCEP.AUDIT.DATE.TIME` | `FsGaBtException_AuditDateTime` | String |  |  |
