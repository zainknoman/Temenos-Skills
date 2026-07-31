# LC.COMM.ACCR.DETAILS — Table Schema

> Source: `INSERTS/I_F.LC.COMM.ACCR.DETAILS` in `LC_Fees.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LC.CA.CURRENCY` | `LcCommAccrDetails_Currency` | TField |  | Currency of Letter of Credit or Drawings contract. |
| 2 | `LC.CA.PRIN.BALANCE` | `LcCommAccrDetails_PrinBalance` |  |  |  |
| 3 | `LC.CA.PRIN.EFF.DATE` | `LcCommAccrDetails_PrinEffDate` |  |  |  |
| 4 | `LC.CA.START.CSN.PERIOD` | `LcCommAccrDetails_StartCsnPeriod` | TField |  | Holds the date from which the commission is calculated for the current schedule. |
| 5 | `LC.CA.END.CSN.PERIOD` | `LcCommAccrDetails_EndCsnPeriod` | TField |  | Holds the start date of commission for the next schedule. |
| 6 | `LC.CA.CSN.AMOUNT` | `LcCommAccrDetails_CsnAmount` | TField |  | Holds the commission amount for the current schedule. |
| 7 | `LC.CA.COMM.TAX.AMOUNT` | `LcCommAccrDetails_CommTaxAmount` | TField |  | Holds the tax component of the commission amount for the current schedule. |
| 8 | `LC.CA.CSN.BASE.DATE` | `LcCommAccrDetails_CsnBaseDate` | TField |  | Reserved for future use. |
| 9 | `LC.CA.ACCR.FROM.DATE` | `LcCommAccrDetails_AccrFromDate` |  |  |  |
| 10 | `LC.CA.ACCR.TO.DATE` | `LcCommAccrDetails_AccrToDate` |  |  |  |
| 11 | `LC.CA.ACCR.DAYS` | `LcCommAccrDetails_AccrDays` |  |  |  |
| 12 | `LC.CA.ACCR.PRIN` | `LcCommAccrDetails_AccrPrin` |  |  |  |
| 13 | `LC.CA.ACCR.RATE` | `LcCommAccrDetails_AccrRate` |  |  |  |
| 14 | `LC.CA.ACCR.AMT` | `LcCommAccrDetails_AccrAmt` |  |  |  |
| 15 | `LC.CA.ACCR.ACT.AMT` | `LcCommAccrDetails_AccrActAmt` |  |  |  |
| 16 | `LC.CA.CSN.RATE` | `LcCommAccrDetails_CsnRate` |  |  |  |
| 17 | `LC.CA.CSN.RATE.EFF.DT` | `LcCommAccrDetails_CsnRateEffDt` |  |  |  |
| 18 | `LC.CA.SCH.CSN.DT` | `LcCommAccrDetails_SchCsnDt` |  |  |  |
| 19 | `LC.CA.SCH.PRC.DT` | `LcCommAccrDetails_SchPrcDt` |  |  |  |
| 20 | `LC.CA.SCH.CSN.AMT` | `LcCommAccrDetails_SchCsnAmt` |  |  |  |
| 21 | `LC.CA.COMM.ST.DATE` | `LcCommAccrDetails_CommStDate` |  |  |  |
| 22 | `LC.CA.PRIN.AMT` | `LcCommAccrDetails_PrinAmt` |  |  |  |
| 23 | `LC.CA.COMM.END.DATE` | `LcCommAccrDetails_CommEndDate` |  |  |  |
| 24 | `LC.CA.COMM.PERIOD` | `LcCommAccrDetails_CommPeriod` | TField |  | Holds the period at which the commission rate is to be applied. System maintained field. |
| 25 | `LC.CA.COMM.CODE` | `LcCommAccrDetails_CommCode` |  |  |  |
| 26 | `LC.CA.COMM.RATE` | `LcCommAccrDetails_CommRate` |  |  |  |
| 27 | `LC.CA.COMM.AMT` | `LcCommAccrDetails_CommAmt` |  |  |  |
| 28 | `LC.CA.RESERVED1` | `LcCommAccrDetails_Reserved1` |  |  |  |
| 29 | `LC.CA.RESERVED2` | `LcCommAccrDetails_Reserved2` |  |  |  |
