# PPT.COMPANY — Table Schema

> Source: `INSERTS/I_F.PPT.COMPANY` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCO.CompanyID` | `PptCompany_Companyid` |  |  |  |
| 2 | `PPCO.CompanyDescription` | `PptCompany_Companydescription` |  |  |  |
| 3 | `PPCO.CompanyCode` | `PptCompany_Companycode` |  |  |  |
| 4 | `PPCO.StatusSODCOB` | `PptCompany_Statussodcob` |  |  |  |
| 5 | `PPCO.CurrentBusinessDate` | `PptCompany_Currentbusinessdate` |  |  |  |
| 6 | `PPCO.LastWorkingDay` | `PptCompany_Lastworkingday` |  |  |  |
| 7 | `PPCO.NextWorkingDay` | `PptCompany_Nextworkingday` |  |  |  |
| 8 | `PPCO.OffsetTime` | `PptCompany_Offsettime` |  |  |  |
| 9 | `PPCO.DateTimeStartedSOD` | `PptCompany_Datetimestartedsod` |  |  |  |
| 10 | `PPCO.DateTimeEndedSOD` | `PptCompany_Datetimeendedsod` |  |  |  |
| 11 | `PPCO.DateTimeStartedCOB` | `PptCompany_Datetimestartedcob` |  |  |  |
| 12 | `PPCO.DateTimeEndedCOB` | `PptCompany_Datetimeendedcob` |  |  |  |
| 13 | `PPCO.EnterpriseDescription` | `PptCompany_Enterprisedescription` |  |  |  |
| 14 | `PPCO.EnterpriseID` | `PptCompany_Enterpriseid` |  |  |  |
| 15 | `PPCO.RACCompany` | `PptCompany_Raccompany` |  |  |  |
| 16 | `PPCO.RSCCompany` | `PptCompany_Rsccompany` |  |  |  |
| 17 | `PPCO.EntryUserID` | `PptCompany_Entryuserid` |  |  |  |
| 18 | `PPCO.EntryDateTime` | `PptCompany_Entrydatetime` |  |  |  |
| 19 | `PPCO.ApproverUserID` | `PptCompany_Approveruserid` |  |  |  |
| 20 | `PPCO.ApprovedDateTime` | `PptCompany_Approveddatetime` |  |  |  |
