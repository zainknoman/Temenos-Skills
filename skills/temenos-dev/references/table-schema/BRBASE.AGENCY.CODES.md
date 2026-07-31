# BRBASE.AGENCY.CODES — Table Schema

> Source: `INSERTS/I_F.BRBASE.AGENCY.CODES` in `BRBASE_InterfaceConnector.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AGENCY.CODE.AGENCY.NAME` | `BrbaseAgencyCodes_AgencyName` | TField |  | Contains the Name of the Agency(Branch). |
| 2 | `AGENCY.CODE.LOCAL.REF` | `BrbaseAgencyCodes_LocalRef` |  |  |  |
| 3 | `AGENCY.CODE.OVERRIDE` | `BrbaseAgencyCodes_Override` |  |  |  |
| 4 | `AGENCY.CODE.RECORD.STATUS` | `BrbaseAgencyCodes_RecordStatus` | String |  |  |
| 5 | `AGENCY.CODE.CURR.NO` | `BrbaseAgencyCodes_CurrNo` | String |  |  |
| 6 | `AGENCY.CODE.INPUTTER` | `BrbaseAgencyCodes_Inputter` |  |  |  |
| 7 | `AGENCY.CODE.DATE.TIME` | `BrbaseAgencyCodes_DateTime` |  |  |  |
| 8 | `AGENCY.CODE.AUTHORISER` | `BrbaseAgencyCodes_Authoriser` | String |  |  |
| 9 | `AGENCY.CODE.CO.CODE` | `BrbaseAgencyCodes_CoCode` | String |  |  |
| 10 | `AGENCY.CODE.DEPT.CODE` | `BrbaseAgencyCodes_DeptCode` | String |  |  |
| 11 | `AGENCY.CODE.AUDITOR.CODE` | `BrbaseAgencyCodes_AuditorCode` | String |  |  |
| 12 | `AGENCY.CODE.AUDIT.DATE.TIME` | `BrbaseAgencyCodes_AuditDateTime` | String |  |  |
