# EM.L.EMAIL.MSG.PROCESSED — Table Schema

> Source: `INSERTS/I_F.EM.L.EMAIL.MSG.PROCESSED` in `CACLRC_ClearingCentralOne.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EM.S.TO.EMAIL.ID` | `EmLEmailMsgProcessed_ToEmailId` |  |  |  |
| 2 | `EM.S.ACCT.NUM` | `EmLEmailMsgProcessed_AcctNum` |  |  |  |
