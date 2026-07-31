# UKOIRT.OI.REPORT.PARAMETER — Table Schema

> Source: `INSERTS/I_F.UKOIRT.OI.REPORT.PARAMETER` in `UKOIRT_OtherInterest.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `OI.REORT.PARAMETER.BANK.REF.NUMBER` | `UkoirtOiReportParameter_BankRefNumber` | TField | Yes | The reference number that has to be updated in the OI report should be updated in this field.Mandatory field. |
| 2 | `OI.REORT.PARAMETER.NON.REPORTABLE.SUB.ASSET` | `UkoirtOiReportParameter_NonReportableSubAsset` |  |  |  |
| 3 | `OI.REORT.PARAMETER.NON.REPORTABLE.RELATION.CODE` | `UkoirtOiReportParameter_NonReportableRelationCode` |  |  |  |
| 4 | `OI.REORT.PARAMETER.NON.REPORTABLE.TAX.TYPE` | `UkoirtOiReportParameter_NonReportableTaxType` |  |  |  |
| 5 | `OI.REORT.PARAMETER.EXEMPTED.ACCOUNT` | `UkoirtOiReportParameter_ExemptedAccount` |  |  |  |
| 6 | `OI.REORT.PARAMETER.ALT.SECURITY.ID` | `UkoirtOiReportParameter_AltSecurityId` | TField |  | Alternate Security Id which needs to be used in report should be configured in this field. Vetted from ALT.SEC.PARAMETER. |
| 7 | `OI.REORT.PARAMETER.TAX.YEAR` | `UkoirtOiReportParameter_TaxYear` | TField | Yes | The financial year for which the OI report has to be extracted is configured in this field. 2022 in this field will get the data between 2021 and 2022. This field will be updated before starting extraction of report.Mandatory field. |
| 8 | `OI.REORT.PARAMETER.INDIVIDUAL.CUSTOMER.CLASS` | `UkoirtOiReportParameter_IndividualCustomerClass` | TField | Yes | This field is vetted from ACCOUNT.CLASS table to configure the SECTOR of the customer.Mandatory Field |
| 9 | `OI.REORT.PARAMETER.LOCAL.REF` | `UkoirtOiReportParameter_LocalRef` |  |  |  |
| 10 | `OI.REORT.PARAMETER.RESERVED.5` | `UkoirtOiReportParameter_Reserved5` | TField |  |  |
| 11 | `OI.REORT.PARAMETER.RESERVED.4` | `UkoirtOiReportParameter_Reserved4` | TField |  |  |
| 12 | `OI.REORT.PARAMETER.RESERVED.3` | `UkoirtOiReportParameter_Reserved3` | TField |  |  |
| 13 | `OI.REORT.PARAMETER.RESERVED.2` | `UkoirtOiReportParameter_Reserved2` | TField |  |  |
| 14 | `OI.REORT.PARAMETER.RESERVED.1` | `UkoirtOiReportParameter_Reserved1` | TField |  |  |
| 15 | `OI.REORT.PARAMETER.OVERRIDE` | `UkoirtOiReportParameter_Override` |  |  |  |
| 16 | `OI.REORT.PARAMETER.RECORD.STATUS` | `UkoirtOiReportParameter_RecordStatus` | String |  |  |
| 17 | `OI.REORT.PARAMETER.CURR.NO` | `UkoirtOiReportParameter_CurrNo` | String |  |  |
| 18 | `OI.REORT.PARAMETER.INPUTTER` | `UkoirtOiReportParameter_Inputter` |  |  |  |
| 19 | `OI.REORT.PARAMETER.DATE.TIME` | `UkoirtOiReportParameter_DateTime` |  |  |  |
| 20 | `OI.REORT.PARAMETER.AUTHORISER` | `UkoirtOiReportParameter_Authoriser` | String |  |  |
| 21 | `OI.REORT.PARAMETER.CO.CODE` | `UkoirtOiReportParameter_CoCode` | String |  |  |
| 22 | `OI.REORT.PARAMETER.DEPT.CODE` | `UkoirtOiReportParameter_DeptCode` | String |  |  |
| 23 | `OI.REORT.PARAMETER.AUDITOR.CODE` | `UkoirtOiReportParameter_AuditorCode` | String |  |  |
| 24 | `OI.REORT.PARAMETER.AUDIT.DATE.TIME` | `UkoirtOiReportParameter_AuditDateTime` | String |  |  |
