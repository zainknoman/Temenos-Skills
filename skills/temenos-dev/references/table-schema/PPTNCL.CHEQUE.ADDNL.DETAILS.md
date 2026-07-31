# PPTNCL.CHEQUE.ADDNL.DETAILS — Table Schema

> Source: `INSERTS/I_F.PPTNCL.CHEQUE.ADDNL.DETAILS` in `PPTNCL_ChequeClearing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPTNCL.CQ.RecordID` | `PptnclChequeAddnlDetails_Recordid` | TField |  |  |
| 2 | `PPTNCL.CQ.ReceivedDate` | `PptnclChequeAddnlDetails_Receiveddate` | TField |  |  |
| 3 | `PPTNCL.CQ.FTNumber` | `PptnclChequeAddnlDetails_Ftnumber` | TField |  |  |
| 4 | `PPTNCL.CQ.PayerAccount` | `PptnclChequeAddnlDetails_Payeraccount` | TField |  |  |
| 5 | `PPTNCL.CQ.PayerAccountCurrency` | `PptnclChequeAddnlDetails_Payeraccountcurrency` | TField |  |  |
| 6 | `PPTNCL.CQ.ChequeAmount` | `PptnclChequeAddnlDetails_Chequeamount` | TField |  |  |
| 7 | `PPTNCL.CQ.ACLKReference1` | `PptnclChequeAddnlDetails_Aclkreference1` | TField |  |  |
| 8 | `PPTNCL.CQ.BlockedAmount1` | `PptnclChequeAddnlDetails_Blockedamount1` | TField |  |  |
| 9 | `PPTNCL.CQ.Is31Received` | `PptnclChequeAddnlDetails_Is31received` | TField |  |  |
| 10 | `PPTNCL.CQ.ACLKReference2` | `PptnclChequeAddnlDetails_Aclkreference2` | TField |  |  |
