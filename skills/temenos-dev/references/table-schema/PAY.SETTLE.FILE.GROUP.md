# PAY.SETTLE.FILE.GROUP — Table Schema

> Source: `INSERTS/I_F.PAY.SETTLE.FILE.GROUP` in `CAEFPA_EFTPap.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAMB.PAY.MAIN.COMPANY` | `PaySettleFileGroup_MainCompany` |  |  |  |
| 2 | `CAMB.PAY.GROUP.COMPANY` | `PaySettleFileGroup_GroupCompany` |  |  |  |
| 3 | `CAMB.PAY.RECORD.STATUS` | `PaySettleFileGroup_RecordStatus` |  |  |  |
| 4 | `CAMB.PAY.CURR.NO` | `PaySettleFileGroup_CurrNo` |  |  |  |
| 5 | `CAMB.PAY.INPUTTER` | `PaySettleFileGroup_Inputter` |  |  |  |
| 6 | `CAMB.PAY.DATE.TIME` | `PaySettleFileGroup_DateTime` |  |  |  |
| 7 | `CAMB.PAY.AUTHORISER` | `PaySettleFileGroup_Authoriser` |  |  |  |
| 8 | `CAMB.PAY.CO.CODE` | `PaySettleFileGroup_CoCode` |  |  |  |
| 9 | `CAMB.PAY.DEPT.CODE` | `PaySettleFileGroup_DeptCode` |  |  |  |
| 10 | `CAMB.PAY.AUDITOR.CODE` | `PaySettleFileGroup_AuditorCode` |  |  |  |
| 11 | `CAMB.PAY.AUDIT.DATE.TIME` | `PaySettleFileGroup_AuditDateTime` |  |  |  |
