# OFS.REQUEST.DETAIL — Table Schema

> Source: `INSERTS/I_F.OFS.REQUEST.DETAIL` in `EB_Interface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OFS.RD.APPLICATION` | `OfsRequestDetail_Application` | TField |  | Identifies the name of the APPLICATION for which a transaction has been done. |
| 2 | `OFS.RD.VERSION` | `OfsRequestDetail_Version` | TField |  | Identifies the VERSION used for the transaction. |
| 3 | `OFS.RD.FUNCTION` | `OfsRequestDetail_Function` | TField |  | Identifies the FUNCTION of the transaction. |
| 4 | `OFS.RD.TRANS.REFERENCE` | `OfsRequestDetail_TransReference` | TField |  | Contains the transaction ID or message ID for the application that was executed. Validation Rules: Standard T24 alphanumeric field with a maximum of 30 characters. |
| 5 | `OFS.RD.USER.NAME` | `OfsRequestDetail_UserName` | TField |  | Contains the sign on name of a valid T24 USER used to perform the request. Validation Rules: Standard T24 alphanumeric field with a maximum of 25 characters. |
| 6 | `OFS.RD.COMPANY` | `OfsRequestDetail_Company` | TField |  | In a multi-company environment it identifies the company to which the transaction is entered. Validation Rules: Standard T24 alphanumeric field with a maximum of 15 characters. |
| 7 | `OFS.RD.DATE.TIME.RECD` | `OfsRequestDetail_DateTimeRecd` | TField |  | Identifies the date and time of the message Received from external application. Validation Rules: Standard T24 alphanumeric field with a maximum of 20 characters. |
| 8 | `OFS.RD.DATE.TIME.QUEUE` | `OfsRequestDetail_DateTimeQueue` | TField |  | Identifies the date and time of the Message in Queue. This will be updated if the message STATUS is QUEUED. Validation Rules: Standard T24 alphanumeric field with a maximum of 20 characters. |
| 9 | `OFS.RD.DATE.TIME.PROC` | `OfsRequestDetail_DateTimeProc` | TField |  | Identifies the date and time of the message Processed. Validation Rules: Standard T24 alphanumeric field with a maximum of 20 characters. |
| 10 | `OFS.RD.STATUS` | `OfsRequestDetail_Status` | TField |  | Identifies the status of the processed message. It can be RECEIVED or QUEUED or ERROR or VALIDATED or PROCESSED or SUSPENDED. Validation Rules: Standard T24 alphanumeric field with a maximum of 10 characters. The following values are permitted: RECEIVED, QUEUED, ERROR, VALIDATED, PROCESSED, SUSPENDED. |
| 11 | `OFS.RD.MSG.IN` | `OfsRequestDetail_MsgIn` | TField |  | Contains the message received from the external application to process the transaction. Validation Rules: Standard T24 alphanumeric field with a maximum of 30 characters. |
| 12 | `OFS.RD.MSG.OUT` | `OfsRequestDetail_MsgOut` | TField |  | Contains the message returned to the external application after processing the message. Validation Rules: Standard T24 alphanumeric field with a maximum of 30 characters. |
| 13 | `OFS.RD.ACTION` | `OfsRequestDetail_Action` | TField |  | Identifies the ACTION for the application. |
| 14 | `OFS.RD.GTS.CONTROL` | `OfsRequestDetail_GtsControl` | TField |  | Specifies the GTS.CONTROL value defined in the version used for the transaction. |
| 15 | `OFS.RD.NO.OF.AUTH` | `OfsRequestDetail_NoOfAuth` | TField |  | Specifies the NO.OF.AUTH value defined in the version used for the transaction. |
| 16 | `OFS.RD.T24.SESSION.NO` | `OfsRequestDetail_T24SessionNo` | TField |  |  |
| 17 | `OFS.RD.PARENT.ID` | `OfsRequestDetail_ParentId` | TField |  |  |
| 18 | `OFS.RD.CACHE.LOAD` | `OfsRequestDetail_CacheLoad` | TField |  |  |
| 19 | `OFS.RD.CACHE.HITS` | `OfsRequestDetail_CacheHits` | TField |  |  |
| 20 | `OFS.RD.NO.OF.READ` | `OfsRequestDetail_NoOfRead` | TField |  |  |
| 21 | `OFS.RD.NO.OF.WRITE` | `OfsRequestDetail_NoOfWrite` | TField |  |  |
| 22 | `OFS.RD.NO.OF.SELECT` | `OfsRequestDetail_NoOfSelect` | TField |  |  |
| 23 | `OFS.RD.SUCCESSFUL.LOCK` | `OfsRequestDetail_SuccessfulLock` | TField |  |  |
| 24 | `OFS.RD.LOCK.COLLISION` | `OfsRequestDetail_LockCollision` | TField |  |  |
| 25 | `OFS.RD.NO.API.CALL` | `OfsRequestDetail_NoApiCall` | TField |  |  |
| 26 | `OFS.RD.DATE.TIME.RECD.LOC` | `OfsRequestDetail_DateTimeRecdLoc` | TField |  | Identifies the date and time of the message received, specific to the current company zone. Validation Rules: Standard T24 alphanumeric field with a maximum of 20 characters. Zone time updated only when USE.LOCAL.TIME field is set in SPF. |
| 27 | `OFS.RD.DATE.TIME.PROC.LOC` | `OfsRequestDetail_DateTimeProc` | TField |  | Identifies the date and time of the message Processed. Validation Rules: Standard T24 alphanumeric field with a maximum of 20 characters. |
| 28 | `OFS.RD.FIELD.CACHE` | `OfsRequestDetail_FieldCache` | TField |  | Denotes the status of field cache functionality whether it is used in current application for which the request has been processed.It can hold the values, 1. FOUND - Field cache is enabled or utilised (it is applicable for very first request in a session or subsequent request of same application). 2. NOT.FOUND - Field cache is not enabled so not used (it can apply for even old format templates or applications forcefully disabled field cache). Validation Rules: Standard T24 alphanumeric field with a maximum of 50 characters. |
