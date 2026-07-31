# SASIMA.PARAMETER — Table Schema

> Source: `INSERTS/I_F.SASIMA.PARAMETER` in `SASIMA_Foundation.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AH.SP.MEMBER.ID` | `SasimaParameter_MemberId` | TField |  | Member's ID number with SIMAH. |
| 2 | `AH.SP.MEMBER.USER` | `SasimaParameter_MemberUser` | TField |  | Member's user ID with SIMAH |
| 3 | `AH.SP.MAX.REPORTING.DAYS.REGULAR` | `SasimaParameter_MaxReportingDaysRegular` | TField |  | Specifies the salary code for reporting to SIMAH. |
| 4 | `AH.SP.MAX.REPORTING.DAYS.COMMERCIAL` | `SasimaParameter_MaxReportingDaysCommercial` | TField |  | Specifies the salary code for reporting to SIMAH. |
| 5 | `AH.SP.COLLATERAL.CODE.SALARY` | `SasimaParameter_CollateralCodeSalary` | TField |  | Specifies the salary code for reporting to SIMAH. |
| 6 | `AH.SP.RETAIL.SECTOR` | `SasimaParameter_RetailSector` |  |  |  |
| 7 | `AH.SP.COMMERCIAL.SECTOR` | `SasimaParameter_CommercialSector` |  |  |  |
| 8 | `AH.SP.ALT.ACCT.TYPE` | `SasimaParameter_AltAcctType` | TField |  | This field is used to define the Alternate account type based on which the account number has to be fetched for the migrated accounts |
| 9 | `AH.SP.LANG.CODE.ENGLISH` | `SasimaParameter_LangCodeEnglish` | TField |  | This field is used to store the position from which the values for English has to be fetched for language specific fields |
| 10 | `AH.SP.LANG.CODE.ARABIC` | `SasimaParameter_LangCodeArabic` | TField |  | This field is used to store the position from which the values for Arabic has to be fetched for language specific fields |
| 11 | `AH.SP.RESPONSE.MSG.TAG` | `SasimaParameter_ResponseMsgTag` | TField |  | Naming convention of the response message tag. |
| 12 | `AH.SP.RESPONSE.RPT.TAG` | `SasimaParameter_ResponseRptTag` | TField |  | Naming convention of the report message tag |
| 13 | `AH.SP.MONTHLY.SALARY.MAX` | `SasimaParameter_MonthlySalaryMax` | TField |  | This field is used to store the Maximum monthly Basic Salary |
| 14 | `AH.SP.TOTAL.MONTHLY.SALARY.MAX` | `SasimaParameter_TotalMonthlySalaryMax` | TField |  | This field is used to store the Total of maximum monthly Basic Salary |
| 15 | `AH.SP.MONTHLY.SALARY.MIN` | `SasimaParameter_MonthlySalaryMin` | TField |  | This field is used to store the Minimum Monthly basic salary |
| 16 | `AH.SP.TOTAL.MONTHLY.SALARY.MIN` | `SasimaParameter_TotalMonthlySalaryMin` | TField |  | This field is used to store the Total of Minimum monthly Basic Salary |
| 17 | `AH.SP.MAXIMUM.ALLOWANCE` | `SasimaParameter_MaximumAllowance` | TField |  | Verifies against the total monthly max salary and triggers an error if greater. |
| 18 | `AH.SP.NO.OF.DAYS` | `SasimaParameter_NoOfDays` | TField |  | Specifies the days based on which override message will be generated for SIMAH webservice. |
| 19 | `AH.SP.EXCEMPTION.CONTRIES` | `SasimaParameter_ExcemptionContries` |  |  |  |
| 20 | `AH.SP.EXCEMPTION.LEGAL.DOC.TYPE` | `SasimaParameter_ExcemptionLegalDocType` |  |  |  |
| 21 | `AH.SP.AGE.MINIMUM` | `SasimaParameter_AgeMinimum` | TField |  | Help Text for this field is unavailable. Please refer to the T24 User Guides for further information. |
| 22 | `AH.SP.PROFIT.PROPERTY` | `SasimaParameter_ProfitProperty` | TField |  | This field is used to define the age restriction for selecting the file for file extraction |
| 23 | `AH.SP.COMMERCIAL.CONTACT.HEADER` | `SasimaParameter_CommercialContactHeader` | TField |  | This field is used to define the age restriction for selecting the file for file extraction |
| 24 | `AH.SP.LOCAL.REF` | `SasimaParameter_LocalRef` |  |  |  |
| 25 | `AH.SP.OVERRIDE` | `SasimaParameter_Override` |  |  |  |
| 26 | `AH.SP.PRODUCT` | `SasimaParameter_Product` |  |  |  |
| 27 | `AH.SP.CLOSE.STATUS` | `SasimaParameter_CloseStatus` |  |  |  |
| 28 | `AH.SP.CYCLE.DAYS` | `SasimaParameter_CycleDays` | TField |  | ACYCID TAG Value arrived from this field. |
| 29 | `AH.SP.BULK.NO.IN.SIMAH` | `SasimaParameter_BulkNoInSimah` | TField |  | This field is used to define the maximum number of contracts to be written to a consolidated SASIMA file. If it is exceeded, contents will be written to next file. It must be a multiple of 10000. |
| 30 | `AH.SP.FEATURE.FLAG` | `SasimaParameter_FeatureFlag` | TField |  | To Enable the SIMAH New Features |
| 31 | `AH.SP.REGENERATE.DAYS` | `SasimaParameter_RegenerationDays` |  |  |  |
| 32 | `AH.SP.RESERVED.7` | `SasimaParameter_Reserved7` |  |  |  |
| 33 | `AH.SP.RESERVED.8` | `SasimaParameter_Reserved8` |  |  |  |
| 34 | `AH.SP.RESERVED.9` | `SasimaParameter_Reserved9` |  |  |  |
| 35 | `AH.SP.RESERVED.10` | `SasimaParameter_Reserved10` |  |  |  |
| 36 | `AH.SP.RECORD.STATUS` | `SasimaParameter_RecordStatus` | String |  | Status of the record |
| 37 | `AH.SP.CURR.NO` | `SasimaParameter_CurrNo` | String |  | Curr numer of the record |
| 38 | `AH.SP.INPUTTER` | `SasimaParameter_Inputter` |  |  |  |
| 39 | `AH.SP.DATE.TIME` | `SasimaParameter_DateTime` |  |  |  |
| 40 | `AH.SP.AUTHORISER` | `SasimaParameter_Authoriser` | String |  |  |
| 41 | `AH.SP.CO.CODE` | `SasimaParameter_CoCode` | String |  |  |
| 42 | `AH.SP.DEPT.CODE` | `SasimaParameter_DeptCode` | String |  |  |
| 43 | `AH.SP.AUDITOR.CODE` | `SasimaParameter_AuditorCode` | String |  |  |
| 44 | `AH.SP.AUDIT.DATE.TIME` | `SasimaParameter_AuditDateTime` | String |  |  |
