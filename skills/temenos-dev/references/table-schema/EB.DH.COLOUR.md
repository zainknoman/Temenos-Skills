# EB.DH.COLOUR — Table Schema

> Source: `INSERTS/I_F.EB.DH.COLOUR` in `CACQOR_ChequeOrdering.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.DH.86.COLOUR` | `EbDhColour_Colour` |  |  |  |
| 2 | `EB.DH.86.RECORD.STATUS` | `EbDhColour_RecordStatus` |  |  |  |
| 3 | `EB.DH.86.CURR.NO` | `EbDhColour_CurrNo` |  |  |  |
| 4 | `EB.DH.86.INPUTTER` | `EbDhColour_Inputter` |  |  |  |
| 5 | `EB.DH.86.DATE.TIME` | `EbDhColour_DateTime` |  |  |  |
| 6 | `EB.DH.86.AUTHORISER` | `EbDhColour_Authoriser` |  |  |  |
| 7 | `EB.DH.86.CO.CODE` | `EbDhColour_CoCode` |  |  |  |
| 8 | `EB.DH.86.DEPT.CODE` | `EbDhColour_DeptCode` |  |  |  |
| 9 | `EB.DH.86.AUDITOR.CODE` | `EbDhColour_AuditorCode` |  |  |  |
| 10 | `EB.DH.86.AUDIT.DATE.TIME` | `EbDhColour_AuditDateTime` |  |  |  |
