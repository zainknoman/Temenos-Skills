# CUSTOMER.CHARGE — Table Schema

> Source: `INSERTS/I_F.CUSTOMER.CHARGE` in `CG_ChargeConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.CCH.APPLICATION` | `CustomerCharge_Application` |  |  |  |
| 2 | `EB.CCH.DEFAULT.GROUP` | `CustomerCharge_DefaultGroup` |  |  |  |
| 3 | `EB.CCH.ACTUAL.GROUP` | `CustomerCharge_ActualGroup` |  |  |  |
| 4 | `EB.CCH.PORTFOLIO.GROUP` | `CustomerCharge_PortfolioGroup` |  |  |  |
| 5 | `EB.CCH.SC.APPLICATION` | `CustomerCharge_ScApplication` |  |  |  |
| 6 | `EB.CCH.PORTFOLIO` | `CustomerCharge_Portfolio` |  |  |  |
| 7 | `EB.CCH.SC.DEF.GROUP` | `CustomerCharge_ScDefGroup` |  |  |  |
| 8 | `EB.CCH.SC.ACT.GROUP` | `CustomerCharge_ScActGroup` |  |  |  |
| 9 | `EB.CCH.TR.APPLICATION` | `CustomerCharge_TrApplication` |  |  |  |
| 10 | `EB.CCH.PORTFOLIO.ID` | `CustomerCharge_PortfolioId` |  |  |  |
| 11 | `EB.CCH.TR.DEF.GROUP` | `CustomerCharge_TrDefGroup` |  |  |  |
| 12 | `EB.CCH.TR.ACT.GROUP` | `CustomerCharge_TrActGroup` |  |  |  |
| 13 | `EB.CCH.DEPOSITORY.GROUP` | `CustomerCharge_DepositoryGroup` | TField | No | Defines the depository charge group. This holds the customer depository charge group in the form "NNN" or "C-NNN" which must be a valid group condition. This is used when calculating safekeeping charges for the depository. Input is optional unless the customer security type is "DEPOSITORY". |
| 14 | `EB.CCH.CHARGE.FREQ` | `CustomerCharge_ChargeFreq` |  |  |  |
| 15 | `EB.CCH.DEBIT.ACCOUNT` | `CustomerCharge_DebitAccount` |  |  |  |
| 16 | `EB.CCH.CHARGE.CODE` | `CustomerCharge_ChargeCode` |  |  |  |
| 17 | `EB.CCH.CHG.COM.ACCOUNT` | `CustomerCharge_ChgComAccount` | TField | No | Defines the account number to be debited when the customer is required to pay commission/charges. This account will be used in the Funds Transfer application only, when the customer is required to pay commission/charges. An override will be required if the account customer is not the same as the customer of the record. 1 to 14 numeric account number 3 - 10 alphanumeric account mnemonic (Optional Input) Must exist on the Account file. Cannot be an internal amount. |
| 18 | `EB.CCH.LOCAL.REF` | `CustomerCharge_LocalRef` |  |  |  |
| 19 | `EB.CCH.TAX.TYPE` | `CustomerCharge_TaxType` |  |  |  |
| 20 | `EB.CCH.TAX.DEF.GROUP` | `CustomerCharge_TaxDefGroup` |  |  |  |
| 21 | `EB.CCH.TAX.ACT.GROUP` | `CustomerCharge_TaxActGroup` |  |  |  |
| 22 | `EB.CCH.CHG.ADV.REQD` | `CustomerCharge_ChgAdvReqd` | TField | Yes | Defines if an advice is required when the charge amount dcerived from the defined CHARGE.CODE is taken. T24 will generate a message type 1960 when this field is set to Y. Default value NO. Y or NO. (Mandatory Field) |
| 23 | `EB.CCH.DELIVERY.REF` | `CustomerCharge_DeliveryRef` |  |  |  |
| 24 | `EB.CCH.CUSTOMER.COMPANY` | `CustomerCharge_CustomerCompany` | TField |  | This field holds a valid company id. Should have an entry in COMPANY file. |
| 25 | `EB.CCH.SPLIT.CHARGE.ENTRY` | `CustomerCharge_SplitChargeEntry` | TField |  | Defines whether the charges are supposed to be raised as seperate or combined entries to the customer account Possible values are YES and NO. If set as 'YES', seperate charge entries will be raised. |
| 26 | `EB.CCH.REBUILD.CUSTOMER.CHARGE` | `CustomerCharge_RebuildCustomerCharge` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 27 | `EB.CCH.STMT.NO` | `CustomerCharge_StmtNo` |  |  |  |
| 28 | `EB.CCH.OVERRIDE` | `CustomerCharge_Override` |  |  |  |
| 29 | `EB.CCH.RECORD.STATUS` | `CustomerCharge_RecordStatus` | String |  |  |
| 30 | `EB.CCH.CURR.NO` | `CustomerCharge_CurrNo` | String |  |  |
| 31 | `EB.CCH.INPUTTER` | `CustomerCharge_Inputter` |  |  |  |
| 32 | `EB.CCH.DATE.TIME` | `CustomerCharge_DateTime` |  |  |  |
| 33 | `EB.CCH.AUTHORISER` | `CustomerCharge_Authoriser` | String |  |  |
| 34 | `EB.CCH.CO.CODE` | `CustomerCharge_CoCode` | String |  |  |
| 35 | `EB.CCH.DEPT.CODE` | `CustomerCharge_DeptCode` | String |  |  |
| 36 | `EB.CCH.AUDITOR.CODE` | `CustomerCharge_AuditorCode` | String |  |  |
| 37 | `EB.CCH.AUDIT.DATE.TIME` | `CustomerCharge_AuditDateTime` | String |  |  |
