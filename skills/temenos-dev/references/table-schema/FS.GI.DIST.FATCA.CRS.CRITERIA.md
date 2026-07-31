# FS.GI.DIST.FATCA.CRS.CRITERIA — Table Schema

> Source: `INSERTS/I_F.FS.GI.DIST.FATCA.CRS.CRITERIA` in `FS_GlobalInvestor.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `FS.GI.DIST.FATCA.CRS.CRITERIA.PARENT.REF.ID` | `FsGiDistFatcaCrsCriteria_ParentRefId` | TField |  | Used for internal mapping purpose. |
| 2 | `FS.GI.DIST.FATCA.CRS.CRITERIA.ORA.ROWID` | `FsGiDistFatcaCrsCriteria_OraRowid` | TField |  | Used for internal mapping purpose. |
| 3 | `FS.GI.DIST.FATCA.CRS.CRITERIA.PARENT.ID.TYPE` | `FsGiDistFatcaCrsCriteria_ParentIdType` | TField |  | Type of Entity for which this instruction is held. Multifonds DB Column is TYPE_ID_CODE. |
| 4 | `FS.GI.DIST.FATCA.CRS.CRITERIA.PARENT.ID` | `FsGiDistFatcaCrsCriteria_ParentId` | TField |  | ID of the Entity for which this instruction is held. Multifonds DB Column is ID_CODE. |
| 5 | `FS.GI.DIST.FATCA.CRS.CRITERIA.CRITERIA` | `FsGiDistFatcaCrsCriteria_Criteria` | TField |  | The criteria code used to identify records linked to the FATCA or CRS logic. Multifonds DB Column is CRITERIA. |
| 6 | `FS.GI.DIST.FATCA.CRS.CRITERIA.FUND.PROMOTER.ID` | `FsGiDistFatcaCrsCriteria_FundPromoterId` | TField |  | Fund Promoter ID subjected to the FATCA or CRS set-up, depending on the corresponding criteria code. Multifonds DB Column is NPROMOTER. |
| 7 | `FS.GI.DIST.FATCA.CRS.CRITERIA.TFC.ID` | `FsGiDistFatcaCrsCriteria_TfcId` | TField | Yes | Legal Entity ID subjected to the FATCA or CRS set-up. The field is mandatory in case a new set-up is added. Multifonds DB Column is NTFC. |
| 8 | `FS.GI.DIST.FATCA.CRS.CRITERIA.SPONSORING.ENTITY.ID` | `FsGiDistFatcaCrsCriteria_SponsoringEntityId` | TField |  | Central Register Internal ID having &apos;Type&apos; as &apos;SE&apos;, can be specified as Sponsoring Entity External ID. Multifonds DB Column is SPONSOR. |
| 9 | `FS.GI.DIST.FATCA.CRS.CRITERIA.AML.JURISDICTION` | `FsGiDistFatcaCrsCriteria_AmlJurisdiction` | TField |  | FATCA/CRS applicable jurisdiction. Multifonds DB Column is JURISDICTION. |
| 10 | `FS.GI.DIST.FATCA.CRS.CRITERIA.TAX.RESIDENCE` | `FsGiDistFatcaCrsCriteria_TaxResidence` | TField |  | Tax residence code for which the FATCA or CRS set-ups are considered. Multifonds DB Column is CTAX_RESIDENCE. |
| 11 | `FS.GI.DIST.FATCA.CRS.CRITERIA.STATUS` | `FsGiDistFatcaCrsCriteria_Status` | TField |  | FATCA or CRS Status defined of the entity, depending on the criteria code. Multifonds DB Column is STATUS. |
| 12 | `FS.GI.DIST.FATCA.CRS.CRITERIA.SUB.STATUS` | `FsGiDistFatcaCrsCriteria_SubStatus` | TField |  | FATCA or CRS sub-status of the entity and is considerable as a specification of the corresponding status, depending on the criteria code. Multifonds DB Column is SUB_STATUS. |
| 13 | `FS.GI.DIST.FATCA.CRS.CRITERIA.THRESHOLD.STATUS` | `FsGiDistFatcaCrsCriteria_ThresholdStatus` | TField |  | FATCA or CRS sub-threshold status, depending on the criteria code. Multifonds DB Column is THRESHOLD_STATUS. |
| 14 | `FS.GI.DIST.FATCA.CRS.CRITERIA.DATE.OF.LAST.CALCULATION` | `FsGiDistFatcaCrsCriteria_DateOfLastCalculation` | TField |  | Date of last calculation. Multifonds DB Column is DLAST_BALC. |
| 15 | `FS.GI.DIST.FATCA.CRS.CRITERIA.LAST.REVIEW.DATE` | `FsGiDistFatcaCrsCriteria_LastReviewDate` | TField |  | The last review date (DD/MM/YYYY). The value must be unique for all FATCA/CRS set-ups. Multifonds DB Column is DLAST_REVIEW. |
| 16 | `FS.GI.DIST.FATCA.CRS.CRITERIA.NEXT.REVIEW.DATE` | `FsGiDistFatcaCrsCriteria_NextReviewDate` | TField |  | The next review date (DD/MM/YYYY). The value must be unique for all FATCA/CRS set-ups. Multifonds DB Column is DNEXT_REVIEW. |
| 17 | `FS.GI.DIST.FATCA.CRS.CRITERIA.SELF.CERTIFICATION` | `FsGiDistFatcaCrsCriteria_SelfCertification` | TField |  | It specifies the document is self certified.The field is for informative purpose. It is considered only for CRS set-up. Multifonds DB Column is SELF_CERT. |
| 18 | `FS.GI.DIST.FATCA.CRS.CRITERIA.PRE.EXISTING` | `FsGiDistFatcaCrsCriteria_PreExisting` | TField |  | It specifies if the document is pre existiong or not. Multifonds DB Column is PRE_EXIST. |
| 19 | `FS.GI.DIST.FATCA.CRS.CRITERIA.EXEMPTION.REASON` | `FsGiDistFatcaCrsCriteria_ExemptionReason` | TField |  | FATCA exempt reason code. Multifonds DB Column is EXMPT_REASON. |
| 20 | `FS.GI.DIST.FATCA.CRS.CRITERIA.REVOKE.END.DATE` | `FsGiDistFatcaCrsCriteria_RevokeEndDate` | TField |  | The revoke or End date (in DD/MM/YYYY format). Multifonds DB Column is DREVOKE. |
| 21 | `FS.GI.DIST.FATCA.CRS.CRITERIA.RULE.CODE` | `FsGiDistFatcaCrsCriteria_RuleCode` | TField |  | Rule Code. Multifonds DB Column is RULE_CODE. |
| 22 | `FS.GI.DIST.FATCA.CRS.CRITERIA.INTERNAL.ID` | `FsGiDistFatcaCrsCriteria_InternalId` | TField |  | Unique internal identifier for FATCA/CRS criteria record. Multifonds DB Column is INTERNAL_ID. |
| 23 | `FS.GI.DIST.FATCA.CRS.CRITERIA.RESERVED10` | `FsGiDistFatcaCrsCriteria_Reserved10` | TField |  |  |
| 24 | `FS.GI.DIST.FATCA.CRS.CRITERIA.RESERVED9` | `FsGiDistFatcaCrsCriteria_Reserved9` | TField |  |  |
| 25 | `FS.GI.DIST.FATCA.CRS.CRITERIA.RESERVED8` | `FsGiDistFatcaCrsCriteria_Reserved8` | TField |  |  |
| 26 | `FS.GI.DIST.FATCA.CRS.CRITERIA.RESERVED7` | `FsGiDistFatcaCrsCriteria_Reserved7` | TField |  |  |
| 27 | `FS.GI.DIST.FATCA.CRS.CRITERIA.RESERVED6` | `FsGiDistFatcaCrsCriteria_Reserved6` | TField |  |  |
| 28 | `FS.GI.DIST.FATCA.CRS.CRITERIA.RESERVED5` | `FsGiDistFatcaCrsCriteria_Reserved5` | TField |  |  |
| 29 | `FS.GI.DIST.FATCA.CRS.CRITERIA.RESERVED4` | `FsGiDistFatcaCrsCriteria_Reserved4` | TField |  |  |
| 30 | `FS.GI.DIST.FATCA.CRS.CRITERIA.RESERVED3` | `FsGiDistFatcaCrsCriteria_Reserved3` | TField |  |  |
| 31 | `FS.GI.DIST.FATCA.CRS.CRITERIA.RESERVED2` | `FsGiDistFatcaCrsCriteria_Reserved2` | TField |  |  |
| 32 | `FS.GI.DIST.FATCA.CRS.CRITERIA.RESERVED1` | `FsGiDistFatcaCrsCriteria_Reserved1` | TField |  |  |
| 33 | `FS.GI.DIST.FATCA.CRS.CRITERIA.LOCAL.REF` | `FsGiDistFatcaCrsCriteria_LocalRef` |  |  |  |
| 34 | `FS.GI.DIST.FATCA.CRS.CRITERIA.OVERRIDE` | `FsGiDistFatcaCrsCriteria_Override` |  |  |  |
| 35 | `FS.GI.DIST.FATCA.CRS.CRITERIA.RECORD.STATUS` | `FsGiDistFatcaCrsCriteria_RecordStatus` | String |  |  |
| 36 | `FS.GI.DIST.FATCA.CRS.CRITERIA.CURR.NO` | `FsGiDistFatcaCrsCriteria_CurrNo` | String |  |  |
| 37 | `FS.GI.DIST.FATCA.CRS.CRITERIA.INPUTTER` | `FsGiDistFatcaCrsCriteria_Inputter` |  |  |  |
| 38 | `FS.GI.DIST.FATCA.CRS.CRITERIA.DATE.TIME` | `FsGiDistFatcaCrsCriteria_DateTime` |  |  |  |
| 39 | `FS.GI.DIST.FATCA.CRS.CRITERIA.AUTHORISER` | `FsGiDistFatcaCrsCriteria_Authoriser` | String |  |  |
| 40 | `FS.GI.DIST.FATCA.CRS.CRITERIA.CO.CODE` | `FsGiDistFatcaCrsCriteria_CoCode` | String |  |  |
| 41 | `FS.GI.DIST.FATCA.CRS.CRITERIA.DEPT.CODE` | `FsGiDistFatcaCrsCriteria_DeptCode` | String |  |  |
| 42 | `FS.GI.DIST.FATCA.CRS.CRITERIA.AUDITOR.CODE` | `FsGiDistFatcaCrsCriteria_AuditorCode` | String |  |  |
| 43 | `FS.GI.DIST.FATCA.CRS.CRITERIA.AUDIT.DATE.TIME` | `FsGiDistFatcaCrsCriteria_AuditDateTime` | String |  |  |
