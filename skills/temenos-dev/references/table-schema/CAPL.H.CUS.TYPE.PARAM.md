# CAPL.H.CUS.TYPE.PARAM — Table Schema

> Source: `INSERTS/I_F.CAPL.H.CUS.TYPE.PARAM` in `CABASE_CustomerRelation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CAPL.CTP.DESCRIPTION` | `CaplHCusTypeParam_Description` |  |  |  |
| 2 | `CAPL.CTP.CONTAINER` | `CaplHCusTypeParam_Container` | TField |  | This field is used to define whether the ID type of Customer is a Container or CIF.Allowed values are YES/NOIf YES the customer is a container.If NO the customer is a CIF. |
| 3 | `CAPL.CTP.OWNERSHIP.RULE` | `CaplHCusTypeParam_OwnershipRule` | TField |  | This field is used to define the condition to be considered for ownership rule for the ID customer.Validation - Valid record from CAPL.H.OWNERSHIP.RULE |
| 4 | `CAPL.CTP.CUS.UNIQUE` | `CaplHCusTypeParam_CusUnique` | TField |  | This field is used to define whether the uniqueness validationapplicable for the ID customer type.Allowed inputs : YES/NOIf set to "Y" if uniqueness is required for this type of customer. Non changeable from "N" to "Y". |
| 5 | `CAPL.CTP.UNIQUENESS.RULE` | `CaplHCusTypeParam_UniquenessRule` | TField |  | This field is associated to the CUS.UNIQUE field. If the CUS.UNIQUE is set to Yes. Then the corresponding uniqueness rule to be mentioned in this field.Applicable when CUS.UNIQUE is set to YESValidation: Valid record from CAPL.H.CUS.UNIQUE.PARAM table. |
| 6 | `CAPL.CTP.SIGNATORY` | `CaplHCusTypeParam_Signatory` | TField |  | This field is used to defien the whether thesignatory validation is required or not for the customer type.Set to "Y" if signatory is required for this type of customer. Non changeable from "N" to "Y".Validation: Radio button field. valide options are Yes / No / None. |
| 7 | `CAPL.CTP.SIGNATORY.RULE` | `CaplHCusTypeParam_SignatoryRule` | TField |  | This field is associated to the SIGNATORY field. If the SIGNATORY is set to Yes. Then the corresponding signatory rule to be mentioned in this field.Validation: Valid record from CAPL.H.SIGNATORY.RULE |
| 8 | `CAPL.CTP.ACCT.PRODUCT.RULE` | `CaplHCusTypeParam_AcctProductRule` | TField |  | No functionality at this point. Reserved for future usage.Points to table CAPL.CUS.PRODUCT.PARAM or a routine where the products or service configuration rules for this customer type are allowed for situations where the ACCT.GEN.CONDITION or AA product designer does not cover. This requirement is customer specific. |
| 9 | `CAPL.CTP.SHARE.ACCT` | `CaplHCusTypeParam_ShareAcct` | TField |  | The purpose of the field is used to define the categories to be considered for Share accounts.Note: Normally Contianer type of customer will have share acconts.Applicable for FI using Member concept.Validation - reocrd of ACCOUNT.CLASS, validates against the category field in ACCOUNT.CLASS record.eg. U-SHARE |
| 10 | `CAPL.CTP.DEFAULTING.RULE` | `CaplHCusTypeParam_DefaultingRule` | TField |  | Reserved for future usage. |
| 11 | `CAPL.CTP.CASCADING.RULE` | `CaplHCusTypeParam_CascadingRule` | TField |  | This field is used to define the cascading rules to be considered for cascade the informations at Customer level and Member level.Valid record from CAPL.CASCADE.RULE table. |
| 12 | `CAPL.CTP.SECTOR.ALLOW` | `CaplHCusTypeParam_SectorAllow` |  |  |  |
| 13 | `CAPL.CTP.INDUSTRY.ALLOW` | `CaplHCusTypeParam_IndustryAllow` |  |  |  |
| 14 | `CAPL.CTP.CUS.REL.CODE.ALLOW` | `CaplHCusTypeParam_CusRelCodeAllow` |  |  |  |
| 15 | `CAPL.CTP.CUS.EB.ROLE.ALLOW` | `CaplHCusTypeParam_CusEbRoleAllow` |  |  |  |
| 16 | `CAPL.CTP.CHK.AA.PRODUCT` | `CaplHCusTypeParam_ChkAaProduct` |  |  |  |
| 17 | `CAPL.CTP.THRESHOLD.LIMIT` | `CaplHCusTypeParam_ThresholdLimit` | TField |  |  |
| 18 | `CAPL.CTP.RESERVED.8` | `CaplHCusTypeParam_Reserved8` | TField |  |  |
| 19 | `CAPL.CTP.SAM.REL.CODE.ALLOW` | `CaplHCusTypeParam_SamRelCodeAllow` |  |  |  |
| 20 | `CAPL.CTP.PROD.REL.CODE.ALLOW` | `CaplHCusTypeParam_ProdRelCodeAllow` |  |  |  |
| 21 | `CAPL.CTP.AA.REL.CODE.ALLOW` | `CaplHCusTypeParam_AaRelCodeAllow` |  |  |  |
| 22 | `CAPL.CTP.SDB.REL.ALLOW` | `CaplHCusTypeParam_SdbRelAllow` |  |  |  |
| 23 | `CAPL.CTP.PROD.ROLE` | `CaplHCusTypeParam_ProdRole` |  |  |  |
| 24 | `CAPL.CTP.TOTAL.DOC.MANDATE` | `CaplHCusTypeParam_TotalDocMandate` | TField |  | This field is used to define the total document required for this type of customer.During on boarding process to capture customer details, valid document for identification purpose, is checked if the document provided meet the business rule.Allowed with max length of 3 numeric character. |
| 25 | `CAPL.CTP.MANDATE.CLASS` | `CaplHCusTypeParam_MandateClass` |  |  |  |
| 26 | `CAPL.CTP.MANDATE.COUNT` | `CaplHCusTypeParam_MandateCount` |  |  |  |
| 27 | `CAPL.CTP.NON.MANDATE.CLASS` | `CaplHCusTypeParam_NonMandateClass` |  |  |  |
| 28 | `CAPL.CTP.NON.MANDATE.COUNT` | `CaplHCusTypeParam_NonMandateCount` |  |  |  |
| 29 | `CAPL.CTP.MDSB.REL.CODE.AL` | `CaplHCusTypeParam_MdsbRelCodeAl` |  |  |  |
| 30 | `CAPL.CTP.MDSB.AA.PROD.ROLE` | `CaplHCusTypeParam_MdsbAaProdRole` |  |  |  |
| 31 | `CAPL.CTP.MDSB.IND.AL` | `CaplHCusTypeParam_MdsbIndAl` |  |  |  |
| 32 | `CAPL.CTP.XML.ADDR.REQD` | `CaplHCusTypeParam_XmlAddrReqd` | TField |  | This field is used to define whether the xml address to be created for a customer automatically in DE.ADDRESS table.Allowed values are YES/NoIf YES - record in DE.ADDRESS get created automatically for XML.1If NO xml address in DE.ADDRESS not get updated automatically. |
| 33 | `CAPL.CTP.CUSTOMER.TYPE` | `CaplHCusTypeParam_CustomerType` | TField |  | This field is used to define the customer type, based on which the customer names are Cascaded to the Member record.Allowed values: Business and Personal.Business - ENT.ORG.NAME in Member record will be cascaded with the details of NAME.1 value of the customer.Personal - ENT.ORG.NAME in Member record will be cascaded with the details of as FAMILY.NAME and first letter of GIVEN.NAMES with separator as , |
| 34 | `CAPL.CTP.LOCAL.REF` | `CaplHCusTypeParam_LocalRef` |  |  |  |
| 35 | `CAPL.CTP.OVERRIDE` | `CaplHCusTypeParam_Override` |  |  |  |
| 36 | `CAPL.CTP.RESERVED.3` | `CaplHCusTypeParam_Reserved3` | TField |  |  |
| 37 | `CAPL.CTP.RESERVED.2` | `CaplHCusTypeParam_Reserved2` | TField |  |  |
| 38 | `CAPL.CTP.RESERVED.1` | `CaplHCusTypeParam_Reserved1` | TField |  |  |
| 39 | `CAPL.CTP.RECORD.STATUS` | `CaplHCusTypeParam_RecordStatus` | String |  |  |
| 40 | `CAPL.CTP.CURR.NO` | `CaplHCusTypeParam_CurrNo` | String |  |  |
| 41 | `CAPL.CTP.INPUTTER` | `CaplHCusTypeParam_Inputter` |  |  |  |
| 42 | `CAPL.CTP.DATE.TIME` | `CaplHCusTypeParam_DateTime` |  |  |  |
| 43 | `CAPL.CTP.AUTHORISER` | `CaplHCusTypeParam_Authoriser` | String |  |  |
| 44 | `CAPL.CTP.CO.CODE` | `CaplHCusTypeParam_CoCode` | String |  |  |
| 45 | `CAPL.CTP.DEPT.CODE` | `CaplHCusTypeParam_DeptCode` | String |  |  |
| 46 | `CAPL.CTP.AUDITOR.CODE` | `CaplHCusTypeParam_AuditorCode` | String |  |  |
| 47 | `CAPL.CTP.AUDIT.DATE.TIME` | `CaplHCusTypeParam_AuditDateTime` | String |  |  |
