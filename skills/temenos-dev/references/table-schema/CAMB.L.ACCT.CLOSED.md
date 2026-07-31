# CAMB.L.ACCT.CLOSED — Table Schema

> Source: `INSERTS/I_F.CAMB.L.ACCT.CLOSED` in `CAPLND_ProlenderInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.AC.CLS.ACCOUNT.ID` | `CambLAcctClosed_AccountId` |  |  |  |
| 2 | `CAMB.AC.CLS.PROD.LINE` | `CambLAcctClosed_ProdLine` |  |  |  |
| 3 | `CAMB.AC.CLS.DATE` | `CambLAcctClosed_Date` |  |  |  |
