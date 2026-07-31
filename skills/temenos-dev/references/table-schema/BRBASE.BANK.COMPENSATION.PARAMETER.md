# BRBASE.BANK.COMPENSATION.PARAMETER — Table Schema

> Source: `INSERTS/I_F.BRBASE.BANK.COMPENSATION.PARAMETER` in `BRBASE_InterfaceConnector.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COM.PARAM.BANK.COMMERCIAL.NAME` | `BrbaseBankCompensationParameter_BankCommercialName` |  |  |  |
| 2 | `COM.PARAM.BANK.FULL.NAME` | `BrbaseBankCompensationParameter_BankFullName` |  |  |  |
| 3 | `COM.PARAM.ISPB.CODE` | `BrbaseBankCompensationParameter_IspbCode` | TField |  | Contains the Numeric ID of the ISPB code of the Bank. |
| 4 | `COM.PARAM.LOCAL.REF` | `BrbaseBankCompensationParameter_LocalRef` |  |  |  |
| 5 | `COM.PARAM.OVERRIDE` | `BrbaseBankCompensationParameter_Override` |  |  |  |
| 6 | `COM.PARAM.RECORD.STATUS` | `BrbaseBankCompensationParameter_RecordStatus` | String |  |  |
| 7 | `COM.PARAM.CURR.NO` | `BrbaseBankCompensationParameter_CurrNo` | String |  |  |
| 8 | `COM.PARAM.INPUTTER` | `BrbaseBankCompensationParameter_Inputter` |  |  |  |
| 9 | `COM.PARAM.DATE.TIME` | `BrbaseBankCompensationParameter_DateTime` |  |  |  |
| 10 | `COM.PARAM.AUTHORISER` | `BrbaseBankCompensationParameter_Authoriser` | String |  |  |
| 11 | `COM.PARAM.CO.CODE` | `BrbaseBankCompensationParameter_CoCode` | String |  |  |
| 12 | `COM.PARAM.DEPT.CODE` | `BrbaseBankCompensationParameter_DeptCode` | String |  |  |
| 13 | `COM.PARAM.AUDITOR.CODE` | `BrbaseBankCompensationParameter_AuditorCode` | String |  |  |
| 14 | `COM.PARAM.AUDIT.DATE.TIME` | `BrbaseBankCompensationParameter_AuditDateTime` | String |  |  |
