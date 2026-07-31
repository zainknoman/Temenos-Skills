# CAPL.PLAN.TRANSACTIONS — Table Schema

> Source: `INSERTS/I_F.CAPL.PLAN.TRANSACTIONS` in `CARGPL_RegisteredPlans.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.PTRAN.DEBIT.CREDIT` | `CaplPlanTransactions_DebitCredit` | TField |  | This field is used to indicate whether the transaction is a debit or credit transaction.Field values are Dr/Cr. |
| 2 | `CAPL.PTRAN.PORTFOLIO.ID` | `CaplPlanTransactions_PortfolioId` | TField |  | This field is used to define the portfoli id for the transaction.Valid record from SECC.ACC.MASTER table. |
| 3 | `CAPL.PTRAN.PLAN.TYPE` | `CaplPlanTransactions_PlanType` | TField |  | This field denotes the plan type for the ransaction perform.Valid record from CAPL.PLAN.TYPE table. |
| 4 | `CAPL.PTRAN.ACCOUNT.ID` | `CaplPlanTransactions_AccountId` | TField |  | Field denotes the account number in which the transaction is done.Valid record from ACCOUNT table. |
| 5 | `CAPL.PTRAN.SPOUSE.ID` | `CaplPlanTransactions_SpouseId` | TField |  | This field denotes the spousal id for the transaction if any.Valid record from CUSTOMER table. |
| 6 | `CAPL.PTRAN.CONTRIBUTOR.ID` | `CaplPlanTransactions_ContributorId` | TField |  | Field is used to denote the contributor id for the plan.Valid record from CUSTOMER table. |
| 7 | `CAPL.PTRAN.BENEFICIARY.ID` | `CaplPlanTransactions_BeneficiaryId` | TField |  | This field is used to denote the beneficiary id for the transaction.Valid record from CUSTOMER table. |
| 8 | `CAPL.PTRAN.RESIDENCE` | `CaplPlanTransactions_Residence` | TField |  | This field denotes the residence of the customer.Valid record from COUNTRY table. |
| 9 | `CAPL.PTRAN.PROVINCE` | `CaplPlanTransactions_Province` | TField |  | This field indicates the province of the customer. |
| 10 | `CAPL.PTRAN.TRANSACTION` | `CaplPlanTransactions_Transaction` | TField |  | This field holds the transaction code for the type of transaction performed.Valid record from CAPL.PLAN.TXNS |
| 11 | `CAPL.PTRAN.CAPL.TXN.CODE` | `CaplPlanTransactions_CaplTxnCode` | TField |  | Field holds the txn code for the spec entry.Valid record from CAPL.PLAN.TXN.TYPE table. |
| 12 | `CAPL.PTRAN.CURRENCY` | `CaplPlanTransactions_Currency` | TField |  | Field holds the currency for the transactionsvalid record from CURRENCY table. |
| 13 | `CAPL.PTRAN.AMOUNT` | `CaplPlanTransactions_Amount` | TField |  | This field hodls the transaction amount for the plan.Valid amount to be defined here. |
| 14 | `CAPL.PTRAN.RECEIPT` | `CaplPlanTransactions_Receipt` | TField |  | This field denotes whether the transaction required receipt or not.Allowed values are Yes/No. |
| 15 | `CAPL.PTRAN.MIN.AMOUNT` | `CaplPlanTransactions_MinAmount` | TField |  | Field to capture/Store the Minimal Withdrawal Amount Not sure |
| 16 | `CAPL.PTRAN.VALUE.DATE` | `CaplPlanTransactions_ValueDate` | TField |  | Field is to store the value date for the transaction perfomred. |
| 17 | `CAPL.PTRAN.BOOKING.DATE` | `CaplPlanTransactions_BookingDate` | TField |  | Field is to store the booking date for the transaction perfomred. |
| 18 | `CAPL.PTRAN.EXCESS.AMOUNT` | `CaplPlanTransactions_ExcessAmount` | TField |  | Field is to store the minimum amount for the plan , in this case if the transaction amount will be updated here.Valid amount to be defined here. |
| 19 | `CAPL.PTRAN.PROV.TAX` | `CaplPlanTransactions_ProvTax` | TField |  | The field indicates the provine tax amount applicable for the transaction performedvalid amount to be defined. |
| 20 | `CAPL.PTRAN.FED.TAX` | `CaplPlanTransactions_FedTax` | TField |  | The field indicates the federal tax amount applicable for the transaction performedvalid amount to be defined. |
| 21 | `CAPL.PTRAN.NR.TAX` | `CaplPlanTransactions_NrTax` | TField |  | The field indicates the non resident tax amount applicable for the transaction performedvalid amount to be defined. |
| 22 | `CAPL.PTRAN.WITHIN.PROV.TAX` | `CaplPlanTransactions_WithinProvTax` | TField |  |  |
| 23 | `CAPL.PTRAN.WITHIN.FED.TAX` | `CaplPlanTransactions_WithinFedTax` | TField |  |  |
| 24 | `CAPL.PTRAN.WITHIN.NR.TAX` | `CaplPlanTransactions_WithinNrTax` | TField |  |  |
| 25 | `CAPL.PTRAN.AFTER.PROV.TAX` | `CaplPlanTransactions_AfterProvTax` | TField |  |  |
| 26 | `CAPL.PTRAN.AFTER.FED.TAX` | `CaplPlanTransactions_AfterFedTax` | TField |  |  |
| 27 | `CAPL.PTRAN.AFTER.NR.TAX` | `CaplPlanTransactions_AfterNrTax` | TField |  |  |
| 28 | `CAPL.PTRAN.SERV.CHARGE` | `CaplPlanTransactions_ServCharge` | TField |  | The field indicates the non service charge amount applicable for the transaction performedvalid amount to be defined. |
| 29 | `CAPL.PTRAN.RESERVED.10` | `CaplPlanTransactions_Reserved10` |  |  |  |
| 30 | `CAPL.PTRAN.RESERVED.9` | `CaplPlanTransactions_Reserved9` | TField |  |  |
| 31 | `CAPL.PTRAN.RESERVED.8` | `CaplPlanTransactions_Reserved8` | TField |  |  |
| 32 | `CAPL.PTRAN.RESERVED.7` | `CaplPlanTransactions_Reserved7` | TField |  |  |
| 33 | `CAPL.PTRAN.RESERVED.6` | `CaplPlanTransactions_Reserved6` | TField |  |  |
| 34 | `CAPL.PTRAN.RESERVED.5` | `CaplPlanTransactions_Reserved5` | TField |  |  |
| 35 | `CAPL.PTRAN.RESERVED.4` | `CaplPlanTransactions_Reserved4` | TField |  |  |
| 36 | `CAPL.PTRAN.RESERVED.3` | `CaplPlanTransactions_Reserved3` | TField |  |  |
| 37 | `CAPL.PTRAN.RESERVED.2` | `CaplPlanTransactions_Reserved2` | TField |  |  |
| 38 | `CAPL.PTRAN.RESERVED.1` | `CaplPlanTransactions_Reserved1` | TField |  |  |
| 39 | `CAPL.PTRAN.LOCAL.REF` | `CaplPlanTransactions_LocalRef` |  |  |  |
| 40 | `CAPL.PTRAN.OVERRIDE` | `CaplPlanTransactions_Override` |  |  |  |
