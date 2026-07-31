# EB.MANDATE.APPLICATION.GROUP — Table Schema

> Source: `INSERTS/I_F.EB.MANDATE.APPLICATION.GROUP` in `EB_Mandate.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.MAND.GRP.MANDATE.APPL` | `EbMandateApplicationGroup_MandateAppl` |  |  |  |
| 2 | `EB.MAND.GRP.MANDATE.REG` | `EbMandateApplicationGroup_MandateReg` |  |  |  |
| 3 | `EB.MAND.GRP.LOCAL.REF` | `EbMandateApplicationGroup_LocalRef` |  |  |  |
| 4 | `EB.MAND.GRP.OVERRIDE` | `EbMandateApplicationGroup_Override` |  |  |  |
| 5 | `EB.MAND.GRP.RECORD.STATUS` | `EbMandateApplicationGroup_RecordStatus` | String |  |  |
| 6 | `EB.MAND.GRP.CURR.NO` | `EbMandateApplicationGroup_CurrNo` | String |  |  |
| 7 | `EB.MAND.GRP.INPUTTER` | `EbMandateApplicationGroup_Inputter` |  |  |  |
| 8 | `EB.MAND.GRP.DATE.TIME` | `EbMandateApplicationGroup_DateTime` |  |  |  |
| 9 | `EB.MAND.GRP.AUTHORISER` | `EbMandateApplicationGroup_Authoriser` | String |  |  |
| 10 | `EB.MAND.GRP.CO.CODE` | `EbMandateApplicationGroup_CoCode` | String |  |  |
| 11 | `EB.MAND.GRP.DEPT.CODE` | `EbMandateApplicationGroup_DeptCode` | String |  |  |
| 12 | `EB.MAND.GRP.AUDITOR.CODE` | `EbMandateApplicationGroup_AuditorCode` | String |  |  |
| 13 | `EB.MAND.GRP.AUDIT.DATE.TIME` | `EbMandateApplicationGroup_AuditDateTime` | String |  |  |
