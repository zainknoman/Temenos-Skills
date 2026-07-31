# FS.GA.VALUATION.METHOD.ACC.EXCEP — Table Schema

> Source: `INSERTS/I_F.FS.GA.VALUATION.METHOD.ACC.EXCEP` in `FS_GlobalAccounting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.PARENT.REF.ID` | `FsGaValuationMethodAccExcep_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.ORA.ROWID` | `FsGaValuationMethodAccExcep_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.FUND.ID` | `FsGaValuationMethodAccExcep_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 4 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.GL.ACCOUNT` | `FsGaValuationMethodAccExcep_GlAccount` | TField |  | GL Account number Multifonds DB Column is NRUBR. |
| 5 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.VALUATION.METHOD` | `FsGaValuationMethodAccExcep_ValuationMethod` | TField |  | This field enable user to define a default valuation method by Fund / GTI / Process Multifonds DB Column is FCYELD. |
| 6 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.VALUATION.METHOD.CLOSING` | `FsGaValuationMethodAccExcep_ValuationMethodClosing` | TField |  | Closing valuation method for asset class at fund level Multifonds DB Column is FCYELD_CLOSING. |
| 7 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.NUMBER.OF.DAYS.TO.SWITCH` | `FsGaValuationMethodAccExcep_NumberOfDaysToSwitch` | TField |  | Number of days to switch one valaution method to other. Multifonds DB Column is NB_SWITCH. |
| 8 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.RESERVED10` | `FsGaValuationMethodAccExcep_Reserved10` | TField |  |  |
| 9 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.RESERVED9` | `FsGaValuationMethodAccExcep_Reserved9` | TField |  |  |
| 10 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.RESERVED8` | `FsGaValuationMethodAccExcep_Reserved8` | TField |  |  |
| 11 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.RESERVED7` | `FsGaValuationMethodAccExcep_Reserved7` | TField |  |  |
| 12 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.RESERVED6` | `FsGaValuationMethodAccExcep_Reserved6` | TField |  |  |
| 13 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.RESERVED5` | `FsGaValuationMethodAccExcep_Reserved5` | TField |  |  |
| 14 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.RESERVED4` | `FsGaValuationMethodAccExcep_Reserved4` | TField |  |  |
| 15 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.RESERVED3` | `FsGaValuationMethodAccExcep_Reserved3` | TField |  |  |
| 16 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.RESERVED2` | `FsGaValuationMethodAccExcep_Reserved2` | TField |  |  |
| 17 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.RESERVED1` | `FsGaValuationMethodAccExcep_Reserved1` | TField |  |  |
| 18 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.LOCAL.REF` | `FsGaValuationMethodAccExcep_LocalRef` |  |  |  |
| 19 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.OVERRIDE` | `FsGaValuationMethodAccExcep_Override` |  |  |  |
| 20 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.RECORD.STATUS` | `FsGaValuationMethodAccExcep_RecordStatus` | String |  |  |
| 21 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.CURR.NO` | `FsGaValuationMethodAccExcep_CurrNo` | String |  |  |
| 22 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.INPUTTER` | `FsGaValuationMethodAccExcep_Inputter` |  |  |  |
| 23 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.DATE.TIME` | `FsGaValuationMethodAccExcep_DateTime` |  |  |  |
| 24 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.AUTHORISER` | `FsGaValuationMethodAccExcep_Authoriser` | String |  |  |
| 25 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.CO.CODE` | `FsGaValuationMethodAccExcep_CoCode` | String |  |  |
| 26 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.DEPT.CODE` | `FsGaValuationMethodAccExcep_DeptCode` | String |  |  |
| 27 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.AUDITOR.CODE` | `FsGaValuationMethodAccExcep_AuditorCode` | String |  |  |
| 28 | `FS.GA.VALUATION.METHOD.ACC.EXCEP.AUDIT.DATE.TIME` | `FsGaValuationMethodAccExcep_AuditDateTime` | String |  |  |
