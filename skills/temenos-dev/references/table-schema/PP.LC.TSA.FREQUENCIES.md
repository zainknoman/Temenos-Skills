# PP.LC.TSA.FREQUENCIES — Table Schema

> Source: `INSERTS/I_F.PP.LC.TSA.FREQUENCIES` in `PP_LocalClearingService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PP.LCF.CompanyID` | `PpLcTsaFrequencies_Companyid` | TField | Yes | Indicates the company ID for which the record is created. Example : BNK,GB1 Validation Rules: Mandatory field. 3 alphanumeric characters. The value links to the field �CompanyID� in PPT.COMPANY |
| 2 | `PP.LCF.LCTSAFrequenciesID` | `PpLcTsaFrequencies_Lctsafrequenciesid` | TField |  | Holds unique ID which refers to the LCTSA Frequencies in the payments hub. Validation Rules: 65 alphanumeric characters. |
| 3 | `PP.LCF.ClearingID` | `PpLcTsaFrequencies_Clearingid` | TField | Yes | Holds ID which refers to the clearing in the payments hub. Validation Rules: Mandatory field. 10 alphanumeric characters. The value links to field 'ClearingID' in PPT.CLEARING |
| 4 | `PP.LCF.TSAServiceID` | `PpLcTsaFrequencies_Tsaserviceid` | TField | Yes | This is the ID of the TSA service from T24 TSA.SERVICE table. Validation Rules: Mandatory field. 50 alphanumeric characters. |
| 5 | `PP.LCF.Frequency1` | `PpLcTsaFrequencies_Frequency1` | TField |  | Frequency 1. Validation Rules: 5 characters. |
| 6 | `PP.LCF.Frequency2` | `PpLcTsaFrequencies_Frequency2` | TField |  | Frequency 2. Validation Rules: 30 characters. |
| 7 | `PP.LCF.Frequency3` | `PpLcTsaFrequencies_Frequency3` | TField |  | Frequency 3. Validation Rules: 30 characters. |
| 8 | `PP.LCF.Frequency4` | `PpLcTsaFrequencies_Frequency4` | TField |  | Frequency 4. Validation Rules: 30 characters. |
| 9 | `PP.LCF.Frequency5` | `PpLcTsaFrequencies_Frequency5` | TField |  | Frequency 5. Validation Rules: 30 characters. |
| 10 | `PP.LCF.RAC` | `PpLcTsaFrequencies_Rac` | TField |  |  |
| 11 | `PP.LCF.RSC` | `PpLcTsaFrequencies_Rsc` | TField |  |  |
| 12 | `PP.LCF.OldID` | `PpLcTsaFrequencies_Oldid` | TField |  |  |
| 13 | `PP.LCF.CurrentID` | `PpLcTsaFrequencies_Currentid` | TField |  |  |
| 14 | `PP.LCF.Action` | `PpLcTsaFrequencies_Action` | TField |  |  |
| 15 | `PP.LCF.OVERRIDE` | `PpLcTsaFrequencies_Override` |  |  |  |
| 16 | `PP.LCF.RECORD.STATUS` | `PpLcTsaFrequencies_RecordStatus` | String |  |  |
| 17 | `PP.LCF.CURR.NO` | `PpLcTsaFrequencies_CurrNo` | String |  |  |
| 18 | `PP.LCF.INPUTTER` | `PpLcTsaFrequencies_Inputter` |  |  |  |
| 19 | `PP.LCF.DATE.TIME` | `PpLcTsaFrequencies_DateTime` |  |  |  |
| 20 | `PP.LCF.AUTHORISER` | `PpLcTsaFrequencies_Authoriser` | String |  |  |
| 21 | `PP.LCF.CO.CODE` | `PpLcTsaFrequencies_CoCode` | String |  |  |
| 22 | `PP.LCF.DEPT.CODE` | `PpLcTsaFrequencies_DeptCode` | String |  |  |
| 23 | `PP.LCF.AUDITOR.CODE` | `PpLcTsaFrequencies_AuditorCode` | String |  |  |
| 24 | `PP.LCF.AUDIT.DATE.TIME` | `PpLcTsaFrequencies_AuditDateTime` | String |  |  |
