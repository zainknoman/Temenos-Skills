# CL.ITEM.BUCKET — Table Schema

> Source: `INSERTS/I_F.CL.ITEM.BUCKET` in `CL_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CL.BK.BUCKET.DATE` | `ClItemBucket_BucketDate` |  |  |  |
| 2 | `CL.BK.BUCKET` | `ClItemBucket_Bucket` |  |  |  |
| 3 | `CL.BK.OVERDUE.AMT` | `ClItemBucket_OverdueAmt` |  |  |  |
| 4 | `CL.BK.OD.CURRENCY` | `ClItemBucket_OdCurrency` |  |  |  |
| 5 | `CL.BK.OUTSTANDING.AMT` | `ClItemBucket_OutstandingAmt` |  |  |  |
| 6 | `CL.BK.CUR.OVERDUE.AMT` | `ClItemBucket_CurOverdueAmt` | TField |  | Current Total overdue amount. |
| 7 | `CL.BK.CUR.OUTS.AMT` | `ClItemBucket_CurOutsAmt` | TField |  | Current Total oustanding amount. |
| 8 | `CL.BK.RESERVED.3` | `ClItemBucket_Reserved3` | TField |  |  |
| 9 | `CL.BK.RESERVED.2` | `ClItemBucket_Reserved2` | TField |  |  |
| 10 | `CL.BK.RESERVED.1` | `ClItemBucket_Reserved1` | TField |  |  |
