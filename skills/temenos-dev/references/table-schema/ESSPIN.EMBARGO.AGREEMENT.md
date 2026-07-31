# ESSPIN.EMBARGO.AGREEMENT — Table Schema

> Source: `INSERTS/I_F.ESSPIN.EMBARGO.AGREEMENT` in `ESSPIN_EmbargoInterface.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ESSPIN.CUSTOMER.ID` | `EsspinEmbargoAgreement_CustomerId` | TField |  | It is the T24 Customer ID of Creditor |
| 2 | `ESSPIN.CONTRACT.IDENTIFIER` | `EsspinEmbargoAgreement_ContractIdentifier` | TField |  |  |
| 3 | `ESSPIN.ENTITY.T24.ACCOUNT` | `EsspinEmbargoAgreement_EntityT24Account` | TField |  | Creditor account held in T24 Bank. If there is an account mentioned in this field, then this takes precedence andembargo amount will be credited to this account. Should be a valid T24 account number. |
| 4 | `ESSPIN.ENTITY.EXT.ACCOUNT` | `EsspinEmbargoAgreement_EntityExtAccount` | TField |  | Creditor account held in other bank. This will be the ultimate account to which embargo amount should be credited.This is captured in this table for information purpose. |
| 5 | `ESSPIN.SINGLE.CREDIT` | `EsspinEmbargoAgreement_SingleCredit` | TField |  | Yes, means (Creditor) entity wants all the embargo credits done during the day to be transferred as single (bulk) credit to its account.No, means (Creditor) entity wants all the embargo credits done are transferred for each corresponding single debit in (Debtor) customer account. Default option is No |
| 6 | `ESSPIN.INTERNAL.ACCOUNT` | `EsspinEmbargoAgreement_InternalAccount` | TField |  | Internal (wash through) account used to park the embargo amount in case creditor does not have T24 account. |
| 7 | `ESSPIN.ENTITY.TYPE` | `EsspinEmbargoAgreement_EntityType` | TField |  | This field holds value as'Regional,'National','Others' |
| 8 | `ESSPIN.START.DATE` | `EsspinEmbargoAgreement_StartDate` | TField |  | The starting date of contract between the creditor and entity bank. |
| 9 | `ESSPIN.END.DATE` | `EsspinEmbargoAgreement_EndDate` | TField |  | The end date of the contract between the creditor and entity bank |
| 10 | `ESSPIN.EMBARGO.PERIOD` | `EsspinEmbargoAgreement_EmbargoPeriod` | TField |  | The period in days the amount blocked in customer account by the creditor |
| 11 | `ESSPIN.DEBIT.CUST.TERM` | `EsspinEmbargoAgreement_DebitCustTerm` | TField |  | Number of days debtor bank can float the blocked funds |
| 12 | `ESSPIN.CURRENCY` | `EsspinEmbargoAgreement_Currency` |  |  |  |
| 13 | `ESSPIN.MIN.AMOUNT` | `EsspinEmbargoAgreement_MinAmount` |  |  |  |
| 14 | `ESSPIN.MAX.AMOUNT` | `EsspinEmbargoAgreement_MaxAmount` |  |  |  |
| 15 | `ESSPIN.COMMUNICATION.CODE` | `EsspinEmbargoAgreement_CommunicationCode` | TField |  | To store internal information by the creditor |
| 16 | `ESSPIN.COMMUNICATION.TYPE` | `EsspinEmbargoAgreement_CommunicationType` | TField |  | To store internal information by the creditor |
| 17 | `ESSPIN.LOCAL.REF` | `EsspinEmbargoAgreement_LocalRef` |  |  |  |
| 18 | `ESSPIN.CREDIT.TYPE` | `EsspinEmbargoAgreement_CreditType` | TField |  |  |
| 19 | `ESSPIN.RESERVED.2` | `EsspinEmbargoAgreement_Reserved2` | TField |  |  |
| 20 | `ESSPIN.RESERVED.3` | `EsspinEmbargoAgreement_Reserved3` | TField |  |  |
| 21 | `ESSPIN.RESERVED.4` | `EsspinEmbargoAgreement_Reserved4` | TField |  |  |
| 22 | `ESSPIN.RESERVED.5` | `EsspinEmbargoAgreement_Reserved5` | TField |  |  |
| 23 | `ESSPIN.RESERVED.6` | `EsspinEmbargoAgreement_Reserved6` | TField |  |  |
| 24 | `ESSPIN.RESERVED.7` | `EsspinEmbargoAgreement_Reserved7` | TField |  |  |
| 25 | `ESSPIN.RESERVED.8` | `EsspinEmbargoAgreement_Reserved8` | TField |  |  |
| 26 | `ESSPIN.RESERVED.9` | `EsspinEmbargoAgreement_Reserved9` | TField |  |  |
| 27 | `ESSPIN.RESERVED.10` | `EsspinEmbargoAgreement_Reserved10` | TField |  |  |
| 28 | `ESSPIN.RESERVED.11` | `EsspinEmbargoAgreement_Reserved11` | TField |  |  |
| 29 | `ESSPIN.RESERVED.12` | `EsspinEmbargoAgreement_Reserved12` | TField |  |  |
| 30 | `ESSPIN.RESERVED.13` | `EsspinEmbargoAgreement_Reserved13` | TField |  |  |
| 31 | `ESSPIN.RESERVED.14` | `EsspinEmbargoAgreement_Reserved14` | TField |  |  |
| 32 | `ESSPIN.RESERVED.15` | `EsspinEmbargoAgreement_Reserved15` | TField |  |  |
| 33 | `ESSPIN.OVERRIDE` | `EsspinEmbargoAgreement_Override` |  |  |  |
| 34 | `ESSPIN.RECORD.STATUS` | `EsspinEmbargoAgreement_RecordStatus` | String |  |  |
| 35 | `ESSPIN.CURR.NO` | `EsspinEmbargoAgreement_CurrNo` | String |  |  |
| 36 | `ESSPIN.INPUTTER` | `EsspinEmbargoAgreement_Inputter` |  |  |  |
| 37 | `ESSPIN.DATE.TIME` | `EsspinEmbargoAgreement_DateTime` |  |  |  |
| 38 | `ESSPIN.AUTHORISER` | `EsspinEmbargoAgreement_Authoriser` | String |  |  |
| 39 | `ESSPIN.CO.CODE` | `EsspinEmbargoAgreement_CoCode` | String |  |  |
| 40 | `ESSPIN.DEPT.CODE` | `EsspinEmbargoAgreement_DeptCode` | String |  |  |
| 41 | `ESSPIN.AUDITOR.CODE` | `EsspinEmbargoAgreement_AuditorCode` | String |  |  |
| 42 | `ESSPIN.AUDIT.DATE.TIME` | `EsspinEmbargoAgreement_AuditDateTime` | String |  |  |
