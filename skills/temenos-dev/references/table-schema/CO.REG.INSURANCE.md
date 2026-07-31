# CO.REG.INSURANCE — Table Schema

> Source: `INSERTS/I_F.CO.REG.INSURANCE` in `CO_ModelBank.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CO.INS.DESCRIPTION` | `CoRegInsurance_Description` |  |  |  |
| 2 | `CO.INS.TYPE` | `CoRegInsurance_Type` | TField |  | TYPE indicates the Insurance type. For example, Term Insurance, Health Insurance, Life Insurance. |
| 3 | `CO.INS.POLICY.NUMBER` | `CoRegInsurance_PolicyNumber` | TField | Yes | An unique number given to the Insured person by the Insurer. Validation Rules: Mandatory field. |
| 4 | `CO.INS.CONTRACT.START.DATE` | `CoRegInsurance_ContractStartDate` | TField |  | "Effective date" on which the Insurance policy will become active. |
| 5 | `CO.INS.CONTRACT.EXPIRY.DATE` | `CoRegInsurance_ContractExpiryDate` | TField |  | Insurance Policy expiry date which is the date when the Policy ends. |
| 6 | `CO.INS.INSURANCE.OWNER` | `CoRegInsurance_InsuranceOwner` | TField |  | Insurance policyholder who has purchased the Insurance cover. |
| 7 | `CO.INS.INSURANCE.COMPANY` | `CoRegInsurance_InsuranceCompany` | TField |  | The financial institution that provides the Insurance cover. |
| 8 | `CO.INS.OTHER.DETAILS` | `CoRegInsurance_OtherDetails` |  |  |  |
| 9 | `CO.INS.INSURED.CUSTOMER` | `CoRegInsurance_InsuredCustomer` | TField |  | Insured customer is the person covered under the Insurance Policy. |
| 10 | `CO.INS.CURRENCY` | `CoRegInsurance_Currency` | TField |  | Currency of the Insurance cover amount. |
| 11 | `CO.INS.INSURANCE.AMOUNT` | `CoRegInsurance_InsuranceAmount` | TField |  | Insurance coverage amount which is the maximum amount of money payable by the Insurance company when a claim is made. |
| 12 | `CO.INS.SURRENDER.VALUE` | `CoRegInsurance_SurrenderValue` | TField |  | The amount of money the policy holder will get from the insurance company if he/she decides to exit the policy before maturity. |
| 13 | `CO.INS.INSURANCE.PREMIUM` | `CoRegInsurance_InsurancePremium` | TField |  | The amount of money paid by the insured person to the insurer to avail Insurance coverage. |
| 14 | `CO.INS.COEFFICIENT` | `CoRegInsurance_Coefficient` | TField |  | Margin Rate which will be applied on the Insurance to cover losses, expenses and profit given to the insurer. |
| 15 | `CO.INS.ADJ.MARKET.VALUE` | `CoRegInsurance_AdjMarketValue` | TField |  | Adjusted Insurance amount calculated by applying Coefficient rate on the Actual Insurance amount. |
| 16 | `CO.INS.SUG.ADJ.MARKET.VALUE` | `CoRegInsurance_SugAdjMarketValue` | TField |  | Revised Adjusted Insurance amount which may differ from the Insurance amount adjusted based on the Coefficient rate. |
| 17 | `CO.INS.LOCAL.REF` | `CoRegInsurance_LocalRef` |  |  |  |
| 18 | `CO.INS.OVERRIDE` | `CoRegInsurance_Override` |  |  |  |
| 19 | `CO.INS.RECORD.STATUS` | `CoRegInsurance_RecordStatus` | String |  |  |
| 20 | `CO.INS.CURR.NO` | `CoRegInsurance_CurrNo` | String |  |  |
| 21 | `CO.INS.INPUTTER` | `CoRegInsurance_Inputter` |  |  |  |
| 22 | `CO.INS.DATE.TIME` | `CoRegInsurance_DateTime` |  |  |  |
| 23 | `CO.INS.AUTHORISER` | `CoRegInsurance_Authoriser` | String |  |  |
| 24 | `CO.INS.CO.CODE` | `CoRegInsurance_CoCode` | String |  |  |
| 25 | `CO.INS.DEPT.CODE` | `CoRegInsurance_DeptCode` | String |  |  |
| 26 | `CO.INS.AUDITOR.CODE` | `CoRegInsurance_AuditorCode` | String |  |  |
| 27 | `CO.INS.AUDIT.DATE.TIME` | `CoRegInsurance_AuditDateTime` | String |  |  |
