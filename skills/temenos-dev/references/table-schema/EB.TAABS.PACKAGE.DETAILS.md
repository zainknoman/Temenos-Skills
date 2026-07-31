# EB.TAABS.PACKAGE.DETAILS — Table Schema

> Source: `INSERTS/I_F.EB.TAABS.PACKAGE.DETAILS` in `EB_ProductConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.TPDT.DESCRIPTION` | `EbTaabsPackageDetails_Description` |  |  |  |
| 2 | `EB.TPDT.DETAIL.INFO` | `EbTaabsPackageDetails_DetailInfo` |  |  |  |
| 3 | `EB.TPDT.USERS` | `EbTaabsPackageDetails_Users` |  |  |  |
| 4 | `EB.TPDT.ROLES` | `EbTaabsPackageDetails_Roles` |  |  |  |
| 5 | `EB.TPDT.NO.OF.RECORDS` | `EbTaabsPackageDetails_NoOfRecords` | TField |  | This field indicates the total number of events captured under this package. The details of the events will be available in EB.TAABS.PACKAGE records |
| 6 | `EB.TPDT.NO.OF.EXCLUSIONS` | `EbTaabsPackageDetails_NoOfExclusions` | TField |  | This field indicates the total number of transactions that has been marked for exclusion. The transactions marked for exclusion will not be released to the target environment. |
| 7 | `EB.TPDT.AUDIT.SHORT.NOTE` | `EbTaabsPackageDetails_AuditShortNote` | TField |  | Noinput field that stores the list of last 10 packages that were associated with this USER or EB.USER.ROLES record. |
| 8 | `EB.TPDT.AUDIT.NOTES.DETAIL` | `EbTaabsPackageDetails_AuditNotesDetail` | TField |  | This field is used to record the detailed information during the Audit and SignOff process for this package. |
| 9 | `EB.TPDT.AUDITED` | `EbTaabsPackageDetails_Audited` | TField |  | Specifies whether this package has been Audited and SignedOff or not. If the field is set to 'Yes' then it means it has been Audited and SignedOff |
| 10 | `EB.TPDT.RESERVED.5` | `EbTaabsPackageDetails_Reserved5` | TField |  |  |
| 11 | `EB.TPDT.RESERVED.4` | `EbTaabsPackageDetails_Reserved4` | TField |  |  |
| 12 | `EB.TPDT.RESERVED.3` | `EbTaabsPackageDetails_Reserved3` | TField |  |  |
| 13 | `EB.TPDT.RESERVED.2` | `EbTaabsPackageDetails_Reserved2` | TField |  |  |
| 14 | `EB.TPDT.RESERVED.1` | `EbTaabsPackageDetails_Reserved1` | TField |  |  |
| 15 | `EB.TPDT.RECORD.STATUS` | `EbTaabsPackageDetails_RecordStatus` | String |  |  |
| 16 | `EB.TPDT.CURR.NO` | `EbTaabsPackageDetails_CurrNo` | String |  |  |
| 17 | `EB.TPDT.INPUTTER` | `EbTaabsPackageDetails_Inputter` |  |  |  |
| 18 | `EB.TPDT.DATE.TIME` | `EbTaabsPackageDetails_DateTime` |  |  |  |
| 19 | `EB.TPDT.AUTHORISER` | `EbTaabsPackageDetails_Authoriser` | String |  |  |
| 20 | `EB.TPDT.CO.CODE` | `EbTaabsPackageDetails_CoCode` | String |  |  |
| 21 | `EB.TPDT.DEPT.CODE` | `EbTaabsPackageDetails_DeptCode` | String |  |  |
| 22 | `EB.TPDT.AUDITOR.CODE` | `EbTaabsPackageDetails_AuditorCode` | String |  |  |
| 23 | `EB.TPDT.AUDIT.DATE.TIME` | `EbTaabsPackageDetails_AuditDateTime` | String |  |  |
