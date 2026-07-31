# FS.GA.VALUATION.EXCEPTION — Table Schema

> Source: `INSERTS/I_F.FS.GA.VALUATION.EXCEPTION` in `FS_FundMaster.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GA.VALUATION.EXCEPTION.FUND.ID` | `FsGaValuationException_FundId` | TField |  | Internal fund identifier Multifonds DB Column is NPTF. |
| 2 | `FS.GA.VALUATION.EXCEPTION.GTI.CODE` | `FsGaValuationException_GtiCode` | TField |  | Corresponds to GTI (asset type) Multifonds DB Column is CGTI. |
| 3 | `FS.GA.VALUATION.EXCEPTION.VALUATION.METHOD` | `FsGaValuationException_ValuationMethod` | TField |  | This field enable user to define a default valuation method by Fund / GTI / Process Multifonds DB Column is FCYELD. |
| 4 | `FS.GA.VALUATION.EXCEPTION.RESERVED10` | `FsGaValuationException_Reserved10` | TField |  |  |
| 5 | `FS.GA.VALUATION.EXCEPTION.RESERVED9` | `FsGaValuationException_Reserved9` | TField |  |  |
| 6 | `FS.GA.VALUATION.EXCEPTION.RESERVED8` | `FsGaValuationException_Reserved8` | TField |  |  |
| 7 | `FS.GA.VALUATION.EXCEPTION.RESERVED7` | `FsGaValuationException_Reserved7` | TField |  |  |
| 8 | `FS.GA.VALUATION.EXCEPTION.RESERVED6` | `FsGaValuationException_Reserved6` | TField |  |  |
| 9 | `FS.GA.VALUATION.EXCEPTION.RESERVED5` | `FsGaValuationException_Reserved5` | TField |  |  |
| 10 | `FS.GA.VALUATION.EXCEPTION.RESERVED4` | `FsGaValuationException_Reserved4` | TField |  |  |
| 11 | `FS.GA.VALUATION.EXCEPTION.RESERVED3` | `FsGaValuationException_Reserved3` | TField |  |  |
| 12 | `FS.GA.VALUATION.EXCEPTION.RESERVED2` | `FsGaValuationException_Reserved2` | TField |  |  |
| 13 | `FS.GA.VALUATION.EXCEPTION.RESERVED1` | `FsGaValuationException_Reserved1` | TField |  |  |
| 14 | `FS.GA.VALUATION.EXCEPTION.RECORD.STATUS` | `FsGaValuationException_RecordStatus` | String |  |  |
| 15 | `FS.GA.VALUATION.EXCEPTION.CURR.NO` | `FsGaValuationException_CurrNo` | String |  |  |
| 16 | `FS.GA.VALUATION.EXCEPTION.INPUTTER` | `FsGaValuationException_Inputter` |  |  |  |
| 17 | `FS.GA.VALUATION.EXCEPTION.DATE.TIME` | `FsGaValuationException_DateTime` |  |  |  |
| 18 | `FS.GA.VALUATION.EXCEPTION.AUTHORISER` | `FsGaValuationException_Authoriser` | String |  |  |
| 19 | `FS.GA.VALUATION.EXCEPTION.CO.CODE` | `FsGaValuationException_CoCode` | String |  |  |
| 20 | `FS.GA.VALUATION.EXCEPTION.DEPT.CODE` | `FsGaValuationException_DeptCode` | String |  |  |
| 21 | `FS.GA.VALUATION.EXCEPTION.AUDITOR.CODE` | `FsGaValuationException_AuditorCode` | String |  |  |
| 22 | `FS.GA.VALUATION.EXCEPTION.AUDIT.DATE.TIME` | `FsGaValuationException_AuditDateTime` | String |  |  |
