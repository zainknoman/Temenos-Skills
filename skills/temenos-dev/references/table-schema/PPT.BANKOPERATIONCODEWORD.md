# PPT.BANKOPERATIONCODEWORD — Table Schema

> Source: `INSERTS/I_F.PPT.BANKOPERATIONCODEWORD` in `PP_SwiftOutService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPBCW.BankOperationCode` | `PptBankoperationcodeword_Bankoperationcode` | TField | Yes | Holds the Bank Operation Code. Validation Rules: Mandatory field. 4 alphanumeric character. |
| 2 | `PPBCW.SequenceNumber` | `PptBankoperationcodeword_Sequencenumber` | TField | Yes | As a Posting Set can have multiple posting lines, Sequence Number is used to order the posting lines within the Posting Set. Validation Rules: Mandatory field. 7 alphanumeric characters. |
| 3 | `PPBCW.CodeWord` | `PptBankoperationcodeword_Codeword` | TField | Yes | The codeword received in the payment instruction. Validation Rules: Mandatory field. 8 alphanumeric characters. |
| 4 | `PPBCW.RACBankOperationCodeWord` | `PptBankoperationcodeword_Racbankoperationcodeword` | TField |  |  |
| 5 | `PPBCW.RSCBankOperationCodeWord` | `PptBankoperationcodeword_Rscbankoperationcodeword` | TField |  |  |
| 6 | `PPBCW.EntryUserID` | `PptBankoperationcodeword_Entryuserid` | TField |  |  |
| 7 | `PPBCW.EntryDateTime` | `PptBankoperationcodeword_Entrydatetime` | TField |  |  |
| 8 | `PPBCW.ApproverUserID` | `PptBankoperationcodeword_Approveruserid` | TField |  |  |
| 9 | `PPBCW.ApprovedDateTime` | `PptBankoperationcodeword_Approveddatetime` | TField |  |  |
