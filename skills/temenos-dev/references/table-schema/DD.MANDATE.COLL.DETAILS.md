# DD.MANDATE.COLL.DETAILS — Table Schema

> Source: `INSERTS/I_F.DD.MANDATE.COLL.DETAILS` in `DD_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DDCD.CUSTOMER` | `DdMandateCollDetails_Customer` | TField |  | This field holds the Customer of DD.DDI |
| 2 | `DDCD.ACCOUNT` | `DdMandateCollDetails_Account` | TField |  | This field holds the Account of DD.DDI |
| 3 | `DDCD.MANDATE.ID` | `DdMandateCollDetails_MandateId` | TField |  | This field holds the ID of DD.DDI |
| 4 | `DDCD.TRANS.REFERENCE` | `DdMandateCollDetails_TransReference` | TField |  | Represents the transaction reference |
| 5 | `DDCD.PAYMENT.SCHEME` | `DdMandateCollDetails_PaymentScheme` | TField |  | Mandate Scheme of DD.DDI |
| 6 | `DDCD.MANDATE.REFERENCE` | `DdMandateCollDetails_MandateReference` | TField |  | Clear Sys Ref of DD.DDI |
| 7 | `DDCD.CREDITOR.ID` | `DdMandateCollDetails_CreditorId` | TField |  | Creditor ID of DD.DDI |
| 8 | `DDCD.CREDITOR.ACCOUNT` | `DdMandateCollDetails_CreditorAccount` | TField |  | Creditor Account of DD.DDI |
| 9 | `DDCD.REMIT.INFO` | `DdMandateCollDetails_RemitInfo` | TField |  | Represents the Remittance information for the SDD |
| 10 | `DDCD.STR.CRED.REF` | `DdMandateCollDetails_StrCredRef` | TField |  | The Payment Reference part of the Structured Remittance Information included in the SDD Collection |
| 11 | `DDCD.STR.CRED.REF.CODE` | `DdMandateCollDetails_StrCredRefCode` | TField |  | The Code indicating the type of the reference supplied as part of the Structured Remittance Information |
| 12 | `DDCD.STR.CRED.REF.ISSR` | `DdMandateCollDetails_StrCredRefIssr` | TField |  | The Issuer of the Structured Creditor Reference |
| 13 | `DDCD.EXECUTION.DATE` | `DdMandateCollDetails_ExecutionDate` | TField |  | Represents the Execution date for the SDD transaction sent |
| 14 | `DDCD.RESERVED.5` | `DdMandateCollDetails_Reserved5` | TField |  | This field is reserved for future use. |
| 15 | `DDCD.RESERVED.4` | `DdMandateCollDetails_Reserved4` | TField |  | This field is reserved for future use. |
| 16 | `DDCD.RESERVED.3` | `DdMandateCollDetails_Reserved3` | TField |  | This field is reserved for future use. |
| 17 | `DDCD.RESERVED.2` | `DdMandateCollDetails_Reserved2` | TField |  | This field is reserved for future use. |
| 18 | `DDCD.RESERVED.1` | `DdMandateCollDetails_Reserved1` | TField |  | This field is reserved for future use. |
