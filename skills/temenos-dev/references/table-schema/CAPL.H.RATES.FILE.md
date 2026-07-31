# CAPL.H.RATES.FILE — Table Schema

> Source: `INSERTS/I_F.CAPL.H.RATES.FILE` in `CATELS_TelephoneBanking.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.RTE.FLE.DESCRIPTION` | `CaplHRatesFile_Description` |  |  |  |
| 2 | `CAPL.RTE.FLE.REF.FILE` | `CaplHRatesFile_RefFile` |  |  |  |
| 3 | `CAPL.RTE.FLE.REF.FILE.ID` | `CaplHRatesFile_RefFileId` |  |  |  |
| 4 | `CAPL.RTE.FLE.CNCL.TXN.TYPE` | `CaplHRatesFile_CnclTxnType` |  |  |  |
| 5 | `CAPL.RTE.FLE.LOC.REF` | `CaplHRatesFile_LocRef` |  |  |  |
| 6 | `CAPL.RTE.FLE.OVERRIDE` | `CaplHRatesFile_Override` |  |  |  |
| 7 | `CAPL.RTE.FLE.RECORD.STATUS` | `CaplHRatesFile_RecordStatus` |  |  |  |
| 8 | `CAPL.RTE.FLE.CURR.NO` | `CaplHRatesFile_CurrNo` |  |  |  |
| 9 | `CAPL.RTE.FLE.INPUTTER` | `CaplHRatesFile_Inputter` |  |  |  |
| 10 | `CAPL.RTE.FLE.DATE.TIME` | `CaplHRatesFile_DateTime` |  |  |  |
| 11 | `CAPL.RTE.FLE.AUTHORISER` | `CaplHRatesFile_Authoriser` |  |  |  |
| 12 | `CAPL.RTE.FLE.CO.CODE` | `CaplHRatesFile_CoCode` |  |  |  |
| 13 | `CAPL.RTE.FLE.DEPT.CODE` | `CaplHRatesFile_DeptCode` |  |  |  |
| 14 | `CAPL.RTE.FLE.AUDITOR.CODE` | `CaplHRatesFile_AuditorCode` |  |  |  |
| 15 | `CAPL.RTE.FLE.AUDIT.DATE.TIME` | `CaplHRatesFile_AuditDateTime` |  |  |  |
