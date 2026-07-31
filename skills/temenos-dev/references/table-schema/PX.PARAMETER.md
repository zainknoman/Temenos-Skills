# PX.PARAMETER — Table Schema

> Source: `INSERTS/I_F.PX.PARAMETER` in `PX_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PXP.DEFAULT.AVAILABLE` | `PxParameter_DefaultAvailable` | TField |  | Field to indicate whether all types of accounts offered by the bank are AVAILABLE for PSD2 processing. If marked as YES, all categories of accounts and products under ACCOUNTS and MULTI.CCY.ACCOUNT offered by thebank are considered as eligible for PSD2 processing. If not, The bank must configure the eligible account types using the Category or AA Product field-sets. |
| 2 | `PXP.AVAIL.CATEG.START` | `PxParameter_AvailCategStart` |  |  |  |
| 3 | `PXP.AVAIL.CATEG.END` | `PxParameter_AvailCategEnd` |  |  |  |
| 4 | `PXP.AVAIL.RESERVED.10` | `PxParameter_AvailReserved10` |  |  |  |
| 5 | `PXP.AVAIL.RESERVED.09` | `PxParameter_AvailReserved09` |  |  |  |
| 6 | `PXP.AVAIL.RESERVED.08` | `PxParameter_AvailReserved08` |  |  |  |
| 7 | `PXP.AVAIL.RESERVED.07` | `PxParameter_AvailReserved07` |  |  |  |
| 8 | `PXP.AVAIL.RESERVED.06` | `PxParameter_AvailReserved06` |  |  |  |
| 9 | `PXP.AVAIL.RESERVED.05` | `PxParameter_AvailReserved05` |  |  |  |
| 10 | `PXP.AVAIL.RESERVED.04` | `PxParameter_AvailReserved04` |  |  |  |
| 11 | `PXP.AVAIL.RESERVED.03` | `PxParameter_AvailReserved03` |  |  |  |
| 12 | `PXP.AVAIL.RESERVED.02` | `PxParameter_AvailReserved02` |  |  |  |
| 13 | `PXP.AVAIL.RESERVED.01` | `PxParameter_AvailReserved01` |  |  |  |
| 14 | `PXP.AVAIL.CATEG` | `PxParameter_AvailCateg` |  |  |  |
| 15 | `PXP.CONSENT.MGMT` | `PxParameter_ConsentMgmt` | TField |  | NOINPUT. For future use should we decide to open up payment consent functionality later |
| 16 | `PXP.OBD.PROVIDER` | `PxParameter_ObdProvider` | TField |  | Field to indicate where TPP role validation occurs. Allowed value is EXTERNAL, means that the Open Banking Directory is maintained outside of Temenos Transact, say, maintained/validated at Open Banking Gateway, validation in Temenos Transact is not required. |
| 17 | `PXP.BLOCK.TPP` | `PxParameter_BlockTpp` |  |  |  |
| 18 | `PXP.AUTH.APPROACH` | `PxParameter_AuthApproach` | TField |  | This field is used to specify whether to use the implicit or explicit approach/workflow while creating the subresource and the content of the response in Payment initiation Validation Rule: Allowed values are IMPLICIT, EXPLICIT. Defaulted to IMPLICIT |
| 19 | `PXP.AVAIL.AA.PROD.MODE` | `PxParameter_AvailAaProdMode` | TField |  | This field used to define rule for avaialble AA product group and available AA product exception If specified as SPECIFIC then Defines that the list is an explicit list of products considered to be availablefor PSD2 which are not otherwise (implicitly) configured. If specified as DEFAULT then defines all products within the defined Product Group are included as available(apart from those defined as exceptions) If specified as NULL,definition via AA Product not defined. Validation Rule: It should take only three values SPECIFIC,DEFAULT and NULL |
| 19 | `PXP.CANC.AUTH.APPROACH` | `PxParameter_CancAuthApproach` | TField |  | This field is used to specify whether to use the implicit or explicit approach/workflow while creating the subresource and the content of the response in Payment cancellation Validation Rule: Allowed values are IMPLICIT, EXPLICIT. Defaulted to IMPLICIT |
| 20 | `PXP.AVAIL.AA.PROD.GRP` | `PxParameter_AvailAaProdGrp` |  |  |  |
| 21 | `PXP.AVAIL.AA.PROD.EXCPT` | `PxParameter_AvailAaProdExcpt` |  |  |  |
| 22 | `PXP.PERMISSIONS.CHECK` | `PxParameter_PermissionsCheck` | TField |  | Field to define where the user's channels permissions validations are managed. Allowed values are NULL and EXTERNAL. EXTERNAL - means the channels permissions are managed in an external system.The expectation is that an external system will check if a user has permission to perform a certain action. NULL - means the channels permissions are managed within Transact via EB.EXTERNAL.USER configurations. |
| 23 | `PXP.RETENTION.PERIOD` | `PxParameter_RetentionPeriod` | TField |  | Field to hold the time period for how long the unprocessed PSD2 payment requests are held in the system beforethey are deleted automatically. When a value is set in this field, the housekeeping service is activated and the unprocessed PSD2 payments arecleared when the service is run. Allowed values: The time period can be defined in minutes, hours, days, months and years The minimum value allowed in this field is 10 minutes (10mm) |
| 24 | `PXP.RESERVED.13` | `PxParameter_Reserved13` |  |  |  |
| 25 | `PXP.RESERVED.12` | `PxParameter_Reserved12` |  |  |  |
| 26 | `PXP.RESERVED.11` | `PxParameter_Reserved11` |  |  |  |
| 27 | `PXP.RESERVED.10` | `PxParameter_Reserved10` |  |  |  |
| 28 | `PXP.RESERVED.09` | `PxParameter_Reserved09` |  |  |  |
| 29 | `PXP.RESERVED.08` | `PxParameter_Reserved08` |  |  |  |
| 30 | `PXP.RESERVED.07` | `PxParameter_Reserved07` |  |  |  |
| 31 | `PXP.RESERVED.06` | `PxParameter_Reserved06` | TField |  |  |
| 32 | `PXP.RESERVED.05` | `PxParameter_Reserved05` | TField |  |  |
| 33 | `PXP.RESERVED.04` | `PxParameter_Reserved04` | TField |  |  |
| 34 | `PXP.RESERVED.03` | `PxParameter_Reserved03` | TField |  |  |
| 35 | `PXP.RESERVED.02` | `PxParameter_Reserved02` | TField |  |  |
| 36 | `PXP.RESERVED.01` | `PxParameter_Reserved01` | TField |  |  |
| 37 | `PXP.LOCAL.REF` | `PxParameter_LocalRef` |  |  |  |
| 38 | `PXP.OVERRIDE` | `PxParameter_Override` |  |  |  |
| 39 | `PXP.RECORD.STATUS` | `PxParameter_RecordStatus` | String |  |  |
| 40 | `PXP.CURR.NO` | `PxParameter_CurrNo` | String |  |  |
| 41 | `PXP.INPUTTER` | `PxParameter_Inputter` |  |  |  |
| 42 | `PXP.DATE.TIME` | `PxParameter_DateTime` |  |  |  |
| 43 | `PXP.AUTHORISER` | `PxParameter_Authoriser` | String |  |  |
| 44 | `PXP.CO.CODE` | `PxParameter_CoCode` | String |  |  |
| 45 | `PXP.DEPT.CODE` | `PxParameter_DeptCode` | String |  |  |
| 46 | `PXP.AUDITOR.CODE` | `PxParameter_AuditorCode` | String |  |  |
| 47 | `PXP.AUDIT.DATE.TIME` | `PxParameter_AuditDateTime` | String |  |  |
