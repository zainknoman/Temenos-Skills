# AA.CUSTOMER.ROLE — Table Schema

> Source: `INSERTS/I_F.AA.CUSTOMER.ROLE` in `AA_Customer.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.CR.DESCRIPTION` | `AaCustomerRole_Description` |  |  |  |
| 2 | `AA.CR.BENEFICIAL.OWNER` | `AaCustomerRole_BeneficialOwner` | TField |  | This field indicates whether the customer(s) pertaining to the role is a beneficial owner of the arrangement. The Beneficial owner is a legal owner of the arrangement and is the responsible customer for the contract with the bank. Options: Yes or No |
| 3 | `AA.CR.TAXABLE` | `AaCustomerRole_Taxable` | TField |  | Defines whether the customer associated with the role is tax liable. Options: Yes or No |
| 4 | `AA.CR.MAX.TAX.LIAB.PERC` | `AaCustomerRole_MaxTaxLiabPerc` | TField |  | Defines the maximum tax liability percentage for this role. Validation rules Valid percentage equal or less than 100% |
| 5 | `AA.CR.LIMIT.CUSTOMER` | `AaCustomerRole_LimitCustomer` | TField |  | Defines whether the customer associated with the role requires a limit. Options: Yes or No Validation rules Must be Yes if the Beneficial Owner field is set to Yes. |
| 6 | `AA.CR.MIN.LIMIT.LIAB.PERC` | `AaCustomerRole_MinLimitLiabPerc` | TField |  | Reserved for Future use. |
| 7 | `AA.CR.MAX.LIMIT.LIAB.PERC` | `AaCustomerRole_MaxLimitLiabPerc` | TField |  | Reserved for Future use. |
| 8 | `AA.CR.GL.CUSTOMER` | `AaCustomerRole_GlCustomer` | TField |  | Defines whether the customer associated with the role be used to drive the composition of GL key. Options: Yes or No Validation rules Must be Yes if the Beneficial Owner field is set to Yes. |
| 9 | `AA.CR.GL.MIN.PERCENT` | `AaCustomerRole_GlMinPercent` | TField |  | Reserved for Future use. |
| 10 | `AA.CR.GL.MAX.PERCENT` | `AaCustomerRole_GlMaxPercent` | TField |  | Reserved for Future use. |
| 11 | `AA.CR.DELIVERY.CUSTOMER` | `AaCustomerRole_DeliveryCustomer` | TField |  | Defines whether the customer associated with the role receives standard delivery messages from T24. Options: Yes or No |
| 12 | `AA.CR.REL.PRICING.AVAIL` | `AaCustomerRole_RelPricingAvail` | TField |  | This field indicates whether, relationship pricing arrangements pertaining to the customer(s) with this role are to be considered while ascertaining and assigning the best possible relationship pricing arrangement to the financial arrangement. |
| 13 | `AA.CR.LOCAL.REF` | `AaCustomerRole_LocalRef` |  |  |  |
| 14 | `AA.CR.EXCLUDE.DORMANCY` | `AaCustomerRole_ExcludeDormancy` | TField |  | This field used to determine whether to exclude customer from dormancy processing or not. If set to YES, the customer is excluded from dormancy process. If the field MAINTAIN.INFO is opted either with HIGH.VOLUME or BASIC.INFO, then it is forced to set the value as YES. Options: Yes or Null |
| 15 | `AA.CR.MAINTAIN.INFO` | `AaCustomerRole_MaintainInfo` | TField |  | Defines whether the customer information needs to be updated on AA.CUSTOMER.ARRANGEMENT or AA.MASS.CUSTOMER.ARRANGEMENT or not both. Options: BASIC.INFO,COMPREHENSIVE,HIGH.VOLUME OR NULL BASIC.INFO - Customer Info will be updated only on AA.ARRANGEMENT. COMPREHENSIVE or NULL - Customer Info will be maintained on AA.ARRANGEMENT, AA.CUSTOMER.ARRANGEMENT and/or AA.CUSTOMER.RELATED.ARRANGEMENTS. HIGH.VOLUME - Customer Info will be updated on AA.ARRANGEMENT and AA.MASS.CUSTOMER.ARRANGEMENT. If the customer is HIGH.VOLUME or BASIC.INFO,it can be only non-beneficiary owner. Validation rules If the customer is High Volume or Basic Info, following validations are present Exclude dormancy should be set as yes. Delivery Customer and App Format fields are allowed to input. Other fields are not allowed to input. Note : For the beneficiary customer, Maintain info should be defined as COMPREHENSIVE or NULL. Otherwise Pricing and other functionalities will not be performed.There was no core functionality related with mass table updation. It was referring only to local development. |
| 16 | `AA.CR.BANK.CUSTOMER` | `AaCustomerRole_BankCustomer` | TField | No | Specify the role belonging to the participation. Optional and allowed value will be YES. |
| 17 | `AA.CR.BANK.ROLE.TYPE` | `AaCustomerRole_BankRoleType` | TField |  |  |
| 18 | `AA.CR.RECORD.STATUS` | `AaCustomerRole_RecordStatus` | String |  |  |
| 19 | `AA.CR.CURR.NO` | `AaCustomerRole_CurrNo` | String |  |  |
| 20 | `AA.CR.INPUTTER` | `AaCustomerRole_Inputter` |  |  |  |
| 21 | `AA.CR.DATE.TIME` | `AaCustomerRole_DateTime` |  |  |  |
| 22 | `AA.CR.AUTHORISER` | `AaCustomerRole_Authoriser` | String |  |  |
| 23 | `AA.CR.CO.CODE` | `AaCustomerRole_CoCode` | String |  |  |
| 24 | `AA.CR.DEPT.CODE` | `AaCustomerRole_DeptCode` | String |  |  |
| 25 | `AA.CR.AUDITOR.CODE` | `AaCustomerRole_AuditorCode` | String |  |  |
| 26 | `AA.CR.AUDIT.DATE.TIME` | `AaCustomerRole_AuditDateTime` | String |  |  |
| 27 | `AA.CR.APP.FORMAT` | `AaCustomerRole_AppFormat` | TField |  | When DE.CUSTOMER.PREFERENCE is created for a customer with this role, the id of the DE.PRODUCT will have the corresponding APP.FORMAT defined in the customer role. System will create as many DE.PRODUCTs as the unique APP.FORMAT based on the number of roles defined here. For example - US0010001.C-346099.8550.AAOWNR Application - AA APP.FORMAT - OWNR Validation rules Can allow any alphanumeric with maximum length of 4. |
| 28 | `AA.CR.EVENT.ROLE` | `AaCustomerRole_EventRole` | TField |  |  |
