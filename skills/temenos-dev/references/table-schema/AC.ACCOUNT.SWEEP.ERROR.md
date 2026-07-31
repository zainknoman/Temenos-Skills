# AC.ACCOUNT.SWEEP.ERROR — Table Schema

> Source: `INSERTS/I_F.AC.ACCOUNT.SWEEP.ERROR` in `ST_Sweeping.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SWP.ERR.EXEC.DATE` | `AcAccountSweepError_ExecDate` | TField |  |  |
| 2 | `SWP.ERR.DR.ACCT.NO` | `AcAccountSweepError_DrAcctNo` | TField |  |  |
| 3 | `SWP.ERR.CR.ACCT.NO` | `AcAccountSweepError_CrAcctNo` | TField |  |  |
| 4 | `SWP.ERR.SWEEP.AMT` | `AcAccountSweepError_SweepAmt` | TField |  |  |
| 5 | `SWP.ERR.SWEEP.ID` | `AcAccountSweepError_SweepId` | TField |  |  |
| 6 | `SWP.ERR.SWEEP.TYPE` | `AcAccountSweepError_SweepType` | TField |  |  |
| 7 | `SWP.ERR.REJ.REASON` | `AcAccountSweepError_RejReason` |  |  |  |
