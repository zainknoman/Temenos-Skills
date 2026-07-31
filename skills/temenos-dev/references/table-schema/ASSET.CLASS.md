# ASSET.CLASS — Table Schema

> Source: `INSERTS/I_F.ASSET.CLASS` in `ST_AssetProcessing.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.AC.DESCRIPTION` | `AssetClass_Description` |  |  |  |
| 2 | `EB.AC.ASSET.CATEGORY` | `AssetClass_AssetCategory` | TField |  | The new Asset Class being set up will be within a predefined range of categories, 11000 - 19999, in the total list of categories.It will also be in the range of Asset Categories within this list. For example, a category within the Fixed Assets range of categories could be for Cars, Asset Classes of this being Rover or BMW. Categories on this list are set up by users of the system. |
| 3 | `EB.AC.PROVISION.CATEG` | `AssetClass_ProvisionCateg` | TField |  | An existing CATEGORY code in the range 11000 19999. |
| 4 | `EB.AC.WRITE.OFF.CATEG` | `AssetClass_WriteOffCateg` | TField |  | An existing CATEGORY code in the range 1100 - 19999 |
| 5 | `EB.AC.DEP.CATEG` | `AssetClass_DepCateg` | TField |  | This a category for depreciation entries, which will be an existing category within a predefined range of categories set up by the user. Validation Rules: Within a predefined range of categories 60000 -64999. |
| 6 | `EB.AC.DEPRECIATION` | `AssetClass_Depreciation` | TField |  | Specifies whether depreciation is allowed for this type of class or not. |
| 7 | `EB.AC.CAPITAL.ALLOWANCE` | `AssetClass_CapitalAllowance` | TField |  | Specifies whether Capital Allowances are to be allowed for this type of Asset Class. The choices are either Yes or No. |
| 8 | `EB.AC.CA.CLAIMED.CATEG` | `AssetClass_CaClaimedCateg` | TField |  | The Capital Allowance claimed category. Must be in the range 11000 - 19999. |
| 9 | `EB.AC.CA.CONTROL.CATEG` | `AssetClass_CaControlCateg` | TField |  | Capital Allowances Control category . Must be in the range 11000 - 19999 |
| 10 | `EB.AC.DEP.TRANS.CODE.DR` | `AssetClass_DepTransCodeDr` | TField |  | The debit transaction code for depreciation . Validation Rules: It must exist on the TRANSACTION. File with DEBIT.CREDIT.INT = DEBIT |
| 11 | `EB.AC.DEP.TRANS.CODE.CR` | `AssetClass_DepTransCodeCr` | TField |  | The credit transaction code for depreciation. It must exist on the TRANSACTION file with DEBIT.CREDIT.IND = CREDIT. |
| 12 | `EB.AC.CA.TRANS.CODE.DR` | `AssetClass_CaTransCodeDr` | TField |  | The debit transaction code for Capital Allowances. It must exist on the TRANSACTION file with DEBIT.CREDIT.INT = DEBIT. |
| 13 | `EB.AC.CA.TRANS.CODE.CR` | `AssetClass_CaTransCodeCr` | TField |  | The credit transaction code for Capital Allowances. It must exist on the TRANSACTION file with DEBIT.CREDIT.INT = CREDIT |
| 14 | `EB.AC.DEPRECIATE.TO.ZERO` | `AssetClass_DepreciateToZero` | TField |  | This field decides how the value of an asset has to be depreciated. Allowed Values are NONE , YES , NO. YES : Depreciates the asset value to Zero. NONE/NO : Depreciates to Residual value (if provided) or to 1. Applicable only for SL , RB and FS |
| 15 | `EB.AC.CWIP.CATEGORY` | `AssetClass_CwipCategory` | TField |  | Identifies the GL Category against which Capital Work In Progress payments will be booked. A valid CATEGORY code in the range 11000-19999 |
| 16 | `EB.AC.PROFIT.CATEGORY` | `AssetClass_ProfitCategory` | TField |  | Identifies the PL Category against which Profit realised from disposal of a fixed assets are booked. A valid CATEGORY code in the range 60000-64999 |
| 17 | `EB.AC.LOSS.CATEGORY` | `AssetClass_LossCategory` | TField |  | Identifies the PL Category against which Loss incurred from disposal of a fixed assets are booked. A valid CATEGORY code in the range 60000-64999 |
| 18 | `EB.AC.PAYABLES.ACCT.CATEGORY` | `AssetClass_PayablesAcctCategory` | TField |  | Identifies the GL Category against which Payables account payments will be booked. A valid CATEGORY code in the range 11000-19999 |
| 19 | `EB.AC.RECEIVABLES.ACCT.CATEGORY` | `AssetClass_ReceivablesAcctCategory` | TField |  | Identifies the GL Category against which receivable account payments will be booked. A valid CATEGORY code in the range 11000-19999 |
| 20 | `EB.AC.ACTIVITY.TXN.DETAILS` | `AssetClass_ActivityTxnDetails` |  |  |  |
| 21 | `EB.AC.TXN.CODE.DR` | `AssetClass_TxnCodeDr` |  |  |  |
| 22 | `EB.AC.TXN.CODE.CR` | `AssetClass_TxnCodeCr` |  |  |  |
| 23 | `EB.AC.RESERVED1` | `AssetClass_Reserved1` |  |  |  |
| 24 | `EB.AC.LOCAL.REF` | `AssetClass_LocalRef` |  |  |  |
| 25 | `EB.AC.OVERRIDE` | `AssetClass_Override` |  |  |  |
| 26 | `EB.AC.RECORD.STATUS` | `AssetClass_RecordStatus` | String |  |  |
| 27 | `EB.AC.CURR.NO` | `AssetClass_CurrNo` | String |  |  |
| 28 | `EB.AC.INPUTTER` | `AssetClass_Inputter` |  |  |  |
| 29 | `EB.AC.DATE.TIME` | `AssetClass_DateTime` |  |  |  |
| 30 | `EB.AC.AUTHORISER` | `AssetClass_Authoriser` | String |  |  |
| 31 | `EB.AC.CO.CODE` | `AssetClass_CoCode` | String |  |  |
| 32 | `EB.AC.DEPT.CODE` | `AssetClass_DeptCode` | String |  |  |
| 33 | `EB.AC.AUDITOR.CODE` | `AssetClass_AuditorCode` | String |  |  |
| 34 | `EB.AC.AUDIT.DATE.TIME` | `AssetClass_AuditDateTime` | String |  |  |
