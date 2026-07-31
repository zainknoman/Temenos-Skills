# AA.PRODUCT.GROUP — Table Schema

> Source: `INSERTS/I_F.AA.PRODUCT.GROUP` in `AA_ProductFramework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AA.PG.DESCRIPTION` | `AaProductGroup_Description` |  |  |  |
| 2 | `AA.PG.FULL.DESC` | `AaProductGroup_FullDesc` |  |  |  |
| 3 | `AA.PG.GROUP.TYPE` | `AaProductGroup_GroupType` |  |  |  |
| 4 | `AA.PG.PRODUCT.LINE` | `AaProductGroup_ProductLine` | TField | Yes | When defining a product group, it is mandatory that the group fall into one of the Product lines released by Temenos. When properties are stated in this table, it is mandatory that they should belong to one of the classes defined on the Product line. Product line is the highest level in designing a product. Validation rules: Should be a valid AA.PRODUCT.LINE id. Maximum of 20 characters |
| 5 | `AA.PG.PROPERTY.CLASS` | `AaProductGroup_PropertyClass` |  |  |  |
| 6 | `AA.PG.PROPERTY` | `AaProductGroup_Property` |  |  |  |
| 7 | `AA.PG.MANDATORY` | `AaProductGroup_Mandatory` |  |  |  |
| 8 | `AA.PG.LOCAL.REF` | `AaProductGroup_LocalRef` |  |  |  |
| 9 | `AA.PG.SYSTEM.GROUP` | `AaProductGroup_SystemGroup` | TField |  | Certain product groups are released by Temenos to perform mapping to existing parameter tables from Product designer conditions. These groups would have YES on these fields. Valid input must be either YES or null. This is system updated field and cannot be edited |
| 10 | `AA.PG.REBUILD.ACTIVITIES` | `AaProductGroup_RebuildActivities` | TField |  | System would perform rebuild activities by default irrespective of this attribute value. Hence no significance for this attribute. Either a new property is introduced into the group or a new activity class is introduced, system would rebuild the activities by default. |
| 11 | `AA.PG.ATTRIBUTE` | `AaProductGroup_Attribute` |  |  |  |
| 12 | `AA.PG.PRODUCT.TYPE` | `AaProductGroup_ProductType` | TField |  | Indicates the product code which would be allowed access for EB.EXTERNAL.USER. Allowed only for OTHER product line. Valid EB.PRODUCT entries are allowed. |
| 13 | `AA.PG.CATEGORY.FROM` | `AaProductGroup_CategoryFrom` |  |  |  |
| 14 | `AA.PG.CATEGORY.TO` | `AaProductGroup_CategoryTo` |  |  |  |
| 15 | `AA.PG.ADDITIONAL.CATEGORY` | `AaProductGroup_AdditionalCategory` |  |  |  |
| 16 | `AA.PG.EXCLUDED.CATEGORY` | `AaProductGroup_ExcludedCategory` |  |  |  |
| 17 | `AA.PG.PORTFOLIOS` | `AaProductGroup_Portfolios` |  |  |  |
| 18 | `AA.PG.PL.PC.CLASS` | `AaProductGroup_PlPcClass` |  |  |  |
| 19 | `AA.PG.RECORD.STATUS` | `AaProductGroup_RecordStatus` | String |  |  |
| 20 | `AA.PG.CURR.NO` | `AaProductGroup_CurrNo` | String |  |  |
| 21 | `AA.PG.INPUTTER` | `AaProductGroup_Inputter` |  |  |  |
| 22 | `AA.PG.DATE.TIME` | `AaProductGroup_DateTime` |  |  |  |
| 23 | `AA.PG.AUTHORISER` | `AaProductGroup_Authoriser` | String |  |  |
| 24 | `AA.PG.CO.CODE` | `AaProductGroup_CoCode` | String |  |  |
| 25 | `AA.PG.DEPT.CODE` | `AaProductGroup_DeptCode` | String |  |  |
| 26 | `AA.PG.AUDITOR.CODE` | `AaProductGroup_AuditorCode` | String |  |  |
| 27 | `AA.PG.AUDIT.DATE.TIME` | `AaProductGroup_AuditDateTime` | String |  |  |
| 28 | `AA.PG.REBUILD.BALANCE.TYPE` | `AaProductGroup_RebuildBalanceType` | TField |  | System will do automatic creation of Balance Types for all properties defined in product group , if Rebuild Balance Type is set to Yes. AC.BALANCE.TYPE will be updated with balance types created. If set to No ,System will not perform creation of Balance Types automatically |
| 29 | `AA.PG.RECONSTRUCT.SETTLEMENT` | `AaProductGroup_ReconstructSettlement` | TField |  | Indicates whether the settlement processing for settlement account needs to be reversed and replayed with the new or changed amounts/rates. Once we opted the Automatic behavior then the behavior should not be changed to Manual or Null. If this field is set then the Parameter Level setup will be ignored for this group alone.Backdated settlement functionality is enabled only if settlement account is AR/AC Account alone Note: Normally we recommend to set this flag at global level(System). This field can be set only when during the creating a new product group. Available options are: NULL/MANUAL - System will behave as existing old settlement process. AUTOMATIC - System will behave in new way where settlement processing is reversed and replayed. |
| 30 | `AA.PG.GROUP.LEVEL` | `AaProductGroup_GroupLevel` | TField |  | This field is to differentiate between the FACILITY or DEAL or CONTINGENT.LIABILITY Product Group. Guarantees can be booked either as an asset (in case of issuance) or a liability (in case of receiving). This field differentiates whether it is a contingent asset or a contingent liability. Depending on the flag, the Accounting entries will be raised. Contingent liability is the only allowed value for the Guarantees product line. If the option Fleet Finance is chosen, the facility can have only the Asset Finance arrangements of the Asset Finance products that are configured in the Sub arrangement Rules This facility can have only one type of Asset finance arrangements. Either Operating or Finance lease |
| 31 | `AA.PG.FEATURE.PROPERTY` | `AaProductGroup_FeatureProperty` |  |  |  |
| 32 | `AA.PG.RESERVED1` | `AaProductGroup_Reserved1` |  |  |  |
| 33 | `AA.PG.FEATURE.MANDATORY` | `AaProductGroup_FeatureMandatory` |  |  |  |
| 34 | `AA.PG.DESIGNER` | `AaProductGroup_Designer` |  |  |  |
| 35 | `AA.PG.RESERVED2` | `AaProductGroup_Reserved2` |  |  |  |
