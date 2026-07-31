# HUWRNT.QUEUE.MAINTENANCE — Table Schema

> Source: `INSERTS/I_F.HUWRNT.QUEUE.MAINTENANCE` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUWRNT.QMAINT.ORIG.NAME.NUMBER.MISMATCH` | `HuwrntQueueMaintenance_OrigNameNumberMismatch` | TField |  | Populated from HUWRNT.QUEUE.ITEMS for queue reference in record id. |
| 2 | `HUWRNT.QMAINT.NEW.NAME.NUMBER.MISMATCH` | `HuwrntQueueMaintenance_NewNameNumberMismatch` | TField |  | User modified result of name number mismatch. Eligible for input only when ORIG.NAME.NUMBER.MISMATCH = Y. |
| 3 | `HUWRNT.QMAINT.CUSTOMER.ID` | `HuwrntQueueMaintenance_CustomerId` | TField |  | Customer ID�s attached to account. |
| 4 | `HUWRNT.QMAINT.ORIG.CUST.LIQUI.STATUS` | `HuwrntQueueMaintenance_OrigCustLiquiStatus` | TField |  | Liquidation status of customer. Poupulated from HUWRNT.QUEUE.ITEMS for particular customer. |
| 5 | `HUWRNT.QMAINT.NEW.CUST.LIQUI.STATUS` | `HuwrntQueueMaintenance_NewCustLiquiStatus` | TField |  | Populated from HUWRNT.QUEUE.ITEMS for particular customer.Input allowed only when ORIG.CUST.LIQUI.STATUS = Y. In case of joint account, input allowed only when INCLUDE.IN.QUEUE = INCLUDE. |
| 6 | `HUWRNT.QMAINT.CANCELLATION.REASON` | `HuwrntQueueMaintenance_CancellationReason` | TField |  | Reason for cancelling the queue |
| 7 | `HUWRNT.QMAINT.EXCLUDED.ACCOUNT.NUMBER` | `HuwrntQueueMaintenance_ExcludedAccountNumber` |  |  |  |
| 8 | `HUWRNT.QMAINT.EXCLUDED.REASON` | `HuwrntQueueMaintenance_ExcludedReason` |  |  |  |
| 9 | `HUWRNT.QMAINT.ADDED.ACCOUNT.NUMBER` | `HuwrntQueueMaintenance_AddedAccountNumber` |  |  |  |
| 10 | `HUWRNT.QMAINT.ADDED.REASON` | `HuwrntQueueMaintenance_AddedReason` |  |  |  |
| 11 | `HUWRNT.QMAINT.SUSPENSION.CODE` | `HuwrntQueueMaintenance_SuspensionCode` | TField |  | Suspension Code. |
| 12 | `HUWRNT.QMAINT.SUSPENSION.REASON` | `HuwrntQueueMaintenance_SuspensionReason` | TField |  | Reason for suspension of queue. Should be a valid record in QUEUE.ITEMS . |
| 13 | `HUWRNT.QMAINT.REVOCATION.REASON` | `HuwrntQueueMaintenance_RevocationReason` | TField |  | Reason for revocation. |
| 14 | `HUWRNT.QMAINT.ORIGINAL.EXPIRY.DATE` | `HuwrntQueueMaintenance_OriginalExpiryDate` | TField |  | Original expiry date. Should be a valid record in queue items. |
| 15 | `HUWRNT.QMAINT.NEW.EXPIRY.DATE` | `HuwrntQueueMaintenance_NewExpiryDate` | TField |  | Modified expiry date. User input allowed only for queue type AB, MBW and CB. |
| 16 | `HUWRNT.QMAINT.PRESENT.BEN.ACCOUNT.NO` | `HuwrntQueueMaintenance_PresentBenAccountNo` | TField |  | Specifies the account number of the beneficiary or payer or initiator of the warrant as received from GIRO |
| 17 | `HUWRNT.QMAINT.PRESENT.BEN.NAME` | `HuwrntQueueMaintenance_PresentBenName` |  |  |  |
| 18 | `HUWRNT.QMAINT.NEW.BEN.ACCOUNT.NO` | `HuwrntQueueMaintenance_NewBenAccountNo` | TField |  | Specifies the new account number of the beneficiary for Criminal block |
| 19 | `HUWRNT.QMAINT.NEW.BEN.NAME` | `HuwrntQueueMaintenance_NewBenName` |  |  |  |
| 20 | `HUWRNT.QMAINT.MODIFICATION.REASON` | `HuwrntQueueMaintenance_ModificationReason` | TField |  | Specifies the modification reason |
| 21 | `HUWRNT.QMAINT.RESERVED.10` | `HuwrntQueueMaintenance_Reserved10` |  |  |  |
| 22 | `HUWRNT.QMAINT.RESERVED.9` | `HuwrntQueueMaintenance_Reserved9` |  |  |  |
| 23 | `HUWRNT.QMAINT.RESERVED.8` | `HuwrntQueueMaintenance_Reserved8` |  |  |  |
| 24 | `HUWRNT.QMAINT.RESERVED.7` | `HuwrntQueueMaintenance_Reserved7` | TField |  | Reserved for future use. |
| 25 | `HUWRNT.QMAINT.RESERVED.6` | `HuwrntQueueMaintenance_Reserved6` | TField |  | Reserved for future use. |
| 26 | `HUWRNT.QMAINT.RESERVED.5` | `HuwrntQueueMaintenance_Reserved5` | TField |  | Reserved for future use. |
| 27 | `HUWRNT.QMAINT.RESERVED.4` | `HuwrntQueueMaintenance_Reserved4` | TField |  | Reserved for future use. |
| 28 | `HUWRNT.QMAINT.RESERVED.3` | `HuwrntQueueMaintenance_Reserved3` | TField |  | Reserved for future use. |
| 29 | `HUWRNT.QMAINT.RESERVED.2` | `HuwrntQueueMaintenance_Reserved2` | TField |  | Reserved for future use. |
| 30 | `HUWRNT.QMAINT.RESERVED.1` | `HuwrntQueueMaintenance_Reserved1` | TField |  | Reserved for future use. |
| 31 | `HUWRNT.QMAINT.LOCAL.REF` | `HuwrntQueueMaintenance_LocalRef` |  |  |  |
| 32 | `HUWRNT.QMAINT.OVERRIDE` | `HuwrntQueueMaintenance_Override` |  |  |  |
| 33 | `HUWRNT.QMAINT.RECORD.STATUS` | `HuwrntQueueMaintenance_RecordStatus` | String |  |  |
| 34 | `HUWRNT.QMAINT.CURR.NO` | `HuwrntQueueMaintenance_CurrNo` | String |  |  |
| 35 | `HUWRNT.QMAINT.INPUTTER` | `HuwrntQueueMaintenance_Inputter` |  |  |  |
| 36 | `HUWRNT.QMAINT.DATE.TIME` | `HuwrntQueueMaintenance_DateTime` |  |  |  |
| 37 | `HUWRNT.QMAINT.AUTHORISER` | `HuwrntQueueMaintenance_Authoriser` | String |  |  |
| 38 | `HUWRNT.QMAINT.CO.CODE` | `HuwrntQueueMaintenance_CoCode` | String |  |  |
| 39 | `HUWRNT.QMAINT.DEPT.CODE` | `HuwrntQueueMaintenance_DeptCode` | String |  |  |
| 40 | `HUWRNT.QMAINT.AUDITOR.CODE` | `HuwrntQueueMaintenance_AuditorCode` | String |  |  |
| 41 | `HUWRNT.QMAINT.AUDIT.DATE.TIME` | `HuwrntQueueMaintenance_AuditDateTime` | String |  |  |
