# CUSTOMER.MASS.BLOCK — Table Schema

> Source: `INSERTS/I_F.CUSTOMER.MASS.BLOCK` in `AC_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CMB.BLOCKING.REASON` | `CustomerMassBlock_BlockingReason` |  |  |  |
| 2 | `CMB.POSTING.RESTRICT` | `CustomerMassBlock_PostingRestrict` | TField | Yes | This is the code by which the Posting Restriction details can be identified. This restriction will be applied for all customers/accounts matching the block conditions Certain ranges of Posting Restriction Codes have a predefined purpose and should not be used for anything else. At present these are as follows: 80-89 PENDING CLOSURE Used to indicate Accounts which will be closed soon, but are not to be closed automatically yet. 90-99 AUTOMATIC CLOSING Used to indicate Accounts which should be closed automatically as soon as all Balances are zero. Validation Rules: 1 to 4 numeric characters based on EB.OBJECT. (Mandatory input) Must be a valid record in POSTING.RESTRICTION table Restrictions defined for AUTOMATIC.CLOSING will not be accepted as valid input |
| 3 | `CMB.BLOCKING.CODE` | `CustomerMassBlock_BlockingCode` | TField | Yes | Used to specify the blocking reason in terms of identifiable code. Validation Rules: EB.LOOKUP field with key as "BLOCKING.CODE" Should have already lined in POSTING.RESTRICT defined Mandatory field |
| 4 | `CMB.START.DATE` | `CustomerMassBlock_StartDate` | TField | Yes | Contains the date from which restriction has to be applied. Validation Rules: Standard Date field, hence date validations are applied. Back dated value not accepted, i.e Date must not be less than today's date Mandatory field |
| 5 | `CMB.EXPIRY.DATE` | `CustomerMassBlock_ExpiryDate` | TField | Yes | Contains the expiry date of the record from which restriction has to be relaxed. Validation Rules: Standard Date field, hence date validations are applied. Date must be greater than START.DATE For existing record date can be entered as TODAY, then block will expire immediately Mandatory field |
| 6 | `CMB.UNBLOCKING.CODE` | `CustomerMassBlock_UnblockingCode` | TField |  | Should be entered when block expiry date is reduced Validation Rules: Should have already lined in POSTING.RESTRICT defined |
| 7 | `CMB.UNBLOCKING.REASON` | `CustomerMassBlock_UnblockingReason` | A (alphanumeric) | Yes | Free text field to define reason for unblocking the customers/accounts Validation Rules: Up to 100 type A (alphanumeric) characters (Non Mandatory Field) |
| 8 | `CMB.BLOCKING.TYPE` | `CustomerMassBlock_BlockingType` | TField | Yes | Defines whether the block is on specific customers mentioned in CUSTOMER.ID field or for range of customer matching selection condition Validation Rules: Option field with INDIVIDUAL or RANGE as values. Mandatory field |
| 9 | `CMB.CUSTOMER.ID` | `CustomerMassBlock_CustomerId` |  |  |  |
| 10 | `CMB.CUS.RESERVED.4` | `CustomerMassBlock_CusReserved4` |  |  |  |
| 11 | `CMB.CUS.RESERVED.3` | `CustomerMassBlock_CusReserved3` |  |  |  |
| 12 | `CMB.CUS.RESERVED.2` | `CustomerMassBlock_CusReserved2` |  |  |  |
| 13 | `CMB.CUS.RESERVED.1` | `CustomerMassBlock_CusReserved1` |  |  |  |
| 14 | `CMB.INCLUDE.AC.ACCOUNTS` | `CustomerMassBlock_IncludeAcAccounts` | TField | Yes | Represents if the block is to be applied for legacy accounts or only to arrangement accounts. If this field is set to YES, then the block will apply to all types of accounts If this field is set to blank/null, then the block will apply to only arrangement accounts Validation Rules: Only option allowed 'Yes' - (Non Mandatory Field) |
| 15 | `CMB.SEL.APPLICATION` | `CustomerMassBlock_SelApplication` | TField | Yes | Used to mass block range of CUSTOMER or ACCOUNT that are matching with the selection criteria Validation Rules: Option Field, allowed values: CUSTOMER or ACCOUNT. Mandatory field when BLOCKING.TYPE is chosen as RANGE, otherwise not allowed |
| 16 | `CMB.SEL.FIELD` | `CustomerMassBlock_SelField` |  |  |  |
| 17 | `CMB.SEL.VALUE` | `CustomerMassBlock_SelValue` |  |  |  |
| 18 | `CMB.SEL.RESERVED.5` | `CustomerMassBlock_SelReserved5` |  |  |  |
| 19 | `CMB.SEL.RESERVED.4` | `CustomerMassBlock_SelReserved4` |  |  |  |
| 20 | `CMB.SEL.RESERVED.3` | `CustomerMassBlock_SelReserved3` |  |  |  |
| 21 | `CMB.SEL.RESERVED.2` | `CustomerMassBlock_SelReserved2` |  |  |  |
| 22 | `CMB.SEL.RESERVED.1` | `CustomerMassBlock_SelReserved1` |  |  |  |
| 23 | `CMB.DEFINE.EXCLUSION` | `CustomerMassBlock_DefineExclusion` | TField | Yes | Field represents if the exclusion needs to be done through a fast-path enquiry which will list all the customer/accounts that will fall under the selection criteria If this field is set to YES and record is Committed then system would automatically force the record to be put on hold and auto launches a fast-path enquiry where user will be able to select the account/customer to be excluded from the block Once the exclusion is completed from the fast-path enquiry user needs to re-open the customer mass block record and all the excluded accounts/customer information will be updated to the mass block record by the system, user can still add/remove the exclusion informtion and commit the record Validation Rules: Only option allowed 'Yes' - (Non Mandatory Field) |
| 24 | `CMB.EX.UN.CUSTOMER.ID` | `CustomerMassBlock_ExUnCustomerId` |  |  |  |
| 25 | `CMB.EXCLUDE.CUSTOMER` | `CustomerMassBlock_ExcludeCustomer` |  |  |  |
| 26 | `CMB.CU.EXPIRY.DATE` | `CustomerMassBlock_CuExpiryDate` |  |  |  |
| 27 | `CMB.CU.UNBLOCKING.CODE` | `CustomerMassBlock_CuUnblockingCode` |  |  |  |
| 28 | `CMB.CU.UNBLOCKING.REASON` | `CustomerMassBlock_CuUnblockingReason` |  |  |  |
| 29 | `CMB.FILTER.RESERVED.2` | `CustomerMassBlock_FilterReserved2` |  |  |  |
| 30 | `CMB.EX.UN.ACCOUNT.ID` | `CustomerMassBlock_ExUnAccountId` |  |  |  |
| 31 | `CMB.EXCLUDE.ACCOUNT` | `CustomerMassBlock_ExcludeAccount` |  |  |  |
| 32 | `CMB.AC.EXPIRY.DATE` | `CustomerMassBlock_AcExpiryDate` |  |  |  |
| 33 | `CMB.AC.UNBLOCKING.CODE` | `CustomerMassBlock_AcUnblockingCode` |  |  |  |
| 34 | `CMB.AC.UNBLOCKING.REASON` | `CustomerMassBlock_AcUnblockingReason` |  |  |  |
| 35 | `CMB.UN.ACCT.RESERVED.5` | `CustomerMassBlock_UnAcctReserved5` |  |  |  |
| 36 | `CMB.UN.ACCT.RESERVED.4` | `CustomerMassBlock_UnAcctReserved4` |  |  |  |
| 37 | `CMB.UN.ACCT.RESERVED.3` | `CustomerMassBlock_UnAcctReserved3` |  |  |  |
| 38 | `CMB.UN.ACCT.RESERVED.2` | `CustomerMassBlock_UnAcctReserved2` |  |  |  |
| 39 | `CMB.UN.ACCT.RESERVED.1` | `CustomerMassBlock_UnAcctReserved1` |  |  |  |
| 40 | `CMB.UN.CUST.RESERVED.5` | `CustomerMassBlock_UnCustReserved5` |  |  |  |
| 41 | `CMB.UN.CUST.RESERVED.4` | `CustomerMassBlock_UnCustReserved4` |  |  |  |
| 42 | `CMB.UN.CUST.RESERVED.3` | `CustomerMassBlock_UnCustReserved3` |  |  |  |
| 43 | `CMB.UN.CUST.RESERVED.2` | `CustomerMassBlock_UnCustReserved2` |  |  |  |
| 44 | `CMB.UN.CUST.RESERVED.1` | `CustomerMassBlock_UnCustReserved1` |  |  |  |
| 45 | `CMB.START.NOTIFY.DAYS` | `CustomerMassBlock_StartNotifyDays` | TField | Yes | Represents the number of working days prior to start of a scheduled block, system should trigger an event and subsequently change the block status from FORWARD to FORWARD-NOTIFIED. Working days will be refereded to the Holiday table of the company(lead company) under which the block is being created Validation Rules: Accepts Numeric Vales - (Non Mandatory Field) |
| 46 | `CMB.EXPIRY.NOTIFY.DAYS` | `CustomerMassBlock_ExpiryNotifyDays` | TField | Yes | Represents the number of working days prior to expiry of a block system should trigger an event and subsequently change the block status from CURRENT to EXPIRY-NOTIFIED. Working days will be refereded to the Holiday table of the company(lead company) under which the block is being created Validation Rules: Accepts Numeric Vales - (Non Mandatory Field) |
| 47 | `CMB.NEXT.EVENT.DATE` | `CustomerMassBlock_NextEventDate` | TField |  | Holds the date on which the next scheduled event would be triggered for the block record. Validation Rules: NO-INPUT field |
| 48 | `CMB.BLOCK.STATUS` | `CustomerMassBlock_BlockStatus` | TField |  | Holds the current status of the block. List of status are Forward, Forward-Notified, Current, Expiry-Notified, Expired and Reversed. Validation Rules: NO-INPUT field |
| 49 | `CMB.AA.BUNDLE.ID` | `CustomerMassBlock_AaBundleId` | TField |  | Specifies an arrangement reference that belongs to the BUNDLE product line. Validation Rules: Must be a valid Arrangement Bundle |
| 50 | `CMB.RESERVED.4` | `CustomerMassBlock_Reserved4` | TField |  |  |
| 51 | `CMB.RESERVED.3` | `CustomerMassBlock_Reserved3` | TField |  |  |
| 52 | `CMB.RESERVED.2` | `CustomerMassBlock_Reserved2` | TField |  |  |
| 53 | `CMB.RESERVED.1` | `CustomerMassBlock_Reserved1` | TField |  |  |
| 54 | `CMB.LOCAL.REF` | `CustomerMassBlock_LocalRef` |  |  |  |
| 55 | `CMB.OVERRIDE` | `CustomerMassBlock_Override` |  |  |  |
| 56 | `CMB.RECORD.STATUS` | `CustomerMassBlock_RecordStatus` | String |  |  |
| 57 | `CMB.CURR.NO` | `CustomerMassBlock_CurrNo` | String |  |  |
| 58 | `CMB.INPUTTER` | `CustomerMassBlock_Inputter` |  |  |  |
| 59 | `CMB.DATE.TIME` | `CustomerMassBlock_DateTime` |  |  |  |
| 60 | `CMB.AUTHORISER` | `CustomerMassBlock_Authoriser` | String |  |  |
| 61 | `CMB.CO.CODE` | `CustomerMassBlock_CoCode` | String |  |  |
| 62 | `CMB.DEPT.CODE` | `CustomerMassBlock_DeptCode` | String |  |  |
| 63 | `CMB.AUDITOR.CODE` | `CustomerMassBlock_AuditorCode` | String |  |  |
| 64 | `CMB.AUDIT.DATE.TIME` | `CustomerMassBlock_AuditDateTime` | String |  |  |
