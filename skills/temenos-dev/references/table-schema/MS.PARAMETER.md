# MS.PARAMETER — Table Schema

> Source: `INSERTS/I_F.MS.PARAMETER` in `ST_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MS.PAR.ACCOUNTING.MODE` | `MsParameter_AccountingMode` | TField |  | Field to decide the Accounting mode for Microservice. Validation rules: Option Field - EXTERNAL/NULL. EXTERNAL - Accounting will be performed in external system. NULL - Accounting will be performed in internal system No change field. Once it is set to EXTERNAL or NULL, accounting will be performed accordingly and it will not be changed again. |
| 2 | `MS.PAR.MOVEMENT.SUPPRESS` | `MsParameter_MovementSuppress` | TField |  | Field to indicate whether accounting entries needs to be update in External accounting mode. Validation rules: Option Field - YES/NO/NULL. YES - Accounting entries will not raised for external accounting mode. NO/NULL - Accounting entries will not raised for external accounting mode. Input allowed only for EXTERNAL accounting mode. No change field. Currently, movements are suppressed for external accounting mode and options to decide movement suppress will be released in future. |
| 3 | `MS.PAR.SYSTEM.IDENTIFIER` | `MsParameter_SystemIdentifier` | TField | Yes | Field used to prefix the arrangement id to form a unique identifier in External GL system. Example: SYSTEM.IDENTIFIER is set as ALMS and a lending arrangement created with id AAACT2007609T14T4Q in the current system. It will be reported as ALMSAAACT2007609T14T4Q in external GL transact system. Each contract id will be prefixed with system identifier in the external system. Validation rules: A maximum of 4 characters may be entered. Input allowed only for EXTERNAL accounting mode. No change field. Mandatory field for external accounting. |
| 4 | `MS.PAR.AA.TRANSACT.MICROSERVICE` | `MsParameter_AaTransactMicroservice` | TField |  | Field to indicate that the arrangement product(Lending/Deposits/Accounts) running as a Microservice. Validation rules: Option Field - YES/NO/NULL. YES - Indicates the arrangement Microservice environment. Input allowed only for EXTERNAL accounting mode. |
| 5 | `MS.PAR.LIMIT.SYSTEM` | `MsParameter_LimitSystem` | TField |  |  |
| 6 | `MS.PAR.EXTERNAL.SYSTEM` | `MsParameter_ExternalSystem` | TField |  |  |
| 7 | `MS.PAR.USE.BANK.REFERENCE.DATA` | `MsParameter_UseBankReferenceData` | TField |  |  |
| 8 | `MS.PAR.USE.IBAN.REFERENCE.DATA` | `MsParameter_UseIbanReferenceData` | TField |  | Value YES is allowed only when Reference system is external Validation rules: Option Field - NULL/YES. Default value is NULL |
| 9 | `MS.PAR.EMIT.BUSINESS.EVENT` | `MsParameter_EmitBusinessEvent` | TField |  | Indicates if the first class business events must be emitted from the system Valid options: YES - Indicates first class business event will be emitted in the system NULL - Indicates first class business event will not be emitted in the system |
| 10 | `MS.PAR.LOCAL.REF` | `MsParameter_LocalRef` |  |  |  |
| 11 | `MS.PAR.OVERRIDE` | `MsParameter_Override` |  |  |  |
| 12 | `MS.PAR.RECORD.STATUS` | `MsParameter_RecordStatus` | String |  |  |
| 13 | `MS.PAR.CURR.NO` | `MsParameter_CurrNo` | String |  |  |
| 14 | `MS.PAR.INPUTTER` | `MsParameter_Inputter` |  |  |  |
| 15 | `MS.PAR.DATE.TIME` | `MsParameter_DateTime` |  |  |  |
| 16 | `MS.PAR.AUTHORISER` | `MsParameter_Authoriser` | String |  |  |
| 17 | `MS.PAR.CO.CODE` | `MsParameter_CoCode` | String |  |  |
| 18 | `MS.PAR.DEPT.CODE` | `MsParameter_DeptCode` | String |  |  |
| 19 | `MS.PAR.AUDITOR.CODE` | `MsParameter_AuditorCode` | String |  |  |
| 20 | `MS.PAR.AUDIT.DATE.TIME` | `MsParameter_AuditDateTime` | String |  |  |
| 21 | `MS.PAR.TBC.TYPE` | `MsParameter_TbcType` |  |  |  |
