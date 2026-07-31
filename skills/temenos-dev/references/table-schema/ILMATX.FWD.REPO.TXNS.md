# ILMATX.FWD.REPO.TXNS — Table Schema

> Source: `INSERTS/I_F.ILMATX.FWD.REPO.TXNS` in `ILMATX_MatrixTaxServerInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `REPO.MATX.VALUE.DATE` | `IlmatxFwdRepoTxns_ValueDate` | TField |  | Value date of the record. |
| 2 | `REPO.MATX.STATUS` | `IlmatxFwdRepoTxns_Status` | TField |  | Stores two values 'HOLD' if Value date is greater than today and 'SENT' if value date reaches today |
| 3 | `REPO.MATX.RESERVED.5` | `IlmatxFwdRepoTxns_Reserved5` | TField |  | Reserved for future use. |
| 4 | `REPO.MATX.RESERVED.4` | `IlmatxFwdRepoTxns_Reserved4` | TField |  | Reserved for future use. |
| 5 | `REPO.MATX.RESERVED.3` | `IlmatxFwdRepoTxns_Reserved3` | TField |  | Reserved for future use. |
| 6 | `REPO.MATX.RESERVED.2` | `IlmatxFwdRepoTxns_Reserved2` | TField |  | Reserved for future use. |
| 7 | `REPO.MATX.RESERVED.1` | `IlmatxFwdRepoTxns_Reserved1` | TField |  | Reserved for future use. |
| 8 | `REPO.MATX.LOCAL.REF` | `IlmatxFwdRepoTxns_LocalRef` |  |  |  |
