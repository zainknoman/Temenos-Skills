# HUWRNT.WARRANT.REQUEST — Table Schema

> Source: `INSERTS/I_F.HUWRNT.WARRANT.REQUEST` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUWRWR.PAYMENT.CCY` | `HuwrntWarrantRequest_PaymentCcy` | TField |  | Currency of warrant. |
| 2 | `HUWRWR.PAYMENT.AMT` | `HuwrntWarrantRequest_PaymentAmt` | TField |  | Amount of warrant. |
| 3 | `HUWRWR.PAYER.ACCOUNT.NO` | `HuwrntWarrantRequest_PayerAccountNo` | TField |  | Account number on which warrant is served. |
| 4 | `HUWRWR.PAYER.NAME` | `HuwrntWarrantRequest_PayerName` |  |  |  |
| 5 | `HUWRWR.VALUE.DATE.PCS` | `HuwrntWarrantRequest_ValueDatePcs` | TField |  | Date on which warrant can be settled, sent by GIRO. |
| 6 | `HUWRWR.BE.CHECK.ID` | `HuwrntWarrantRequest_BeCheckId` | TField |  | Check ID of Bill of Exchange. |
| 7 | `HUWRWR.COLLECTION.TYPE` | `HuwrntWarrantRequest_CollectionType` | TField |  | Warrant type, A valid External transaction code in HUWRNT.TRANSACTION.PARAM. |
| 8 | `HUWRWR.EXPIRY.DATE` | `HuwrntWarrantRequest_ExpiryDate` | TField |  | Date until which the warrant has to be queued. |
| 9 | `HUWRWR.DATE.TIME.PCS` | `HuwrntWarrantRequest_DateTimePcs` | TField |  | Date and time, record was created in PCS. |
| 10 | `HUWRWR.DATE.TIME.SYSTEM` | `HuwrntWarrantRequest_DateTimeSystem` | TField |  | Date and time, record was created in T24. |
| 11 | `HUWRWR.WARRANT.STATUS` | `HuwrntWarrantRequest_WarrantStatus` | TField |  | Status of the Warrant. |
| 12 | `HUWRWR.BEN.ACCOUNT.NO` | `HuwrntWarrantRequest_BenAccountNo` | TField |  | Beneficiary Account Number as received from GIRO. |
| 13 | `HUWRWR.BEN.NAME` | `HuwrntWarrantRequest_BenName` |  |  |  |
| 14 | `HUWRWR.NARRATIVE` | `HuwrntWarrantRequest_Narrative` |  |  |  |
| 15 | `HUWRWR.PROCESS.CHANNEL` | `HuwrntWarrantRequest_ProcessChannel` | TField |  | Channel through which warrant has arrived. Given by PCS. |
| 16 | `HUWRWR.PREVIOUS.SETTLED.AMOUNT` | `HuwrntWarrantRequest_PreviousSettledAmount` | TField |  | Specifies the amount that is settled for the warrant queue item in legacy system. |
| 17 | `HUWRWR.NUM.OF.PAYMENTS.MADE` | `HuwrntWarrantRequest_NumOfPaymentsMade` | TField |  | Specifies the number of payments that have been made previously for the warrant collection. |
| 18 | `HUWRWR.MIGRATED.WARRANT` | `HuwrntWarrantRequest_MigratedWarrant` | TField |  | Specifies whether warrant request is migrated or not. |
| 19 | `HUWRWR.RESERVED.12` | `HuwrntWarrantRequest_Reserved12` | TField |  | Reserved for future use. |
| 20 | `HUWRWR.RESERVED.11` | `HuwrntWarrantRequest_Reserved11` | TField |  | Reserved for future use. |
| 21 | `HUWRWR.RESERVED.10` | `HuwrntWarrantRequest_Reserved10` | TField |  | Reserved for future use. |
| 22 | `HUWRWR.RESERVED.9` | `HuwrntWarrantRequest_Reserved9` | TField |  | Reserved for future use. |
| 23 | `HUWRWR.RESERVED.8` | `HuwrntWarrantRequest_Reserved8` | TField |  | Reserved for future use. |
| 24 | `HUWRWR.RESERVED.7` | `HuwrntWarrantRequest_Reserved7` | TField |  | Reserved for future use. |
| 25 | `HUWRWR.RESERVED.6` | `HuwrntWarrantRequest_Reserved6` | TField |  | Reserved for future use. |
| 26 | `HUWRWR.RESERVED.5` | `HuwrntWarrantRequest_Reserved5` | TField |  | Reserved for future use. |
| 27 | `HUWRWR.RESERVED.4` | `HuwrntWarrantRequest_Reserved4` | TField |  | Reserved for future use. |
| 28 | `HUWRWR.RESERVED.3` | `HuwrntWarrantRequest_Reserved3` | TField |  | Reserved for future use. |
| 29 | `HUWRWR.RESERVED.2` | `HuwrntWarrantRequest_Reserved2` | TField |  | Reserved for future use. |
| 30 | `HUWRWR.RESERVED.1` | `HuwrntWarrantRequest_Reserved1` | TField |  | Reserved for future use. |
| 31 | `HUWRWR.LOCAL.REF` | `HuwrntWarrantRequest_LocalRef` |  |  |  |
| 32 | `HUWRWR.OVERRIDE` | `HuwrntWarrantRequest_Override` |  |  |  |
| 33 | `HUWRWR.RECORD.STATUS` | `HuwrntWarrantRequest_RecordStatus` | String |  |  |
| 34 | `HUWRWR.CURR.NO` | `HuwrntWarrantRequest_CurrNo` | String |  |  |
| 35 | `HUWRWR.INPUTTER` | `HuwrntWarrantRequest_Inputter` |  |  |  |
| 36 | `HUWRWR.DATE.TIME` | `HuwrntWarrantRequest_DateTime` |  |  |  |
| 37 | `HUWRWR.AUTHORISER` | `HuwrntWarrantRequest_Authoriser` | String |  |  |
| 38 | `HUWRWR.CO.CODE` | `HuwrntWarrantRequest_CoCode` | String |  |  |
| 39 | `HUWRWR.DEPT.CODE` | `HuwrntWarrantRequest_DeptCode` | String |  |  |
| 40 | `HUWRWR.AUDITOR.CODE` | `HuwrntWarrantRequest_AuditorCode` | String |  |  |
| 41 | `HUWRWR.AUDIT.DATE.TIME` | `HuwrntWarrantRequest_AuditDateTime` | String |  |  |
