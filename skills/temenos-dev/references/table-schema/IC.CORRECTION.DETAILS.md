# IC.CORRECTION.DETAILS — Table Schema

> Source: `INSERTS/I_F.IC.CORRECTION.DETAILS` in `IC_InterestAndCapitalisation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IC.CORDT.INTEREST.TYPE` | `IcCorrectionDetails_InterestType` |  |  |  |
| 2 | `IC.CORDT.CORRECTION.ID` | `IcCorrectionDetails_CorrectionId` |  |  |  |
| 3 | `IC.CORDT.ADJ.INT.AMT` | `IcCorrectionDetails_AdjIntAmt` |  |  |  |
| 4 | `IC.CORDT.ADJ.TAX.AMT` | `IcCorrectionDetails_AdjTaxAmt` |  |  |  |
| 5 | `IC.CORDT.WITHHELD.INT.AMT` | `IcCorrectionDetails_WithheldIntAmt` |  |  |  |
| 6 | `IC.CORDT.RESERVED.10` | `IcCorrectionDetails_Reserved10` | TField |  |  |
| 7 | `IC.CORDT.RESERVED.9` | `IcCorrectionDetails_Reserved9` | TField |  |  |
| 8 | `IC.CORDT.RESERVED.8` | `IcCorrectionDetails_Reserved8` | TField |  |  |
| 9 | `IC.CORDT.RESERVED.7` | `IcCorrectionDetails_Reserved7` | TField |  |  |
| 10 | `IC.CORDT.RESERVED.6` | `IcCorrectionDetails_Reserved6` | TField |  |  |
| 11 | `IC.CORDT.RESERVED.5` | `IcCorrectionDetails_Reserved5` | TField |  |  |
| 12 | `IC.CORDT.RESERVED.4` | `IcCorrectionDetails_Reserved4` | TField |  |  |
| 13 | `IC.CORDT.RESERVED.3` | `IcCorrectionDetails_Reserved3` | TField |  |  |
| 14 | `IC.CORDT.RESERVED.2` | `IcCorrectionDetails_Reserved2` | TField |  |  |
| 15 | `IC.CORDT.RESERVED.1` | `IcCorrectionDetails_Reserved1` | TField |  |  |
