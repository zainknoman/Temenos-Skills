# FS.GA.TCN.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.TCN.EXCEPTION` in `FS_FundMaster.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.TCN.EXCEPTION.FUND.ID` | `FsGaTcnException_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.TCN.EXCEPTION.GTI.CODE` | `FsGaTcnException_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 3 | `FS.GA.TCN.EXCEPTION.ACCRUALS.METHOD` | `FsGaTcnException_AccrualsMethod` | TField |  | Accrual Method Multifonds DB Column is ACCRUAL_METHOD. |
| 4 | `FS.GA.TCN.EXCEPTION.RESERVED10` | `FsGaTcnException_Reserved10` | TField |  |  |
| 5 | `FS.GA.TCN.EXCEPTION.RESERVED9` | `FsGaTcnException_Reserved9` | TField |  |  |
| 6 | `FS.GA.TCN.EXCEPTION.RESERVED8` | `FsGaTcnException_Reserved8` | TField |  |  |
| 7 | `FS.GA.TCN.EXCEPTION.RESERVED7` | `FsGaTcnException_Reserved7` | TField |  |  |
| 8 | `FS.GA.TCN.EXCEPTION.RESERVED6` | `FsGaTcnException_Reserved6` | TField |  |  |
| 9 | `FS.GA.TCN.EXCEPTION.RESERVED5` | `FsGaTcnException_Reserved5` | TField |  |  |
| 10 | `FS.GA.TCN.EXCEPTION.RESERVED4` | `FsGaTcnException_Reserved4` | TField |  |  |
| 11 | `FS.GA.TCN.EXCEPTION.RESERVED3` | `FsGaTcnException_Reserved3` | TField |  |  |
| 12 | `FS.GA.TCN.EXCEPTION.RESERVED2` | `FsGaTcnException_Reserved2` | TField |  |  |
| 13 | `FS.GA.TCN.EXCEPTION.RESERVED1` | `FsGaTcnException_Reserved1` | TField |  |  |
| 14 | `FS.GA.TCN.EXCEPTION.RECORD.STATUS` | `FsGaTcnException_RecordStatus` | String |  |  |
| 15 | `FS.GA.TCN.EXCEPTION.CURR.NO` | `FsGaTcnException_CurrNo` | String |  |  |
| 16 | `FS.GA.TCN.EXCEPTION.INPUTTER` | `FsGaTcnException_Inputter` |  |  |  |
| 17 | `FS.GA.TCN.EXCEPTION.DATE.TIME` | `FsGaTcnException_DateTime` |  |  |  |
| 18 | `FS.GA.TCN.EXCEPTION.AUTHORISER` | `FsGaTcnException_Authoriser` | String |  |  |
| 19 | `FS.GA.TCN.EXCEPTION.CO.CODE` | `FsGaTcnException_CoCode` | String |  |  |
| 20 | `FS.GA.TCN.EXCEPTION.DEPT.CODE` | `FsGaTcnException_DeptCode` | String |  |  |
| 21 | `FS.GA.TCN.EXCEPTION.AUDITOR.CODE` | `FsGaTcnException_AuditorCode` | String |  |  |
| 22 | `FS.GA.TCN.EXCEPTION.AUDIT.DATE.TIME` | `FsGaTcnException_AuditDateTime` | String |  |  |
