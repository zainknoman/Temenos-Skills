# PP.OUT.CC.TRANSACTION — Table Schema

> Source: `INSERTS/I_F.PP.OUT.CC.TRANSACTION` in `PP_OutwardMappingFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPOCC.CompanyId` | `PpOutCcTransaction_Companyid` | TField |  |  |
| 2 | `PPOCC.FTNumber` | `PpOutCcTransaction_Ftnumber` | TField |  |  |
| 3 | `PPOCC.IncomingMessageType` | `PpOutCcTransaction_Incomingmessagetype` | TField |  |  |
| 4 | `PPOCC.DebitValueDate` | `PpOutCcTransaction_Debitvaluedate` | TField |  |  |
| 5 | `PPOCC.SendersReferenceIncoming` | `PpOutCcTransaction_Sendersreferenceincoming` | TField |  |  |
| 6 | `PPOCC.ChequeNumber` | `PpOutCcTransaction_Chequenumber` | TField |  |  |
| 7 | `PPOCC.ChequeDate` | `PpOutCcTransaction_Chequedate` | TField |  |  |
| 8 | `PPOCC.CreditPartyRole` | `PpOutCcTransaction_Creditpartyrole` |  |  |  |
| 9 | `PPOCC.CreditPartyName` | `PpOutCcTransaction_Creditpartyname` |  |  |  |
| 10 | `PPOCC.CreditPartyNationalId` | `PpOutCcTransaction_Creditpartynationalid` |  |  |  |
| 11 | `PPOCC.CreditPartyIdentifierCode` | `PpOutCcTransaction_Creditpartyidentifiercode` |  |  |  |
| 12 | `PPOCC.CreditPartyAccountLine` | `PpOutCcTransaction_Creditpartyaccountline` |  |  |  |
| 13 | `PPOCC.DebitPartyRole` | `PpOutCcTransaction_Debitpartyrole` |  |  |  |
| 14 | `PPOCC.DebitPartyName` | `PpOutCcTransaction_Debitpartyname` |  |  |  |
| 15 | `PPOCC.DebitPartyNationalId` | `PpOutCcTransaction_Debitpartynationalid` |  |  |  |
| 16 | `PPOCC.DebitPartyIdentifierCode` | `PpOutCcTransaction_Debitpartyidentifiercode` |  |  |  |
| 17 | `PPOCC.DebitPartyAccountLine` | `PpOutCcTransaction_Debitpartyaccountline` |  |  |  |
| 18 | `PPOCC.AdditionalInformationCode` | `PpOutCcTransaction_Additionalinformationcode` |  |  |  |
| 19 | `PPOCC.AdditionalInfTypeLineSeq` | `PpOutCcTransaction_Additionalinftypelineseq` |  |  |  |
| 20 | `PPOCC.AdditionalInfLine` | `PpOutCcTransaction_Additionalinfline` |  |  |  |
| 21 | `PPOCC.TransformedHdr` | `PpOutCcTransaction_Transformedhdr` | TField |  |  |
| 22 | `PPOCC.TransformedTxn` | `PpOutCcTransaction_Transformedtxn` | TField |  |  |
| 23 | `PPOCC.FileReference` | `PpOutCcTransaction_Filereference` | TField |  |  |
| 24 | `PPOCC.BulkReference` | `PpOutCcTransaction_Bulkreference` | TField |  |  |
