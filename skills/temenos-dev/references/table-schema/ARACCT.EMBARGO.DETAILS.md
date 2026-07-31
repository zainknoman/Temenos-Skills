# ARACCT.EMBARGO.DETAILS — Table Schema

> Source: `INSERTS/I_F.ARACCT.EMBARGO.DETAILS` in `ARACCT_AccountAlias.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ARACCT.TRADE.DATE` | `AracctEmbargoDetails_TradeDate` | TField |  | Holds the date and time of the balance request or embargo request |
| 2 | `ARACCT.CUIT` | `AracctEmbargoDetails_Cuit` | TField |  | Holds the CUIT/CUIL/Legalid of the customer |
| 3 | `ARACCT.ACCOUNT.HOLDER.NAME` | `AracctEmbargoDetails_AccountHolderName` |  |  |  |
| 4 | `ARACCT.CBU.ACCOUNT.NUMBER` | `AracctEmbargoDetails_CbuAccountNumber` | TField |  | Holds CBU account number |
| 5 | `ARACCT.ACCOUNT.CCY` | `AracctEmbargoDetails_AccountCcy` | TField |  | Holds the account currency |
| 6 | `ARACCT.SEIZURE.NUMBER` | `AracctEmbargoDetails_SeizureNumber` | TField |  | Holds the number of seizure process |
| 7 | `ARACCT.SEIZURE.OFFICIAL.DATE` | `AracctEmbargoDetails_SeizureOfficialDate` | TField |  | Holds the official date of the seizure process |
| 8 | `ARACCT.CASE.FILE` | `AracctEmbargoDetails_CaseFile` | TField |  | Holds the case file of the seizure |
| 9 | `ARACCT.COURT.NO` | `AracctEmbargoDetails_CourtNo` | TField |  | Holds the court number |
| 10 | `ARACCT.JUDGE.NAME` | `AracctEmbargoDetails_JudgeName` | TField |  | Holds the name of the judge |
| 11 | `ARACCT.CAPITAL.AMOUNT` | `AracctEmbargoDetails_CapitalAmount` | TField |  | Holds the capital amount of the customer |
| 12 | `ARACCT.INTEREST.AMOUNT` | `AracctEmbargoDetails_InterestAmount` | TField |  | Holds the interest amount of the customer |
| 13 | `ARACCT.BANK.CODE` | `AracctEmbargoDetails_BankCode` | TField |  | Holds the name of the bank |
| 14 | `ARACCT.BRANCH.OFFICE` | `AracctEmbargoDetails_BranchOffice` | TField |  | Holds the branch details of the bank. |
| 15 | `ARACCT.ACCOUNT.NO` | `AracctEmbargoDetails_AccountNo` | TField |  | Holds the account number |
| 16 | `ARACCT.COURT.OFFICE.NO` | `AracctEmbargoDetails_CourtOfficeNo` | TField |  | Holds the court office number |
| 17 | `ARACCT.COELSA.PUBLISH.DATE` | `AracctEmbargoDetails_CoelsaPublishDate` | TField |  | Holds the date and time of the trade published in the COELSA |
| 18 | `ARACCT.ORDER.INFORMATION` | `AracctEmbargoDetails_OrderInformation` |  |  |  |
| 19 | `ARACCT.SEIZURE.STATUS` | `AracctEmbargoDetails_SeizureStatus` | TField |  | Indicate seizure is finished or completed |
| 20 | `ARACCT.COURT.EMPLOYEE.NO` | `AracctEmbargoDetails_CourtEmployeeNo` | TField |  | Number of the court employee |
| 21 | `ARACCT.TRANSFER` | `AracctEmbargoDetails_Transfer` | TField |  | Yes/No value |
| 22 | `ARACCT.VALID.BALANCE` | `AracctEmbargoDetails_ValidBalance` | TField |  | Current or Future or Both |
| 23 | `ARACCT.CODE` | `AracctEmbargoDetails_Code` | TField |  | Holds the code of the request |
| 24 | `ARACCT.TYPE` | `AracctEmbargoDetails_Type` | TField |  | Holds the organisation type |
| 25 | `ARACCT.LEGAL.DOC.TYPE` | `AracctEmbargoDetails_LegalDocType` | TField |  | Holds the legal document type |
| 26 | `ARACCT.PENDING.SEIZURE.AMOUNT` | `AracctEmbargoDetails_PendingSeizureAmount` | TField |  | Holds the pending seizure amount for the customer |
| 27 | `ARACCT.PROVINCE` | `AracctEmbargoDetails_Province` | TField |  | Holds the province code |
| 28 | `ARACCT.SEIZURE.ORIGINATE.OFFICE` | `AracctEmbargoDetails_SeizureOriginateOffice` | TField |  | Holds the seizure initiated office |
| 29 | `ARACCT.DEBIT.ID` | `AracctEmbargoDetails_DebitId` | TField |  | Unique number of the embargo |
| 30 | `ARACCT.ORIGINAL.SEIZURE.AMOUNT` | `AracctEmbargoDetails_OriginalSeizureAmount` | TField |  | Holds the original seizure amount |
| 31 | `ARACCT.DEBIT.CCY` | `AracctEmbargoDetails_DebitCcy` | TField |  | Holds the debit currency |
| 32 | `ARACCT.USD.QUOTATION` | `AracctEmbargoDetails_UsdQuotation` | TField |  | Holds the dollar price |
| 33 | `ARACCT.AMOUNT.TO.BE.SEIZED` | `AracctEmbargoDetails_AmountToBeSeized` | TField |  | Holds the amount to be seized in the account |
| 34 | `ARACCT.EMBARGO.DATE` | `AracctEmbargoDetails_EmbargoDate` | TField |  | Holds the embargo date |
| 35 | `ARACCT.REASON.FOR.SEZIURE.LIFT` | `AracctEmbargoDetails_ReasonForSeziureLift` |  |  |  |
| 36 | `ARACCT.LOW.DATE` | `AracctEmbargoDetails_LowDate` | TField |  | Should hold the low date of discharge file |
| 37 | `ARACCT.HIGH.DATE` | `AracctEmbargoDetails_HighDate` | TField |  | Should hold the high date of discharge file |
| 38 | `ARACCT.REQUEST.TYPE` | `AracctEmbargoDetails_RequestType` | TField |  | It should be updated either Balance Enquiry or Embargo Request |
| 39 | `ARACCT.RESPONSE.CODE` | `AracctEmbargoDetails_ResponseCode` | TField |  | Holds the response code |
| 40 | `ARACCT.RESPONSE.DATE` | `AracctEmbargoDetails_ResponseDate` | TField |  | Date and time of the response |
| 41 | `ARACCT.RESPONSE.CATEGORY` | `AracctEmbargoDetails_ResponseCategory` | TField |  | Holds the account type |
| 42 | `ARACCT.RESPONSE.OWNERS` | `AracctEmbargoDetails_ResponseOwners` | TField |  | No.of. Account holders |
| 43 | `ARACCT.RESPONSE.ACCOUNT.BALANCE` | `AracctEmbargoDetails_ResponseAccountBalance` | TField |  | Holds the available balance of the account |
| 44 | `ARACCT.RESPONSE.AVAILABLE.BALANCE` | `AracctEmbargoDetails_ResponseAvailableBalance` | TField |  | Holds the balance of the account that can be blocked/seized |
| 45 | `ARACCT.RESPONSE.AMOUNT.SEIZED` | `AracctEmbargoDetails_ResponseAmountSeized` | TField |  | Holds the particular of seized amount on the account |
| 46 | `ARACCT.CORRES.ACCOUNT.NUMBER` | `AracctEmbargoDetails_CorresAccountNumber` | TField |  | Account Number corresponding to CBU account |
| 47 | `ARACCT.CORRES.PRODUCT.LINE` | `AracctEmbargoDetails_CorresProductLine` | TField |  | Product line of the account |
| 48 | `ARACCT.SEIZURE.REMOVED` | `AracctEmbargoDetails_SeizureRemoved` | TField |  | Yes/No value for Seizure |
| 49 | `ARACCT.CYCLE` | `AracctEmbargoDetails_Cycle` | TField |  | Holds the sequence of the cycle |
| 50 | `ARACCT.TOTAL.EMBARGO` | `AracctEmbargoDetails_TotalEmbargo` | TField |  | Holds the total embargo amount |
| 51 | `ARACCT.AVL.BALANCE.FOR.SEIZURE` | `AracctEmbargoDetails_AvlBalanceForSeizure` | TField |  | Holds the available balance on the account for seizure |
| 52 | `ARACCT.OUTSTANDING.BALANCE` | `AracctEmbargoDetails_OutstandingBalance` | TField |  | Holds the seized balance on the account |
| 53 | `ARACCT.STATE` | `AracctEmbargoDetails_State` | TField |  | Holds the state of embargo |
| 54 | `ARACCT.RESPONSE.IDENT.CODE` | `AracctEmbargoDetails_ResponseIdentCode` | TField |  | Holds the identification code of the customer |
| 55 | `ARACCT.RESPONSE.DATE.QUOTE` | `AracctEmbargoDetails_ResponseDateQuote` | TField |  | Holds the date of quotation |
| 56 | `ARACCT.VEP.NO` | `AracctEmbargoDetails_VepNo` | TField |  | Holds the VEP number |
| 57 | `ARACCT.REVERSAL` | `AracctEmbargoDetails_Reversal` | TField |  | Holds the value if record need to be Reversed or not |
| 58 | `ARACCT.REVERSAL.PROCESSED` | `AracctEmbargoDetails_ReversalProcessed` | TField |  | The value is set if the record is reversed. |
| 59 | `ARACCT.INTEREST.PROPERTIES` | `AracctEmbargoDetails_InterestProperties` |  |  |  |
| 60 | `ARACCT.CUSTOMER` | `AracctEmbargoDetails_Customer` | TField |  | Holds the current Customer Id |
| 61 | `ARACCT.REQUEST.APPLY` | `AracctEmbargoDetails_RequestApply` | TField |  | Holds the incoming Request apply value |
| 62 | `ARACCT.LOCAL.REF` | `AracctEmbargoDetails_LocalRef` |  |  |  |
| 63 | `ARACCT.PRIORITY.ACCOUNT` | `AracctEmbargoDetails_PriorityAccount` | TField |  | Holds the Priority Account number for the current customer |
| 64 | `ARACCT.RELEASE.AMOUNT` | `AracctEmbargoDetails_ReleaseAmount` | TField |  | Holds the amount requested in Lift of seizure |
| 65 | `ARACCT.RELEASE.DATE.TIME` | `AracctEmbargoDetails_ReleaseDateTime` |  |  |  |
| 66 | `ARACCT.RESPONSE.SENT` | `AracctEmbargoDetails_ResponseSent` | TField |  | This field contains yes if response is sent |
| 67 | `ARACCT.ACCOUNT.TYPE` | `AracctEmbargoDetails_AccountType` | TField |  | Type of account associated with the CBU |
| 68 | `ARACCT.RECON.ACCOUNT.NO` | `AracctEmbargoDetails_ReconAccountNo` | TField |  | Reconciliation Account number associated with the CBU (13 numbers are completed with 0 on the left) |
| 69 | `ARACCT.RESERVED.7` | `AracctEmbargoDetails_Reserved7` | TField |  | Reserved for future use |
| 70 | `ARACCT.RESERVED.8` | `AracctEmbargoDetails_Reserved8` | TField |  | Reserved for future use |
| 71 | `ARACCT.RESERVED.9` | `AracctEmbargoDetails_Reserved9` | TField |  | Reserved for future use |
| 72 | `ARACCT.RESERVED.10` | `AracctEmbargoDetails_Reserved10` | TField |  | Reserved for future use |
| 73 | `ARACCT.RESERVED.11` | `AracctEmbargoDetails_Reserved11` | TField |  | Reserved for future use |
| 74 | `ARACCT.RESERVED.12` | `AracctEmbargoDetails_Reserved12` | TField |  | Reserved for future use |
| 75 | `ARACCT.RESERVED.13` | `AracctEmbargoDetails_Reserved13` | TField |  | Reserved for future use |
| 76 | `ARACCT.RESERVED.14` | `AracctEmbargoDetails_Reserved14` | TField |  | Reserved for future use |
| 77 | `ARACCT.RESERVED.15` | `AracctEmbargoDetails_Reserved15` | TField |  | Reserved for future use |
| 78 | `ARACCT.OVERRIDE` | `AracctEmbargoDetails_Override` |  |  |  |
| 79 | `ARACCT.RECORD.STATUS` | `AracctEmbargoDetails_RecordStatus` | String |  |  |
| 80 | `ARACCT.CURR.NO` | `AracctEmbargoDetails_CurrNo` | String |  |  |
| 81 | `ARACCT.INPUTTER` | `AracctEmbargoDetails_Inputter` |  |  |  |
| 82 | `ARACCT.DATE.TIME` | `AracctEmbargoDetails_DateTime` |  |  |  |
| 83 | `ARACCT.AUTHORISER` | `AracctEmbargoDetails_Authoriser` | String |  |  |
| 84 | `ARACCT.CO.CODE` | `AracctEmbargoDetails_CoCode` | String |  |  |
| 85 | `ARACCT.DEPT.CODE` | `AracctEmbargoDetails_DeptCode` | String |  |  |
| 86 | `ARACCT.AUDITOR.CODE` | `AracctEmbargoDetails_AuditorCode` | String |  |  |
| 87 | `ARACCT.AUDIT.DATE.TIME` | `AracctEmbargoDetails_AuditDateTime` | String |  |  |
