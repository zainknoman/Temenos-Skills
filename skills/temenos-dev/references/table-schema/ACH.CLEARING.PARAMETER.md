# ACH.CLEARING.PARAMETER — Table Schema

> Source: `INSERTS/I_F.ACH.CLEARING.PARAMETER` in `ACHFRM_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `ACH.PAR.DESCRIPTION` | `AchClearingParameter_Description` |  |  |  |
| 2 | `ACH.PAR.ROUTING.COMPANY` | `AchClearingParameter_RoutingCompany` |  |  |  |
| 3 | `ACH.PAR.OUR.RTN.NUMBER` | `AchClearingParameter_OurRtnNumber` |  |  |  |
| 4 | `ACH.PAR.EARLY.DEP.ACCT` | `AchClearingParameter_EarlyDepAcct` |  |  |  |
| 5 | `ACH.PAR.RESERVED.27` | `AchClearingParameter_Reserved27` |  |  |  |
| 6 | `ACH.PAR.RESERVED.26` | `AchClearingParameter_Reserved26` |  |  |  |
| 7 | `ACH.PAR.FED.RESERVE.NUMBER` | `AchClearingParameter_FedReserveNumber` | TField |  | 10 Positions - Federal reserve number. |
| 8 | `ACH.PAR.ACH.OPERATOR.RTN` | `AchClearingParameter_AchOperatorRtn` |  |  |  |
| 9 | `ACH.PAR.VALIDATION.TYPE` | `AchClearingParameter_ValidationType` | TField |  | Specifies Inward file validation criteria. FED - Validate FED file and skip CORP file CORPORATE - Validate CORP file and skip FED file ALL - Validate both FED and CORP file NONE - Skip FED and CORP file validation |
| 10 | `ACH.PAR.INWARD.FILE.PATH` | `AchClearingParameter_InwardFilePath` | TField |  | 65 Positions - Inward file path. |
| 11 | `ACH.PAR.OUTWARD.FILE.PATH` | `AchClearingParameter_OutwardFilePath` | TField |  | 65 Positions - Outward file path |
| 12 | `ACH.PAR.ARCHIVING.FILE.PATH` | `AchClearingParameter_ArchivingFilePath` | TField |  | 65 Positions - Archived file path. |
| 13 | `ACH.PAR.WORK.FILE.PATH` | `AchClearingParameter_WorkFilePath` | TField |  | 65 Positions - Work file path. |
| 14 | `ACH.PAR.ERROR.FILE.PATH` | `AchClearingParameter_ErrorFilePath` | TField |  | 65 Positions - Error file path. |
| 15 | `ACH.PAR.OUT.CLEARING.ACCT` | `AchClearingParameter_OutClearingAcct` | TField |  | 16 Positions - Clearing account for outgoing entries. |
| 16 | `ACH.PAR.RESERVED.25` | `AchClearingParameter_Reserved25` | TField |  | Reserved Field |
| 17 | `ACH.PAR.RESERVED.24` | `AchClearingParameter_Reserved24` | TField |  | Reserved Field |
| 18 | `ACH.PAR.RESERVED.23` | `AchClearingParameter_Reserved23` | TField |  | Reserved Field |
| 19 | `ACH.PAR.RESERVED.22` | `AchClearingParameter_Reserved22` | TField |  | Reserved Field |
| 20 | `ACH.PAR.RESERVED.21` | `AchClearingParameter_Reserved21` | TField |  | Reserved Field |
| 21 | `ACH.PAR.RETURN.DAYS` | `AchClearingParameter_ReturnDays` | TField |  | 3 Positions - Returns can be originated only within the number of days specified in this field. |
| 22 | `ACH.PAR.RETENTION.PERIOD` | `AchClearingParameter_RetentionPeriod` | TField |  | 3 Positions - Number of days that transactions are retained in history. Retention Period must be greater than Return Days. |
| 23 | `ACH.PAR.LEAD.DAYS.DR` | `AchClearingParameter_LeadDaysDr` | TField |  | 4 Positions - Number of ACH lead days for debit transactions. |
| 24 | `ACH.PAR.LEAD.DAYS.CR` | `AchClearingParameter_LeadDaysCr` | TField |  | 4 Positions - Number of ACH lead days for credit transactions. |
| 25 | `ACH.PAR.ACCOUNTING.PRODUCT` | `AchClearingParameter_AccountingProduct` | TField |  | 35 Positions - Decription of Product used to post accounting entries. |
| 26 | `ACH.PAR.POSTING.ORDER` | `AchClearingParameter_PostingOrder` | TField |  | Radio button - Options are: None, Post Entries By ID, Post Entries By Account |
| 27 | `ACH.PAR.PROCESSING.COMPANY` | `AchClearingParameter_ProcessingCompany` |  |  |  |
| 28 | `ACH.PAR.VALIDATION.LEVEL` | `AchClearingParameter_ValidationLevel` | TField |  | 1 Position - Pre-validation - This is the first level validation which happens before loading the file into the warehouse. During this process, all data acceptance criteria defined by ACH operators are performed. Validation levels will be: 1 - Any errors(File/Batch/Entry error) will result in file rejection 2 - Batch errors will result in file rejection 3 - Entry errors will result in Batch rejection Null - Default level. File errors will reject the file, batch error will reject the batch and entry/addenda errors will be ignored. |
| 29 | `ACH.PAR.SAMEDAY.CUTOFF.TIME` | `AchClearingParameter_SamedayCutoffTime` | TField |  | This field will hold the last distribution cutoff time when same day batches would be processed. Any files with same day batches sent to the FED after this cutoff time would be treated as next day settlement batches and the FED inserts the settlement date as the next Fed processing date. |
| 30 | `ACH.PAR.COMPANY.ID` | `AchClearingParameter_CompanyId` | TField |  | Originator ID for the bank for retail transactions. Maximum chars allowed is 10. Value should be formatted by right justified and filling zeros if length is less than 10. For example 0001234567 |
| 31 | `ACH.PAR.COMPANY.NAME` | `AchClearingParameter_CompanyName` | TField |  | This will be the company name of the bank for retail transactions. It will be used to update company name ACH.BATCH when initiating ACH from payment order and Direct Debit. |
| 32 | `ACH.PAR.ENTRY.THRESHOLD` | `AchClearingParameter_EntryThreshold` | TField |  | Defines the threshold amount for reporting in large dollar report. This threshold is checked for any ach entries originated by a corporate in an ACH batch. In case the amount is greater it would be flagged as a large dollar amount in ACH.ENTRIES table. |
| 33 | `ACH.PAR.SAMEDAY.LIMIT` | `AchClearingParameter_SamedayLimit` | TField | Yes | Captures the limit for same day transaction. This is a mandatory field. |
| 34 | `ACH.PAR.EARLY.DEP.DAYS` | `AchClearingParameter_EarlyDepDays` | TField |  | Field to Configure the business days for early deposit of ACH Credits. The value in this field would be subtracted from the settlement date to arrive at the posting date for the entry |
| 35 | `ACH.PAR.EARLY.DEP.SEC` | `AchClearingParameter_EarlyDepSec` |  |  |  |
| 36 | `ACH.PAR.ENTRY.ENRICH.API` | `AchClearingParameter_EntryEnrichApi` | TField |  | Routine attached could be either: A jBC implementation by using an EB.API record with a source type of BASIC. Please refer the ACH.ENTRY.ENRICH.BASIC.API routine in the Public Folder. For java implementations: An EB.API record id with a source type of HOOK which implements an interface defined in the EB.API record ACH.CLEARING.ENTRY.ENRICH.HOOK. This field supports the ClearingHouseHook.updateEntry() method. The Clearing Class is in the hook.countrymodelbank.usa package which is in ACHFRM_ClearingHouseHook.jar shipped with T24. |
| 37 | `ACH.PAR.RDFI.IMPOSED.VALIDATIONS` | `AchClearingParameter_RdfiImposedValidations` |  |  |  |
| 38 | `ACH.PAR.PRE.NOTE.AUTORETURN` | `AchClearingParameter_PreNoteAutoReturn` |  |  |  |
| 39 | `ACH.PAR.EARLY.REVERSAL` | `AchClearingParameter_EarlyReversal` | TField |  | Field to allow early reversal of an entry which was previously posted as an early deposit |
| 40 | `ACH.PAR.MAX.ROWS.PER.FILE` | `AchClearingParameter_MaxRowsPerFile` | TField |  | This field is referred by incoming warehouse upload batch process. Specify the maximum number of rows required in each split file. Depending on the volume of entries anticipated this field value can be adjusted to improve NACHA file upload process Validation rules: 3-5 Numeric value i.e. in range 100-99999 |
| 41 | `ACH.PAR.AUTO.RETURN` | `AchClearingParameter_AutoReturn` | TField |  | Field to capture if incoming payment exceptions are to be returned automatically on the settlement date |
| 42 | `ACH.PAR.APPLY.CORRECTIONS` | `AchClearingParameter_ApplyCorrections` | TField |  | Flag to indicate when a Notification of change(COR) is received, if recipient/payee information recorded in the system is to be corrected based on the NOC information. If chosen, the information recorded in BENEFICIARY, STANDING.ORDER, DD.DDI and DB.DEBIT.COLLECTION.ORDER will be corrected based on the NOC information received |
| 43 | `ACH.PAR.RESERVED.5` | `AchClearingParameter_Reserved5` | TField |  | Reserved Field |
| 44 | `ACH.PAR.RESERVED.4` | `AchClearingParameter_Reserved4` | TField |  | Reserved Field |
| 45 | `ACH.PAR.RESERVED.3` | `AchClearingParameter_Reserved3` | TField |  | Reserved Field |
| 46 | `ACH.PAR.RESERVED.2` | `AchClearingParameter_Reserved2` | TField |  | Reserved Field |
| 47 | `ACH.PAR.RESERVED.1` | `AchClearingParameter_Reserved1` | TField |  | Reserved Field |
| 48 | `ACH.PAR.LOCAL.REF` | `AchClearingParameter_LocalRef` |  |  |  |
| 49 | `ACH.PAR.OVERRIDE` | `AchClearingParameter_Override` |  |  |  |
| 50 | `ACH.PAR.RECORD.STATUS` | `AchClearingParameter_RecordStatus` | String |  |  |
| 51 | `ACH.PAR.CURR.NO` | `AchClearingParameter_CurrNo` | String |  |  |
| 52 | `ACH.PAR.INPUTTER` | `AchClearingParameter_Inputter` |  |  |  |
| 53 | `ACH.PAR.DATE.TIME` | `AchClearingParameter_DateTime` |  |  |  |
| 54 | `ACH.PAR.AUTHORISER` | `AchClearingParameter_Authoriser` | String |  |  |
| 55 | `ACH.PAR.CO.CODE` | `AchClearingParameter_CoCode` | String |  |  |
| 56 | `ACH.PAR.DEPT.CODE` | `AchClearingParameter_DeptCode` | String |  |  |
| 57 | `ACH.PAR.AUDITOR.CODE` | `AchClearingParameter_AuditorCode` | String |  |  |
| 58 | `ACH.PAR.AUDIT.DATE.TIME` | `AchClearingParameter_AuditDateTime` | String |  |  |
