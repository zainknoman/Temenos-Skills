# TNFCOP.INFO.SHEET — Table Schema

> Source: `INSERTS/I_F.TNFCOP.INFO.SHEET` in `TNFCOP_InformationSheet.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `INFO.SHEET.TYPE` | `TnfcopInfoSheet_Type` | TField |  | This field is to store the Information Sheet type |
| 2 | `INFO.SHEET.DOMICILIATION.NO` | `TnfcopInfoSheet_DomiciliationNo` | TField |  | This field stores the domiciliation number generated, this field should be inputted by the system and no manual input |
| 3 | `INFO.SHEET.DOMICILIATION.DATE` | `TnfcopInfoSheet_DomiciliationDate` | TField |  | This field is to store the date on when the information sheet is domiciled |
| 4 | `INFO.SHEET.CUSTOMER.ACCOUNT` | `TnfcopInfoSheet_CustomerAccount` | TField |  | This field stores the account number of the customer for whom the Information sheet is created |
| 5 | `INFO.SHEET.COUNTRY.DESTINATION` | `TnfcopInfoSheet_CountryDestination` | TField |  | This field stores the final destination country for the transaction |
| 6 | `INFO.SHEET.NO.OF.PAYMENTS` | `TnfcopInfoSheet_NoOfPayments` | TField |  | This field stores the number of payments which will be done using the information sheet |
| 7 | `INFO.SHEET.BP.CODE` | `TnfcopInfoSheet_BpCode` | TField |  | This field stores the BP code used for the information sheet |
| 8 | `INFO.SHEET.BENEFICIARY.NAME` | `TnfcopInfoSheet_BeneficiaryName` | TField |  | This field stores the name of the beneficiary for the information sheet |
| 9 | `INFO.SHEET.BENEFICIARY.NATION` | `TnfcopInfoSheet_BeneficiaryNation` | TField |  | This field stores the nationality of the Beneficiary. The below are the allowed values:E : Foreigner T: Tunisian |
| 10 | `INFO.SHEET.BENE.SHORT.NAME` | `TnfcopInfoSheet_BeneShortName` | TField |  | This field stores the short name of the beneficiary |
| 11 | `INFO.SHEET.CURRENCY` | `TnfcopInfoSheet_Currency` | TField |  | This field stores the currency in which the information sheet is created |
| 12 | `INFO.SHEET.SETT.SOURCE` | `TnfcopInfoSheet_SettSource` | TField |  | This field stores the settlement Source code for the Settlement for information sheet. Allowed values are :10 20 40 50 |
| 13 | `INFO.SHEET.SETT.CODE` | `TnfcopInfoSheet_SettCode` | TField |  | This field stores the settlement type in which the payment is made to the beneficiary. Allowed values are : 15 = Cash transfer 21 = Transfer 22 = Check transfer |
| 14 | `INFO.SHEET.REQUEST.AMOUNT` | `TnfcopInfoSheet_RequestAmount` | TField |  | This field stores the amount requested by the customer for the information sheet |
| 15 | `INFO.SHEET.CANCEL.DATE` | `TnfcopInfoSheet_CancelDate` | TField |  | This field stores the date on when the Information sheet is cancelled |
| 16 | `INFO.SHEET.CANCEL.REASON` | `TnfcopInfoSheet_CancelReason` | TField |  | This field stores the reason for which the information sheet is cancelled |
| 17 | `INFO.SHEET.STATUS` | `TnfcopInfoSheet_Status` | TField |  | This field stores the status of the information sheet |
| 18 | `INFO.SHEET.RESERVE.TXN.REF` | `TnfcopInfoSheet_ReserveTxnRef` |  |  |  |
| 19 | `INFO.SHEET.RESERVE.AMT` | `TnfcopInfoSheet_ReserveAmt` |  |  |  |
| 20 | `INFO.SHEET.RESERVE.TXN.CCY` | `TnfcopInfoSheet_ReserveTxnCcy` |  |  |  |
| 21 | `INFO.SHEET.RESERVE.DATE` | `TnfcopInfoSheet_ReserveDate` |  |  |  |
| 22 | `INFO.SHEET.RELEASE.AMT` | `TnfcopInfoSheet_ReleaseAmt` |  |  |  |
| 23 | `INFO.SHEET.RELEASE.DATE` | `TnfcopInfoSheet_ReleaseDate` |  |  |  |
| 24 | `INFO.SHEET.RESERVE.REF` | `TnfcopInfoSheet_ReserveRef` |  |  |  |
| 25 | `INFO.SHEET.SETT.TXN.REF` | `TnfcopInfoSheet_SettTxnRef` |  |  |  |
| 26 | `INFO.SHEET.SETTLEMENT.AMT` | `TnfcopInfoSheet_SettlementAmt` |  |  |  |
| 27 | `INFO.SHEET.SETTLEMENT.CCY` | `TnfcopInfoSheet_SettlementCcy` |  |  |  |
| 28 | `INFO.SHEET.SETTLEMENT.DATE` | `TnfcopInfoSheet_SettlementDate` |  |  |  |
| 29 | `INFO.SHEET.CHARGE.ACCT` | `TnfcopInfoSheet_ChargeAcct` | TField |  | This field stores the account from which the charge has to be debited from the customer |
| 30 | `INFO.SHEET.CHARGE.TYPE` | `TnfcopInfoSheet_ChargeType` |  |  |  |
| 31 | `INFO.SHEET.CHARGE.AMT` | `TnfcopInfoSheet_ChargeAmt` |  |  |  |
| 32 | `INFO.SHEET.TAX.AMT` | `TnfcopInfoSheet_TaxAmt` |  |  |  |
| 33 | `INFO.SHEET.LOAN.REF` | `TnfcopInfoSheet_LoanRef` | TField |  | This field stores the Loan Reference provided by CBT |
| 34 | `INFO.SHEET.LOAN.DATE` | `TnfcopInfoSheet_LoanDate` | TField |  | This field stores the date on when the loan is taken by the customer |
| 35 | `INFO.SHEET.LOAN.MAT.DATE` | `TnfcopInfoSheet_LoanMatDate` | TField |  | This field stores the maturity date of the Loan taken by the customer |
| 36 | `INFO.SHEET.EXTRACTION.DATE` | `TnfcopInfoSheet_ExtractionDate` | TField |  | Extraction Date on when files are extracted from T24s |
| 37 | `INFO.SHEET.IDENTIFICATION.TYPE` | `TnfcopInfoSheet_IdentificationType` | TField |  | This field store the type of Identification document submitted by the customer |
| 38 | `INFO.SHEET.LOCAL.REF` | `TnfcopInfoSheet_LocalRef` |  |  |  |
| 39 | `INFO.SHEET.OVERRIDE` | `TnfcopInfoSheet_Override` |  |  |  |
| 40 | `INFO.SHEET.RECORD.STATUS` | `TnfcopInfoSheet_RecordStatus` | String |  |  |
| 41 | `INFO.SHEET.CURR.NO` | `TnfcopInfoSheet_CurrNo` | String |  |  |
| 42 | `INFO.SHEET.INPUTTER` | `TnfcopInfoSheet_Inputter` |  |  |  |
| 43 | `INFO.SHEET.DATE.TIME` | `TnfcopInfoSheet_DateTime` |  |  |  |
| 44 | `INFO.SHEET.AUTHORISER` | `TnfcopInfoSheet_Authoriser` | String |  |  |
| 45 | `INFO.SHEET.CO.CODE` | `TnfcopInfoSheet_CoCode` | String |  |  |
| 46 | `INFO.SHEET.DEPT.CODE` | `TnfcopInfoSheet_DeptCode` | String |  |  |
| 47 | `INFO.SHEET.AUDITOR.CODE` | `TnfcopInfoSheet_AuditorCode` | String |  |  |
| 48 | `INFO.SHEET.AUDIT.DATE.TIME` | `TnfcopInfoSheet_AuditDateTime` | String |  |  |
| 49 | `INFO.SHEET.TITLE.SHEET.REF` | `TnfcopInfoSheet_TitleSheetRef` | TField |  | This field refers to a valid title reference from the tables of TNFCOP.INFO.SHEET , TNFCOP.FORM.APPLICATION , TNFCOP.FOREIGN.TRADE.TITLE for which a payment has been initiatedIts a neighbour field. |
| 50 | `INFO.SHEET.CUST.IDENT.TYPE` | `TnfcopInfoSheet_CustIdentType` | TField |  | This field Value to be defaulted as CIN OR CS. Its a neighbour field |
| 51 | `INFO.SHEET.PAYMENT.MODE` | `TnfcopInfoSheet_PaymentMode` | TField |  | This filed indicates the settlement code for the payment initiated for schooling OR Professional fileIts a neighbour field. |
| 52 | `INFO.SHEET.FT.REFERENCE` | `TnfcopInfoSheet_FtReference` | TField |  | This filed refers to the corresponding payment transaction referenceIts a neighbour field |
| 53 | `INFO.SHEET.TRF.ELIGIBLE` | `TnfcopInfoSheet_TrfEligible` | TField |  | This field stores Yes or NO field, A value of YES indicates that the indicated title code is eligible for transfer.Its a neighbour field. |
| 54 | `INFO.SHEET.CHARGE.COLLECTED` | `TnfcopInfoSheet_ChargeCollected` |  |  |  |
| 55 | `INFO.SHEET.AUTO.RESERVE.IND` | `TnfcopInfoSheet_AutoReserveInd` |  |  |  |
| 56 | `INFO.SHEET.AUTO.SETT.IND` | `TnfcopInfoSheet_AutoSettInd` |  |  |  |
| 57 | `INFO.SHEET.REMARKS` | `TnfcopInfoSheet_Remarks` | TField |  | This field denotes the remarks on additional information and resubmission of the Information Sheet. |
