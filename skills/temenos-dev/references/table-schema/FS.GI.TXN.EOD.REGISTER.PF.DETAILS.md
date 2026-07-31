# FS.GI.TXN.EOD.REGISTER.PF.DETAILS — Table Schema

> Source: `INSERTS/I_F.FS.GI.TXN.EOD.REGISTER.PF.DETAILS` in `FS_GlobalInvestorTransactions.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.FUND.ID` | `FsGiTxnEodRegisterPfDetails_FundId` | TField |  | Fund ID for which register PF is calculated. Multifonds DB Column is NPTF. |
| 2 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.SHARE.CLASS.CODE` | `FsGiTxnEodRegisterPfDetails_ShareClassCode` | TField |  | Share class for the selected TA fund. Multifonds DB Column is TPART. |
| 3 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.REGISTER.ID` | `FsGiTxnEodRegisterPfDetails_RegisterId` | TField |  | Register ID for which performance fee is calculated. Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.NAV.DATE` | `FsGiTxnEodRegisterPfDetails_NavDate` | TField |  | NAV date for which register level performance fee is calculated. Multifonds DB Column is NAVDATE. |
| 5 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.REGISTER.POSITION` | `FsGiTxnEodRegisterPfDetails_RegisterPosition` | TField |  | Quantity of shares held by the register. Multifonds DB Column is QUANTITY. |
| 6 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.AVERAGE.CRP` | `FsGiTxnEodRegisterPfDetails_AverageCrp` | TField |  | Average cumulative relative performance. Multifonds DB Column is AVG_CRP. |
| 7 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.POSITION.PF.ACCRUAL` | `FsGiTxnEodRegisterPfDetails_PositionPfAccrual` | TField |  | Position performance fee accrual on end of day. Multifonds DB Column is QTY_PF_ACCRUAL. |
| 8 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.NET.EQ.BALANCE` | `FsGiTxnEodRegisterPfDetails_NetEqBalance` | TField |  | Remaining equalisation credit/debit of the contract. Multifonds DB Column is NET_EQUAL_BALANCE. |
| 9 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.USABLE.NET.EQ.BALANCE` | `FsGiTxnEodRegisterPfDetails_UsableNetEqBalance` | TField |  | Equalization amount that can be used for redemption / crystallizations. Multifonds DB Column is USABLE_NET_EQUAL_BALANCE. |
| 10 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.NET.PERIOD.CRYSTALLIZED.PF` | `FsGiTxnEodRegisterPfDetails_NetPeriodCrystallizedPf` | TField |  | Net Period Crystallized performance fee. If there is no contract on the NAV date for register then the value of this field is zero. Multifonds DB Column is NET_PERIOD_CRYST. |
| 11 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.CUMMULATIVE.CRYT.PF.AMOUNT` | `FsGiTxnEodRegisterPfDetails_CummulativeCrytPfAmount` | TField |  | Cumulative crystallized performance fee on contract. Multifonds DB Column is CUMULATIVE_CRYST_PF. |
| 12 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.INVESTOR.PF.ACCRUAL` | `FsGiTxnEodRegisterPfDetails_InvestorPfAccrual` | TField |  | Client performance fee accrual on end of day. Multifonds DB Column is CLI_PF_ACCRUAL. |
| 13 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.STATUS` | `FsGiTxnEodRegisterPfDetails_Status` | TField |  | Status of performance fee calculated. Multifonds DB Column is STATUS. |
| 14 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.CALCULATED.DATE` | `FsGiTxnEodRegisterPfDetails_CalculatedDate` | TField |  | Calculated timestamp. Multifonds DB Column is DCALCULATED. |
| 15 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.CALCULATED.BY` | `FsGiTxnEodRegisterPfDetails_CalculatedBy` | TField |  | User who calculated. Multifonds DB Column is CALCULATED_BY. |
| 16 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.EXCEPTION.VALIDATED.DATE` | `FsGiTxnEodRegisterPfDetails_ExceptionValidatedDate` | TField |  | Exception validated date. Multifonds DB Column is DVALIDATED. |
| 17 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.VALIDATED.BY` | `FsGiTxnEodRegisterPfDetails_ValidatedBy` | TField |  | User who validated exception. Multifonds DB Column is VALIDATED_BY. |
| 18 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.RESERVED10` | `FsGiTxnEodRegisterPfDetails_Reserved10` | TField |  |  |
| 19 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.RESERVED9` | `FsGiTxnEodRegisterPfDetails_Reserved9` | TField |  |  |
| 20 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.RESERVED8` | `FsGiTxnEodRegisterPfDetails_Reserved8` | TField |  |  |
| 21 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.RESERVED7` | `FsGiTxnEodRegisterPfDetails_Reserved7` | TField |  |  |
| 22 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.RESERVED6` | `FsGiTxnEodRegisterPfDetails_Reserved6` | TField |  |  |
| 23 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.RESERVED5` | `FsGiTxnEodRegisterPfDetails_Reserved5` | TField |  |  |
| 24 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.RESERVED4` | `FsGiTxnEodRegisterPfDetails_Reserved4` | TField |  |  |
| 25 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.RESERVED3` | `FsGiTxnEodRegisterPfDetails_Reserved3` | TField |  |  |
| 26 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.RESERVED2` | `FsGiTxnEodRegisterPfDetails_Reserved2` | TField |  |  |
| 27 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.RESERVED1` | `FsGiTxnEodRegisterPfDetails_Reserved1` | TField |  |  |
| 28 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.LOCAL.REF` | `FsGiTxnEodRegisterPfDetails_LocalRef` |  |  |  |
| 29 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.OVERRIDE` | `FsGiTxnEodRegisterPfDetails_Override` |  |  |  |
| 30 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.RECORD.STATUS` | `FsGiTxnEodRegisterPfDetails_RecordStatus` | String |  |  |
| 31 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.CURR.NO` | `FsGiTxnEodRegisterPfDetails_CurrNo` | String |  |  |
| 32 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.INPUTTER` | `FsGiTxnEodRegisterPfDetails_Inputter` |  |  |  |
| 33 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.DATE.TIME` | `FsGiTxnEodRegisterPfDetails_DateTime` |  |  |  |
| 34 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.AUTHORISER` | `FsGiTxnEodRegisterPfDetails_Authoriser` | String |  |  |
| 35 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.CO.CODE` | `FsGiTxnEodRegisterPfDetails_CoCode` | String |  |  |
| 36 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.DEPT.CODE` | `FsGiTxnEodRegisterPfDetails_DeptCode` | String |  |  |
| 37 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.AUDITOR.CODE` | `FsGiTxnEodRegisterPfDetails_AuditorCode` | String |  |  |
| 38 | `FS.GI.TXN.EOD.REGISTER.PF.DETAILS.AUDIT.DATE.TIME` | `FsGiTxnEodRegisterPfDetails_AuditDateTime` | String |  |  |
