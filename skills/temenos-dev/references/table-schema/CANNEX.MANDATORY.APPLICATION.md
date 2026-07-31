# CANNEX.MANDATORY.APPLICATION — Table Schema

> Source: `INSERTS/I_F.CANNEX.MANDATORY.APPLICATION` in `CACANN_CannexDeposits.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CNX.MAN.APP.APPLICATION` | `CannexMandatoryApplication_Application` |  |  |  |
| 2 | `CNX.MAN.APP.FIELD.NAME` | `CannexMandatoryApplication_FieldName` |  |  |  |
| 3 | `CNX.MAN.APP.LOCAL.REF` | `CannexMandatoryApplication_LocalRef` |  |  |  |
| 4 | `CNX.MAN.APP.OVERRIDE` | `CannexMandatoryApplication_Override` |  |  |  |
| 5 | `CNX.MAN.APP.RECORD.STATUS` | `CannexMandatoryApplication_RecordStatus` | String |  |  |
| 6 | `CNX.MAN.APP.CURR.NO` | `CannexMandatoryApplication_CurrNo` | String |  |  |
| 7 | `CNX.MAN.APP.INPUTTER` | `CannexMandatoryApplication_Inputter` |  |  |  |
| 8 | `CNX.MAN.APP.DATE.TIME` | `CannexMandatoryApplication_DateTime` |  |  |  |
| 9 | `CNX.MAN.APP.AUTHORISER` | `CannexMandatoryApplication_Authoriser` | String |  |  |
| 10 | `CNX.MAN.APP.CO.CODE` | `CannexMandatoryApplication_CoCode` | String |  |  |
| 11 | `CNX.MAN.APP.DEPT.CODE` | `CannexMandatoryApplication_DeptCode` | String |  |  |
| 12 | `CNX.MAN.APP.AUDITOR.CODE` | `CannexMandatoryApplication_AuditorCode` | String |  |  |
| 13 | `CNX.MAN.APP.AUDIT.DATE.TIME` | `CannexMandatoryApplication_AuditDateTime` | String |  |  |
