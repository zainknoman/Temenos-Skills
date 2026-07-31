# EB.TAABS.USER.PACKAGES — Table Schema

> Source: `INSERTS/I_F.EB.TAABS.USER.PACKAGES` in `EB_ProductConfig.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `EB.TPUP.PACKAGE.NAME` | `EbTaabsUserPackages_PackageName` | TField |  | This field contains reference to EB.TAABS.PACKAGE.DETAILS application. It indicates the packages that are associated with this USER or EB.USER.ROLES record. |
| 2 | `EB.TPUP.PACKAGE.HISTORY` | `EbTaabsUserPackages_PackageHistory` |  |  |  |
| 3 | `EB.TPUP.RESERVED.5` | `EbTaabsUserPackages_Reserved5` | TField |  |  |
| 4 | `EB.TPUP.RESERVED.4` | `EbTaabsUserPackages_Reserved4` | TField |  |  |
| 5 | `EB.TPUP.RESERVED.3` | `EbTaabsUserPackages_Reserved3` | TField |  |  |
| 6 | `EB.TPUP.RESERVED.2` | `EbTaabsUserPackages_Reserved2` | TField |  |  |
| 7 | `EB.TPUP.RESERVED.1` | `EbTaabsUserPackages_Reserved1` | TField |  |  |
| 8 | `EB.TPUP.RECORD.STATUS` | `EbTaabsUserPackages_RecordStatus` | String |  |  |
| 9 | `EB.TPUP.CURR.NO` | `EbTaabsUserPackages_CurrNo` | String |  |  |
| 10 | `EB.TPUP.INPUTTER` | `EbTaabsUserPackages_Inputter` |  |  |  |
| 11 | `EB.TPUP.DATE.TIME` | `EbTaabsUserPackages_DateTime` |  |  |  |
| 12 | `EB.TPUP.AUTHORISER` | `EbTaabsUserPackages_Authoriser` | String |  |  |
| 13 | `EB.TPUP.CO.CODE` | `EbTaabsUserPackages_CoCode` | String |  |  |
| 14 | `EB.TPUP.DEPT.CODE` | `EbTaabsUserPackages_DeptCode` | String |  |  |
| 15 | `EB.TPUP.AUDITOR.CODE` | `EbTaabsUserPackages_AuditorCode` | String |  |  |
| 16 | `EB.TPUP.AUDIT.DATE.TIME` | `EbTaabsUserPackages_AuditDateTime` | String |  |  |
