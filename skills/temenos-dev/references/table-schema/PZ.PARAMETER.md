# PZ.PARAMETER — Table Schema

> Source: `INSERTS/I_F.PZ.PARAMETER` in `PZ_Config.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `PZP.DEFAULT.AVAILABLE` | `PzParameter_DefaultAvailable` | TField |  | Field to indicate whether all types of accounts offered by the bank are AVAILABLE for PSD2 processing. If markedas YES, all categories of accounts and products under ACCOUNTS and MULTI.CCY.ACCOUNT offered by the bank areconsidered as eligible for PSD2 processing. If not, the bank must configure the eligible account types using theCategory or AA Product field-sets. |
| 2 | `PZP.AVAIL.CATEG.START` | `PzParameter_AvailCategStart` |  |  |  |
| 3 | `PZP.AVAIL.CATEG.END` | `PzParameter_AvailCategEnd` |  |  |  |
| 4 | `PZP.AVAIL.RESERVED.10` | `PzParameter_AvailReserved10` |  |  |  |
| 5 | `PZP.AVAIL.RESERVED.09` | `PzParameter_AvailReserved09` |  |  |  |
| 6 | `PZP.AVAIL.RESERVED.08` | `PzParameter_AvailReserved08` |  |  |  |
| 7 | `PZP.AVAIL.RESERVED.07` | `PzParameter_AvailReserved07` |  |  |  |
| 8 | `PZP.AVAIL.RESERVED.06` | `PzParameter_AvailReserved06` |  |  |  |
| 9 | `PZP.AVAIL.RESERVED.05` | `PzParameter_AvailReserved05` |  |  |  |
| 10 | `PZP.AVAIL.RESERVED.04` | `PzParameter_AvailReserved04` |  |  |  |
| 11 | `PZP.AVAIL.RESERVED.03` | `PzParameter_AvailReserved03` |  |  |  |
| 12 | `PZP.AVAIL.RESERVED.02` | `PzParameter_AvailReserved02` |  |  |  |
| 13 | `PZP.AVAIL.RESERVED.01` | `PzParameter_AvailReserved01` |  |  |  |
| 14 | `PZP.AVAIL.CATEG` | `PzParameter_AvailCateg` |  |  |  |
| 15 | `PZP.CONSENT.MGMT` | `PzParameter_ConsentMgmt` | TField |  | Field to specify if the consent management id done via t24 or not. If specified as INTERNAL then consent managed via t24 If specified as EXTERNAL then consent managed is outsourced Validation Rule: It should either take two values INTERNAL or EXTERNAL For INTERNAL consent managemement validations required for all AIS APIs |
| 16 | `PZP.OBD.PROVIDER` | `PzParameter_ObdProvider` | TField |  | Field to indicate where TPP role validation occurs. Allowed value is EXTERNAL, means that the Open Banking Directory is maintained outside of Temenos Transact, say, maintained/validated at Open Banking Gateway, validation in Temenos Transact is not required. |
| 17 | `PZP.BLOCK.TPP` | `PzParameter_BlockTpp` |  |  |  |
| 18 | `PZP.CONSENT.LEVEL` | `PzParameter_ConsentLevel` | TField |  | Field to specify whether the bank is operating a GLOBAL or COMPANY level consent GLOBAL means the consent arrangement can contain accounts from multiple companies that share the same customers COMPANY means the consent arrangement will hold only accounts from the lead company Validation Rule: It should either take two values GLOBAL or COMPANY |
| 19 | `PZP.AVAIL.AA.PROD.MODE` | `PzParameter_AvailAaProdMode` | TField |  | This field used to define rule for avaialble AA product group and available AA product exception If specified as SPECIFIC then Defines that the list is an explicit list of products considered to be availablefor PSD2 which are not otherwise (implicitly) configured. If specified as DEFAULT then defines all products within the defined Product Group are included as available(apart from those defined as exceptions) If specified as NULL,definition via AA Product not defined. Validation Rule: It should take only three values SPECIFIC,DEFAULT and NULL |
| 20 | `PZP.AVAIL.AA.PROD.GRP` | `PzParameter_AvailAaProdGrp` |  |  |  |
| 21 | `PZP.AVAIL.AA.PROD.EXCPT` | `PzParameter_AvailAaProdExcpt` |  |  |  |
| 22 | `PZP.PERMISSIONS.CHECK` | `PzParameter_PermissionsCheck` | TField |  | Field to define where the user's channels permissions validations are managed. Validation Rule: Allowed values are NULL and EXTERNAL. EXTERNAL - means the channels permissions are managed in an external system. The expectation is that an external system will check if a user has permission to perform a certain action. NULL - means the channels permissions are managed within Transact via EB.EXTERNAL.USER configurations. |
| 23 | `PZP.RETENTION.PERIOD` | `PzParameter_RetentionPeriod` | TField |  | Defines the period after which orphaned PSD2 records(that are still in exception) will be deleted. Field to hold the time period for how long the unprocessed PSD2 consent requests are held in the system beforethey are deleted automatically. When a value is set in this field, the housekeeping service is activated and the unprocessed consents are clearedwhen the service is run. Validation Rules: Allowed values - The time period can be defined in minutes(XMM), hours(XHH), days(XD), months(XM) and years(XY). The minimum value allowed in this field is 10 minutes (10mm). |
| 24 | `PZP.LOCAL.REF` | `PzParameter_LocalRef` |  |  |  |
| 25 | `PZP.OVERRIDE` | `PzParameter_Override` |  |  |  |
| 26 | `PZP.RECORD.STATUS` | `PzParameter_RecordStatus` | String |  |  |
| 27 | `PZP.CURR.NO` | `PzParameter_CurrNo` | String |  |  |
| 28 | `PZP.INPUTTER` | `PzParameter_Inputter` |  |  |  |
| 29 | `PZP.DATE.TIME` | `PzParameter_DateTime` |  |  |  |
| 30 | `PZP.AUTHORISER` | `PzParameter_Authoriser` | String |  |  |
| 31 | `PZP.CO.CODE` | `PzParameter_CoCode` | String |  |  |
| 32 | `PZP.DEPT.CODE` | `PzParameter_DeptCode` | String |  |  |
| 33 | `PZP.AUDITOR.CODE` | `PzParameter_AuditorCode` | String |  |  |
| 34 | `PZP.AUDIT.DATE.TIME` | `PzParameter_AuditDateTime` | String |  |  |
| 35 | `PZP.TOKENISE.ACCOUNT.ID` | `PzParameter_TokeniseAccountId` | TField |  | Field to allow the bank to generate random account ID for each populated account within the Account ConsentArrangement. If set to Yes, a unique ID will be populated for each account in the Account Consent Arrangement. The unique reference is used by the TPP to address the account in the AIS endpoints. Validation Rules: Allowed values are: Null - Tokenised values are not generated for the accounts within the consent. No - Tokenised values are not generated for the accounts within the consent. Yes - Tokenised values are generatedfor the accounts within the consent. Validation - When set to Yes, this value cannot be changed back to No or Null. |
