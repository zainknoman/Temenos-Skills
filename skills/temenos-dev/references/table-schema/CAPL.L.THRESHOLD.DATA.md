# CAPL.L.THRESHOLD.DATA — Table Schema

> Source: `INSERTS/I_F.CAPL.L.THRESHOLD.DATA` in `CAATMI_EverlinkATMInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.THLD.TXN.REF` | `CaplLThresholdData_TxnRef` |  |  |  |
| 2 | `CAPL.THLD.TXN.AMT` | `CaplLThresholdData_TxnAmt` |  |  |  |
| 3 | `CAPL.THLD.TXN.CCY` | `CaplLThresholdData_TxnCcy` |  |  |  |
| 4 | `CAPL.THLD.CR.ACCOUNT` | `CaplLThresholdData_CrAccount` |  |  |  |
| 5 | `CAPL.THLD.LOCK.REF.ID` | `CaplLThresholdData_LockRefId` |  |  |  |
| 6 | `CAPL.THLD.TOT.AMOUNT` | `CaplLThresholdData_TotAmount` |  |  |  |
| 7 | `CAPL.THLD.TOT.AMOUNT.LCY` | `CaplLThresholdData_TotAmountLcy` |  |  |  |
| 8 | `CAPL.THLD.RESERVED.4` | `CaplLThresholdData_Reserved4` |  |  |  |
| 9 | `CAPL.THLD.RESERVED.3` | `CaplLThresholdData_Reserved3` |  |  |  |
| 10 | `CAPL.THLD.RESERVED.2` | `CaplLThresholdData_Reserved2` |  |  |  |
| 11 | `CAPL.THLD.RESERVED.1` | `CaplLThresholdData_Reserved1` |  |  |  |
