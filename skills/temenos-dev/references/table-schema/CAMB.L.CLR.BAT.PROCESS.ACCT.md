# CAMB.L.CLR.BAT.PROCESS.ACCT — Table Schema

> Source: `INSERTS/I_F.CAMB.L.CLR.BAT.PROCESS.ACCT` in `CACSIT_CoverdraftSweep.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CWB.CBPA.TRANS.DATE` | `CwbLClrBatProcessAcct_TransDate` |  |  |  |
| 2 | `CWB.CBPA.ACCT.NATURE` | `CwbLClrBatProcessAcct_AcctNature` |  |  |  |
| 3 | `CWB.CBPA.RESERVED.10` | `CwbLClrBatProcessAcct_Reserved10` |  |  |  |
| 4 | `CWB.CBPA.RESERVED.9` | `CwbLClrBatProcessAcct_Reserved9` |  |  |  |
| 5 | `CWB.CBPA.RESERVED.8` | `CwbLClrBatProcessAcct_Reserved8` |  |  |  |
| 6 | `CWB.CBPA.RESERVED.7` | `CwbLClrBatProcessAcct_Reserved7` |  |  |  |
| 7 | `CWB.CBPA.RESERVED.6` | `CwbLClrBatProcessAcct_Reserved6` |  |  |  |
| 8 | `CWB.CBPA.RESERVED.5` | `CwbLClrBatProcessAcct_Reserved5` |  |  |  |
| 9 | `CWB.CBPA.RESERVED.4` | `CwbLClrBatProcessAcct_Reserved4` |  |  |  |
| 10 | `CWB.CBPA.RESERVED.3` | `CwbLClrBatProcessAcct_Reserved3` |  |  |  |
| 11 | `CWB.CBPA.RESERVED.2` | `CwbLClrBatProcessAcct_Reserved2` |  |  |  |
| 12 | `CWB.CBPA.RESERVED.1` | `CwbLClrBatProcessAcct_Reserved1` |  |  |  |
