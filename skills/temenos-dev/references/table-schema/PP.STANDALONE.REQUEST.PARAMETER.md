# PP.STANDALONE.REQUEST.PARAMETER — Table Schema

> Source: `INSERTS/I_F.PP.STANDALONE.REQUEST.PARAMETER` in `PP_PaymentWorkflowGUI.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPSRP.DebitAccValidationRequest` | `PpStandaloneRequestParameter_Debitaccvalidationrequest` | TField |  | Hold Mapping record ID ( ID of PP.STANDALONE.REQUEST.MAPPING) which needs to used while sending debit account validation request. |
| 2 | `PPSRP.CreditAccValidationRequest` | `PpStandaloneRequestParameter_Creditaccvalidationrequest` | TField |  | Hold Mapping record ID ( ID of PP.STANDALONE.REQUEST.MAPPING) which needs to used while sending credit account validation request. |
| 3 | `PPSRP.DebitChgAccValidationRequest` | `PpStandaloneRequestParameter_Debitchgaccvalidationrequest` | TField |  | Hold Mapping record ID ( ID of PP.STANDALONE.REQUEST.MAPPING) which needs to used while sending debit charge account validation request. |
| 4 | `PPSRP.CreditChgAccValidationRequest` | `PpStandaloneRequestParameter_Creditchgaccvalidationrequest` | TField |  | Hold Mapping record ID ( ID of PP.STANDALONE.REQUEST.MAPPING) which needs to used while sending credit charge account validation request. |
| 5 | `PPSRP.FundsReserveRequest` | `PpStandaloneRequestParameter_Fundsreserverequest` | TField |  | Hold Mapping record ID ( ID of PP.STANDALONE.REQUEST.MAPPING) which needs to used while sending funds reservation request. |
| 6 | `PPSRP.PostingReqForAcctEntries` | `PpStandaloneRequestParameter_Postingreqforacctentries` | TField |  |  |
| 7 | `PPSRP.PostingReqForBalResAndEntries` | `PpStandaloneRequestParameter_Postingreqforbalresandentries` | TField |  | Hold Mapping record ID ( ID of PP.STANDALONE.REQUEST.MAPPING) which needs to used while sending request for balance reservation as well as raising accounting entries. |
| 8 | `PPSRP.CancelReserveRequest` | `PpStandaloneRequestParameter_Cancelreserverequest` | TField |  | Hold Mapping record ID ( ID of PP.STANDALONE.REQUEST.MAPPING) which needs to used while sending cancellation request for balance reservation. |
| 9 | `PPSRP.ReversePostingRequest` | `PpStandaloneRequestParameter_Reversepostingrequest` | TField |  | Hold Mapping record ID ( ID of PP.STANDALONE.REQUEST.MAPPING) which needs to used while sending request to reverse account entries which are already raised. |
| 10 | `PPSRP.MandateValidateRequest` | `PpStandaloneRequestParameter_Mandatevalidaterequest` | TField |  | Hold Mapping record ID ( ID of PP.STANDALONE.REQUEST.MAPPING) which needs to used while sending request to validate Direct Debit Mandate. |
| 11 | `PPSRP.MandateUpdateRequest` | `PpStandaloneRequestParameter_Mandateupdaterequest` | TField |  | Hold Mapping record ID ( ID of PP.STANDALONE.REQUEST.MAPPING) which needs to used while sending request to update Direct Debit Mandate. |
| 12 | `PPSRP.MandateReopenRequest` | `PpStandaloneRequestParameter_Mandatereopenrequest` | TField |  | Hold Mapping record ID ( ID of PP.STANDALONE.REQUEST.MAPPING) which needs to used while sending request to reopen Direct Debit Mandate. |
| 13 | `PPSRP.CreditAccountCheckFeeRequest` | `PpStandaloneRequestParameter_Creditaccountcheckfeerequest` | TField |  | Hold Mapping record ID ( ID of PP.STANDALONE.REQUEST.MAPPING) which needs to used while sending request to check Credit Account and Calculate Fee. |
| 14 | `PPSRP.DebitAccountCheckFeeRequest` | `PpStandaloneRequestParameter_Debitaccountcheckfeerequest` | TField |  | Hold Mapping record ID ( ID of PP.STANDALONE.REQUEST.MAPPING) which needs to used while sending request to check Debit Account and Calculate Fee. |
| 15 | `PPSRP.Waitforinstpostingresp` | `PpStandaloneRequestParameter_Waitforinstpostingresp` | TField |  |  |
| 16 | `PPSRP.RESERVED.7` | `PpStandaloneRequestParameter_Reserved7` | TField |  |  |
| 17 | `PPSRP.RESERVED.6` | `PpStandaloneRequestParameter_Reserved6` | TField |  |  |
| 18 | `PPSRP.RESERVED.5` | `PpStandaloneRequestParameter_Reserved5` | TField |  |  |
| 19 | `PPSRP.RESERVED.4` | `PpStandaloneRequestParameter_Reserved4` | TField |  |  |
| 20 | `PPSRP.RESERVED.3` | `PpStandaloneRequestParameter_Reserved3` | TField |  |  |
| 21 | `PPSRP.RESERVED.2` | `PpStandaloneRequestParameter_Reserved2` | TField |  |  |
| 22 | `PPSRP.RESERVED.1` | `PpStandaloneRequestParameter_Reserved1` | TField |  |  |
| 23 | `PPSRP.OVERRIDE` | `PpStandaloneRequestParameter_Override` |  |  |  |
| 24 | `PPSRP.RECORD.STATUS` | `PpStandaloneRequestParameter_RecordStatus` | String |  |  |
| 25 | `PPSRP.CURR.NO` | `PpStandaloneRequestParameter_CurrNo` | String |  |  |
| 26 | `PPSRP.INPUTTER` | `PpStandaloneRequestParameter_Inputter` |  |  |  |
| 27 | `PPSRP.DATE.TIME` | `PpStandaloneRequestParameter_DateTime` |  |  |  |
| 28 | `PPSRP.AUTHORISER` | `PpStandaloneRequestParameter_Authoriser` | String |  |  |
| 29 | `PPSRP.CO.CODE` | `PpStandaloneRequestParameter_CoCode` | String |  |  |
| 30 | `PPSRP.DEPT.CODE` | `PpStandaloneRequestParameter_DeptCode` | String |  |  |
| 31 | `PPSRP.AUDITOR.CODE` | `PpStandaloneRequestParameter_AuditorCode` | String |  |  |
| 32 | `PPSRP.AUDIT.DATE.TIME` | `PpStandaloneRequestParameter_AuditDateTime` | String |  |  |
