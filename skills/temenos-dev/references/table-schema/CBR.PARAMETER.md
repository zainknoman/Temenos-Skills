# CBR.PARAMETER — Table Schema

> Source: `INSERTS/I_F.CBR.PARAMETER` in `FINEXT_CBR.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `CBR.DESCRIPTION` | `CbrParameter_Description` |  |  |  |
| 2 | `CBR.CBR.ID.NUMBER` | `CbrParameter_CbrIdNumber` | TField |  | The field should be keyed in with a unique identifier. This unique identifier is to identify each branch, office, or credit central where information is verified |
| 3 | `CBR.REC.DESC.WORD` | `CbrParameter_RecDescWord` | TField |  | The field Contains a value equal to the length of the physical record. example the value should be 426 for fixed length format |
| 4 | `CBR.REC.IDENTIFIER` | `CbrParameter_RecIdentifier` | TField |  | This field identifies the header segment of the file. The value should be defined as HEADER |
| 5 | `CBR.CYCLE.NUMBER` | `CbrParameter_CycleNumber` | TField |  | This field should configured with internal cycle code for reporting. |
| 6 | `CBR.INNOVIS.CODE` | `CbrParameter_InnovisCode` | TField |  | This field holds the Credit agency Innovis Programme identifier |
| 7 | `CBR.EQUIFAX.CODE` | `CbrParameter_EquifaxCode` | TField |  | This field holds the Credit agency Equifax Programme identifier. |
| 8 | `CBR.EXPERIAN.CODE` | `CbrParameter_ExperianCode` | TField |  | This field holds the Credit agency Experian Programme identifier. |
| 9 | `CBR.TRANS.UNION.CODE` | `CbrParameter_TransUnionCode` | TField |  | This field holds the Credit agency Trans Union Programme identifier. |
| 10 | `CBR.PROGRAM.DATE` | `CbrParameter_ProgramDate` | TField |  | Reports the configured date in the header segment in metro 2 file in format MMDDYYYY |
| 11 | `CBR.REPORTER.NAME` | `CbrParameter_ReporterName` | TField |  | Report the name of the company name sending the data. |
| 12 | `CBR.REPORTER.ADDR` | `CbrParameter_ReporterAddr` | TField |  | Report address of the company sending the data. |
| 13 | `CBR.REPORTER.TEL.NO` | `CbrParameter_ReporterTelNo` | TField |  | Reporters telephone number should be mapped in this field. |
| 14 | `CBR.VENDOR.NAME` | `CbrParameter_VendorName` | TField |  | This field should updated with the vendor name and details to update in the header segment. |
| 15 | `CBR.SOFTWARE.VER.NO` | `CbrParameter_SoftwareVerNo` | TField |  | This field should updated with software version name. |
| 16 | `CBR.INNOVIS.PRBC` | `CbrParameter_InnovisPrbc` | TField |  | The field should updated with a unique identification number assigned by this consumer reporting agency. |
| 17 | `CBR.EQUIFAX.PRBC` | `CbrParameter_EquifaxPrbc` | TField |  | The field should updated with a unique identification number assigned by this consumer reporting agency. |
| 18 | `CBR.TRANS.UNION.PRBC` | `CbrParameter_TransUnionPrbc` | TField |  | The field should updated with a unique identification number assigned by this consumer reporting agency. |
| 19 | `CBR.EXPERIAN.PRBC` | `CbrParameter_ExperianPrbc` | TField |  | The field should updated with a unique identification number assigned by this consumer reporting agency. |
| 20 | `CBR.PORTFOLIO.CATEG` | `CbrParameter_PortfolioCateg` |  |  |  |
| 21 | `CBR.PORTFOLIO.TYPE` | `CbrParameter_PortfolioType` |  |  |  |
| 22 | `CBR.ACCT.TYPE.CATEG` | `CbrParameter_AcctTypeCateg` |  |  |  |
| 23 | `CBR.ACOUNT.TYPE` | `CbrParameter_AcountType` |  |  |  |
| 24 | `CBR.RESERVED.1` | `CbrParameter_Reserved1` | TField |  |  |
| 25 | `CBR.RESERVED.2` | `CbrParameter_Reserved2` | TField |  |  |
| 26 | `CBR.RESERVED.3` | `CbrParameter_Reserved3` | TField |  |  |
| 27 | `CBR.JSEGMENT` | `CbrParameter_Jsegment` | TField |  | This field specifies whether the Metro 2 file J1 / J2 segments required for delinquent loans or for all loans. Validation Rules Values should be ALL_DELINQ. |
| 28 | `CBR.PRODUCTS` | `CbrParameter_Products` |  |  |  |
| 29 | `CBR.DELINQ.AMT.LIMIT` | `CbrParameter_DelinqAmtLimit` |  |  |  |
| 30 | `CBR.RESERVED.4` | `CbrParameter_Reserved4` | TField |  |  |
| 31 | `CBR.RESERVED.5` | `CbrParameter_Reserved5` | TField |  |  |
| 32 | `CBR.RESERVED.6` | `CbrParameter_Reserved6` | TField |  |  |
| 33 | `CBR.FROM.DAYS` | `CbrParameter_FromDays` |  |  |  |
| 34 | `CBR.TO.DAYS` | `CbrParameter_ToDays` |  |  |  |
| 35 | `CBR.ACCT.STATUS` | `CbrParameter_AcctStatus` |  |  |  |
| 36 | `CBR.PAYMENT.RATING` | `CbrParameter_PaymentRating` |  |  |  |
| 37 | `CBR.RESERVED.7` | `CbrParameter_Reserved7` | TField |  |  |
| 38 | `CBR.RESERVED.8` | `CbrParameter_Reserved8` | TField |  |  |
| 39 | `CBR.RESERVED.9` | `CbrParameter_Reserved9` | TField |  |  |
| 40 | `CBR.LEGACY.ID.TYPE` | `CbrParameter_LegacyIdType` | TField |  | This should be the alternate id type to get the legacy loan number. |
| 41 | `CBR.CLOSURE.DAYS` | `CbrParameter_ClosureDays` | TField |  | This will hold the number of months after which closed loans will not to be reported. |
| 42 | `CBR.TERM.AMOUNT.CONV` | `CbrParameter_TermAmountConv` | TField |  | This is a conditional field to convert the actual schedule amount is converted as per metro 2 format if its set as YES. |
| 43 | `CBR.RESERVED.10` | `CbrParameter_Reserved10` | TField |  |  |
| 44 | `CBR.RESERVED.11` | `CbrParameter_Reserved11` | TField |  |  |
| 45 | `CBR.RESERVED.12` | `CbrParameter_Reserved12` | TField |  |  |
| 46 | `CBR.RESERVED.13` | `CbrParameter_Reserved13` | TField |  |  |
| 47 | `CBR.RESERVED.14` | `CbrParameter_Reserved14` | TField |  |  |
| 48 | `CBR.RESERVED.15` | `CbrParameter_Reserved15` | TField |  |  |
| 49 | `CBR.RECORD.STATUS` | `CbrParameter_RecordStatus` | String |  |  |
| 50 | `CBR.CURR.NO` | `CbrParameter_CurrNo` | String |  |  |
| 51 | `CBR.INPUTTER` | `CbrParameter_Inputter` |  |  |  |
| 52 | `CBR.DATE.TIME` | `CbrParameter_DateTime` |  |  |  |
| 53 | `CBR.AUTHORISER` | `CbrParameter_Authoriser` | String |  |  |
| 54 | `CBR.CO.CODE` | `CbrParameter_CoCode` | String |  |  |
| 55 | `CBR.DEPT.CODE` | `CbrParameter_DeptCode` | String |  |  |
| 56 | `CBR.AUDITOR.CODE` | `CbrParameter_AuditorCode` | String |  |  |
| 57 | `CBR.AUDIT.DATE.TIME` | `CbrParameter_AuditDateTime` | String |  |  |
