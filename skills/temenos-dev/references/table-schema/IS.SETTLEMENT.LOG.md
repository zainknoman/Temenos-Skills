# IS.SETTLEMENT.LOG — Table Schema

> Source: `INSERTS/I_F.IS.SETTLEMENT.LOG` in `IS_Payment.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.SEL.CUSTOMER` | `IsSettlementLog_Customer` | TField |  | Customer id of the arrangement. |
| 2 | `IS.SEL.DATE` | `IsSettlementLog_Date` | TField |  | Date of repayment to the arrangement is made. |
| 3 | `IS.SEL.SETTLEMENT.TYPE` | `IsSettlementLog_SettlementType` | TField |  | This field displays the type of settlement is done in the arrangement. Ex:Repayment. |
| 4 | `IS.SEL.ARRANGEMENT.REF` | `IsSettlementLog_ArrangementRef` | TField |  | AA arrangement id |
| 5 | `IS.SEL.TRANS.REFERENCE` | `IsSettlementLog_TransReference` |  |  |  |
| 6 | `IS.SEL.EXPECTED.AMOUNT` | `IsSettlementLog_ExpectedAmount` |  |  |  |
| 7 | `IS.SEL.ACTUAL.AMOUNT` | `IsSettlementLog_ActualAmount` |  |  |  |
| 8 | `IS.SEL.RESERVED.5` | `IsSettlementLog_Reserved5` |  |  |  |
| 9 | `IS.SEL.RESERVED.4` | `IsSettlementLog_Reserved4` |  |  |  |
| 10 | `IS.SEL.RESERVED.3` | `IsSettlementLog_Reserved3` |  |  |  |
| 11 | `IS.SEL.RESERVED.2` | `IsSettlementLog_Reserved2` |  |  |  |
| 12 | `IS.SEL.RESERVED.1` | `IsSettlementLog_Reserved1` |  |  |  |
