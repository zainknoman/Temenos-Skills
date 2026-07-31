# CAPL.UB.PAYMENT.XREF — Table Schema

> Source: `INSERTS/I_F.CAPL.UB.PAYMENT.XREF` in `CAEBPS_EbillsInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `UB.PMT.XREF.STATUS` | `CaplUbPaymentXref_Status` |  |  |  |
| 2 | `UB.PMT.XREF.UB.PAY.REF` | `CaplUbPaymentXref_UbPayRef` |  |  |  |
| 3 | `UB.PMT.XREF.FAIL.REASON` | `CaplUbPaymentXref_FailReason` |  |  |  |
| 4 | `UB.PMT.XREF.FAIL.CNT` | `CaplUbPaymentXref_FailCnt` | TField |  | Field is used to store the Number of times the bill payment is failed.Treated as fail count.Eg. 3 |
| 5 | `UB.PMT.XREF.NEXT.RETRY` | `CaplUbPaymentXref_NextRetry` | TField |  | Field is used to store the date on which the next try for the bill payment will be executed.Validation- Updated based on NO.OF.RETRY field in in CAPL.UB.RECURR.PAYMENT Table |
| 6 | `UB.PMT.XREF.START.DATE` | `CaplUbPaymentXref_StartDate` | TField |  | Field to store the start date from which the bill payment is failed.Mapped from the Second part of ID.Used for the Enquiry Report selection |
| 7 | `UB.PMT.XREF.END.DATE` | `CaplUbPaymentXref_EndDate` | TField |  | Field to store the date till which the ill payment is failed.Mapped from the Second part of ID.Used for the Enquiry Report selection |
| 8 | `UB.PMT.XREF.RESERVED.1` | `CaplUbPaymentXref_Reserved1` | TField |  |  |
| 9 | `UB.PMT.XREF.RESERVED.2` | `CaplUbPaymentXref_Reserved2` | TField |  |  |
| 10 | `UB.PMT.XREF.RESERVED.3` | `CaplUbPaymentXref_Reserved3` | TField |  |  |
| 11 | `UB.PMT.XREF.RESERVED.4` | `CaplUbPaymentXref_Reserved4` | TField |  |  |
| 12 | `UB.PMT.XREF.RESERVED.5` | `CaplUbPaymentXref_Reserved5` | TField |  |  |
| 13 | `UB.PMT.XREF.RESERVED.6` | `CaplUbPaymentXref_Reserved6` | TField |  |  |
| 14 | `UB.PMT.XREF.RESERVED.7` | `CaplUbPaymentXref_Reserved7` | TField |  |  |
| 15 | `UB.PMT.XREF.RESERVED.8` | `CaplUbPaymentXref_Reserved8` | TField |  |  |
| 16 | `UB.PMT.XREF.RESERVED.9` | `CaplUbPaymentXref_Reserved9` | TField |  |  |
| 17 | `UB.PMT.XREF.RESERVED.10` | `CaplUbPaymentXref_Reserved10` | TField |  |  |
