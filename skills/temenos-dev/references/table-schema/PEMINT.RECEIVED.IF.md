# PEMINT.RECEIVED.IF — Table Schema

> Source: `INSERTS/I_F.PEMINT.RECEIVED.IF` in `PEMINT_DDAService.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PEMINT.RIF.CompanyID` | `PemintReceivedIf_Companyid` | TField |  | Indicates the company ID for which the record is created. Example: BNK,GB1 Validation Rules: 3 alphanumeric characters. |
| 2 | `PEMINT.RIF.FTNumber` | `PemintReceivedIf_Ftnumber` | TField |  | FTNumber is unique within a company. It is used to identify the records related to one payment. Validation Rules: 16 alphanumeric characters. |
| 3 | `PEMINT.RIF.FileReference` | `PemintReceivedIf_Filereference` | TField |  | Specifies the unique reference the request received from payment system. |
| 4 | `PEMINT.RIF.ReceivedDateTime` | `PemintReceivedIf_Receiveddatetime` | TField |  | Specifies the date and time the request received. Validation Rules: 17 characters Date Time format. Example: 2021021533072 The value is not editable by the user. |
| 5 | `PEMINT.RIF.ReceivedMsg` | `PemintReceivedIf_Receivedmsg` | TField |  | Holds the payload of the received request message. |
| 6 | `PEMINT.RIF.Status` | `PemintReceivedIf_Status` | TField |  | Specifies the process status of the request RECEIVED - For a successful commit on the system. DUPLICATE - If any duplicate exists. PENDING � If the request is being retried. PROCESSED � If the request is processed. |
| 7 | `PEMINT.RIF.ResponseSent` | `PemintReceivedIf_Responsesent` | TField |  | Specifies the actual standalone response sent back to Payment system for the received request. The value is not editable by the user. |
| 8 | `PEMINT.RIF.RESERVED.2` | `PemintReceivedIf_Reserved2` |  |  |  |
| 9 | `PEMINT.RIF.RESERVED.3` | `PemintReceivedIf_Reserved3` |  |  |  |
| 10 | `PEMINT.RIF.RESERVED.4` | `PemintReceivedIf_Reserved4` | TField |  | Reserve field for future use. Validation Rules: |
| 11 | `PEMINT.RIF.STMT.NOS` | `PemintReceivedIf_StmtNos` |  |  |  |
| 12 | `PEMINT.RIF.OVERRIDE` | `PemintReceivedIf_Override` |  |  |  |
| 13 | `PEMINT.RIF.RECORD.STATUS` | `PemintReceivedIf_RecordStatus` | String |  |  |
| 14 | `PEMINT.RIF.CURR.NO` | `PemintReceivedIf_CurrNo` | String |  |  |
| 15 | `PEMINT.RIF.INPUTTER` | `PemintReceivedIf_Inputter` |  |  |  |
| 16 | `PEMINT.RIF.DATE.TIME` | `PemintReceivedIf_DateTime` |  |  |  |
| 17 | `PEMINT.RIF.AUTHORISER` | `PemintReceivedIf_Authoriser` | String |  |  |
| 18 | `PEMINT.RIF.CO.CODE` | `PemintReceivedIf_CoCode` | String |  |  |
| 19 | `PEMINT.RIF.DEPT.CODE` | `PemintReceivedIf_DeptCode` | String |  |  |
| 20 | `PEMINT.RIF.AUDITOR.CODE` | `PemintReceivedIf_AuditorCode` | String |  |  |
| 21 | `PEMINT.RIF.AUDIT.DATE.TIME` | `PemintReceivedIf_AuditDateTime` | String |  |  |
