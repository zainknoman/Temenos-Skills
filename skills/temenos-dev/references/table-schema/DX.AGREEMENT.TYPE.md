# DX.AGREEMENT.TYPE — Table Schema

> Source: `INSERTS/I_F.DX.AGREEMENT.TYPE` in `DX_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DX.AGR.TYP.DESCRIPTION` | `DxAgreementType_Description` |  |  |  |
| 2 | `DX.AGR.TYP.LOCAL.REF` | `DxAgreementType_LocalRef` |  |  |  |
| 3 | `DX.AGR.TYP.RESERVED.5` | `DxAgreementType_Reserved5` | TField |  |  |
| 4 | `DX.AGR.TYP.RESERVED.4` | `DxAgreementType_Reserved4` | TField |  |  |
| 5 | `DX.AGR.TYP.RESERVED.3` | `DxAgreementType_Reserved3` | TField |  |  |
| 6 | `DX.AGR.TYP.RESERVED.2` | `DxAgreementType_Reserved2` | TField |  |  |
| 7 | `DX.AGR.TYP.RESERVED.1` | `DxAgreementType_Reserved1` | TField |  |  |
| 8 | `DX.AGR.TYP.RECORD.STATUS` | `DxAgreementType_RecordStatus` | String |  |  |
| 9 | `DX.AGR.TYP.CURR.NO` | `DxAgreementType_CurrNo` | String |  |  |
| 10 | `DX.AGR.TYP.INPUTTER` | `DxAgreementType_Inputter` |  |  |  |
| 11 | `DX.AGR.TYP.DATE.TIME` | `DxAgreementType_DateTime` |  |  |  |
| 12 | `DX.AGR.TYP.AUTHORISER` | `DxAgreementType_Authoriser` | String |  |  |
| 13 | `DX.AGR.TYP.CO.CODE` | `DxAgreementType_CoCode` | String |  |  |
| 14 | `DX.AGR.TYP.DEPT.CODE` | `DxAgreementType_DeptCode` | String |  |  |
| 15 | `DX.AGR.TYP.AUDITOR.CODE` | `DxAgreementType_AuditorCode` | String |  |  |
| 16 | `DX.AGR.TYP.AUDIT.DATE.TIME` | `DxAgreementType_AuditDateTime` | String |  |  |
