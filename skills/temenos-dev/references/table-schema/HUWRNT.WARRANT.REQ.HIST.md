# HUWRNT.WARRANT.REQ.HIST — Table Schema

> Source: `INSERTS/I_F.HUWRNT.WARRANT.REQ.HIST` in `HUWRNT_Queuing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `HUWWRH.PAYMENT.CCY` | `HuwrntWarrantReqHist_PaymentCcy` | TField |  | Currency of warrant. |
| 2 | `HUWWRH.PAYMENT.AMT` | `HuwrntWarrantReqHist_PaymentAmt` | TField |  | Amount of warrant. |
| 3 | `HUWWRH.PAYER.ACCOUNT.NO` | `HuwrntWarrantReqHist_PayerAccountNo` | TField |  | Account number on which warrant is served. |
| 4 | `HUWWRH.PAYER.NAME` | `HuwrntWarrantReqHist_PayerName` |  |  |  |
| 5 | `HUWWRH.VALUE.DATE.PCS` | `HuwrntWarrantReqHist_ValueDatePcs` | TField |  | Date on which warrant can be settled, sent by GIRO. |
| 6 | `HUWWRH.BE.CHECK.ID` | `HuwrntWarrantReqHist_BeCheckId` | TField |  | Check ID of Bill of Exchange. |
| 7 | `HUWWRH.COLLECTION.TYPE` | `HuwrntWarrantReqHist_CollectionType` | TField |  | Warrant type, A valid External transaction code in HUWRNT.TRANSACTION.PARAM. |
| 8 | `HUWWRH.EXPIRY.DATE` | `HuwrntWarrantReqHist_ExpiryDate` | TField |  | Date until which the warrant has to be queued. |
| 9 | `HUWWRH.DATE.TIME.PCS` | `HuwrntWarrantReqHist_DateTimePcs` | TField |  | Date and time, record was created in PCS. |
| 10 | `HUWWRH.DATE.TIME.SYSTEM` | `HuwrntWarrantReqHist_DateTimeSystem` | TField |  | Date and time, record was created in T24. |
| 11 | `HUWWRH.WARRANT.STATUS` | `HuwrntWarrantReqHist_WarrantStatus` | TField |  | Status of the Warrant. |
| 12 | `HUWWRH.BEN.ACCOUNT.NO` | `HuwrntWarrantReqHist_BenAccountNo` | TField |  | Beneficiary Account Number as received from GIRO. |
| 13 | `HUWWRH.BEN.NAME` | `HuwrntWarrantReqHist_BenName` |  |  |  |
| 14 | `HUWWRH.NARRATIVE` | `HuwrntWarrantReqHist_Narrative` |  |  |  |
| 15 | `HUWWRH.PROCESS.CHANNEL` | `HuwrntWarrantReqHist_ProcessChannel` | TField |  | Channel through which warrant has arrived. Given by PCS. |
| 16 | `HUWWRH.REASON` | `HuwrntWarrantReqHist_Reason` |  |  |  |
| 17 | `HUWWRH.STMT.NOS` | `HuwrntWarrantReqHist_StmtNos` |  |  |  |
| 18 | `HUWWRH.PREVIOUS.SETTLED.AMOUNT` | `HuwrntWarrantReqHist_PreviousSettledAmount` | TField |  | Specifies the amount that is settled for the warrant queue item in legacy system. |
| 19 | `HUWWRH.NUM.OF.PAYMENTS.MADE` | `HuwrntWarrantReqHist_NumOfPaymentsMade` | TField |  | Specifies the number of payments that have been made previously for the warrant collection. |
| 20 | `HUWWRH.MIGRATED.WARRANT` | `HuwrntWarrantReqHist_MigratedWarrant` | TField |  | Specifies whether warrant request is migrated or not. |
| 21 | `HUWWRH.RESERVED.11` | `HuwrntWarrantReqHist_Reserved11` | TField |  | Reserved for future use. |
| 22 | `HUWWRH.RESERVED.10` | `HuwrntWarrantReqHist_Reserved10` | TField |  | Reserved for future use. |
| 23 | `HUWWRH.RESERVED.9` | `HuwrntWarrantReqHist_Reserved9` | TField |  | Reserved for future use. |
| 24 | `HUWWRH.RESERVED.8` | `HuwrntWarrantReqHist_Reserved8` | TField |  | Reserved for future use. |
| 25 | `HUWWRH.RESERVED.7` | `HuwrntWarrantReqHist_Reserved7` | TField |  | Reserved for future use. |
| 26 | `HUWWRH.RESERVED.6` | `HuwrntWarrantReqHist_Reserved6` | TField |  | Reserved for future use. |
| 27 | `HUWWRH.RESERVED.5` | `HuwrntWarrantReqHist_Reserved5` | TField |  | Reserved for future use. |
| 28 | `HUWWRH.RESERVED.4` | `HuwrntWarrantReqHist_Reserved4` | TField |  | Reserved for future use. |
| 29 | `HUWWRH.RESERVED.3` | `HuwrntWarrantReqHist_Reserved3` | TField |  | Reserved for future use. |
| 30 | `HUWWRH.RESERVED.2` | `HuwrntWarrantReqHist_Reserved2` | TField |  | Reserved for future use. |
| 31 | `HUWWRH.RESERVED.1` | `HuwrntWarrantReqHist_Reserved1` | TField |  | Reserved for future use. |
| 32 | `HUWWRH.LOCAL.REF` | `HuwrntWarrantReqHist_LocalRef` |  |  |  |
| 33 | `HUWWRH.OVERRIDE` | `HuwrntWarrantReqHist_Override` |  |  |  |
| 34 | `HUWWRH.RECORD.STATUS` | `HuwrntWarrantReqHist_RecordStatus` | String |  |  |
| 35 | `HUWWRH.CURR.NO` | `HuwrntWarrantReqHist_CurrNo` | String |  |  |
| 36 | `HUWWRH.INPUTTER` | `HuwrntWarrantReqHist_Inputter` |  |  |  |
| 37 | `HUWWRH.DATE.TIME` | `HuwrntWarrantReqHist_DateTime` |  |  |  |
| 38 | `HUWWRH.AUTHORISER` | `HuwrntWarrantReqHist_Authoriser` | String |  |  |
| 39 | `HUWWRH.CO.CODE` | `HuwrntWarrantReqHist_CoCode` | String |  |  |
| 40 | `HUWWRH.DEPT.CODE` | `HuwrntWarrantReqHist_DeptCode` | String |  |  |
| 41 | `HUWWRH.AUDITOR.CODE` | `HuwrntWarrantReqHist_AuditorCode` | String |  |  |
| 42 | `HUWWRH.AUDIT.DATE.TIME` | `HuwrntWarrantReqHist_AuditDateTime` | String |  |  |
