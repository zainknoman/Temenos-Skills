# USIRAC.DISTRIBUTION.DETAILS — Table Schema

> Source: `INSERTS/I_F.USIRAC.DISTRIBUTION.DETAILS` in `USIRAC_IRA.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DIST.DETS.DISTRIBUTION.DATE` | `UsiracDistributionDetails_DistributionDate` |  |  |  |
| 2 | `DIST.DETS.IRA.ID` | `UsiracDistributionDetails_IraId` |  |  |  |
| 3 | `DIST.DETS.DISTRIBUTION.AMT` | `UsiracDistributionDetails_DistributionAmt` |  |  |  |
| 4 | `DIST.DETS.DISTRIBUTION.TXN` | `UsiracDistributionDetails_DistributionTxn` |  |  |  |
| 5 | `DIST.DETS.DISTRIBUTION.TYPE` | `UsiracDistributionDetails_DistributionType` |  |  |  |
| 6 | `DIST.DETS.ACTIVITY.STATUS` | `UsiracDistributionDetails_ActivityStatus` |  |  |  |
| 7 | `DIST.DETS.RESERVED.13` | `UsiracDistributionDetails_Reserved13` |  |  |  |
| 8 | `DIST.DETS.RESERVED.12` | `UsiracDistributionDetails_Reserved12` |  |  |  |
| 9 | `DIST.DETS.RESERVED.11` | `UsiracDistributionDetails_Reserved11` |  |  |  |
| 10 | `DIST.DETS.RESERVED.10` | `UsiracDistributionDetails_Reserved10` | TField |  |  |
| 11 | `DIST.DETS.RESERVED.9` | `UsiracDistributionDetails_Reserved9` | TField |  |  |
| 12 | `DIST.DETS.RESERVED.8` | `UsiracDistributionDetails_Reserved8` | TField |  |  |
| 13 | `DIST.DETS.RESERVED.7` | `UsiracDistributionDetails_Reserved7` | TField |  |  |
| 14 | `DIST.DETS.RESERVED.6` | `UsiracDistributionDetails_Reserved6` | TField |  |  |
| 15 | `DIST.DETS.RESERVED.5` | `UsiracDistributionDetails_Reserved5` | TField |  |  |
| 16 | `DIST.DETS.RESERVED.4` | `UsiracDistributionDetails_Reserved4` | TField |  |  |
| 17 | `DIST.DETS.RESERVED.3` | `UsiracDistributionDetails_Reserved3` | TField |  |  |
| 18 | `DIST.DETS.RESERVED.2` | `UsiracDistributionDetails_Reserved2` | TField |  |  |
| 19 | `DIST.DETS.RESERVED.1` | `UsiracDistributionDetails_Reserved1` | TField |  |  |
