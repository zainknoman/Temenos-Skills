# PPT.FEETYPE — Table Schema

> Source: `INSERTS/I_F.PPT.FEETYPE` in `PP_FeeDeterminationService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPFET.FeeTypeID` | `PptFeetype_Feetypeid` |  |  |  |
| 2 | `PPFET.CompanyID` | `PptFeetype_Companyid` |  |  |  |
| 3 | `PPFET.FeeType` | `PptFeetype_Feetype` |  |  |  |
| 4 | `PPFET.StartDateFeeType` | `PptFeetype_Startdatefeetype` |  |  |  |
| 5 | `PPFET.ConditionalIndicator` | `PptFeetype_Conditionalindicator` |  |  |  |
| 6 | `PPFET.BeneficiaryChargeAllowed` | `PptFeetype_Beneficiarychargeallowed` |  |  |  |
| 7 | `PPFET.LanguageID1` | `PptFeetype_Languageid1` |  |  |  |
| 8 | `PPFET.FeeDescription1` | `PptFeetype_Feedescription1` |  |  |  |
| 9 | `PPFET.LanguageID2` | `PptFeetype_Languageid2` |  |  |  |
| 10 | `PPFET.FeeDescription2` | `PptFeetype_Feedescription2` |  |  |  |
| 11 | `PPFET.LanguageID3` | `PptFeetype_Languageid3` |  |  |  |
| 12 | `PPFET.FeeDescription3` | `PptFeetype_Feedescription3` |  |  |  |
| 13 | `PPFET.PercentageVATOnCharge` | `PptFeetype_Percentagevatoncharge` |  |  |  |
| 14 | `PPFET.EndDateFeeType` | `PptFeetype_Enddatefeetype` |  |  |  |
| 15 | `PPFET.RACFeeType` | `PptFeetype_Racfeetype` |  |  |  |
| 16 | `PPFET.RSCFeeType` | `PptFeetype_Rscfeetype` |  |  |  |
| 17 | `PPFET.EntryUserID` | `PptFeetype_Entryuserid` |  |  |  |
| 18 | `PPFET.EntryDateTime` | `PptFeetype_Entrydatetime` |  |  |  |
| 19 | `PPFET.ApproverUserID` | `PptFeetype_Approveruserid` |  |  |  |
| 20 | `PPFET.ApprovedDateTime` | `PptFeetype_Approveddatetime` |  |  |  |
