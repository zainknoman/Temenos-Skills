# PP.CUSTOMERRESPONSESECTION — Table Schema

> Source: `INSERTS/I_F.PP.CUSTOMERRESPONSESECTION` in `PP_CustomerPaymentStatusReport.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCRS.FileReference` | `PpCustomerresponsesection_Filereference` | TField |  |  |
| 2 | `PPCRS.FTNumber` | `PpCustomerresponsesection_Ftnumber` | TField |  |  |
| 3 | `PPCRS.ResponseCodeLevel` | `PpCustomerresponsesection_Responsecodelevel` | TField |  |  |
| 4 | `PPCRS.AcknowledgementType` | `PpCustomerresponsesection_Acknowledgementtype` | TField |  |  |
| 5 | `PPCRS.OutputChannel` | `PpCustomerresponsesection_Outputchannel` | TField |  |  |
| 6 | `PPCRS.StatusReportFlag` | `PpCustomerresponsesection_Statusreportflag` | TField |  |  |
| 7 | `PPCRS.ResponseCode` | `PpCustomerresponsesection_Responsecode` | TField |  |  |
| 8 | `PPCRS.ErrorText` | `PpCustomerresponsesection_Errortext` | TField |  |  |
