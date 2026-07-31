# PPL.FILTERINGPAYMENTS — Table Schema

> Source: `INSERTS/I_F.PPL.FILTERINGPAYMENTS` in `PP_FilteringService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPFPY.CompanyID` | `PplFilteringpayments_Companyid` |  |  |  |
| 2 | `PPFPY.Ranking` | `PplFilteringpayments_Ranking` |  |  |  |
| 3 | `PPFPY.FilteringProduct` | `PplFilteringpayments_Filteringproduct` |  |  |  |
| 4 | `PPFPY.OutputChannel` | `PplFilteringpayments_Outputchannel` |  |  |  |
| 5 | `PPFPY.OutgoingMessageType` | `PplFilteringpayments_Outgoingmessagetype` |  |  |  |
| 6 | `PPFPY.SkipFilterIndicator` | `PplFilteringpayments_Skipfilterindicator` |  |  |  |
| 7 | `PPFPY.StartDateFilteringPayments` | `PplFilteringpayments_Startdatefilteringpayments` |  |  |  |
| 8 | `PPFPY.EndDateFilteringPayments` | `PplFilteringpayments_Enddatefilteringpayments` |  |  |  |
| 9 | `PPFPY.RACFilteringPayments` | `PplFilteringpayments_Racfilteringpayments` |  |  |  |
| 10 | `PPFPY.RSCFilteringPayments` | `PplFilteringpayments_Rscfilteringpayments` |  |  |  |
| 11 | `PPFPY.EntryUserID` | `PplFilteringpayments_Entryuserid` |  |  |  |
| 12 | `PPFPY.EntryDateTime` | `PplFilteringpayments_Entrydatetime` |  |  |  |
| 13 | `PPFPY.ApproverUserID` | `PplFilteringpayments_Approveruserid` |  |  |  |
| 14 | `PPFPY.ApprovedDateTime` | `PplFilteringpayments_Approveddatetime` |  |  |  |
