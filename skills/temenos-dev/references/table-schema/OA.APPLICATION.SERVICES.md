# OA.APPLICATION.SERVICES — Table Schema

> Source: `INSERTS/I_F.OA.APPLICATION.SERVICES` in `OA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.OAS.ACTIVITY` | `OaApplicationServices_Activity` | TField |  | This field will indicate list of activities that can be performed on the OA.APPLICATION. Valid activities are : 1. UPDATE.PURPOSE-APPLICATION activity allows the user to add a new purpose to an existing application. 2. UPDATE.PRODUCT-APPLICATION activity allows the user to add a new product to an existing system or amend the existing product. 3. UPDATE.PARTY-APPLICATION activity allows the user to add a new party to an existing application. 4. UPDATE.PARTY.REFERENCE-APPLICATION activity allows the user to add party reference for the existing party form. 5. UPDATE.ASSET.REFERENCE-APPLICATION activity allows the user to add collateral/limit reference for the existing asset form. 5. CHANGE.OWNER-APPLICATION activity allows the user to change the Application owner. 6. CHANGE.STAGE.OWNER-APPLICATION activity allows to change the stage owner in an application. |
| 2 | `OA.OAS.APPLICATION.ID` | `OaApplicationServices_ApplicationId` | TField |  | This field will have a valid OA.APPLICATION id for which the update needs to happen. |
| 3 | `OA.OAS.PURPOSE` | `OaApplicationServices_Purpose` |  |  |  |
| 4 | `OA.OAS.PRODUCT` | `OaApplicationServices_Product` |  |  |  |
| 5 | `OA.OAS.OWNER` | `OaApplicationServices_Owner` |  |  |  |
| 6 | `OA.OAS.RESERVED.10` | `OaApplicationServices_Reserved10` | TField |  |  |
| 7 | `OA.OAS.RESERVED.9` | `OaApplicationServices_Reserved9` | TField |  |  |
| 8 | `OA.OAS.RESERVED.8` | `OaApplicationServices_Reserved8` | TField |  |  |
| 9 | `OA.OAS.RESERVED.7` | `OaApplicationServices_Reserved7` | TField |  |  |
| 10 | `OA.OAS.RESERVED.6` | `OaApplicationServices_Reserved6` | TField |  |  |
| 11 | `OA.OAS.DOMAIN.TYPE` | `OaApplicationServices_DomainType` |  |  |  |
| 12 | `OA.OAS.ROLE` | `OaApplicationServices_Role` |  |  |  |
| 13 | `OA.OAS.SEQUENCE` | `OaApplicationServices_Sequence` |  |  |  |
| 14 | `OA.OAS.REFERENCE` | `OaApplicationServices_Reference` |  |  |  |
| 15 | `OA.OAS.RESERVED.5` | `OaApplicationServices_Reserved5` | TField |  |  |
| 16 | `OA.OAS.RESERVED.4` | `OaApplicationServices_Reserved4` | TField |  |  |
| 17 | `OA.OAS.RESERVED.3` | `OaApplicationServices_Reserved3` | TField |  |  |
| 18 | `OA.OAS.RESERVED.2` | `OaApplicationServices_Reserved2` | TField |  |  |
| 19 | `OA.OAS.RESERVED.1` | `OaApplicationServices_Reserved1` | TField |  |  |
| 20 | `OA.OAS.LOCAL.REF` | `OaApplicationServices_LocalRef` |  |  |  |
| 21 | `OA.OAS.OVERRIDE` | `OaApplicationServices_Override` |  |  |  |
| 22 | `OA.OAS.RECORD.STATUS` | `OaApplicationServices_RecordStatus` | String |  |  |
| 23 | `OA.OAS.CURR.NO` | `OaApplicationServices_CurrNo` | String |  |  |
| 24 | `OA.OAS.INPUTTER` | `OaApplicationServices_Inputter` |  |  |  |
| 25 | `OA.OAS.DATE.TIME` | `OaApplicationServices_DateTime` |  |  |  |
| 26 | `OA.OAS.AUTHORISER` | `OaApplicationServices_Authoriser` | String |  |  |
| 27 | `OA.OAS.CO.CODE` | `OaApplicationServices_CoCode` | String |  |  |
| 28 | `OA.OAS.DEPT.CODE` | `OaApplicationServices_DeptCode` | String |  |  |
| 29 | `OA.OAS.AUDITOR.CODE` | `OaApplicationServices_AuditorCode` | String |  |  |
| 30 | `OA.OAS.AUDIT.DATE.TIME` | `OaApplicationServices_AuditDateTime` | String |  |  |
