# CL.ITEM.WEIGHT — Table Schema

> Source: `INSERTS/I_F.CL.ITEM.WEIGHT` in `CL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CL.INWGT.OUTSTD.AMT.UPTO` | `ClItemWeight_OutstdAmtUpto` |  |  |  |
| 2 | `CL.INWGT.OTS.WEIGHT` | `ClItemWeight_OtsWeight` |  |  |  |
| 3 | `CL.INWGT.ODUE.AMT.UPTO` | `ClItemWeight_OdueAmtUpto` |  |  |  |
| 4 | `CL.INWGT.ODUE.WGT` | `ClItemWeight_OdueWgt` |  |  |  |
| 5 | `CL.INWGT.BLACK.LIST.WGT` | `ClItemWeight_BlackListWgt` | TField |  | Which weight to be given to items with black-list flag is �Y�. |
| 6 | `CL.INWGT.BPTP.UPTO.NO` | `ClItemWeight_BptpUptoNo` |  |  |  |
| 7 | `CL.INWGT.BPTP.WEIGHT` | `ClItemWeight_BptpWeight` |  |  |  |
| 8 | `CL.INWGT.PD.DAYS.UPTO` | `ClItemWeight_PdDaysUpto` |  |  |  |
| 9 | `CL.INWGT.PD.DAYS.WEIGHT` | `ClItemWeight_PdDaysWeight` |  |  |  |
| 10 | `CL.INWGT.DNO.ACT.UPTO` | `ClItemWeight_DnoActUpto` |  |  |  |
| 11 | `CL.INWGT.DNO.ACT.WGT` | `ClItemWeight_DnoActWgt` |  |  |  |
| 12 | `CL.INWGT.UL.LOAN.SECURED` | `ClItemWeight_UlLoanSecured` |  |  |  |
| 13 | `CL.INWGT.SECURITY.WGT` | `ClItemWeight_SecurityWgt` |  |  |  |
| 14 | `CL.INWGT.LAST.OUTCOME` | `ClItemWeight_LastOutcome` |  |  |  |
| 15 | `CL.INWGT.LAST.OCOME.WGT` | `ClItemWeight_LastOcomeWgt` |  |  |  |
| 16 | `CL.INWGT.LOCAL.REF` | `ClItemWeight_LocalRef` |  |  |  |
| 17 | `CL.INWGT.RESERVED.5` | `ClItemWeight_Reserved5` | TField |  |  |
| 18 | `CL.INWGT.RESERVED.4` | `ClItemWeight_Reserved4` | TField |  |  |
| 19 | `CL.INWGT.RESERVED.3` | `ClItemWeight_Reserved3` | TField |  |  |
| 20 | `CL.INWGT.RESERVED.2` | `ClItemWeight_Reserved2` | TField |  |  |
| 21 | `CL.INWGT.RESERVED.1` | `ClItemWeight_Reserved1` | TField |  |  |
| 22 | `CL.INWGT.RECORD.STATUS` | `ClItemWeight_RecordStatus` | String |  |  |
| 23 | `CL.INWGT.CURR.NO` | `ClItemWeight_CurrNo` | String |  |  |
| 24 | `CL.INWGT.INPUTTER` | `ClItemWeight_Inputter` |  |  |  |
| 25 | `CL.INWGT.DATE.TIME` | `ClItemWeight_DateTime` |  |  |  |
| 26 | `CL.INWGT.AUTHORISER` | `ClItemWeight_Authoriser` | String |  |  |
| 27 | `CL.INWGT.CO.CODE` | `ClItemWeight_CoCode` | String |  |  |
| 28 | `CL.INWGT.DEPT.CODE` | `ClItemWeight_DeptCode` | String |  |  |
| 29 | `CL.INWGT.AUDITOR.CODE` | `ClItemWeight_AuditorCode` | String |  |  |
| 30 | `CL.INWGT.AUDIT.DATE.TIME` | `ClItemWeight_AuditDateTime` | String |  |  |
