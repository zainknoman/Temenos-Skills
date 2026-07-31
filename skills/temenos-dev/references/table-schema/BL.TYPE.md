# BL.TYPE — Table Schema

> Source: `INSERTS/I_F.BL.TYPE` in `BL_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BL.TYP.DESCRIPTION` | `BlType_Description` |  |  |  |
| 2 | `BL.TYP.SHORT.DESC` | `BlType_ShortDesc` |  |  |  |
| 3 | `BL.TYP.CATEGORY` | `BlType_Category` | TField | Yes | The category of the Bill (whether it is Discounted or Collection or Collateral) under which it will be reported has to be input in this field. This field will be defaulted during the BL.REGISTER processing. Once authorised this field cannot be changed. To change existing category use New Category field. ie. 21050 for Bills Discount or 30000 for Bills Collateral or 30001 for Bills Collection etc... Validation Rules: 5 numeric characters. (Mandatory input) The code entered must be present on the CATEGORY file. |
| 4 | `BL.TYP.PRODUCT.TYPE` | `BlType_ProductType` | TField |  | This field defines the type of Product and conditions to be applied. Validation Rules: Allowed Products are - Discounting,Collection,Factoring,Forfaiting. Not allowed with existing product definitions - DISCOUNT,COLLATERAL,COLLECTION. |
| 5 | `BL.TYP.ADV.DISBURSEMENT` | `BlType_AdvDisbursement` | TField |  | This field defines whether the Payment can be made in advance. Validation Rules: Allowed Values are "Allowed" and "Not Allowed". Not Allowed for Product type Collection. Must be Allowed for Product type Discounting. Default Value - Allowed for other Product Types. |
| 6 | `BL.TYP.RETENTION.MARGIN` | `BlType_RetentionMargin` | TField |  | This field defines whether retention margin is applicable for the product type. Validation Rules: Allowed Values are "Allowed" and "Not Allowed". Not Allowed for Product type Collection. Allowed only when ADV.DISBURSEMENT is set to "Allowed". |
| 7 | `BL.TYP.RET.MARGIN.ENTRY` | `BlType_RetMarginEntry` | TField |  | This field defines whether contingent entry needs to be raised for retention margin amount. Validation Rules: Allowed values are "Yes" and "No". Allowed only when RETENTION.MARGIN is set to "Allowed". Allowed when ADV.DISBURSEMENT is set to "Not Allowed"(Collection). If YES is chosen with RETENTION.MARGIN as "ALLOWED", contingent entry will be raised for the margin amount. If YES is chosen with ADV.DISBURSEMENT as "NOT.ALLOWED", contingent entry will be raised for the bill amount. |
| 8 | `BL.TYP.PART.DISBURSEMENT` | `BlType_PartDisbursement` | TField |  | This field defines whether partial disbursement is allowed against available discount amount for the product type. Validation Rules: Allowed values are "Allowed" and "Not Allowed". Input to be allowed only when ADV.DISBURSEMENT is set to 'Allowed'. Default Value - "Not Allowed". |
| 9 | `BL.TYP.PART.SETTLEMENT` | `BlType_PartSettlement` | TField |  | This field defines whether partial settlement is allowed under the product type. Validation Rules: Allowed values are "Allowed" and "Not Allowed". Default value - 'Allowed'. |
| 10 | `BL.TYP.CHANGE.PRODUCT` | `BlType_ChangeProduct` | TField |  | This field defines whether product type can be modified. Validation Rules: Allowed only when Product type is Collection. Default value - "Allowed" for product Collection and "Not Allowed" for other product types. |
| 11 | `BL.TYP.LIABILITY.PTY` | `BlType_LiabilityPty` |  |  |  |
| 12 | `BL.TYP.INFO.LIMIT.PTY` | `BlType_InfoLimitPty` |  |  |  |
| 13 | `BL.TYP.INFO.LIMIT.REF` | `BlType_InfoLimitRef` | TField | Yes | This field defines the valid limit product for info limit party. Validation Rules: Mandatory when INFO.LIMIT.PARTY is defined expect for "Buyer-Seller". Must be valid limit product from LIMIT.REFERENCE. Must be defined as 'IN'(Info limit) in FX.TIME.BAND field in LIMIT.REFERENCE. |
| 14 | `BL.TYP.AGEING.AT.MAT` | `BlType_AgeingAtMat` | TField | Yes | This field defines whether ageing process needs to be triggered if bill is not settled on maturity date. Validation Rules: Allowed values are Yes and No. Mandatory when ADV.DISBURSEMENT is set to 'Allowed'. |
| 15 | `BL.TYP.CONSOLIDATION.REQD` | `BlType_ConsolidationReqd` | TField | Yes | This field defines whether accounting and limit updation should be consolidated when multiple invoices are processed under batch. Validation Rules: Allowed values are Yes and No. Mandatory Field when PRODUCT.TYPE is defined. |
| 16 | `BL.TYP.NEW.CATEGORY` | `BlType_NewCategory` | TField |  | If the already defined Category has to be changed, the new category shall be given in this field. The new category code changes to category code during next end of day processing. All the current BL contracts which has the existing category code assigned to new category code and the transaction pertaining to these contracts assigned with new category code during End of day processing. Validation Rules: T24 Standard Category Code Must have a record in CATEGORY table. |
| 17 | `BL.TYP.RECOURSE` | `BlType_Recourse` | TField |  | This field defines whether the deal customer is liable in case of non settlement of bills. Validation Rules: Allowed Values are Yes, No, Partial. Not allowed for Collection. Default Value - 'Yes' for all other Products. |
| 18 | `BL.TYP.DISCOUNT` | `BlType_Discount` | TField |  | This is an YES OR NO Field which will determine whether the BL.REGISTER of this type could be included in a Discount Contract. Validation Rules: YES or NO |
| 19 | `BL.TYP.REDISCOUNT` | `BlType_Rediscount` | TField |  | This field defines whether re-discounting is allowed for the product. Validation Rules: Allowed values are "Allowed" and "Not Allowed". Allowed only with Product Discounting. Default value - "Allowed" for product Discounting and "Not Allowed" for other product types. |
| 20 | `BL.TYP.ACCEPT` | `BlType_Accept` | TField |  | For future use |
| 21 | `BL.TYP.COLLATERAL` | `BlType_Collateral` | TField |  | This is an YES or NO field which will determine whether the BL.REGISTER of this type could be included in a Collateral Type of a Contract. Validation Rules: YES or NO |
| 22 | `BL.TYP.COLLECTION` | `BlType_Collection` | TField |  | This is an YES OR NO Field which will determine whether the BL.REGISTER of this type could be included in a Discount Contract. Validation Rules: YES or NO |
| 23 | `BL.TYP.MAX.TERM` | `BlType_MaxTerm` | TField |  | This field defines the maximum tenor of the Bill that is acceptable. If the tenor of the Bill exceeds the defined parameter, an override message will appear. Both Minimum and maximum must have a same term (ie. Month or Days) Validation Rules: Months 1M, 2 M Days 10, 365 |
| 24 | `BL.TYP.MIN.TERM` | `BlType_MinTerm` | TField |  | This field defines the minimum tenor of the Bill that is acceptable. If the tenor of the Bill exceeds the defined parameter, an override message will appear. Both minimum and maximum term must have same term (ie.Month or Days) Validation Rules: Months 1M, 2 M Days 10, 365 |
| 25 | `BL.TYP.APPLICATION.FORMAT` | `BlType_ApplicationFormat` | TField | No | This field can be used to specify the application format which will be used instead of the default value "1" while generating messages for BR's which has this BL.TYPE. This allows the format of advices to be defined at the BL.TYPE level. When input is valid in this field, appropriate record should be available in the DE.FORMAT.PRINT file. The value in this field will form the second part of the key to the file DE.FORMAT.PRINT. The key will be derived appending the value in this field to the literal 'BL'. For example, input of a '2' in this field will mean that the key to DE.FORMAT.PRINT will be 405.BL2.1.GB instead of the default 405.1.1.GB. Thus there should be a record in DE.FORMAT.PRINT with id as 405.BL2.1.GB. Validation Rules: 4 numeric characters. Optional input. Default is 1 if left blank. |
| 26 | `BL.TYP.RESERVED.9` | `BlType_Reserved9` | TField |  |  |
| 27 | `BL.TYP.RESERVED.8` | `BlType_Reserved8` | TField |  |  |
| 28 | `BL.TYP.RESERVED.7` | `BlType_Reserved7` | TField |  |  |
| 29 | `BL.TYP.RESERVED.6` | `BlType_Reserved6` | TField |  |  |
| 30 | `BL.TYP.RESERVED.5` | `BlType_Reserved5` | TField |  |  |
| 31 | `BL.TYP.RESERVED.4` | `BlType_Reserved4` | TField |  |  |
| 32 | `BL.TYP.RESERVED.3` | `BlType_Reserved3` | TField |  |  |
| 33 | `BL.TYP.RESERVED.2` | `BlType_Reserved2` | TField |  |  |
| 34 | `BL.TYP.RESERVED.1` | `BlType_Reserved1` | TField |  |  |
| 35 | `BL.TYP.LOCAL.REF` | `BlType_LocalRef` |  |  |  |
| 36 | `BL.TYP.RECORD.STATUS` | `BlType_RecordStatus` | String |  |  |
| 37 | `BL.TYP.CURR.NO` | `BlType_CurrNo` | String |  |  |
| 38 | `BL.TYP.INPUTTER` | `BlType_Inputter` |  |  |  |
| 39 | `BL.TYP.DATE.TIME` | `BlType_DateTime` |  |  |  |
| 40 | `BL.TYP.AUTHORISER` | `BlType_Authoriser` | String |  |  |
| 41 | `BL.TYP.CO.CODE` | `BlType_CoCode` | String |  |  |
| 42 | `BL.TYP.DEPT.CODE` | `BlType_DeptCode` | String |  |  |
| 43 | `BL.TYP.AUDITOR.CODE` | `BlType_AuditorCode` | String |  |  |
| 44 | `BL.TYP.AUDIT.DATE.TIME` | `BlType_AuditDateTime` | String |  |  |
