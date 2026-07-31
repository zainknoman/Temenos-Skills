# FS.GA.FUND.CODES.EQUIVALENCES — Table Schema

> Source: `INSERTS/I_F.FS.GA.FUND.CODES.EQUIVALENCES` in `FS_Equivalence.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.FUND.CODES.EQUIVALENCES.PARENT.REF.ID` | `FsGaFundCodesEquivalences_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.FUND.CODES.EQUIVALENCES.ORA.ROWID` | `FsGaFundCodesEquivalences_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.FUND.CODES.EQUIVALENCES.MULTIFONDS.FUND` | `FsGaFundCodesEquivalences_MultifondsFund` | TField |  | Multifonds Fund Multifonds DB Column is PTF_MULTIFONDS. |
| 4 | `FS.GA.FUND.CODES.EQUIVALENCES.SOURCE.SYSTEM.FUND` | `FsGaFundCodesEquivalences_SourceSystemFund` | TField |  | Source System Fund Multifonds DB Column is PTF_REPRISE. |
| 5 | `FS.GA.FUND.CODES.EQUIVALENCES.INTERFACE.AUTO.ACCOUNTING` | `FsGaFundCodesEquivalences_InterfaceAutoAccounting` | TField |  | Auto accounting of interfaced data Multifonds DB Column is TRT_INTERFACE. |
| 6 | `FS.GA.FUND.CODES.EQUIVALENCES.LOAD.TRANSACTIONS` | `FsGaFundCodesEquivalences_LoadTransactions` | TField |  | Indicates whether transactions through interface can be loaded or not Multifonds DB Column is LOAD_TRS. |
| 7 | `FS.GA.FUND.CODES.EQUIVALENCES.RETEN.DURATION.OF.ACCTG.STS` | `FsGaFundCodesEquivalences_RetenDurationOfAcctgSts` | TField |  | Retention duration of accounting status for the loaded transactions Multifonds DB Column is NBJ_PRG_ACCOUNTED. |
| 8 | `FS.GA.FUND.CODES.EQUIVALENCES.RETEN.DURATION.OF.REJ.STS` | `FsGaFundCodesEquivalences_RetenDurationOfRejSts` | TField |  | Retention duration of rejection status for the loaded transactions Multifonds DB Column is NBJ_PRG_REJECTED. |
| 9 | `FS.GA.FUND.CODES.EQUIVALENCES.RETEN.DURATION.OF.NOT.PROC.STS` | `FsGaFundCodesEquivalences_RetenDurationOfNotProcSts` | TField |  | Retention duration of not processed status for the loaded transactions Multifonds DB Column is NBJ_PRG_NO_PROCESSED. |
| 10 | `FS.GA.FUND.CODES.EQUIVALENCES.DAYS.SUBTR.FROM.ACCTG.DATE` | `FsGaFundCodesEquivalences_DaysSubtrFromAcctgDate` | TField |  | Enter a number of days to be subtracted from the accounting date Multifonds DB Column is NBJ_SUB_DCTA. |
| 11 | `FS.GA.FUND.CODES.EQUIVALENCES.DAYS.ADD.TO.ACCOUNTING.DATE` | `FsGaFundCodesEquivalences_DaysAddToAccountingDate` | TField |  | Enter a number of days to be Added to the accounting date Multifonds DB Column is NBJ_ADD_DVAL. |
| 12 | `FS.GA.FUND.CODES.EQUIVALENCES.DESCRIPTION` | `FsGaFundCodesEquivalences_Description` | TField |  | Description of transaction. Multifonds DB Column is XLIBELLE. |
| 13 | `FS.GA.FUND.CODES.EQUIVALENCES.MAXIMUM.PERCENTAGE` | `FsGaFundCodesEquivalences_MaximumPercentage` | TField |  | Maximum Percentage Multifonds DB Column is PCT_MAX. |
| 14 | `FS.GA.FUND.CODES.EQUIVALENCES.FEES.FOR.FUND` | `FsGaFundCodesEquivalences_FeesForFund` | TField |  | Fees For Fund Multifonds DB Column is COMM_FONDS. |
| 15 | `FS.GA.FUND.CODES.EQUIVALENCES.INTERFACE.START.TIME` | `FsGaFundCodesEquivalences_InterfaceStartTime` | TField |  | Interface Start Time Multifonds DB Column is HEURE_MAX. |
| 16 | `FS.GA.FUND.CODES.EQUIVALENCES.AUTO.ACCOUNTING` | `FsGaFundCodesEquivalences_AutoAccounting` | TField |  | Auto Accounting Multifonds DB Column is AUTO_ACCOUNTING. |
| 17 | `FS.GA.FUND.CODES.EQUIVALENCES.RESERVED10` | `FsGaFundCodesEquivalences_Reserved10` | TField |  |  |
| 18 | `FS.GA.FUND.CODES.EQUIVALENCES.RESERVED9` | `FsGaFundCodesEquivalences_Reserved9` | TField |  |  |
| 19 | `FS.GA.FUND.CODES.EQUIVALENCES.RESERVED8` | `FsGaFundCodesEquivalences_Reserved8` | TField |  |  |
| 20 | `FS.GA.FUND.CODES.EQUIVALENCES.RESERVED7` | `FsGaFundCodesEquivalences_Reserved7` | TField |  |  |
| 21 | `FS.GA.FUND.CODES.EQUIVALENCES.RESERVED6` | `FsGaFundCodesEquivalences_Reserved6` | TField |  |  |
| 22 | `FS.GA.FUND.CODES.EQUIVALENCES.RESERVED5` | `FsGaFundCodesEquivalences_Reserved5` | TField |  |  |
| 23 | `FS.GA.FUND.CODES.EQUIVALENCES.RESERVED4` | `FsGaFundCodesEquivalences_Reserved4` | TField |  |  |
| 24 | `FS.GA.FUND.CODES.EQUIVALENCES.RESERVED3` | `FsGaFundCodesEquivalences_Reserved3` | TField |  |  |
| 25 | `FS.GA.FUND.CODES.EQUIVALENCES.RESERVED2` | `FsGaFundCodesEquivalences_Reserved2` | TField |  |  |
| 26 | `FS.GA.FUND.CODES.EQUIVALENCES.RESERVED1` | `FsGaFundCodesEquivalences_Reserved1` | TField |  |  |
| 27 | `FS.GA.FUND.CODES.EQUIVALENCES.LOCAL.REF` | `FsGaFundCodesEquivalences_LocalRef` |  |  |  |
| 28 | `FS.GA.FUND.CODES.EQUIVALENCES.OVERRIDE` | `FsGaFundCodesEquivalences_Override` |  |  |  |
| 29 | `FS.GA.FUND.CODES.EQUIVALENCES.RECORD.STATUS` | `FsGaFundCodesEquivalences_RecordStatus` | String |  |  |
| 30 | `FS.GA.FUND.CODES.EQUIVALENCES.CURR.NO` | `FsGaFundCodesEquivalences_CurrNo` | String |  |  |
| 31 | `FS.GA.FUND.CODES.EQUIVALENCES.INPUTTER` | `FsGaFundCodesEquivalences_Inputter` |  |  |  |
| 32 | `FS.GA.FUND.CODES.EQUIVALENCES.DATE.TIME` | `FsGaFundCodesEquivalences_DateTime` |  |  |  |
| 33 | `FS.GA.FUND.CODES.EQUIVALENCES.AUTHORISER` | `FsGaFundCodesEquivalences_Authoriser` | String |  |  |
| 34 | `FS.GA.FUND.CODES.EQUIVALENCES.CO.CODE` | `FsGaFundCodesEquivalences_CoCode` | String |  |  |
| 35 | `FS.GA.FUND.CODES.EQUIVALENCES.DEPT.CODE` | `FsGaFundCodesEquivalences_DeptCode` | String |  |  |
| 36 | `FS.GA.FUND.CODES.EQUIVALENCES.AUDITOR.CODE` | `FsGaFundCodesEquivalences_AuditorCode` | String |  |  |
| 37 | `FS.GA.FUND.CODES.EQUIVALENCES.AUDIT.DATE.TIME` | `FsGaFundCodesEquivalences_AuditDateTime` | String |  |  |
