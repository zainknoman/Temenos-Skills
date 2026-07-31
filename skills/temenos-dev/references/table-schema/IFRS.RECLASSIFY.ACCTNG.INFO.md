# IFRS.RECLASSIFY.ACCTNG.INFO — Table Schema

> Source: `INSERTS/I_F.IFRS.RECLASSIFY.ACCTNG.INFO` in `IA_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IFRS.RE.AC.INF.RECLASSIFICATION.DATE` | `IfrsReclassifyAcctngInfo_ReclassificationDate` |  |  |  |
| 2 | `IFRS.RE.AC.INF.PREV.IFRS.CLASSIFICATION` | `IfrsReclassifyAcctngInfo_PrevIfrsClassification` |  |  |  |
| 3 | `IFRS.RE.AC.INF.PREV.IAS.SUB.TYPE` | `IfrsReclassifyAcctngInfo_PrevIasSubType` |  |  |  |
| 4 | `IFRS.RE.AC.INF.ACCTNG.HEAD` | `IfrsReclassifyAcctngInfo_AcctngHead` |  |  |  |
| 5 | `IFRS.RE.AC.INF.AMOUNT` | `IfrsReclassifyAcctngInfo_Amount` |  |  |  |
