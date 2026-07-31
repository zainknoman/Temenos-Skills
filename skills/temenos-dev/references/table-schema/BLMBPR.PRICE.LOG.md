# BLMBPR.PRICE.LOG — Table Schema

> Source: `INSERTS/I_F.BLMBPR.PRICE.LOG` in `BLMBPR_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BLMBPR.LOG.SEC.NO` | `BlmbprPriceLog_SecNo` | TField |  | This filed will update the SECURITY.MASTER id for the process inward file. |
| 2 | `BLMBPR.LOG.CREATION.DATE` | `BlmbprPriceLog_CreationDate` | TField |  | Which date the record was processed to update the SM record. |
| 3 | `BLMBPR.LOG.TIME.STAMP` | `BlmbprPriceLog_TimeStamp` | TField |  | Time Stamp of the Processed record will be updated in this field. |
| 4 | `BLMBPR.LOG.MSG.DETAIL` | `BlmbprPriceLog_MsgDetail` | TField |  | Incoming request for the processed record will be update in the MSG.DETAIL field. |
| 5 | `BLMBPR.LOG.STATUS` | `BlmbprPriceLog_Status` | TField |  |  |
| 6 | `BLMBPR.LOG.REJECTION.REASON` | `BlmbprPriceLog_RejectionReason` | TField |  | If the record was rejected means the reason will update in this field. |
| 7 | `BLMBPR.LOG.RESERVED.5` | `BlmbprPriceLog_Reserved5` | TField |  |  |
| 8 | `BLMBPR.LOG.RESERVED.4` | `BlmbprPriceLog_Reserved4` | TField |  |  |
| 9 | `BLMBPR.LOG.RESERVED.3` | `BlmbprPriceLog_Reserved3` | TField |  |  |
| 10 | `BLMBPR.LOG.RESERVED.2` | `BlmbprPriceLog_Reserved2` | TField |  |  |
| 11 | `BLMBPR.LOG.RESERVED.1` | `BlmbprPriceLog_Reserved1` | TField |  |  |
| 12 | `BLMBPR.LOG.LOCAL.REF` | `BlmbprPriceLog_LocalRef` |  |  |  |
