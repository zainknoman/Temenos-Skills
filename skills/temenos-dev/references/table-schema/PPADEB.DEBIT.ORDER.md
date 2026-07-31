# PPADEB.DEBIT.ORDER — Table Schema

> Source: `INSERTS/I_F.PPADEB.DEBIT.ORDER` in `PPADEB_DebitOrder.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PPDOR.DEBIT.ORDER.PRODUCT` | `PpadebDebitOrder_DebitOrderProduct` | TField | Yes | Should be a valid Debit order product. Mandatory field. |
| 2 | `PPDOR.CREDIT.PARTY.REFERENCE` | `PpadebDebitOrder_CreditPartyReference` | TField |  | Credit party reference such as legal document number, CUIT etc.. |
| 3 | `PPDOR.CREDIT.ACCOUNT.NUMBER` | `PpadebDebitOrder_CreditAccountNumber` | TField |  | Alternate ID of the credit account number. The alternate key will be a valid record in ALT.ACCT.PARAMETER |
| 4 | `PPDOR.CREDIT.PARTY.BANK.CODE` | `PpadebDebitOrder_CreditPartyBankCode` | TField |  | Bank code of the credit account number |
| 5 | `PPDOR.CREDIT.PARTY.BRANCH.CODE` | `PpadebDebitOrder_CreditPartyBranchCode` | TField |  | Branch code of the credit account number |
| 6 | `PPDOR.CREDIT.ACCOUNT.CURRENCY` | `PpadebDebitOrder_CreditAccountCurrency` | TField |  | Currency of the credit account number |
| 7 | `PPDOR.CREDIT.PARTY.TERMINAL.CODE` | `PpadebDebitOrder_CreditPartyTerminalCode` | TField |  | Terminal code of the credit account. Stored for information purposes |
| 8 | `PPDOR.CREDIT.ACCOUNT.ALIAS` | `PpadebDebitOrder_CreditAccountAlias` | TField |  | Alias of the credit account number |
| 9 | `PPDOR.CREDIT.ACCOUNT.TYPE` | `PpadebDebitOrder_CreditAccountType` | TField |  | Account type of the credit account number |
| 10 | `PPDOR.CREDIT.PARTY.NAME` | `PpadebDebitOrder_CreditPartyName` | TField |  | Credit party Name. |
| 11 | `PPDOR.DEBIT.PARTY.REFERENCE` | `PpadebDebitOrder_DebitPartyReference` | TField |  | Debit party reference such as legal document number, CUIT etc.. |
| 12 | `PPDOR.DEBIT.ACCOUNT.NUMBER` | `PpadebDebitOrder_DebitAccountNumber` | TField |  | Alternate ID of the Debit account number. The alternate key will be a valid record in ALT.ACCT.PARAMETER |
| 13 | `PPDOR.DEBIT.PARTY.BANK.CODE` | `PpadebDebitOrder_DebitPartyBankCode` | TField |  | Bank code of the debit account number |
| 14 | `PPDOR.DEBIT.PARTY.BRANCH.CODE` | `PpadebDebitOrder_DebitPartyBranchCode` | TField |  | Branch code of the debit account number |
| 15 | `PPDOR.DEBIT.ACCOUNT.ALIAS` | `PpadebDebitOrder_DebitAccountAlias` | TField |  | Alias of the debit account number |
| 16 | `PPDOR.DEBIT.ACCOUNT.CURRENCY` | `PpadebDebitOrder_DebitAccountCurrency` | TField |  | Currency of the debit account number |
| 17 | `PPDOR.DEBIT.ACCOUNT.TYPE` | `PpadebDebitOrder_DebitAccountType` | TField |  | Account type of the debit account number |
| 18 | `PPDOR.DEBIT.PARTY.NAME` | `PpadebDebitOrder_DebitPartyName` | TField |  | Debit Party Name |
| 19 | `PPDOR.NARRATIVE` | `PpadebDebitOrder_Narrative` | TField |  | Description field to provide other information |
| 20 | `PPDOR.REQUEST.PURPOSE` | `PpadebDebitOrder_RequestPurpose` | TField |  | Field to capture the purpose of the transaction |
| 21 | `PPDOR.REQUEST.CURRENCY` | `PpadebDebitOrder_RequestCurrency` | TField |  | Currency of the transaction |
| 22 | `PPDOR.REQUEST.AMOUNT` | `PpadebDebitOrder_RequestAmount` | TField |  | Amount requested by the credit party (requestor) |
| 23 | `PPDOR.REQUEST.VALIDITY` | `PpadebDebitOrder_RequestValidity` | TField |  | Validity period of the transaction. This value will be entered by the requestor (credit party) while initiation a debit order request. |
| 24 | `PPDOR.STATUS` | `PpadebDebitOrder_Status` | TField |  | Status of the Debit order transaction |
| 25 | `PPDOR.STATUS.DESCRIPTION` | `PpadebDebitOrder_StatusDescription` | TField |  | Description of the status. |
| 26 | `PPDOR.STATUS.DATE` | `PpadebDebitOrder_StatusDate` | TField |  | The date of the respective status update is available in this field. |
| 27 | `PPDOR.RESPONSE.CODE` | `PpadebDebitOrder_ResponseCode` | TField |  | Response code from clearing house or the error code that has to be sent to clearing house is updated in this field. If a record is committed with a value in this field, an IF event will be emitted |
| 28 | `PPDOR.RESPONSE.DESCRIPTION` | `PpadebDebitOrder_ResponseDescription` | TField |  | Response description from clearing house |
| 29 | `PPDOR.TRANSACTION.REFERENCE` | `PpadebDebitOrder_TransactionReference` | TField |  | End to end reference of the transaction |
| 30 | `PPDOR.CREATION.DATE` | `PpadebDebitOrder_CreationDate` | TField |  | Date of debit order creation in UTC format |
| 31 | `PPDOR.EXPIRY.DATE.TIME` | `PpadebDebitOrder_ExpiryDateTime` |  |  |  |
| 32 | `PPDOR.SUSPICIOUS.ACTIVITY.SCORE` | `PpadebDebitOrder_SuspiciousActivityScore` | TField |  | Field to store the scoring suspicious activity received from clearing. |
| 33 | `PPDOR.SUSPICIOUS.ACTIVITY.RULES` | `PpadebDebitOrder_SuspiciousActivityRules` | TField |  | Description field to capture the rules on suspicious activity received from clearing. |
| 34 | `PPDOR.DIRECTION` | `PpadebDebitOrder_Direction` | TField |  | Direction of the debit order. Inward - Incoming debit order request to the debtor Outward - Outward debit order request initiated by the requestor (credit party). |
| 35 | `PPDOR.BUSINESS.DATE` | `PpadebDebitOrder_BusinessDate` | TField |  | Field to store the business date provided by clearing |
| 36 | `PPDOR.OPERATION` | `PpadebDebitOrder_Operation` | TField |  | Field for user to perform necessary operations Accept - Debtor to accept the incoming debit order request Reject - Debtor to reject the incoming debit order request Cancel - Requestor to cancel the debit order initiated. Cancellation can only be triggered if there is no underlying payment in TPH. |
| 37 | `PPDOR.REJECTION.REASON` | `PpadebDebitOrder_RejectionReason` | TField | Yes | Field for mentioning the reason for rejection. Mandatory field when field 'Operation' = 'Reject' |
| 38 | `PPDOR.AUTO.ACCEPT` | `PpadebDebitOrder_AutoAccept` | TField |  | Field for denoting that the transaction has been auto-accepted. Valid only for incoming debit order requests. This field will be set to Yes by the system if the auto-acceptance conditions defined in field 'Auto Acceptance API' of debit order product table are satisfied. No input field for the user. |
| 39 | `PPDOR.LATITUDE` | `PpadebDebitOrder_Latitude` | TField |  | Field to update the Latitude |
| 40 | `PPDOR.LONGITUDE` | `PpadebDebitOrder_Longitude` | TField |  | Field to update the Longitude |
| 41 | `PPDOR.OPERATION.BY.SAME.PERSON` | `PpadebDebitOrder_OperationBySamePerson` | TField |  | Field to denote if the transaction is performed by the same person. This field is updated with the value sent from the clearing house and stored for information purpose only. |
| 42 | `PPDOR.ENROLLMENT.STATUS` | `PpadebDebitOrder_EnrollmentStatus` | TField |  | Field to denote the enrollment status of the customer. This field is updated with the value sent from the clearing house and stored for information purpose only. |
| 43 | `PPDOR.PREAUTHORIZATION` | `PpadebDebitOrder_Preauthorization` | TField |  |  |
| 44 | `PPDOR.SELLER.DESCRIPTION` | `PpadebDebitOrder_SellerDescription` | TField |  | Free text field for storing requestor information |
| 45 | `PPDOR.IP.ADDRESS` | `PpadebDebitOrder_IpAddress` | TField |  | Field to store the IP address of the customer initiating the debit order |
| 46 | `PPDOR.DEVICE.TYPE` | `PpadebDebitOrder_DeviceType` | TField |  | Field to indicate the device type used by the requestor to initiate a debit order request. Information field provided by channels. |
| 47 | `PPDOR.OPERATING.SYSTEM` | `PpadebDebitOrder_OperatingSystem` | TField |  | Field to indicate the operation system used by the requestor to initiate a debit order request. Information field provided by channels. |
| 48 | `PPDOR.SIM.CODE` | `PpadebDebitOrder_SimCode` | TField |  | Field to store the SIM code |
| 49 | `PPDOR.IMEI.CODE` | `PpadebDebitOrder_ImeiCode` | TField |  | Field to store the IMEI code of the device |
| 50 | `PPDOR.MAX.DATE.TO.BE.REVERSED` | `PpadebDebitOrder_MaxDateToBeReversed` | TField |  | Field to indicate upto which date the transaction can be reversed. |
| 51 | `PPDOR.NARRATIVE.OF.THE.CHARGEBACK` | `PpadebDebitOrder_NarrativeOfTheChargeback` | TField |  | Reason to initiate the chargeback. |
| 52 | `PPDOR.CHARGEBACK.ID` | `PpadebDebitOrder_ChargebackId` | TField |  | ID of the chargeback. This chargeback ID field is used to store the reference from COELSA |
| 53 | `PPDOR.CHARGEBACK.STATUS` | `PpadebDebitOrder_ChargebackStatus` | TField |  | Status of the chargeback. This chargeback status field will be updated based on the response from COELSA |
| 54 | `PPDOR.RECURRENCE` | `PpadebDebitOrder_Recurrence` | TField |  | Indicates whether it is a Recurrent debit order - auto-accepted by the Buyer or Spot debit order - manually accepted by the Buyer.'True' implies Recurrent debit Order.'False' implies Spot debit Order. |
| 55 | `PPDOR.RECURRENCE.ID` | `PpadebDebitOrder_RecurrenceId` | TField | Yes | Indicates the ID of recurrence registration. This should be a valid COELSA Recurrence ID.Mandatory when Recurrence = 'True'. Non-input when Recurrence = 'False' |
| 56 | `PPDOR.BENEFIT` | `PpadebDebitOrder_Benefit` | TField |  | Indicates the unique benefit name for a seller.This should be auto-populated based on the Recurrence ID. |
| 57 | `PPDOR.RESERVED.3` | `PpadebDebitOrder_Reserved3` | TField |  |  |
| 58 | `PPDOR.RESERVED.2` | `PpadebDebitOrder_Reserved2` | TField |  |  |
| 59 | `PPDOR.RESERVED.1` | `PpadebDebitOrder_Reserved1` | TField |  |  |
| 60 | `PPDOR.LOCAL.REF` | `PpadebDebitOrder_LocalRef` |  |  |  |
| 61 | `PPDOR.OVERRIDE` | `PpadebDebitOrder_Override` |  |  |  |
| 62 | `PPDOR.RECORD.STATUS` | `PpadebDebitOrder_RecordStatus` | String |  |  |
| 63 | `PPDOR.CURR.NO` | `PpadebDebitOrder_CurrNo` | String |  |  |
| 64 | `PPDOR.INPUTTER` | `PpadebDebitOrder_Inputter` |  |  |  |
| 65 | `PPDOR.DATE.TIME` | `PpadebDebitOrder_DateTime` |  |  |  |
| 66 | `PPDOR.AUTHORISER` | `PpadebDebitOrder_Authoriser` | String |  |  |
| 67 | `PPDOR.CO.CODE` | `PpadebDebitOrder_CoCode` | String |  |  |
| 68 | `PPDOR.DEPT.CODE` | `PpadebDebitOrder_DeptCode` | String |  |  |
| 69 | `PPDOR.AUDITOR.CODE` | `PpadebDebitOrder_AuditorCode` | String |  |  |
| 70 | `PPDOR.AUDIT.DATE.TIME` | `PpadebDebitOrder_AuditDateTime` | String |  |  |
| 71 | `PPDOR.CREDIT.CUSTOMER.ID` | `PpadebDebitOrder_CreditCustomerId` | TField |  | ID of the Customer to whom the Account belongs |
