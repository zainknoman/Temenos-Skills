# IS.ASSET.REVIEW — Table Schema

> Source: `INSERTS/I_F.IS.ASSET.REVIEW` in `IS_Purchase.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `IS.ASR.CUSTOMER` | `IsAssetReview_Customer` | TField | Yes | The Customer who requests the asset and the contract is booked for the same. Validation Rules: 1. Field Mandatory and No Change. 2. Must be a valid record in the table CUSTOMER. |
| 2 | `IS.ASR.PURCHASE.REF` | `IsAssetReview_PurchaseRef` | TField | Yes | The Contract through which the Customer has initiated the Asset Request. Validation Rules: 1. Field Mandatory. 2. Must be a valid record from the table IS.CONTRACT. |
| 3 | `IS.ASR.COMMODITY` | `IsAssetReview_Commodity` | TField |  | Commodity of the purchase contract that is being reviewed. The commodity should be purchased in the contract through the application IS.CONTRACT. Validation Rules: 1. The commodity must be purchased in the Contract. |
| 4 | `IS.ASR.ASSET.REF` | `IsAssetReview_AssetRef` | TField |  | The asset for which the review is performed. The asset should one of the assets required in the contract through the application IS.CONTRACT Validation Rules: 1. The asset must be purchased in the Contract. |
| 5 | `IS.ASR.CURRENCY` | `IsAssetReview_Currency` | TField |  | Currency of the Purchase contract. Validation Rules: 1. Defaulted from the IS.CONTRACT record. 2. Valid record from CURRENCY table |
| 6 | `IS.ASR.VALUE.DATE` | `IsAssetReview_ValueDate` | TField |  | The date that the valuation is effective. Validation Rules: 1. Standard T24 Date field. |
| 7 | `IS.ASR.DESCRIPTION` | `IsAssetReview_Description` |  |  |  |
| 8 | `IS.ASR.CUSTOMER.ACCT` | `IsAssetReview_CustomerAcct` | TField |  | The Customer account recorded in the Asset Request Contract. The Customer contribution is collected from the account given in this field. The account number is defaulted from the Asset Request contract Validation Rules: 1. Must be a valid record in the table ACCOUNT. 2. Account must belong to the Contract Customer. 3. NOSTRO or VOSTRO account not allowed. |
| 9 | `IS.ASR.REVIEWER` | `IsAssetReview_Reviewer` | TField | Yes | The Appraiser or Surveyor who reviews the asset. Validation Rules: 1. Valid record in the table IS.REVIEWER. 2. Field Mandatory. |
| 10 | `IS.ASR.REVIEWER.NAME` | `IsAssetReview_ReviewerName` | TField |  | Name of the Appraiser. Defaulted as Name of the Customer (@ID being Customer Reference). It can be over-written to specify User-Defined names. Validation Rules: 1. Defaulted as NAME.1 from the Customer table. 2. Standard T24 Alphanumeric field. |
| 11 | `IS.ASR.REVIEWER.TYPE` | `IsAssetReview_ReviewerType` | TField |  | The Type of review the reviewer will perform. Validation Rules: 1. Field No-input. 2. The value to be defaulted from &quot;TYPE&quot; field of the IS.REVIEWER table. |
| 12 | `IS.ASR.REVIEWER.ACCT` | `IsAssetReview_ReviewerAcct` | TField |  | Account of the Reviewer in the logged-in Company and Contract Currency. This account number is defaulted from the parameterization of IS.REVIEWER record. Validation Rules: 1. Must be a valid record in the table ACCOUNT. 2. Account must belong to the Reviewer Customer. 3. NOSTRO or VOSTRO account not allowed. |
| 13 | `IS.ASR.REVIEW.DATE` | `IsAssetReview_ReviewDate` | TField |  | The Visit Date of the appraiser. This is the date on which the Appraiser visits and records review status of the Asset. Validation Rules: 1. Standard T24 Date field. |
| 14 | `IS.ASR.APPRAISER.VALUE` | `IsAssetReview_AppraiserValue` | TField |  | The amount that the appraiser has valuated on the asset. |
| 15 | `IS.ASR.PROGRESS.PERCENT` | `IsAssetReview_ProgressPercent` | TField |  | The Progress percentage of the asset (say Building Construction) being reviewed. It will be a user-defined value fed by the user based on the appraisal details. Validation Rules: 1. Accepts a Valid Percentage. |
| 16 | `IS.ASR.PROJECT.STATUS` | `IsAssetReview_ProjectStatus` | TField |  | The Progress status of the Appraisal whether the asset manufacture/ building construction is in Schedule, Late, etc. Validation Rules: 1. The valid values are On Schedule, Late, Ahead of Schedule. |
| 17 | `IS.ASR.NOTES` | `IsAssetReview_Notes` | TField |  | Any comments provided by the appraiser during the survey is recorded in this field. Validation Rules: 1. Standard T24 Alphanumeric field. |
| 18 | `IS.ASR.VALUATION.FEES` | `IsAssetReview_ValuationFees` | TField | Yes | The Valuation Fees to be paid to the Appraiser. Validation Rules: 1. Field Mandatory. 2. Must be a non-negative value. 3. Bank contribution and Customer contribution should sum to the value in the field VALUATION.FEES |
| 19 | `IS.ASR.BANK.SHARE` | `IsAssetReview_BankShare` | TField |  | Bank&apos;s contribution for the Appraiser fees. Validation Rules: 1. Bank contribution and Customer contribution should sum to the value in the field VALUATION.FEES |
| 20 | `IS.ASR.CUST.SHARE` | `IsAssetReview_CustShare` | TField |  | Customer&apos;s contribution for the Appraiser fees. Validation Rules: 1. Bank contribution and Customer contribution should sum to the value in the field VALUATION.FEES |
| 21 | `IS.ASR.NEXT.REVIEW.DATE` | `IsAssetReview_NextReviewDate` | TField |  | The Next visit date of the Review planned. Validation Rules: 1. Standard T24 Date field. 2. Date should be greater than TODAY. |
| 22 | `IS.ASR.RESERVED.15` | `IsAssetReview_Reserved15` |  |  |  |
| 23 | `IS.ASR.RESERVED.14` | `IsAssetReview_Reserved14` | TField |  |  |
| 24 | `IS.ASR.RESERVED.13` | `IsAssetReview_Reserved13` | TField |  |  |
| 25 | `IS.ASR.RESERVED.12` | `IsAssetReview_Reserved12` | TField |  |  |
| 26 | `IS.ASR.RESERVED.11` | `IsAssetReview_Reserved11` | TField |  |  |
| 27 | `IS.ASR.RESERVED.10` | `IsAssetReview_Reserved10` | TField |  |  |
| 28 | `IS.ASR.RESERVED.9` | `IsAssetReview_Reserved9` | TField |  |  |
| 29 | `IS.ASR.RESERVED.8` | `IsAssetReview_Reserved8` | TField |  |  |
| 30 | `IS.ASR.RESERVED.7` | `IsAssetReview_Reserved7` | TField |  |  |
| 31 | `IS.ASR.RESERVED.6` | `IsAssetReview_Reserved6` | TField |  |  |
| 32 | `IS.ASR.RESERVED.5` | `IsAssetReview_Reserved5` | TField |  |  |
| 33 | `IS.ASR.RESERVED.4` | `IsAssetReview_Reserved4` | TField |  |  |
| 34 | `IS.ASR.RESERVED.3` | `IsAssetReview_Reserved3` | TField |  |  |
| 35 | `IS.ASR.RESERVED.2` | `IsAssetReview_Reserved2` | TField |  |  |
| 36 | `IS.ASR.RESERVED.1` | `IsAssetReview_Reserved1` | TField |  |  |
| 37 | `IS.ASR.LOCAL.REF` | `IsAssetReview_LocalRef` |  |  |  |
| 38 | `IS.ASR.STMT.NOS` | `IsAssetReview_StmtNos` |  |  |  |
| 39 | `IS.ASR.OVERRIDE` | `IsAssetReview_Override` |  |  |  |
| 40 | `IS.ASR.RECORD.STATUS` | `IsAssetReview_RecordStatus` | String |  |  |
| 41 | `IS.ASR.CURR.NO` | `IsAssetReview_CurrNo` | String |  |  |
| 42 | `IS.ASR.INPUTTER` | `IsAssetReview_Inputter` |  |  |  |
| 43 | `IS.ASR.DATE.TIME` | `IsAssetReview_DateTime` |  |  |  |
| 44 | `IS.ASR.AUTHORISER` | `IsAssetReview_Authoriser` | String |  |  |
| 45 | `IS.ASR.CO.CODE` | `IsAssetReview_CoCode` | String |  |  |
| 46 | `IS.ASR.DEPT.CODE` | `IsAssetReview_DeptCode` | String |  |  |
| 47 | `IS.ASR.AUDITOR.CODE` | `IsAssetReview_AuditorCode` | String |  |  |
| 48 | `IS.ASR.AUDIT.DATE.TIME` | `IsAssetReview_AuditDateTime` | String |  |  |
