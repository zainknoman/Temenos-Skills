# COLLATERAL.POOL — Table Schema

> Source: `INSERTS/I_F.COLLATERAL.POOL` in `CO_Contract.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `COLL.POOL.DESCRIPTION` | `CollateralPool_Description` |  |  |  |
| 2 | `COLL.POOL.REFERENCE.CURRENCY` | `CollateralPool_ReferenceCurrency` | TField | No | Base currency used to convert the value of the Collaterals and Exposures to calculate Sufficiency Ratio. Also used for Reporting purpose. Validation Rules: Valid T24 Currency. Optional field. |
| 3 | `COLL.POOL.COLL.ACCOUNT.ID` | `CollateralPool_CollAccountId` |  |  |  |
| 4 | `COLL.POOL.EXPOSURE.COMPANY` | `CollateralPool_ExposureCompany` |  |  |  |
| 5 | `COLL.POOL.EXPOSURE.ID` | `CollateralPool_ExposureId` |  |  |  |
| 6 | `COLL.POOL.RISK.EXCLUSION.ID` | `CollateralPool_RiskExclusionId` |  |  |  |
| 7 | `COLL.POOL.EXPOSURE.LIMIT` | `CollateralPool_ExposureLimit` |  |  |  |
| 8 | `COLL.POOL.RESERVED19` | `CollateralPool_Reserved19` |  |  |  |
| 9 | `COLL.POOL.RESERVED18` | `CollateralPool_Reserved18` |  |  |  |
| 10 | `COLL.POOL.RESERVED17` | `CollateralPool_Reserved17` |  |  |  |
| 11 | `COLL.POOL.RESERVED16` | `CollateralPool_Reserved16` |  |  |  |
| 12 | `COLL.POOL.SUFFICIENCY.RATIO` | `CollateralPool_SufficiencyRatio` | TField |  | Ratio that indicates the sufficiency of the collateral to cover the given amount of Exposures. Validation Rules: System Maintained field. It will be calculated with the formula (Total Amount of Collaterals / Total Amount of Exposures). |
| 13 | `COLL.POOL.START.DATE` | `CollateralPool_StartDate` | TField | No | Date from which the Collateral Pool is effective. When not defined, system will default Today's Date. Validation Rules: Standard T24 Date format. Optional field. Can be back dated or forward dated as well. |
| 14 | `COLL.POOL.REVIEW.DATE.FREQ` | `CollateralPool_ReviewDateFreq` | TField | No | Date and frequency at which the collateral Pool should be reviewed. A combined date and frequency field which is automatically cycled by the system as part of the end-of-day process. Validation Rules: 17 type frequency format. Optional input Review Date cannot be less than Start Date. |
| 15 | `COLL.POOL.EXPIRY.DATE` | `CollateralPool_ExpiryDate` | TField | No | Represents the Expiry date of the Collateral Pool. The Status of the Collateral Pool becomes 'LIQ' when this date is reached. Validation Rules: Standard T24 Date format. Optional field. Cannot be less than Start Date. An override will be raised when the Expiry date of the Collateral Accounts pledged is beyond this Expiry date. |
| 16 | `COLL.POOL.ALLOCATION.OPTION` | `CollateralPool_AllocationOption` | TField |  | Allocation method in which the Exposures and Collaterals in the Collaterals Pools have to get allocated. Validation Rules: Valid Options are: ALLOCATION.PARAMETER - Allocation will be done based on the Asset Order defined in CO.ALLOCATION.PARAMETER table. STANDARD - Allocation will be done based on the ascending order of Collateral Codes. MANUAL - Allocation will be done in the order of the Collaterals defined in COLLATERAL.ACCOUNT and in the order of Collateral Accounts linked in Pool. NULL - When left as blank, allocation method defined in the field DEFAULT.POOL.ALLOCATION in COLLATERAL.PARAMETER will be followed. If DEFAULT.POOL.ALLOCATION field is also left blank, then by default STANDARD allocation will be followed. |
| 17 | `COLL.POOL.POOL.LEVEL.HAIRCUT` | `CollateralPool_PoolLevelHaircut` | TField |  | Defines the percentage by which the collateral execution value will be trimmed further at the Collateral Pool level. Validation Rules: Value should be in the range 1-100. |
| 18 | `COLL.POOL.POOL.RANKING` | `CollateralPool_PoolRanking` | TField | No | Ranking of the Collateral Pool Validation Rules: Optional field. |
| 19 | `COLL.POOL.STATUS` | `CollateralPool_Status` | TField |  | The status of the Collateral Pool determined based on the Start Date and Expiry Date of the Pool. The status of the collateral Pool is indicated in this field as follows: FWD - forward status; Start date is forward. CUR - current status; Expiry date is forward and Start Date is earlier or equal to today. LIQ - liquidated status; Expiry Date is past the today date. This field is automatically maintained by the system by an end-of-day process and is updated in accordance with any changes to the dates online. Validation Rules: Possible values are 'FWD', 'CUR', 'LIQ'. System maintained field. |
| 20 | `COLL.POOL.ALLOC.WORK.ID` | `CollateralPool_AllocWorkId` | TField |  | When Exposures and Collateral Accounts are linked to a Pool, allocation will take place between the Exposure and Collaterals and the allocation details will be updated in LIMIT.COL.ALLOC.WORK file. The Id to Limit Col Alloc Work file will be updated in this field. Validation Rules: System Maintained field. |
| 21 | `COLL.POOL.ONLINE.UPDATE` | `CollateralPool_OnlineUpdate` | TField |  | If security assets are pledged as Collateral and any change in value of assets will be updated in Collateral during end of the process. If the value of such collaterals attached as part of Collateral Pool has to be updated online, then this field has to be set as Yes in addition to the other setups required for Collateral Online Revaluation. For non-security assets pledged as Collateral which is attached as part of Collateral Pool, revaluation will take place either in COB or if Collateral is amended. Validation Rules: Yes or No Field. If this field is set as Yes, then revaluation of Collateral values will be updated online subject to other Online Revaluation setups. If this field is set as No/Null, then online revaluation of Collateral will not happen. |
| 22 | `COLL.POOL.RESERVED15` | `CollateralPool_Reserved15` | TField |  |  |
| 23 | `COLL.POOL.RESERVED14` | `CollateralPool_Reserved14` | TField |  |  |
| 24 | `COLL.POOL.RESERVED13` | `CollateralPool_Reserved13` | TField |  |  |
| 25 | `COLL.POOL.RESERVED12` | `CollateralPool_Reserved12` | TField |  |  |
| 26 | `COLL.POOL.RESERVED11` | `CollateralPool_Reserved11` | TField |  |  |
| 27 | `COLL.POOL.RESERVED10` | `CollateralPool_Reserved10` | TField |  |  |
| 28 | `COLL.POOL.RESERVED9` | `CollateralPool_Reserved9` | TField |  |  |
| 29 | `COLL.POOL.RESERVED8` | `CollateralPool_Reserved8` | TField |  |  |
| 30 | `COLL.POOL.RESERVED7` | `CollateralPool_Reserved7` | TField |  |  |
| 31 | `COLL.POOL.RESERVED6` | `CollateralPool_Reserved6` | TField |  |  |
| 32 | `COLL.POOL.RESERVED5` | `CollateralPool_Reserved5` | TField |  |  |
| 33 | `COLL.POOL.RESERVED4` | `CollateralPool_Reserved4` | TField |  |  |
| 34 | `COLL.POOL.RESERVED3` | `CollateralPool_Reserved3` | TField |  |  |
| 35 | `COLL.POOL.RESERVED2` | `CollateralPool_Reserved2` | TField |  |  |
| 36 | `COLL.POOL.RESERVED1` | `CollateralPool_Reserved1` | TField |  |  |
| 37 | `COLL.POOL.LOCAL.REF` | `CollateralPool_LocalRef` |  |  |  |
| 38 | `COLL.POOL.OVERRIDE` | `CollateralPool_Override` |  |  |  |
| 39 | `COLL.POOL.RECORD.STATUS` | `CollateralPool_RecordStatus` | String |  |  |
| 40 | `COLL.POOL.CURR.NO` | `CollateralPool_CurrNo` | String |  |  |
| 41 | `COLL.POOL.INPUTTER` | `CollateralPool_Inputter` |  |  |  |
| 42 | `COLL.POOL.DATE.TIME` | `CollateralPool_DateTime` |  |  |  |
| 43 | `COLL.POOL.AUTHORISER` | `CollateralPool_Authoriser` | String |  |  |
| 44 | `COLL.POOL.CO.CODE` | `CollateralPool_CoCode` | String |  |  |
| 45 | `COLL.POOL.DEPT.CODE` | `CollateralPool_DeptCode` | String |  |  |
| 46 | `COLL.POOL.AUDITOR.CODE` | `CollateralPool_AuditorCode` | String |  |  |
| 47 | `COLL.POOL.AUDIT.DATE.TIME` | `CollateralPool_AuditDateTime` | String |  |  |
