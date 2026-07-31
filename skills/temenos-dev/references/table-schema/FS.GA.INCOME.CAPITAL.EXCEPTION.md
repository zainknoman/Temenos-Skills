# FS.GA.INCOME.CAPITAL.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.INCOME.CAPITAL.EXCEPTION` in `FS_FundMaster.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.INCOME.CAPITAL.EXCEPTION.FUND.ID` | `FsGaIncomeCapitalException_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.INCOME.CAPITAL.EXCEPTION.GTI.CODE` | `FsGaIncomeCapitalException_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 3 | `FS.GA.INCOME.CAPITAL.EXCEPTION.TRANSACTION.TYPE.VAL` | `FsGaIncomeCapitalException_TransactionTypeVal` | TField |  | Transaction Type Val Multifonds DB Column is COPER_VAL. |
| 4 | `FS.GA.INCOME.CAPITAL.EXCEPTION.INCOME.AND.CAPITAL.EXCEPTION` | `FsGaIncomeCapitalException_IncomeAndCapitalException` | TField |  | Income And Capital Exception Flag Multifonds DB Column is FLG_INC_CAP. |
| 5 | `FS.GA.INCOME.CAPITAL.EXCEPTION.DATE.OF.CREATION` | `FsGaIncomeCapitalException_DateOfCreation` | TField |  | Date of creation of a particular object in the system (Static Data / Transactions / Process) Multifonds DB Column is DCREATE. |
| 6 | `FS.GA.INCOME.CAPITAL.EXCEPTION.UPDATED.DATE` | `FsGaIncomeCapitalException_UpdatedDate` | TField |  | Updated Date Multifonds DB Column is DUPDATE. |
| 7 | `FS.GA.INCOME.CAPITAL.EXCEPTION.RESERVED10` | `FsGaIncomeCapitalException_Reserved10` | TField |  |  |
| 8 | `FS.GA.INCOME.CAPITAL.EXCEPTION.RESERVED9` | `FsGaIncomeCapitalException_Reserved9` | TField |  |  |
| 9 | `FS.GA.INCOME.CAPITAL.EXCEPTION.RESERVED8` | `FsGaIncomeCapitalException_Reserved8` | TField |  |  |
| 10 | `FS.GA.INCOME.CAPITAL.EXCEPTION.RESERVED7` | `FsGaIncomeCapitalException_Reserved7` | TField |  |  |
| 11 | `FS.GA.INCOME.CAPITAL.EXCEPTION.RESERVED6` | `FsGaIncomeCapitalException_Reserved6` | TField |  |  |
| 12 | `FS.GA.INCOME.CAPITAL.EXCEPTION.RESERVED5` | `FsGaIncomeCapitalException_Reserved5` | TField |  |  |
| 13 | `FS.GA.INCOME.CAPITAL.EXCEPTION.RESERVED4` | `FsGaIncomeCapitalException_Reserved4` | TField |  |  |
| 14 | `FS.GA.INCOME.CAPITAL.EXCEPTION.RESERVED3` | `FsGaIncomeCapitalException_Reserved3` | TField |  |  |
| 15 | `FS.GA.INCOME.CAPITAL.EXCEPTION.RESERVED2` | `FsGaIncomeCapitalException_Reserved2` | TField |  |  |
| 16 | `FS.GA.INCOME.CAPITAL.EXCEPTION.RESERVED1` | `FsGaIncomeCapitalException_Reserved1` | TField |  |  |
| 17 | `FS.GA.INCOME.CAPITAL.EXCEPTION.RECORD.STATUS` | `FsGaIncomeCapitalException_RecordStatus` | String |  |  |
| 18 | `FS.GA.INCOME.CAPITAL.EXCEPTION.CURR.NO` | `FsGaIncomeCapitalException_CurrNo` | String |  |  |
| 19 | `FS.GA.INCOME.CAPITAL.EXCEPTION.INPUTTER` | `FsGaIncomeCapitalException_Inputter` |  |  |  |
| 20 | `FS.GA.INCOME.CAPITAL.EXCEPTION.DATE.TIME` | `FsGaIncomeCapitalException_DateTime` |  |  |  |
| 21 | `FS.GA.INCOME.CAPITAL.EXCEPTION.AUTHORISER` | `FsGaIncomeCapitalException_Authoriser` | String |  |  |
| 22 | `FS.GA.INCOME.CAPITAL.EXCEPTION.CO.CODE` | `FsGaIncomeCapitalException_CoCode` | String |  |  |
| 23 | `FS.GA.INCOME.CAPITAL.EXCEPTION.DEPT.CODE` | `FsGaIncomeCapitalException_DeptCode` | String |  |  |
| 24 | `FS.GA.INCOME.CAPITAL.EXCEPTION.AUDITOR.CODE` | `FsGaIncomeCapitalException_AuditorCode` | String |  |  |
| 25 | `FS.GA.INCOME.CAPITAL.EXCEPTION.AUDIT.DATE.TIME` | `FsGaIncomeCapitalException_AuditDateTime` | String |  |  |
