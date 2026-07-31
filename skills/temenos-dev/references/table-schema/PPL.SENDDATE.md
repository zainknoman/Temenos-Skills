# PPL.SENDDATE — Table Schema

> Source: `INSERTS/I_F.PPL.SENDDATE` in `PP_DateDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPSDT.CompanyID` | `PplSenddate_Companyid` |  |  |  |
| 2 | `PPSDT.StartDateSendDate` | `PplSenddate_Startdatesenddate` |  |  |  |
| 3 | `PPSDT.Channel` | `PplSenddate_Channel` |  |  |  |
| 4 | `PPSDT.Source` | `PplSenddate_Source` |  |  |  |
| 5 | `PPSDT.CurrencyGroup` | `PplSenddate_Currencygroup` |  |  |  |
| 6 | `PPSDT.WarehouseFlag` | `PplSenddate_Warehouseflag` |  |  |  |
| 7 | `PPSDT.Priority` | `PplSenddate_Priority` |  |  |  |
| 8 | `PPSDT.CTRBTRIndicator` | `PplSenddate_Ctrbtrindicator` |  |  |  |
| 9 | `PPSDT.Ranking` | `PplSenddate_Ranking` |  |  |  |
| 10 | `PPSDT.SendDateBase` | `PplSenddate_Senddatebase` |  |  |  |
| 11 | `PPSDT.SendDateOffset` | `PplSenddate_Senddateoffset` |  |  |  |
| 12 | `PPSDT.CoverIndicator` | `PplSenddate_Coverindicator` |  |  |  |
| 13 | `PPSDT.EndDateSendDate` | `PplSenddate_Enddatesenddate` |  |  |  |
| 14 | `PPSDT.RACSendDate` | `PplSenddate_Racsenddate` |  |  |  |
| 15 | `PPSDT.RSCSendDate` | `PplSenddate_Rscsenddate` |  |  |  |
| 16 | `PPSDT.EntryUserID` | `PplSenddate_Entryuserid` |  |  |  |
| 17 | `PPSDT.EntryDateTime` | `PplSenddate_Entrydatetime` |  |  |  |
| 18 | `PPSDT.ApproverUserID` | `PplSenddate_Approveruserid` |  |  |  |
| 19 | `PPSDT.ApprovedDateTime` | `PplSenddate_Approveddatetime` |  |  |  |
