# AC.FUNDS.DIVERSION.PARAM — Table Schema

> Source: `INSERTS/I_F.AC.FUNDS.DIVERSION.PARAM` in `AC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AC.FDP.DEF.FUNDS.DIVERSION` | `AcFundsDiversionParam_DefFundsDiversion` | TField |  | Field to decide Default Funds Diversion setup for Accounts. Validation rules: Option Field - YES/NO. YES will be set by default. YES - Funds Diversion will be performed for the Original Transaction account and Entry posted against the Diversion account. NO - Funds Diversion will not be performed and the Entry will be posted against the Original Transaction Account |
| 2 | `AC.FDP.TRANSACTION.CODE` | `AcFundsDiversionParam_TransactionCode` |  |  |  |
| 3 | `AC.FDP.ALLOW.MEMO.ENTRY.DIVERSION` | `AcFundsDiversionParam_AllowMemoEntryDiversion` | TField | No | Decides if system should allow diversion of memo entry to parent account incase if parent account's company is different than transaction company and if INTERCO.PARAMETER is not defined. Validation rules: Optional field. Valid values are: YES/NO/NULL. YES - Even if INTERCO.PARAMETER is not defined, funds can be diverted if memo account parent belongs to different company than transaction company. NO/NULL - If INTERCO.PARAMETER is not defined, then funds cannot be diverted if memo parent account belongs to different company than transaction company. This field has to be set at SYSTEM level. |
| 4 | `AC.FDP.SYSTEM.ID` | `AcFundsDiversionParam_SystemId` |  |  |  |
| 5 | `AC.FDP.SYS.ID.SIGN` | `AcFundsDiversionParam_SysIdSign` |  |  |  |
| 6 | `AC.FDP.SYS.TXN.CODE` | `AcFundsDiversionParam_SysTxnCode` |  |  |  |
| 7 | `AC.FDP.SYS.TXN.CODE.SIGN` | `AcFundsDiversionParam_SysTxnCodeSign` |  |  |  |
| 8 | `AC.FDP.LOCAL.REF` | `AcFundsDiversionParam_LocalRef` |  |  |  |
| 9 | `AC.FDP.OVERRIDE` | `AcFundsDiversionParam_Override` |  |  |  |
| 10 | `AC.FDP.RECORD.STATUS` | `AcFundsDiversionParam_RecordStatus` | String |  |  |
| 11 | `AC.FDP.CURR.NO` | `AcFundsDiversionParam_CurrNo` | String |  |  |
| 12 | `AC.FDP.INPUTTER` | `AcFundsDiversionParam_Inputter` |  |  |  |
| 13 | `AC.FDP.DATE.TIME` | `AcFundsDiversionParam_DateTime` |  |  |  |
| 14 | `AC.FDP.AUTHORISER` | `AcFundsDiversionParam_Authoriser` | String |  |  |
| 15 | `AC.FDP.CO.CODE` | `AcFundsDiversionParam_CoCode` | String |  |  |
| 16 | `AC.FDP.DEPT.CODE` | `AcFundsDiversionParam_DeptCode` | String |  |  |
| 17 | `AC.FDP.AUDITOR.CODE` | `AcFundsDiversionParam_AuditorCode` | String |  |  |
| 18 | `AC.FDP.AUDIT.DATE.TIME` | `AcFundsDiversionParam_AuditDateTime` | String |  |  |
