# FS.GI.DIST.USTAX.OPTIONS — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.USTAX.OPTIONS` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.USTAX.OPTIONS.PARENT.REF.ID` | `FsGiDistUstaxOptions_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.USTAX.OPTIONS.ORA.ROWID` | `FsGiDistUstaxOptions_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.USTAX.OPTIONS.REGISTER.ID` | `FsGiDistUstaxOptions_RegisterId` | TField |  | Register internal ID Multifonds DB Column is NREGISTER. |
| 4 | `FS.GI.DIST.USTAX.OPTIONS.EXEMPT.REASON.CODE` | `FsGiDistUstaxOptions_ExemptReasonCode` | TField |  | US Tax exempt reason code. Multifonds DB Column is REASON_CODE. |
| 5 | `FS.GI.DIST.USTAX.OPTIONS.EXEMPT.STATUS.REVIEW.DATE` | `FsGiDistUstaxOptions_ExemptStatusReviewDate` | TField |  | US Tax exempt status review date (in DD/MM/YYYY format). Multifonds DB Column is REVIEW_DATE. |
| 6 | `FS.GI.DIST.USTAX.OPTIONS.US.TAX.ID` | `FsGiDistUstaxOptions_UsTaxId` | TField |  | US Tax Internal ID Multifonds DB Column is US_TAXID. |
| 7 | `FS.GI.DIST.USTAX.OPTIONS.W9.CERTIFICATION.FLAG` | `FsGiDistUstaxOptions_W9CertificationFlag` | TField |  | Flag indicates that w9 certification is active. Multifonds DB Column is W9_FLAG. |
| 8 | `FS.GI.DIST.USTAX.OPTIONS.W9.CERTIFICATION.DATE` | `FsGiDistUstaxOptions_W9CertificationDate` | TField | Yes | W9 certification date. The field is active and mandatory only when W-9 certification flag is set as &quot;Y&quot;. Multifonds DB Column is W9_DATE. |
| 9 | `FS.GI.DIST.USTAX.OPTIONS.W9.CERTIFICATION.TYPE` | `FsGiDistUstaxOptions_W9CertificationType` | TField | Yes | W9 certification type code. The field is active and is mandatory when &apos;W-9 certification flag&apos; check box is set as &quot;Y&quot;. Multifonds DB Column is W9_TYPE. |
| 10 | `FS.GI.DIST.USTAX.OPTIONS.BACK.UP.WITH.REASON.CODE` | `FsGiDistUstaxOptions_BackUpWithReasonCode` | TField |  | Backup with holding reason code. This field can be updated only when &apos;Exempt reason code&apos; is not specified. Multifonds DB Column is BACKUP_CODE. |
| 11 | `FS.GI.DIST.USTAX.OPTIONS.BACK.UP.WITHHOLDING.YEAR` | `FsGiDistUstaxOptions_BackUpWithholdingYear` | TField | Yes | Back up withholding year (in 4 digit). This field is active and mandatory when &apos;Back up withholding reason&apos; is specified. Multifonds DB Column is BACKUP_YEAR. |
| 12 | `FS.GI.DIST.USTAX.OPTIONS.RESERVED10` | `FsGiDistUstaxOptions_Reserved10` | TField |  |  |
| 13 | `FS.GI.DIST.USTAX.OPTIONS.RESERVED9` | `FsGiDistUstaxOptions_Reserved9` | TField |  |  |
| 14 | `FS.GI.DIST.USTAX.OPTIONS.RESERVED8` | `FsGiDistUstaxOptions_Reserved8` | TField |  |  |
| 15 | `FS.GI.DIST.USTAX.OPTIONS.RESERVED7` | `FsGiDistUstaxOptions_Reserved7` | TField |  |  |
| 16 | `FS.GI.DIST.USTAX.OPTIONS.RESERVED6` | `FsGiDistUstaxOptions_Reserved6` | TField |  |  |
| 17 | `FS.GI.DIST.USTAX.OPTIONS.RESERVED5` | `FsGiDistUstaxOptions_Reserved5` | TField |  |  |
| 18 | `FS.GI.DIST.USTAX.OPTIONS.RESERVED4` | `FsGiDistUstaxOptions_Reserved4` | TField |  |  |
| 19 | `FS.GI.DIST.USTAX.OPTIONS.RESERVED3` | `FsGiDistUstaxOptions_Reserved3` | TField |  |  |
| 20 | `FS.GI.DIST.USTAX.OPTIONS.RESERVED2` | `FsGiDistUstaxOptions_Reserved2` | TField |  |  |
| 21 | `FS.GI.DIST.USTAX.OPTIONS.RESERVED1` | `FsGiDistUstaxOptions_Reserved1` | TField |  |  |
| 22 | `FS.GI.DIST.USTAX.OPTIONS.LOCAL.REF` | `FsGiDistUstaxOptions_LocalRef` |  |  |  |
| 23 | `FS.GI.DIST.USTAX.OPTIONS.OVERRIDE` | `FsGiDistUstaxOptions_Override` |  |  |  |
| 24 | `FS.GI.DIST.USTAX.OPTIONS.RECORD.STATUS` | `FsGiDistUstaxOptions_RecordStatus` | String |  |  |
| 25 | `FS.GI.DIST.USTAX.OPTIONS.CURR.NO` | `FsGiDistUstaxOptions_CurrNo` | String |  |  |
| 26 | `FS.GI.DIST.USTAX.OPTIONS.INPUTTER` | `FsGiDistUstaxOptions_Inputter` |  |  |  |
| 27 | `FS.GI.DIST.USTAX.OPTIONS.DATE.TIME` | `FsGiDistUstaxOptions_DateTime` |  |  |  |
| 28 | `FS.GI.DIST.USTAX.OPTIONS.AUTHORISER` | `FsGiDistUstaxOptions_Authoriser` | String |  |  |
| 29 | `FS.GI.DIST.USTAX.OPTIONS.CO.CODE` | `FsGiDistUstaxOptions_CoCode` | String |  |  |
| 30 | `FS.GI.DIST.USTAX.OPTIONS.DEPT.CODE` | `FsGiDistUstaxOptions_DeptCode` | String |  |  |
| 31 | `FS.GI.DIST.USTAX.OPTIONS.AUDITOR.CODE` | `FsGiDistUstaxOptions_AuditorCode` | String |  |  |
| 32 | `FS.GI.DIST.USTAX.OPTIONS.AUDIT.DATE.TIME` | `FsGiDistUstaxOptions_AuditDateTime` | String |  |  |
