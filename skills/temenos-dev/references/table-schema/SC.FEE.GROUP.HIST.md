# SC.FEE.GROUP.HIST — Table Schema

> Source: `INSERTS/I_F.SC.FEE.GROUP.HIST` in `SC_ScfConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SFGH.DATE.FROM` | `ScFeeGroupHist_DateFrom` |  |  |  |
| 2 | `SFGH.DATE.TO` | `ScFeeGroupHist_DateTo` |  |  |  |
| 3 | `SFGH.PAYMENT` | `ScFeeGroupHist_Payment` |  |  |  |
| 4 | `SFGH.PORT.LIST` | `ScFeeGroupHist_PortList` |  |  |  |
| 5 | `SFGH.RESERVED7` | `ScFeeGroupHist_Reserved7` | TField |  |  |
| 6 | `SFGH.RESERVED6` | `ScFeeGroupHist_Reserved6` | TField |  |  |
| 7 | `SFGH.RESERVED5` | `ScFeeGroupHist_Reserved5` | TField |  |  |
| 8 | `SFGH.RESERVED4` | `ScFeeGroupHist_Reserved4` | TField |  |  |
| 9 | `SFGH.RESERVED3` | `ScFeeGroupHist_Reserved3` | TField |  |  |
| 10 | `SFGH.RESERVED2` | `ScFeeGroupHist_Reserved2` | TField |  |  |
| 11 | `SFGH.RESERVED1` | `ScFeeGroupHist_Reserved1` | TField |  |  |
