# AFRCIP.PAYMENT.INCIDENT — Table Schema

> Source: `INSERTS/I_F.AFRCIP.PAYMENT.INCIDENT` in `AFRCIP_CentralisedPaymentIncidents.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AFRCIP.PAY.INCI.PAYMENT.REFERENCE` | `AfrcipPaymentIncident_PaymentReference` | TField |  | This field holds Payment reference number |
| 2 | `AFRCIP.PAY.INCI.NUMBER.VALUE` | `AfrcipPaymentIncident_NumberValue` | TField |  | This field holds cheque number for cheque transaction and Mandatereference number for DD |
| 3 | `AFRCIP.PAY.INCI.ACCOUNT.NUMBER` | `AfrcipPaymentIncident_AccountNumber` | TField |  | This field holds account number belongs to cheque number |
| 4 | `AFRCIP.PAY.INCI.NATURE.OF.DECLARATION` | `AfrcipPaymentIncident_NatureOfDeclaration` | TField |  | This field hold nature of declaration 00-Creation, 02 -Regularisation, 02- Annulation/cancellation |
| 5 | `AFRCIP.PAY.INCI.INCIDENT.CODE` | `AfrcipPaymentIncident_IncidentCode` | TField |  | This field refers to incident code. |
| 6 | `AFRCIP.PAY.INCI.EXTRACTION.DATE` | `AfrcipPaymentIncident_ExtractionDate` | TField |  | This field holds date when the record extracted. |
| 7 | `AFRCIP.PAY.INCI.SOURCE.OF.DECLARATION` | `AfrcipPaymentIncident_SourceOfDeclaration` | TField |  | This field holds source of declaration.0-PCIP, 1-CCIP,2-SI,3-SYSTAC,4-GIMAC |
| 8 | `AFRCIP.PAY.INCI.CONTROL.STATUS` | `AfrcipPaymentIncident_ControlStatus` | TField |  | This field holds control status.1-Accepted. 2-Rejected. 3-On Hold |
| 9 | `AFRCIP.PAY.INCI.PENALTY.AMOUNT` | `AfrcipPaymentIncident_PenaltyAmount` | TField |  | This field holds penalty payable amount. |
| 10 | `AFRCIP.PAY.INCI.ERROR.FIELD.NAME` | `AfrcipPaymentIncident_ErrorFieldName` | TField |  | This field holds the fields name raising error. |
| 11 | `AFRCIP.PAY.INCI.FIELD.VALUE` | `AfrcipPaymentIncident_FieldValue` | TField |  | This field holds the value of field mentioned in ERROR.FIELD.NAME. |
| 12 | `AFRCIP.PAY.INCI.ERROR.REASON.CODE` | `AfrcipPaymentIncident_ErrorReasonCode` | TField |  | This field holds the error reason code. |
| 13 | `AFRCIP.PAY.INCI.ERROR.DETAILS` | `AfrcipPaymentIncident_ErrorDetails` | TField |  | This field holds the error details. |
| 14 | `AFRCIP.PAY.INCI.LOCAL.REF` | `AfrcipPaymentIncident_LocalRef` |  |  |  |
| 15 | `AFRCIP.PAY.INCI.OVERRIDE` | `AfrcipPaymentIncident_Override` |  |  |  |
| 16 | `AFRCIP.PAY.INCI.RECORD.STATUS` | `AfrcipPaymentIncident_RecordStatus` | String |  |  |
| 17 | `AFRCIP.PAY.INCI.CURR.NO` | `AfrcipPaymentIncident_CurrNo` | String |  |  |
| 18 | `AFRCIP.PAY.INCI.INPUTTER` | `AfrcipPaymentIncident_Inputter` |  |  |  |
| 19 | `AFRCIP.PAY.INCI.DATE.TIME` | `AfrcipPaymentIncident_DateTime` |  |  |  |
| 20 | `AFRCIP.PAY.INCI.AUTHORISER` | `AfrcipPaymentIncident_Authoriser` | String |  |  |
| 21 | `AFRCIP.PAY.INCI.CO.CODE` | `AfrcipPaymentIncident_CoCode` | String |  |  |
| 22 | `AFRCIP.PAY.INCI.DEPT.CODE` | `AfrcipPaymentIncident_DeptCode` | String |  |  |
| 23 | `AFRCIP.PAY.INCI.AUDITOR.CODE` | `AfrcipPaymentIncident_AuditorCode` | String |  |  |
| 24 | `AFRCIP.PAY.INCI.AUDIT.DATE.TIME` | `AfrcipPaymentIncident_AuditDateTime` | String |  |  |
