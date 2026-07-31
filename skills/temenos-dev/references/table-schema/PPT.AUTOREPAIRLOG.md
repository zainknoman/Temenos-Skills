# PPT.AUTOREPAIRLOG — Table Schema

> Source: `INSERTS/I_F.PPT.AUTOREPAIRLOG` in `PP_AutomatedRepairToolService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPARL.FTNumber` | `PptAutorepairlog_Ftnumber` | TField |  | Unique payment reference generated for each payment by the payments hub. |
| 2 | `PPARL.CompanyID` | `PptAutorepairlog_Companyid` | TField |  | Indicates the company ID for which the record is created. Example : BNK,GB1 The value links to the field �CompanyID� in PPT.COMPANY |
| 3 | `PPARL.ProcessingDate` | `PptAutorepairlog_Processingdate` | TField |  | Date on which payment is processed. |
| 4 | `PPARL.PreviousPaymentData` | `PptAutorepairlog_Previouspaymentdata` | TField |  | Original Payment Data received by the payments hub before enrichment by Auto Repair tool |
| 5 | `PPARL.EnrichedPaymentData` | `PptAutorepairlog_Enrichedpaymentdata` | TField |  | Payment Data received after enrichment from Auto Repair tool |
