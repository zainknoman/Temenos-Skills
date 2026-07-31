# LC.COMM.CALC.DETAILS — Table Schema

> Source: `INSERTS/I_F.LC.COMM.CALC.DETAILS` in `LC_Fees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LC.CC.CURRENCY` | `LcCommCalcDetails_Currency` | TField |  | Holds the currency of LETTER.OF.CREDIT or DRAWINGS contract. |
| 2 | `LC.CC.COMM.CODE` | `LcCommCalcDetails_CommCode` | TField |  | Holds valid record of PERIODIC.COMMISSION table. |
| 3 | `LC.CC.EFFECTIVE.DATE` | `LcCommCalcDetails_EffectiveDate` |  |  |  |
| 4 | `LC.CC.CSN.CODE` | `LcCommCalcDetails_CsnCode` |  |  |  |
| 5 | `LC.CC.UPTO.DAYS` | `LcCommCalcDetails_UptoDays` |  |  |  |
| 6 | `LC.CC.UPTO.AMT` | `LcCommCalcDetails_UptoAmt` |  |  |  |
| 7 | `LC.CC.CSN.RATE` | `LcCommCalcDetails_CsnRate` |  |  |  |
| 8 | `LC.CC.CSN.AMT` | `LcCommCalcDetails_CsnAmt` |  |  |  |
| 9 | `LC.CC.RESERVED.5` | `LcCommCalcDetails_Reserved5` | TField |  |  |
| 10 | `LC.CC.RESERVED.4` | `LcCommCalcDetails_Reserved4` | TField |  |  |
| 11 | `LC.CC.RESERVED.3` | `LcCommCalcDetails_Reserved3` | TField |  |  |
| 12 | `LC.CC.RESERVED.2` | `LcCommCalcDetails_Reserved2` | TField |  |  |
| 13 | `LC.CC.RESERVED.1` | `LcCommCalcDetails_Reserved1` | TField |  |  |
