# DE.PRODUCT — Table Schema

> Source: `INSERTS/I_F.DE.PRODUCT` in `PF_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DE.PRD.MESSAGE.STATUS` | `DeProduct_MessageStatus` | TField | No | Specifies the status that a message matching this product key should be set to. During formatting, if delete is specified on the product record, the message record is checked to see if delete is allowed for the message type currently being processed. If delete is not allowed, the status of 'DELETE' on the product record is ignored. Validation Rules: 'HOLD' 'DELETE' or nothing. (Optional input) If the product record is for a specific message type and delete is not allowed for the message type, 'DELETE' cannot be entered. |
| 2 | `DE.PRD.PRIORITY` | `DeProduct_Priority` | TField | No | Specifies the Priority that a message matching this product key should be set to. Urgent ('U') is the highest priority, and requires immediate confirmation of delivery if this can be provided by the carrier. Priority ('P') has a lower priority than 'U'. Everything else is Normal ('N'). Note : The priority defined in this table will increase the priority of a message but will never decrease it, e.g. a product record is set up with a priority of 'P'. If a message matching the product key has a priority of 'U' it will remain unchanged. However, if a message has a priority of 'N', it will be changed to 'P'. Validation Rules: 'U', 'P' or nothing. (Optional input) |
| 3 | `DE.PRD.CARR.ADD.NO` | `DeProduct_CarrierAddrNo` |  |  |  |
| 4 | `DE.PRD.TRANSLATION` | `DeProduct_Translation` |  |  |  |
| 5 | `DE.PRD.FORMAT` | `DeProduct_Format` |  |  |  |
| 6 | `DE.PRD.COPIES` | `DeProduct_Copies` |  |  |  |
| 7 | `DE.PRD.CUSTOMER` | `DeProduct_Customer` |  |  |  |
| 8 | `DE.PRD.SEND.OTHER.RECEPIENTS.ONLY` | `DeProduct_SendOtherRecepientsOnly` |  |  |  |
| 9 | `DE.PRD.RESERVED.4` | `DeProduct_Reserved4` |  |  |  |
| 10 | `DE.PRD.HOLD.MAIL.END` | `DeProduct_HoldMailEnd` |  |  |  |
| 11 | `DE.PRD.HOLD.MAIL.OPT` | `DeProduct_HoldMailOpt` |  |  |  |
| 12 | `DE.PRD.LOCAL.REF` | `DeProduct_LocalRef` |  |  |  |
| 13 | `DE.PRD.OVERRIDE` | `DeProduct_Override` |  |  |  |
| 14 | `DE.PRD.RECORD.STATUS` | `DeProduct_RecordStatus` | String |  |  |
| 15 | `DE.PRD.CURR.NO` | `DeProduct_CurrNo` | String |  |  |
| 16 | `DE.PRD.INPUTTER` | `DeProduct_Inputter` |  |  |  |
| 17 | `DE.PRD.DATE.TIME` | `DeProduct_DateTime` |  |  |  |
| 18 | `DE.PRD.AUTHORISER` | `DeProduct_Authoriser` | String |  |  |
| 19 | `DE.PRD.CO.CODE` | `DeProduct_CoCode` | String |  |  |
| 20 | `DE.PRD.DEPT.CODE` | `DeProduct_DeptCode` | String |  |  |
| 21 | `DE.PRD.AUDITOR.CODE` | `DeProduct_AuditorCode` | String |  |  |
| 22 | `DE.PRD.AUDIT.DATE.TIME` | `DeProduct_AuditDateTime` | String |  |  |
| 23 | `DE.PRD.START.DATE` | `DeProduct_StartDate` |  |  |  |
| 24 | `DE.PRD.END.DATE` | `DeProduct_EndDate` |  |  |  |
| 25 | `DE.PRD.HOLD.OUTPUT` | `DeProduct_HoldOutput` |  |  |  |
| 26 | `DE.PRD.HOLD.MAIL.START` | `DeProduct_HoldMailStart` |  |  |  |
| 27 | `DE.PRD.OTHER.RECEPIENTS` | `Deproduct_OtherRecepients` |  |  |  |
| 28 | `DE.PRD.OTHER.RECEPIENTS.LANGUAGE` | `DeProduct_OtherRecepientsLanguage` |  |  |  |
| 29 | `DE.PRD.OTHER.RECEPIENTS.FORMAT` | `DeProduct_OtherRecepientsFormat` |  |  |  |
| 30 | `DE.PRD.OTHER.RECEPIENTS.COPIES` | `DeProduct_OtherRecepientsCopies` |  |  |  |
