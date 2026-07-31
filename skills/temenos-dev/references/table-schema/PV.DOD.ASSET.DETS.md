# PV.DOD.ASSET.DETS — Table Schema

> Source: `INSERTS/I_F.PV.DOD.ASSET.DETS` in `PV_DodRules.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PV.DOD.AST.OBLIGOR.ID` | `PvDodAssetDets_ObligorId` | TField |  | This system updated field holds the obligor id for which the asset belongs to. The ID of the obligor corresponds to either an individual obligor(customer id) or a joint obligor(System created id). The ID is a valid record from the OX.OBLIGOR.DETAILS table. |
| 2 | `PV.DOD.AST.OBLIGOR.CLASSIFICATION` | `PvDodAssetDets_ObligorClassification` | TField |  | This system updated field holds the classification of an obligor as in the field OBLIGOR.CLASSIFICATION in OX.OBLIGOR.DETAILS table. Possible values are Retail and Non-Retail. The Individuals and SMEs classified under Retail fall under the Retail classification, while the corporate and corporate SMEs fall under the non-retail classification. |
| 3 | `PV.DOD.AST.CURRENCY` | `PvDodAssetDets_Currency` | TField |  | This system updated field holds the valid Currency code corresponding to that of the Asset. |
| 4 | `PV.DOD.AST.EXPOSURE.AMT` | `PvDodAssetDets_ExposureAmt` | TField |  | This system updated field holds the outstanding amount of an asset corresponding to the record id, as on the Business end date. System refers to the parametric values defined in the field EXPOSUREEXLBALTYPE and PASTDUEEXLBALTYPE in PV.DOD.PARAMETER to calculate the outstanding amount or exposure amount. Amount is updated with respect to contract currency. |
| 5 | `PV.DOD.AST.PAST.DUE.AMT` | `PvDodAssetDets_PastDueAmt` | TField |  | This system updated field holds the past due amount of the asset, as on the Business end date. The value is updated by the system during the close of business as per the parameterisation defined in the field PASTDUEEXLBALTYPE in PV.DOD.PARAMETER. Amount is updated with respect to contract currency. |
| 6 | `PV.DOD.AST.DPD.COUNT` | `PvDodAssetDets_DpdCount` | TField |  | This system updated field stores the Days Past Due for the asset as per the record ID. Days Past Due refers to the number of calendar days the past dues are outstanding, when those amounts are material enough to breach the threshold limits. This field will be reset to Null when materiality threshold tests are not passed or when obligor becomes Inactive. |
| 7 | `PV.DOD.AST.DPD.DATE.LAST.UPD` | `PvDodAssetDets_DpdDateLastUpd` | TField |  | The system updated field stores the date on which the PAST.DUE.AMT and EXPOSURE.AMT is last updated by the system. Standard date format. |
| 8 | `PV.DOD.AST.EXP.DPD.DEFAULT.DATE` | `PvDodAssetDets_ExpDpdDefaultDate` | TField |  | This system updated field holds the date on which the asset is expected to enter the default status as per the DPD Count Days defined in PV.DOD.PARAMETER. Update to this field happens whenever the past due amount breaches the materiality threshold limits. The value in this field gets cleared whenever the past due amount does not breach the materiality threshold limits and the asset moves out of Default Status. This field value will be cleared, when the system reaches the date mentioned in this EXP.DPD.DEFAULT.DATE field. Standard date format(Calendar days). Example: The DPD count defined in PV.DOD.PARAMETER - 90 The Close of Business system date, on which materiality threshold is breached - January 1st, 2021 The expected default date (updated during the COB) - March 31st, 2021 |
| 9 | `PV.DOD.AST.DPD.DEFAULT.FLAG` | `PvDodAssetDets_DpdDefaultFlag` | TField |  | This field holds the value as YES, when the date in the EXP.DPD.DEFAULT.DATE field in PV.DOD.ASSET.DETS is reached. Possible values - Yes / Null. 'Yes' value refers to the status of the asset as Default. Null value refers to the status of the asset as Performing. This field value is cleared, when DPD.COUNT is reset to Null automatically by the system. Validation Rules: No changes allowed from Null to Yes by user during online. Can be manually changed from Yes to Null to clear all DPD related field except exposure and past due details. |
| 10 | `PV.DOD.AST.DPD.DEFAULT.DATE` | `PvDodAssetDets_DpdDefaultDate` | TField |  | This system updated field holds the date on which the DPD default flag was set to YES by the system or in other words the date on which the asset entered the default status. This field value is cleared, when DPD.COUNT is reset to Null automatically by the system. Standard date format. |
| 11 | `PV.DOD.AST.DPD.DEFAULT.CHG.REASON` | `PvDodAssetDets_DpdDefaultChgReason` | TField | Yes | This field holds the reason for the manual removal of the DPD default flag by the user. Mandatory input only when the DPD default flag is changed from Yes to Null manually. The reason can be selected by the user from the drop down list, as defined in the record PV.CHG.REASON in the EB.LOOKUP table. Additional reasons can be added to the corresponding EB.LOOKUP record. This field is cleared automatically by the system, when a DPD default flag is set afresh. |
| 12 | `PV.DOD.AST.PREV.DPD.DEFAULT.DATE` | `PvDodAssetDets_PrevDpdDefaultDate` |  |  |  |
| 13 | `PV.DOD.AST.RESERVED.10` | `PvDodAssetDets_Reserved10` | TField |  |  |
| 14 | `PV.DOD.AST.RESERVED.9` | `PvDodAssetDets_Reserved9` | TField |  |  |
| 15 | `PV.DOD.AST.RESERVED.8` | `PvDodAssetDets_Reserved8` | TField |  |  |
| 16 | `PV.DOD.AST.RESERVED.7` | `PvDodAssetDets_Reserved7` | TField |  |  |
| 17 | `PV.DOD.AST.RESERVED.6` | `PvDodAssetDets_Reserved6` | TField |  |  |
| 18 | `PV.DOD.AST.RESERVED.5` | `PvDodAssetDets_Reserved5` | TField |  |  |
| 19 | `PV.DOD.AST.RESERVED.4` | `PvDodAssetDets_Reserved4` | TField |  |  |
| 20 | `PV.DOD.AST.RESERVED.3` | `PvDodAssetDets_Reserved3` | TField |  |  |
| 21 | `PV.DOD.AST.RESERVED.2` | `PvDodAssetDets_Reserved2` | TField |  |  |
| 22 | `PV.DOD.AST.RESERVED.1` | `PvDodAssetDets_Reserved1` | TField |  |  |
| 23 | `PV.DOD.AST.OVERRIDE` | `PvDodAssetDets_Override` |  |  |  |
| 24 | `PV.DOD.AST.RECORD.STATUS` | `PvDodAssetDets_RecordStatus` | String |  |  |
| 25 | `PV.DOD.AST.CURR.NO` | `PvDodAssetDets_CurrNo` | String |  |  |
| 26 | `PV.DOD.AST.INPUTTER` | `PvDodAssetDets_Inputter` |  |  |  |
| 27 | `PV.DOD.AST.DATE.TIME` | `PvDodAssetDets_DateTime` |  |  |  |
| 28 | `PV.DOD.AST.AUTHORISER` | `PvDodAssetDets_Authoriser` | String |  |  |
| 29 | `PV.DOD.AST.CO.CODE` | `PvDodAssetDets_CoCode` | String |  |  |
| 30 | `PV.DOD.AST.DEPT.CODE` | `PvDodAssetDets_DeptCode` | String |  |  |
| 31 | `PV.DOD.AST.AUDITOR.CODE` | `PvDodAssetDets_AuditorCode` | String |  |  |
| 32 | `PV.DOD.AST.AUDIT.DATE.TIME` | `PvDodAssetDets_AuditDateTime` | String |  |  |
