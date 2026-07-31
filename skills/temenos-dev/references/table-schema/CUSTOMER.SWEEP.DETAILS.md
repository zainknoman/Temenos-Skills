# CUSTOMER.SWEEP.DETAILS — Table Schema

> Source: `INSERTS/I_F.CUSTOMER.SWEEP.DETAILS` in `CACSIT_CoverdraftSweep.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CWB.SWF.TO.ACCOUNT` | `CustomerSweepDetails_ToAccount` |  |  |  |
| 2 | `CWB.SWF.AC.CASH.POOL` | `CustomerSweepDetails_AcCashPool` |  |  |  |
| 3 | `CWB.SWF.RESERVED.5` | `CustomerSweepDetails_Reserved5` |  |  |  |
| 4 | `CWB.SWF.RESERVED.4` | `CustomerSweepDetails_Reserved4` |  |  |  |
| 5 | `CWB.SWF.RESERVED.3` | `CustomerSweepDetails_Reserved3` |  |  |  |
| 6 | `CWB.SWF.RESERVED.2` | `CustomerSweepDetails_Reserved2` |  |  |  |
| 7 | `CWB.SWF.RESERVED.1` | `CustomerSweepDetails_Reserved1` |  |  |  |
| 8 | `CWB.SWF.FROM.ACCOUNT` | `CustomerSweepDetails_FromAccount` |  |  |  |
| 9 | `CWB.SWF.INTEREST.REPAYMENT` | `CustomerSweepDetails_InterestRepayment` |  |  |  |
| 10 | `CWB.SWF.RESERVED.10` | `CustomerSweepDetails_Reserved10` |  |  |  |
| 11 | `CWB.SWF.RESERVED.9` | `CustomerSweepDetails_Reserved9` |  |  |  |
| 12 | `CWB.SWF.RESERVED.8` | `CustomerSweepDetails_Reserved8` |  |  |  |
| 13 | `CWB.SWF.RESERVED.7` | `CustomerSweepDetails_Reserved7` |  |  |  |
| 14 | `CWB.SWF.RESERVED.6` | `CustomerSweepDetails_Reserved6` |  |  |  |
| 15 | `CWB.SWF.CAPITAL.REPAYMENT` | `CustomerSweepDetails_CapitalRepayment` |  |  |  |
| 16 | `CWB.SWF.RESERVED.20` | `CustomerSweepDetails_Reserved20` | TField |  |  |
| 17 | `CWB.SWF.RESERVED.19` | `CustomerSweepDetails_Reserved19` | TField |  |  |
| 18 | `CWB.SWF.RESERVED.18` | `CustomerSweepDetails_Reserved18` | TField |  |  |
| 19 | `CWB.SWF.RESERVED.17` | `CustomerSweepDetails_Reserved17` | TField |  |  |
| 20 | `CWB.SWF.RESERVED.16` | `CustomerSweepDetails_Reserved16` | TField |  |  |
| 21 | `CWB.SWF.RESERVED.15` | `CustomerSweepDetails_Reserved15` | TField |  |  |
| 22 | `CWB.SWF.RESERVED.14` | `CustomerSweepDetails_Reserved14` | TField |  |  |
| 23 | `CWB.SWF.RESERVED.13` | `CustomerSweepDetails_Reserved13` | TField |  |  |
| 24 | `CWB.SWF.RESERVED.12` | `CustomerSweepDetails_Reserved12` | TField |  |  |
| 25 | `CWB.SWF.RESERVED.11` | `CustomerSweepDetails_Reserved11` | TField |  |  |
