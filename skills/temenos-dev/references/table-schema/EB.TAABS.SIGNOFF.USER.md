# EB.TAABS.SIGNOFF.USER — Table Schema

> Source: `INSERTS/I_F.EB.TAABS.SIGNOFF.USER` in `EB_ProductConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.TSOU.PACKAGE.NAME` | `EbTaabsSignoffUser_PackageName` |  |  |  |
| 2 | `EB.TSOU.LOCAL.REF` | `EbTaabsSignoffUser_LocalRef` |  |  |  |
| 3 | `EB.TSOU.OVERRIDE` | `EbTaabsSignoffUser_Override` |  |  |  |
| 4 | `EB.TSOU.RECORD.STATUS` | `EbTaabsSignoffUser_RecordStatus` | String |  |  |
| 5 | `EB.TSOU.CURR.NO` | `EbTaabsSignoffUser_CurrNo` | String |  |  |
| 6 | `EB.TSOU.INPUTTER` | `EbTaabsSignoffUser_Inputter` |  |  |  |
| 7 | `EB.TSOU.DATE.TIME` | `EbTaabsSignoffUser_DateTime` |  |  |  |
| 8 | `EB.TSOU.AUTHORISER` | `EbTaabsSignoffUser_Authoriser` | String |  |  |
| 9 | `EB.TSOU.CO.CODE` | `EbTaabsSignoffUser_CoCode` | String |  |  |
| 10 | `EB.TSOU.DEPT.CODE` | `EbTaabsSignoffUser_DeptCode` | String |  |  |
| 11 | `EB.TSOU.AUDITOR.CODE` | `EbTaabsSignoffUser_AuditorCode` | String |  |  |
| 12 | `EB.TSOU.AUDIT.DATE.TIME` | `EbTaabsSignoffUser_AuditDateTime` | String |  |  |
