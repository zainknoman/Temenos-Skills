# ILMATX.OPTIMISATION.DETAILS — Table Schema

> Source: `INSERTS/I_F.ILMATX.OPTIMISATION.DETAILS` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ILMATX.RESPONSE.STATUS` | `IlmatxOptimisationDetails_ResponseStatus` | TField |  | This field holds 3 values which describes whether the record is Response Received, Processed or NotProcessed. |
| 2 | `ILMATX.TAX.AMOUNT` | `IlmatxOptimisationDetails_TaxAmount` | TField |  | This field holds the Amount needs to be debited from Customer Account. |
| 3 | `ILMATX.REFUND.AMOUNT` | `IlmatxOptimisationDetails_RefundAmount` | TField |  | This field holds the Amount needs to be credited to Customer Account. |
| 4 | `ILMATX.ACCOUNT.ENTRY.REF` | `IlmatxOptimisationDetails_AccountEntryRef` | TField |  | This field holds the Reference when the AC.INWARD.ENTRY has been created. |
| 5 | `ILMATX.RESERVED.5` | `IlmatxOptimisationDetails_Reserved5` | TField |  | Reserved for future use. |
| 6 | `ILMATX.RESERVED.4` | `IlmatxOptimisationDetails_Reserved4` | TField |  | Reserved for future use. |
| 7 | `ILMATX.RESERVED.3` | `IlmatxOptimisationDetails_Reserved3` | TField |  | Reserved for future use. |
| 8 | `ILMATX.RESERVED.2` | `IlmatxOptimisationDetails_Reserved2` | TField |  | Reserved for future use. |
| 9 | `ILMATX.RESERVED.1` | `IlmatxOptimisationDetails_Reserved1` | TField |  | Reserved for future use. |
| 10 | `ILMATX.LOCAL.REF` | `IlmatxOptimisationDetails_LocalRef` |  |  |  |
| 11 | `ILMATX.OVERRIDE` | `IlmatxOptimisationDetails_Override` |  |  |  |
| 12 | `ILMATX.RECORD.STATUS` | `IlmatxOptimisationDetails_RecordStatus` | String |  |  |
| 13 | `ILMATX.CURR.NO` | `IlmatxOptimisationDetails_CurrNo` | String |  |  |
| 14 | `ILMATX.INPUTTER` | `IlmatxOptimisationDetails_Inputter` |  |  |  |
| 15 | `ILMATX.DATE.TIME` | `IlmatxOptimisationDetails_DateTime` |  |  |  |
| 16 | `ILMATX.AUTHORISER` | `IlmatxOptimisationDetails_Authoriser` | String |  |  |
| 17 | `ILMATX.CO.CODE` | `IlmatxOptimisationDetails_CoCode` | String |  |  |
| 18 | `ILMATX.DEPT.CODE` | `IlmatxOptimisationDetails_DeptCode` | String |  |  |
| 19 | `ILMATX.AUDITOR.CODE` | `IlmatxOptimisationDetails_AuditorCode` | String |  |  |
| 20 | `ILMATX.AUDIT.DATE.TIME` | `IlmatxOptimisationDetails_AuditDateTime` | String |  |  |
