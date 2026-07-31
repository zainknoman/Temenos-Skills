# MIFID.PF.GRP.TER.DETAILS — Table Schema

> Source: `INSERTS/I_F.MIFID.PF.GRP.TER.DETAILS` in `MIFDII_IRP.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MIFID.PF.GRP.GENERATED.DATE` | `MifidPfGrpTerDetails_GeneratedDate` | TField |  | This field stores the report Generated date. Validation Rule: This is a NOINPUT field. |
| 2 | `MIFID.PF.GRP.VAL.START.DATE` | `MifidPfGrpTerDetails_ValStartDate` | TField |  | This field stores the Valuation start date. Validation Rule: This is a NOINPUT field. |
| 3 | `MIFID.PF.GRP.REF.CCY` | `MifidPfGrpTerDetails_RefCcy` | TField |  | This field stores the Reference Currency of Portfolio/Group. Validation Rule: This is a NOINPUT field. |
| 4 | `MIFID.PF.GRP.VALUATION` | `MifidPfGrpTerDetails_Valuation` | TField |  | This field stores the Value of Valaution of Portfolio/Group. Validation Rule: This is a NOINPUT field. |
| 5 | `MIFID.PF.GRP.RETURN.PCT` | `MifidPfGrpTerDetails_ReturnPct` | TField |  | This field stores the Performance Return of Portfolio/Group. Validation Rule: This is a NOINPUT field. |
| 6 | `MIFID.PF.GRP.INV.PROGRAM` | `MifidPfGrpTerDetails_InvProgram` | TField |  | This field stores the Invest program of Portfolio /Group. Validation Rule: This is a NOINPUT field. |
| 7 | `MIFID.PF.GRP.BENCHMARK` | `MifidPfGrpTerDetails_Benchmark` | TField |  | This field stores the Benchmark of Portfolio/Group. Validation Rule: This is a NOINPUT field. |
| 8 | `MIFID.PF.GRP.CURRENT.TER.PCT` | `MifidPfGrpTerDetails_CurrentTerPct` | TField |  | This field stores the TER Percentage. Validation Rule: This is a NOINPUT field. |
| 9 | `MIFID.PF.GRP.CUM.TER.COST` | `MifidPfGrpTerDetails_CumTerCost` |  |  |  |
| 10 | `MIFID.PF.GRP.OTHER.CHGS` | `MifidPfGrpTerDetails_OtherChgs` | TField |  | This field stores the Other MIFID Charges. Validation Rule: This is a NOINPUT field. |
| 11 | `MIFID.PF.GRP.LOCAL.REF` | `MifidPfGrpTerDetails_LocalRef` |  |  |  |
| 12 | `MIFID.PF.GRP.RESERVED.10` | `MifidPfGrpTerDetails_Reserved10` | TField |  |  |
| 13 | `MIFID.PF.GRP.RESERVED.9` | `MifidPfGrpTerDetails_Reserved9` | TField |  |  |
| 14 | `MIFID.PF.GRP.RESERVED.8` | `MifidPfGrpTerDetails_Reserved8` | TField |  |  |
| 15 | `MIFID.PF.GRP.RESERVED.7` | `MifidPfGrpTerDetails_Reserved7` | TField |  |  |
| 16 | `MIFID.PF.GRP.RESERVED.6` | `MifidPfGrpTerDetails_Reserved6` | TField |  |  |
| 17 | `MIFID.PF.GRP.RESERVED.5` | `MifidPfGrpTerDetails_Reserved5` | TField |  |  |
| 18 | `MIFID.PF.GRP.RESERVED.4` | `MifidPfGrpTerDetails_Reserved4` | TField |  |  |
| 19 | `MIFID.PF.GRP.RESERVED.3` | `MifidPfGrpTerDetails_Reserved3` | TField |  |  |
| 20 | `MIFID.PF.GRP.RESERVED.2` | `MifidPfGrpTerDetails_Reserved2` | TField |  |  |
| 21 | `MIFID.PF.GRP.RESERVED.1` | `MifidPfGrpTerDetails_Reserved1` | TField |  |  |
| 22 | `MIFID.PF.GRP.OVERRIDE` | `MifidPfGrpTerDetails_Override` |  |  |  |
