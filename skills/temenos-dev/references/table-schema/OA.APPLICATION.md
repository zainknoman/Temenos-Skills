# OA.APPLICATION — Table Schema

> Source: `INSERTS/I_F.OA.APPLICATION` in `OA_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OA.APP.ACTIVITY.PURPOSE` | `OaApplication_ActivityPurpose` | TField |  | This field is only allowed for activities of class type "TRANSIT.STAGE-APPLICATION" when moving application from one stage to an other. Since the Application has more than one purpose,( example , BUY.HOME can be bundled with PURCHASE.INSURANCE), the different purposes can moved separately from/to different stages Hence this field indicate the purpose concernate by the TRANSIT.STAGE-APPLICATION activity 1)Input is validated against AA.PURPOSE table |
| 2 | `OA.APP.ACTIVITY` | `OaApplication_Activity` | TField | Yes | This field defines the Activity to be processed against the Application. Input is validated against AA.CLASS.TYPE.ACTIVITY table Input is mandatory |
| 3 | `OA.APP.PURPOSE` | `OaApplication_Purpose` |  |  |  |
| 4 | `OA.APP.VERSION` | `OaApplication_Version` |  |  |  |
| 5 | `OA.APP.PRODUCT` | `OaApplication_Product` |  |  |  |
| 6 | `OA.APP.DOMAIN.CLASS` | `OaApplication_DomainClass` |  |  |  |
| 7 | `OA.APP.ROLE` | `OaApplication_Role` |  |  |  |
| 8 | `OA.APP.TYPE` | `OaApplication_Type` |  |  |  |
| 9 | `OA.APP.SEQUENCE` | `OaApplication_Sequence` |  |  |  |
| 10 | `OA.APP.REFERENCE` | `OaApplication_Reference` |  |  |  |
| 11 | `OA.APP.FORM.PURPOSE` | `OaApplication_FormPurpose` |  |  |  |
| 12 | `OA.APP.FORM` | `OaApplication_Form` |  |  |  |
| 13 | `OA.APP.STATUS` | `OaApplication_Status` |  |  |  |
| 14 | `OA.APP.FORM.REFERENCE` | `OaApplication_FormReference` |  |  |  |
| 15 | `OA.APP.LINK.TYPE` | `OaApplication_LinkType` |  |  |  |
| 16 | `OA.APP.LINK.REFERENCE` | `OaApplication_LinkReference` |  |  |  |
| 17 | `OA.APP.APPLICATION.REFERENCE` | `OaApplication_ApplicationReference` | TField |  | This fields accepts the application reference of an existing application. It will be used to copy the data from previous application to current application. |
| 18 | `OA.APP.RESERVED.6` | `OaApplication_Reserved6` | TField |  |  |
| 19 | `OA.APP.RESERVED.5` | `OaApplication_Reserved5` | TField |  |  |
| 20 | `OA.APP.RESERVED.4` | `OaApplication_Reserved4` | TField |  |  |
| 21 | `OA.APP.RESERVED.3` | `OaApplication_Reserved3` | TField |  |  |
| 22 | `OA.APP.RESERVED.2` | `OaApplication_Reserved2` | TField |  |  |
| 23 | `OA.APP.ID.COMPONENT` | `OaApplication_IdComponent` | TField |  |  |
| 24 | `OA.APP.LOCAL.REF` | `OaApplication_LocalRef` |  |  |  |
| 25 | `OA.APP.OVERRIDE` | `OaApplication_Override` |  |  |  |
| 26 | `OA.APP.RECORD.STATUS` | `OaApplication_RecordStatus` | String |  |  |
| 27 | `OA.APP.CURR.NO` | `OaApplication_CurrNo` | String |  |  |
| 28 | `OA.APP.INPUTTER` | `OaApplication_Inputter` |  |  |  |
| 29 | `OA.APP.DATE.TIME` | `OaApplication_DateTime` |  |  |  |
| 30 | `OA.APP.AUTHORISER` | `OaApplication_Authoriser` | String |  |  |
| 31 | `OA.APP.CO.CODE` | `OaApplication_CoCode` | String |  |  |
| 32 | `OA.APP.DEPT.CODE` | `OaApplication_DeptCode` | String |  |  |
| 33 | `OA.APP.AUDITOR.CODE` | `OaApplication_AuditorCode` | String |  |  |
| 34 | `OA.APP.AUDIT.DATE.TIME` | `OaApplication_AuditDateTime` | String |  |  |
| 35 | `OA.APP.ASSET.REFERENCE` | `OaApplication_AssetReference` |  |  |  |
| 36 | `OA.APP.UNIQUE.IDENTIFIER` | `OaApplication_UniqueIdentifier` |  |  |  |
