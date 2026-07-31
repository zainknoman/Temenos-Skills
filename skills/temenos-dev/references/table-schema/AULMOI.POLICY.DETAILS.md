# AULMOI.POLICY.DETAILS — Table Schema

> Source: `INSERTS/I_F.AULMOI.POLICY.DETAILS` in `AULMOI_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `POLICY.DET.CUSTOMER` | `AulmoiPolicyDetails_Customer` | TField |  | Loan Borrower Customer Number |
| 2 | `POLICY.DET.POLICY.IDENTIFIER` | `AulmoiPolicyDetails_PolicyIdentifier` | TField |  | Policy identifiers will be issued by the insurer as part of origination or bulk insurance and will be unique across policies from a single insurer. |
| 3 | `POLICY.DET.INSURER.NAME` | `AulmoiPolicyDetails_InsurerName` | TField |  | Name of the Insurance Company |
| 4 | `POLICY.DET.POLICY.STATUS` | `AulmoiPolicyDetails_PolicyStatus` | TField |  | Status of each policy. Possible Values:1. In Force 2. Cancelled |
| 5 | `POLICY.DET.PREMIUM.CAPITALIZE` | `AulmoiPolicyDetails_PremiumCapitalize` | TField |  | To identify if a policy premium was capitalized or not. Possible Values: Y or NY � meaning premium was capitalized with loan principle. N � meaning premium was not capitalized with loan principle and paid by the borrower separately |
| 6 | `POLICY.DET.BULK.PURCHASE` | `AulmoiPolicyDetails_BulkPurchase` | TField |  | To identify if a policy was purchased individually or under bulk. Possible Values: Y or NY � meaning Bulk Policy was purchased. N � meaning Individual Policy was purchased |
| 7 | `POLICY.DET.EFFECTIVE.DATE` | `AulmoiPolicyDetails_EffectiveDate` | TField |  | Policy Effective Date � This date will be provided by the insurer in the origination or bulk insurance process and may not be the date that the policy is recorded in the MEB systems. Must be of the format DDMMYYYY |
| 8 | `POLICY.DET.AMT.INSURED` | `AulmoiPolicyDetails_AmtInsured` | TField |  | Amount Insured against each policy |
| 9 | `POLICY.DET.POLICY.LOADER` | `AulmoiPolicyDetails_PolicyLoader` |  |  |  |
| 10 | `POLICY.DET.POLICY.NARRATIVE` | `AulmoiPolicyDetails_PolicyNarrative` | TField |  | Free text notes against each policy |
| 11 | `POLICY.DET.TPC` | `AulmoiPolicyDetails_Tpc` | TField |  | Third Party Cost (TPC) flag of each policy. Possible Values: Y or N |
| 12 | `POLICY.DET.PAY.RECEIPT.NO` | `AulmoiPolicyDetails_PayReceiptNo` |  |  |  |
| 13 | `POLICY.DET.PAYMENT.DATE` | `AulmoiPolicyDetails_PaymentDate` |  |  |  |
| 14 | `POLICY.DET.PAYMENT.METHOD` | `AulmoiPolicyDetails_PaymentMethod` |  |  |  |
| 15 | `POLICY.DET.PREMIUM.PAID.BY` | `AulmoiPolicyDetails_PremiumPaidBy` |  |  |  |
| 16 | `POLICY.DET.POLICY.PREMIUM` | `AulmoiPolicyDetails_PolicyPremium` |  |  |  |
| 17 | `POLICY.DET.GST.AMT` | `AulmoiPolicyDetails_GstAmt` |  |  |  |
| 18 | `POLICY.DET.STAMP.DUTY.AMT` | `AulmoiPolicyDetails_StampDutyAmt` |  |  |  |
| 19 | `POLICY.DET.CLAIM.DATE` | `AulmoiPolicyDetails_ClaimDate` |  |  |  |
| 20 | `POLICY.DET.CLAIM.AMOUNT` | `AulmoiPolicyDetails_ClaimAmount` |  |  |  |
| 21 | `POLICY.DET.CLAIM.STATUS` | `AulmoiPolicyDetails_ClaimStatus` |  |  |  |
| 22 | `POLICY.DET.CLAIM.AMT.RECEIVED` | `AulmoiPolicyDetails_ClaimAmtReceived` |  |  |  |
| 23 | `POLICY.DET.INS.CLM.RECD.DATE` | `AulmoiPolicyDetails_InsClmRecdDate` |  |  |  |
| 24 | `POLICY.DET.INSURANCE.STATUS` | `AulmoiPolicyDetails_InsuranceStatus` | TField |  | Possible values: HLIC, Gemico, DUA, ME, DUA Insured, Non DUA Insured, Exception, NON-Uninsured |
| 25 | `POLICY.DET.LOCAL.REF` | `AulmoiPolicyDetails_LocalRef` |  |  |  |
| 26 | `POLICY.DET.OVERRIDE` | `AulmoiPolicyDetails_Override` |  |  |  |
| 27 | `POLICY.DET.RECORD.STATUS` | `AulmoiPolicyDetails_RecordStatus` | String |  |  |
| 28 | `POLICY.DET.CURR.NO` | `AulmoiPolicyDetails_CurrNo` | String |  |  |
| 29 | `POLICY.DET.INPUTTER` | `AulmoiPolicyDetails_Inputter` |  |  |  |
| 30 | `POLICY.DET.DATE.TIME` | `AulmoiPolicyDetails_DateTime` |  |  |  |
| 31 | `POLICY.DET.AUTHORISER` | `AulmoiPolicyDetails_Authoriser` | String |  |  |
| 32 | `POLICY.DET.CO.CODE` | `AulmoiPolicyDetails_CoCode` | String |  |  |
| 33 | `POLICY.DET.DEPT.CODE` | `AulmoiPolicyDetails_DeptCode` | String |  |  |
| 34 | `POLICY.DET.AUDITOR.CODE` | `AulmoiPolicyDetails_AuditorCode` | String |  |  |
| 35 | `POLICY.DET.AUDIT.DATE.TIME` | `AulmoiPolicyDetails_AuditDateTime` | String |  |  |
