# RT.INDICIA.DETS — Table Schema

> Source: `INSERTS/I_F.RT.INDICIA.DETS` in `RT_IndiciaChecks.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RID.APPLN.ID` | `RtIndiciaDets_ApplnId` |  |  |  |
| 2 | `RID.BEN.ID` | `RtIndiciaDets_BenId` |  |  |  |
| 3 | `RID.FATCA.BEN.COUNTRY` | `RtIndiciaDets_FatcaBenCountry` |  |  |  |
| 4 | `RID.CRS.BEN.COUNTRY` | `RtIndiciaDets_CrsBenCountry` |  |  |  |
| 5 | `RID.STO.INDICATOR` | `RtIndiciaDets_StoIndicator` |  |  |  |
| 6 | `RID.END.DATE` | `RtIndiciaDets_EndDate` |  |  |  |
| 7 | `RID.EFFECTIVE.DATE` | `RtIndiciaDets_EffectiveDate` |  |  |  |
| 8 | `RID.HOLDMAIL.START.DATE` | `RtIndiciaDets_HoldmailStartDate` | TField |  |  |
| 9 | `RID.HOLDMAIL.END.DATE` | `RtIndiciaDets_HoldmailEndDate` | TField |  |  |
