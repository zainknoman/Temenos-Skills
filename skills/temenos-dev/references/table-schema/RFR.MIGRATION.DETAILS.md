# RFR.MIGRATION.DETAILS — Table Schema

> Source: `INSERTS/I_F.RFR.MIGRATION.DETAILS` in `ST_RateParameters.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `RFR.MGD.APPLICATION.NAME` | `RfrMigrationDetails_ApplicationName` | TField |  | Application or product used for migration. Example : LD.LOANS.AND.DEPOSITS, SAVINGS.ACCOUNT in case of AA Validation rule: Should be a valid application or a product in case of arrangement |
| 2 | `RFR.MGD.IBOR.CUTOFF.DATE` | `RfrMigrationDetails_IborCutoffDate` | TField |  | IBOR Discontinuation date Validation rule: Back value date is not possible |
| 3 | `RFR.MGD.VERSION.NAME` | `RfrMigrationDetails_VersionName` | TField |  | Valid version of application used for RFR migration process. Validation rule: Must be a valid version for the application |
| 4 | `RFR.MGD.MODE` | `RfrMigrationDetails_Mode` | TField |  | Define the type of migration Preview: Used for the verification process. Contract update does not take place Execute: Actual contract update is carried out Validation rule: Valid values: Preview OR Execute |
| 5 | `RFR.MGD.INT.PERIOD.END.DATE` | `RfrMigrationDetails_IntPeriodEndDate` | TField |  | Define Interest period end date Valid values: Valid date and blank Blank : Process all contracts (applicable only for Preview mode) |
| 6 | `RFR.MGD.CONTRACT.ID` | `RfrMigrationDetails_ContractId` |  |  |  |
| 7 | `RFR.MGD.CURRENCY` | `RfrMigrationDetails_Currency` |  |  |  |
| 8 | `RFR.MGD.CUSTOMER` | `RfrMigrationDetails_Customer` |  |  |  |
| 9 | `RFR.MGD.MATURITY.DATE` | `RfrMigrationDetails_MaturityDate` |  |  |  |
| 10 | `RFR.MGD.CUR.INT.PER.END.DAT` | `RfrMigrationDetails_CurIntPerEndDat` |  |  |  |
| 11 | `RFR.MGD.OLD.PI.KEY` | `RfrMigrationDetails_OldPiKey` |  |  |  |
| 12 | `RFR.MGD.NEW.PI.KEY` | `RfrMigrationDetails_NewPiKey` |  |  |  |
| 13 | `RFR.MGD.NEW.ADJ.SPREAD` | `RfrMigrationDetails_NewAdjSpread` |  |  |  |
| 14 | `RFR.MGD.EXCLUSION.FLAG` | `RfrMigrationDetails_ExclusionFlag` |  |  |  |
| 15 | `RFR.MGD.MIGRATION.STATUS` | `RfrMigrationDetails_MigrationStatus` |  |  |  |
| 16 | `RFR.MGD.RFR.INT.PROPERTY` | `RfrMigrationDetails_RfrIntProperty` |  |  |  |
