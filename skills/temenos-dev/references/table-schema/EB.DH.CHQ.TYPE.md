# EB.DH.CHQ.TYPE — Table Schema

> Source: `INSERTS/I_F.EB.DH.CHQ.TYPE` in `CACQOR_ChequeOrdering.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.DH.13.DESCRIPTION` | `EbDhChqType_Description` |  |  |  |
| 2 | `EB.DH.13.RECORD.STATUS` | `EbDhChqType_RecordStatus` |  |  |  |
| 3 | `EB.DH.13.CURR.NO` | `EbDhChqType_CurrNo` |  |  |  |
| 4 | `EB.DH.13.INPUTTER` | `EbDhChqType_Inputter` |  |  |  |
| 5 | `EB.DH.13.DATE.TIME` | `EbDhChqType_DateTime` |  |  |  |
| 6 | `EB.DH.13.AUTHORISER` | `EbDhChqType_Authoriser` |  |  |  |
| 7 | `EB.DH.13.CO.CODE` | `EbDhChqType_CoCode` |  |  |  |
| 8 | `EB.DH.13.DEPT.CODE` | `EbDhChqType_DeptCode` |  |  |  |
| 9 | `EB.DH.13.AUDITOR.CODE` | `EbDhChqType_AuditorCode` |  |  |  |
| 10 | `EB.DH.13.AUDIT.DATE.TIME` | `EbDhChqType_AuditDateTime` |  |  |  |
