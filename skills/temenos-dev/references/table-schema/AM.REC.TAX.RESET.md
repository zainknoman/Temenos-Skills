# AM.REC.TAX.RESET — Table Schema

> Source: `INSERTS/I_F.AM.REC.TAX.RESET` in `AM_RecoverableTax.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `REC.TX.RESET.FREQ` | `AmRecTaxReset_ResetFreq` |  |  |  |
| 2 | `REC.TX.PORT.CRIT.ID` | `AmRecTaxReset_PortCritId` |  |  |  |
| 3 | `REC.TX.INSTR.CRIT.ID` | `AmRecTaxReset_InstrCritId` |  |  |  |
| 4 | `REC.TX.RECORD.STATUS` | `AmRecTaxReset_RecordStatus` | String |  |  |
| 5 | `REC.TX.CURR.NO` | `AmRecTaxReset_CurrNo` | String |  |  |
| 6 | `REC.TX.INPUTTER` | `AmRecTaxReset_Inputter` |  |  |  |
| 7 | `REC.TX.DATE.TIME` | `AmRecTaxReset_DateTime` |  |  |  |
| 8 | `REC.TX.AUTHORISER` | `AmRecTaxReset_Authoriser` | String |  |  |
| 9 | `REC.TX.CO.CODE` | `AmRecTaxReset_CoCode` | String |  |  |
| 10 | `REC.TX.DEPT.CODE` | `AmRecTaxReset_DeptCode` | String |  |  |
| 11 | `REC.TX.AUDITOR.CODE` | `AmRecTaxReset_AuditorCode` | String |  |  |
| 12 | `REC.TX.AUDIT.DATE.TIME` | `AmRecTaxReset_AuditDateTime` | String |  |  |
