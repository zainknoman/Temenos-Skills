# DESCTX.ALLINFEES.TRANSACTIONS — Table Schema

> Source: `INSERTS/I_F.DESCTX.ALLINFEES.TRANSACTIONS` in `DESCTX_Taxation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SECTRAS.FEES.APPLICATION` | `DesctxAllinfeesTransactions_Application` | TField |  | This field holds the application where charge is posted Values: 1. SC.ADVISORY.CHG.POSTED 2. AC.CHARGE.REQUEST |
| 2 | `SECTRAS.FEES.TRANSACTION.REF` | `DesctxAllinfeesTransactions_TransactionRef` | TField |  | This field contains the Transaction id of the underlying application |
| 3 | `SECTRAS.FEES.MSG.TO.SECTRAS` | `DesctxAllinfeesTransactions_MsgToSectras` | TField |  | This field is used to indicate what kind of message needs to be sent to Sectras. Values: 1. CANCEL.AND.BOOK 2. BOOK 3. CANCEL |
| 4 | `SECTRAS.FEES.STATUS` | `DesctxAllinfeesTransactions_Status` | TField |  | This field indicates the status of the transaction. Values: 1. READY.TO.SEND 2. SUCCESS 3. ERROR 4. CANCELLED |
| 5 | `SECTRAS.FEES.TRANSACTION.DATE` | `DesctxAllinfeesTransactions_TransactionDate` | TField |  | This field holds the date of first entry of the transaction. |
| 6 | `SECTRAS.FEES.AUTHORISATION.DATE` | `DesctxAllinfeesTransactions_AuthorisationDate` | TField |  | This field holds the date of authorisation of the transaction. |
| 7 | `SECTRAS.FEES.VALUE.DATE` | `DesctxAllinfeesTransactions_ValueDate` | TField |  | This field holds the value date of the transaction. |
| 8 | `SECTRAS.FEES.LOCAL.REF` | `DesctxAllinfeesTransactions_LocalRef` |  |  |  |
| 9 | `SECTRAS.FEES.RECORD.STATUS` | `DesctxAllinfeesTransactions_RecordStatus` | String |  |  |
| 10 | `SECTRAS.FEES.CURR.NO` | `DesctxAllinfeesTransactions_CurrNo` | String |  |  |
| 11 | `SECTRAS.FEES.INPUTTER` | `DesctxAllinfeesTransactions_Inputter` |  |  |  |
| 12 | `SECTRAS.FEES.DATE.TIME` | `DesctxAllinfeesTransactions_DateTime` |  |  |  |
| 13 | `SECTRAS.FEES.AUTHORISER` | `DesctxAllinfeesTransactions_Authoriser` | String |  |  |
| 14 | `SECTRAS.FEES.CO.CODE` | `DesctxAllinfeesTransactions_CoCode` | String |  |  |
| 15 | `SECTRAS.FEES.DEPT.CODE` | `DesctxAllinfeesTransactions_DeptCode` | String |  |  |
| 16 | `SECTRAS.FEES.AUDITOR.CODE` | `DesctxAllinfeesTransactions_AuditorCode` | String |  |  |
| 17 | `SECTRAS.FEES.AUDIT.DATE.TIME` | `DesctxAllinfeesTransactions_AuditDateTime` | String |  |  |
