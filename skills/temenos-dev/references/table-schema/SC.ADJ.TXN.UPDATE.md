# SC.ADJ.TXN.UPDATE — Table Schema

> Source: `INSERTS/I_F.SC.ADJ.TXN.UPDATE` in `SC_SccEntitlements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.ADJ.CUSTOMER` | `ScAdjTxnUpdate_Customer` | TField | Yes | Valid customer id. validation rules: The customer in the corresponding entitlement record defined in the TXN.ID field. Validation error is raised ifall the entitlements are not belong to the same customer. Mandatory field |
| 2 | `SC.ADJ.TAX.TYPE` | `ScAdjTxnUpdate_TaxType` | TField |  | Valid TAX.TYPE id to which adjustment needs to be made. validation rules: Madatory field. |
| 3 | `SC.ADJ.ADJ.TYPE` | `ScAdjTxnUpdate_AdjType` | TField |  | Whether the adjustment is for over or under withholding. validation rules: Madatory field. Over - Debit the account in the field REIMB.TAX.ACCT.CAT and credit the customer account in the fieldREIMB.CU.ACCOUNT Under - Credit the account in the field REIMB.TAX.ACCT.CAT and debit the customer account in the fieldREIMB.CU.ACCOUNT |
| 4 | `SC.ADJ.TRANS.DATE` | `ScAdjTxnUpdate_TransDate` | TField |  | Date is used to update DEBIT.VALUE.DATE or CREDIT.VALUE.DATE of the FUNDS.TRANSFER record created afteradjustment. validation rules: Non Madatory field. Defaulted to today if the field doesnt have value. |
| 5 | `SC.ADJ.TAX.CCY` | `ScAdjTxnUpdate_TaxCcy` | TField | Yes | Currency is used to calculate the final adjustment amount and for creating FUNDS.TRANSFER record. validation rules: Mandatory field. |
| 6 | `SC.ADJ.TXN.ID` | `ScAdjTxnUpdate_TxnId` |  |  |  |
| 7 | `SC.ADJ.SECURITY.NO` | `ScAdjTxnUpdate_SecurityNo` |  |  |  |
| 8 | `SC.ADJ.EVENT.TYPE` | `ScAdjTxnUpdate_EventType` |  |  |  |
| 9 | `SC.ADJ.SOURCE.LOCAL` | `ScAdjTxnUpdate_SourceLocal` |  |  |  |
| 10 | `SC.ADJ.ENT.TRANS.DATE` | `ScAdjTxnUpdate_EntTransDate` |  |  |  |
| 11 | `SC.ADJ.ENT.TRANS.CCY` | `ScAdjTxnUpdate_EntTransCcy` |  |  |  |
| 12 | `SC.ADJ.ENTITLEMENT.AMT` | `ScAdjTxnUpdate_EntitlementAmt` |  |  |  |
| 13 | `SC.ADJ.WHT.INCOME` | `ScAdjTxnUpdate_WhtIncome` |  |  |  |
| 14 | `SC.ADJ.TAX.RATE` | `ScAdjTxnUpdate_TaxRate` |  |  |  |
| 15 | `SC.ADJ.TAX.AMOUNT` | `ScAdjTxnUpdate_TaxAmount` |  |  |  |
| 16 | `SC.ADJ.CU.ACCT.NO` | `ScAdjTxnUpdate_CuAcctNo` |  |  |  |
| 17 | `SC.ADJ.CU.ACCT.CCY` | `ScAdjTxnUpdate_CuAcctCcy` |  |  |  |
| 18 | `SC.ADJ.CU.NET.AMT` | `ScAdjTxnUpdate_CuNetAmt` |  |  |  |
| 19 | `SC.ADJ.TAX.ACCOUNT` | `ScAdjTxnUpdate_TaxAccount` |  |  |  |
| 20 | `SC.ADJ.TAX.AMOUNT.CCY` | `ScAdjTxnUpdate_TaxAmountCcy` |  |  |  |
| 21 | `SC.ADJ.NEW.INCOME.CCY` | `ScAdjTxnUpdate_NewIncomeCcy` |  |  |  |
| 22 | `SC.ADJ.NEW.WHT.INCOME` | `ScAdjTxnUpdate_NewWhtIncome` |  |  |  |
| 23 | `SC.ADJ.NEW.INC.EXC.RATE` | `ScAdjTxnUpdate_NewIncExcRate` |  |  |  |
| 24 | `SC.ADJ.NEW.INC.TXN.CCY` | `ScAdjTxnUpdate_NewIncTxnCcy` |  |  |  |
| 25 | `SC.ADJ.NEW.TAX.RATE` | `ScAdjTxnUpdate_NewTaxRate` |  |  |  |
| 26 | `SC.ADJ.NEW.TAX.TXN.CCY` | `ScAdjTxnUpdate_NewTaxTxnCcy` |  |  |  |
| 27 | `SC.ADJ.NEW.TAX.EXC.RATE` | `ScAdjTxnUpdate_NewTaxExcRate` |  |  |  |
| 28 | `SC.ADJ.ADJ.TAX.CCY` | `ScAdjTxnUpdate_AdjTaxCcy` |  |  |  |
| 29 | `SC.ADJ.ADJ.TAX.LCCY` | `ScAdjTxnUpdate_AdjTaxLccy` |  |  |  |
| 30 | `SC.ADJ.NEW.TAX.EFF.DATE` | `ScAdjTxnUpdate_NewTaxEffDate` |  |  |  |
| 31 | `SC.ADJ.RESERVED.9` | `ScAdjTxnUpdate_Reserved9` |  |  |  |
| 32 | `SC.ADJ.RESERVED.8` | `ScAdjTxnUpdate_Reserved8` |  |  |  |
| 33 | `SC.ADJ.RESERVED.7` | `ScAdjTxnUpdate_Reserved7` |  |  |  |
| 34 | `SC.ADJ.RESERVED.6` | `ScAdjTxnUpdate_Reserved6` |  |  |  |
| 35 | `SC.ADJ.REIMB.TAX.CCY` | `ScAdjTxnUpdate_ReimbTaxCcy` | TField |  | Total adjusted tax amount in tax currency for which FUNDS.TRANSFER record will be created. validation rules: No input field. |
| 36 | `SC.ADJ.REIMB.TAX.ACCT.CAT` | `ScAdjTxnUpdate_ReimbTaxAcctCat` | TField | Yes | Category to which reimburstment of tax amount should be credit or debited based on the option in ADJ.TYPE field.This field is defaulted from the field REIMBURSE.CAT of the application SC.WHT.ADJ.PARAM. If the fieldREIMBURSE.CAT is not specified then this field should be a valid account. Adjusted tax amount in event currency validation rules: Mandatory field |
| 37 | `SC.ADJ.REIMB.TAX.EXC.RATE` | `ScAdjTxnUpdate_ReimbTaxExcRate` | TField |  | Exchange rate between REIMB.TAX.CCY and LCCY. |
| 38 | `SC.ADJ.REIMB.TAX.AMT.LCCY` | `ScAdjTxnUpdate_ReimbTaxAmtLccy` | TField |  | Total adjusted tax amount in local currency. validation rules: No input field. |
| 39 | `SC.ADJ.REIMB.CU.ACCOUNT` | `ScAdjTxnUpdate_ReimbCuAccount` | TField |  | Customer account to which tax has to be adjusted. validation rules: Valid account |
| 40 | `SC.ADJ.REIMB.CU.ACC.CCY` | `ScAdjTxnUpdate_ReimbCuAccCcy` | TField |  | Currency of the customer account defined in REIMB.CU.ACCOUNT field validation rules: No input field |
| 41 | `SC.ADJ.REIMB.CU.EXC.RATE` | `ScAdjTxnUpdate_ReimbCuExcRate` | TField |  | Exchange rate between TAX.CCY and REIMB.CU.ACC.CCY. |
| 42 | `SC.ADJ.REIMB.TAX.CU.ACCY` | `ScAdjTxnUpdate_ReimbTaxCuAccy` | TField |  | TAX amount in account currency. validation rules: No input field |
| 43 | `SC.ADJ.FT.ID` | `ScAdjTxnUpdate_FtId` | TField |  | FUNDS.TRANSFER id generated after authorising the record for reimbursment. validation rules: No input field |
| 44 | `SC.ADJ.TOTAL.ADJ.AMOUNT` | `ScAdjTxnUpdate_TotalAdjAmount` | TField |  | This field holds the sum of ADJ.AMOUNT |
| 45 | `SC.ADJ.VALUE.DATE` | `ScAdjTxnUpdate_ValueDate` | TField |  | This field holds the value date for payment |
| 46 | `SC.ADJ.SC.INCOME.RECLASSIFICATION` | `ScAdjTxnUpdate_ScIncomeReclassification` | TField |  | Holds the SC.INCOME.RECLASSIFICATION id Validation rules: No-input field |
| 47 | `SC.ADJ.LINK.REFERENCE` | `ScAdjTxnUpdate_LinkReference` | TField |  | This field indicates the transaction is created for events subject to S302 regulation of US IRS |
| 48 | `SC.ADJ.RESERVED.1` | `ScAdjTxnUpdate_Reserved1` | TField |  |  |
| 49 | `SC.ADJ.LOCAL.REF` | `ScAdjTxnUpdate_LocalRef` |  |  |  |
| 50 | `SC.ADJ.OVERRIDE` | `ScAdjTxnUpdate_Override` |  |  |  |
| 51 | `SC.ADJ.RECORD.STATUS` | `ScAdjTxnUpdate_RecordStatus` | String |  |  |
| 52 | `SC.ADJ.CURR.NO` | `ScAdjTxnUpdate_CurrNo` | String |  |  |
| 53 | `SC.ADJ.INPUTTER` | `ScAdjTxnUpdate_Inputter` |  |  |  |
| 54 | `SC.ADJ.DATE.TIME` | `ScAdjTxnUpdate_DateTime` |  |  |  |
| 55 | `SC.ADJ.AUTHORISER` | `ScAdjTxnUpdate_Authoriser` | String |  |  |
| 56 | `SC.ADJ.CO.CODE` | `ScAdjTxnUpdate_CoCode` | String |  |  |
| 57 | `SC.ADJ.DEPT.CODE` | `ScAdjTxnUpdate_DeptCode` | String |  |  |
| 58 | `SC.ADJ.AUDITOR.CODE` | `ScAdjTxnUpdate_AuditorCode` | String |  |  |
| 59 | `SC.ADJ.AUDIT.DATE.TIME` | `ScAdjTxnUpdate_AuditDateTime` | String |  |  |
| 60 | `SC.ADJ.INCOME.CODE` | `ScAdjTxnUpdate_IncomeCode` |  |  |  |
| 61 | `SC.ADJ.INCOME.AMOUNT` | `ScAdjTxnUpdate_IncomeAmount` |  |  |  |
| 62 | `SC.ADJ.INC.TAX.AMOUNT` | `ScAdjTxnUpdate_IncTaxAmount` |  |  |  |
| 63 | `SC.ADJ.INC.TAX.RATE` | `ScAdjTxnUpdate_IncTaxRate` |  |  |  |
| 64 | `SC.ADJ.TOTAL.TAX` | `ScAdjTxnUpdate_TotalTax` |  |  |  |
| 65 | `SC.ADJ.NEW.INCOME.CODE` | `ScAdjTxnUpdate_NewIncomeCode` |  |  |  |
| 66 | `SC.ADJ.NEW.INCOME.AMOUNT` | `ScAdjTxnUpdate_NewIncomeAmount` |  |  |  |
| 67 | `SC.ADJ.NEW.INC.TAX.AMOUNT` | `ScAdjTxnUpdate_NewIncTaxAmount` |  |  |  |
| 68 | `SC.ADJ.NEW.INC.TAX.RATE` | `ScAdjTxnUpdate_NewIncTaxRate` |  |  |  |
| 69 | `SC.ADJ.NEW.TOTAL.TAX` | `ScAdjTxnUpdate_NewTotalTax` |  |  |  |
| 70 | `SC.ADJ.ADJ.AMOUNT` | `ScAdjTxnUpdate_AdjAmount` |  |  |  |
| 71 | `SC.ADJ.NEW.INC.MAN.TAX.AMT` | `ScAdjTxnUpdate_NewIncManTaxAmt` |  |  |  |
| 72 | `SC.ADJ.MRGR.INCOME.CODE` | `ScAdjTxnUpdate_MrgrIncomeCode` |  |  |  |
| 73 | `SC.ADJ.TAX.EFF.DATE` | `ScAdjTxnUpdate_TaxEffDate` |  |  |  |
