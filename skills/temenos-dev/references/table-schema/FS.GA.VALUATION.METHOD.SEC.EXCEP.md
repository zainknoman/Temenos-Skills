# FS.GA.VALUATION.METHOD.SEC.EXCEP — Table Schema

> Source: `INSERTS/I_F.FS.GA.VALUATION.METHOD.SEC.EXCEP` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.PARENT.REF.ID` | `FsGaValuationMethodSecExcep_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.ORA.ROWID` | `FsGaValuationMethodSecExcep_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.FUND.ID` | `FsGaValuationMethodSecExcep_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.GTI.CODE` | `FsGaValuationMethodSecExcep_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 5 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.VALUATION.METHOD` | `FsGaValuationMethodSecExcep_ValuationMethod` | TField |  | This field enable user to define a default valuation method by Fund / GTI / Process Multifonds DB Column is FCYELD. |
| 6 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.VALUATION.METHOD.CLOSING` | `FsGaValuationMethodSecExcep_ValuationMethodClosing` | TField |  | Closing valuation method for asset class at fund level Multifonds DB Column is FCYELD_CLOSING. |
| 7 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.NUMBER.OF.DAYS.TO.SWITCH` | `FsGaValuationMethodSecExcep_NumberOfDaysToSwitch` | TField |  | Number of days to switch one valaution method to other. Multifonds DB Column is NB_SWITCH. |
| 8 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.LOCAL.CURRENCY` | `FsGaValuationMethodSecExcep_LocalCurrency` | TField |  | Denotes the currency like EUR,USD etc Multifonds DB Column is CMON. |
| 9 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.VALUATION.METHOD.TO.SWITCH` | `FsGaValuationMethodSecExcep_ValuationMethodToSwitch` | TField |  | The specific valuation method (Code) to swith over when it reaches maturity of the instrument Multifonds DB Column is FCYELD_SWITCH. |
| 10 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.FOR.REIMBURSEMENT.PRIME` | `FsGaValuationMethodSecExcep_ForReimbursementPrime` | TField |  | The French Market for Bonds and Bond-assimilated instruments (Indexed Bonds, Convertible Bonds, ABS / MBS) and for TCN post comptA A s&quot; is to calculate the amortization on each transaction and NAV.&quot; Multifonds DB Column is FLG_REIMB_PRIME. |
| 11 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.TAIWAN.FUTURE.VARIATION.MARGIN` | `FsGaValuationMethodSecExcep_TaiwanFutureVariationMargin` | TField |  | This field is related to the functionality of Taiwan futures-Variation Margin. If the checkbox is ticked, V1 valuation method is subject to Taiwan futures. Multifonds DB Column is FLG_VM_ACC. |
| 12 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.RESERVED10` | `FsGaValuationMethodSecExcep_Reserved10` | TField |  |  |
| 13 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.RESERVED9` | `FsGaValuationMethodSecExcep_Reserved9` | TField |  |  |
| 14 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.RESERVED8` | `FsGaValuationMethodSecExcep_Reserved8` | TField |  |  |
| 15 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.RESERVED7` | `FsGaValuationMethodSecExcep_Reserved7` | TField |  |  |
| 16 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.RESERVED6` | `FsGaValuationMethodSecExcep_Reserved6` | TField |  |  |
| 17 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.RESERVED5` | `FsGaValuationMethodSecExcep_Reserved5` | TField |  |  |
| 18 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.RESERVED4` | `FsGaValuationMethodSecExcep_Reserved4` | TField |  |  |
| 19 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.RESERVED3` | `FsGaValuationMethodSecExcep_Reserved3` | TField |  |  |
| 20 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.RESERVED2` | `FsGaValuationMethodSecExcep_Reserved2` | TField |  |  |
| 21 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.RESERVED1` | `FsGaValuationMethodSecExcep_Reserved1` | TField |  |  |
| 22 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.LOCAL.REF` | `FsGaValuationMethodSecExcep_LocalRef` |  |  |  |
| 23 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.OVERRIDE` | `FsGaValuationMethodSecExcep_Override` |  |  |  |
| 24 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.RECORD.STATUS` | `FsGaValuationMethodSecExcep_RecordStatus` | String |  |  |
| 25 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.CURR.NO` | `FsGaValuationMethodSecExcep_CurrNo` | String |  |  |
| 26 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.INPUTTER` | `FsGaValuationMethodSecExcep_Inputter` |  |  |  |
| 27 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.DATE.TIME` | `FsGaValuationMethodSecExcep_DateTime` |  |  |  |
| 28 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.AUTHORISER` | `FsGaValuationMethodSecExcep_Authoriser` | String |  |  |
| 29 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.CO.CODE` | `FsGaValuationMethodSecExcep_CoCode` | String |  |  |
| 30 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.DEPT.CODE` | `FsGaValuationMethodSecExcep_DeptCode` | String |  |  |
| 31 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.AUDITOR.CODE` | `FsGaValuationMethodSecExcep_AuditorCode` | String |  |  |
| 32 | `FS.GA.VALUATION.METHOD.SEC.EXCEP.AUDIT.DATE.TIME` | `FsGaValuationMethodSecExcep_AuditDateTime` | String |  |  |
