# FS.GI.DIST.AML.COMPLIANCE — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.AML.COMPLIANCE` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.AML.COMPLIANCE.PARENT.REF.ID` | `FsGiDistAmlCompliance_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.AML.COMPLIANCE.ORA.ROWID` | `FsGiDistAmlCompliance_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.AML.COMPLIANCE.PARENT.ID.TYPE` | `FsGiDistAmlCompliance_ParentIdType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.DIST.AML.COMPLIANCE.PARENT.ID` | `FsGiDistAmlCompliance_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.DIST.AML.COMPLIANCE.INITIAL.COMPLIANT.DATE` | `FsGiDistAmlCompliance_InitialCompliantDate` | TField |  | Initial Compliant Date. Multifonds DB Column is INITIAL_COMPLIANT_DATE. |
| 6 | `FS.GI.DIST.AML.COMPLIANCE.LAST.REVIEW.DATE` | `FsGiDistAmlCompliance_LastReviewDate` | TField |  | Last AML review date. Multifonds DB Column is LAST_REVIEW_DATE. |
| 7 | `FS.GI.DIST.AML.COMPLIANCE.NEXT.REVIEW.DATE` | `FsGiDistAmlCompliance_NextReviewDate` | TField |  | Next AML Review date. Multifonds DB Column is NEXT_REVIEW_DATE. |
| 8 | `FS.GI.DIST.AML.COMPLIANCE.RESERVED10` | `FsGiDistAmlCompliance_Reserved10` | TField |  |  |
| 9 | `FS.GI.DIST.AML.COMPLIANCE.RESERVED9` | `FsGiDistAmlCompliance_Reserved9` | TField |  |  |
| 10 | `FS.GI.DIST.AML.COMPLIANCE.RESERVED8` | `FsGiDistAmlCompliance_Reserved8` | TField |  |  |
| 11 | `FS.GI.DIST.AML.COMPLIANCE.RESERVED7` | `FsGiDistAmlCompliance_Reserved7` | TField |  |  |
| 12 | `FS.GI.DIST.AML.COMPLIANCE.RESERVED6` | `FsGiDistAmlCompliance_Reserved6` | TField |  |  |
| 13 | `FS.GI.DIST.AML.COMPLIANCE.RESERVED5` | `FsGiDistAmlCompliance_Reserved5` | TField |  |  |
| 14 | `FS.GI.DIST.AML.COMPLIANCE.RESERVED4` | `FsGiDistAmlCompliance_Reserved4` | TField |  |  |
| 15 | `FS.GI.DIST.AML.COMPLIANCE.RESERVED3` | `FsGiDistAmlCompliance_Reserved3` | TField |  |  |
| 16 | `FS.GI.DIST.AML.COMPLIANCE.RESERVED2` | `FsGiDistAmlCompliance_Reserved2` | TField |  |  |
| 17 | `FS.GI.DIST.AML.COMPLIANCE.RESERVED1` | `FsGiDistAmlCompliance_Reserved1` | TField |  |  |
| 18 | `FS.GI.DIST.AML.COMPLIANCE.LOCAL.REF` | `FsGiDistAmlCompliance_LocalRef` |  |  |  |
| 19 | `FS.GI.DIST.AML.COMPLIANCE.OVERRIDE` | `FsGiDistAmlCompliance_Override` |  |  |  |
| 20 | `FS.GI.DIST.AML.COMPLIANCE.RECORD.STATUS` | `FsGiDistAmlCompliance_RecordStatus` | String |  |  |
| 21 | `FS.GI.DIST.AML.COMPLIANCE.CURR.NO` | `FsGiDistAmlCompliance_CurrNo` | String |  |  |
| 22 | `FS.GI.DIST.AML.COMPLIANCE.INPUTTER` | `FsGiDistAmlCompliance_Inputter` |  |  |  |
| 23 | `FS.GI.DIST.AML.COMPLIANCE.DATE.TIME` | `FsGiDistAmlCompliance_DateTime` |  |  |  |
| 24 | `FS.GI.DIST.AML.COMPLIANCE.AUTHORISER` | `FsGiDistAmlCompliance_Authoriser` | String |  |  |
| 25 | `FS.GI.DIST.AML.COMPLIANCE.CO.CODE` | `FsGiDistAmlCompliance_CoCode` | String |  |  |
| 26 | `FS.GI.DIST.AML.COMPLIANCE.DEPT.CODE` | `FsGiDistAmlCompliance_DeptCode` | String |  |  |
| 27 | `FS.GI.DIST.AML.COMPLIANCE.AUDITOR.CODE` | `FsGiDistAmlCompliance_AuditorCode` | String |  |  |
| 28 | `FS.GI.DIST.AML.COMPLIANCE.AUDIT.DATE.TIME` | `FsGiDistAmlCompliance_AuditDateTime` | String |  |  |
