# FX.AGREEMENT.TYPE — Table Schema

> Source: `INSERTS/I_F.FX.AGREEMENT.TYPE` in `FX_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FX.AGR.TYP.DESCRIPTION` | `FxAgreementType_Description` |  |  |  |
| 2 | `FX.AGR.TYP.LOCAL.REF` | `FxAgreementType_LocalRef` |  |  |  |
| 3 | `FX.AGR.TYP.RESERVED.5` | `FxAgreementType_Reserved5` | TField |  |  |
| 4 | `FX.AGR.TYP.RESERVED.4` | `FxAgreementType_Reserved4` | TField |  |  |
| 5 | `FX.AGR.TYP.RESERVED.3` | `FxAgreementType_Reserved3` | TField |  |  |
| 6 | `FX.AGR.TYP.RESERVED.2` | `FxAgreementType_Reserved2` | TField |  |  |
| 7 | `FX.AGR.TYP.RESERVED.1` | `FxAgreementType_Reserved1` | TField |  |  |
| 8 | `FX.AGR.TYP.RECORD.STATUS` | `FxAgreementType_RecordStatus` | String |  |  |
| 9 | `FX.AGR.TYP.CURR.NO` | `FxAgreementType_CurrNo` | String |  |  |
| 10 | `FX.AGR.TYP.INPUTTER` | `FxAgreementType_Inputter` |  |  |  |
| 11 | `FX.AGR.TYP.DATE.TIME` | `FxAgreementType_DateTime` |  |  |  |
| 12 | `FX.AGR.TYP.AUTHORISER` | `FxAgreementType_Authoriser` | String |  |  |
| 13 | `FX.AGR.TYP.CO.CODE` | `FxAgreementType_CoCode` | String |  |  |
| 14 | `FX.AGR.TYP.DEPT.CODE` | `FxAgreementType_DeptCode` | String |  |  |
| 15 | `FX.AGR.TYP.AUDITOR.CODE` | `FxAgreementType_AuditorCode` | String |  |  |
| 16 | `FX.AGR.TYP.AUDIT.DATE.TIME` | `FxAgreementType_AuditDateTime` | String |  |  |
