# SC.WHT.INC.BASE — Table Schema

> Source: `INSERTS/I_F.SC.WHT.INC.BASE` in `SC_SccEntitlements.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `SC.WIB.CLASSIFICATION` | `ScWhtIncBase_Classification` | TField |  | Client classification (FATCA STATUS) from FATCA.CUSTOMER.SUPPLEMENTARY.INFO record. |
| 2 | `SC.WIB.SECURITY.NO` | `ScWhtIncBase_SecurityNo` | TField |  | The security master ID of the entitlement. |
| 3 | `SC.WIB.EVENT.TYPE` | `ScWhtIncBase_EventType` | TField |  | Event type of the entitlement |
| 4 | `SC.WIB.DEPOSITORY` | `ScWhtIncBase_Depository` | TField |  | Depository from the entitlement record |
| 5 | `SC.WIB.SUB.ACCOUNT` | `ScWhtIncBase_SubAccount` | TField |  | Sub account from the entitlement record |
| 6 | `SC.WIB.SOURCE.LOCAL` | `ScWhtIncBase_SourceLocal` | TField |  | Whether the withholding is done at source or local. |
| 7 | `SC.WIB.TRANS.DATE` | `ScWhtIncBase_TransDate` | TField |  | Value date of the entitlement |
| 8 | `SC.WIB.TRANS.CCY` | `ScWhtIncBase_TransCcy` | TField |  | Event currency of the entitlement |
| 9 | `SC.WIB.ENTITLEMENT.AMT` | `ScWhtIncBase_EntitlementAmt` | TField |  | Entitlement amount of the underlying entitlement record |
| 10 | `SC.WIB.WHT.INCOME` | `ScWhtIncBase_WhtIncome` | TField |  | Final WHT income on which tax is applied. |
| 11 | `SC.WIB.TAX.RATE` | `ScWhtIncBase_TaxRate` | TField |  | The rate at which the original tax is levied. |
| 12 | `SC.WIB.TAX.AMOUNT` | `ScWhtIncBase_TaxAmount` | TField |  | Tax amount of the entitlement |
| 13 | `SC.WIB.CU.ACCT.NO` | `ScWhtIncBase_CuAcctNo` | TField |  | The customer account of the entitlement record |
| 14 | `SC.WIB.CU.ACCT.CCY` | `ScWhtIncBase_CuAcctCcy` | TField |  | The currency of the account in the field Cu Acct No. |
| 15 | `SC.WIB.CU.NET.AMT` | `ScWhtIncBase_CuNetAmt` | TField |  | The net amount of the entitlement. |
| 16 | `SC.WIB.TAX.ACCOUNT` | `ScWhtIncBase_TaxAccount` | TField |  | Tax account to which the tax amounts are originally posted |
| 17 | `SC.WIB.TAX.AMOUNT.CCY` | `ScWhtIncBase_TaxAmountCcy` | TField |  | Tax amount posted to the account in the field TAX.ACCOUNT. |
| 18 | `SC.WIB.TAX.AMOUNT.LCCY` | `ScWhtIncBase_TaxAmountLccy` | TField |  | The tax amount in local currency. |
| 19 | `SC.WIB.ORG.TAX.AMOUNT` | `ScWhtIncBase_OrgTaxAmount` | TField |  | Tax amount before offsetting the tax from SC.WHT.SOURCE.LOCAL application. |
| 20 | `SC.WIB.OFF.TAX.AMOUNT` | `ScWhtIncBase_OffTaxAmount` | TField |  | Tax amount after offsetting the tax from SC.WHT.SOURCE.LOCAL application. |
| 21 | `SC.WIB.OFF.TAX.CODE` | `ScWhtIncBase_OffTaxCode` | TField |  | Tax code used for offsetting given in SC.WHT.SOURCE.LOCAL application. |
| 22 | `SC.WIB.OFF.TAX.RATE` | `ScWhtIncBase_OffTaxRate` | TField |  | Tax rate used for offsetting given in SC.WHT.SOURCE.LOCAL application. |
| 23 | `SC.WIB.ADJ.DATE` | `ScWhtIncBase_AdjDate` |  |  |  |
| 24 | `SC.WIB.ADJ.TYPE` | `ScWhtIncBase_AdjType` |  |  |  |
| 25 | `SC.WIB.ADJ.INCOME` | `ScWhtIncBase_AdjIncome` |  |  |  |
| 26 | `SC.WIB.ADJ.TAX.AMT` | `ScWhtIncBase_AdjTaxAmt` |  |  |  |
| 27 | `SC.WIB.ADJ.TAX.RATE` | `ScWhtIncBase_AdjTaxRate` |  |  |  |
| 28 | `SC.WIB.ADJ.FT.ID` | `ScWhtIncBase_AdjFtId` |  |  |  |
| 29 | `SC.WIB.ADJ.CU.ACCT` | `ScWhtIncBase_AdjCuAcct` |  |  |  |
| 30 | `SC.WIB.ADJ.TAX.ACCT` | `ScWhtIncBase_AdjTaxAcct` |  |  |  |
| 31 | `SC.WIB.ADJ.TAX.AMT.LCCY` | `ScWhtIncBase_AdjTaxAmtLccy` |  |  |  |
| 32 | `SC.WIB.NEW.INCOME.CODE` | `ScWhtIncBase_NewIncomeCode` |  |  |  |
| 33 | `SC.WIB.NEW.INCOME.AMOUNT` | `ScWhtIncBase_NewIncomeAmount` |  |  |  |
| 34 | `SC.WIB.NEW.INC.TAX.AMOUNT` | `ScWhtIncBase_NewIncTaxAmount` |  |  |  |
| 35 | `SC.WIB.NEW.INC.TAX.RATE` | `ScWhtIncBase_NewIncTaxRate` |  |  |  |
| 36 | `SC.WIB.NEW.TOTAL.TAX` | `ScWhtIncBase_NewTotalTax` |  |  |  |
| 37 | `SC.WIB.TOTAL.WHT.INCOME` | `ScWhtIncBase_TotalWhtIncome` | TField |  | The adjusted income after taking into account all the adjustments to income above |
| 38 | `SC.WIB.TOTAL.TAX.AMOUNT` | `ScWhtIncBase_TotalTaxAmount` | TField |  | The total tax amount in event currency after adding all the tax adjustment amounts from SC.ADJ.TXN.UPDATEapplication. |
| 39 | `SC.WIB.TOTAL.TAX.AMT.LCCY` | `ScWhtIncBase_TotalTaxAmtLccy` | TField |  | The total tax amount in local currency |
| 40 | `SC.WIB.ENT.STATUS` | `ScWhtIncBase_EntStatus` | TField |  | Entitlement status "LIVE" - updated when entitlement record is authorised from INA status "REVE" - updated when entitlement record is reversed from RNA status |
| 41 | `SC.WIB.CUSTOMER` | `ScWhtIncBase_Customer` | TField |  | The customer in the entitlement record. |
| 42 | `SC.WIB.ENT.ID` | `ScWhtIncBase_EntId` | TField |  | Entitlement id pertaining to this record |
| 43 | `SC.WIB.RATE.TYPE` | `ScWhtIncBase_RateType` | TField |  | Rate type from DIARY record |
| 44 | `SC.WIB.GROSS.AMT` | `ScWhtIncBase_GrossAmt` | TField |  | Gross amount calculated based on the rate type of diary.Updated only for TXN.TAX.CODE with TAX.PARAM.FILE asFATCA.PARAMETER. If the rate type in DIARY is NET then following calculation is performed to get the GROSS.AMT NET AMT of 7000 is converted into GROSS AMT of 10000 with 30% source tax DEAL.AMT = 7000 * 100 / (100 - 30) = 10000 |
| 45 | `SC.WIB.TAX.CODE` | `ScWhtIncBase_TaxCode` | TField |  |  |
| 46 | `SC.WIB.TAX.EFF.DATE` | `ScWhtIncBase_TaxEffDate` |  |  |  |
