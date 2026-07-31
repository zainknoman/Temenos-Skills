# AFRBOP.ERROR.LOG — Table Schema

> Source: `INSERTS/I_F.AFRBOP.ERROR.LOG` in `AFRBOP_BalanceOfPayment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AFRBOP.ERROR.STMT.ENTRY.ID` | `AfrbopErrorLog_StmtEntryId` |  |  |  |
| 2 | `AFRBOP.ERROR.CUSTOMER.ID` | `AfrbopErrorLog_CustomerId` | TField |  | This field contains the Customer Id |
| 3 | `AFRBOP.ERROR.TRANSACTION.REFERENCE` | `AfrbopErrorLog_TransactionReference` | TField |  |  |
| 4 | `AFRBOP.ERROR.ERROR.DETAILS` | `AfrbopErrorLog_ErrorDetails` |  |  |  |
| 5 | `AFRBOP.ERROR.FILE.EXTRACTION.DATE` | `AfrbopErrorLog_FileExtractionDate` | TField |  | Date on which the files are generated |
| 6 | `AFRBOP.ERROR.LOCAL.REF` | `AfrbopErrorLog_LocalRef` |  |  |  |
| 7 | `AFRBOP.ERROR.RESERVED.5` | `AfrbopErrorLog_Reserved5` | TField |  | This field is reserved for future use |
| 8 | `AFRBOP.ERROR.RESERVED.4` | `AfrbopErrorLog_Reserved4` | TField |  | This field is reserved for future use |
| 9 | `AFRBOP.ERROR.RESERVED.3` | `AfrbopErrorLog_Reserved3` | TField |  | This field is reserved for future use |
| 10 | `AFRBOP.ERROR.RESERVED.2` | `AfrbopErrorLog_Reserved2` | TField |  | This field is reserved for future use |
| 11 | `AFRBOP.ERROR.RESERVED.1` | `AfrbopErrorLog_Reserved1` | TField |  | This field is reserved for future use |
