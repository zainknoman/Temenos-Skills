# MT.TENANT.CONTACT — Table Schema

> Source: `INSERTS/I_F.MT.TENANT.CONTACT` in `MT_Framework.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `MT.TC.DESCRIPTION` | `MtTenantContact_Description` |  |  |  |
| 2 | `MT.TC.CONTACT.NAME` | `MtTenantContact_ContactName` | TField | Yes | Specifies the name of the contact point Validation Rules: Maximum of 35 alphanumerics allowed Mandatory field |
| 3 | `MT.TC.MOBILE.NUMBER` | `MtTenantContact_MobileNumber` | TField |  | This field will contain mobile number of the tenant contact Validation Rules: Maximum of 17 characters allowed . |
| 4 | `MT.TC.LANDLINE` | `MtTenantContact_Landline` | TField |  | This field can contain land line number of the tenant contact point Validation Rules: Allowed maximum of 17 characters |
| 5 | `MT.TC.EMAIL` | `MtTenantContact_Email` | TField |  | This field can contain official Email address of the tenant contact point Validation Rules: Maximum of 50 characters allowed. |
| 6 | `MT.TC.CONTACT.TYPE` | `MtTenantContact_ContactType` |  |  |  |
| 7 | `MT.TC.CONTACT.DETAILS` | `MtTenantContact_ContactDetails` |  |  |  |
| 8 | `MT.TC.RESERVED.8` | `MtTenantContact_Reserved8` | TField |  |  |
| 9 | `MT.TC.RESERVED.7` | `MtTenantContact_Reserved7` | TField |  |  |
| 10 | `MT.TC.RESERVED.6` | `MtTenantContact_Reserved6` | TField |  |  |
| 11 | `MT.TC.RESERVED.5` | `MtTenantContact_Reserved5` | TField |  |  |
| 12 | `MT.TC.RESERVED.4` | `MtTenantContact_Reserved4` | TField |  |  |
| 13 | `MT.TC.RESERVED.3` | `MtTenantContact_Reserved3` | TField |  |  |
| 14 | `MT.TC.RESERVED.2` | `MtTenantContact_Reserved2` | TField |  |  |
| 15 | `MT.TC.RESERVED.1` | `MtTenantContact_Reserved1` | TField |  |  |
| 16 | `MT.TC.LOCAL.REF` | `MtTenantContact_LocalRef` |  |  |  |
| 17 | `MT.TC.OVERRIDE` | `MtTenantContact_Override` |  |  |  |
| 18 | `MT.TC.RECORD.STATUS` | `MtTenantContact_RecordStatus` | String |  |  |
| 19 | `MT.TC.CURR.NO` | `MtTenantContact_CurrNo` | String |  |  |
| 20 | `MT.TC.INPUTTER` | `MtTenantContact_Inputter` |  |  |  |
| 21 | `MT.TC.DATE.TIME` | `MtTenantContact_DateTime` |  |  |  |
| 22 | `MT.TC.AUTHORISER` | `MtTenantContact_Authoriser` | String |  |  |
| 23 | `MT.TC.CO.CODE` | `MtTenantContact_CoCode` | String |  |  |
| 24 | `MT.TC.DEPT.CODE` | `MtTenantContact_DeptCode` | String |  |  |
| 25 | `MT.TC.AUDITOR.CODE` | `MtTenantContact_AuditorCode` | String |  |  |
| 26 | `MT.TC.AUDIT.DATE.TIME` | `MtTenantContact_AuditDateTime` | String |  |  |
