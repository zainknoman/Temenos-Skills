# IS.SETTLEMENT.LOG.HIST — Table Schema

> Source: `INSERTS/I_F.IS.SETTLEMENT.LOG.HIST` in `IS_Payment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.SEH.CUSTOMER` | `IsSettlementLogHist_Customer` | TField |  |  |
| 2 | `IS.SEH.DATE` | `IsSettlementLogHist_Date` | TField |  |  |
| 3 | `IS.SEH.SETTLEMENT.TYPE` | `IsSettlementLogHist_SettlementType` | TField |  |  |
| 4 | `IS.SEH.ARRANGEMENT.REF` | `IsSettlementLogHist_ArrangementRef` | TField |  |  |
| 5 | `IS.SEH.TRANS.REFERENCE` | `IsSettlementLogHist_TransReference` |  |  |  |
| 6 | `IS.SEH.EXPECTED.AMOUNT` | `IsSettlementLogHist_ExpectedAmount` |  |  |  |
| 7 | `IS.SEH.ACTUAL.AMOUNT` | `IsSettlementLogHist_ActualAmount` |  |  |  |
| 8 | `IS.SEH.RESERVED.5` | `IsSettlementLogHist_Reserved5` |  |  |  |
| 9 | `IS.SEH.RESERVED.4` | `IsSettlementLogHist_Reserved4` |  |  |  |
| 10 | `IS.SEH.RESERVED.3` | `IsSettlementLogHist_Reserved3` |  |  |  |
| 11 | `IS.SEH.RESERVED.2` | `IsSettlementLogHist_Reserved2` |  |  |  |
| 12 | `IS.SEH.RESERVED.1` | `IsSettlementLogHist_Reserved1` |  |  |  |
