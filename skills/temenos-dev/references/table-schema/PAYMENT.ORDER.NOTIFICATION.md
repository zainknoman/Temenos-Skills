# PAYMENT.ORDER.NOTIFICATION — Table Schema

> Source: `INSERTS/I_F.PAYMENT.ORDER.NOTIFICATION` in `PI_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PI.PON.FILE.MSG.ID` | `PaymentOrderNotification_FileMsgId` | TField |  |  |
| 2 | `PI.PON.BULK.FILE.ID` | `PaymentOrderNotification_BulkFileId` | TField |  |  |
| 3 | `PI.PON.PAYMENT.ORDER.ID` | `PaymentOrderNotification_PaymentOrderId` | TField |  |  |
| 4 | `PI.PON.PAYMENT.COMPLETE` | `PaymentOrderNotification_PaymentComplete` | TField |  |  |
| 5 | `PI.PON.PAYMENT.SYSTEM.STATUS` | `PaymentOrderNotification_PaymentSystemStatus` | TField |  |  |
| 6 | `PI.PON.STATUS.REASON.CODE` | `PaymentOrderNotification_StatusReasonCode` | TField |  |  |
| 7 | `PI.PON.PAYMENT.SYSTEM.ID` | `PaymentOrderNotification_PaymentSystemId` | TField |  |  |
| 8 | `PI.PON.PAYMENT.SYSTEM.RESPONSE.ID` | `PaymentOrderNotification_PaymentSystemResponseId` | TField |  |  |
| 9 | `PI.PON.PAYMENT.STATUS.ADD.INFO` | `PaymentOrderNotification_PaymentStatusAddInfo` | TField |  |  |
| 10 | `PI.PON.RESPONSE.ORIGINATOR` | `PaymentOrderNotification_ResponseOriginator` | TField |  |  |
| 11 | `PI.PON.CREATED.BY` | `PaymentOrderNotification_CreatedBy` | TField |  |  |
| 12 | `PI.PON.STATUS` | `PaymentOrderNotification_Status` | TField |  |  |
| 13 | `PI.PON.CONTEXT.NAME` | `PaymentOrderNotification_ContextName` |  |  |  |
| 14 | `PI.PON.CONTEXT.VALUE` | `PaymentOrderNotification_ContextValue` |  |  |  |
| 15 | `PI.PON.CREATION.DATE` | `PaymentOrderNotification_CreationDate` | TField |  |  |
| 16 | `PI.PON.SOURCE.SYSTEM` | `PaymentOrderNotification_SourceSystem` | TField |  |  |
| 17 | `PI.PON.RESPONSE.TYPE` | `PaymentOrderNotification_ResponseType` | TField |  |  |
| 18 | `PI.PON.EXTERNAL.FILE.ID` | `PaymentOrderNotification_ExternalFileId` | TField |  |  |
| 19 | `PI.PON.EXTERNAL.RESPONSE.ID` | `PaymentOrderNotification_ExternalResponseId` | TField |  |  |
| 20 | `PI.PON.REPLY.ORIGINATOR` | `PaymentOrderNotification_ReplyOriginator` | TField |  |  |
| 21 | `PI.PON.DDA.RESPONSE` | `PaymentOrderNotification_DdaResponse` | TField |  |  |
| 22 | `PI.PON.RESERVED.14` | `PaymentOrderNotification_Reserved14` |  |  |  |
| 23 | `PI.PON.RESERVED.13` | `PaymentOrderNotification_Reserved13` |  |  |  |
| 24 | `PI.PON.RESERVED.12` | `PaymentOrderNotification_Reserved12` |  |  |  |
| 25 | `PI.PON.RESERVED.11` | `PaymentOrderNotification_Reserved11` | TField |  |  |
| 26 | `PI.PON.RESERVED.10` | `PaymentOrderNotification_Reserved10` | TField |  |  |
| 27 | `PI.PON.RESERVED.9` | `PaymentOrderNotification_Reserved9` | TField |  |  |
| 28 | `PI.PON.RESERVED.8` | `PaymentOrderNotification_Reserved8` | TField |  |  |
| 29 | `PI.PON.RESERVED.7` | `PaymentOrderNotification_Reserved7` | TField |  |  |
| 30 | `PI.PON.RESERVED.6` | `PaymentOrderNotification_Reserved6` | TField |  |  |
| 31 | `PI.PON.RESERVED.5` | `PaymentOrderNotification_Reserved5` | TField |  |  |
| 32 | `PI.PON.RESERVED.4` | `PaymentOrderNotification_Reserved4` | TField |  |  |
| 33 | `PI.PON.RESERVED.3` | `PaymentOrderNotification_Reserved3` | TField |  |  |
| 34 | `PI.PON.RESERVED.2` | `PaymentOrderNotification_Reserved2` | TField |  |  |
| 35 | `PI.PON.RESERVED.1` | `PaymentOrderNotification_Reserved1` | TField |  |  |
| 36 | `PI.PON.LOCAL.REF` | `PaymentOrderNotification_LocalRef` |  |  |  |
| 37 | `PI.PON.OVERRIDE` | `PaymentOrderNotification_Override` |  |  |  |
| 38 | `PI.PON.RECORD.STATUS` | `PaymentOrderNotification_RecordStatus` | String |  |  |
| 39 | `PI.PON.CURR.NO` | `PaymentOrderNotification_CurrNo` | String |  |  |
| 40 | `PI.PON.INPUTTER` | `PaymentOrderNotification_Inputter` |  |  |  |
| 41 | `PI.PON.DATE.TIME` | `PaymentOrderNotification_DateTime` |  |  |  |
| 42 | `PI.PON.AUTHORISER` | `PaymentOrderNotification_Authoriser` | String |  |  |
| 43 | `PI.PON.CO.CODE` | `PaymentOrderNotification_CoCode` | String |  |  |
| 44 | `PI.PON.DEPT.CODE` | `PaymentOrderNotification_DeptCode` | String |  |  |
| 45 | `PI.PON.AUDITOR.CODE` | `PaymentOrderNotification_AuditorCode` | String |  |  |
| 46 | `PI.PON.AUDIT.DATE.TIME` | `PaymentOrderNotification_AuditDateTime` | String |  |  |
