# ACFA.TYPE — Table Schema

> Source: `INSERTS/I_F.ACFA.TYPE` in `AC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACFA.TYP.DESCRIPTION` | `AcfaType_Description` |  |  |  |
| 2 | `ACFA.TYP.UPDATE.ACTIVATION.FILE` | `AcfaType_UpdateActivationFile` | TField |  | Field to indicate if BAL.CHK.LISTENER.ACTIVATION has to be updated or not. Validation Rules: Allowed values are Y/NO/Null/EXTERNAL/BUSINESS.EVENT. If NULL/YES, the file will be updated. EXTERNAL option will enable system to emit event when underlying record is authorised. BUSINESS.EVENT-When set a first class business event will be emitted when the ACFA is authorised. |
| 3 | `ACFA.TYP.DDA.FUNDS.CHECK` | `AcfaType_DdaFundsCheck` | TField |  | Field to indicate if funds check has to be performed for the transaction. Validation Rules: Allowed values are Y/NO/Null. If NULL/YES, funds check will be performed |
| 4 | `ACFA.TYP.ALLOWED.FUNDS.DECISION` | `AcfaType_AllowedFundsDecision` |  |  |  |
| 5 | `ACFA.TYP.ALLOWED.RESERVATION` | `AcfaType_AllowedReservation` | TField |  | Field to indicate if funds has to be reserved. Validation Rules: Allowed values are Y/NO/Null/Auth-only. If NULL/YES, funds will be reserved. When Allowed reservation is Auth-only, then reservation will happen in AUTH stage and AC.LOCKED.EVENTS will be raised only during authorization of ACFA. |
| 6 | `ACFA.TYP.ALLOWED.APPROVAL.CODE` | `AcfaType_AllowedApprovalCode` |  |  |  |
| 7 | `ACFA.TYP.RETENTION.PERIOD` | `AcfaType_RetentionPeriod` | TField |  | Defines for how many days AC.FUNDS.AUTHORISATION records with FUND.AUTH.STATUS as 'AUTHORISED', 'BOOKED' and 'CANCELLED' will remain in live. Validation Rule: Input allowed only for id as DEFAULT. Number of days till 99 can be defined with either C or W denoting calendar and working days respectively e.g., 5C or 5W. If only number of days is input then it will be assumed as calendar days. |
| 8 | `ACFA.TYP.RESERVED.4` | `AcfaType_Reserved4` | TField |  | Reserved field for future use. Validation Rule: Live table. No Input |
| 9 | `ACFA.TYP.RESERVED.3` | `AcfaType_Reserved3` | TField |  | Reserved field for future use. Validation Rule: Live table. No Input |
| 10 | `ACFA.TYP.RESERVED.2` | `AcfaType_Reserved2` | TField |  | Reserved field for future use. Validation Rule: Live table. No Input |
| 11 | `ACFA.TYP.RESERVED.1` | `AcfaType_Reserved1` | TField |  | Reserved field for future use. Validation Rule: Live table. No Input |
| 12 | `ACFA.TYP.LOCAL.REF` | `AcfaType_LocalRef` |  |  |  |
| 13 | `ACFA.TYP.OVERRIDE` | `AcfaType_Override` |  |  |  |
| 14 | `ACFA.TYP.RECORD.STATUS` | `AcfaType_RecordStatus` | String |  |  |
| 15 | `ACFA.TYP.CURR.NO` | `AcfaType_CurrNo` | String |  | It's the Curr number of the record. Validation Rule: Numeric value Live table - No input field |
| 16 | `ACFA.TYP.INPUTTER` | `AcfaType_Inputter` |  |  |  |
| 17 | `ACFA.TYP.DATE.TIME` | `AcfaType_DateTime` |  |  |  |
| 18 | `ACFA.TYP.AUTHORISER` | `AcfaType_Authoriser` | String |  | It denotes the Authoriser of the record. Validation Rule: Valid user ID Live table - No input field |
| 19 | `ACFA.TYP.CO.CODE` | `AcfaType_CoCode` | String |  | This is an I-Descriptor field. Holds the Company code value. |
| 20 | `ACFA.TYP.DEPT.CODE` | `AcfaType_DeptCode` | String |  |  |
| 21 | `ACFA.TYP.AUDITOR.CODE` | `AcfaType_AuditorCode` | String |  |  |
| 22 | `ACFA.TYP.AUDIT.DATE.TIME` | `AcfaType_AuditDateTime` | String |  |  |
