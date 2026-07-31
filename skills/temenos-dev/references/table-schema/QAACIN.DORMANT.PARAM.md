# QAACIN.DORMANT.PARAM — Table Schema

> Source: `INSERTS/I_F.QAACIN.DORMANT.PARAM` in `QAACIN_DormantAccounts.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `QAACIN.DORM.ACCOUNT.STATUS` | `QaacinDormantParam_AccountStatus` |  |  |  |
| 2 | `QAACIN.DORM.POSTING.RESTRICT` | `QaacinDormantParam_PostingRestrict` |  |  |  |
| 3 | `QAACIN.DORM.QATAR.ID.DOC.TYPE` | `QaacinDormantParam_QatarIdDocType` | TField |  | Details of the legal document type that represents the Qatar ID |
| 4 | `QAACIN.DORM.PASSPORT.DOC.TYPE` | `QaacinDormantParam_PassportDocType` | TField |  | Details of the legal document type that represents the passport type |
| 5 | `QAACIN.DORM.COMPANY.REG.DOC.TYPE` | `QaacinDormantParam_CompanyRegDocType` | TField |  | Details of the legal document type that represents the company registration type |
| 6 | `QAACIN.DORM.RESERVED.1` | `QaacinDormantParam_Reserved1` | TField |  | reserved for future use. |
| 7 | `QAACIN.DORM.RESERVED.2` | `QaacinDormantParam_Reserved2` | TField |  | reserved for future use. |
| 8 | `QAACIN.DORM.RESERVED.3` | `QaacinDormantParam_Reserved3` | TField |  | reserved for future use. |
| 9 | `QAACIN.DORM.RESERVED.4` | `QaacinDormantParam_Reserved4` | TField |  | reserved for future use. |
| 10 | `QAACIN.DORM.RESERVED.5` | `QaacinDormantParam_Reserved5` | TField |  | reserved for future use. |
| 11 | `QAACIN.DORM.RESERVED.6` | `QaacinDormantParam_Reserved6` | TField |  | reserved for future use. |
| 12 | `QAACIN.DORM.RESERVED.7` | `QaacinDormantParam_Reserved7` | TField |  | reserved for future use. |
| 13 | `QAACIN.DORM.RESERVED.8` | `QaacinDormantParam_Reserved8` | TField |  | reserved for future use. |
| 14 | `QAACIN.DORM.RESERVED.9` | `QaacinDormantParam_Reserved9` | TField |  | reserved for future use. |
| 15 | `QAACIN.DORM.RESERVED.10` | `QaacinDormantParam_Reserved10` | TField |  | reserved for future use. |
| 16 | `QAACIN.DORM.LOCAL.REF` | `QaacinDormantParam_LocalRef` |  |  |  |
| 17 | `QAACIN.DORM.OVERRIDE` | `QaacinDormantParam_Override` |  |  |  |
| 18 | `QAACIN.DORM.RECORD.STATUS` | `QaacinDormantParam_RecordStatus` | String |  | Indicates the record status |
| 19 | `QAACIN.DORM.CURR.NO` | `QaacinDormantParam_CurrNo` | String |  | Indicates the number of time record is modified and saved |
| 20 | `QAACIN.DORM.INPUTTER` | `QaacinDormantParam_Inputter` |  |  |  |
| 21 | `QAACIN.DORM.DATE.TIME` | `QaacinDormantParam_DateTime` |  |  |  |
| 22 | `QAACIN.DORM.AUTHORISER` | `QaacinDormantParam_Authoriser` | String |  |  |
| 23 | `QAACIN.DORM.CO.CODE` | `QaacinDormantParam_CoCode` | String |  |  |
| 24 | `QAACIN.DORM.DEPT.CODE` | `QaacinDormantParam_DeptCode` | String |  |  |
| 25 | `QAACIN.DORM.AUDITOR.CODE` | `QaacinDormantParam_AuditorCode` | String |  |  |
| 26 | `QAACIN.DORM.AUDIT.DATE.TIME` | `QaacinDormantParam_AuditDateTime` | String |  |  |
