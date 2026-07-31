# PPADBR.DEBIN.REGISTRATION — Table Schema

> Source: `INSERTS/I_F.PPADBR.DEBIN.REGISTRATION` in `PPADBR_DebinRegistration.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `DR.CUSTOMER.ID` | `PpadbrDebinRegistration_CustomerId` | TField |  | Customer registering for DEBIN services. He could be a Buyer or seller depending on the field 'Role' |
| 2 | `DR.ROLE` | `PpadbrDebinRegistration_Role` | TField |  | Flag to denote the role of the DEBIN participant |
| 3 | `DR.LEGAL.DOC.NO` | `PpadbrDebinRegistration_LegalDocNo` | TField |  | Document reference of the DEBIN participant |
| 4 | `DR.CBU.ACCOUNT.NO` | `PpadbrDebinRegistration_CbuAccountNo` | TField | Yes | CBU number of the DEBIN participant. Mandatory input |
| 5 | `DR.CUST.BANK.CODE` | `PpadbrDebinRegistration_CustBankCode` | TField |  | Bank code of the CBU number. Will be defaulted from 1st three positions of 'CBU Number' |
| 6 | `DR.CUST.BRANCH.CODE` | `PpadbrDebinRegistration_CustBranchCode` | TField |  | Branch code of CBU number. Will be defaulted from 4th-8th position of 'CBU Number' |
| 7 | `DR.ACCOUNT.NAME` | `PpadbrDebinRegistration_AccountName` | TField |  | Name of the Customer registered to DEBIN service |
| 8 | `DR.ACCOUNT.SUR.NAME` | `PpadbrDebinRegistration_AccountSurName` | TField |  | Surname of the Customer registered to DEBIN service |
| 9 | `DR.CUSTOMER.EMAIL` | `PpadbrDebinRegistration_CustomerEmail` | TField |  | Email of the Customer registered to DEBIN service |
| 10 | `DR.SELLER.LIMIT.CCY` | `PpadbrDebinRegistration_SellerLimitCcy` |  |  |  |
| 11 | `DR.SELLER.LIMIT.AMT` | `PpadbrDebinRegistration_SellerLimitAmt` |  |  |  |
| 12 | `DR.SELLER.NO.OF.TXNS` | `PpadbrDebinRegistration_SellerNoOfTxns` |  |  |  |
| 13 | `DR.AUTO.ACCEPT.SELLER.REF` | `PpadbrDebinRegistration_AutoAcceptSellerRef` |  |  |  |
| 14 | `DR.AUTO.ACCEPT.CCY` | `PpadbrDebinRegistration_AutoAcceptCcy` |  |  |  |
| 15 | `DR.AUTO.ACCEPT.AMT` | `PpadbrDebinRegistration_AutoAcceptAmt` |  |  |  |
| 16 | `DR.RESERVED.15` | `PpadbrDebinRegistration_Reserved15` |  |  |  |
| 17 | `DR.RESERVED.14` | `PpadbrDebinRegistration_Reserved14` |  |  |  |
| 18 | `DR.RESERVED.13` | `PpadbrDebinRegistration_Reserved13` |  |  |  |
| 19 | `DR.RESERVED.12` | `PpadbrDebinRegistration_Reserved12` |  |  |  |
| 20 | `DR.RESERVED.11` | `PpadbrDebinRegistration_Reserved11` |  |  |  |
| 21 | `DR.ACTION` | `PpadbrDebinRegistration_Action` | TField |  | Field for user to perform necessary operations - De-register, Re-activation and define Seller Limits. Option Seller limit will be allowed only for Seller |
| 22 | `DR.STATUS` | `PpadbrDebinRegistration_Status` | TField |  | Status of the DEBIN registration is available in this field. Noinput field for the user |
| 23 | `DR.STATUS.DATE` | `PpadbrDebinRegistration_StatusDate` | TField |  | The date of the respective status update is available in this field. Noinput field for the user |
| 24 | `DR.RESPONSE.CODE` | `PpadbrDebinRegistration_ResponseCode` | TField |  | Response code from clearing house (COELSA) is updated in this field using API. Noinput field for the user |
| 25 | `DR.RESPONSE.DESC` | `PpadbrDebinRegistration_ResponseDesc` | TField |  | Response description from clearing house (COELSA) is updated in this field using API. Noinput field for the user |
| 26 | `DR.RESERVED.10` | `PpadbrDebinRegistration_Reserved10` | TField |  |  |
| 27 | `DR.RESERVED.9` | `PpadbrDebinRegistration_Reserved9` | TField |  |  |
| 28 | `DR.RESERVED.8` | `PpadbrDebinRegistration_Reserved8` | TField |  |  |
| 29 | `DR.RESERVED.7` | `PpadbrDebinRegistration_Reserved7` | TField |  |  |
| 30 | `DR.RESERVED.6` | `PpadbrDebinRegistration_Reserved6` | TField |  |  |
| 31 | `DR.RESERVED.5` | `PpadbrDebinRegistration_Reserved5` | TField |  |  |
| 32 | `DR.RESERVED.4` | `PpadbrDebinRegistration_Reserved4` | TField |  |  |
| 33 | `DR.RESERVED.3` | `PpadbrDebinRegistration_Reserved3` | TField |  |  |
| 34 | `DR.RESERVED.2` | `PpadbrDebinRegistration_Reserved2` | TField |  |  |
| 35 | `DR.RESERVED.1` | `PpadbrDebinRegistration_Reserved1` | TField |  |  |
| 36 | `DR.LOCAL.REF` | `PpadbrDebinRegistration_LocalRef` |  |  |  |
| 37 | `DR.OVERRIDE` | `PpadbrDebinRegistration_Override` |  |  |  |
| 38 | `DR.RECORD.STATUS` | `PpadbrDebinRegistration_RecordStatus` | String |  |  |
| 39 | `DR.CURR.NO` | `PpadbrDebinRegistration_CurrNo` | String |  |  |
| 40 | `DR.INPUTTER` | `PpadbrDebinRegistration_Inputter` |  |  |  |
| 41 | `DR.DATE.TIME` | `PpadbrDebinRegistration_DateTime` |  |  |  |
| 42 | `DR.AUTHORISER` | `PpadbrDebinRegistration_Authoriser` | String |  |  |
| 43 | `DR.CO.CODE` | `PpadbrDebinRegistration_CoCode` | String |  |  |
| 44 | `DR.DEPT.CODE` | `PpadbrDebinRegistration_DeptCode` | String |  |  |
| 45 | `DR.AUDITOR.CODE` | `PpadbrDebinRegistration_AuditorCode` | String |  |  |
| 46 | `DR.AUDIT.DATE.TIME` | `PpadbrDebinRegistration_AuditDateTime` | String |  |  |
