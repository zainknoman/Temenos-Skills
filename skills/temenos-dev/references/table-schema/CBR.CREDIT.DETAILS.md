# CBR.CREDIT.DETAILS — Table Schema

> Source: `INSERTS/I_F.CBR.CREDIT.DETAILS` in `FINEXT_CBR.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CBR.CR.PRIMARY.CUSTOMER` | `CbrCreditDetails_PrimaryCustomer` | TField |  | This field updated with customer ID from the arrangement record. This field holds the value of primary customer or base customer mentioned in base segment in Metro 2 File |
| 2 | `CBR.CR.PROCESS.IND` | `CbrCreditDetails_ProcessInd` | TField |  | This fault defaulted with the value as '1' always. |
| 3 | `CBR.CR.TIME.STAMP` | `CbrCreditDetails_TimeStamp` | TField |  | The field updated with account extracted time in format MMDDYYYYHHMMSS |
| 4 | `CBR.CR.CORRECTION.IND` | `CbrCreditDetails_CorrectionInd` | TField |  | Default '0' and '1' for corrections only.The service will always default as 1, in case of correction occurred the data will updated as 1 manually in the physical file. |
| 5 | `CBR.CR.BANK.IDENTITY` | `CbrCreditDetails_BankIdentity` | TField |  | The field inputted with unique identification code for branch wise manually CBR.PARAMETER. ex.BRANCH CBR EXTRACT |
| 6 | `CBR.CR.CYCLE.NUMBER` | `CbrCreditDetails_CycleNumber` | TField |  | The field updated with CYCLE.NUMBER defined in USBTCH.CBR.PARAMETER Contains the cycle number for the information being reported, if reporting by cycles. If data contains more than one cycle, report the first cycle number found on the data |
| 7 | `CBR.CR.CONSUMER.AC.NO` | `CbrCreditDetails_ConsumerAcNo` | TField |  | The field updated with individual's complete and unique account number as extracted from arrangement file |
| 8 | `CBR.CR.PORTFOLIO.TYPE` | `CbrCreditDetails_PortfolioType` | TField |  | The field updated with portfolio type defined for each arrangement category in CBR.PARAMETER |
| 9 | `CBR.CR.ACCOUNT.TYPE` | `CbrCreditDetails_AccountType` | TField |  |  |
| 10 | `CBR.CR.DATE.OPENED` | `CbrCreditDetails_DateOpened` | TField |  | Report the date the account was originally opened. Retain the original date, regardless of future activities such as transfer. |
| 11 | `CBR.CR.CREDIT.LIMIT` | `CbrCreditDetails_CreditLimit` | TField |  | Report the following values. LOC-assigned credit Limit, Instalment - zero fill, Mortgage - zero fill, Open - zero fill, Revolving - assigned credit limit.. |
| 12 | `CBR.CR.ORIG.LOAN.AMT` | `CbrCreditDetails_OrigLoanAmt` | TField |  | LOC-Highest balance ever attained, Instalment- Original loan amount excluding interest payments, Revolving - highest balance ever attained, Mortgage - Original amount of the loan excluding interest payments.. |
| 13 | `CBR.CR.TERM.DURATION` | `CbrCreditDetails_TermDuration` | TField |  | Contains the duration of credit extended. For LOC-constant value of "LOC", Instalment-number of months, Mortgage-Number of years, Open-constant of 001, Revolving -constant value of REV. |
| 14 | `CBR.CR.TERM.FREQ` | `CbrCreditDetails_TermFreq` | TField |  | Report the frequency of payment due. |
| 15 | `CBR.CR.SCH.PAY.AMOUNT` | `CbrCreditDetails_SchPayAmount` | TField |  | Minimum amount due based on balance excluding PD amount-LOC, regular monthly payment - Instalment, same as LOC for revolving, zero fill-Open. |
| 16 | `CBR.CR.ACTUAL.PAY.AMT` | `CbrCreditDetails_ActualPayAmt` | TField |  | Report the $ amount of the payment amount received this reporting period. If multiple payments are made, field should reflect the total payments made.. |
| 17 | `CBR.CR.ACCOUNT.STATUS` | `CbrCreditDetails_AccountStatus` | TField |  | Contains the status code that properly identifies the current condition of the account as of the date of account information. |
| 18 | `CBR.CR.PAYMENT.RATING` | `CbrCreditDetails_PaymentRating` | TField |  | For certain account status in ACCOUNT.STATUS, this field has to be reported. For more details refer lending-credit reporting format V01. |
| 19 | `CBR.CR.PAY.HIS.YR.MONTH` | `CbrCreditDetails_PayHisYrMonth` |  |  |  |
| 20 | `CBR.CR.DELINQUENCY.CODE` | `CbrCreditDetails_DelinquencyCode` |  |  |  |
| 21 | `CBR.CR.NUMBER.OF.DAYS.PD` | `CbrCreditDetails_NumberOfDaysPd` |  |  |  |
| 22 | `CBR.CR.RESERVED.1` | `CbrCreditDetails_Reserved1` | TField |  |  |
| 23 | `CBR.CR.RESERVED.2` | `CbrCreditDetails_Reserved2` | TField |  |  |
| 24 | `CBR.CR.RESERVED.3` | `CbrCreditDetails_Reserved3` | TField |  |  |
| 25 | `CBR.CR.RESERVED.4` | `CbrCreditDetails_Reserved4` | TField |  |  |
| 26 | `CBR.CR.RESERVED.5` | `CbrCreditDetails_Reserved5` | TField |  |  |
| 27 | `CBR.CR.SPECIAL.COMMENT` | `CbrCreditDetails_SpecialComment` | TField |  | Free text field updated with user comments. |
| 28 | `CBR.CR.COMPLIANCE.CODE` | `CbrCreditDetails_ComplianceCode` | TField |  | Allows the reporting of a condition that is required for legal compliance; e.g., according to the Fair Credit Reporting Act (FCRA) or Fair Credit Billing Act (FCBA).. |
| 29 | `CBR.CR.CURRENT.BALANCE` | `CbrCreditDetails_CurrentBalance` | TField |  | Enter the total balance of the account, rounded off to the nearest dollar amount; credit balances reported as zero.. |
| 30 | `CBR.CR.AMOUNT.PAST.DUE` | `CbrCreditDetails_AmountPastDue` | TField |  | Report the amount past due in whole dollars only. The field can include late charge and fees. |
| 31 | `CBR.CR.ORG.CHRGOFF.AMT` | `CbrCreditDetails_OrgChrgoffAmt` | TField |  | For account status codes 64 and 97(all portfolio types) report the original amount charged to loss, regardless of the declining balance. If payments are received from the consumer, report the outstanding balance in the current balance and amount past due fields |
| 32 | `CBR.CR.ACCT.INFO.DATE` | `CbrCreditDetails_AcctInfoDate` | TField |  | Updated with account information in the Base Segment, such as Account Status and Current Balance, must be reported as of the date in this field.. |
| 33 | `CBR.CR.FIRST.DELINQUENCE` | `CbrCreditDetails_FirstDelinquence` | TField |  | Updates with Date of First Delinquency. |
| 34 | `CBR.CR.DATE.CLOSED` | `CbrCreditDetails_DateClosed` | TField |  | For all portfolio types, contains the date the account was closed to further purchases, paid in full or sold. For Line of Credit, Open or Revolving accounts, there may be a balance due.. |
| 35 | `CBR.CR.LAST.PAY.DATE` | `CbrCreditDetails_LastPayDate` | TField |  | Report the date of the most recent consumer payment, whether full or partial payment is made. |
| 36 | `CBR.CR.INTEREST.TYPE.IND` | `CbrCreditDetails_InterestTypeInd` | TField |  | Updates with interest type indicator F - Fixed or V - Variable. |
| 37 | `CBR.CR.TRANSACTION.TYPE` | `CbrCreditDetails_TransactionType` | TField |  | Updates with indicator a new record, a new borrower or a change in consumer identification. |
| 38 | `CBR.CR.CATEGORY` | `CbrCreditDetails_Category` | TField |  | Updates with the category code for each arrangement. |
| 39 | `CBR.CR.ACCT.COMPANY` | `CbrCreditDetails_AcctCompany` | TField |  | Updates the company code created for arrangement. |
| 40 | `CBR.CR.OLD.LOAN.NR` | `CbrCreditDetails_OldLoanNr` | TField |  | Updates the alternative loan number for each arrangement. |
| 41 | `CBR.CR.ECOA.CODE` | `CbrCreditDetails_EcoaCode` | TField |  |  |
| 42 | `CBR.CR.RESERVED.6` | `CbrCreditDetails_Reserved6` | TField |  |  |
| 43 | `CBR.CR.RESERVED.7` | `CbrCreditDetails_Reserved7` | TField |  |  |
| 44 | `CBR.CR.RESERVED.8` | `CbrCreditDetails_Reserved8` | TField |  |  |
| 45 | `CBR.CR.RESERVED.9` | `CbrCreditDetails_Reserved9` | TField |  |  |
| 46 | `CBR.CR.RESERVED.10` | `CbrCreditDetails_Reserved10` | TField |  |  |
| 47 | `CBR.CR.K3.AGENCY.ID` | `CbrCreditDetails_K3AgencyId` | TField |  |  |
| 48 | `CBR.CR.K3.MG.AC.NUMBER` | `CbrCreditDetails_K3MgAcNumber` | TField |  | Updates the Agency Identifier. |
| 49 | `CBR.CR.K3.MG.INFO.NUMBER` | `CbrCreditDetails_K3MgInfoNumber` | TField |  | Updates the Mortgage Information Number. |
| 50 | `CBR.CR.RESERVED.11` | `CbrCreditDetails_Reserved11` | TField |  |  |
| 51 | `CBR.CR.RESERVED.12` | `CbrCreditDetails_Reserved12` | TField |  |  |
| 52 | `CBR.CR.RESERVED.13` | `CbrCreditDetails_Reserved13` | TField |  |  |
| 53 | `CBR.CR.RESERVED.14` | `CbrCreditDetails_Reserved14` | TField |  |  |
| 54 | `CBR.CR.RESERVED.15` | `CbrCreditDetails_Reserved15` | TField |  |  |
| 55 | `CBR.CR.RESERVED.16` | `CbrCreditDetails_Reserved16` | TField |  |  |
| 56 | `CBR.CR.RESERVED.17` | `CbrCreditDetails_Reserved17` | TField |  |  |
| 57 | `CBR.CR.RESERVED.18` | `CbrCreditDetails_Reserved18` | TField |  |  |
| 58 | `CBR.CR.RESERVED.19` | `CbrCreditDetails_Reserved19` | TField |  |  |
| 59 | `CBR.CR.RESERVED.20` | `CbrCreditDetails_Reserved20` | TField |  |  |
