# USREGS.FIRE.FILE.DETAILS — Table Schema

> Source: `INSERTS/I_F.USREGS.FIRE.FILE.DETAILS` in `USREGS_YearEndTaxReporting.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FF.DETS.CURRENT.RECORD` | `UsregsFireFileDetails_CurrentRecord` | TField |  |  |
| 2 | `FF.DETS.PREVIOUS.RECORD` | `UsregsFireFileDetails_PreviousRecord` | TField |  |  |
| 3 | `FF.DETS.DEPOSIT.INCOME` | `UsregsFireFileDetails_DepositIncome` | TField |  |  |
| 4 | `FF.DETS.FEDERAL.WHT` | `UsregsFireFileDetails_FederalWht` | TField |  |  |
| 5 | `FF.DETS.OTHER.WHT` | `UsregsFireFileDetails_OtherWht` | TField |  |  |
| 6 | `FF.DETS.WITH.ALLOW` | `UsregsFireFileDetails_WithAllow` | TField |  |  |
| 7 | `FF.DETS.STATE.INCOME.TAX` | `UsregsFireFileDetails_StateIncomeTax` | TField |  |  |
| 8 | `FF.DETS.PAY.AMT.1` | `UsregsFireFileDetails_PayAmt1` | TField |  |  |
| 9 | `FF.DETS.PAY.AMT.2` | `UsregsFireFileDetails_PayAmt2` | TField |  |  |
| 10 | `FF.DETS.PAY.AMT.3` | `UsregsFireFileDetails_PayAmt3` | TField |  |  |
| 11 | `FF.DETS.PAY.AMT.4` | `UsregsFireFileDetails_PayAmt4` | TField |  |  |
| 12 | `FF.DETS.PAY.AMT.5` | `UsregsFireFileDetails_PayAmt5` | TField |  |  |
| 13 | `FF.DETS.PAY.AMT.6` | `UsregsFireFileDetails_PayAmt6` | TField |  |  |
| 14 | `FF.DETS.PAY.AMT.7` | `UsregsFireFileDetails_PayAmt7` | TField |  |  |
| 15 | `FF.DETS.PAY.AMT.8` | `UsregsFireFileDetails_PayAmt8` | TField |  |  |
| 16 | `FF.DETS.PAY.AMT.9` | `UsregsFireFileDetails_PayAmt9` | TField |  |  |
| 17 | `FF.DETS.PAY.AMT.10` | `UsregsFireFileDetails_PayAmt10` | TField |  |  |
| 18 | `FF.DETS.PAY.AMT.11` | `UsregsFireFileDetails_PayAmt11` | TField |  |  |
| 19 | `FF.DETS.PAY.AMT.12` | `UsregsFireFileDetails_PayAmt12` | TField |  |  |
| 20 | `FF.DETS.PAY.AMT.13` | `UsregsFireFileDetails_PayAmt13` | TField |  |  |
| 21 | `FF.DETS.PAY.AMT.14` | `UsregsFireFileDetails_PayAmt14` | TField |  |  |
| 22 | `FF.DETS.PAY.AMT.15` | `UsregsFireFileDetails_PayAmt15` | TField |  |  |
| 23 | `FF.DETS.PAY.AMT.16` | `UsregsFireFileDetails_PayAmt16` | TField |  |  |
| 24 | `FF.DETS.LOCAL.INCOME` | `UsregsFireFileDetails_LocalIncome` | TField |  |  |
| 25 | `FF.DETS.STATE.INCOME` | `UsregsFireFileDetails_StateIncome` | TField |  |  |
| 26 | `FF.DETS.NET.INCOME` | `UsregsFireFileDetails_NetIncome` | TField |  |  |
