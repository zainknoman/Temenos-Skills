# PPT.CLEARINGRETURNCODE — Table Schema

> Source: `INSERTS/I_F.PPT.CLEARINGRETURNCODE` in `PP_DirectDebitChequeService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPCGR.CompanyID` | `PptClearingreturncode_Companyid` |  |  |  |
| 2 | `PPCGR.ClearingID` | `PptClearingreturncode_Clearingid` |  |  |  |
| 3 | `PPCGR.ClearingCurrency` | `PptClearingreturncode_Clearingcurrency` |  |  |  |
| 4 | `PPCGR.ClearingNatureCode` | `PptClearingreturncode_Clearingnaturecode` |  |  |  |
| 5 | `PPCGR.ClearingReturnCode` | `PptClearingreturncode_Clearingreturncode` |  |  |  |
| 6 | `PPCGR.StartDateClearingReturnCode` | `PptClearingreturncode_Startdateclearingreturncode` |  |  |  |
| 7 | `PPCGR.MessagePaymentType` | `PptClearingreturncode_Messagepaymenttype` |  |  |  |
| 8 | `PPCGR.ReturnCodeDescription` | `PptClearingreturncode_Returncodedescription` |  |  |  |
| 9 | `PPCGR.EndDateClearingReturnCode` | `PptClearingreturncode_Enddateclearingreturncode` |  |  |  |
| 10 | `PPCGR.RACClearingReturnCode` | `PptClearingreturncode_Racclearingreturncode` |  |  |  |
| 11 | `PPCGR.RSCClearingReturnCode` | `PptClearingreturncode_Rscclearingreturncode` |  |  |  |
| 12 | `PPCGR.EntryUserID` | `PptClearingreturncode_Entryuserid` |  |  |  |
| 13 | `PPCGR.EntryDateTime` | `PptClearingreturncode_Entrydatetime` |  |  |  |
| 14 | `PPCGR.ApproverUserID` | `PptClearingreturncode_Approveruserid` |  |  |  |
| 15 | `PPCGR.ApprovedDateTime` | `PptClearingreturncode_Approveddatetime` |  |  |  |
| 16 | `PPCGR.RouteToException` | `PptClearingreturncode_Routetoexception` |  |  |  |
| 17 | `PPCGR.TransactionType` | `PptClearingreturncode_Transactiontype` |  |  |  |
| 18 | `PPCGR.ReturnCodeLevel` | `PptClearingreturncode_Returncodelevel` |  |  |  |
