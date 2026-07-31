# USRETL.CHECK.COLLECTION — Table Schema

> Source: `INSERTS/I_F.USRETL.CHECK.COLLECTION` in `USRETL_CheckCollection.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USCKC.ACCOUNT.NUMBER` | `UsretlCheckCollection_AccountNumber` | TField |  | Account Number printed on check. First segment of &amp;ID. This is a noinput field and defaulted from &amp;ID |
| 2 | `USCKC.ACCOUNT.COMPANY` | `UsretlCheckCollection_AccountCompany` | TField |  | Company code where account is maintained. Clearing entry will be posted in this company code. |
| 3 | `USCKC.LEAD.COMPANY` | `UsretlCheckCollection_LeadCompany` | TField |  | Financial Lead Company of ACCOUNT.COMPANY. This field is referred by USCK21.NOSTRO.SETTLEMENT batch job to aggregate total to settle with FED Nostro. |
| 4 | `USCKC.ROUTING.NUMBER` | `UsretlCheckCollection_RoutingNumber` | TField |  | Routing Number printed on check. Second segment of &amp;ID. This is a noinput field and defaulted from &amp;ID |
| 5 | `USCKC.CHECK.NUMBER` | `UsretlCheckCollection_CheckNumber` | TField |  | Check Number printed on check. Third segment of &amp;ID. This is a noinput field and defaulted from &amp;ID |
| 6 | `USCKC.CURRENCY` | `UsretlCheckCollection_Currency` | TField |  | Check Currency. This is currently defaulted to USD, other currency checks are currently out of scope. |
| 7 | `USCKC.AMOUNT` | `UsretlCheckCollection_Amount` | TField |  | Check amount. Valid amount with 2 digits after decimal. |
| 8 | `USCKC.CREDIT.OR.DEBIT` | `UsretlCheckCollection_CreditOrDebit` | TField |  | Credit or Debit transaction sign to ACCOUNT.NUMBER. For a check deposit, this field is updated with CREDIT and for Inward Clearing/Inward Returns, this field is updated as DEBIT Possible values: CREDIT, DEBIT |
| 9 | `USCKC.CHECK.TYPE` | `UsretlCheckCollection_CheckType` | TField |  | When check routing number matches the routing number in USRETL.CHECK.CLEARING.PARAMETER - GOV.ROUTING.NO, Check type is considered GOVERNMENT. When check routing number matches USRETL.CHECK.CLEARING.PARAMETER - ONUS.ROUTING.NO, Check type is considered ON-US. When check routing number does not match GOV.ROUTING.NO or ONUS.ROUTING.NO the check type is considered as default LOCAL. Possible values: GOVERNMENT, ON-US,LOCAL |
| 10 | `USCKC.IMAGE.REFERENCE` | `UsretlCheckCollection_ImageReference` | TField |  | This field contains the digital check image reference. This value is supplied in CHECK21 inward clearing file for each item. |
| 11 | `USCKC.CHECK.TXN.CODE` | `UsretlCheckCollection_CheckTxnCode` | TField |  | This field contains the transaction code assigned by CHECK21 vendor(Alogent) to each item. Clients may agree to use specific transaction codes for forced exception posting while processing CHECK21 inward clearing file. Such codes will be configured in USRETL.CHECK.CLEARING.PARAMETER - EXCEPTION.TXN.CODE Input format : 4 Alphanumeric characters |
| 12 | `USCKC.ORIGINAL.VALUE.DATE` | `UsretlCheckCollection_OriginalValueDate` | TField |  | Value Date of original entry posting i.e. when the original inward clearing check is posted. Input format : YYYYMMDD |
| 13 | `USCKC.ORIGINAL.DEPOSIT.DATE` | `UsretlCheckCollection_OriginalDepositDate` | TField |  | Calendar Date when check was deposited. This information is mapped from CHECK21 - Inward Returns File. Input format : YYYYMMDD |
| 14 | `USCKC.PROCESSING.DATE` | `UsretlCheckCollection_ProcessingDate` | TField |  | This field contains the processing date of the transaction. Data format : YYYYMMDD |
| 15 | `USCKC.SPLIT.EXPOSURE.DATE` | `UsretlCheckCollection_SplitExposureDate` |  |  |  |
| 16 | `USCKC.SPLIT.EXPOSURE.AMOUNT` | `UsretlCheckCollection_SplitExposureAmount` |  |  |  |
| 17 | `USCKC.STATUS` | `UsretlCheckCollection_Status` | TField |  | Current status of check. DEPOSITED � Other/same bank check deposited through RDC DEPOSIT.FAILED � Other/same bank check deposited through RDC that failed deposit due to technical/business error(s) encountered while entry posting. After errors are manually fixed, Check must be resubmitted through RDC. RETURNED � Previously deposited other bank check when returned. CLEARED � Inward clearing of house checks deposited in other institutions. The funds on the check have been successfully collected. REJECTED � Inward clearing of house checks deposited in other institutions. Clearing was rejected due to account restrictions, stops or NSF. EXCEPTION - incorrect account, forced exception or technical error, that needs to be resolved or pending resolution in the back office will be updated as Exceptions. LOADED - Interim status when information from inward clearing file is captured. Following this status is entry posting that may result in either CLEARED or EXCEPTION RETURN.LOADED - Interim status when information from inward return file is captured. Following this status is return entry posting that may result in either RETURNED or EXCEPTION |
| 18 | `USCKC.STATUS.DATE` | `UsretlCheckCollection_StatusDate` | TField |  | Calendar date of last STATUS change. Data format : YYYYMMDD |
| 19 | `USCKC.EXPIRY.DATE` | `UsretlCheckCollection_ExpiryDate` | TField |  |  |
| 20 | `USCKC.SUSP.POSTED.TO` | `UsretlCheckCollection_SuspPostedTo` | TField |  | This field contains the suspense account to which this check amount has been posted instead of ACCOUNT.NUMBER when STATUS is EXCEPTION Data format : USDccccNNNN, where cccc - is suspense category code configured in AC.ENTRY.PARAM and NNNN is the account sequence number. |
| 21 | `USCKC.SUSP.FT.ID` | `UsretlCheckCollection_SuspFtId` | TField |  | This field contains the suspense FUNDS.TRANSFER reference parked in FHLD status for manual intervention when STATUS is EXCEPTION Data format : Valid FUNDS.TRANSFER reference. |
| 22 | `USCKC.EXCEPTION.REASON` | `UsretlCheckCollection_ExceptionReason` |  |  |  |
| 23 | `USCKC.ORIG.ENTRY.REF` | `UsretlCheckCollection_OrigEntryRef` | TField |  | Reference to AC.INWARD.ENTRY record, check deposit entry from RDC or CHECK21 inward clearing file is posted using Generic Accounting Inteface and the corresponding log file (AC.INWARD.ENTRY) record reference is maintained in this field. This is a NOINPUT field and updated by RDC and CHECK21 interface. A valid entry in AC.INWARD.ENTRY table. |
| 24 | `USCKC.CHARGE.AMOUNT` | `UsretlCheckCollection_ChargeAmount` | TField |  | This field contains the charge amount from CHECK21 - inward return file applicable for return transactions. This is an information only field, return charges must be configured in account arrangement product. This is a NOINPUT field and updated by CHECK21 interface. |
| 25 | `USCKC.RET.OR.REJ.CODE` | `UsretlCheckCollection_RetOrRejCode` | TField |  | When an item is RETURNED or REJECTED, the appropriate return code is mapped to this field. Valid list of FED check return codes configured in virutal table - TXN.RETURN.CODE. |
| 26 | `USCKC.RETURN.DESCRIPTION` | `UsretlCheckCollection_ReturnDescription` | TField |  | When an item is RETURNED or REJECTED, the description of RET.OR.REJ.CODE is mapped to this field. Description of FED check return codes configured in virutal table - TXN.RETURN.CODE. |
| 27 | `USCKC.RETURN.PROCESSING.DATE` | `UsretlCheckCollection_ReturnProcessingDate` | TField |  | Transact Date when an item is RETURNED or REJECTED, it is on this date that a REJECTED item will be included in CHECK21 - outward exception file . Data format : YYYYMMDD RET.ENTRY.REF |
| 28 | `USCKC.RET.ENTRY.REF` | `UsretlCheckCollection_RetEntryRef` |  |  |  |
| 29 | `USCKC.DISPOSITION` | `UsretlCheckCollection_Disposition` | TField |  | This field contains the disposition of item recevied. This is an information only field and is captured only while processing CHECK21 - Inward return file. Possible values: IRD - Image Replacement Document. Representment - Check Represented. |
| 30 | `USCKC.NAME` | `UsretlCheckCollection_Name` | TField |  | Depositor name. This is an information only field and is captured only while processing CHECK21 - Inward return file. This is a NOINPUT field and updated by CHECK21 interface. |
| 31 | `USCKC.ADDRESS.LINE` | `UsretlCheckCollection_AddressLine` |  |  |  |
| 32 | `USCKC.STATE` | `UsretlCheckCollection_State` | TField |  | State of the Depositor's city address. This is an information only field and is captured only while processing CHECK21 - Inward return file. This is a NOINPUT field and updated by CHECK21 interface. Valid entry is US.STATE table |
| 33 | `USCKC.ZIP` | `UsretlCheckCollection_Zip` | TField |  | Zip code of Depositor's city address. This is an information only field and is captured only while processing CHECK21 - Inward return file. This is a NOINPUT field and updated by CHECK21 interface. |
| 34 | `USCKC.ADDITIONAL.INFO` | `UsretlCheckCollection_AdditionalInfo` |  |  |  |
| 35 | `USCKC.DEPOSIT.ACCOUNT.NO` | `UsretlCheckCollection_DepositAccountNo` | TField |  | Depositor's bank account number. This is an information only field and is captured only while processing CHECK21 - Inward return file. This is a NOINPUT field and updated by CHECK21 interface. |
| 36 | `USCKC.COLLECTION.HIST` | `UsretlCheckCollection_CollectionHist` |  |  |  |
| 37 | `USCKC.RESERVED.10` | `UsretlCheckCollection_Reserved10` |  |  |  |
| 38 | `USCKC.RESERVED.9` | `UsretlCheckCollection_Reserved9` |  |  |  |
| 39 | `USCKC.RESERVED.8` | `UsretlCheckCollection_Reserved8` |  |  |  |
| 40 | `USCKC.RESERVED.7` | `UsretlCheckCollection_Reserved7` |  |  |  |
| 41 | `USCKC.RESERVED.6` | `UsretlCheckCollection_Reserved6` | TField |  |  |
| 42 | `USCKC.RESERVED.5` | `UsretlCheckCollection_Reserved5` | TField |  |  |
| 43 | `USCKC.RESERVED.4` | `UsretlCheckCollection_Reserved4` | TField |  |  |
| 44 | `USCKC.RESERVED.3` | `UsretlCheckCollection_Reserved3` | TField |  |  |
| 45 | `USCKC.RESERVED.2` | `UsretlCheckCollection_Reserved2` | TField |  |  |
| 46 | `USCKC.RESERVED.1` | `UsretlCheckCollection_Reserved1` | TField |  |  |
| 47 | `USCKC.OVERRIDE` | `UsretlCheckCollection_Override` |  |  |  |
| 48 | `USCKC.STMT.NOS` | `UsretlCheckCollection_StmtNos` |  |  |  |
| 49 | `USCKC.RECORD.STATUS` | `UsretlCheckCollection_RecordStatus` | String |  |  |
| 50 | `USCKC.CURR.NO` | `UsretlCheckCollection_CurrNo` | String |  |  |
| 51 | `USCKC.INPUTTER` | `UsretlCheckCollection_Inputter` |  |  |  |
| 52 | `USCKC.DATE.TIME` | `UsretlCheckCollection_DateTime` |  |  |  |
| 53 | `USCKC.AUTHORISER` | `UsretlCheckCollection_Authoriser` | String |  |  |
| 54 | `USCKC.CO.CODE` | `UsretlCheckCollection_CoCode` | String |  |  |
| 55 | `USCKC.DEPT.CODE` | `UsretlCheckCollection_DeptCode` | String |  |  |
| 56 | `USCKC.AUDITOR.CODE` | `UsretlCheckCollection_AuditorCode` | String |  |  |
| 57 | `USCKC.AUDIT.DATE.TIME` | `UsretlCheckCollection_AuditDateTime` | String |  |  |
