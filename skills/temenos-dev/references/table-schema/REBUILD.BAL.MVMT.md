# REBUILD.BAL.MVMT — Table Schema

> Source: `INSERTS/I_F.REBUILD.BAL.MVMT` in `MI_BalanceMovementBuild.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `BLD.BAL.DESCRIPTION` | `RebuildBalMvmt_Description` |  |  |  |
| 2 | `BLD.BAL.REBUILD.DATE` | `RebuildBalMvmt_RebuildDate` | TField |  | When the BALANCE.MOVEMENT file is required to be rebuilt then this field should hold the date from which the rebuild is to take place. This field is used in conjunction with the REBUILD.ACCOUNTS and REBUILD.CONTRACTS fields which calls the rebuild job and modifies the records on the BA.MVMT.BVAL file. Validation Rules: Standard T24 date field. |
| 3 | `BLD.BAL.REBUILD.ACCOUNTS` | `RebuildBalMvmt_RebuildAccounts` | TField | No | This field is used as part of the rebuild processing. If this field is set to Y then upon verification the calculation, population and the refinancing dates for ACCOUNTS only will be reset to the earliest movement, or if a rebuild date is present, the earliest movement after that rebuild.date. Performing this action will not run the calculation, population and refinancing rate extraction jobs, but those jobs may be included on the same REBUILD.BAL.MVMT record. Validation Rules: Input must be either Y or N. Optional Input. |
| 4 | `BLD.BAL.REBUILD.CONTRACTS` | `RebuildBalMvmt_RebuildContracts` | TField | No | This field is used as part of the rebuild processing. If this field is set to Y then upon verification the calculation, population and the refinancing dates for CONTRACTS only will be reset to the earliest movement, or if a rebuild date is present, the earliest movement after that rebuild.date. Performing this action will not run the calculation, population and refinancing rate extraction jobs, but those jobs may be included on the same REBUILD.BAL.MVMT record. Validation Rules: Input must be either Y or N. Optional Input. |
| 5 | `BLD.BAL.POPULATE.BAL.MVMT` | `RebuildBalMvmt_PopulateBalMvmt` | TField | No | This field is used to trigger the population job. When a record is verified with this field containing a 'Y' any movements which have occurred since the last population will be reflected on the BALANCE.MOVEMENT file. When this job has been run the field BACK.VAL.DATE on the BAL.MVMT.BVAL file will be set to null, indicating that the account or contract is up to date and does not need to be processed. Validation Rules: Input must be either Y or N. Optional Input. If left blank then this field defaults to N at run time. |
| 6 | `BLD.BAL.CALCULATE.AVG` | `RebuildBalMvmt_CalculateAvg` | TField | No | This field is used to trigger the calculation of average balances on the BALANCE.MOVMENT file. Once this job is completed for each account or contract the CALC.AVG.FROM field on the corresponding BAL.MVMT.BVAL record will be set to yesterdays date - indicating that the account or contract has had the average calculated on it up to and including that date. Validation Rules: Input must be Y or N. Optional Input. Null defualts to N. |
| 7 | `BLD.BAL.EXTRACT.REFIN.RATE` | `RebuildBalMvmt_ExtractRefinRate` | TField |  | This field is used to indicate whether or not the extraction of refinancing rates is required. If this flag is set to Y then the refinancing rates will be extracted according to the table set up on the MI.PARAMETER record. Validation Rules: Input must be Y or N. If this field is left blank then the refinance rate extraction job will ot be run. |
| 8 | `BLD.BAL.RESERVED.15` | `RebuildBalMvmt_Reserved15` | TField |  |  |
| 9 | `BLD.BAL.RESERVED.14` | `RebuildBalMvmt_Reserved14` | TField |  |  |
| 10 | `BLD.BAL.RESERVED.13` | `RebuildBalMvmt_Reserved13` | TField |  |  |
| 11 | `BLD.BAL.RESERVED.12` | `RebuildBalMvmt_Reserved12` | TField |  | This field is reserved for future use. |
| 12 | `BLD.BAL.RESERVED.11` | `RebuildBalMvmt_Reserved11` | TField |  | This field is reserved for future use. |
| 13 | `BLD.BAL.RESERVED.10` | `RebuildBalMvmt_Reserved10` | TField |  | This field is reserved for future use. |
| 14 | `BLD.BAL.RESERVED.9` | `RebuildBalMvmt_Reserved9` | TField |  | This field is reserved for future use. |
| 15 | `BLD.BAL.RESERVED.8` | `RebuildBalMvmt_Reserved8` | TField |  | This field is reserved for future use. |
| 16 | `BLD.BAL.RESERVED.7` | `RebuildBalMvmt_Reserved7` | TField |  | This field is reserved for future use. |
| 17 | `BLD.BAL.RESERVED.6` | `RebuildBalMvmt_Reserved6` | TField |  | This field is reserved for future use. |
| 18 | `BLD.BAL.RESERVED.5` | `RebuildBalMvmt_Reserved5` | TField |  | This field is reserved for future use. |
| 19 | `BLD.BAL.RESERVED.4` | `RebuildBalMvmt_Reserved4` | TField |  | This field is reserved for future use. |
| 20 | `BLD.BAL.RESERVED.3` | `RebuildBalMvmt_Reserved3` | TField |  | This field is reserved for future use. |
| 21 | `BLD.BAL.RESERVED.2` | `RebuildBalMvmt_Reserved2` | TField |  | This field is reserved for future use. |
| 22 | `BLD.BAL.RESERVED.1` | `RebuildBalMvmt_Reserved1` | TField |  | This field is reserved for future use. |
| 23 | `BLD.BAL.RECORD.STATUS` | `RebuildBalMvmt_RecordStatus` | String |  | Record status |
| 24 | `BLD.BAL.CURR.NO` | `RebuildBalMvmt_CurrNo` | String |  |  |
| 25 | `BLD.BAL.INPUTTER` | `RebuildBalMvmt_Inputter` |  |  |  |
| 26 | `BLD.BAL.DATE.TIME` | `RebuildBalMvmt_DateTime` |  |  |  |
| 27 | `BLD.BAL.AUTHORISER` | `RebuildBalMvmt_Authoriser` | String |  |  |
| 28 | `BLD.BAL.CO.CODE` | `RebuildBalMvmt_CoCode` | String |  |  |
| 29 | `BLD.BAL.DEPT.CODE` | `RebuildBalMvmt_DeptCode` | String |  |  |
| 30 | `BLD.BAL.AUDITOR.CODE` | `RebuildBalMvmt_AuditorCode` | String |  |  |
| 31 | `BLD.BAL.AUDIT.DATE.TIME` | `RebuildBalMvmt_AuditDateTime` | String |  |  |
