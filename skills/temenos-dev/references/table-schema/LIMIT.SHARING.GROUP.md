# LIMIT.SHARING.GROUP — Table Schema

> Source: `INSERTS/I_F.LIMIT.SHARING.GROUP` in `LI_GroupLimit.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `LI.SG.SHORT.DESC` | `LimitSharingGroup_ShortDesc` |  |  |  |
| 2 | `LI.SG.CREDIT.LINE` | `LimitSharingGroup_CreditLine` | TField | Yes | This field is to denote Top product line of the Group Limit. Main Group: For Main group the credit line should be specified with a Global limit reference value when multiple allowed products are specified.In case alphanumeric limit reference is used it must not have any parent i.e., it should be top most product. Sub Group: For sub groups the credit line can be a global limit reference or a product reference or sub-product reference. Credit line is mandatory for Sub group as sub group limits are created for the credit line defined here. When global reference is specified it should be same as the Main group credit line value. When product reference is specified, it should be an allowed product in the Main group. When sub group product reference is specified, it should be a valid reference child of any of the allowed products in the Main group. For sub group the credit line must be top most reference Validation Rules: 1-10 numeric character Limit reference value.It must be a valid record on the LIMIT.REFERENCE file.Mandatory for Sub group.Mandatory for Main group when multiple values are specified in ALLOWED.PRODUCT field. |
| 3 | `LI.SG.PARENT.GROUP` | `LimitSharingGroup_ParentGroup` | TField | Yes | Used for sub groups to create a hierarchy with main group. This field should not be entered for Main groups and is mandatory for sub groups. A valid main group key can only be specified, this field will not accept sub group key as a parent group. Validation Rules: 1 Character (M), 1 to 9-digit sequence number. It must be a valid main group record on the LIMIT.SHARING.GROUP file |
| 4 | `LI.SG.ALLOWED.CUSTOMER` | `LimitSharingGroup_AllowedCustomer` |  |  |  |
| 5 | `LI.SG.ALLOWED.PRODUCT` | `LimitSharingGroup_AllowedProduct` |  |  |  |
| 6 | `LI.SG.MASTER.GROUP.KEY` | `LimitSharingGroup_MasterGroupKey` | TField |  | This field will be automatically updated by system during authorization with the master group key in which the sharing group key is linked. This will be updated only for the Main group and not for the sub groups. The Master group in LI.MASTER.GROUP will contain the group of sharing group keys with linked customers. The reallocation will happen based on the LI.MASTER.GROUP information. (For E.g if there are two sharing groups with related customers part of a master group, any reallocation on one group will do a reallocation on the other group based on the defined priority) Validation Rules: This is a no input field. Valid record from LI.MASTER.GROUP. |
| 7 | `LI.SG.LOCAL.REF` | `LimitSharingGroup_LocalRef` |  |  |  |
| 8 | `LI.SG.SINGLE.LINE.SER.NO` | `LimitSharingGroup_SingleLineSerNo` | TField |  | Holds the serial number of sharing group limit. Limit records can be created only if the serial number is input in this field. Any transaction of a customer belonging to this group can utilize this limit, irrespective of the Individual credit line serial numbers which the contract utilizes. If value of this field is blank, multiple credit lines can be created using serial numbers from 1 to 99. Example: Group Limit setup Limit Sharing Group M000000001 SINGLE.LINE.SER.NO 02 Allowed Product 0002000 Allowed Customer 900001 Transaction for Customer 900001 TXN REF Contract Limit Ref Limit Utilized Group Limit utilized Transaction 1 2020.01 M000000001.0002000.02.900001 Yes Transaction 2 2020.03 M000000001.0002000.02.900001 Yes Transaction 3 3030.01 900001.0003000.01 No, since Product is not a part of group limit. Validation Rules: NOCHANGE field. Accepted values are 1- 99. For Sub group limits, value in this field must be same as Parent group limit setup. |
| 9 | `LI.SG.RESERVED.4` | `LimitSharingGroup_Reserved4` | TField |  | Reserved for future use. This is a no input field. |
| 10 | `LI.SG.RESERVED.3` | `LimitSharingGroup_Reserved3` | TField |  | Reserved for future use. This is a no input field. |
| 11 | `LI.SG.RESERVED.2` | `LimitSharingGroup_Reserved2` | TField |  | Reserved for future use. This is a no input field. |
| 12 | `LI.SG.OVERRIDE` | `LimitSharingGroup_Override` |  |  |  |
| 13 | `LI.SG.RECORD.STATUS` | `LimitSharingGroup_RecordStatus` | String |  |  |
| 14 | `LI.SG.CURR.NO` | `LimitSharingGroup_CurrNo` | String |  |  |
| 15 | `LI.SG.INPUTTER` | `LimitSharingGroup_Inputter` |  |  |  |
| 16 | `LI.SG.DATE.TIME` | `LimitSharingGroup_DateTime` |  |  |  |
| 17 | `LI.SG.AUTHORISER` | `LimitSharingGroup_Authoriser` | String |  |  |
| 18 | `LI.SG.CO.CODE` | `LimitSharingGroup_CoCode` | String |  |  |
| 19 | `LI.SG.DEPT.CODE` | `LimitSharingGroup_DeptCode` | String |  |  |
| 20 | `LI.SG.AUDITOR.CODE` | `LimitSharingGroup_AuditorCode` | String |  |  |
| 21 | `LI.SG.AUDIT.DATE.TIME` | `LimitSharingGroup_AuditDateTime` | String |  |  |
