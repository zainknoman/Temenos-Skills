# USREGS.CONTACT.DETAILS — Table Schema

> Source: `INSERTS/I_F.USREGS.CONTACT.DETAILS` in `USREGS_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `USREGS.CONTACT.CUSTOMER` | `UsregsContactDetails_Customer` |  |  |  |
| 2 | `USREGS.CONTACT.CUS.CONTACT` | `UsregsContactDetails_CusContact` | TField |  | Field to capture if the changes were initiated by Customer. Allowed values are Y and N or Null. |
| 3 | `USREGS.CONTACT.CONTACT.TYPE` | `UsregsContactDetails_ContactType` |  |  |  |
| 4 | `USREGS.CONTACT.IDD.PREFIX` | `UsregsContactDetails_IddPrefix` |  |  |  |
| 5 | `USREGS.CONTACT.CONTACT.DATA` | `UsregsContactDetails_ContactData` |  |  |  |
| 6 | `USREGS.CONTACT.DEVICE.PRIVACY` | `UsregsContactDetails_DevicePrivacy` |  |  |  |
| 7 | `USREGS.CONTACT.PRIMARY.CONTACT` | `UsregsContactDetails_PrimaryContact` |  |  |  |
| 8 | `USREGS.CONTACT.PREF.CONTACT.TIME` | `UsregsContactDetails_PrefContactTime` |  |  |  |
| 9 | `USREGS.CONTACT.TCPA.CONSENT` | `UsregsContactDetails_TcpaConsent` |  |  |  |
| 10 | `USREGS.CONTACT.CONSENT.DATE` | `UsregsContactDetails_ConsentDate` |  |  |  |
| 11 | `USREGS.CONTACT.LOCAL.REF` | `UsregsContactDetails_LocalRef` |  |  |  |
| 12 | `USREGS.CONTACT.OVERRIDE` | `UsregsContactDetails_Override` |  |  |  |
| 13 | `USREGS.CONTACT.RECORD.STATUS` | `UsregsContactDetails_RecordStatus` | String |  |  |
| 14 | `USREGS.CONTACT.CURR.NO` | `UsregsContactDetails_CurrNo` | String |  |  |
| 15 | `USREGS.CONTACT.INPUTTER` | `UsregsContactDetails_Inputter` |  |  |  |
| 16 | `USREGS.CONTACT.DATE.TIME` | `UsregsContactDetails_DateTime` |  |  |  |
| 17 | `USREGS.CONTACT.AUTHORISER` | `UsregsContactDetails_Authoriser` | String |  |  |
| 18 | `USREGS.CONTACT.CO.CODE` | `UsregsContactDetails_CoCode` | String |  |  |
| 19 | `USREGS.CONTACT.DEPT.CODE` | `UsregsContactDetails_DeptCode` | String |  |  |
| 20 | `USREGS.CONTACT.AUDITOR.CODE` | `UsregsContactDetails_AuditorCode` | String |  |  |
| 21 | `USREGS.CONTACT.AUDIT.DATE.TIME` | `UsregsContactDetails_AuditDateTime` | String |  |  |
