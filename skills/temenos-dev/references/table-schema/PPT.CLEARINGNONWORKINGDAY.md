# PPT.CLEARINGNONWORKINGDAY — Table Schema

> Source: `INSERTS/I_F.PPT.CLEARINGNONWORKINGDAY` in `PP_StaticDataGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCGH.CompanyID` | `PptClearingnonworkingday_Companyid` |  |  |  |
| 2 | `PPCGH.CountryCode` | `PptClearingnonworkingday_Countrycode` |  |  |  |
| 3 | `PPCGH.Region` | `PptClearingnonworkingday_Region` |  |  |  |
| 4 | `PPCGH.DayDate` | `PptClearingnonworkingday_Daydate` |  |  |  |
| 5 | `PPCGH.ChannelName` | `PptClearingnonworkingday_Channelname` |  |  |  |
| 6 | `PPCGH.RACClearingNonWorkingDay` | `PptClearingnonworkingday_Racclearingnonworkingday` |  |  |  |
| 7 | `PPCGH.RSCClearingNonWorkingDay` | `PptClearingnonworkingday_Rscclearingnonworkingday` |  |  |  |
| 8 | `PPCGH.EntryUserID` | `PptClearingnonworkingday_Entryuserid` |  |  |  |
| 9 | `PPCGH.EntryDateTime` | `PptClearingnonworkingday_Entrydatetime` |  |  |  |
| 10 | `PPCGH.ApproverUserID` | `PptClearingnonworkingday_Approveruserid` |  |  |  |
| 11 | `PPCGH.ApprovedDateTime` | `PptClearingnonworkingday_Approveddatetime` |  |  |  |
