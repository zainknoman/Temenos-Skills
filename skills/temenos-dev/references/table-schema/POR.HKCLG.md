# POR.HKCLG — Table Schema

> Source: `INSERTS/I_F.POR.HKCLG` in `PP_LocalClearingHKCLGService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PORHK.CompanyID` | `PorHkclg_Companyid` |  |  |  |
| 2 | `PORHK.FTNumber` | `PorHkclg_Ftnumber` |  |  |  |
| 3 | `PORHK.FileReference` | `PorHkclg_Filereference` |  |  |  |
| 4 | `PORHK.FileSenderReference` | `PorHkclg_Filesenderreference` |  |  |  |
| 5 | `PORHK.ClearingProcessingDate` | `PorHkclg_Clearingprocessingdate` |  |  |  |
| 6 | `PORHK.CurrencyCode` | `PorHkclg_Currencycode` |  |  |  |
| 7 | `PORHK.CDReferenceNumber` | `PorHkclg_Cdreferencenumber` |  |  |  |
| 8 | `PORHK.CDDraweeMemberClearingCode` | `PorHkclg_Cddraweememberclearingcode` |  |  |  |
| 9 | `PORHK.CDDraweeMemberBranchCode` | `PorHkclg_Cddraweememberbranchcode` |  |  |  |
| 10 | `PORHK.CDDrawerAccountNumber` | `PorHkclg_Cddraweraccountnumber` |  |  |  |
| 11 | `PORHK.CDTransactionCode` | `PorHkclg_Cdtransactioncode` |  |  |  |
| 12 | `PORHK.CDTransactionAmount` | `PorHkclg_Cdtransactionamount` |  |  |  |
| 13 | `PORHK.CDUniqueIdentifier` | `PorHkclg_Cduniqueidentifier` |  |  |  |
| 14 | `PORHK.CDCollectingMemberClearingCode` | `PorHkclg_Cdcollectingmemberclearingcode` |  |  |  |
| 15 | `PORHK.CDCollectingMemberBranchCode` | `PorHkclg_Cdcollectingmemberbranchcode` |  |  |  |
| 16 | `PORHK.CDHighValueIndicator` | `PorHkclg_Cdhighvalueindicator` |  |  |  |
| 17 | `PORHK.CDSpecialHandlingIndicator` | `PorHkclg_Cdspecialhandlingindicator` |  |  |  |
| 18 | `PORHK.CDNCBatchIndicator` | `PorHkclg_Cdncbatchindicator` |  |  |  |
| 19 | `PORHK.CDSplitTicketIndicator` | `PorHkclg_Cdsplitticketindicator` |  |  |  |
