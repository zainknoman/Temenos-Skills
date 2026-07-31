# CAMB.AC.ONLINE.CLOSURE — Table Schema

> Source: `INSERTS/I_F.CAMB.AC.ONLINE.CLOSURE` in `CARGPL_RegisteredPlans.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CCSAC.ACCT.CLOSE.DATE` | `CambAcOnlineClosure_AcctCloseDate` |  |  |  |
| 2 | `CCSAC.CAP.ACCT` | `CambAcOnlineClosure_CapAcct` |  |  |  |
| 3 | `CCSAC.OFS.TXN.ID` | `CambAcOnlineClosure_OfsTxnId` |  |  |  |
| 4 | `CCSAC.OFS.ERROR` | `CambAcOnlineClosure_OfsError` |  |  |  |
| 5 | `CCSAC.STATUS` | `CambAcOnlineClosure_Status` |  |  |  |
| 6 | `CCSAC.STATUS.GROUP` | `CambAcOnlineClosure_StatusGroup` |  |  |  |
| 7 | `CCSAC.CUSTOMER` | `CambAcOnlineClosure_Customer` |  |  |  |
| 8 | `CCSAC.RESERVED.3` | `CambAcOnlineClosure_Reserved3` |  |  |  |
| 9 | `CCSAC.RESERVED.2` | `CambAcOnlineClosure_Reserved2` |  |  |  |
| 10 | `CCSAC.RESERVED.1` | `CambAcOnlineClosure_Reserved1` |  |  |  |
| 11 | `CCSAC.LOCAL.REF` | `CambAcOnlineClosure_LocalRef` |  |  |  |
