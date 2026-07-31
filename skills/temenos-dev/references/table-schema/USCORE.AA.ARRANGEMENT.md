# USCORE.AA.ARRANGEMENT — Table Schema

> Source: `INSERTS/I_F.USCORE.AA.ARRANGEMENT` in `USCORE_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USCORE.CBR.ACCT.STATUS` | `UscoreAaArrangement_CbrAcctStatus` | TField |  | This field is used to store the Account status code as per metro2 format of Credit bureau reporting Valid codes are 05,11, 13, 61-65,71,78,80,82, 83, 84, 89, 93-97, DA, DF |
| 2 | `USCORE.CBR.PYMT.RATING` | `UscoreAaArrangement_CbrPymtRating` | TField |  | This field is used to store Payment ratings based on overdue status as per metro2 format of Credit bureau reporting valid codes are:0 - Current account (0 to 29 days past the due date)1 - 30-59 days past the due date2 - 60-89 days past the due date3 - 90-119 days past the due date4 - 120-149 days past the due date5 - 150-179 days past the due date6 - 180 or more days past the due dateG - CollectionL - Charge-off |
| 3 | `USCORE.CBR.CMPLN.CODE` | `UscoreAaArrangement_CbrCmplnCode` | TField |  | This field is used to enter the legal compliance code as mentioned by Fair Credit Reporting Act(FRCA) |
| 4 | `USCORE.CBR.CHARGE.OFF` | `UscoreAaArrangement_CbrChargeOff` | TField |  | For account status codes 64 and 97(all portfolio types), this field is used to store the original amount charged to loss, regardless of the declining balance in the current balance and amount past due |
| 5 | `USCORE.RESERVED.11` | `UscoreAaArrangement_Reserved11` |  |  |  |
| 6 | `USCORE.ORIGIN` | `UscoreAaArrangement_Origin` | TField |  |  |
| 7 | `USCORE.RESERVED.12` | `UscoreAaArrangement_Reserved12` |  |  |  |
| 8 | `USCORE.RESERVED.13` | `UscoreAaArrangement_Reserved13` |  |  |  |
| 9 | `USCORE.RESERVED.14` | `UscoreAaArrangement_Reserved14` |  |  |  |
| 10 | `USCORE.RESERVED.15` | `UscoreAaArrangement_Reserved15` |  |  |  |
| 11 | `USCORE.RESERVED.16` | `UscoreAaArrangement_Reserved16` |  |  |  |
| 12 | `USCORE.RESERVED.17` | `UscoreAaArrangement_Reserved17` |  |  |  |
| 13 | `USCORE.RESERVED.18` | `UscoreAaArrangement_Reserved18` | TField |  |  |
| 14 | `USCORE.ORIGINAL.AMOUNT` | `UscoreAaArrangement_OriginalAmount` | TField |  |  |
| 15 | `USCORE.APPLICATION.DATE` | `UscoreAaArrangement_ApplicationDate` | TField |  | This field is used to store AA loan application date Standard date format. |
| 16 | `USCORE.LOAN.TYPE` | `UscoreAaArrangement_LoanType` | TField |  | This field is used to specify the type of loan: whether loan is a conventional loan or non-conventional loan valid codes are:1 (Conventional)2 (FHA)3 (VA)4 (FSA/RHS) |
| 17 | `USCORE.PROPERTY.TYPE` | `UscoreAaArrangement_PropertyType` | TField |  | This field is used to specify Reflects whether the property is single family or multi family or manufactured house valid codes are:1 (1 to 4 Family)2 (Manufactured Housing)3 (Multifamily) |
| 18 | `USCORE.LOAN.PURPOSE` | `UscoreAaArrangement_LoanPurpose` | TField |  | This field is used to specify purpose of Loan valid codes are:1 (Home Purchase)2 (Home Improvement)3 (Refinance) |
| 19 | `USCORE.RESERVED.19` | `UscoreAaArrangement_Reserved19` | TField |  |  |
| 20 | `USCORE.PRE.APPROVAL` | `UscoreAaArrangement_PreApproval` | TField |  | This field is used to specify whether the loan is pre-approved or not valid codes are:1(Requested)2(Not requested)3(Not applicable) |
| 21 | `USCORE.RESERVED.20` | `UscoreAaArrangement_Reserved20` | TField |  |  |
| 22 | `USCORE.RESERVED.21` | `UscoreAaArrangement_Reserved21` | TField |  |  |
| 23 | `USCORE.RESERVED.22` | `UscoreAaArrangement_Reserved22` | TField |  |  |
| 24 | `USCORE.RESERVED.23` | `UscoreAaArrangement_Reserved23` | TField |  |  |
| 25 | `USCORE.PURCHASE.TYPE` | `UscoreAaArrangement_PurchaseType` | TField |  | This field is used to store the loan purchase type: whether it is originated or sold or from secondary market investors etc. valid codes are:0(Not originated or sold in calendar year)1(Fannie Mae)2(Ginnie Mae)3(Freddie Mac)4(Farmer Mac)5(Private Securitization)6(Commercial Bank, Savings Bank or Association)7(Life Ins Co; CU; Mtg. Bank or finance company)8(Affiliate)9(Other) |
| 26 | `USCORE.HOEPA.STATUS` | `UscoreAaArrangement_HoepaStatus` | TField |  | This field is used to specify whether the loan is applicable for Home Ownership Equity and Protection Act or not valid codes are:1(HOEPA loan)2(Not a HOEPA loan) |
| 27 | `USCORE.LIEN.STATUS` | `UscoreAaArrangement_LienStatus` | TField |  | This field is used to specify the loan lien status on the loan property valid codes are:1(First Lien)2(Subordinate Lien)3(No Lien)4(Not Applicable) |
| 28 | `USCORE.DEBT.RESTRUCTURE` | `UscoreAaArrangement_DebtRestructure` | TField |  | This field is used to indicate if the arrangement is considered to be a troubled debt restructure. valid codes are:1 (Y)2 (N) |
| 29 | `USCORE.OWNERSHIP.TYPE` | `UscoreAaArrangement_OwnershipType` | TField |  |  |
| 30 | `USCORE.MTG.ACQ.DATE` | `UscoreAaArrangement_MtgAcqDate` | TField |  | Date that the mortgage was acquired by the bank. |
| 31 | `USCORE.1098.OTHER` | `UscoreAaArrangement_1098Other` |  |  |  |
| 32 | `USCORE.RESERVED.28` | `UscoreAaArrangement_Reserved28` | TField |  |  |
| 33 | `USCORE.RESERVED.29` | `UscoreAaArrangement_Reserved29` | TField |  |  |
| 34 | `USCORE.RESERVED.30` | `UscoreAaArrangement_Reserved30` | TField |  |  |
| 35 | `USCORE.RESERVED.31` | `UscoreAaArrangement_Reserved31` | TField |  |  |
| 36 | `USCORE.RESERVED.32` | `UscoreAaArrangement_Reserved32` | TField |  |  |
| 37 | `USCORE.RESERVED.33` | `UscoreAaArrangement_Reserved33` | TField |  |  |
| 38 | `USCORE.RESERVED.34` | `UscoreAaArrangement_Reserved34` | TField |  |  |
| 39 | `USCORE.RESERVED.35` | `UscoreAaArrangement_Reserved35` | TField |  |  |
| 40 | `USCORE.RESERVED.36` | `UscoreAaArrangement_Reserved36` | TField |  |  |
| 41 | `USCORE.RESERVED.37` | `UscoreAaArrangement_Reserved37` | TField |  |  |
| 42 | `USCORE.RESERVED.38` | `UscoreAaArrangement_Reserved38` | TField |  |  |
| 43 | `USCORE.RESERVED.39` | `UscoreAaArrangement_Reserved39` | TField |  |  |
| 44 | `USCORE.RESERVED.40` | `UscoreAaArrangement_Reserved40` | TField |  |  |
| 45 | `USCORE.RESERVED.41` | `UscoreAaArrangement_Reserved41` | TField |  |  |
| 46 | `USCORE.RESERVED.42` | `UscoreAaArrangement_Reserved42` | TField |  |  |
| 47 | `USCORE.RESERVED.43` | `UscoreAaArrangement_Reserved43` | TField |  |  |
| 48 | `USCORE.RESERVED.44` | `UscoreAaArrangement_Reserved44` | TField |  |  |
| 49 | `USCORE.RESERVED.45` | `UscoreAaArrangement_Reserved45` | TField |  |  |
| 50 | `USCORE.RESERVED.46` | `UscoreAaArrangement_Reserved46` | TField |  |  |
| 51 | `USCORE.RESERVED.47` | `UscoreAaArrangement_Reserved47` | TField |  |  |
| 52 | `USCORE.RESERVED.48` | `UscoreAaArrangement_Reserved48` | TField |  |  |
| 53 | `USCORE.RESERVED.49` | `UscoreAaArrangement_Reserved49` | TField |  |  |
| 54 | `USCORE.OVERRIDE` | `UscoreAaArrangement_Override` |  |  |  |
| 55 | `USCORE.RECORD.STATUS` | `UscoreAaArrangement_RecordStatus` | String |  |  |
| 56 | `USCORE.CURR.NO` | `UscoreAaArrangement_CurrNo` | String |  |  |
| 57 | `USCORE.INPUTTER` | `UscoreAaArrangement_Inputter` |  |  |  |
| 58 | `USCORE.DATE.TIME` | `UscoreAaArrangement_DateTime` |  |  |  |
| 59 | `USCORE.AUTHORISER` | `UscoreAaArrangement_Authoriser` | String |  |  |
| 60 | `USCORE.CO.CODE` | `UscoreAaArrangement_CoCode` | String |  |  |
| 61 | `USCORE.DEPT.CODE` | `UscoreAaArrangement_DeptCode` | String |  |  |
| 62 | `USCORE.AUDITOR.CODE` | `UscoreAaArrangement_AuditorCode` | String |  |  |
| 63 | `USCORE.AUDIT.DATE.TIME` | `UscoreAaArrangement_AuditDateTime` | String |  |  |
