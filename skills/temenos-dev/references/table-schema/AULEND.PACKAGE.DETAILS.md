# AULEND.PACKAGE.DETAILS — Table Schema

> Source: `INSERTS/I_F.AULEND.PACKAGE.DETAILS` in `AULEND_AnnualPackageFee.jar` (positions/aliases via `pipeline/insert_parse.py`); type/mandatory/description via `pipeline/html_parse.py` from JavaDoc HTML.
> Multivalue status is NOT captured here — cross-check `com/temenos/t24/api/records/` per the MV-field-detection rule in `skills/temenos-dev/SKILL.md` before treating any field as single-value.
> Type/mandatory are inferred from JavaDoc free text and may be blank where the HTML gave no clear signal — do not treat a blank as "optional".

| Position | Field Name | Java Alias | Type | Mandatory | Description |
|----------|------------|------------|------|-----------|--------------|
| 1 | `AULEND.PACKAGEDETAILS.LOAN.ID` | `AulendPackageDetails_LoanId` |  |  |  |
| 2 | `AULEND.PACKAGEDETAILS.MASTER.LOAN` | `AulendPackageDetails_MasterLoan` |  |  |  |
| 3 | `AULEND.PACKAGEDETAILS.LOAN.STATUS` | `AulendPackageDetails_LoanStatus` |  |  |  |
| 4 | `AULEND.PACKAGEDETAILS.FEE.INITIAL.DATE` | `AulendPackageDetails_FeeInitialDate` | TField |  | This is the initial date on which the package fee has been charged. This field will be updated with the disbursement date of the master loan. If the loan has multiple disbursements, the first disbursement will be updated as Fee Initial Date. After initial charging of fee, next date of charging will be effective from FEE.INITIAL.DATE and the same will be scheduled based on the frequency defined in Payment Schedule for the Charge payment type. Disbursements in subsequent loans will not be considered for this date as fee will be waived in those loans under the package. This field is associated field of LOAN.ID field. |
| 5 | `AULEND.PACKAGEDETAILS.WAIVE.PACKAGEFEE` | `AulendPackageDetails_WaivePackagefee` | TField |  | This field is to indicate the waiver of Package Fee for entire Loan package. This field will have two values Yes or No. This field will be user inputtable and can be set to Yes or No. If this field is updated as Yes, it indicates that the Package Fee is waived for entire Loan Package by updating fee waiver in Master Loan even though Master Loan field is set as Yes. If this field is updated as No, it indicates that the Package Fee is not waived and will be charged in Master Loan either Capitalized or Due according to option chosen. This field is associated field of LOAN.ID field. |
| 6 | `AULEND.PACKAGEDETAILS.LOCAL.REF` | `AulendPackageDetails_LocalRef` |  |  |  |
| 7 | `AULEND.PACKAGEDETAILS.OVERRIDE` | `AulendPackageDetails_Override` |  |  |  |
| 8 | `AULEND.PACKAGEDETAILS.RECORD.STATUS` | `AulendPackageDetails_RecordStatus` | String |  |  |
| 9 | `AULEND.PACKAGEDETAILS.CURR.NO` | `AulendPackageDetails_CurrNo` | String |  |  |
| 10 | `AULEND.PACKAGEDETAILS.INPUTTER` | `AulendPackageDetails_Inputter` |  |  |  |
| 11 | `AULEND.PACKAGEDETAILS.DATE.TIME` | `AulendPackageDetails_DateTime` |  |  |  |
| 12 | `AULEND.PACKAGEDETAILS.AUTHORISER` | `AulendPackageDetails_Authoriser` | String |  |  |
| 13 | `AULEND.PACKAGEDETAILS.CO.CODE` | `AulendPackageDetails_CoCode` | String |  |  |
| 14 | `AULEND.PACKAGEDETAILS.DEPT.CODE` | `AulendPackageDetails_DeptCode` | String |  |  |
| 15 | `AULEND.PACKAGEDETAILS.AUDITOR.CODE` | `AulendPackageDetails_AuditorCode` | String |  |  |
| 16 | `AULEND.PACKAGEDETAILS.AUDIT.DATE.TIME` | `AulendPackageDetails_AuditDateTime` | String |  |  |
