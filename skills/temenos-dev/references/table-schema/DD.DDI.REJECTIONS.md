# DD.DDI.REJECTIONS — Table Schema

> Source: `INSERTS/I_F.DD.DDI.REJECTIONS` in `HKDDPR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DD.DDI.REJECT.FIELD.NAME` | `DdDdiRejections_FieldName` |  |  |  |
| 2 | `DD.DDI.REJECT.FIELD.VALUE` | `DdDdiRejections_FieldValue` |  |  |  |
| 3 | `DD.DDI.REJECT.ERROR.MESSAGE` | `DdDdiRejections_ErrorMessage` |  |  |  |
| 4 | `DD.DDI.REJECT.RESERVED.13` | `DdDdiRejections_Reserved13` |  |  |  |
| 5 | `DD.DDI.REJECT.RESERVED.12` | `DdDdiRejections_Reserved12` |  |  |  |
| 6 | `DD.DDI.REJECT.RESERVED.11` | `DdDdiRejections_Reserved11` |  |  |  |
| 7 | `DD.DDI.REJECT.TRANSACTION.DATE` | `DdDdiRejections_TransactionDate` | TField |  | Date of DD.DDI Transaction |
| 8 | `DD.DDI.REJECT.RESERVED.10` | `DdDdiRejections_Reserved10` | TField |  |  |
| 9 | `DD.DDI.REJECT.RESERVED.9` | `DdDdiRejections_Reserved9` | TField |  |  |
| 10 | `DD.DDI.REJECT.RESERVED.8` | `DdDdiRejections_Reserved8` | TField |  |  |
| 11 | `DD.DDI.REJECT.RESERVED.7` | `DdDdiRejections_Reserved7` | TField |  |  |
| 12 | `DD.DDI.REJECT.RESERVED.6` | `DdDdiRejections_Reserved6` | TField |  |  |
| 13 | `DD.DDI.REJECT.RESERVED.5` | `DdDdiRejections_Reserved5` | TField |  |  |
| 14 | `DD.DDI.REJECT.RESERVED.4` | `DdDdiRejections_Reserved4` | TField |  |  |
| 15 | `DD.DDI.REJECT.RESERVED.3` | `DdDdiRejections_Reserved3` | TField |  |  |
| 16 | `DD.DDI.REJECT.RESERVED.2` | `DdDdiRejections_Reserved2` | TField |  |  |
| 17 | `DD.DDI.REJECT.RESERVED.1` | `DdDdiRejections_Reserved1` | TField |  |  |
| 18 | `DD.DDI.REJECT.LOCAL.REF` | `DdDdiRejections_LocalRef` |  |  |  |
